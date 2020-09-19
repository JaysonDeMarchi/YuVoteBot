FROM python:rc-alpine

WORKDIR /usr/src/app/

RUN pip install \
    bs4 \
    prompt_toolkit \
    requests

COPY . .

CMD [ "tail", "-f", "/dev/null" ]
