from models import Movie
from db.connection import session
from typing import List

get_movies_query = session.prepare("SELECT * FROM movies")
get_movies_by_title_query = session.prepare("SELECT * FROM movies WHERE title = ?")


def get_movies() -> List[Movie]:
    rows = session.execute(get_movies_query).all()
    return [Movie(**row._asdict()) for row in rows]


def get_movie_by_title(title: str) -> Movie | None:
    row = session.execute(get_movies_by_title_query, [title]).one()
    return Movie(**row._asdict()) if row else None


create_movie_query = session.prepare(
    "INSERT INTO movies (title, duration, genres, rating) VALUES (?, ?, ?, ?)"
)


def create_movie(new_movie: Movie):
    session.execute(
        create_movie_query,
        [
            new_movie.title,
            new_movie.duration,
            new_movie.genres,
            new_movie.rating,
        ],
    )


delete_movie_query = session.prepare("DELETE FROM movies WHERE title = ?")


def delete_movie_by_title(title: str):
    session.execute(delete_movie_query, [title])
    return None
