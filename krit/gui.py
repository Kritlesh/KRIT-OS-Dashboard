"""
KRIT GUI Dashboard
Modern desktop interface with dark theme
"""

import logging
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
import psutil
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class KritGUI:
    """Main dashboard GUI"""
    
    def __init__(self, core, config):
        """Initialize GUI"""
        self.core = core
        self.config = config
        self.root = None
        self.splash = None
        
        # Colors - Dark theme
        self.colors = {
            'bg': '#1a1a2e',
            'bg_secondary': '#16213e',
            'accent': '#0f3460',
            'accent_light': '#533483',
            'text': '#eaeaea',
            'text_secondary': '#94a1b2',
            'success': '#06ffa5',
            'warning': '#ffd32a',
            'danger': '#ff4757'
        }
        
        logger.info("GUI initialized")
    
    def show_splash(self):
        """Show splash screen with loading animation"""
        self.splash = tk.Tk()
        self.splash.title("KRIT OS")
        self.splash.geometry("400x300")
        self.splash.configure(bg=self.colors['bg'])
        self.splash.overrideredirect(True)
        
        # Center window
        self.splash.update_idletasks()
        x = (self.splash.winfo_screenwidth() // 2) - 200
        y = (self.splash.winfo_screenheight() // 2) - 150
        self.splash.geometry(f"400x300+{x}+{y}")
        
        # Logo/Title
        title = tk.Label(
            self.splash,
            text="KRIT OS",
            font=("Arial", 36, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['success']
        )
        title.pack(pady=50)
        
        # Subtitle
        subtitle = tk.Label(
            self.splash,
            text="Local AI Desktop Assistant",
            font=("Arial", 12),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        )
        subtitle.pack()
        
        # Loading indicator
        self.loading_label = tk.Label(
            self.splash,
            text="Initializing...",
            font=("Arial", 10),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        self.loading_label.pack(pady=30)
        
        # Progress animation
        self.progress_bar = ttk.Progressbar(
            self.splash,
            length=300,
            mode='indeterminate'
        )
        self.progress_bar.pack()
        self.progress_bar.start(10)
        
        # Schedule main window
        self.splash.after(3000, self.show_main_window)
        
        self.splash.mainloop()
    
    def show_main_window(self):
        """Show main dashboard window"""
        if self.splash:
            self.splash.destroy()
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("KRIT OS Dashboard")
        
        # Window size
        width = self.config.get('ui', {}).get('width', 1200)
        height = self.config.get('ui', {}).get('height', 800)
        self.root.geometry(f"{width}x{height}")
        self.root.configure(bg=self.colors['bg'])
        
        # Create main layout
        self.create_layout()
        
        # Start system monitor
        self.start_system_monitor()
        
        logger.info("Main window displayed")
    
    def create_layout(self):
        """Create main dashboard layout"""
        # Sidebar
        self.create_sidebar()
        
        # Main content area
        self.main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top row - System stats
        self.create_system_stats()
        
        # Middle row - Notes and Calendar
        middle_frame = tk.Frame(self.main_frame, bg=self.colors['bg'])
        middle_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.create_notes_viewer(middle_frame)
        self.create_calendar_widget(middle_frame)
        
        # Bottom row - Terminal
        self.create_terminal()
    
    def create_sidebar(self):
        """Create sidebar with plugin buttons"""
        sidebar = tk.Frame(self.root, bg=self.colors['bg_secondary'], width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        sidebar.pack_propagate(False)
        
        # Title
        title = tk.Label(
            sidebar,
            text="KRIT",
            font=("Arial", 24, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['success']
        )
        title.pack(pady=20)
        
        # Plugin buttons
        plugins = [
            ("🗓️ Calendar", self.open_calendar),
            ("📝 Notes", self.open_notes),
            ("🎵 Music", self.open_music),
            ("🌐 Web", self.open_web),
            ("⚙️ System", self.open_system),
            ("🚀 Launch", self.open_launcher),
        ]
        
        for text, command in plugins:
            btn = tk.Button(
                sidebar,
                text=text,
                font=("Arial", 11),
                bg=self.colors['accent'],
                fg=self.colors['text'],
                activebackground=self.colors['accent_light'],
                activeforeground=self.colors['text'],
                border=0,
                cursor="hand2",
                command=command
            )
            btn.pack(fill=tk.X, padx=10, pady=5)
        
        # Status indicator
        self.status_label = tk.Label(
            sidebar,
            text="● Online",
            font=("Arial", 10),
            bg=self.colors['bg_secondary'],
            fg=self.colors['success']
        )
        self.status_label.pack(side=tk.BOTTOM, pady=20)
    
    def create_system_stats(self):
        """Create system statistics display"""
        stats_frame = tk.LabelFrame(
            self.main_frame,
            text="System Status",
            font=("Arial", 12, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text'],
            bd=2
        )
        stats_frame.pack(fill=tk.X, pady=5)
        
        # Create stat labels
        self.cpu_label = self.create_stat_label(stats_frame, "CPU: 0%")
        self.ram_label = self.create_stat_label(stats_frame, "RAM: 0%")
        self.disk_label = self.create_stat_label(stats_frame, "Disk: 0%")
        self.net_label = self.create_stat_label(stats_frame, "Network: 0 KB/s")
    
    def create_stat_label(self, parent, text):
        """Create a stat label"""
        label = tk.Label(
            parent,
            text=text,
            font=("Arial", 10),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text']
        )
        label.pack(side=tk.LEFT, padx=20, pady=10)
        return label
    
    def create_notes_viewer(self, parent):
        """Create notes viewer"""
        notes_frame = tk.LabelFrame(
            parent,
            text="Quick Notes",
            font=("Arial", 11, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text']
        )
        notes_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.notes_text = scrolledtext.ScrolledText(
            notes_frame,
            bg=self.colors['accent'],
            fg=self.colors['text'],
            font=("Courier", 10),
            insertbackground=self.colors['text'],
            wrap=tk.WORD
        )
        self.notes_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Load notes
        self.load_notes()
    
    def create_calendar_widget(self, parent):
        """Create calendar and reminders"""
        cal_frame = tk.LabelFrame(
            parent,
            text="Calendar & Reminders",
            font=("Arial", 11, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text']
        )
        cal_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Date display
        date_label = tk.Label(
            cal_frame,
            text=datetime.now().strftime("%B %d, %Y"),
            font=("Arial", 14, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['success']
        )
        date_label.pack(pady=10)
        
        # Reminders list
        self.reminders_text = scrolledtext.ScrolledText(
            cal_frame,
            bg=self.colors['accent'],
            fg=self.colors['text'],
            font=("Arial", 10),
            height=10,
            wrap=tk.WORD
        )
        self.reminders_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.load_reminders()
    
    def create_terminal(self):
        """Create mini terminal console"""
        term_frame = tk.LabelFrame(
            self.main_frame,
            text="Console",
            font=("Arial", 11, "bold"),
            bg=self.colors['bg_secondary'],
            fg=self.colors['text']
        )
        term_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.terminal = scrolledtext.ScrolledText(
            term_frame,
            bg='#000000',
            fg='#00ff00',
            font=("Courier", 9),
            height=8,
            insertbackground='#00ff00'
        )
        self.terminal.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.log("KRIT OS Terminal v1.0")
        self.log(f"System started at {datetime.now().strftime('%H:%M:%S')}")
        self.log("Listening for commands...")
    
    def start_system_monitor(self):
        """Start background thread for system monitoring"""
        def monitor():
            while True:
                try:
                    # Update stats
                    cpu = psutil.cpu_percent(interval=1)
                    ram = psutil.virtual_memory().percent
                    disk = psutil.disk_usage('/').percent
                    net = psutil.net_io_counters()
                    
                    # Update labels
                    self.cpu_label.config(text=f"CPU: {cpu}%")
                    self.ram_label.config(text=f"RAM: {ram}%")
                    self.disk_label.config(text=f"Disk: {disk}%")
                    self.net_label.config(
                        text=f"Network: {net.bytes_sent // 1024} KB/s"
                    )
                    
                except Exception as e:
                    logger.error(f"Monitor error: {e}")
                
                time.sleep(2)
        
        monitor_thread = threading.Thread(target=monitor, daemon=True)
        monitor_thread.start()
    
    def log(self, message):
        """Add message to terminal"""
        if self.terminal:
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.terminal.insert(tk.END, f"[{timestamp}] {message}\n")
            self.terminal.see(tk.END)
    
    def load_notes(self):
        """Load notes from file"""
        notes_file = Path("data/notes.txt")
        if notes_file.exists():
            try:
                self.notes_text.delete(1.0, tk.END)
                self.notes_text.insert(1.0, notes_file.read_text())
            except Exception as e:
                logger.error(f"Failed to load notes: {e}")
    
    def load_reminders(self):
        """Load reminders"""
        self.reminders_text.insert(tk.END, "No reminders set.\n")
        self.reminders_text.insert(tk.END, "Say 'remind me to...' to add one!")
    
    # Plugin window methods
    def open_calendar(self):
        self.log("Opening Calendar plugin...")
    
    def open_notes(self):
        self.log("Opening Notes plugin...")
    
    def open_music(self):
        self.log("Opening Music plugin...")
    
    def open_web(self):
        self.log("Opening Web plugin...")
    
    def open_system(self):
        self.log("Opening System Control plugin...")
    
    def open_launcher(self):
        self.log("Opening App Launcher...")
    
    def run(self):
        """Start GUI main loop"""
        if self.root:
            logger.info("Starting GUI main loop")
            self.root.mainloop()
    
    def destroy(self):
        """Destroy GUI"""
        if self.root:
            self.root.quit()
            self.root.destroy()
        logger.info("GUI destroyed")