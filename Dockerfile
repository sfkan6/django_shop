# The base image we want to inherit from
FROM python:3.10-slim

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  POETRY_VERSION=1.0.3 \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

# set work directory
WORKDIR /code
COPY pyproject.toml poetry.lock /code/

RUN pip install "poetry==$POETRY_VERSION" \
&& poetry config virtualenvs.create false \
&& poetry install --no-interaction --no-ansi

# copy project
COPY . /code/

RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]

#CMD ["python", "django_shop/manage.py", "runserver", "0.0.0.0:8000"]
