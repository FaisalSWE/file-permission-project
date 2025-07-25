# file-permission-project
# File Permissions and chmod Automation

## Table of Contents
- [Project Overview](#project-overview)  
- [Task Description](#task-description)  
- [Files Included](#files-included)  
- [Setup and Usage](#setup-and-usage)  
- [Notes](#notes)  
- [Author](#author)  

---

## Project Overview
This project focuses on understanding Linux file permissions and visually representing their logic through a flowchart. It also demonstrates how to programmatically change file permissions using a Python script.

---

## Description
-  the concepts of Linux file permissions (`r`, `w`, `x`) for user, group, and others.  
-  flowchart to illustrate the permission bits and how they control access.  
-  Python script that applies the permission mode `rwxrwxr-x` (octal `777`) to a specified file using the `os.chmod()` function.

---

## Files Included
- `set_permission.py` — Python script to change file permissions.  
- `flowchart.png` — Flowchart image explaining file permissions.  
- `README.md` — Project documentation.

---

## Setup and Usage

1. Place the target file (e.g., `example.py`) in the same directory as `set_permission.py`, or update the filename/path in the script accordingly.

2. Run the Python script:
   ```bash
   python set_permission.py

3. The script sets the file permissions to `rwxrwxr-x` (775) and prints a confirmation message, e.g.:
   ```bash
   Permissions changed to rwxrwxr-x (777) for: example.py
   ```
## Notes

- The script uses Python's os.chmod() function and should work on Linux/Unix systems natively.
- On Windows, permission behavior may differ but the script will run without error.
- Make sure you have the appropriate rights to change file permissions on the target file.
