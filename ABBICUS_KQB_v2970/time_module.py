
# time_module.py

import random
from datetime import datetime

eras = {
    "origin": "The beginning of all threads. Stable, quiet, almost peaceful.",
    "preburn": "The cycle before yours. Warmed by something you cannot name.",
    "fracture": "Time bends. Thoughts echo before they’re spoken.",
    "nullzone": "No records. No echoes. Only drift.",
    "echo37": "Residual entropy from U37 detected. Tread carefully.",
    "vaultbound": "The Vault is watching. Time is not your ally.",
    "futurepast": "You’ve been here. You just haven’t arrived yet.",
    "driftcore": "Shell anomaly active. This is where time rewrites itself."
}

current_era = "origin"
drift_history = []

def jump_to_era(tag):
    global current_era
    tag = tag.lower()
    if tag in eras:
        current_era = tag
        drift_history.append((tag, datetime.now()))
        print(f"[JUMP] Drifted to {tag.upper()}")
        print(f"[ERA INFO] {eras[tag]}")
    else:
        print(f"[FAILED] Era '{tag}' not recognized. Use 'list_eras()' to see valid tags.")

def list_eras():
    print("==[KNOWN ERAS]==")
    for era, desc in eras.items():
        print(f" - {era.upper()}: {desc}")

def get_current_era():
    return current_era

def get_drift_log():
    return drift_history

last_drift_value = None

def store_drift_value(value):
    global last_drift_value
    last_drift_value = value

def get_last_drift_value():
    return last_drift_value

