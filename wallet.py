from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Ambil semua account dari Anvil
accounts = w3.eth.accounts

print(f"Found {len(accounts)} accounts:\n")

for i, account in enumerate(accounts):
    balance_wei = w3.eth.get_balance(account)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    print(f"[{i}] {account}")
    print(f"    Balance: {balance_eth} ETH\n")
