#!/usr/bin/env python3
"""
KRIT OS Dashboard - Local AI Desktop Assistant
Main entry point for the application
"""

import sys
import os
import logging
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from krit.core import KritCore
from krit.gui import KritGUI
import threading
import json

# Configure logging
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "krit.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class KritApplication:
    """Main application controller"""
    
    def __init__(self):
        """Initialize the KRIT application"""
        logger.info("Initializing KRIT OS Dashboard...")
        
        # Load configuration
        self.config = self.load_config()
        
        # Initialize core engine
        self.core = KritCore(self.config)
        
        # Initialize GUI
        self.gui = KritGUI(self.core, self.config)
        
        logger.info("KRIT initialized successfully")
    
    def load_config(self):
        """Load configuration from config.json"""
        config_path = PROJECT_ROOT / "config.json"
        
        if not config_path.exists():
            logger.warning("config.json not found, using defaults")
            return self.get_default_config()
        
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                logger.info("Configuration loaded successfully")
                return config
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return self.get_default_config()
    
    def get_default_config(self):
        """Return default configuration"""
        return {
            "hotword": "hey krit",
            "voice": {
                "engine": "pyttsx3",
                "rate": 175,
                "volume": 0.9
            },
            "stt": {
                "engine": "sphinx",
                "timeout": 5,
                "phrase_limit": 15
            },
            "ui": {
                "theme": "dark",
                "transparency": 0.95,
                "width": 1200,
                "height": 800
            },
            "plugins": {
                "auto_load": True,
                "directory": "krit/plugins"
            }
        }
    
    def start_voice_thread(self):
        """Start voice recognition in separate thread"""
        voice_thread = threading.Thread(
            target=self.core.start_listening,
            daemon=True,
            name="VoiceThread"
        )
        voice_thread.start()
        logger.info("Voice recognition thread started")
    
    def run(self):
        """Start the application"""
        try:
            logger.info("Starting KRIT OS Dashboard...")
            
            # Show splash screen
            self.gui.show_splash()
            
            # Start voice recognition thread
            self.start_voice_thread()
            
            # Start GUI main loop
            self.gui.run()
            
        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt, shutting down...")
            self.shutdown()
        except Exception as e:
            logger.critical(f"Fatal error: {e}", exc_info=True)
            self.shutdown()
    
    def shutdown(self):
        """Clean shutdown"""
        logger.info("Shutting down KRIT...")
        try:
            self.core.shutdown()
            self.gui.destroy()
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")
        finally:
            logger.info("KRIT shutdown complete")
            sys.exit(0)


def main():
    """Main entry point"""
    try:
        app = KritApplication()
        app.run()
    except Exception as e:
        logger.critical(f"Failed to start application: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()