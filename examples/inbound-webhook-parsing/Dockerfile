FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "-u", "app.py"]
