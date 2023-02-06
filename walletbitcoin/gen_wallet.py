from bitcoinlib.wallets import Wallet, wallet_delete_if_exists
from bitcoinlib.mnemonic import Mnemonic

wallet_delete_if_exists('Bitcoin')

passphrase = Mnemonic().generate()

wallet = Wallet.create('Bitcoin', keys=passphrase, network='bitcoin')
address = wallet.get_key().address

print(f'Tu dirección BTC: {address}\nTu frase secreta: {passphrase}')