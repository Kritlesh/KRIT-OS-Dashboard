# 🚀 KRIT OS Dashboard - Quick Start Guide

Get up and running with KRIT in 5 minutes!

---

## ⚡ Super Quick Install (One Command)

### Windows
```bash
git clone https://github.com/yourusername/KRIT-OS-Dashboard.git && cd KRIT-OS-Dashboard && bash INSTALL.sh && bash run.sh
```

### Linux/macOS
```bash
git clone https://github.com/yourusername/KRIT-OS-Dashboard.git && cd KRIT-OS-Dashboard && chmod +x INSTALL.sh run.sh && ./INSTALL.sh && ./run.sh
```

---

## 📋 Step-by-Step Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/KRIT-OS-Dashboard.git
cd KRIT-OS-Dashboard
```

### Step 2: Run Installer
```bash
# Linux/macOS
chmod +x INSTALL.sh
./INSTALL.sh

# Windows (Git Bash)
bash INSTALL.sh
```

### Step 3: Start KRIT
```bash
# Linux/macOS
./run.sh

# Windows (Git Bash)
bash run.sh

# Or manually
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows
python main.py
```

---

## 🎤 First Time Usage

### 1. Launch Application
- Splash screen appears
- Wait for "Krit online" voice message
- Dashboard window opens

### 2. Test Microphone
Say: **"Hey Krit"**
- KRIT should respond: "Yes?"
- If no response, check microphone settings

### 3. Try Basic Commands

**Say**: "Hello"
**KRIT**: "Hello! How can I help you?"

**Say**: "What's today's date?"
**KRIT**: "Today is December 2nd, 2025"

**Say**: "Take a note meeting at 3pm"
**KRIT**: "Note saved: meeting at 3pm"

---

## 🎯 Essential Voice Commands

### Wake Up KRIT
```
"Hey Krit"  → Activates the assistant
```

### Quick Actions
```
"Hello"              → Greeting
"How are you?"       → Status check
"Thank you"          → Courtesy response
"What time is it?"   → Current time
"What's the date?"   → Current date
```

### Set Reminders
```
"Remind me to call John at 3pm"
"Set reminder to meeting in 30 minutes"
"List my reminders"
```

### Take Notes
```
"Take a note [your note content]"
"Read my notes"
"Search notes for meeting"
```

### Control Music
```
"Play music"
"Pause music"
"Volume up"
"Next song"
```

### Search Web
```
"Search Google for Python tutorials"
"Search YouTube for music"
"Open YouTube"
```

### Launch Apps
```
"Open Chrome"
"Launch Calculator"
"Start Terminal"
```

### System Control
```
"Lock screen"
"Sleep"
"Volume up"
"Brightness down"
```

---

## 🎨 Dashboard Overview

```
┌─────────────────────────────────────────────────────┐
│  KRIT OS Dashboard                                   │
├───────┬─────────────────────────────────────────────┤
│       │  System Status                               │
│ 🗓️    │  CPU: 45%  RAM: 62%  Disk: 78%              │
│ Cal   ├──────────────────────┬───────────────────────┤
│       │  Quick Notes         │  Calendar & Reminders │
│ 📝    │  • Meeting notes     │  📅 Dec 02, 2025      │
│ Notes │  • Todo list         │  ⏰ Team call - 10am  │
│       │                      │  ⏰ Lunch - 12pm      │
│ 🎵    ├──────────────────────┴───────────────────────┤
│ Music │  Console                                     │
│       │  [10:15:23] Krit online                      │
│ 🌐    │  [10:15:25] Listening for commands...       │
│ Web   │  [10:16:01] Command: take a note            │
│       │                                               │
│ ⚙️    │                                               │
│ System│                                               │
│       │                                               │
│ 🚀    │                                               │
│ Launch│                                               │
│       │                                               │
│ ●     │                                               │
│ Online│                                               │
└───────┴───────────────────────────────────────────────┘
```

### Sidebar Buttons
- **🗓️ Calendar**: Open calendar plugin
- **📝 Notes**: View and manage notes
- **🎵 Music**: Music controls
- **🌐 Web**: Web search interface
- **⚙️ System**: System settings
- **🚀 Launch**: App launcher

---

## ⚙️ Quick Configuration

### Change Wake Word
Edit `config.json`:
```json
{
  "hotword": "hey assistant"
}
```

### Adjust Voice Speed
```json
{
  "voice": {
    "rate": 150
  }
}
```
(100 = slow, 175 = normal, 250 = fast)

### Change Theme Colors
Edit `krit/gui.py`:
```python
self.colors = {
    'bg': '#1a1a2e',           # Dark blue background
    'accent': '#0f3460',       # Accent color
    'success': '#06ffa5',      # Green highlights
}
```

---

## 🔧 Troubleshooting

### Microphone Not Detected

**Linux**:
```bash
# List audio devices
arecord -l

