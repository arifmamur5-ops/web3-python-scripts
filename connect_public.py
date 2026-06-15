from web3 import Web3

PUBLIC_RPC = "https://mobbishly-bioplasmic-mariah.ngrok-free.dev"
API_KEY = "arif-secret-key-2026"

w3 = Web3(Web3.HTTPProvider(
    PUBLIC_RPC,
    request_kwargs={
        'headers': {
            'Content-Type': 'application/json',
            'ngrok-skip-browser-warning': 'true',
            'X-API-Key': API_KEY
        }
    }
))

print(f"Connected: {w3.is_connected()}")
print(f"Chain ID:  {w3.eth.chain_id}")
print(f"Block:     {w3.eth.block_number}")
print("✅ Authenticated connection via public RPC!")
