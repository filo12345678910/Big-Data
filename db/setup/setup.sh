#! /bin/bash

CASSANDRA_HOST=${CASSANDRA_HOST:-cassandra-master}
CASSANDRA_PORT=${CASSANDRA_PORT:-9042}
SCRIPTS_DIR=${SCRIPTS_DIR:-/scripts}

#alias cqlsh="cqlsh $CASSANDRA_HOST $CASSANDRA_PORT --cqlversion=$CQLVERSION"
# Function to check if Cassandra is up
function check_cassandra {
    echo ""
    cqlsh $CASSANDRA_HOST $CASSANDRA_PORT --cqlversion=$CQLVERSION -e "DESC KEYSPACES;"
    return $?
}

# Wait until Cassandra is available
echo "Waiting for Cassandra to be available at $CASSANDRA_HOST:$CASSANDRA_PORT..."
until check_cassandra; do
    echo "Cassandra is not available under $CASSANDRA_HOST:$CASSANDRA_PORT with version $CQLVERSION. Retrying in 5 seconds..."
    sleep 5
done

echo "Cassandra is up and running!"

# Execute all CQL scripts in the specified directory
for script in $SCRIPTS_DIR/*.cql; do
    echo "Executing $script..."
    cqlsh $CASSANDRA_HOST $CASSANDRA_PORT --cqlversion=$CQLVERSION -f $script
    if [ $? -ne 0 ]; then
        echo "Failed to execute $script"
        exit 1
    fi
done

echo "All scripts executed successfully!"
