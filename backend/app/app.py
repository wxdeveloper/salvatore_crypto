import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from dependencies import get_crypto_service
from services import CryptoService


app = FastAPI(
    title='testovich API',
    version='0.0.1',
    description='get all crypto',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fetch_data")
async def fetch_data(crypto_service: CryptoService = Depends(get_crypto_service)):
    try:
        return await crypto_service.get_data()
    except:
        HTTPException(status_code=403, detail='[Error external serve disconnect]')
    
    
if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)