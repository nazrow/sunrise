FROM python:3.10-slim
WORKDIR /build
COPY ./requirements.txt .
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y curl gcc git && \
    pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
WORKDIR /app
CMD python main.py