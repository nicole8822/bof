import requests
import json
import time
import matplotlib.pyplot as plt
import networkx as nx
import io
import random

# Communication Core Variables - FIXED TO CORRECT API PATHWAY
TELEGRAM_BASE_URL = "https://telegram.org"
CHAT_ID = 6660670214
WHALE_THRESHOLD_MNT = 1  # Kept at 1 MNT for instant verification

# Premium Web3 Gateways - Your working endpoints array
RPC_ENDPOINTS = [
    "https://1rpc.io/mantle",
    "https://mantle-mainnet.public.blastapi.io",
    "https://mantle.drpc.org",
    "https://rpc.mantle.xyz"
]

def send_visual_intelligence_report(mnt_value, tx_from, tx_to, tx_hash, usd_value, execution_mode="LIVE"):
    """Compiles on-chain transaction metrics into a network topology flowchart map"""
    print(f"🎨 [{execution_mode}] Compiling Visual Flow Chart...")
    
    G = nx.DiGraph()
    src = tx_from if tx_from else "Unknown Wallet"
    dst = tx_to if tx_to else "Contract Deployment"
    
    lbl_from = f"Whale Origin\n({src[:6]}...{src[-4:]})"
    lbl_to = f"Recipient Target\n({dst[:6]}...{dst[-4:] if tx_to else 'Contract'})"
    G.add_edge(lbl_from, lbl_to, weight=mnt_value)
    
    # Render with dark luxury trading theme layout parameters
    plt.figure(figsize=(7, 4), facecolor='#111827')
    ax = plt.gca()
    ax.set_facecolor('#111827')
    
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='#10B981', node_size=2800, alpha=0.9, edgecolors='#F59E0B')
    # FIXED: Corrected networkx layout array drawing argument name
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='#9CA3AF', width=3, arrowstyle='->', arrowsize=22)
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='#FFFFFF', font_weight='bold')
    
    plt.title(f"MANTLE NETWORK: AI WHALE FLOW GRAPH ({execution_mode})", color='#F59E0B', fontsize=11, fontweight='bold', pad=12)
    plt.axis('off')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor='#111827')
    buf.seek(0)
    plt.close()
    
    alert_msg = (
        f"🦈 *MANTLE AI VISUAL REPORT ({execution_mode})* 🦈\n\n"
        f"💰 *Volume:* `{mnt_value:,.2f} MNT` (~*${usd_value:,.2f} USD*)\n"
        f"👤 *From:* `{src}`\n"
        f"🎯 *To:* `{dst}`\n\n"
        f"📈 *Status:* Intelligence metrics analyzed cleanly via blockchain loop tracking.\n"
        f"🌐 [Verify on MantleScan](https://mantle.xyz{tx_hash})"
    )
    
    files = {'photo': ('graph.png', buf, 'image/png')}
    data = {'chat_id': CHAT_ID, 'caption': alert_msg, 'parse_mode': 'Markdown'}
    
    try:
        # FIXED: Routing directly through the dedicated telegram endpoint channel
        res = requests.post(f"{TELEGRAM_BASE_URL}/sendPhoto", data=data, files=files, timeout=15)
        if res.status_code == 200:
            print("✨ Analytics Image Dispatched to Telegram Interface Successfully!")
        else:
            print(f"⚠️ Telegram rejected asset payload: {res.text}")
    except Exception as e:
        print(f"Media routing anomaly caught: {e}")

def get_rpc_data_resilient(method, params=[]):
    payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    
    shuffled_nodes = list(RPC_ENDPOINTS)
    random.shuffle(shuffled_nodes)
    
    for rpc_url in shuffled_nodes:
        try:
            response = requests.post(rpc_url, data=json.dumps(payload), headers=headers, timeout=5)
            if response.status_code == 200:
                json_data = response.json()
                if "result" in json_data and json_data["result"] is not None:
                    return json_data.get("result")
        except Exception:
            continue
    return None

def trigger_sandbox_simulation():
    """Failsafe simulation mode that tracks realistic transactions locally when IPs are blocked"""
    print("\n🚀 Entering Autonomous Hackathon Simulation Mode...")
    print("🟢 Fail-Safe Sandbox Enabled. Simulating Live Block Matrix streams...")
    
    mock_block = 95850900
    addresses = [
        "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
        "0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
        "0x281055af98248E738a5927774A17d23F365701a4",
        "0xC02aaA39b223FE8D0A0e5C4F27ead9083C756Cc2"
    ]
    
    while True:
        try:
            txs_count = random.randint(1, 5)
            print(f"🔍 Scanning block #{mock_block} ({txs_count} txs)...")
            
            if random.choice([True, False]):
                mnt_value = random.uniform(5000, 125000)
                usd_value = mnt_value * 0.85
                tx_from = random.choice(addresses)
                tx_to = random.choice(addresses)
                while tx_to == tx_from:
                    tx_to = random.choice(addresses)
                    
                tx_hash = "0x" + "".join(random.choices("abcdef0123456789", k=64))
                send_visual_intelligence_report(mnt_value, tx_from, tx_to, tx_hash, usd_value, execution_mode="SANDBOX")
                
            mock_block += 1
            time.sleep(6)
        except KeyboardInterrupt:
            print("\nSafe sandbox environment storage preservation complete.")
            break

def start_tracker_loop():
    print("🦈 Mantle Visual Analytics Agent Core Booted.")
    print("Market Valuation Reference Online: 1 MNT = $0.8500 USD")
    
    hex_current = get_rpc_data_resilient("eth_blockNumber")
    if not hex_current:
        print("⚠️ All network gateways throttled. Initiating cloud safe path strategy...")
        trigger_sandbox_simulation()
        return
        
    last_scanned_block = int(hex_current, 16)
    print(f"🟢 Direct Live Tracking Connected at block #{last_scanned_block}")

    while True:
        try:
            hex_latest = get_rpc_data_resilient("eth_blockNumber")
            if hex_latest:
                latest_block = int(hex_latest, 16)
                while last_scanned_block <= latest_block:
                    hex_block = hex(last_scanned_block)
                    block_data = get_rpc_data_resilient("eth_getBlockByNumber", [hex_block, True])
                    if block_data and "transactions" in block_data:
                        tx_list = block_data["transactions"]
                        print(f"🔍 Scanning block #{last_scanned_block} ({len(tx_list)} txs)...")
                        for tx in tx_list:
                            wei_value = int(tx.get("value", "0x0"), 16)
                            mnt_value = wei_value / 10**18
                            if mnt_value >= WHALE_THRESHOLD_MNT:
                                send_visual_intelligence_report(
                                    mnt_value, tx.get("from"), tx.get("to"), 
                                    tx.get("hash"), mnt_value * 0.85, "LIVE"
                                )
                    last_scanned_block += 1
            time.sleep(3)
        except KeyboardInterrupt:
            print("\nSafe execution breakdown shutdown complete.")
            break
        except Exception as e:
            print(f"Buffer logic anomaly: {e}")
            time.sleep(5)

if __name__ == "__main__":
    start_tracker_loop()
