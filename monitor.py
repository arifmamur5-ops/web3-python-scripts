from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

def check_node_health():
    try:
        connected = w3.is_connected()
        block = w3.eth.block_number
        gas = w3.eth.gas_price
        
        print(f"{'='*40}")
        print(f"Status    : {'HEALTHY' if connected else 'DOWN'}")
        print(f"Block     : {block}")
        print(f"Gas Price : {gas} wei")
        print(f"{'='*40}")
        
    except Exception as e:
        print(f"ERROR: {e}")

# Monitor setiap 10 detik
print("Starting node monitor... (Ctrl+C to stop)")
while True:
    check_node_health()
    time.sleep(10)
