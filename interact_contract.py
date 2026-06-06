from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Ganti dengan contract address lo
CONTRACT_ADDRESS = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"

# ABI dari Counter contract
ABI = [
    {
        "inputs": [],
        "name": "increment",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "number",
        "outputs": [{"type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
account = w3.eth.accounts[0]

# Load contract
contract = w3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=ABI
)

# Baca nilai awal
print(f"Counter before: {contract.functions.number().call()}")

# Increment 3x
for i in range(3):
    tx = contract.functions.increment().build_transaction({
        'from': account,
        'nonce': w3.eth.get_transaction_count(account),
        'gas': 100000,
        'gasPrice': w3.eth.gas_price,
        'chainId': w3.eth.chain_id
    })
    
    signed = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Increment {i+1}: tx {tx_hash.hex()[:20]}...")

# Baca nilai akhir
print(f"Counter after: {contract.functions.number().call()}")