# Test recording
arecord -d 3 test.wav
aplay test.wav
```

**Windows**:
- Settings → Privacy → Microphone → Allow apps
- Right-click speaker icon → Recording devices → Enable microphone

### "Module not found" Error

```bash
# Reinstall dependencies
source venv/bin/activate
pip install --force-reinstall -r requirements.txt
```

### Low Volume or No Sound

**Check TTS Volume**:
Edit `config.json`:
```json
{
  "voice": {
    "volume": 0.9
  }
}
```

### Hotword Not Working

1. **Speak clearly**: "Hey Krit" with slight pause between words
2. **Check logs**: `logs/krit.log`
3. **Adjust sensitivity**: Edit `krit/hotword.py`

```python
self.recognizer.energy_threshold = 3000  # Try different values
```

---

## 📱 Usage Tips

### Best Practices

1. **Speak Naturally**: No need for robot voice
2. **Pause After Wake Word**: Wait for "Yes?" response
3. **One Command at a Time**: Break complex tasks into steps
4. **Use Specific Keywords**: "open chrome" not "launch browser"
5. **Check Console**: Monitor activity in dashboard console

### Voice Recognition Tips

- **Quiet Environment**: Reduces false positives
- **Clear Pronunciation**: Especially for wake word
- **Moderate Volume**: Not too loud or soft
- **Consistent Distance**: Stay 1-2 feet from mic

---

## 🚦 System Requirements

### Minimum
- **CPU**: Dual-core 1.5 GHz
- **RAM**: 2 GB
- **Storage**: 500 MB
- **OS**: Windows 10, Ubuntu 20.04, macOS 11

### Recommended
- **CPU**: Quad-core 2.0 GHz
- **RAM**: 4 GB
- **Storage**: 1 GB
- **Microphone**: USB or built-in
- **Speakers**: Any output device

---

## 📚 Next Steps

### Customize KRIT
1. **Add Custom Commands**: See [Plugin Development](README.md#plugin-development)
2. **Modify GUI**: Edit `krit/gui.py`
3. **Configure Apps**: Edit `data/launcher_config.json`

### Explore Features
1. **Try All Plugins**: Test each sidebar button
2. **Set Daily Reminders**: Build your schedule
3. **Take Voice Notes**: Document ideas hands-free
4. **Control System**: Use voice for common tasks

### Learn More
- **Full Documentation**: [README.md](README.md)
- **Plugin Guide**: [PLUGIN_GUIDE.md](docs/PLUGIN_GUIDE.md)
- **Architecture**: [ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## 🆘 Getting Help

### Documentation
- [README.md](README.md) - Complete documentation
- [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) - Common issues
- [VOICE_COMMANDS.md](docs/VOICE_COMMANDS.md) - All commands

### Support Channels
- **GitHub Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas
- **Email**: support@krit-os.dev

### Community
- Share your custom plugins
- Contribute improvements
- Help other users

---

## ✅ Quick Checklist

Before asking for help, verify:

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Dependencies installed (`pip list`)
- [ ] Microphone working (test with system recorder)
- [ ] Virtual environment activated (`which python`)
- [ ] Config file exists (`config.json`)
- [ ] Logs checked (`logs/krit.log`)

---

<div align="center">

**🎉 Congratulations! You're ready to use KRIT OS!**

Say "Hey Krit" and start commanding your computer with your voice!

</div>