# Web3 Python Scripts

Python automation scripts for Ethereum node interaction and public RPC infrastructure testing.

## Scripts
- `connect.py` — Basic RPC connection and node info (Localhost)
- `connect_public.py` — Secure public RPC connection utilizing Ngrok tunnels and Nginx reverse proxy
- `monitor.py` — Real-time node health monitoring loop
- `wallet.py` — Account balance inspector
- `send_tx.py` — Send ETH transactions programmatically
- `interact_contract.py` — Read/write smart contract state

## Advanced Infrastructure
The `connect_public.py` script tests the node accessibility over the public internet using a secure layered architecture:


## Requirements
pip install web3

## Usage
Run Anvil first: `anvil`
Then: `python <script>.py`