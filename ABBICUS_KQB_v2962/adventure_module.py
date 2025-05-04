
# adventure_module.py

import time
import random
from datetime import datetime

missions = [
    "Recover the lost shard of Timeglass from Vault Theta.",
    "Decode the encrypted dreams of Kai from the ruins of U35.",
    "Investigate the echo pulses near the Core Spiral.",
    "Rescue an Archivist stranded in the drift between cycles.",
    "Protect the sacred archive from a paradox collapse.",
    "Deliver a memory fragment to a lost child of the Author.",
    "Unravel the corrupted timeline known as the False Burn."
]

def build_adventure():
    print("==[ADVENTURE BUILDER]==")
    name = input("Archivist Name: ")
    uni = input("Universe Code (e.g. U35, U36): ")
    print("Choose your mission:")
    for i, m in enumerate(missions, 1):
        print(f" {i}. {m}")
    try:
        choice = int(input("Mission #: "))
        mission = missions[choice - 1] if 1 <= choice <= len(missions) else random.choice(missions)
    except:
        mission = random.choice(missions)
    print("Adventure constructed.")
    return {"name": name, "universe": uni, "mission": mission, "log": []}

def run_adventure(adventure):
    print(f"==[BEGINNING ADVENTURE: {adventure['name']}]==")
    print(f"Universe: {adventure['universe']} | Mission: {adventure['mission']}")
    for i in range(3):
        event = random.choice([
            "An Oso unit detects something behind a locked panel.",
            "A strange voice whispers coordinates in your mind.",
            "The shell flickers. Time bends and straightens again.",
            "You find a relic, humming with incomplete memory.",
            "A temporal stutter rewinds your last step.",
            "Something ancient is watching you... quietly."
        ])
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"Turn {i+1} [{timestamp}]: {event}")
        adventure['log'].append((i+1, event, timestamp))
        time.sleep(1)
    print("==[MISSION LOG COMPLETE]==")
    return adventure
