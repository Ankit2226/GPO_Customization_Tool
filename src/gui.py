import tkinter as tk
from tkinter import ttk  # For the progress bar
import psutil  # For system information like RAM, storage
from gpo_scanner import scan_gpo
from cis_checker import check_cis_compliance
from report_generator import generate_pdf_report
import platform

def fetch_system_info():
    # Fetching system name, RAM, and storage details
    system_name = platform.node()
    ram = psutil.virtual_memory().total // (1024 ** 3)  # RAM in GB
    storage = psutil.disk_usage('/').total // (1024 ** 3)  # Storage in GB
    return system_name, ram, storage

def fetch_memory_info():
    # Get memory usage information
    mem = psutil.virtual_memory()
    total_memory = mem.total // (1024 ** 3)  # Convert to GB
    used_memory = mem.used // (1024 ** 3)    # Convert to GB
    memory_percent = mem.percent  # Percentage of used memory
    return total_memory, used_memory, memory_percent

def fetch_storage_info():
    # Get storage usage information
    disk = psutil.disk_usage('/')
    total_storage = disk.total // (1024 ** 3)  # Convert to GB
    used_storage = disk.used // (1024 ** 3)    # Convert to GB
    storage_percent = disk.percent  # Percentage of used storage
    return total_storage, used_storage, storage_percent

def create_gui():
    def on_scan():
        gpo_list = scan_gpo()
        compliance_report = check_cis_compliance(gpo_list)
        generate_pdf_report(compliance_report, "output/compliance_report.pdf")

    root = tk.Tk()
    root.title("GPO Customization Tool")
    root.geometry("600x500")  # Set width and height of the window

    # Fetch system, memory, and storage info
    system_name, ram, _ = fetch_system_info()
    total_memory, used_memory, memory_percent = fetch_memory_info()
    total_storage, used_storage, storage_percent = fetch_storage_info()

    # Title and Description
    title_label = tk.Label(root, text="GPO Customization Tool", font=("Arial", 20))
    title_label.pack(pady=10)

    description_label = tk.Label(root, text="Customize and check GPO compliance based on CIS Benchmark")
    description_label.pack(pady=5)

    # Display system info
    system_info_frame = tk.Frame(root)
    system_info_frame.pack(pady=10)

    system_name_label = tk.Label(system_info_frame, text=f"System Name: {system_name}", font=("Arial", 12))
    system_name_label.grid(row=0, column=0, padx=10)

    ram_label = tk.Label(system_info_frame, text=f"RAM: {ram} GB", font=("Arial", 12))
    ram_label.grid(row=1, column=0, padx=10)

    # Memory usage section
    memory_frame = tk.Frame(root)
    memory_frame.pack(pady=10)

    memory_label = tk.Label(memory_frame, text=f"Memory Usage: {used_memory} GB / {total_memory} GB", font=("Arial", 12))
    memory_label.grid(row=0, column=0, padx=10)

    # Progress bar for memory
    memory_progress = ttk.Progressbar(memory_frame, length=400, mode='determinate')
    memory_progress.grid(row=1, column=0, padx=10)
    memory_progress['value'] = memory_percent  # Set progress based on memory usage

    # Memory percentage label
    memory_percent_label = tk.Label(memory_frame, text=f"{memory_percent}%", font=("Arial", 12))
    memory_percent_label.grid(row=1, column=1, padx=10)

    # Storage usage section
    storage_frame = tk.Frame(root)
    storage_frame.pack(pady=20)

    storage_label = tk.Label(storage_frame, text=f"Storage Usage: {used_storage} GB / {total_storage} GB", font=("Arial", 12))
    storage_label.grid(row=0, column=0, padx=10)

    # Progress bar for storage
    storage_progress = ttk.Progressbar(storage_frame, length=400, mode='determinate')
    storage_progress.grid(row=1, column=0, padx=10)
    storage_progress['value'] = storage_percent  # Set progress based on storage usage

    # Storage percentage label
    storage_percent_label = tk.Label(storage_frame, text=f"{storage_percent}%", font=("Arial", 12))
    storage_percent_label.grid(row=1, column=1, padx=10)

    # Scan button
    scan_button = tk.Button(root, text="Scan GPO", command=on_scan, width=20, height=2, bg='lightblue', font=("Arial", 12))
    scan_button.pack(pady=20)

    # Exit button
    exit_button = tk.Button(root, text="Exit", command=root.quit, width=20, height=2, bg='lightcoral', font=("Arial", 12))
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
