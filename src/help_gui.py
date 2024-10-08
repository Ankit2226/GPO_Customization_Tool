import tkinter as tk
from tkinter import ttk

class HelpGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="Help & Documentation", font=("Arial", 24))
        self.label.pack(pady=20)

        self.help_text = tk.Text(self, height=15, width=60)
        self.help_text.pack(pady=10)

        self.help_text.insert(tk.END, "This tool helps manage GPO compliance...\n")
