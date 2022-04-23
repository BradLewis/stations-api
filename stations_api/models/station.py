from typing import Optional
from fastapi_camelcase import CamelModel


class Station(CamelModel):
    id: int
    station_id: int
    station_name: str
    province: str
    climate_id: str
    latitude: Optional[float]
    longitude: Optional[float]
    elevation: Optional[int]
    first_year: int
    last_year: int
