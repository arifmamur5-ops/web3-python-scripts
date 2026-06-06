from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Ambil 2 account dari Anvil
sender = w3.eth.accounts[0]
receiver = w3.eth.accounts[1]

# Private key account[0] dari Anvil
private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

print(f"Sender  : {sender}")
print(f"Receiver: {receiver}")

# Cek balance sebelum
before = w3.eth.get_balance(receiver)
print(f"\nBalance before: {w3.from_wei(before, 'ether')} ETH")

# Build transaksi
tx = {
    'from': sender,
    'to': receiver,
    'value': w3.to_wei(1, 'ether'),
    'gas': 21000,
    'gasPrice': w3.eth.gas_price,
    'nonce': w3.eth.get_transaction_count(sender),
    'chainId': w3.eth.chain_id
}

# Sign dan kirim
signed = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)

print(f"\nTx Hash : {tx_hash.hex()}")

# Tunggu konfirmasi
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Status  : {'SUCCESS' if receipt.status == 1 else 'FAILED'}")
print(f"Block   : {receipt.blockNumber}")

# Cek balance sesudah
after = w3.eth.get_balance(receiver)
print(f"\nBalance after: {w3.from_wei(after, 'ether')} ETH")
print(f"Received: {w3.from_wei(after - before, 'ether')} ETH")
