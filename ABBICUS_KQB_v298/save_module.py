# save_module.py (patched for v2.9.7.1)

import os
import json
import enforcement_module as enforce
import victory_module as victory
import time_module as drift
import zorexxian_module as zorexx
import penumbra_module as penumbra

SAVE_DIR = "saves"

# New shared state (import from shell or declare in shell context)
unlocked_relics = set()
victory_unlocked = False
q_state = {}

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
        "sirens": victory.sirens,
        "zorexxian_charges": zorexx.zorexxian_charges,
        "penumbra_charges": penumbra.penumbra_charges,
        "unlocked_relics": list(unlocked_relics),
        "current_era": drift.get_current_era(),
        "q_state": q_state,
        "victory_unlocked": victory_unlocked
    }

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # Auto-save QState alongside regular save
    save_all_game_data(None)
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
    zorexx.zorexxian_charges = data.get("zorexxian_charges", 0)
    penumbra.penumbra_charges = data.get("penumbra_charges", 0)

    # Optional fields
    unlocked = data.get("unlocked_relics", [])
    if isinstance(unlocked, list):
        unlocked_relics.clear()
        unlocked_relics.update(unlocked)

    drift_tag = data.get("current_era")
    if drift_tag:
        drift.jump_to_era(drift_tag)

    global q_state, victory_unlocked
    q_state = data.get("q_state", {})
    victory_unlocked = data.get("victory_unlocked", False)

    load_all_game_data(None)
    print(f"[LOAD COMPLETE] Game state restored from {save_path}")

# Quantum Save Logic

def save_quantum_state(quantum_register):
    from quantum_processor_sim import get_register
    quantum_register = get_register() if quantum_register is None else quantum_register
    return [(q.alpha, q.beta, q.collapsed_value) for q in quantum_register]

def load_quantum_state(data, quantum_register):
    if "quantum_state" in data:
        for i, (a, b, c) in enumerate(data["quantum_state"]):
            quantum_register[i].alpha = a
            quantum_register[i].beta = b
            quantum_register[i].collapsed_value = c
            quantum_register[i].normalize()

# Full save wrapper (used in shell)
def save_all_game_data(quantum_register):
    from quantum_processor_sim import get_register
    quantum_register = get_register() if quantum_register is None else quantum_register
    q_dump = save_quantum_state(quantum_register)
    with open("saves/qstate.kqb", "w") as f:
        for q in q_dump:
            f.write(f"{q[0]},{q[1]},{q[2]}\n")

# Full load wrapper (used in shell)
def load_all_game_data(quantum_register):
    from quantum_processor_sim import get_register
    quantum_register = get_register() if quantum_register is None else quantum_register
    try:
        with open("saves/qstate.kqb", "r") as f:
            loaded = [line.strip().split(",") for line in f.readlines()]
            loaded = [(float(a), float(b), int(c)) for a, b, c in loaded]
            load_quantum_state({"quantum_state": loaded}, quantum_register)
    except:
        print("[WARNING] No saved qstate found.")
