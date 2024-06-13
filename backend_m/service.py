import uuid
import random
import time

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
    result = session.execute("SELECT * FROM trains WHERE id = %s", (train_id,))
    train = result.one()
    if not train:
        print("There is no train with this id")
        return 0
    if train.capacity == 0:
        print("There are no more seats left on this train")
        return 0
    
    capacity_update = session.execute("""
        UPDATE trains SET capacity = %s 
        WHERE id = %s IF capacity = %s
        """, (train.capacity - 1, train_id, train.capacity))
    
    if not capacity_update.was_applied:
        print("Failed to decrement capacity, possibly due to race condition")
        return 0

    result_2 = session.execute("SELECT * FROM trainss WHERE train_id = %s AND name = 'none' ALLOW FILTERING", (train_id,))
    available_seat = result_2.one()
    if not available_seat:
        print("No available seats found")
        return 0
    
    seat_update = session.execute("""
        UPDATE trainss SET name = %s 
        WHERE seat_id = %s AND train_id = %s IF name = 'none'
        """, (name, available_seat.seat_id, train_id))
    
    if seat_update.was_applied:
        print(f'You have successfully reserved seat number: {available_seat.seat_id}')
        return 1
    else:
        session.execute("UPDATE trains SET capacity = %s WHERE id = %s", (train.capacity, train_id))
        print("Failed to reserve the seat, rolled back capacity change")
        return 0

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