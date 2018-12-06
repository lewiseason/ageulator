FROM python:3.6-alpine
WORKDIR /usr/src/app

COPY . ./
RUN pip install --no-cache-dir gunicorn flask
CMD [ "gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "ageulator.ageulator:app" ]

