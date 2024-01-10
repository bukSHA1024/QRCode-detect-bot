FROM --platform=linux/amd64 python:3.12

RUN apt update && apt -y install libzbar0

WORKDIR /bot

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src .
ENTRYPOINT python /bot/main.py
