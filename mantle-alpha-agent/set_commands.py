"""
MANTLE ALPHA AGENT - TELEGRAM MENU COMMANDS REGISTRY
===================================================
Description: Explicitly registers slash macros with the Telegram Bot API.
             Enables native clickable pop-up interface menus for all users.
"""

import requests
from config import TELEGRAM_BASE_URL

def register_bot_commands():
    url = f"{TELEGRAM_BASE_URL}/setMyCommands"
    
    # Defining an elite, premium set of analytical controls for users
    payload = {
        "commands": [
            {
                "command": "status",
                "description": "📋 Audit active configuration matrices & runtime states."
            },
            {
                "command": "set_threshold",
                "description": "💰 Adjust minimum Whale detection boundary (e.g., /set_threshold 25000)"
            },
            {
                "command": "set_theme",
                "description": "🎨 Toggle terminal layouts (CYBERPUNK, RADAR_GREEN, TACTICAL_RED)"
            },
            {
                "command": "set_asset",
                "description": "💱 Update dynamic token label metrics (e.g., /set_asset mETH)"
            },
            {
                "command": "help",
                "description": "🎯 Print high-density system manuals and operational guides."
            }
        ]
    }
    
    print("📡 Injecting command definitions into Telegram infrastructure...")
    try:
        response = requests.post(url, json=payload, timeout=12)
        if response.status_code == 200 and response.json().get("ok"):
            print("✨ SUCCESS: Clickable menu commands registered perfectly on Telegram servers!")
        else:
            print(f"❌ Rejection response received: {response.text}")
    except Exception as e:
        print(f"❌ Connection error during layout registration: {e}")

if __name__ == "__main__":
    register_bot_commands()
