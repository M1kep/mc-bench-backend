FROM python:3.12.7

COPY deps/requirements.txt requirements.txt
COPY deps/worker-requirements.txt worker-requirements.txt
RUN pip install -r requirements.txt -r worker-requirements.txt

COPY . /usr/lib/mc-bench-backend
RUN pip install /usr/lib/mc-bench-backend[worker]


CMD ["celery", "-A", "mc_bench.apps.admin_worker", "worker", "-Q", "admin"]
