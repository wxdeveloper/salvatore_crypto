import aioredis

from aioredis import Redis


class RedisCL:
    def __init__(self) -> None:
        self.url = 'redis'
        self._client:Redis = None
    
    async def connect(self):
        self._client = await aioredis.from_url(self.url)

    async def disconnect(self):
        await self._client.close()

    @property
    def client(self) -> Redis:
        return self._client