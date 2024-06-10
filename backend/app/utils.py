import httpx

from dataclasses import dataclass, field
from typing import List
from schemas import CryptoAbstract, Storage, Link

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
        )
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
        async with httpx.AsyncClient() as cleint:
            for items in self.link.array:
                name = items['name']
                if name in self.storage.data:
                    height = self.storage.data[name][0]['height']
                    res = await cleint.get(f'{items["link_total_balance"]}{height}')
                    print(res.json())
    async def result(self):
        await self.height()
        await self.total()