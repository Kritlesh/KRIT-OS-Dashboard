# 🤖 KRIT OS Dashboard - Local AI Desktop Assistant

<div align="center">

![KRIT OS](https://img.shields.io/badge/KRIT-OS%20v1.0-success?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A production-ready JARVIS-like voice assistant with modern GUI dashboard**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Commands](#-voice-commands) • [Plugins](#-plugin-development)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Voice Commands](#-voice-commands)
- [Plugin Development](#-plugin-development)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

KRIT OS Dashboard is a fully-featured, production-ready local AI desktop assistant inspired by JARVIS. It provides:

- **Offline Voice Recognition** - Works without internet connection
- **Hotword Detection** - Always listening for "Hey Krit"
- **Modern GUI Dashboard** - Beautiful dark-themed interface with system monitoring
- **Plugin Architecture** - Easily extensible with custom plugins
- **Cross-Platform** - Windows, Linux, and macOS support

---

## ✨ Features

### 🎤 Voice Capabilities
- **Hotword Activation**: "Hey Krit" to wake up the assistant
- **Offline STT**: PocketSphinx for complete privacy
- **Natural Language Commands**: Speak naturally, no rigid syntax
- **Text-to-Speech**: Smooth voice responses

### 🖥️ Dashboard Interface
- **System Monitor**: Real-time CPU, RAM, Disk, and Network stats
- **Notes Viewer**: Quick access to voice notes
- **Calendar & Reminders**: Voice-activated scheduling
- **Mini Terminal**: Command console with logs
- **Plugin Sidebar**: Quick access to all features

### 🔌 Built-in Plugins

#### 📅 Calendar & Reminders
- Set reminders by voice
- Background reminder checker
- Popup notifications
- Daily schedule management

#### 📝 Notes
- Voice note-taking
- Read notes aloud
- Search functionality
- Persistent JSON storage

#### 🎵 Music Control
- Play/pause/stop music
- Volume control
- Media key integration
- Cross-platform support

#### 🌐 Web Search
- Google search
- YouTube search
- Website shortcuts
- Direct URL opening

#### ⚙️ System Control
- Shutdown/restart
- Sleep/hibernate
- Lock screen
- Volume & brightness control

#### 🚀 App Launcher
- Voice app launching
- Configurable app paths
- Cross-platform launchers

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         KRIT OS                              │
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │   GUI Layer  │    │  Voice Layer │    │ Plugin System│ │
│  │  (Tkinter)   │◄───┤   (STT/TTS)  │◄───┤   (Dynamic)  │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
│         │                    │                    │         │
│         └────────────────────┼────────────────────┘         │
│                              │                              │
│                     ┌────────▼────────┐                     │
│                     │   Core Engine   │                     │
│                     │  Command Router │                     │
│                     └────────┬────────┘                     │
│                              │                              │
│         ┌────────────────────┼────────────────────┐         │
│         │                    │                    │         │
│  ┌──────▼──────┐    ┌────────▼────────┐   ┌──────▼──────┐ │
│  │  Calendar   │    │     Notes       │   │   Music     │ │
│  │   Plugin    │    │     Plugin      │   │   Plugin    │ │
│  └─────────────┘    └─────────────────┘   └─────────────┘ │
│                                                              │
│  ┌─────────────┐    ┌─────────────┐      ┌─────────────┐  │
│  │ Web Search  │    │   System    │      │     App     │  │
│  │   Plugin    │    │   Control   │      │  Launcher   │  │
│  └─────────────┘    └─────────────┘      └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Microphone
- Speakers/Headphones

### Windows Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/KRIT-OS-Dashboard.git
cd KRIT-OS-Dashboard

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install PyAudio (Windows)
pip install pipwin
pipwin install pyaudio

# 5. Run KRIT
python main.py
```

### Linux Installation (Debian/Ubuntu)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/KRIT-OS-Dashboard.git
cd KRIT-OS-Dashboard

# 2. Install system dependencies
sudo apt-get update
sudo apt-get install -y python3-pyaudio portaudio19-dev \
    espeak-ng alsa-utils libasound2-dev

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Run KRIT
python main.py
```

### Arch Linux Installation

```bash
# 1. Install dependencies
sudo pacman -S python-pyaudio portaudio espeak-ng alsa-utils

# 2. Clone and setup
git clone https://github.com/yourusername/KRIT-OS-Dashboard.git
cd KRIT-OS-Dashboard
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Run KRIT
python main.py
```

### macOS Installation

```bash
# 1. Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install dependencies
brew install portaudio

# 3. Clone and setup
git clone https://github.com/yourusername/KRIT-OS-Dashboard.git
cd KRIT-OS-Dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Run KRIT
python main.py
```

---

## 🚀 Usage

### Starting KRIT

```bash
# Activate virtual environment
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Run application
python main.py
```

### First Run

1. **Splash Screen** appears with loading animation
2. **Voice Calibration** - Adjusts for ambient noise
3. **Dashboard Opens** - Main interface with all features
4. **KRIT says**: "Krit online."
5. **Say**: "Hey Krit" to activate

### Basic Workflow

1. **Activate**: Say "Hey Krit"
2. **Wait**: Listen for "Yes?"
3. **Command**: Speak your command naturally
4. **Response**: KRIT executes and responds

---

## 🗣️ Voice Commands

### General Commands

```
"Hey Krit"                  # Wake word
"Hello"                     # Greeting
"How are you?"              # Status check
"Thank you"                 # Courtesy
"Exit" / "Quit"             # Close KRIT
```

### 📅 Calendar & Reminders

```
"Remind me to call John at 3pm"
"Set reminder to meeting in 30 minutes"
"What's today's date?"
"List my reminders"
"Clear all reminders"
```

### 📝 Notes

```
"Take a note [your note]"
"Write note [content]"
"Read my notes"
"Search notes for [keyword]"
"Delete last note"
```

### 🎵 Music Control

```
"Play music"
"Pause music"
"Stop music"
"Next song"
"Previous song"
"Volume up"
"Volume down"
"Mute"
```

### 🌐 Web Search

```
"Search Google for [query]"
"Search YouTube for [query]"
"Open YouTube"
"Open Google"
"Open GitHub"
"Go to facebook.com"
```

### ⚙️ System Control

```
"Shutdown"
"Restart"
"Sleep"
"Lock screen"
"Brightness up"
"Brightness down"
"Volume up"
"Volume down"
```

### 🚀 App Launcher

```
"Open Chrome"
"Open Firefox"
"Open VS Code"
"Launch Calculator"
"Start Terminal"
"Open File Explorer"
```

---

## 🔌 Plugin Development

### Creating a Custom Plugin

1. **Create Plugin File**: `krit/plugins/my_plugin.py`

```python
import logging

logger = logging.getLogger(__name__)

class MyPlugin:
    """My custom plugin"""
    
    name = "My Plugin"
    version = "1.0.0"
    commands = ["keyword1", "keyword2"]  # Trigger words
    
    def __init__(self, core):
        """Initialize plugin"""
        self.core = core
        logger.info(f"{self.name} initialized")
    
    def handle_command(self, text):
        """Handle voice commands"""
        text = text.lower()
        
        if "keyword1" in text:
            self.do_something()
        elif "keyword2" in text:
            self.do_something_else()
        else:
            self.core.speak("I can help with...")
    
    def do_something(self):
        """Your custom functionality"""
        self.core.speak("Doing something!")
        logger.info("Did something")
    
    def do_something_else(self):
        """More functionality"""
        self.core.speak("Doing something else!")
    
    def shutdown(self):
        """Cleanup when plugin shuts down"""
        logger.info(f"{self.name} shutdown")
```

2. **Plugin Features**:
   - **Auto-loaded** on startup
   - Access to **core.speak()** for TTS
   - Access to **core.listen()** for STT
   - Persistent storage in `data/` directory

3. **Best Practices**:
   - Use descriptive command keywords
   - Handle errors gracefully
   - Log important actions
   - Clean up resources in shutdown()

---

## ⚙️ Configuration

### config.json

```json
{
  "hotword": "hey krit",
  "voice": {
    "engine": "pyttsx3",
    "rate": 175,
    "volume": 0.9
  },
  "stt": {
    "engine": "sphinx",  // Options: sphinx, google, vosk
    "timeout": 5,
    "phrase_limit": 15
  },
  "ui": {
    "theme": "dark",
    "width": 1200,
    "height": 800
  }
}
```

### Customization Options

- **Hotword**: Change wake word
- **Voice Rate**: Adjust TTS speed (100-300)
- **Volume**: Set TTS volume (0.0-1.0)
- **STT Engine**: Choose recognition engine
- **UI Size**: Adjust window dimensions

---

## 📦 Building Executables

### Windows Executable

```bash
cd installers
./build_windows_exe.sh
# Output: dist/KRIT-OS.exe
```

### Linux .deb Package

```bash
cd installers
chmod +x build_deb_package.sh
./build_deb_package.sh
# Output: krit-os_1.0.0_amd64.deb
```

### AppImage (Universal Linux)

```bash
cd installers
# Edit appimage_builder.yml if needed
appimage-builder --recipe appimage_builder.yml
# Output: KRIT-OS-x86_64.AppImage
```

---

## 🐛 Troubleshooting

### Microphone Not Working

**Windows**:
```bash
# Check microphone permissions
Settings > Privacy > Microphone > Allow apps
```

**Linux**:
```bash
# Test microphone
arecord -l
# Fix permissions
sudo usermod -a -G audio $USER
```

### Voice Recognition Issues

1. **Check ambient noise**: Calibrate in quiet environment
2. **Adjust threshold**: Modify `energy_threshold` in config
3. **Try different engine**: Switch from sphinx to google

### Import Errors

```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Install system packages (Linux)
sudo apt-get install python3-pyaudio portaudio19-dev
```

### GUI Not Showing

```bash
# Check display
echo $DISPLAY  # Linux

# Reinstall tk
sudo apt-get install python3-tk  # Linux
```

### Performance Issues

1. **Lower UI refresh rate**
2. **Disable unused plugins**
3. **Reduce logging level**
4. **Use lightweight STT engine**

---

## 📸 Screenshots

```
┌───────────────────────────────────────────────────────────────┐
│  KRIT OS                                                       │
├───────┬───────────────────────────────────────────────────────┤
│       │  System Status                                         │
│ 🗓️    │  CPU: 45%  RAM: 62%  Disk: 78%  Network: 1.2 MB/s    │
│       ├───────────────────────────────────────────────────────┤
│ 📝    │  Quick Notes              │  Calendar & Reminders     │
│       │  ─────────────            │  ───────────────────      │
│ 🎵    │  Meeting notes...         │  December 02, 2025        │
│       │  Project ideas...         │                           │
│ 🌐    │                           │  ⏰ Team standup - 10am   │
│       │                           │  ⏰ Client call - 2pm     │
│ ⚙️    │                           │                           │
│       ├───────────────────────────────────────────────────────┤
│ 🚀    │  Console                                               │
│       │  ─────────────────────────────────────────────────────│
│ ●     │  [10:15:23] KRIT OS Terminal v1.0                     │
│ Online│  [10:15:24] System started                            │
│       │  [10:15:25] Listening for commands...                 │
└───────┴───────────────────────────────────────────────────────┘
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Development Setup

```bash
# Install development dependencies
pip install pytest black flake8

# Run tests
pytest tests/

# Format code
black krit/

# Lint code
flake8 krit/
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **PocketSphinx** - Offline speech recognition
- **pyttsx3** - Text-to-speech synthesis
- **SpeechRecognition** - Unified STT interface
- **psutil** - System monitoring

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/KRIT-OS-Dashboard/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/KRIT-OS-Dashboard/discussions)
- **Email**: ytkritlesh@gmail.com

---

<div align="center">

**Made with ❤️ by the KRIT Development Team**

⭐ Star us on GitHub — it motivates us a lot!

</div>
