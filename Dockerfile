# The base image we want to inherit from
FROM python:3.10-slim

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  POETRY_VERSION=1.0.3 \
  POETRY_CACHE_DIR='/var/cache/pypoetry'


# copy project and set work directory
COPY . /code/
WORKDIR /code

# Install requirements
RUN pip install "poetry==$POETRY_VERSION" \
&& poetry config virtualenvs.create false \
&& poetry install --no-interaction --no-ansi


RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]

#CMD ["python", "django_shop/manage.py", "runserver", "0.0.0.0:8000"]
