FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /python

RUN pip install --no-cache-dir Flask
RUN pip install --no-cache-dir gunicorn
RUN mkdir /flask_download
COPY trash* /flask_download/

COPY flask-server.py .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "flask-server:app"]