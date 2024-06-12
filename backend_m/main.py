from connection import session
import service
service.start(session)
while 1:
    input()