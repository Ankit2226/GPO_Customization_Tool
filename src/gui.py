import tkinter as tk
from gpo_dashboard import GpoDashboard
from gpo_scanner_gui import GpoScannerGUI
from compliance_checker import ComplianceChecker
from report_generator_gui import ReportGeneratorGUI
from gpo_management_gui import GpoManagementGUI
from gpo_deployment_gui import GpoDeploymentGUI
from settings_gui import SettingsGUI
from help_gui import HelpGUI

def create_gui():
    root = tk.Tk()
    root.title("GPO Compliance Tool")

    # Create a notebook for tabbed interface
    notebook = tk.ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create and add frames for each screen
    dashboard_frame = GpoDashboard(notebook)
    scanner_frame = GpoScannerGUI(notebook)
    compliance_frame = ComplianceChecker(notebook)
    report_frame = ReportGeneratorGUI(notebook)
    management_frame = GpoManagementGUI(notebook)
    deployment_frame = GpoDeploymentGUI(notebook)
    settings_frame = SettingsGUI(notebook)
    help_frame = HelpGUI(notebook)

    # Add frames to the notebook
    notebook.add(dashboard_frame, text="Dashboard")
    notebook.add(scanner_frame, text="GPO Scanner")
    notebook.add(compliance_frame, text="Compliance Checker")
    notebook.add(report_frame, text="Report Generator")
    notebook.add(management_frame, text="GPO Management")
    notebook.add(deployment_frame, text="GPO Deployment")
    notebook.add(settings_frame, text="Settings")
    notebook.add(help_frame, text="Help")

    root.mainloop()
