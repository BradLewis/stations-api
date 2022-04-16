from typing import List
from fastapi import FastAPI
from stations_api.data.stations_repository import StationsRepository
from stations_api.models.station import Station


class Api:
    def __init__(self, stations_repository: StationsRepository):
        self._stations_repository = stations_repository

    def create_app(self):
        app = FastAPI()

        @app.get("/api/status")
        async def status():
            return "Running!"

        @app.get("/api/stations/id/{id}", response_model=Station)
        async def get_station_by_id(id: int):
            print(f"Retrieving station with id: {id}")
            return await self._stations_repository.get_by_id(id)

        @app.get("/api/stations/name/{name}", response_model=List[Station])
        async def get_stations_by_name(name: str):
            print(f"Received request for stations with name: {name}")
            return await self._stations_repository.get_by_name(name)

        return app
