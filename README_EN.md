# 🎤 Discord Voice Channel Creator

🌍 Language: **English** | [Polski](README.md)

A Discord bot that automatically creates and manages temporary voice channels with a full management panel.

[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/rAmfu/Discord-Voice-Channel-Creator)
[![Python](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-blue)](https://github.com/Rapptz/discord.py)

---

## 📋 Table of Contents
- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Debian 12 Installation](#-debian-12-installation)
- [🔧 Running in the Background](#-running-in-the-background)
- [🐳 Docker](#-docker)
- [📁 File Structure](#-file-structure)
- [🎯 How It Works](#-how-it-works)
- [🔐 Security](#-security)
- [📝 Configuration](#-configuration)
- [🛠️ Technical Details](#️-technical-details)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [💬 Support](#-support)

---

## ✨ Features

### 🚀 Automatic Channel Creation
- When a user joins the **trigger channel**, the bot automatically creates a new private voice channel for them
- Each user gets their own personalized channel in the format: `🎤 {username}`
- Channels are created in the same category as the trigger channel

### ⚙️ Management Panel
After creating a channel, an interactive panel with an embed appears in the channel. The channel owner can:

| Function | Description |
|----------|-------------|
| **👥 User Limit** | Sets the maximum number of people in the channel (0-99) |
| **🔒 Private / Public** | Toggles channel visibility |
| **✏️ Rename** | Changes the channel name |
| **📝 Change Description** | Adds/removes a channel description (displayed in the embed) |
| **👑 Transfer Ownership** | Transfers channel control to another user |
| **🚪 Kick User** | Kicks a person from the channel |
| **🚫 Block User** | Blocks access to the channel |
| **🔓 Unblock User** | Restores access for a blocked user |
| **🗑️ Delete Channel** | Deletes the channel |

### 🧹 Automatic Cleanup
- Empty channels are automatically deleted after 15 seconds
- Prevents the accumulation of unused channels

### 🔄 Data Persistence
- Channel owner data is saved in the `channels.json` file
- Management panels are automatically restored after bot restart

### 🛡️ Duplicate Protection
- Each user can only have one temporary channel
- Prevents creating multiple channels for the same user

---

## 🚀 Quick Start

### Requirements
- Python 3.8 or newer
- Discord bot token with appropriate permissions
- Discord server with administrator permissions

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/rAmfu/Discord-Voice-Channel-Creator.git
cd Discord-Voice-Channel-Creator
```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install discord.py
```

4. **Configure the bot:**
   - Open the `bot.py` file
   - Set your variables:
   ```python
   TOKEN = "your_bot_token"
   GUILD_ID = 123456789012345678  # Your server ID
   TRIGGER_CHANNEL_ID = 123456789012345678  # Trigger channel ID
   ```

5. **Run the bot:**
```bash
python bot.py
```

> **⚠️ IMPORTANT:** Always run the bot in a virtual environment! If you see `(venv)` before the username in the terminal, it means the environment is active.

### Required Bot Permissions
- `Manage Channels` - to create, edit, and delete channels
- `Connect` - to join voice channels
- `Move Members` - to move users between channels
- `Manage Permissions` - to set channel permissions
- `View Channels` - to see channels
- `Send Messages` - to send the management panel
- `Embed Links` - for displaying embeds
- `Voice Activity` - to monitor voice state

### Required Intents
- `guilds` - server information
- `members` - member details
- `voice_states` - voice activity tracking
- `message_content` - message handling

---

## 📦 Debian 12 Installation

### Step 1: System Update
```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Basic Tools
```bash
sudo apt install -y python3 python3-pip git python3-venv
```

### Step 3: Download the Bot
```bash
git clone https://github.com/rAmfu/Discord-Voice-Channel-Creator.git
cd Discord-Voice-Channel-Creator
```

### Step 4: Create Virtual Environment
```bash
python3 -m venv venv
```

### Step 5: Activate Environment and Install Dependencies
```bash
source venv/bin/activate
pip install discord.py
```

### Step 6: Configuration
```bash
nano bot.py
```
Enter your data:
```python
TOKEN = "your_bot_token"
GUILD_ID = 123456789012345678
TRIGGER_CHANNEL_ID = 123456789012345678
```

### Step 7: Run
```bash
python bot.py
```

### Important: How to Always Run the Bot in a Virtual Environment?

**Method 1: One Line**
```bash
source venv/bin/activate && python bot.py
```

**Method 2: Two Lines**
```bash
source venv/bin/activate
python bot.py
```

**Method 3: Direct Use of Python from venv**
```bash
./venv/bin/python bot.py
```

> **📌 Tip:** When the environment is active, you will see `(venv)` before the username in the terminal:
> ```bash
> (venv) user@server:~$
> ```

---

## 🔧 Running in the Background

### Method 1: Screen (recommended)
```bash
# Install screen (if you don't have it)
sudo apt install -y screen

# Run the bot in a screen session with virtual environment
screen -S voicebot
source venv/bin/activate && python bot.py

# Exit the session (bot continues running)
Ctrl+A, then D

# Return to the session
screen -r voicebot

# Stop the bot
Ctrl+C
```

### Method 2: Systemd (service)
```bash
# Create service file
sudo nano /etc/systemd/system/voicebot.service
```

Enter:
```ini
[Unit]
Description=Discord Voice Channel Bot
After=network.target

[Service]
Type=simple
User=bot-kick
WorkingDirectory=/home/bot-kick/Discord-Voice-Channel-Creator
ExecStart=/home/bot-kick/Discord-Voice-Channel-Creator/venv/bin/python /home/bot-kick/Discord-Voice-Channel-Creator/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# Activate the service
sudo systemctl daemon-reload
sudo systemctl enable voicebot
sudo systemctl start voicebot

# Service status
sudo systemctl status voicebot

# Logs
sudo journalctl -u voicebot -f
```

### Method 3: Tmux
```bash
# Install tmux
sudo apt install -y tmux

# Run
tmux new -s voicebot
source venv/bin/activate && python bot.py

# Exit
Ctrl+B, then D

# Return
tmux attach -t voicebot
```

### Method 4: Startup Script
```bash
# Create start.sh file
nano start.sh
```

Enter:
```bash
#!/bin/bash
cd /home/bot-kick/Discord-Voice-Channel-Creator
source venv/bin/activate
python bot.py
```

```bash
# Add permissions
chmod +x start.sh

# Run
./start.sh
```

---

## 🐳 Docker

### Docker Installation
```bash
sudo apt install -y docker.io docker-compose
```

### Creating Dockerfile
```bash
cat > Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

RUN pip install discord.py

COPY bot.py .
COPY channels.json .

CMD ["python", "bot.py"]
EOF
```

### Building and Running
```bash
# Build image
docker build -t voicebot .

# Run in background
docker run -d --name voicebot --restart unless-stopped voicebot

# Check logs
docker logs -f voicebot

# Stop
docker stop voicebot

# Remove container
docker rm voicebot
```

### Docker Compose
```bash
cat > docker-compose.yml << 'EOF'
version: '3'

services:
  voicebot:
    build: .
    container_name: voicebot
    restart: unless-stopped
    volumes:
      - ./channels.json:/app/channels.json
EOF
```

```bash
# Run
docker-compose up -d

# Logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## 📁 File Structure

```
Discord-Voice-Channel-Creator/
├── bot.py              # Main bot code
├── channels.json       # Channel owner data (created automatically)
├── LICENSE            # MIT License
├── README.md          # This file
├── venv/              # Virtual environment (created automatically)
├── Dockerfile         # For Docker (optional)
├── docker-compose.yml # For Docker Compose (optional)
├── requirements.txt   # Dependencies (optional)
└── start.sh           # Startup script (optional)
```

---

## 🎯 How It Works

1. **User joins** the trigger channel
2. **Bot creates** a new voice channel with the user's name
3. **User is moved** to their new channel
4. **Management panel appears** with embed and controls
5. **User can customize** their channel using the interactive menu
6. **When the channel is empty**, it is automatically deleted after 15 seconds

---

## 🔐 Security

- Only the channel owner can use the management panel
- Old owner loses all permissions after ownership transfer
- Permissions are automatically removed when deleting the channel

---

## 📝 Configuration

The bot uses three main configuration variables:

```python
TOKEN = "your_bot_token"
GUILD_ID = 123456789012345678
TRIGGER_CHANNEL_ID = 123456789012345678
```

### How to Find Server and Channel IDs?
1. Enable **Developer Mode** in Discord (Settings → Advanced → Developer Mode)
2. Right-click on the server → **Copy ID**
3. Right-click on the channel → **Copy ID**

---

## 🛠️ Technical Details

- Built using the [discord.py](https://github.com/Rapptz/discord.py) library
- Uses Discord UI Components (Buttons, Select Menus, Modals)
- Persistent views for panel restoration
- JSON data storage (no database required)
- Loop-based cleanup system (15-second interval)
- Event-based channel creation

---

## 🐛 Troubleshooting

### Problem: `ModuleNotFoundError: No module named 'discord'`
```bash
# Check if the environment is active
source venv/bin/activate

# Install discord.py
pip install discord.py

# Check installation
pip list | grep discord
```

### Problem: Bot doesn't connect to Discord
- Check if the token is correct
- Check if intents are enabled in the developer panel
- Check internet connection
- Check if the virtual environment is active

### Problem: Bot doesn't create channels
- Check if the bot has channel management permissions
- Check if the trigger channel exists
- Check bot logs

### Problem: Error 404 when deleting a channel
- Bot first sends a response, then deletes the channel
- If the error occurs, check if the channel has already been deleted

### Problem: Virtual environment doesn't work
```bash
# Check if venv is installed
python3 -m venv --help

# If not, install
sudo apt install python3-venv

# Create a new environment
rm -rf venv
python3 -m venv venv
```

---

## 🤝 Contributing

Contributions are welcome! If you have an idea for improvement, report it via [Issue](https://github.com/rAmfu/Discord-Voice-Channel-Creator/issues) or submit a [Pull Request](https://github.com/rAmfu/Discord-Voice-Channel-Creator/pulls).

1. Fork the project
2. Create your branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

For questions, problems, or suggestions, open an [Issue](https://github.com/rAmfu/Discord-Voice-Channel-Creator/issues) on GitHub.

---

## 🌟 Author

**rAmfu**
- GitHub: [@rAmfu](https://github.com/rAmfu)

---

**Created with ❤️ for the Discord community**
