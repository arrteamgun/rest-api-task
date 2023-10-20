FROM postgres:latest

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=questions

COPY init.sql /docker-entrypoint-initdb.d/