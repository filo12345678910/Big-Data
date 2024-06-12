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

    for i in range(2):
        capacity = random.randint(20, 40)
        insert_data_trains(session, i, capacity)
        for j in range(capacity):
            insert_data_trainss(session, j, i, 'none')

def input_1(session, train_id, name):
    result = session.execute("SELECT * FROM trains WHERE id = %s", (train_id, ))
    if not result.one():
        print("There is no train with this id")
        return 0
    if result[0][1] == 0:
        print("There are no more seats left on this train")
        return 0
    session.execute("""UPDATE trains SET capacity = %s WHERE id = %s""", (result[0][1] - 1, train_id))
    result_2 = session.execute("SELECT * FROM trainss WHERE train_id = %s AND name = 'none' ALLOW FILTERING", (train_id,))
    session.execute("""UPDATE trainss SET name = %s
    WHERE seat_id = %s AND train_id = %s""", (name, result_2[0][0], train_id))
    print(f'You have succesfully reserved seat number: {result_2[0][0]}')
    return 1

def input_2(session, old_name, new_name):
    result = session.execute("SELECT * FROM trainss WHERE name = %s ALLOW FILTERING", (old_name, ))
    if not result.one():
        print("There is no reservation with this name")
        return 0
    row = result.one()
    seat_id, train_id = row.seat_id, row.train_id
    session.execute("""UPDATE trainss SET name = %s 
    WHERE seat_id = %s AND train_id = %s""", (new_name, seat_id, train_id))
    print(f'You have succesfully changed a name from: {old_name} to {new_name}')
    return 1

def input_3(session, name):
    result = session.execute("SELECT * FROM trainss WHERE name = %s ALLOW FILTERING", (name, ))
    if not result.one():
        print("There is no reservation with this name")
        return 0
    row = result.one()
    seat_id, train_id = row.seat_id, row.train_id
    print(f"The reservation on the name: {name}, has train number: {train_id} and seat number: {seat_id}")
    return 1

def input_4(session, train_id, seat_id):
    result = session.execute("""SELECT * FROM trainss 
    WHERE seat_id = %s AND train_id = %s ALLOW FILTERING""", (seat_id, train_id))
    if not result.one():
        print("There is no seat with these numbers")
        return 0
    row = result.one()
    name = row.name
    if name == 'none':
        print("This seat is not reserved")
        return 0
    print(f"The reservation on the name: {name}, has train number: {train_id} and seat number: {seat_id}")
    return 1