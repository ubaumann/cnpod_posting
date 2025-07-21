# Computer Network Basic Repo for Posting services

The idea is to serve a pod for each switch int the computer networking module to use RESTconf calls

- http://<server>/pod-1/sw01
- http://<server>/pod-1/sw02
- ...

The `docker compose` demonstrates the PoC with the server and 2 switches. K8s deployment is following asap.

Create your own `.env` based on `.env-example` and set the username password.
