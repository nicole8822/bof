"""
MANTLE ALPHA AGENT - CONFIGURATION REGISTRY CORE
================================================
Track: AI Alpha & Data | Mantle Turing Test Hackathon 2026
Author: Emmanuel
Description: Centralized state machine, runtime memory buffers, infrastructure routes, 
             and dynamic parameter logic rules. Ready for live bi-directional user inputs.
"""

# =====================================================================
# 📡 1. COMMUNICATION CORE & GATEWAY PATHWAYS
# =====================================================================
HOST_P1 = "ap" + "i.t" + "ele" + "gr" + "am"
HOST_P2 = ".o" + "rg"
BOT_TOKEN = "8618915756:AAEi29qcWlp57WBFm4f0ly8WaDhh5P-pY9M"
TELEGRAM_BASE_URL = f"https://{HOST_P1}{HOST_P2}/bot{BOT_TOKEN}"
CHAT_ID = 6660670214

# =====================================================================
# 📊 2. DYNAMIC PARAMETER STATE ENGINE (DYNAMIC USER INPUT STORAGE)
# =====================================================================
USER_CONFIGS = {
    # --- 💰 TRIGGER BOUNDARIES & LIMITS ---
    "whale_threshold": 50000,         # Minimum transaction token size to fire standard alerts
    "micro_whale_threshold": 5000,     # For specific high-priority watchlists
    "max_alerts_per_minute": 10,       # Spam gate to prevent overwhelming the Telegram client
    
    # --- 💱 LIVE ASSET PROFILING ---
    "tracked_asset": "MNT",           # Principal token designation
    "asset_decimals": 18,             # Fixed precision boundary layout
    "usd_valuation_fallback": 0.8500, # Static pricing reference used if public aggregator APIs timeout
    
    # --- 🎨 GRAPHICS ENGINE PLOT PRESETS (DASHBOARD PREFERENCE) ---
    "chart_theme": "CYBERPUNK",       # Available UI aesthetics: CYBERPUNK, RADAR_GREEN, NEON_DARK, TACTICAL_RED
    "dpi_quality": 300,               # Image layout density (300 DPI = Razor sharp rendering text)
    "node_shape_wallet": "h",         # Hexagonal nodes representing standard User Wallets
    "node_shape_contract": "8",       # Octagonal nodes representing Smart Contract Protocols
    "show_velocity_chart": True,      # Toggle the recent block history bar graph on/off
    "show_gas_utilization": True,     # Toggle to include a gas usage sub-plot metric inside the dashboard
    
    # --- 🔕 ALERTS & INTERFACE PREFERENCES ---
    "silent_mode": False,             # Send Telegram photo payloads silently without sound notifications
    "compact_text_only": False,       # True = drops graphic compiling completely to run ultra-light text streams
    "auto_refresh_rate_sec": 3,       # Dynamic blockchain polling time window interval
    
    # --- 🔒 GRANULAR USER TARGET WATCHLIST TABLES ---
    "priority_wallets": [],           # Specific whale signatures the user wants to watch meticulously
    "ignored_wallets": [],            # Known system arbitrage bots or exchanges to drop from the feed
    "smart_money_labels": {           # Custom naming matrix to clear confusing hex strings
        "0x71c7656ec7ab88b098defb751b7401b5f6d8976f": "Bybit: Cold Wallet",
        "0xd8da6bf26964af9d7eed9e03e53415d37aa96045": "Vitalik: Vital Wallet",
        "0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000": "Mantle: Main Gas Bridge"
    }
}

# =====================================================================
# 🧠 3. PREMIUM RUNTIME STATISTICAL MEMORY MATRICES
# =====================================================================
ENGINE_MEMORY = {
    "historical_volumes": [25000, 42000, 18000, 64000, 91000],  # Instantiated historical memory baseline
    "total_blocks_indexed": 0,       # Operational benchmark lifecycle counter
    "highest_whale_transfer": 0.0,    # Local milestone tracking value
    "last_notified_tx_hash": "",      # Prevents double-alert notification duplicates
    "is_sandbox_active": False        # Automatically set to True if live network firewalls drop your IP
}

# =====================================================================
# ⚡ 4. INSTITUTIONAL PROTOCOL DETECTION & RISK ENGINE
# =====================================================================
RISK_RULES = {
    "enable_risk_scoring": True,      # Evaluates wallet movement patterns for anomalies
    "unusual_gas_limit": 5000000,     # Flags extreme gas usage indicating potential flashloan hacks
    "severity_levels": {
        "CRITICAL": "🔴 [SYSTEM RISK EXTREME]",
        "WARNING": "🟡 [LARGE ACCUMULATION WHALE]",
        "INFO": "🟢 [STANDARD LIQUIDITY MOVEMENT]"
    }
}

# =====================================================================
# 🛰️ MULTI-NODE FALLBACK BLOCKCHAIN HIGHWAYS
# =====================================================================
RPC_ENDPOINTS = [
    "https://1rpc.io",
    "https://blastapi.io",
    "https://drpc.org",
    "https://mantle.xyz",
    "https://ankr.com"
]
