
# Enhanced retrocausality module

from copy import deepcopy

IMMUTABLE = {"invoke abbicus", "/gamma_tune", "/collapse_all", "/reset_all"}

last_action = None
last_state = {}

def log_action(action, state):
    global last_action, last_state
    if any(action.startswith(imm) for imm in IMMUTABLE):
        return  # Skip logging for system commands
    last_action = action
    last_state = deepcopy(state)
    print(f"[RETRO] Logged action: {action}")

def undo_action():
    global last_action, last_state
    if last_action is None:
        print("[RETRO] No reversible action recorded.")
        return None, {}
    print(f"[RETRO] Undoing action: {last_action}")
    return last_action, deepcopy(last_state)
