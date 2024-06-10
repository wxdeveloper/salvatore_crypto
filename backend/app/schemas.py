from dataclasses import dataclass
from abc import ABC, abstractmethod

class CryptoAbstract(ABC):
    @abstractmethod
    async def height():
        pass

    @abstractmethod
    async def total():
        pass

    @abstractmethod
    async def result():
        pass

@dataclass
class Storage:
    data: dict

@dataclass
class Link:
    name: str
    link_height: str
    link_total_balance: str

    def __getitem__(self, key):
        return getattr(self, key)