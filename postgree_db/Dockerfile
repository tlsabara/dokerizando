FROM postgres:11
MAINTAINER "tlsabara"

ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV DEF_FOLDER=/docker-entrypoint-initdb.d/

COPY ./ $DEF_FOLDER

EXPOSE 5432
