from web3 import Web3
import requests

# Public RPC endpoint lo
PUBLIC_RPC = "https://mobbishly-bioplasmic-mariah.ngrok-free.dev"

# Connect via public URL
w3 = Web3(Web3.HTTPProvider(
    PUBLIC_RPC,
    request_kwargs={
        'headers': {
            'Content-Type': 'application/json',
            'ngrok-skip-browser-warning': 'true'
        }
    }
))

print(f"Public RPC: {PUBLIC_RPC}")
print(f"Connected:  {w3.is_connected()}")
print(f"Chain ID:   {w3.eth.chain_id}")
print(f"Block:      {w3.eth.block_number}")
print()
print("✅ Your node is accessible from the internet!")
