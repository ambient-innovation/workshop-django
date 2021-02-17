FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Move pipfiles to project.
ADD Pipfile Pipfile.lock ./

RUN pip install -U pip pipenv

RUN pipenv install --system --deploy

RUN mkdir /src
COPY . /src/
WORKDIR /src

# Run collectstatic for whitenoise
RUN python ./manage.py collectstatic --noinput

# Create empty env-file to avoid warnings
RUN touch ./apps/config/.env

# Set variable for celery
ENV COLUMNS=80

EXPOSE 8000

CMD ["./scripts/run_backend.sh"]
