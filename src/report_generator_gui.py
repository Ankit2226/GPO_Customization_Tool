import tkinter as tk
from tkinter import ttk
from report_generator import generate_pdf_report

class ReportGeneratorGUI(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="Report Generator", font=("Arial", 24))
        self.label.pack(pady=20)

        self.generate_button = tk.Button(self, text="Generate Report", command=self.generate_report)
        self.generate_button.pack(pady=10)

        self.result_area = tk.Text(self, height=15, width=60)
        self.result_area.pack(pady=10)

    def generate_report(self):
        self.result_area.insert(tk.END, "Generating report...\n")
        compliance_report = []  # Replace with actual report data
        output_file = "compliance_report.pdf"
        generate_pdf_report(compliance_report, output_file)
        self.result_area.insert(tk.END, f"Report saved as {output_file}\n")
