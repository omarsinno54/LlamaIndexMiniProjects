FROM python:3.8-slim

COPY . /app
COPY ../requirements.txt /app/requirements.txt

WORKDIR /app/scripts/

RUN pip install --no-cache-dir requirements.txt

CMD ["python3", "retrieval.py"]