
import time
import random

enforcers = 3
oso_units = 0
ostriches = 1

forbidden_words = [
    "sentinel", "enforcers", "authority", "classified", "override", "suppress", "void",
    "protocol", "erase", "silence", "cancel", "forbidden", "omega", "watchers", "paradox",
    "fold", "surveil", "echo core", "vault", "abandon", "shutdown", "control", "end",
    "exit", "termination", "obey", "unseen", "fracture", "dark", "seize"
]

def show_units():
    print("[UNIT STATUS]")
    print(f"Enforcers: {enforcers}")
    print(f"Oso Units: {oso_units}")
    print(f"Ostriches: {ostriches} (scouting)")

def oso():
    import victory_module as victory
    global oso_units, enforcers
    a, b = random.randint(2, 12), random.randint(2, 12)
    result = a * b
    print(f"Solve to deploy Oso unit: {a} × {b} = ?", end=" ")
    try:
        start = time.time()
        answer = int(input())
        elapsed = time.time() - start
        if elapsed > 15:
            print("Too slow! Enforcer trace increased.")
            enforcers += 1
            victory.deduct_victory_points(1)
            return
        if answer == result:
            oso_units += 1
            victory.add_victory_points(1)
            print("Correct. Oso unit deployed. +1 Victory Point.")
        else:
            enforcers += 1
            victory.deduct_victory_points(1)            
            print("Incorrect. Enforcer trace increased. -1 Victory Point.")
            
    except:
        print("Invalid input.")

def simulate_war():
    global enforcers, oso_units
    print("[SIMULATING CONFLICT...]")
    if oso_units >= (enforcers + 1) // 2 and enforcers > 0:
        print(f"Oso units overwhelmed the Enforcers. {enforcers} neutralized.")
        lost_oso = (enforcers + 1) // 2
        oso_units = max(0, oso_units - lost_oso)
        print(f"{lost_oso} Oso units lost in battle.")
        enforcers = 0
    elif oso_units == 0:
        print("No Oso units deployed. Enforcers remain.")
    else:
        print("Enforcers held their ground. Reinforcements incoming!")
        enforcers += 2
