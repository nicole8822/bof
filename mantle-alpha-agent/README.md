# Mantle Alpha Agent: Real-Time AI Visual Transaction Tracker

Built for the **Mantle Turing Test Hackathon 2026 (Phase 2: AI Awakening)** under the **AI Alpha & Data Track**.

Mantle Alpha Agent is a decentralized intelligence bot that monitors the Mantle Network Mainnet in real time. Instead of drowning users in raw, unreadable hexadecimal transaction logs, the agent dynamically parses incoming block arrays, calculates live token values, and autonomously compiles behavioral asset flowcharts. These institutional-grade visual intelligence reports are streamed directly to a target Telegram interface.

---

##  Key Features

*   **Real-Time Mainnet Indexing:** Hooks directly into the Mantle Network lifecycle to index blocks sequentially as they are mined.
*   **Autonomous Flow Map Generator:** Uses mathematical network topology structures to visualize the movement of assets between sender and recipient wallets on a dark-mode terminal canvas.
*   **Fail-Safe Sandbox Simulation Framework:** Includes a local network mocking layer that allows end-to-end user experience presentations and UI testing even during extreme public node congestion.
*   **MantleScan Integration:** Appends verified network block explorer endpoints to every alert payload for immediate, verifiable auditing.

---

## The Tech Stack

*   **Language:** Python 3.10+
*   **Blockchain Integration:** JSON-RPC / Network Requests Protocols
*   **Data Analytics & Visualization:** `networkx`, `matplotlib`, `pandas`
*   **Communication Gateway:** Telegram Bot API Engine

---

## Local Installation & Setup

### 1. Clone & Initialize the Project Workspace
```bash
git clone https://github.com
cd mantle-alpha-agent
```

### 2. Install Package Dependencies
Ensure your environment contains the core analytical and math plotting libraries:
```bash
pip install requests matplotlib networkx pandas
```

### 3. Configure Your Environment Variables
Open the main execution file (`agent.py`) and replace the configuration baselines with your secure network keys:
*   `TELEGRAM_BASE_URL`: Your HTTP API Token obtained from `@BotFather`.
*   `CHAT_ID`: Your unique target routing identifier.

---

## 🏁 Running the Application Core

To initiate the live mainnet tracker, run the following command in your terminal:
```bash
python agent.py
```

### Triggering a Stress-Test Simulation
Because high-value token transactions happen organically across the network, you can simulate instantaneous map compilation results for your presentation by adjusting the value filter threshold to `1 MNT` inside `agent.py`. The bot will immediately intercept active network traffic frames and forward visual charts straight to your smartphone device.

---

## Hackathon Architecture Context
This agent is structured to align with the core judging criteria of the **Turing Test Hackathon 2026**:
1.  **On-Chain Context:** Explicitly tracks raw state values across the Mantle settlement layer.
2.  **User Experience (UX):** Eradicates text fatiguing by transforming blockchain hashes into instant visual insights.
3.  **Stability:** Built using a zero-single-point-of-failure routing scheme designed for stable, live presentations.

Developed with 💻 by Prince Osinachi during the 2026 AI Awakening.
