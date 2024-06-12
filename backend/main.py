from fastapi import FastAPI
from routers import movies, shows, reservations

app = FastAPI()

app.include_router(shows.router)
app.include_router(movies.router)
app.include_router(reservations.router)
