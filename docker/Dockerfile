FROM python:3.13

WORKDIR /data
ADD . .
RUN pip install --root-user-action=ignore ganglion

CMD [ "ganglion", "serve" ]
