
import os
from datetime import datetime

def ensure_log_directory():
    folder = "Session Logs"
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[LOG] Created folder: {folder}")
        else:
            print(f"[LOG] Folder already exists: {folder}")
        return folder
    except Exception as e:
        print(f"[LOG ERROR] Failed to create log directory: {e}")
        return None

def generate_log_filename():
    now = datetime.now()
    return now.strftime("session_%Y%m%d_%H%M%S.txt")

def save_session_log(lines):
    folder = ensure_log_directory()
    if not folder:
        print("[LOG ERROR] Could not ensure log directory.")
        return
    filename = generate_log_filename()
    path = os.path.join(folder, filename)
    print(f"[LOG] Saving session log to: {path}")
    try:
        with open(path, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"[ABBI] Session saved: {path}")
    except Exception as e:
        print(f"[LOG ERROR] Failed to save session log: {e}")
        with open("log_error_debug.txt", "w", encoding="utf-8") as error_file:
            error_file.write(f"Failed to save to {path}\nError: {e}")
