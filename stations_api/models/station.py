from pydantic import BaseModel


class Station(BaseModel):
    id: int
    station_id: int
    station_name: str
    province: str
    climate_id: str
    latitude: float
    longitude: float
    elevation: int
    first_year: int
    last_year: int
