from datetime import datetime
from db.connection import session
from models import MovieShow, Seat
from db.rooms import get_room_by_name
import uuid

get_shows_by_movie_title_query = session.prepare(
    "SELECT * FROM movie_shows_by_movie WHERE movie_title = ? AND show_time > ?"
)
get_show_by_id_query = session.prepare(
    "SELECT * FROM movie_shows_by_id WHERE show_id = ?"
)


def get_show_by_movie(movie_title: str, show_time: datetime | None = datetime.now()):
    rows = session.execute(
        get_shows_by_movie_title_query, [movie_title, show_time]
    ).all()
    return [
        MovieShow(
            uuid=row.uuid,
            movie=row.movie_title,
            room=row.room_name,
            show_time=row.show_time,
        )
        for row in rows
    ]


def get_show_by_id(show_uuid):
    row = session.execute(get_show_by_id_query, [show_uuid]).one()
    return MovieShow(
        uuid=row.uuid,
        movie=row.movie_title,
        room=row.room_name,
        show_time=row.show_time,
    )


get_seats_by_show = session.prepare("SELECT * FROM seats_by_show WHERE show_id = ?")


def get_seats_for_show(show_uuid):
    rows = session.execute(get_seats_by_show, [show_uuid])
    return [Seat(**row._asdict()) for row in rows]


create_show_by_id = session.prepare(
    "INSERT INTO movie_shows_by_id (show_id, movie_title, room_name, show_time) VALUES (?, ?, ?, ?)"
)
create_show_by_movie = session.prepare(
    "INSERT INTO movie_shows_by_movie (show_id, movie_title, room_name, show_time) VALUES (?, ?, ?, ?)"
)
create_seat = session.prepare("INSERT INTO seats_by_show (show_id, seat) VALUES (?, ?)")


def create_show(show: MovieShow):
    new_show_id = uuid.uuid4()
    room = get_room_by_name(show.room)
    session.execute(
        create_show_by_id,
        [
            new_show_id,
            show.movie,
            show.room,
            show.show_time,
        ],
    )
    session.execute(
        create_show_by_movie,
        [
            new_show_id,
            show.movie,
            show.room,
            show.show_time,
        ],
    )
    for seat in room.seats:
        session.execute(
            create_seat,
            [new_show_id, seat],
        )


delete_show_by_id = session.prepare("DELETE FROM movie_shows_by_id WHERE show_id = ?")
delete_show_by_movie_id = session.prepare(
    "DELETE FROM movie_shows_by_movie WHERE movie_title = ? AND show_time = ? AND room_name = ?"
)


def delete_show(show_uuid):
    show = get_show_by_id(show_uuid)
    session.execute(delete_show_by_id, [show_uuid])
    session.execute(delete_show_by_movie_id, [show.movie, show.show_time, show.room])
