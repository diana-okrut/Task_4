FROM python:3.10.0-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init --create-home -r -u 1000 -g ${APP_USER} ${APP_USER}

ARG APP_DIR=/home/${APP_USER}/project/
RUN mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}
WORKDIR ${APP_DIR}

RUN pip install --upgrade pip

COPY requirements.txt ${APP_DIR}
RUN pip install -r  requirements.txt

COPY --chown=${APP_USER}:${APP_USER} . ${APP_DIR}

USER ${APP_USER}:${APP_USER}

ENTRYPOINT ['/bin/bash', '-c']
