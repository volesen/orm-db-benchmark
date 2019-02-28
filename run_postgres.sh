docker run \
    -e POSTGRES_USER=root \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=test \
    -p 5432:5432 \
    postgres
