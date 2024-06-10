import uvicorn
import httpx
import urllib.parse

from fastapi import FastAPI

from dataclasses import dataclass, field
from typing import List, Dict, TypedDict
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
    
@dataclass
class CryptoLink:
    array: List[Link] = field(default_factory=lambda: 
    [
        Link(
            name='shentu', 
            link_height='https://shentu-api.testovi.ch/cosmos/base/tendermint/v1beta1/blocks/latest',
            link_total_balance='https://shentu-api.testovi.ch/cosmos/staking/v1beta1/validators/shentuvaloper1m8qkqhmymvq5a8a6wfz35g523rx0pqamuuy7zt/delegations?height'
        ),
        
        Link(name='stargaze', 
            link_height='https://stargaze-api.testovi.ch/cosmos/base/tendermint/v1beta1/blocks/latest', 
            link_total_balance='https://stargaze-api.testovi.ch/cosmos/staking/v1beta1/validators/starsvaloper1tnx3z8ke9za65v32qxhu65mav2282jru8989a6/delegations?height'
        ),

        Link(name='comdex', 
            link_height='https://comdex-api.testovi.ch/cosmos/base/tendermint/v1beta1/blocks/latest', 
            link_total_balance='https://comdex-api.testovi.ch/cosmos/staking/v1beta1/validators/comdexvaloper1jum0pjcuxhj5dh7r6alhledh2ustw9wqrrftv8/delegations?height'
        ),

        # Link(name='comdex', 
        #     link_height='https://umee-api.testovi.ch/cosmos/base/tendermint/v1beta1/blocks/latest', 
        #     link_total_balance='https://comdex-api.testovi.ch/cosmos/staking/v1beta1/validators/starsvaloper1tnx3z8ke9za65v32qxhu65mav2282jru8989a6/delegations?height'
        # )

    ])


@dataclass
class CryptoRepostiry(CryptoAbstract):
    link: CryptoLink
    storage: Storage
    
    async def height(self):
        async with httpx.AsyncClient() as client:
            for items in self.link.array:
                res = await client.get(items['link_height'])
                height = res.json()['block']['header']['height']
                self.storage.data[items['name']] = [{
                    'height': height
                }]

    async def total(self):
        async with httpx.AsyncClient() as client:
            paginaiton_summ: Dict[str, List[int]] = {}

            for item in self.link.array:
                name = item['name']
                if name in self.storage.data:
                    height = self.storage.data[name][0]['height']
                    next_key = None
                    paginaiton_summ[name] = []

                    while True:
                        url = f'{item["link_total_balance"]}{height}'
                        if next_key:
                            url += f'&pagination.key={next_key}'
                        
                        encoded_url = urllib.parse.quote(url, safe=':/?&=')
                        response = await client.get(encoded_url)
                        if response.status_code != 200:
                            break

                        data = response.json()
                        next_key = data['pagination'].get('next_key')
                        total_wallets = int(data['pagination']['total'])
                        
                        if total_wallets > 0:
                            self.storage.data[name].append({'total': total_wallets})

                        for delegation in data['delegation_responses']:
                            paginaiton_summ[name].append(int(delegation['balance']['amount']))
                        
                        if not next_key:
                            break
                raise Exception('Not found height')
            for name, amounts in paginaiton_summ.items():
                total_amount = sum(amounts) // 1_000_000
                self.storage.data[name].append({'amount': total_amount})

    async def result(self):
        await self.height()
        await self.total()

@dataclass
class Crypto:
    ...

app = FastAPI(
    title='testovich API',
    version='0.0.1',
    description='get all crypto'
)

@app.get('/')
async def get_all_info():
    storage = Storage({})
    all_link = CryptoLink()
    a = CryptoRepostiry(all_link, storage)
    await a.result()
    print(storage.data)
    return 'fwefew'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)