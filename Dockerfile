FROM python:3.10-slim-buster
ENV DONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /srv

ENV debian_frontend noninteractive

RUN apt-get update -y ;\
    apt install -y \
    build-essential \
    libmemcached-dev \
    zlib1g-dev \
    gcc g++ \
    inetutils-ping \
    netcat

ADD requirements.txt .
RUN pip install -r ./requirements.txt

CMD while ! python3 manage.py sqlflush > /dev/null 2>&1 ; do sleep 1 ; done && \
    python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --mobile_number 09121234567 --noinput; \
    gunicorn -b 0.0.0.0:8000 backend.wsgi