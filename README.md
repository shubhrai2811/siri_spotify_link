# 🎵 Siri Spotify Voice Control

> **Say it, Play it!** A smart macOS Siri Shortcut that lets you dictate any song, artist, album, or playlist and instantly opens it in your Spotify desktop app.

[![macOS](https://img.shields.io/badge/macOS-Compatible-blue.svg)](https://www.apple.com/macos/)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-green.svg)](https://www.python.org/)
[![Spotify API](https://img.shields.io/badge/Spotify-API-1DB954.svg)](https://developer.spotify.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

- 🎯 **Smart Search**: Finds tracks, albums, artists, and playlists
- 🖥️ **Desktop App Integration**: Opens directly in Spotify app (not web player)
- 🆓 **Free Account Compatible**: Works with both free and premium Spotify
- 🗣️ **Natural Voice Control**: Just say what you want to hear
- ⚡ **Lightning Fast**: Instant results with intelligent prioritization
- 🔒 **Secure**: Uses official Spotify OAuth2 authentication

---

## 🚀 How It Works

1. **Say**: _"Hey Siri, [Your Phrase]"_ (e.g., "Hey Siri, BJ")
2. **Siri asks**: _"What's the text?"_
3. **Dictate**: _"Bohemian Rhapsody by Queen"_ (or any song/artist/album)
4. **Listen**: Song opens instantly in your Spotify desktop app!

```
"Hey Siri, BJ" → "What's the text?" → "Shape of You Ed Sheeran" → 🎵 Plays immediately!
```

### Search Intelligence
- **Tracks First**: Finds specific songs
- **Albums Second**: Full album requests  
- **Artists Third**: Artist discography
- **Playlists Last**: Curated playlists

---

## 🛠️ Installation

### Prerequisites
- macOS with Shortcuts app
- Python 3.7 or higher
- Spotify desktop app installed
- Spotify Developer account (free)

### Step 1: Clone Repository
```bash
git clone https://github.com/shubhrai2811/siri_spotify_link.git
cd siri_spotify_link
```

### Step 2: Set Up Virtual Environment
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Spotify Developer Setup

1. **Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)**
2. **Click "Create App"**
3. **Fill in app details**:
   - App Name: `Siri Voice Control` (or any name)
   - App Description: `Voice control for Spotify`
   - Redirect URI: `http://127.0.0.1:8000/callback`
   - Which API/SDKs: `Web API`
4. **Save your app**
5. **Copy your credentials**:
   - Client ID
   - Client Secret

### Step 4: Configure Script

Open `spotify_voice.py` and update your credentials:

```python
client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "http://127.0.0.1:8000/callback"  # Keep this as-is
```

### Step 5: Create macOS Shortcut

1. **Open Shortcuts app** on your Mac
2. **Click the "+" to create new shortcut**
3. **Add these actions in order**:

   **Action 1: "Dictate Text"**
   - Search for "Dictate Text" and add it
   - This will capture your voice input
   
   **Action 2: "Run Shell Script"** 
   - Search for "Run Shell Script" and add it
   - Configure as follows:
     - **Shell**: `/bin/bash`
     - **Pass Input**: `as arguments`
     - **Script**: 
     ```bash
     cd /path/to/spotify_siri && source .venv/bin/activate && python siri_spotify_link/spotify_voice.py "$@"
     ```
     
     ⚠️ **Replace `/path/to/spotify_siri`** with your actual parent directory path. For example:
     ```bash
     cd /Users/prolevelnoob/CodePlayground/prsnl/spotify_siri && source .venv/bin/activate && python siri_spotify_link/spotify_voice.py "$@"
     ```

4. **Configure Siri Phrase**:
   - Click the settings icon in your shortcut
   - Add to Siri with a **unique, short phrase** that won't conflict with Siri commands
   - **Recommended phrases**: 
     - Your initials (e.g., "BJ", "AK", "SM")
     - A unique word (e.g., "Jam", "Vibe", "Tune")
     - A short code (e.g., "SP", "MX", "DJ")
   
   ⚠️ **AVOID these phrases**:
   - ❌ Anything with "Spotify" (triggers "Spotify hasn't added support")
   - ❌ "Play" or "Music" (conflicts with Apple Music)
   - ❌ "Run" or "Go" (may launch apps or maps)
   - ❌ Common commands like "Search", "Find", "Open"

5. **Name your shortcut**:
   - Give it any name you like (e.g., "Audio Control", "Voice DJ", etc.)
   - The name doesn't affect functionality

---

## 🎯 Usage Examples

| Voice Command | What It Finds |
|---------------|---------------|
| `"Blinding Lights"` | → Track by The Weeknd |
| `"Abbey Road Beatles"` | → The Beatles album |
| `"Taylor Swift"` | → Artist page |
| `"Today's Top Hits"` | → Spotify playlist |
| `"Bohemian Rhapsody Queen"` | → Specific track |

---

## 🔧 Troubleshooting

### Common Issues

**❌ "Permission denied" error**
```bash
chmod +x spotify_voice.py
```

**❌ "Spotify hasn't added support with Siri"**
- Your Siri phrase conflicts with built-in commands
- Try a different phrase like "Find song" or "Music search"

**❌ "ModuleNotFoundError: No module named 'spotipy'"**
- Make sure your virtual environment is activated
- Reinstall: `pip install spotipy`

**❌ Opens in web player instead of desktop app**
- Make sure Spotify desktop app is installed and running
- The script will auto-fallback to web if desktop isn't available

### First-Time Setup
- You'll need to authenticate with Spotify on first run
- A browser window will open for OAuth authorization
- Click "Agree" to grant permissions

---

## 🔒 Privacy & Security

- ✅ Uses official Spotify OAuth2 (no password storage)
- ✅ Credentials stored locally only
- ✅ No data sent to third parties
- ✅ Open source - audit the code yourself

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Found a bug or want to improve something? 

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⭐ Show Your Support

If this project helped you, please give it a ⭐ star on GitHub!

---

<div align="center">

**Made with ❤️ for music lovers who want Siri to actually work with Spotify**

[Report Bug](https://github.com/shubhrai2811/siri_spotify_link/issues) • [Request Feature](https://github.com/shubhrai2811/siri_spotify_link/issues)

</div>

