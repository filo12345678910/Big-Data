import uuid
import random

def insert_data_trains(session, a, b):
    session.execute("""
    INSERT INTO trains (id, capacity)
    VALUES (%s, %s)
    """, (a, b))

def insert_data_trainss(session, a, b, c):
    session.execute("""
    INSERT INTO trainss (seat_id, train_id, name)
    VALUES (%s, %s, %s)
    """, (a, b, c))

def query_data(session, table):
    result = session.execute("SELECT * FROM " + table)
    for row in result:
        print(row)

def clear_table(session, table_name):
    session.execute(f"TRUNCATE {table_name}")

def start(session):
    clear_table(session, 'trains')
    clear_table(session, 'trainss')

    for i in range(10):
        capacity = random.randint(20, 40)
        insert_data_trains(session, i, capacity)
        for j in range(capacity):
            insert_data_trainss(session, j, i, 'none')

    query_data(session, 'trains')
    query_data(session, 'trainss')