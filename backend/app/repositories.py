import asyncio
import json
import urllib

from typing import Dict, List
from httpx import AsyncClient, HTTPStatusError
from models import CryptoLink, Storage, Link
from redis_CL import RedisCL


class CryptoRepository:
    def __init__(
    self, 
    link: CryptoLink, 
    storage: Storage, 
    redis: RedisCL
    ) -> None:
        
        self.link = link
        self.storage = storage
        self.redis = redis

    async def fetch_json(
        self, 
        client: AsyncClient, 
        url: str
        ) -> Dict:
        
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError:
            return None
        except Exception:
            return None

    async def fetch_height(
        self, 
        client: AsyncClient, 
        link: Link
        ) -> Dict[str, int]:
        
        data = await self.fetch_json(client, link.link_height)
        if not data:
            return {}
        height = data['block']['header']['height']
        return {link.name: {'height': height}}

    async def fetch_total(
        self, 
        client: AsyncClient, 
        link: Link, 
        height: int
        ) -> Dict[str, int]:
        
        next_key = None
        total_wallets = 0
        total_amount = 0
        while True:
            url = f'{link.link_total_balance}{height}'
            if next_key:
                url += f'&pagination.key={next_key}'
            encoded_url = urllib.parse.quote(url, safe=':/?&=')
            data: Dict[str, Dict[str, int]] = await self.fetch_json(client, encoded_url)
            if not data:
                break
            next_key = data['pagination'].get('next_key')
            total_wallets += int(data['pagination']['total'])
            for delegation in data['delegation_responses']:
                total_amount += int(delegation['balance']['amount'])
            if not next_key:
                break
        return {
            link.name: {
                'total': total_wallets,
                'amount': total_amount // 1_000_000,
                'img': link.name,
                'link': link.link_refresh
            }
        }

    async def process_link(
        self, 
        client: AsyncClient, 
        link: Link
        ) -> Dict[str, Dict[str, int]]:
        
        height_data: Dict[str, Dict[str, int]]  = await self.fetch_height(client, link)
        if not height_data:
            return {}
        height = int(height_data[link.name]['height'])
        total_data = await self.fetch_total(client, link, height)
        if not total_data:
            return height_data
        height_data[link.name].update(total_data[link.name])
        return height_data

    async def process_links(self):
        async with AsyncClient() as client:
            tasks = [self.process_link(client, link) for link in self.link.array]
            results = await asyncio.gather(*tasks)
            for result in results:
                if result:
                    self.storage.data.append(result)

    #redis
    async def get_cached_data(self, key: str):
        data = await self.redis.client.get(key)
        if data:
            return json.loads(data)
        return None

    async def set_cached_data(
        self, 
        key: str, 
        value: List[Dict[str, Dict[str, int]]], 
        expire: int = 21600
        ):
        await self.redis.client.set(key, json.dumps(value), expire)
        
    async def result(self):
        key = 'crypto'
        cached_data = await self.get_cached_data(key)
        if cached_data:
            return cached_data
        
        await self.process_links()
        await self.set_cached_data(key, self.storage.data)
        return self.storage.data