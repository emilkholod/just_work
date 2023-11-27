FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_HOME=/home/app
ENV PATH=$APP_HOME/.local/bin:$PATH

RUN apt-get update && apt-get install -y netcat-traditional

RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app
USER app:app

COPY ./requirements.txt /
RUN pip install --user -r requirements.txt

COPY --chown=app:app /docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

COPY ./mysite /mysite
WORKDIR /mysite
