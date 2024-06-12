from fastapi import Depends
from aioredis import Redis

from repositories import CryptoRepository
from services import CryptoService
from models import Storage, CryptoLink
from redis_CL import RedisCL


async def get_storage() -> Storage:
    return Storage()

async def get_crypto_link() -> CryptoLink:
    return CryptoLink()

async def get_redisCL(
    redis: RedisCL
) -> Redis:
    return redis.client

async def get_crypto_repository(
    link: CryptoLink = Depends(get_crypto_link), 
    storage: Storage = Depends(get_storage),
    redis: RedisCL = Depends(get_redisCL)
) -> CryptoRepository:
    return CryptoRepository(link, storage, redis)

async def get_crypto_service(
    repository: CryptoRepository = Depends(get_crypto_repository)
) -> CryptoService:
    return CryptoService(repository)    