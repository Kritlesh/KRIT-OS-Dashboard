"""
Application Launcher Plugin
Voice-controlled app launching
"""

import logging
import platform
import subprocess
import json
from pathlib import Path

logger = logging.getLogger(__name__)


class LauncherPlugin:
    """Application launcher plugin"""
    
    name = "App Launcher"
    version = "1.0.0"
    commands = ["open", "launch", "start", "run"]
    
    def __init__(self, core):
        """Initialize launcher plugin"""
        self.core = core
        self.system = platform.system()
        self.config_file = Path("data/launcher_config.json")
        
        # Load or create launcher config
        self.apps = self.load_config()
        
        logger.info("Launcher plugin initialized")
    
    def load_config(self):
        """Load launcher configuration"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load launcher config: {e}")
        
        # Default configurations by platform
        return self.get_default_apps()
    
    def get_default_apps(self):
        """Get default application paths by platform"""
        if self.system == "Windows":
            return {
                "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
                "edge": "microsoft-edge:",
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "paint": "mspaint.exe",
                "explorer": "explorer.exe",
                "cmd": "cmd.exe",
                "powershell": "powershell.exe",
                "vscode": "code",
                "word": "WINWORD.EXE",
                "excel": "EXCEL.EXE",
                "outlook": "OUTLOOK.EXE",
                "spotify": "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Spotify\\Spotify.exe",
                "discord": "C:\\Users\\%USERNAME%\\AppData\\Local\\Discord\\app-*\\Discord.exe",
            }
        elif self.system == "Linux":
            return {
                "chrome": "google-chrome",
                "firefox": "firefox",
                "terminal": "gnome-terminal",
                "files": "nautilus",
                "calculator": "gnome-calculator",
                "text": "gedit",
                "vscode": "code",
                "spotify": "spotify",
                "discord": "discord",
            }
        elif self.system == "Darwin":
            return {
                "chrome": "open -a 'Google Chrome'",
                "safari": "open -a Safari",
                "firefox": "open -a Firefox",
                "terminal": "open -a Terminal",
                "finder": "open -a Finder",
                "calculator": "open -a Calculator",
                "textedit": "open -a TextEdit",
                "vscode": "open -a 'Visual Studio Code'",
                "spotify": "open -a Spotify",
                "discord": "open -a Discord",
            }
        
        return {}
    
    def save_config(self):
        """Save launcher configuration"""
        try:
            self.config_file.parent.mkdir(exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.apps, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save launcher config: {e}")
    
    def handle_command(self, text):
        """Handle launcher commands"""
        text = text.lower()
        
        # Extract app name
        for trigger in ["open", "launch", "start", "run"]:
            if trigger in text:
                app_name = text.replace(trigger, "").strip()
                self.launch_app(app_name)
                return
        
        self.core.speak("Which application would you like to open?")
    
    def launch_app(self, app_name):
        """Launch an application by name"""
        app_name = app_name.lower().strip()
        
        # Try to find app in config
        app_path = None
        
        for name, path in self.apps.items():
            if name in app_name or app_name in name:
                app_path = path
                break
        
        if not app_path:
            # Try common variations
            if "browser" in app_name:
                app_path = self.apps.get("chrome") or self.apps.get("firefox")
            elif "code" in app_name or "vs code" in app_name:
                app_path = self.apps.get("vscode")
            elif "file" in app_name:
                app_path = self.apps.get("explorer") or self.apps.get("files") or self.apps.get("finder")
        
        if app_path:
            try:
                self.execute_app(app_path)
                self.core.speak(f"Opening {app_name}")
                logger.info(f"Launched app: {app_name}")
            except Exception as e:
                logger.error(f"Failed to launch {app_name}: {e}")
                self.core.speak(f"Sorry, I couldn't open {app_name}")
        else:
            # Try to launch by name directly
            try:
                self.execute_app(app_name)
                self.core.speak(f"Opening {app_name}")
            except Exception as e:
                logger.error(f"App not found: {app_name}")
                self.core.speak(f"I don't know how to open {app_name}. You can add it to the launcher config.")
    
    def execute_app(self, app_path):
        """Execute application"""
        if self.system == "Windows":
            if app_path.endswith('.exe') or app_path.endswith('.com'):
                subprocess.Popen(app_path, shell=True)
            else:
                subprocess.Popen(f"start {app_path}", shell=True)
                
        elif self.system == "Linux":
            subprocess.Popen(app_path, shell=True)
            
        elif self.system == "Darwin":
            if app_path.startswith("open"):
                subprocess.Popen(app_path, shell=True)
            else:
                subprocess.Popen(f"open -a '{app_path}'", shell=True)
    
    def add_app(self, name, path):
        """Add new app to launcher"""
        self.apps[name.lower()] = path
        self.save_config()
        logger.info(f"Added app to launcher: {name}")
    
    def remove_app(self, name):
        """Remove app from launcher"""
        name = name.lower()
        if name in self.apps:
            del self.apps[name]
            self.save_config()
            logger.info(f"Removed app from launcher: {name}")
            return True
        return False
    
    def list_apps(self):
        """List all configured apps"""
        return list(self.apps.keys())
    
    def shutdown(self):
        """Shutdown plugin"""
        logger.info("Shutting down launcher plugin")
        self.save_config()