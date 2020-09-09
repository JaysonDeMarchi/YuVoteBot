FROM python:rc-alpine

WORKDIR /user/src/app/

RUN pip install requests

COPY . .

CMD [ "tail", "-f", "/dev/null" ]
