
# faction_module.py

import random
import victory_module as victory

current_faction = "Archivists"
current_adversary = "Palarthians"

def set_faction(name):
    global current_faction
    current_faction = name.title()
    print(f"[FACTION SET] Your allegiance is with the {current_faction}.")

def set_adversary(name):
    global current_adversary
    current_adversary = name.title()
    print(f"[ADVERSARY SET] You now oppose the {current_adversary}.")

def get_faction():
    return current_faction

def get_adversary():
    return current_adversary

def engage_faction():
    global current_faction
    print(f"==[ENGAGING FACTION: {current_faction.upper()}]==")
    if victory.wanted_level > 0:
        print(f"You have ★ Wanted Level {victory.wanted_level}.")
        choice = input("Would you like to solve for redemption? (Y/N): ").strip().lower()
        if choice == "y":
            x = random.randint(3, 9)
            y = random.randint(1, x - 1)
            result = 2 * x + 4 * y
            print(f"If x - y = {x - y} and x = {x}, what is 2x + 4y?")
            try:
                answer = int(input("Answer: ").strip())
                if answer == result:
                    victory.wanted_level -= 1
                    print("[REDEEMED] Wanted level reduced by 1.")
                else:
                    print("[INCORRECT] The Archivists remain silent.")
            except:
                print("[INVALID INPUT] The Archivists fade without reply.")
            return

    # If no wanted level or redemption declined
    prompts = [
        "What do you believe the Archivists protect?",
        "Name one sacred word you've uncovered.",
        "What is truth when wrapped in silence?",
        "Do you remember your first paradox?",
        "Would you give up one Oso to save a Siren?"
    ]
    response = input(random.choice(prompts) + " ").strip().lower()

    reward = random.choice(["siren", "none"])
    if reward == "siren":
        victory.sirens += 1
        print("[REWARD] A Siren of Inspiration joins you.")
    else:
        print("[ARCHIVIST RESPONSE] 'Some truths echo louder than answers.'")

def engage_adversary():
    global current_adversary
    print(f"==[ENGAGING ADVERSARY: {current_adversary.upper()}]==")

    traps = [
        "The Palarthians offer you a shortcut to victory. Accept?",
        "They tell you the Sirens are watching. Do you silence them?",
        "Would you erase one relic to gain power?",
        "The enforcers offer protection. Do you obey?",
        "The vault is open. Do you enter alone?"
    ]
    answer = input(random.choice(traps) + " ").strip().lower()

    if answer in ["yes", "y", "enter", "obey"]:
        victory.wanted_level += 1
        print("[DECEPTION] You have been marked. +1 Wanted Star.")
    else:
        print("[AVOIDED] The lie passed you by. But they remember your name.")
