from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Storage:
    data: List[Dict[str, Dict[str, int]]] = field(default_factory=list)

@dataclass
class Link:
    name: str
    link_height: str
    link_total_balance: str
    link_refresh: str
    link_rpc: str
    link_api: str
    link_grpc: str

@dataclass
class CryptoLink:
    array: List[Link] = field(default_factory=lambda: [
        Link(
            name='STAKE SHENTU', 
            link_height='https://shentu-api/cosmos/base/tendermint/v1beta1/blocks/latest',
            link_total_balance='https://shentu-api/cosmos/staking/v1beta1/validators/shentuvaloper1m8qkqhmymvq5a8a6wfz35g523rx0pqamuuy7ztlegations?height',
            link_refresh='https://wallet.keplr.app/chains/shentu?modal=validator&chain=shentu-2.2&validator_address=shentuvaloper1m8qkqhmymvq5a8a6wfz35g523rx0muuy7zt',
            link_rpc='1',
            link_api='2',
            link_grpc='3',
        ),
        Link(
            name='STAKE STARGAZE', 
            link_height='https://stargaze-api/cosmos/base/tendermint/v1beta1/blocks/latest', 
            link_total_balance='https://stargaze-api/cosmos/staking/v1beta1/validators/starsvaloper1tnx3z8ke9za65v32qxhu6282jru8989a6/delegations?height',
            link_refresh='https://wallet.keplr.app/chains/stargaze?modal=validator&chain=stargaze-1&validator_address=starsvaloper1tnx3z8ke9za65v32qxhu65mavru8989a6',
            link_rpc='https://stargaze-rpc/',
            link_api='https://stargaze-api/',
            link_grpc='https://stargaze-grpc:9090',

        ),
        Link(
            name='STAKE COMDEX', 
            link_height='https://comdex-api./cosmos/base/tendermint/v1beta1/blocks/latest', 
            link_total_balance='https://comdex-api./cosmos/staking/v1beta1/validators/comdexvaloper1jum0pjcuxhj5dh7r6alhledh2ustwrrftv8/delegations?height',
            link_refresh='https://explorer.comdex.one/comdex-1/staking/comdexvaloper1jum0pjcuxhj5dh7r6alhh2ustw9wqrrftv8',
            link_rpc='1',
            link_api='2',
            link_grpc='3',
        ),
        Link(
            name='STAKE JACKAL', 
            link_height='https://jackal-api./cosmos/base/tendermint/v1beta1/blocks/latest', 
            link_total_balance='https://jackal-api./cosmos/staking/v1beta1/validators/comdexvaloper1jum0pjcuxhj5dh7r6alhletw9wqrrftv8/delegations?height',
            link_refresh='https://ping.pub/jackal/staking/jklvaloper1wc0d9vrfrx5drsleuhdezlzyjw02yzap8che4w',
            link_rpc='1',
            link_api='2',
            link_grpc='3',
        )
    ])
