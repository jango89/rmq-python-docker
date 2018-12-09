FROM python:2.7-alpine

RUN pip install pika

#Python print enabled
ENV PYTHONUNBUFFERED=1

# Actually install the application
WORKDIR /usr/src/app

COPY consumer.py .
COPY send_email.py .

CMD ["python", "/usr/src/app/consumer.py"]