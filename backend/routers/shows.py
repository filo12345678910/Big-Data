from fastapi.routing import APIRouter
import db.shows as shows
from models import MovieShow
from uuid import UUID

router = APIRouter()


@router.get("/shows/{movie_title}")
def get_shows(movie_title: str):
    return shows.get_show_by_movie(movie_title)


@router.get("/shows/{show_uuid}")
def get_show(show_uuid: UUID):
    return shows.get_show_by_id(show_uuid)


@router.get("/shows/{show_uuid}/seats")
def get_seats(show_uuid: UUID):
    return shows.get_seats_for_show(show_uuid)


@router.post("/shows")
def add_show(show: MovieShow):
    return shows.create_show(show)


@router.delete("/shows/{show_uuid}")
def delete_show(show_uuid: UUID):
    return shows.delete_show(show_uuid)
