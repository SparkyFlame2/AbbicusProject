
# adventure_npc_module.py

import random
import abbicus_predict as predict
import time_module as drift

# NPC dialogue pools
npc_lines = {
    "maggie": [
        "You’re drifting too fast. Want me to reroute your anchor?",
        "This era feels off… You sure you’re in the right one?",
        "You ever think the Enforcers aren't chasing you, but waiting for you?"
    ],
    "tayla": [
        "Logic says jump, intuition says hide. What’s your call?",
        "Watch the pattern—there's always a pattern.",
        "The Vault is just a metaphor. Probably."
    ],
    "ghost": [
        "We made this path before you. You just forgot.",
        "Echoes remember things we never lived.",
        "Time isn’t real. But your fear of it is."
    ]
}

def npc_speak(name="maggie"):
    if name not in npc_lines:
        print(f"[ERROR] NPC '{name}' not recognized.")
        return

    drift_val = predict.get_drift()
    current_era = drift.get_current_era()

    line = random.choice(npc_lines[name])

    # Modify tone or warning based on context
    if drift_val and drift_val < 0:
        line += " You’re moving backward too far."
    elif drift_val and drift_val > 1e42:
        line += " Your presence is starting to fracture the shell."
    
    if current_era == "vaultbound" and name == "ghost":
        line = "You hear a thousand versions of yourself scream... and fall silent."

    print(f"[{name.upper()}] “{line}”")
