import os


class Settings:
    INTERNAL_OBJECT_BUCKET = os.environ["INTERNAL_OBJECT_BUCKET"]
    EXTERNAL_OBJECT_BUCKET = os.environ["EXTERNAL_OBJECT_BUCKET"]
    FAST_RENDER = os.environ.get("FAST_RENDER") == "true"
    HUMANIZE_LOGS = os.environ.get("HUMANIZE_LOGS") == "true"
    
    # Rendering optimization settings
    MATERIAL_BATCH_SIZE = int(os.environ.get("MATERIAL_BATCH_SIZE", "20"))
    TEXTURE_ATLAS_ENABLED = os.environ.get("TEXTURE_ATLAS_ENABLED", "false") == "true"
    MESH_MERGE_THRESHOLD = int(os.environ.get("MESH_MERGE_THRESHOLD", "100"))
    COMPRESSION_LEVEL = int(os.environ.get("COMPRESSION_LEVEL", "5"))  # 1-10, higher = more compression but slower
    RENDER_SAMPLES = int(os.environ.get("RENDER_SAMPLES", "8"))  # Lower = faster


settings = Settings()
