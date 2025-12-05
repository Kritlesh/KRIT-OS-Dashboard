"""
Calendar & Reminder Plugin
Voice-activated calendar and reminder system
"""

import logging
import json
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path
from tkinter import messagebox

logger = logging.getLogger(__name__)


class CalendarPlugin:
    """Calendar and reminder management plugin"""
    
    name = "Calendar & Reminders"
    version = "1.0.0"
    commands = ["remind", "reminder", "calendar", "schedule", "appointment"]
    
    def __init__(self, core):
        """Initialize calendar plugin"""
        self.core = core
        self.data_file = Path("data/reminders.json")
        self.data_file.parent.mkdir(exist_ok=True)
        
        self.reminders = self.load_reminders()
        
        # Start background reminder checker
        self.running = True
        self.checker_thread = threading.Thread(
            target=self._reminder_checker,
            daemon=True,
            name="ReminderChecker"
        )
        self.checker_thread.start()
        
        logger.info("Calendar plugin initialized")
    
    def load_reminders(self):
        """Load reminders from file"""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load reminders: {e}")
        return []
    
    def save_reminders(self):
        """Save reminders to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.reminders, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save reminders: {e}")
    
    def handle_command(self, text):
        """Handle calendar commands"""
        text = text.lower()
        
        if "remind me" in text or "set reminder" in text:
            self.set_reminder(text)
        elif "list reminder" in text or "show reminder" in text:
            self.list_reminders()
        elif "clear reminder" in text or "delete reminder" in text:
            self.clear_reminders()
        elif "what's today" in text or "today's date" in text:
            self.tell_date()
        else:
            self.core.speak("I can help you set reminders and check your calendar.")
    
    def set_reminder(self, text):
        """Set a new reminder from voice command"""
        try:
            # Parse reminder text
            # Example: "remind me to call John at 3pm"
            # Example: "remind me to meeting in 30 minutes"
            
            if "at" in text:
                # Time-based reminder
                parts = text.split("at")
                task = parts[0].replace("remind me to", "").strip()
                time_str = parts[1].strip()
                
                # Parse time (simplified)
                reminder_time = self.parse_time(time_str)
                
            elif "in" in text:
                # Relative time reminder
                parts = text.split("in")
                task = parts[0].replace("remind me to", "").strip()
                duration = parts[1].strip()
                
                # Parse duration
                reminder_time = self.parse_duration(duration)
            else:
                # Immediate reminder
                task = text.replace("remind me to", "").replace("set reminder", "").strip()
                reminder_time = datetime.now() + timedelta(minutes=5)
            
            # Create reminder
            reminder = {
                'id': len(self.reminders) + 1,
                'task': task,
                'time': reminder_time.isoformat(),
                'created': datetime.now().isoformat(),
                'active': True
            }
            
            self.reminders.append(reminder)
            self.save_reminders()
            
            time_str = reminder_time.strftime("%I:%M %p")
            self.core.speak(f"Reminder set: {task} at {time_str}")
            logger.info(f"Reminder created: {task} at {time_str}")
            
        except Exception as e:
            logger.error(f"Failed to set reminder: {e}")
            self.core.speak("Sorry, I couldn't set that reminder. Please try again.")
    
    def parse_time(self, time_str):
        """Parse time string to datetime"""
        # Simplified time parsing
        # TODO: Implement robust time parsing
        now = datetime.now()
        
        if "pm" in time_str:
            hour = int(time_str.split("pm")[0].strip())
            if hour != 12:
                hour += 12
        elif "am" in time_str:
            hour = int(time_str.split("am")[0].strip())
        else:
            hour = int(time_str.split(":")[0])
        
        return now.replace(hour=hour, minute=0, second=0, microsecond=0)
    
    def parse_duration(self, duration_str):
        """Parse duration string to datetime"""
        now = datetime.now()
        
        if "minute" in duration_str:
            minutes = int(''.join(filter(str.isdigit, duration_str)))
            return now + timedelta(minutes=minutes)
        elif "hour" in duration_str:
            hours = int(''.join(filter(str.isdigit, duration_str)))
            return now + timedelta(hours=hours)
        elif "day" in duration_str:
            days = int(''.join(filter(str.isdigit, duration_str)))
            return now + timedelta(days=days)
        
        return now + timedelta(minutes=30)
    
    def list_reminders(self):
        """List all active reminders"""
        active = [r for r in self.reminders if r['active']]
        
        if not active:
            self.core.speak("You have no reminders.")
            return
        
        self.core.speak(f"You have {len(active)} reminder{'s' if len(active) > 1 else ''}.")
        
        for reminder in active[:3]:  # Speak first 3
            time_obj = datetime.fromisoformat(reminder['time'])
            time_str = time_obj.strftime("%I:%M %p")
            self.core.speak(f"{reminder['task']} at {time_str}")
    
    def clear_reminders(self):
        """Clear all reminders"""
        count = len([r for r in self.reminders if r['active']])
        
        if count == 0:
            self.core.speak("You have no reminders to clear.")
            return
        
        for reminder in self.reminders:
            reminder['active'] = False
        
        self.save_reminders()
        self.core.speak(f"Cleared {count} reminder{'s' if count > 1 else ''}.")
    
    def tell_date(self):
        """Tell current date"""
        now = datetime.now()
        date_str = now.strftime("%A, %B %d, %Y")
        self.core.speak(f"Today is {date_str}")
    
    def _reminder_checker(self):
        """Background thread to check reminders"""
        while self.running:
            try:
                now = datetime.now()
                
                for reminder in self.reminders:
                    if not reminder['active']:
                        continue
                    
                    reminder_time = datetime.fromisoformat(reminder['time'])
                    
                    # Check if reminder time has passed
                    if now >= reminder_time:
                        self.trigger_reminder(reminder)
                        reminder['active'] = False
                        self.save_reminders()
                
                time.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                logger.error(f"Reminder checker error: {e}")
                time.sleep(60)
    
    def trigger_reminder(self, reminder):
        """Trigger a reminder notification"""
        logger.info(f"Triggering reminder: {reminder['task']}")
        
        # Speak reminder
        self.core.speak(f"Reminder: {reminder['task']}")
        
        # Show popup notification
        try:
            messagebox.showinfo(
                "KRIT Reminder",
                f"⏰ {reminder['task']}",
            )
        except Exception as e:
            logger.error(f"Failed to show notification: {e}")
    
    def shutdown(self):
        """Shutdown plugin"""
        logger.info("Shutting down calendar plugin")
        self.running = False
        if self.checker_thread.is_alive():
            self.checker_thread.join(timeout=2)