
# abbicus_retrocausality.py

last_action = None
last_state = {}

def log_action(action, state):
    global last_action, last_state
    last_action = action
    last_state = state.copy()

def undo_action():
    global last_action, last_state
    return last_action, last_state
