# demo
FROM alpine:3.6

ENV AUTHOR "teachmyself@126.com"

ADD . /demo

RUN set -xue; \
    apk update && apk add \
        py2-pip
        && \
    pip install pip --upgrade && \
    pip install requirements.txt && \
    rm -rf /var/cache/apk/* ~/.cache /usr/share/man

CMD ["python", "-m", "SimpleHTTPServer"]
