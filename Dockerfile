FROM python:3.8-slim-buster

WORKDIR /romano_web_api/app

RUN apt-get update && \
  apt-get install -y \
  git

RUN pip install \
  pylint \
  pylint-flask \
  pytest \
  pytest-cov

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "app.py"]