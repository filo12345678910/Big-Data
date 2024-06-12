DROP KEYSPACE IF EXISTS train;

CREATE KEYSPACE IF NOT EXISTS train WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
};

USE train;

CREATE TABLE IF NOT EXISTS trains (
    id INT PRIMARY KEY,
    capacity INT
);

CREATE TABLE IF NOT EXISTS trainss (
    seat_id INT,
    train_id INT,
    name TEXT,
    PRIMARY KEY (seat_id, train_id)
);