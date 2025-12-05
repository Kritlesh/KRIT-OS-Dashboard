# 🎤 KRIT OS - Complete Voice Commands Reference

This document contains every voice command supported by KRIT OS Dashboard.

---

## 🔊 Wake Word

**Primary**: `"Hey Krit"`

**Alternatives** (detected as variations):
- "Hey Chris"
- "Hey Crit"
- "A Creek" (common misrecognition)

**Response**: "Yes?"

---

## 💬 General Conversation

### Greetings
| Command | Response |
|---------|----------|
| "Hello" | "Hello! How can I help you?" |
| "Hi" | "Hello! How can I help you?" |
| "Good morning" | "Hello! How can I help you?" |

### Status Checks
| Command | Response |
|---------|----------|
| "How are you?" | "I'm functioning optimally, thank you!" |
| "Are you there?" | "Yes, I'm here!" |
| "What can you do?" | Explains capabilities |

### Courtesy
| Command | Response |
|---------|----------|
| "Thank you" | "You're welcome!" |
| "Thanks" | "You're welcome!" |

### Exit
| Command | Action |
|---------|--------|
| "Exit" | Closes KRIT |
| "Quit" | Closes KRIT |
| "Goodbye" | Says goodbye and exits |

---

## 📅 Calendar & Reminders Plugin

### Set Reminders

#### Time-Based Reminders
```
"Remind me to [task] at [time]"

Examples:
- "Remind me to call John at 3pm"
- "Remind me to meeting at 2:30"
- "Remind me to take medicine at 9am"
```

#### Relative Time Reminders
```
"Remind me to [task] in [duration]"

Examples:
- "Remind me to check email in 30 minutes"
- "Remind me to leave in 2 hours"
- "Remind me to workout in 1 hour"
```

#### Quick Reminders
```
"Remind me to [task]"  → Sets reminder for 5 minutes

Example:
- "Remind me to check the oven"
```

### View Reminders
| Command | Action |
|---------|--------|
| "List my reminders" | Reads all active reminders |
| "Show reminders" | Reads all active reminders |
| "What are my reminders?" | Reads all active reminders |

### Date Information
| Command | Response |
|---------|----------|
| "What's today?" | Speaks current date |
| "What's the date?" | Speaks current date |
| "Today's date" | Speaks current date |

### Clear Reminders
| Command | Action |
|---------|--------|
| "Clear reminders" | Removes all reminders |
| "Delete all reminders" | Removes all reminders |
| "Clear all reminders" | Removes all reminders |

---

## 📝 Notes Plugin

### Create Notes

#### Direct Notes
```
"Take a note [content]"

Examples:
- "Take a note meeting with Bob at 3pm"
- "Take a note buy milk and eggs"
- "Take a note project deadline Friday"
```

#### Interactive Notes
```
"Take a note"  → Prompts for content
"Write note"   → Prompts for content
"Save note"    → Prompts for content
```

### Read Notes
| Command | Action |
|---------|--------|
| "Read my notes" | Reads last 3 notes |
| "Show notes" | Reads last 3 notes |
| "List notes" | Reads last 3 notes |

### Search Notes
```
"Search notes for [keyword]"

Examples:
- "Search notes for meeting"
- "Find note about project"
- "Search notes for Bob"
```

### Delete Notes
| Command | Action |
|---------|--------|
| "Delete last note" | Removes most recent note |
| "Clear last note" | Removes most recent note |

---

## 🎵 Music Control Plugin

### Playback Control
| Command | Action |
|---------|--------|
| "Play music" | Starts/resumes playback |
| "Start music" | Starts/resumes playback |
| "Pause music" | Pauses playback |
| "Pause" | Pauses playback |
| "Stop music" | Stops playback |
| "Stop" | Stops playback |

### Track Navigation
| Command | Action |
|---------|--------|
| "Next song" | Skips to next track |
| "Skip" | Skips to next track |
| "Previous song" | Goes to previous track |
| "Last song" | Goes to previous track |

### Volume Control
| Command | Action |
|---------|--------|
| "Volume up" | Increases volume |
| "Volume down" | Decreases volume |
| "Mute" | Mutes audio |

---

## 🌐 Web Search Plugin

### Google Search
```
"Search Google for [query]"
"Google search [query]"

Examples:
- "Search Google for Python tutorials"
- "Google search weather forecast"
- "Search Google for best restaurants nearby"
```

### YouTube Search
```
"Search YouTube for [query]"
"YouTube search [query]"

Examples:
- "Search YouTube for music videos"
- "YouTube search cooking recipes"
- "Search YouTube for workout videos"
```

### Open Websites

#### Common Shortcuts
| Command | Opens |
|---------|-------|
| "Open YouTube" | youtube.com |
| "Open Google" | google.com |
| "Open Gmail" | mail.google.com |
| "Open Facebook" | facebook.com |
| "Open Twitter" | twitter.com |
| "Open Reddit" | reddit.com |
| "Open GitHub" | github.com |
| "Open Stack Overflow" | stackoverflow.com |
| "Open Wikipedia" | wikipedia.org |
| "Open Amazon" | amazon.com |
| "Open Netflix" | netflix.com |

#### Custom URLs
```
"Open website [url]"
"Go to [url]"

Examples:
- "Open website example.com"
- "Go to github.com"
```

---

## ⚙️ System Control Plugin

### Power Management
| Command | Action | Delay |
|---------|--------|-------|
| "Shutdown" | Shuts down computer | 10 seconds |
| "Shut down" | Shuts down computer | 10 seconds |
| "Restart" | Restarts computer | 10 seconds |
| "Reboot" | Restarts computer | 10 seconds |
| "Sleep" | Puts computer to sleep | Immediate |
| "Hibernate" | Hibernates computer | Immediate |

