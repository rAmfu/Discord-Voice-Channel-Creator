# 🎤 Discord Voice Channel Creator

🌍 Language: **English** | [Polski](README.md) 🔄 Version: **Node-js** | [Python](https://github.com/rAmfu/Discord-Voice-Channel-Creator/README_EN.md)

  A Discord bot for automatic creation and management of temporary voice channels. Built with Node.js and discord.js v14.

  
  
  

## ✨ Features

  

- 🚀 **Auto-create channels** – When a user joins the trigger channel, the bot automatically creates a voice channel for them.

- 👑 **Management panel** – Each channel owner receives an interactive embed panel.
- 🔒 **Privacy management** – Switch between public and private channels.
- 👥 **Access management** – Add or remove access for selected users.
- ✏️ **Customization** – Change name, description, and user limit.
- 👑 **Ownership transfer** – Transfer the channel to another user.
- 🚫 **Moderation** – Kick and ban users.
- 🗑️ **Auto-cleanup** – Automatically delete empty channels.
- 🔄 **Refresh** – Button to manually update the panel.

  
  
  

## 📋 Requirements

  

- Node.js v16.9.0 or higher
- Discord bot with proper permissions
- Discord server with a trigger channel

  
  
  

## 🚀 Installation

  

### 1. Clone the repository

```
git  clone  https://github.com/your-username/temporary-voice-bot.git
cd  temporary-voice-bot
```

  

### 2. Install dependencies

```bash
npm  install
```

  

### 3. Create a `.env` file in the root directory

```
BOT_TOKEN=your_bot_token
GUILD_ID=your_server_id
TRIGGER_CHANNEL_ID=your_trigger_channel_id
```

  

### 4. Folder structure

```
temporary-voice-bot/
├── src/
│ └── bot.js
├── channels.json
└── .env
```

  
  
  

## 🤖 Bot Configuration

  

### 1. Create a bot on the Discord Developer Portal

- Go to [Discord Developer Portal](https://discord.com/developers/applications)
- Click "New Application" and enter a name
- Go to the "Bot" tab
- Click "Add Bot" and confirm
- Copy the **TOKEN** – needed for the `.env` file

  

### 2. Enable intents

In the "Bot" tab, enable:
- ✅ Presence Intent
- ✅ Server Members Intent
- ✅ Message Content Intent

  

### 3. Invite the bot to your server

In the "OAuth2" → "URL Generator" tab:
- Select "bot" and "applications.commands"
- Select the following permissions:
- Manage Channels
- Move Members
- Connect
- Speak
- View Channel
- Manage Roles
- Copy the generated URL and open it in your browser

  

### 4. Get server and channel IDs

- Enable **Developer Mode** in Discord (Settings → Advanced)
- Right-click your server → "Copy ID"
- Right-click the trigger channel → "Copy ID"

  
  
  

## 🎯 Bot Permissions

  

The bot requires the following permissions:

-  `Manage Channels` – create and delete channels
-  `Move Members` – move users between channels
-  `Connect` – join voice channels
-  `Speak` – speak in voice channels
-  `View Channel` – see channels
-  `Manage Roles` – edit channel permissions

  
  
  

## 🚀 Running the Bot

  

```
node  src/bot.js
```

 

Or with nodemon (for development):

```
npm  install  -g  nodemon
nodemon  src/bot.js
```

  
  
  

## 📁 File Structure

  

```
temporary-voice-bot/
├── src/
│ └── bot.js # Main bot file
├── channels.json # Channel owner data (auto-generated)
├── .env # Environment variables
├── package.json # Dependencies
└── README.md # This documentation
```

  
  
  

## 🔧 Environment Variables

  

| Variable | Description | Example |
|--|--|--|
| `BOT_TOKEN` | Discord bot token | `MTIzNDU2Nzg5MDEyMzQ1Njc4OQ.G...` |
| `GUILD_ID` | Discord server ID | `123456789012345678` |
| `TRIGGER_CHANNEL_ID` | Trigger channel ID | `123456789012345678` |

  
  
  

## 🎮 How to Use

  

1.  **Join the trigger channel** – The bot will automatically create a channel for you.
2.  **Management panel** – After creation, an embed panel appears.
3.  **Manage your channel** – Use the dropdown menu to:
- Set user limit
- Toggle public/private
- Change name
- Change description
- Transfer ownership
- Add/Remove access
- Kick/Ban users
- Delete the channel

  
  
  

## 📸 Management Panel Example

  

```
🎤 Your Channel Panel
👑 Owner: @User
🔊 Channel name: 🎤 Name
👥 Users in channel: • @User1 • @User2
👤 Users with access: 🔒 Only the owner has access
ℹ️ Info: • Limit: 5 • Status: 🔒 Private
⚙️ Management: Use the menu below to manage the channel.
```

  
  
  

## 🛠️ Troubleshooting

  

### Bot does not respond

- Check if the token in `.env` is correct
- Ensure the bot has the proper permissions
- Check the console logs

  

### Channel is not created

- Verify that `TRIGGER_CHANNEL_ID` is correct
- Ensure the trigger channel has a category (parent)
- Check that the bot has `Manage Channels` permission

  

### Error: "Application did not respond"

- The bot uses `deferReply()` for slower operations
- Check your internet connection
- Restart the bot

  
  
  

## 📝 License

  

MIT License – free to use

  
  
  

## 👨‍💻 Author

  

rAmfu – [GitHub](https://github.com/rAmfu)
rAmfu - [Portfolio](https://ramfu.ovh)

  
  
  

## ⭐ Acknowledgments

  
- [discord.js](https://discord.js.org/) – Discord library
- All contributors

  
  
  

**NOTE:** Bot requires Node.js v16.9.0 or higher!
