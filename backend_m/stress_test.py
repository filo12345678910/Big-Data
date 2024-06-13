import concurrent.futures
import random
import time
import service

def stress_test_1(session):
    start_time = time.time()

    def make_request():
        session.execute("SELECT * FROM trains WHERE id = %s", (0,))

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(make_request) for _ in range(10000)]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    print(f"Stress Test 1 completed in {time.time() - start_time} seconds")

def stress_test_2(session):
    start_time = time.time()

    def make_request():
        if random.choice([True, False]):
            session.execute("SELECT * FROM trains WHERE id = %s", (0,))
        else:
            service.input_1(session, 0, 'test')

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(make_request) for _ in range(10000)]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    print(f"Stress Test 2 completed in {time.time() - start_time} seconds")

def stress_test_3(session):
    start_time = time.time()

    def make_reservation(client_id):
        for seat_id in range(40):
            service.input_1(session, 1, str(client_id))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(make_reservation, client_id) for client_id in range(2)]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    print(f"Stress Test 3 completed in {time.time() - start_time} seconds")