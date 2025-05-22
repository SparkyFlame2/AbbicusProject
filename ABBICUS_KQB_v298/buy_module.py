
# buy_module.py

from time import time
from collections import deque

# Simulated external state interfaces (to be connected in main_shell)
import penumbra_module
enforce = None
victory = None
time_state = None
inventory = None

penumbra_factories = 0
factory_queue = deque()
MAX_FACTORIES = 5

def set_interfaces(enf, vic, tstate, inv):
    global enforce, victory, time_state, inventory
    enforce = enf
    victory = vic
    time_state = tstate
    inventory = inv

def buy(item):
    global penumbra_factories

    if item == "jump_charge forward":
        if victory.sirens >= 5 and enforce.oso_units >= 3:
            victory.sirens -= 5
            enforce.oso_units -= 3
            time_state["jump_forward_tokens"] += 1
            return "[BUY] Acquired Forward Jump Charge."
        return "[ERROR] Not enough Sirens or Oso Units."

    elif item == "jump_charge retro":
        if victory.points >= 10 and enforce.ostriches >= 3:
            victory.points -= 10
            enforce.ostriches -= 3
            time_state["jump_retro_tokens"] += 1
            return "[BUY] Acquired Retro Jump Charge."
        return "[ERROR] Not enough Victory Points or Ostriches."

    elif item == "traverser_ship":
        if victory.archive_mastery >= 5:
            victory.archive_mastery -= 5
            inventory["has_traverser"] = True
            return "[BUY] Traverser Ship acquired."
        return "[ERROR] Not enough Archive Mastery."

    elif item == "traverser_retro_pass":
        if not inventory.get("has_traverser", False):
            return "[ERROR] Traverser Ship required first."
        if victory.points >= 20:
            victory.points -= 20
            inventory["has_retro_pass"] = True
            return "[BUY] Retro Traverser Pass acquired."
        return "[ERROR] Not enough Victory Points."

    elif item == "cycle_pass":
        if inventory.get("has_traverser", False):
            inventory["cycle_pass_unlocked"] = True
            return "[BUY] Cycle Pass granted."
        return "[ERROR] Traverser required."

    elif item == "penumbra_factory":
        global penumbra_factories
        if victory.archive_mastery >= 1 and penumbra_factories < MAX_FACTORIES:
            victory.archive_mastery -= 1
            penumbra_factories += 1
            factory_queue.append((time(), penumbra_factories))
            return f"[BUY] Penumbra Factory #{penumbra_factories} created."
        return "[ERROR] Max factories reached or not enough mastery points."

    
    elif item == "zorrexian_challenge_charge":
        if enforce.oso_units > 0 or enforce.advanced_oso > 0 or victory.sirens > 0 or enforce.ostriches > 0:
            enforce.oso_units = 0
            enforce.advanced_oso = 0
            victory.sirens = 0
            enforce.ostriches = 0
            time_state["zorrexian_challenge_ready_at"] = time() + 300  # 5 minutes cooldown
            time_state["zorrexian_waves"] = 5
            return "[BUY] Zorrexian Challenge Charge purchased. First wave will be ready in 5 minutes."
        return "[ERROR] No units to sacrifice for Zorrexian Challenge."

        return "[ERROR] Unknown item."

def claim_factory_units():
    ready_units = 0
    now = time()
    for _ in range(len(factory_queue)):
        start_time, factory_id = factory_queue.popleft()
        if now - start_time >= 600 and penumbra_module.get_charges() > 0:
            penumbra_module.use_charge()
            penumbra_module.deploy_penumbra_units()
  # 10 minutes
            ready_units += 3
        else:
            factory_queue.append((start_time, factory_id))  # Not ready yet
    return f"[FACTORY] {ready_units} units claimed." if ready_units else "[FACTORY] No units ready."
