FROM python:3.6-alpine
RUN pip install \
  "elasticsearch~=5.1.0" \
  "certifi~=2017.1.23"

COPY . /scripts
VOLUME /data
