
import time
import random
from datetime import datetime

# Universe Date (UD) = 30 seconds
UD_DURATION_SECONDS = 30
TOTAL_CYCLE_UD = 10000
start_time = time.time()
random.seed()

# Lore-defined jump points (manual jumps)
eras = {
    "origin": {"timestamp": 0, "label": "The Origin Point", "phase": "Primordial Era"},
    "preburn": {"timestamp": 300, "label": "The Age Before Fire", "phase": "Primordial Era"},
    "fracture": {"timestamp": 900, "label": "Fracture Zone", "phase": "Primordial Era"},
    "nullzone": {"timestamp": 1800, "label": "Temporal Nullzone", "phase": "Age of Myths"},
    "echo": {"timestamp": 2700, "label": "Echo Point", "phase": "Age of Myths"},
    "morrow": {"timestamp": 3600, "label": "The Morrow Line", "phase": "Cultural Renaissance"},
    "modern": {"timestamp": 4500, "label": "The Industrial Age", "phase": "Cultural Renaissance"},
    "postmodern": {"timestamp": 6200, "label": "The Rise of AI", "phase": "Scientific Ascension"},
    "collapse": {"timestamp": 9900, "label": "Cycle Collapse"},
}

current_era = "origin"

# ====== Time Tracking Functions ======

last_drift_value = None

def drift_nudge():
    global last_drift_value
    if last_drift_value is None:
        return

    if random.choice([True, False]):
        last_drift_value *= 10
    else:
        last_drift_value /= 10

    if 0 < abs(last_drift_value) < 1e-10:
        last_drift_value = -1e-10 if last_drift_value > 0 else last_drift_value


def store_drift_value(val):
    global last_drift_value
    last_drift_value = val

def get_drift_value():
    return last_drift_value if last_drift_value is not None else 0

def get_current_ud():
    return int((time.time() - start_time) / UD_DURATION_SECONDS)

def get_jump_ud():
    return int(eras.get(current_era, {}).get("timestamp", 0) / UD_DURATION_SECONDS)

def get_timestamp():
    return time.time()

def get_cycle_progress():
    return min(get_current_ud() / TOTAL_CYCLE_UD, 1.0)

def get_current_era():
    return eras.get(current_era, {}).get("phase", "Unknown Era")
def show_current_era():
    return ["current_era"]


def list_all_eras():
    return ["origin","preburn", "fracture", "nullzone", "echo", "morrow", "modern", "postmodern", "collapse"]

def get_era_timestamp(tag):
    return eras.get(tag, {}).get("timestamp", 0)

# ====== Manual Era Jump System (Tagged Beacons) ======

def jump_to_era(tag):
    global current_era
    if tag in eras:
        current_era = tag
        return f"[TIME] Jumped to {eras[tag]['label']} ({tag})"
    return "[ERROR] Unknown era tag."

def get_current_jump_label():
    return eras.get(current_era, {}).get("label", "Unknown")
