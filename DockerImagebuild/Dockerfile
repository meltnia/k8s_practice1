FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential nfs-common \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /python

RUN pip install --no-cache-dir Flask
RUN pip install --no-cache-dir gunicorn

COPY flask-server.py .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "flask-server:app"]