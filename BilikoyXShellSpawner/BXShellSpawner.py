import os
import sys
import argparse
import tkinter as tk
from tkinter import messagebox
import webbrowser as w
import logging

##### BilikoyX Shell Spawner 1.1 #####

# Setup logging
logging.basicConfig(filename='shell_spawner.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Account links
telegram = "https://t.me/bilikoy"
github = "https://github.com/bilikoy"
facebook = "https://facebook.com/bilikoy"
whatsapp = "https://wa.me/bilikoy"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def spawn_shell(shell_type):
    logging.info(f"Attempting to spawn {shell_type} shell.")
    if shell_type == 'nt':
        print("Spawning NT-based shell (Windows)...")
        os.system("cmd")  # Windows Command Shell
    elif shell_type == 'posix':
        print("Spawning POSIX-based shell (Linux/MacOS)...")
        os.system("/bin/bash")  # Bash Shell
    elif shell_type == 'powershell':
        print("Spawning PowerShell...")
        os.system("powershell")  # PowerShell
    else:
        print("Invalid shell type.")
        logging.error("Invalid shell type specified.")

def show_support_links():
    clear_screen()
    messagebox.showinfo("Support Links", f"""
    THIS IS MY ACCOUNT LINK, PLEASE CONSIDER TO SUPPORT ME!
    -------------------------
    | TELEGRAM = {telegram} |
    | GITHUB = {github}   |
    | FACEBOOK = {facebook} |
    | WHATSAPP = {whatsapp} |
    -------------------------
    SUPPORT ME AND I WILL MAKE MORE ADVANCED SHELL-TERMINAL SPAWNER!
    """)

def on_spawn_shell(shell_var):
    shell_type = shell_var.get()
    if shell_type:
        spawn_shell(shell_type)
    else:
        messagebox.showwarning("Warning", "Please select an OS type.")

def run_gui():
    root = tk.Tk()
    root.title("BilikoyX Shell Spawner 1.1")
    root.geometry("400x300")

    tk.Label(root, text="Welcome to BilikoyX Shell Spawner!", font=("Helvetica", 14)).pack(pady=10)

    shell_var = tk.StringVar(value="")
    tk.Label(root, text="Select Your OS:", font=("Helvetica", 12)).pack(pady=5)
    tk.Radiobutton(root, text="Windows Command Shell", variable=shell_var, value="nt").pack(anchor="w")
    tk.Radiobutton(root, text="Linux/MacOS Bash Shell", variable=shell_var, value="posix").pack(anchor="w")
    tk.Radiobutton(root, text="PowerShell", variable=shell_var, value="powershell").pack(anchor="w")

    tk.Button(root, text="Spawn Shell", command=lambda: on_spawn_shell(shell_var)).pack(pady=20)
    tk.Button(root, text="Support Links", command=show_support_links).pack(pady=10)

    root.mainloop()

def print_banner():
    print("----------------------------")
    print(" BilikoyX Shell Spawner 1.1 ")
    print("----------------------------")

def print_shell_options():
    print("Available Shell Options:")
    print("1. nt - Windows Command Shell")
    print("2. posix - Linux/MacOS Bash Shell")
    print("3. powershell - PowerShell")
    print("4. help - Show this help")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BilikoyX Shell Spawner 1.1")
    parser.add_argument('-i', '--interface', action='store_true', help="Run in graphical interface mode.")
    parser.add_argument('-s', '--shell', choices=['nt', 'posix', 'powershell'], help="Specify the shell type: 'nt' for Windows, 'posix' for Linux/MacOS, or 'powershell' for PowerShell.")
    parser.add_argument('--support', action='store_true', help="Show social media links to support the project.")
    parser.add_argument('-b', '--banner', action='store_true', help="Print the banner.")
    parser.add_argument('--options', action='store_true', help="Show available shell options.")

    args = parser.parse_args()

    if args.banner:
        print_banner()
        sys.exit()

    if args.support:
        show_support_links()
        sys.exit()

    if args.options:
        print_shell_options()
        sys.exit()

    if args.interface:
        run_gui()
    elif args.shell:
        spawn_shell(args.shell)
    else:
        clear_screen()
        print("Select Your OS to spawn a shell:")
        print("(1) Windows Command Shell (nt)")
        print("(2) Linux/MacOS Bash Shell (posix)")
        print("(3) PowerShell (powershell)")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            spawn_shell('nt')
        elif choice == '2':
            spawn_shell('posix')
        elif choice == '3':
            spawn_shell('powershell')
        else:
            print("Invalid choice. Exiting.")
            logging.error("Invalid choice entered.")
            sys.exit()
