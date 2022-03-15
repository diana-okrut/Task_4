FROM python:3.10.0-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init --create-home -r -u 1000 -g ${APP_USER} ${APP_USER}

WORKDIR /online_course
COPY . .
RUN pip install -r  requirements.txt

#ENTRYPOINT []
#
#CMD []
