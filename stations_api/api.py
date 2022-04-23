from typing import List
from fastapi import FastAPI, Request
from stations_api.data.stations_repository import StationsRepository
from stations_api.models.station import Station
from loguru import logger


class Api:
    def __init__(self, stations_repository: StationsRepository):
        self._stations_repository = stations_repository

    def create_app(self):
        app = FastAPI(docs_url="/api/stations/docs", redoc_url="/api/stations/redoc")

        @app.exception_handler(Exception)
        async def handle_exception(request: Request, exc: Exception):
            logger.exception(f"Exception occurred for request: {request.path_params}")
            return {"error": str(exc)}, 500

        @app.get("/api/stations/status")
        async def status():
            return "Running!"

        @app.get("/api/stations/id/{id}", response_model=Station)
        async def get_station_by_id(id: int):
            logger.info(f"Retrieving station with id: {id}")
            response = await self._stations_repository.get_by_id(id)
            logger.info(f"Received response: {response}")
            return response

        @app.get("/api/stations/name/{name}", response_model=List[Station])
        async def get_stations_by_name(name: str):
            logger.info(f"Received request for stations with name: {name}")
            return await self._stations_repository.get_by_name(name)

        return app
