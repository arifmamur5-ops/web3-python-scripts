# Web3 Python Scripts

Python automation scripts for Ethereum node interaction and public RPC infrastructure testing.

## Scripts
- `connect.py` — Basic RPC connection and node info (Localhost)
- `connect_public.py` — Secure public RPC connection utilizing Ngrok tunnels and Nginx reverse proxy
- `monitor.py` — Real-time node health monitoring loop
- `wallet.py` — Account balance inspector
- `send_tx.py` — Send ETH transactions programmatically
- `interact_contract.py` — Read/write smart contract state

## Advanced Infrastructure (Session 7)
The `connect_public.py` script tests the node accessibility over the public internet using a secure layered architecture:

```
Internet ──> Ngrok Tunnel ──> Nginx Reverse Proxy (Port 2096) ──> Anvil Core (Port 8545)
```
This setup ensures the local node is securely exposed with custom rate limiting configured at the Nginx layer.

## Requirements
```bash
pip install web3 requests

```
## Usage
### Local Execution
 1. Run Anvil first:
   ```bash
   anvil
   
   ```
 2. Run any local script:
   ```bash
   python connect.py
   
   ```
### Public RPC Tunnel Execution
 1. Ensure Anvil and Nginx are running locally on your system.
 2. Start the Ngrok tunnel pointing to your secure Nginx port:
   ```bash
   ngrok http 2096
   
   ```
 3. Update the PUBLIC_RPC variable inside connect_public.py with your active Ngrok URL.
 4. Execute the public connection script:
   ```bash
   python connect_public.py
   
   ```