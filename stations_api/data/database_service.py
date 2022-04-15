from contextlib import asynccontextmanager
from aiomysql import Connection
import aiomysql


class DatabaseService:
    def __init__(self):
        self._pool = None
        self._config = None

    @asynccontextmanager
    async def get_connection(self) -> Connection:
        if self._pool is None:
            self._pool = await aiomysql.create_pool(**self._config)

        async with self._pool.acquire() as conn:
            yield conn
