FROM python:3.10
LABEL authors="florinekieraga"

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["fastapi", "run", "model_backend.py", "--port", "8016"]
