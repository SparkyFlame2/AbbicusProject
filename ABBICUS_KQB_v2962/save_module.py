
# save_module.py

import os
import json
import enforcement_module as enforce
import victory_module as victory

SAVE_DIR = "saves"

def save_game(filename):
    if not filename.endswith(".kqb"):
        filename += ".kqb"
    os.makedirs(SAVE_DIR, exist_ok=True)
    save_path = os.path.join(SAVE_DIR, filename)

    data = {
        "enforcers": enforce.enforcers,
        "oso_units": enforce.oso_units,
        "ostriches": enforce.ostriches,
        "victory_points": victory.victory_points,
        "time_jail_count": victory.time_jail_count,
        "wanted_level": victory.wanted_level,
        "sentinels": victory.sentinels,
        "sentinel_shards": victory.sentinel_shards,
        "advanced_oso": victory.advanced_oso,
        "sirens": victory.sirens
    }

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"[SAVE COMPLETE] Game state saved to {save_path}")

def load_game(filename):
    if not filename.endswith(".kqb"):
        filename += ".kqb"
    save_path = os.path.join(SAVE_DIR, filename)

    if not os.path.exists(save_path):
        print("[ERROR] Save file not found.")
        return

    with open(save_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    enforce.enforcers = data.get("enforcers", 0)
    enforce.oso_units = data.get("oso_units", 0)
    enforce.ostriches = data.get("ostriches", 0)
    victory.victory_points = data.get("victory_points", 0)
    victory.time_jail_count = data.get("time_jail_count", 0)
    victory.wanted_level = data.get("wanted_level", 0)
    victory.sentinels = data.get("sentinels", 0)
    victory.sentinel_shards = data.get("sentinel_shards", 0)
    victory.advanced_oso = data.get("advanced_oso", 0)
    victory.sirens = data.get("sirens", 0)

    print(f"[LOAD COMPLETE] Game state restored from {save_path}")


# Quantum Save Logic
def save_quantum_state(quantum_register):
    return [(q.alpha, q.beta, q.collapsed_value) for q in quantum_register]

def load_quantum_state(data, quantum_register):
    if "quantum_state" in data:
        for i, (a, b, c) in enumerate(data["quantum_state"]):
            quantum_register[i].alpha = a
            quantum_register[i].beta = b
            quantum_register[i].collapsed_value = c
            quantum_register[i].normalize()
