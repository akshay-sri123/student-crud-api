FROM python:3.8-slim-buster

ARG DB_USERNAME
ARG DB_PASSWORD
ENV DB_USERNAME=$DB_USERNAME
ENV DB_PASSWORD=$DB_PASSWORD
ENV FLASK_APP=app/app.py

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

RUN chmod +x /app/docker-entrypoint.sh

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
ENTRYPOINT ["/app/docker-entrypoint.sh"]
