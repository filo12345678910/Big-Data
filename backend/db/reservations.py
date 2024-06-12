from models import SeatReservation
from db.connection import session

create_reservation = session.prepare(
    query="""INSERT INTO seat_reservations (show_id, seat, user_mail) VALUES (?, ?, ?) IF NOT EXISTS"""
)
create_reservation_by_user = session.prepare(
    "INSERT INTO reservations_by_user (user_mail, show_id, seat) VALUES (?, ?, ?)"
)


def create_reservation_for_show(reservation: SeatReservation):
    # create a reservation for a seat, if successful add it to reservations by user
    session.execute(
        create_reservation,
        [
            reservation.show_uuid,
            reservation.seat,
            reservation.user,
        ],
    )


get_reservation_query = session.prepare(
    "SELECT * FROM seat_reservations WHERE show_id = ?"
)


def get_reservations_for_show(show_uuid):
    rows = session.execute(get_reservation_query, [show_uuid])
    return [SeatReservation(**row._asdict()) for row in rows]
