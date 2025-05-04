
# adventure_save_module.py

import os
import json
from datetime import datetime

SAVE_DIR = "saves/adventures"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_adventure(filename, log, era="unknown"):
    if not filename.endswith(".adv"):
        filename += ".adv"
    path = os.path.join(SAVE_DIR, filename)
    data = {
        "era": era,
        "timestamp": datetime.now().isoformat(),
        "log": log
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[SAVE COMPLETE] Adventure saved to: {path}")

def load_adventure(filename):
    if not filename.endswith(".adv"):
        filename += ".adv"
    path = os.path.join(SAVE_DIR, filename)
    if not os.path.exists(path):
        print("[ERROR] Adventure save not found.")
        return None
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"[LOAD SUCCESS] Loaded adventure from {data['timestamp']} in ERA: {data['era']}")
    for entry in data["log"]:
        turn, scene, choice, stamp = entry
        print(f"Scene {turn} [{stamp}]: {scene} => {choice}")
    return data
