"""
MANTLE ALPHA AGENT - DECENRALIZED WEB3 RPC TRANSPORT LAYER
=========================================================
Track: AI Alpha & Data | Mantle Turing Test Hackathon 2026
Author: Emmanuel
Description: High-performance blockchain data transport engine. Features live 
             multi-node latency benchmarking, automatic gas cost calculations, 
             and external market aggregation API integrations with secure fallbacks.
"""

import requests
import json
import time
import random
from config import RPC_ENDPOINTS, USER_CONFIGS, ENGINE_MEMORY

def benchmark_and_sort_nodes():
    """Pings all configured Mantle endpoints and sorts them by latency speed"""
    tested_nodes = []
    payload = {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 99}
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    
    for url in RPC_ENDPOINTS:
        start_time = time.perf_counter()
        try:
            res = requests.post(url, data=json.dumps(payload), headers=headers, timeout=3.5)
            if res.status_code == 200:
                elapsed = time.perf_counter() - start_time
                tested_nodes.append((elapsed, url))
        except Exception:
            continue
            
    tested_nodes.sort(key=lambda x: x)
    sorted_urls = [node for latency, node in tested_nodes]
    return sorted_urls if sorted_urls else RPC_ENDPOINTS

def query_mantle_rpc(method, params=[]):
    """Dispatches payload requests to the fastest operational RPC endpoint natively"""
    payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    
    optimized_routes = benchmark_and_sort_nodes()
    for rpc_url in optimized_routes:
        try:
            response = requests.post(rpc_url, data=json.dumps(payload), headers=headers, timeout=5)
            if response.status_code == 200:
                json_data = response.json()
                if "result" in json_data and json_data["result"] is not None:
                    return json_data.get("result")
        except Exception:
            continue
    return None

def fetch_live_asset_market_price():
    """Queries price metrics dynamically and falls back securely if rate-limited"""
    target_id = "mantle" if USER_CONFIGS["tracked_asset"].upper() == "MNT" else "ethereum"
    url = f"https://coingecko.com{target_id}&vs_currencies=usd"
    
    try:
        res = requests.get(url, timeout=3.5)
        if res.status_code == 200:
            price_data = res.json()
            market_price = price_data.get(target_id, {}).get("usd")
            if market_price:
                USER_CONFIGS["usd_valuation_fallback"] = float(market_price)
                return float(market_price)
    except Exception:
        pass
    return float(USER_CONFIGS["usd_valuation_fallback"])

def calculate_transaction_risk_metrics(tx_data, mnt_value):
    """Profiles transaction characteristics to compute a threat severity level"""
    risk_score = 10
    if mnt_value >= (USER_CONFIGS["whale_threshold"] * 5):
        risk_score += 35
    elif mnt_value >= USER_CONFIGS["whale_threshold"]:
        risk_score += 15
        
    gas_limit = int(tx_data.get("gas", "0x0"), 16)
    if gas_limit > 5000000:
        risk_score += 40
    elif gas_limit > 500000:
        risk_score += 15
        
    if not tx_data.get("to"):
        risk_score += 15
        
    return min(risk_score, 100)

def profile_block_transactions_array(block_data):
    """Iterates through block arrays to extract and parse transactional vectors without hardcoding"""
    if not block_data or "transactions" not in block_data:
        return []
        
    compiled_transactions = []
    tx_list = block_data["transactions"]
    current_market_price = fetch_live_asset_market_price()
    
    for tx in tx_list:
        tx_from = str(tx.get("from", "")).lower()
        tx_to = str(tx.get("to", "")).lower()
        hex_value = tx.get("value", "0x0")
        wei_value = int(hex_value, 16)
        mnt_value = wei_value / 10**18
        
        # Priority Flag Check: Alert if volume matches boundary OR if address sits in custom priority watchlist
        is_priority = (tx_from in USER_CONFIGS["priority_wallets"]) or (tx_to in USER_CONFIGS["priority_wallets"])
        
        if mnt_value >= USER_CONFIGS["whale_threshold"] or is_priority:
            # Check if address sits in user explicit ignore table
            if (tx_from in USER_CONFIGS["ignored_wallets"]) or (tx_to in USER_CONFIGS["ignored_wallets"]):
                continue
                
            gas_used = int(tx.get("gas", "0x5208"), 16)
            usd_value = mnt_value * current_market_price
            risk_score = calculate_transaction_risk_metrics(tx, mnt_value)
            
            profiled_tx = {
                "hash": tx.get("hash"),
                "from": tx.get("from"),
                "to": tx.get("to"),
                "value_tokens": mnt_value,
                "value_usd": usd_value,
                "gas_used": gas_used,
                "risk_score": risk_score
            }
            compiled_transactions.append(profiled_tx)
            
            if mnt_value > ENGINE_MEMORY["highest_whale_transfer"]:
                ENGINE_MEMORY["highest_whale_transfer"] = mnt_value
                
    return compiled_transactions
