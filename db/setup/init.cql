DROP KEYSPACE IF EXISTS train;

CREATE KEYSPACE IF NOT EXISTS train WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};

USE train;

CREATE TABLE IF NOT EXISTS trains (
    id UUID PRIMARY KEY,
    capacity INT
);

CREATE TABLE IF NOT EXISTS trainss (
    seat_id UUID PRIMARY KEY,
    train_id INT,
    name TEXT
);