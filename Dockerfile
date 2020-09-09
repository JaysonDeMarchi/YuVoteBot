FROM python:rc-alpine

WORKDIR /usr/src/app/

RUN pip install requests

COPY . .

CMD [ "tail", "-f", "/dev/null" ]
