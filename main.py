import tkinter as tk
from tkinter import messagebox, PhotoImage
import json
import csv
import os
from datetime import datetime
import threading
import socket
import keyboard 

# Load student data
def load_students():
    with open("students.json", "r") as f:
        return json.load(f)

# Record login to CSV
def record_login(enrollment, name):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")  # 24-hour format
    with open("login_logs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP : " + ip,"NAME : "+ name,"ENROLLMENT : "+enrollment, "DATE : " + date_str,"TIME : " +time_str])

# Validate enrollment number
def validate():
    enrollment = entry.get().lower()
    if enrollment in students:
        name = students[enrollment]["name"]
        record_login(enrollment, name)
        root.destroy()  # Unlock the screen
    else:
        messagebox.showerror("Error", "❌ Invalid Enrollment Number")
        entry.delete(0, tk.END)

# Disable window close (Alt + F4)
def disable_event():
    pass

# Block certain key combinations
def block_keys():
    keys_to_block = ['alt+tab', 'ctrl+esc', 'alt+esc', 'alt+space']
    for key_combo in keys_to_block:
        keyboard.block_key(key_combo)


#get ip of the system
def get_ip():
    hostname = socket.gethostname()  # Get the machine's hostname
    ip_address = socket.gethostbyname(hostname)  # Get the corresponding IP address
    return ip_address

# Example usage:
ip = get_ip()
print(f"System IP Address: {ip}")

# Start key blocking in separate thread
keyblock_thread = threading.Thread(target=block_keys, daemon=True)
keyblock_thread.start()

# Initialize GUI
root = tk.Tk()
root.title("Student Login")
root.attributes('-fullscreen', True)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.bind("<Alt-F4>", lambda e: "break")

students = load_students()

frame = tk.Frame(root)
frame.pack(expand=True)

# College logo
if os.path.exists("logo.png"):
    logo = PhotoImage(file="logo.png")
    logo_label = tk.Label(frame, image=logo)
    logo_label.image = logo
    logo_label.pack(pady=10)

# College name
college_label = tk.Label(frame, text="LNCT University", font=("Arial", 28, "bold"), fg="blue")
college_label.pack(pady=10)

# Entry field
label = tk.Label(frame, text="Enter Your Enrollment Number", font=("Arial", 20))
label.pack(pady=10)

entry = tk.Entry(frame, font=("Arial", 18), justify='center')
entry.pack(pady=10)
entry.focus()

button = tk.Button(frame, text="Login", command=validate, font=("Arial", 16))
button.pack(pady=10)

root.mainloop()
