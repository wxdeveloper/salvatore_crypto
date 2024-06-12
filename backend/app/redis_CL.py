from redis.asyncio import Redis as aioredis


class RedisCL:
    def __init__(self) -> None:
        self.url = 'redis://salvatore_crypto-redis-1:6379'
        self._client:aioredis = None
    
    @property
    def client(self):
        return self._client

    async def connect(self):
        self._client = await aioredis.from_url(self.url)

    async def disconnect(self):
        await self._client.close()


redis = RedisCL()