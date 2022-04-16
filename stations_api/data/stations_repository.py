from typing import Dict, List
from stations_api.data.database_service import DatabaseService


class StationsRepository:
    def __init__(self, database_service: DatabaseService):
        self._database_service = database_service

    async def get_by_id(self, id: int) -> Dict:
        async with self._database_service.get_connection() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute("SELECT * FROM stations WHERE id = %s", (id,))
                return await cursor.fetchone()

    async def get_by_name(self, name: str) -> List[Dict]:
        async with self._database_service.get_connection() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(
                    "SELECT * FROM stations WHERE name like '%s'", (name,)
                )
                return await cursor.fetchall()
