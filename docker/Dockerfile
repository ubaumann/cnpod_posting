FROM python:3.13

WORKDIR /data
ADD . .
RUN pip install --root-user-action=ignore ganglion

EXPOSE 8080

CMD [ "ganglion", "serve" ]
