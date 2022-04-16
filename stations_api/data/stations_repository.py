from typing import Dict, List
from stations_api.data.database_service import DatabaseService
import aiomysql


class StationsRepository:
    def __init__(self, database_service: DatabaseService):
        self._database_service = database_service

    async def get_by_id(self, id: int) -> Dict:
        async with self._database_service.get_cursor() as cursor:
            await cursor.execute("SELECT * FROM stations WHERE id = %s", (id,))
            return await cursor.fetchone()

    async def get_by_name(self, name: str) -> List[Dict]:
        async with self._database_service.get_cursor() as cursor:
            await cursor.execute(
                "SELECT * FROM stations WHERE station_name like %s", (f"{name}%",)
            )
            return await cursor.fetchall()
