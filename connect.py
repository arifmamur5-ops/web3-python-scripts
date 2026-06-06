from web3 import Web3

# Connect ke Anvil (jalanin anvil dulu di terminal lain)
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Cek koneksi
print(f"Connected: {w3.is_connected()}")
print(f"Chain ID: {w3.eth.chain_id}")
print(f"Latest block: {w3.eth.block_number}")
print(f"Gas price: {w3.eth.gas_price}")
