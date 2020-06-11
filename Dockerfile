FROM python:3.7

# Ensure logging is up to date, don't buffer log messages
ENV PYTHONUNBUFFERED 1

# Base uWSGI configuration
ENV UWSGI_MASTER=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy
# Num processes & threads per process
ENV UWSGI_PROCESSES=2 UWSGI_THREADS=2
# Http traffic port
EXPOSE 8000
ENV UWSGI_HTTP=:8000
# Django wsgi entrypoint
ENV UWSGI_WSGI_FILE=config/wsgi.py

# Set workdir in docker fs
WORKDIR /opt/app

# Move requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install uwsgi

# Move other sourcefiles
COPY . .

CMD ["uwsgi", "--show-config"]
