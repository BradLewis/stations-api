from pydantic import BaseModel
import datetime as dt


class Station(BaseModel):
    id: int
    station_id: int
    station_name: str
    province: str
    climate_id: str
    latitude: float
    longitude: float
    elevation: int
    first_year: dt.date
    last_year: dt.date
