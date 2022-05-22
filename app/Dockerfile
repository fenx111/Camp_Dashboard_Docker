FROM python:3.9.7-slim
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . .
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
	&& pip install --upgrade pip \
	&& pip install -r requirements.txt