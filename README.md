# 🎥 Automated Twitch Clipping & Posting Tool (In Progress)

A Python-based tool that connects to the **Twitch Helix API** and **EventSub WebSocket** to monitor chat activity, detect high-engagement moments, and automatically create and manage clips for streamers.

> 🚧 **Project Status:** In Active Development  
> Current focus: real-time chat event streaming and OAuth integration.

---

## 🚀 Features (In Progress)

### ✅ Implemented
- **OAuth 2.0 Authentication:**  
  Securely generates and refreshes access tokens for Twitch API requests using environment variables.
- **Broadcaster Lookup:**  
  Queries Twitch Helix endpoints to identify broadcaster IDs and channel metadata.
- **Chat Event Listener:**  
  Connects to Twitch **EventSub WebSocket** to receive real-time messages and events.
- **Structured JSON Logging:**  
  Parses and stores incoming chat messages for later analysis or AI processing.

### 🧠 Planned
- **Chat Spike Detection:**  
  Detect bursts of chat activity or specific keywords to trigger clip creation.
- **Automated Clip Creation:**  
  Use Twitch’s **Create Clip** endpoint to automatically capture highlights.
- **Cloud Storage Integration:**  
  Upload and manage generated clips through AWS, Google Cloud, or Firebase/Firestore.
- **AI Editing Integration:**  
  Send created clips to an external **AI video editor** for automatic trimming, captioning, or highlight generation.

---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python |
| **Libraries** | `requests`, `asyncio`, `websockets`, `dotenv`, `json` |
| **APIs** | Twitch Helix API, EventSub WebSocket |
| **Auth** | OAuth 2.0 (App and User tokens) |
| **Planned Tools** | Cloud storage, external AI video editors |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/SamuelPechan/twitch-clipping-bot.git
cd twitch-clipping-bot
