from mc_bench.util.celery import make_worker_celery_app
from mc_bench.util.logging import configure_logging

from .config import settings

configure_logging(humanize=settings.HUMANIZE_LOGS)

app = make_worker_celery_app(
    conf=dict(
        worker_prefetch_multiplier=4,
    )
)
