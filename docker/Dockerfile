FROM python:3.13

WORKDIR /data
ADD . .
RUN mkdir -p db
RUN mkdir -p .keys
RUN pip install --root-user-action=ignore ganglion cryptography

EXPOSE 8080
ENV PUBLIC_URL=127.0.0.1:8080
ENV HTTP_PROTOCOL=http
ENV WS_PROTOCOL=ws

CMD [ "ganglion", "serve", "--config", "ganglion-local.toml" ]
