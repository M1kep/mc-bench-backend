import json
import os
import tempfile

from mc_bench.minecraft.biome_lookup import BiomeLookup
from mc_bench.minecraft.rendering import Renderer, TimeOfDay
from mc_bench.minecraft.resources import ResourceLoader
from mc_bench.minecraft.schematic import load_schematic, to_minecraft_world
from mc_bench.models.run import Artifact, RenderingSample
from mc_bench.util.object_store import get_client as get_object_store_client
from mc_bench.worker.run_stage import StageContext, run_stage_task

from ..app import app
from ..config import settings


@run_stage_task(
    name="run.render_sample",
    app=app,
    max_retries=0,
    stage=RenderingSample,
    retry_on_failure=False,
    restart_run_on_failure=False,
)
def render_sample(stage_context: StageContext):
    resource_loader = ResourceLoader(
        version=stage_context.run.template.minecraft_version,
    )

    schematic_artifact = stage_context.sample.get_schematic_artifact()
    command_list_artifact = stage_context.sample.get_command_list_artifact()
    summary_artifact = stage_context.sample.get_build_summary_artifact()

    command_list = json.loads(
        command_list_artifact.download_artifact().getvalue().decode("utf-8")
    )
    summary = json.loads(
        summary_artifact.download_artifact().getvalue().decode("utf-8")
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        schematic_filepath = os.path.join(temp_dir, "build.schem")

        rendered_model_glb_filepath = os.path.join(temp_dir, "build-rendered-model.glb")

        with open(schematic_filepath, "wb") as f:
            f.write(schematic_artifact.download_artifact().getvalue())

        biome_fills = []
        for command in command_list:
            if command["kind"] == "fill" and command["command"].startswith(
                "/fillbiome"
            ):
                biome_fills.append(command)

        biome_lookup = BiomeLookup(
            biome_data=biome_fills, bounding_box=summary["boundingBox"]
        )

        loaded_schematic = load_schematic(schematic_filepath, biome_lookup)
        minecraft_world = to_minecraft_world(loaded_schematic, resource_loader)
        placed_blocks = minecraft_world.to_blender_blocks()

        renderer = Renderer()
        renderer.render_blocks(
            placed_blocks=placed_blocks,
            types=["glb"],
            time_of_day=TimeOfDay.NOON,
            pre_export=False,
            name=rendered_model_glb_filepath,
            fast_render=settings.FAST_RENDER,
        )

        object_client = get_object_store_client()

        render_artifact_spec = stage_context.sample.render_artifact_spec(
            stage_context.db
        )
        for key in ["rendered_model_glb"]:
            object_client.fput_object(
                bucket_name=settings.INTERNAL_OBJECT_BUCKET,
                object_name=render_artifact_spec[key]["object_prototype"]
                .materialize(**render_artifact_spec[key]["object_parts"])
                .get_path(),
                file_path=rendered_model_glb_filepath,
            )

        for key, spec in render_artifact_spec.items():
            artifact = Artifact(
                kind=spec["artifact_kind"],
                run_id=stage_context.run.id,
                sample_id=stage_context.sample.id,
                bucket=settings.INTERNAL_OBJECT_BUCKET,
                key=spec["object_prototype"]
                .materialize(**spec["object_parts"])
                .get_path(),
            )
            stage_context.db.add(artifact)
        stage_context.db.commit()

    run_id = stage_context.run_id
    sample_id = stage_context.sample.id

    return run_id, sample_id
