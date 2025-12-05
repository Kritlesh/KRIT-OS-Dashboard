"""
Hotword Detection
Listens for wake word "Hey Krit"
"""

import logging
import speech_recognition as sr
from typing import Optional

logger = logging.getLogger(__name__)


class HotwordDetector:
    """Hotword detection using speech recognition"""
    
    def __init__(self, hotword: str = "hey krit"):
        """
        Initialize hotword detector
        
        Args:
            hotword: Wake word to listen for
        """
        self.hotword = hotword.lower()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.running = False
        
        # Configure recognizer for hotword detection
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        
        # Calibrate
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            logger.info(f"Hotword detector initialized for '{self.hotword}'")
        except Exception as e:
            logger.error(f"Failed to initialize hotword detector: {e}")
    
    def detect(self, timeout: Optional[int] = None) -> bool:
        """
        Listen for hotword
        
        Args:
            timeout: Maximum time to wait (None for indefinite)
        
        Returns:
            True if hotword detected, False otherwise
        """
        try:
            with self.microphone as source:
                # Listen for audio
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=3
                )
                
                # Quick recognition using sphinx (offline)
                try:
                    text = self.recognizer.recognize_sphinx(audio)
                    text = text.lower().strip()
                    
                    # Check for hotword
                    if self.hotword in text or \
                       "hey chris" in text or \
                       "hey crit" in text or \
                       "a creek" in text:  # Common misrecognitions
                        logger.info(f"Hotword detected: '{text}'")
                        return True
                    
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    pass
                
                return False
                
        except sr.WaitTimeoutError:
            return False
        except Exception as e:
            logger.debug(f"Hotword detection error: {e}")
            return False
    
    def start_background_detection(self, callback):
        """
        Start background hotword detection
        
        Args:
            callback: Function to call when hotword detected
        """
        def audio_callback(recognizer, audio):
            try:
                text = recognizer.recognize_sphinx(audio)
                text = text.lower().strip()
                
                if self.hotword in text or \
                   "hey chris" in text or \
                   "hey crit" in text:
                    callback()
                    
            except:
                pass
        
        # Start background listening
        self.running = True
        stop_listening = self.recognizer.listen_in_background(
            self.microphone,
            audio_callback,
            phrase_time_limit=3
        )
        
        logger.info("Background hotword detection started")
        return stop_listening
    
    def shutdown(self):
        """Cleanup resources"""
        self.running = False
        logger.info("Hotword detector shutdown")