from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from dependencies import get_crypto_service, get_crypto_link
from services import CryptoService
from redis_CL import redis
from models import CryptoLink

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis.connect()
    yield
    await redis.disconnect()

app = FastAPI(
    title='TSTVCH API',
    version='0.0.1',
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-data", response_model=None)
async def get_data(crypto_service: CryptoService = Depends(get_crypto_service)):
    try:
        return await crypto_service.get_data()
    except:
        HTTPException(status_code=403, detail='[Error external serve disconnect]')

@app.get('/get-services', response_model=None)
async def get_services(crypto_link: CryptoLink = Depends(get_crypto_link)):
    response = [
    {
        'name': link.name, 
        'rpc': link.link_rpc, 
        'api': link.link_api, 
        'grpc': link.link_grpc,
    }
    for link in crypto_link.array
    ]
    return response