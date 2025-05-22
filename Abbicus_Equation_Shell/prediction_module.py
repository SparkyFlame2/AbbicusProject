import random
from state_log import read_log

def predict_next_state():
    log = read_log()
    if not log:
        return random.uniform(0, 10)
    last_line = log[-1]
    try:
        last_input = float(last_line.split()[1])
        drift = float(last_line.split()[3])
        return last_input + (drift * random.uniform(0.9, 1.1))
    except:
        return random.uniform(0, 10)
