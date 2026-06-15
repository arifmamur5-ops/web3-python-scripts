# Web3 Python Scripts

Python automation scripts for Ethereum node interaction and secure public RPC infrastructure architectures.

## Scripts
- `connect.py` — Basic RPC connection and node info (Localhost)
- `connect_public.py` — Secure public RPC connection with X-API-Key validation via network tunnels
- `monitor.py` — Real-time node health monitoring loop
- `wallet.py` — Account balance inspector
- `send_tx.py` — Send ETH transactions programmatically
- `interact_contract.py` — Read/write smart contract state

## Advanced Infrastructure Architecture (Session 7 & 8)
Production-ready edge infrastructure designed to securely expose local node capabilities to the public internet:


```
Internet ──> Ngrok Tunnel ──> Nginx Gateway (Port 2096) ──> Anvil Node (Port 8545)
│
[API Key Auth Filter]
```

### Infrastructure Features Implemented:
1. **Reverse Proxying:** Traffic from port 2096 is systematically scrubbed and upstreamed to the node's native execution port.
2. **Rate Limiting:** Protects the internal blockchain node from RPC flooding and denial-of-service attempts.
3. **Gateway Authentication:** Enforces strict header checks (`X-API-Key`). Non-authenticated payloads are instantly dropped with HTTP `401 Unauthorized` payloads before hitting the blockchain state.

## Requirements
```bash
pip install web3 requests python-dotenv

```
## Usage
 1. Run Anvil first: anvil
 2. Start the secure edge gateway tunnel: ngrok http 2096
 3. Execute the authenticated public python script: python connect_public.py

