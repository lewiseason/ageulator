# ageulator

Tells you how old you are, in days.

## Usage

Python & Flask CLI:

```shell
FLASK_APP=ageulator/ageulator.py BIRTHDAY=1992-12-21 flask run
```

Docker:

```shell
docker run -p 8000:8000 -e BIRTHDAY=1992-12-21 lewiseason/ageulator
```

Docker & `nginx-proxy`:

```shell
docker run -e VIRTUAL_HOST=ageulator.lewiseason.co.uk -e BIRTHDAY=1992-12-21 lewiseason/ageulator
```

## Dependencies

[flask] is BSD licensed, [bulma] is MIT licensed.

[bulma]: https://bulma.io/
[flask]: http://flask.pocoo.org/

## Packaging

```shell
docker build -t ageulator .
docker tag ageulator lewiseason/ageulator:latest
docker push lewiseason/ageulator:latest
```
