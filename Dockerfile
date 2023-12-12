FROM python:3.8

WORKDIR /code

COPY ./app /code/app
COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME coolenv