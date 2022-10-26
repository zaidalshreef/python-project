FROM python:3.7.12-buster

COPY . /app

WORKDIR /app


RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "-b", ":8080", "main:app"]