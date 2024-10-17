FROM python:3.10
LABEL authors="florinekieraga"

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /app

CMD ["fastapi", "run", "app/model_backend.py", "--port", "80"]
