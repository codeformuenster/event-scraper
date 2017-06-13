FROM python:3.6-alpine

RUN apk --no-cache add libxslt libffi-dev \
  && apk --no-cache add --virtual .build-deps \
    gcc python-dev musl-dev libffi-dev openssl-dev \
    libxml2-dev libxslt-dev \
  && pip install \
    "scrapy~=1.3.3" \
    "geopy~=1.11.0" \
    "ipython~=5.3.0" \
  && apk del .build-deps

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN mkdir /tmp/data

CMD ["scrapy", "crawl", "uni_muenster_termine", "-o", "/tmp/data/uni_muenster_termine.jl"]
