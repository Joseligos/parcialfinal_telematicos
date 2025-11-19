FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY webapp/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt || \
    pip install flask gunicorn mysql-connector-python flask-sqlalchemy

COPY webapp /app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]

