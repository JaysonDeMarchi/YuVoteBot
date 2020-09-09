FROM python:rc-alpine

WORKDIR /usr/src/app/

RUN pip install \
    bs4 \
    requests

COPY . .

CMD [ "tail", "-f", "/dev/null" ]
