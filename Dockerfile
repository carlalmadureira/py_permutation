FROM python:3.7-alpine

RUN pip install --upgrade pip

RUN apk add --virtual .build-dependencies \
    --no-cache \
    python3-dev \
    build-base \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    pcre-dev

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN apk add --no-cache pcre

WORKDIR /permutation
ADD ./permutation .

ADD ./requirements.txt .
RUN pip install -r requirements.txt

RUN rm -rf /var/cache/apk/*

CMD ["sh", "run.sh"]