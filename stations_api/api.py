from typing import List
from fastapi import FastAPI
from stations_api.models.station import Station


class Api:
    def __init__(self):
        pass

    def create_app(self):
        app = FastAPI()

        @app.get("/status")
        async def status():
            return "Running!"

        @app.get("/stations/id/{id}", response_model=Station)
        async def get_station_by_id(id: int):
            return Station()

        @app.get("/stations/name/{name}", response_model=List[Station])
        async def get_stations_by_name(name: str):
            return []

        return app
