from connection import session
import service
service.start(session)
while 1:
    print("""
0 - show entire database
1 - make a reservation
2 - update a reservation
3 - see reservation by name
4 - see reservation by seat and train id
          """)
    x = input()
    if x == '0':
        service.query_data(session, 'trains')
        service.query_data(session, 'trainss')
    if x == '1':
        print("Provide a train id and a name")
        y = input()
        if len(y.split()) != 2:
            print("Invalid Input")
        else:
            service.input_1(session, int(y.split()[0]), y.split()[1])
    if x == '2':
        print("Provide an old name, and a new name to update")
        y = input()
        if len(y.split()) != 2:
            print("Invalid Input")
        else:
            service.input_2(session, y.split()[0], y.split()[1])
    if x == '3':
        print("Provide a name")
        y = input()
        if len(y.split()) != 1:
            print("Invalid Input")
        else:
            service.input_3(session, y.split()[0])
    if x == '4':
        print("Provide a train and seat number")
        y = input()
        if len(y.split()) != 2:
            print("Invalid Input")
        else:
            service.input_4(session, y.split()[0], y.split()[1])
    else:
        print("Invalid Input")