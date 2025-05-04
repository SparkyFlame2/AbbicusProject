
# time_module.py – Drift-Conscious Jump System

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

era_order = list(eras.keys())
current_era = "origin"
drift_history = []
latest_drift_value = None

def store_drift_value(val):
    global latest_drift_value
    latest_drift_value = val

def jump_to_era(tag):
    global current_era
    tag = tag.lower()

    if latest_drift_value is None:
        print("[FAILED] You must invoke the Abbicus Equation before jumping.")
        return

    if tag not in eras:
        print(f"[FAILED] Era '{tag}' not recognized. Use 'list_eras()' to see valid tags.")
        return

    current_index = era_order.index(current_era)
    target_index = era_order.index(tag)
    direction = target_index - current_index

    if latest_drift_value > 0 and direction < 0:
        print("[JUMP FAILED] Drift signature only allows forward jumps.")
        return
    elif latest_drift_value < 0 and direction > 0:
        print("[JUMP FAILED] Drift signature only allows backward jumps.")
        return

    if random.random() < 0.15:
        print("[JUMP FAILED] Entropy was not on your side.")
        return

    current_era = tag
    drift_history.append((tag, datetime.now()))
    print(f"[JUMP] Drifted to {tag.upper()}")
    print(f"[ERA INFO] {eras[tag]}")

def list_eras():
    print("==[KNOWN ERAS]==")
    for era, desc in eras.items():
        print(f" - {era.upper()}: {desc}")

def get_current_era():
    return current_era

def get_drift_log():
    return drift_history
