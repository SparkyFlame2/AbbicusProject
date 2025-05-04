
# adventure_branching_module.py – Era-Based Branching

import random
from datetime import datetime
import abbicus_predict as predict
import abbicus_retrocausality as retro

MAX_SCENES = 30

# Era-specific story prompts
era_story_nodes = {
    "origin": [
        "You awaken in a quiet, sealed archive.",
        "Time feels untouched here—static, preserved.",
        "You find a relic with no inscription, humming faintly."
    ],
    "fracture": [
        "A glitch in the corridor resets your step.",
        "You speak and hear your voice before you open your mouth.",
        "A shadow of yourself is waiting at the next corner."
    ],
    "vaultbound": [
        "The Vault pulses as if aware of your presence.",
        "An echo tries to rewrite your thoughts.",
        "A forbidden name is scratched into the console."
    ],
    "echo37": [
        "Residual drift makes the air hum.",
        "You see memories that aren't yours yet.",
        "A figure made of entropy points down two paths."
    ],
    "driftcore": [
        "Everything is in motion, even the stillness.",
        "Drift spirals form on the shell's glass.",
        "The story rewrites itself before your eyes."
    ],
    "nullzone": [
        "No data. No input. Only echoes remain.",
        "Something once lived here, but even the decay is gone.",
        "An empty shell of a story awaits its first sentence."
    ]
}

choice_templates = [
    ["Step forward", "Examine surroundings", "Wait and listen"],
    ["Respond to the echo", "Continue in silence", "Backtrack quickly"],
    ["Run toward the light", "Hide behind the driftwall", "Shout your true name"]
]

def get_choices():
    return random.choice(choice_templates)

def get_scene_from_era(era):
    return random.choice(era_story_nodes.get(era, ["The shell glitches. Nothing appears."]))

def start_adventure(era_tag="origin"):
    log = []
    print(f"==[ADVENTURE IN ERA: {era_tag.upper()}]==")
    for turn in range(1, MAX_SCENES + 1):
        scene = get_scene_from_era(era_tag)
        choices = get_choices()
        stamp = datetime.now().strftime("%H:%M:%S")

        print(f"--- SCENE {turn} [{stamp}] ---")
        print(scene)
        for idx, choice in enumerate(choices, 1):
            print(f"  {idx}. {choice}")
        
        predict_val = predict.get_prediction()
        if predict_val is not None:
            print(f"[PREDICTION] Consider option: {predict_val}")
        
        try:
            selection = int(input("Your choice (1/2/3): ").strip())
            if 1 <= selection <= len(choices):
                decision = choices[selection - 1]
                print(f"[DECISION] You chose: {decision}")
                retro.log_action("adventure", {"turn": turn, "scene": scene, "choice": decision})
                log.append((turn, scene, decision, stamp))
                predict.clear_prediction()
            else:
                print("[ERROR] Invalid choice. Skipping scene.")
        except:
            print("[ERROR] Input failed. Skipping scene.")
        
        if turn == MAX_SCENES:
            print("==[END OF ADVENTURE]==")
            break
    return log

def undo_last_choice():
    drift = predict.get_drift()
    if drift is None or drift >= 0:
        print("[FIXED POINT] Cannot reverse timeline without negative drift.")
        return
    action, state = retro.undo_action()
    if action == "adventure":
        print(f"[RETROCAUSALITY SUCCESS] Undoing last choice from Scene {state['turn']}.")
    else:
        print("[NO ACTION] No valid adventure step to reverse.")
