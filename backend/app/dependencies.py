from fastapi import Depends
from redis.asyncio import Redis

from repositories import CryptoRepository
from services import CryptoService
from models import Storage, CryptoLink
from redis_CL import RedisCL, redis

async def get_storage():
    return Storage()

async def get_crypto_link():
    return CryptoLink()

async def get_redisCL():
    return redis

async def get_crypto_repository(
    link: CryptoLink = Depends(get_crypto_link), 
    storage: Storage = Depends(get_storage),
    redis: RedisCL = Depends(get_redisCL)
):
    return CryptoRepository(link, storage, redis)

async def get_crypto_service(
    repository: CryptoRepository = Depends(get_crypto_repository)
):
    return CryptoService(repository)