
# EnrollSecure

## Project Overview

**EnrollSecure** is a Python-based login application that ensures secure access to computers for students. Upon starting the system, the application prompts students to enter their **enrollment number**. If the entered number matches a record in a JSON file, the student gains access. The login time is then logged in a CSV file for record-keeping.

## Features

- **Fullscreen** GUI application developed using **Tkinter**.
- Requests the student to enter their **enrollment number**.
- Validates the enrollment number against a **JSON file** with stored student data.
- Logs the **login time** (hour, minute, and second) into a **CSV file**.
- Displays **LNCT University** as the college name.
- Shows the **college logo** (`logo.png`).
- Prevents system access until the correct enrollment number is entered.

## How to Run

1. Clone the repository or download the project files.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
##Inspiration
The idea for this project came during a discussion with Professor Abhishek Dubey at LNCT University. The professor's insights on student login security inspired the development of this application to ensure that only authorized students can access the computer.

##Requirements
-Python 3.x
-Tkinter (for GUI)
-JSON file containing student data
-logo.png (college logo image)
