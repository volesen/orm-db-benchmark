FROM postgres:11.2

# Set enviroment variables

ENV POSTGRES_USER=root

ENV POSTGRES_PASSWORD=password

ENV POSTGRES_DB=test

COPY dump.sql /dump.sql

# psql test < dump.sql