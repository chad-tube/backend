FROM python:3.11.4-slim-bullseye

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system deps
RUN apt-get update

# Install deps
RUN pip install --upgrade pip

COPY ./requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app
RUN chmod +x entrypoints/runserver.sh

ENTRYPOINT [ "bash", "entrypoints/runserver.sh" ]
