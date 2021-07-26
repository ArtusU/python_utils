from web3 import Web3
import config



GANACHE_NODE_PROVIDER = config.GANACHE_NODE_PROVIDER
ADDRESS_1 = config.ADDRESS_1
GANACHE_ADDRESS_1_SECRET_KEY = config.GANACHE_SECRET_KEY_ADDRESS_1
ADDRESS_2 = config.ADDRESS_2
GANACHE_ADDRESS_2_SECRET_KEY = config.GANACHE_SECRET_KEY_ADDRESS_2

web3_connection = Web3(Web3.HTTPProvider(GANACHE_NODE_PROVIDER))

global_gas = 4500000
global_gas_price = web3_connection.toWei(8, 'gwei')

def are_we_connected():
    return web3_connection.isConnected()


def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)


def transfer_eth(sender, receiver, signature, amount_eth):
    transaction_body = {
        'nonce': get_nonce(sender),
        'to':receiver,
        'value': web3_connection.toWei(amount_eth, 'ether'),
        'gas': global_gas,
        'gasPrice': global_gas_price
    }

    signed_transaction = web3_connection.eth.account.sign_transaction(transaction_body, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result