### Screen Lock
| Command | Action |
|---------|--------|
| "Lock screen" | Locks the screen |
| "Lock" | Locks the screen |

### Brightness Control
| Command | Action |
|---------|--------|
| "Brightness up" | Increases screen brightness |
| "Brightness down" | Decreases screen brightness |

### Volume Control
| Command | Action |
|---------|--------|
| "Volume up" | Increases system volume |
| "Volume down" | Decreases system volume |

---

## 🚀 App Launcher Plugin

### Launch Applications

#### Web Browsers
| Command | Launches |
|---------|----------|
| "Open Chrome" | Google Chrome |
| "Open Firefox" | Mozilla Firefox |
| "Open Edge" | Microsoft Edge |
| "Open Safari" | Safari (macOS) |

#### System Apps
| Command | Launches |
|---------|----------|
| "Open Calculator" | Calculator app |
| "Launch Calculator" | Calculator app |
| "Open Notepad" | Notepad (Windows) |
| "Open Paint" | Paint (Windows) |
| "Open Terminal" | Terminal/Command Prompt |
| "Open File Explorer" | File Manager |
| "Open Files" | File Manager (Linux) |
| "Open Finder" | Finder (macOS) |

#### Development Tools
| Command | Launches |
|---------|----------|
| "Open VS Code" | Visual Studio Code |
| "Open Code" | Visual Studio Code |

#### Office Apps
| Command | Launches |
|---------|----------|
| "Open Word" | Microsoft Word |
| "Open Excel" | Microsoft Excel |
| "Open Outlook" | Microsoft Outlook |

#### Communication
| Command | Launches |
|---------|----------|
| "Open Spotify" | Spotify |
| "Open Discord" | Discord |

### Generic Launcher
```
"Open [app name]"
"Launch [app name]"
"Start [app name]"
"Run [app name]"

Examples:
- "Open Steam"
- "Launch Photoshop"
- "Start Slack"
```

---

## 🎯 Command Patterns

### Time Formats Supported
- **12-hour**: "3pm", "10am", "2:30pm"
- **24-hour**: "15:00", "22:30"
- **Relative**: "in 30 minutes", "in 2 hours", "in 1 day"

### Duration Formats
- **Minutes**: "30 minutes", "5 mins"
- **Hours**: "2 hours", "1 hour"
- **Days**: "2 days", "1 day"

### Keywords Recognized
- **Time**: at, in, by, before, after
- **Action**: remind, note, open, play, search
- **Navigation**: next, previous, back, forward
- **Control**: up, down, on, off, start, stop

---

## 🔄 Command Flow

### Typical Interaction
```
User: "Hey Krit"
KRIT: "Yes?"
User: "Remind me to call John at 3pm"
KRIT: "Reminder set: call John at 3:00 PM"
```

### Multi-Step Commands
```
User: "Hey Krit"
KRIT: "Yes?"
User: "Take a note"
KRIT: "What would you like to note?"
User: "Meeting with team tomorrow"
KRIT: "Note saved: Meeting with team tomorrow"
```

---

## 📊 Command Categories Summary

| Category | Commands | Examples |
|----------|----------|----------|
| General | 8 | Hello, Thanks, Exit |
| Calendar | 12 | Reminders, Date |
| Notes | 8 | Take note, Read notes |
| Music | 10 | Play, Pause, Volume |
| Web | 20+ | Search, Open websites |
| System | 10 | Shutdown, Lock, Volume |
| Launcher | 30+ | Open apps |
| **Total** | **~100** | |

---

## 💡 Tips for Better Recognition

### DO:
- ✅ Speak clearly and naturally
- ✅ Use complete phrases
- ✅ Wait for "Yes?" before commanding
- ✅ Use specific keywords
- ✅ Speak at normal volume

### DON'T:
- ❌ Rush commands
- ❌ Use slang or abbreviations
- ❌ Command while KRIT is speaking
- ❌ Speak too loudly or softly
- ❌ Combine multiple commands

---

## 🔊 Voice Recognition Settings

### Adjust Sensitivity
Edit `krit/stt.py`:
```python
self.recognizer.energy_threshold = 4000  # Higher = less sensitive
```

### Adjust Timeout
Edit `config.json`:
```json
{
  "stt": {
    "timeout": 5,        // Maximum wait time
    "phrase_limit": 15   // Maximum phrase length
  }
}
```

---

## 🆕 Adding Custom Commands

See [PLUGIN_GUIDE.md](docs/PLUGIN_GUIDE.md) for creating custom plugins with new commands.

### Quick Example
```python
class MyPlugin:
    commands = ["weather", "forecast"]
    
    def handle_command(self, text):
        if "weather" in text:
            self.core.speak("Checking weather...")
```

---

## 🐛 Command Not Working?

### Troubleshooting Steps

1. **Check Console**: Look for recognition in dashboard console
2. **Check Logs**: `logs/krit.log` shows what was recognized
3. **Test Microphone**: Say "Hey Krit" first
4. **Adjust Volume**: Speak clearly at normal volume
5. **Check Plugin**: Ensure relevant plugin is loaded

### Common Issues

| Issue | Solution |
|-------|----------|
| Hotword not detected | Adjust `energy_threshold` |
| Commands misunderstood | Speak more clearly |
| No response | Check microphone permissions |
| Wrong action | Use exact command keywords |

---

<div align="center">

**📖 For more help, see [README.md](README.md) or [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)**

</div>