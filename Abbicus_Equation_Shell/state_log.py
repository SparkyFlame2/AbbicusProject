LOG_FILE = "abbicus_log.txt"

def log_state(state):
    with open(LOG_FILE, "a") as f:
        f.write(f"Input: {state['input']:.4f} Drift: {state['drift']:.4f}\n")

def read_log():
    try:
        with open(LOG_FILE, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
