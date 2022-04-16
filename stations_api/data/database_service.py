from contextlib import asynccontextmanager
from aiomysql import Connection
import aiomysql

from stations_api.configuration import Configuration


class DatabaseService:
    def __init__(self, config: Configuration):
        self._pool = None
        self._config = config

    @asynccontextmanager
    async def get_connection(self) -> Connection:
        if self._pool is None:
            self._pool = await aiomysql.create_pool(
                host=self._config.database_creds.host,
                user=self._config.database_creds.username,
                password=self._config.database_creds.password,
                db=self._config.database_creds.database,
            )

        async with self._pool.acquire() as conn:
            yield conn
