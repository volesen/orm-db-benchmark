FROM mongo:3.4.19-jessie

COPY dump/ /tmp/dump/

CMD mongod --fork --logpath /var/log/mongodb.log; \
    mongorestore --gzip /tmp/dump/; \
    mongod --shutdown; \
    docker-entrypoint.sh mongod
