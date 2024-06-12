from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from dependencies import get_crypto_service
from services import CryptoService
from redis_CL import redis

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis.connect()
    yield
    await redis.disconnect()

app = FastAPI(
    title='testovich API',
    version='0.0.1',
    description='get all crypto',
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