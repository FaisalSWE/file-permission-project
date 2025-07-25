#set_permission.py
import os

file_path = "example.py"
os.chmod(file_path, 0o777) #rwxrwxr-x
print(f"Permissions changed to rwxrwxr-x (777) for: {file_path}")
