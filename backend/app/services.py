from repositories import CryptoRepository
from typing import Dict, List

class CryptoService:
    def __init__(self, repository: CryptoRepository) -> None:
        self.repository = repository

    async def get_data(self) -> List[Dict[str, Dict[str, int]]]:
        return await self.repository.result()