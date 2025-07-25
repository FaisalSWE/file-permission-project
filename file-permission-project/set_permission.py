#set_permission.py
import os

file_path = "example.py"
os.chmod(file_path, 0o775) #rwxrwxr-x
print(f"Permissions changed to rwxrwxr-x (775) for: {file_path}")
