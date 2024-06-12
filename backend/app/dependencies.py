from fastapi import Depends

from repositories import CryptoRepository
from services import CryptoService
from models import Storage, CryptoLink

async def get_storage():
    return Storage()

async def get_crypto_link():
    return CryptoLink()

async def get_crypto_repository(
    link: CryptoLink = Depends(get_crypto_link), 
    storage: Storage = Depends(get_storage)
    ):
    return CryptoRepository(link, storage)

async def get_crypto_service(
    repository: CryptoRepository = Depends(get_crypto_repository)
    ):
    return CryptoService(repository)    