from fastapi.routing import APIRouter
import db.movies as movies
from models import Movie

router = APIRouter()


@router.get("/movies")
def get_movies():
    return movies.get_movies()


@router.get("/movies/{movie_title}")
def get_movie(movie_title: str):
    return movies.get_movie_by_title(movie_title)


@router.post("/movies")
def add_movie(movie: Movie):
    return movies.create_movie(movie)


@router.delete("/movies/{movie_title}")
def delete_movie(movie_title: str):
    return movies.delete_movie_by_title(movie_title)
