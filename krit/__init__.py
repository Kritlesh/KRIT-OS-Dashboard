"""
KRIT OS Dashboard
Local AI Desktop Assistant

A production-ready voice assistant with modern GUI dashboard
"""

__version__ = "1.0.0"
__author__ = "KRIT Development Team"
__license__ = "MIT"

from krit.core import KritCore
from krit.gui import KritGUI
from krit.stt import SpeechToText
from krit.tts import TextToSpeech
from krit.hotword import HotwordDetector

__all__ = [
    'KritCore',
    'KritGUI',
    'SpeechToText',
    'TextToSpeech',
    'HotwordDetector',
]