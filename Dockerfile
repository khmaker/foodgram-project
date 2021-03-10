# pull official base image
FROM python:slim

# create directory for the app user
RUN mkdir -p /app

# create the appropriate directories
ENV APP_HOME=/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY requirements.txt $APP_HOME
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY ./foodgram/ $APP_HOME

RUN python manage.py collectstatic --noinput
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000