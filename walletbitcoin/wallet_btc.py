from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.mnemonic import Mnemonic

passphrase = input('Inserta tu frase secreta: ')
wallet = wallet_create_or_open('Bitcoin', keys=passphrase, network='bitcoin')

address = wallet.get_key().address
balance = wallet.balance()

print(f'Tu dirección BTC: {address}')
print(f'Tu balance: {balance} BTC')