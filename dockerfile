FROM python:3.10-buster

COPY . /app

WORKDIR /app


RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["gunicorn", "-b", ":8080", "app:app"]