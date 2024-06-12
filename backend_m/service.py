from connection import session
import uuid

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

clear_table(session, 'trains')
clear_table(session, 'trainss')

insert_data_trains(session, uuid.uuid4(), 43)
insert_data_trainss(session, uuid.uuid4(), 1, 'sda')

clear_table(session, 'trains')
clear_table(session, 'trainss')

