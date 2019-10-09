FROM python:3.7-alpine

ENV TZ Asia/Hong_Kong

RUN apk add --no-cache --virtual .build-deps \
        build-base \
        tzdata \
		gcc \
		libc-dev \
		bash \
		linux-headers  && \
 pip install uwsgi

WORKDIR /source

COPY ./requirements.txt requirements.txt

RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r  requirements.txt

EXPOSE 5000

VOLUME ["/data"]

ADD . /source

ENTRYPOINT ["uwsgi"]

CMD ["--ini", "uwsgi.ini"]
