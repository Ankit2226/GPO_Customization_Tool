import tkinter as tk
from tkinter import ttk

class GpoDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        label = tk.Label(self, text="Welcome to the GPO Compliance Tool", font=("Arial", 24))
        label.pack(pady=20)

        self.summary_label = tk.Label(self, text="Compliance Summary", font=("Arial", 16))
        self.summary_label.pack(pady=10)

        self.status_label = tk.Label(self, text="Total GPOs: 0, Compliant: 0, Non-compliant: 0", font=("Arial", 12))
        self.status_label.pack(pady=10)
