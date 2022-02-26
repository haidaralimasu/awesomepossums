from scripts.helpful_scripts import get_account
from brownie import AwesomePossums, config, network
import os


def deploy_nft():
    account = get_account()

    # verfiying smart contract
    publish_source = config["networks"][network.show_active()]["verify"]

    print('deploying NFT contract ...')
    nft = AwesomePossums.deploy(
        'AwesomePossums',
        'APN',
        'https://gateway.pinata.cloud/ipfs/Qma4UxBgWeh7SbMSEqGCssbWHhtQA3PR3GGGFGSm3czRyW/',
        'https://gateway.pinata.cloud/ipfs/QmcbaaNZrFKM9v2jqy3ddJwcGe2kThpF5T8NHdgqPbpM1c',
        {"from": account},
        publish_source=publish_source
    )

    print(f'nft is deployed at {nft.address}')

    os.remove('address.txt')
    f = open('address.txt', 'a')
    f.write(f'nft deployed at {nft.address}')
    f.close()


def main():
    deploy_nft()
