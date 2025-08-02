FROM python:3.13

WORKDIR /data
ADD . .
RUN mkdir -p db
RUN mkdir -p .keys
RUN pip install --root-user-action=ignore ganglion cryptography

EXPOSE 8080

CMD [ "ganglion", "serve", "--config", "ganglion-local.toml" ]
