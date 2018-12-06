FROM python:3.6-alpine
LABEL maintainer=me@lewiseason.co.uk

WORKDIR /usr/src/app
EXPOSE 8000/tcp

COPY . ./
RUN pip install --no-cache-dir gunicorn flask
CMD [ "gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "ageulator.ageulator:app" ]
