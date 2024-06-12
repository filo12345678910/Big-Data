_yippee_

## How to setup database

1. Go to db folder
2. Run `docker-compose up -d`
3. Run `docker logs cqlsh-setup -f` to see when the setup scripts for a database are done
4. If you want to change the scripts for seeding database, you can add them to any file in db/setup/ folder ended in .cql
5. You can connect to the database with default credentials: `cqlsh -u cassandra -p cassandra`
