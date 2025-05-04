
# zorexxian_module.py – Oversees orbital Zorexxian Dropships

import random

zorexxian_charges = 0

def accrue_charge():
    global zorexxian_charges
    zorexxian_charges += 1
    print(f"[ZOREXXIAN CHARGE] Current charges: {zorexxian_charges}")

def get_charges():
    return zorexxian_charges

def deploy_dropship():
    global zorexxian_charges
    if zorexxian_charges == 0:
        print("[ZOREXXIAN] No charges to deploy.")
        return []

    zorexxian_charges = 0
    roll = random.randint(1, 100)
    if roll <= 30:
        print("[ZOREXXIAN] Mixed Unit Drop: 2 Sentinels + 3 Enforcers")
        return ["sentinel", "sentinel", "enforcer", "enforcer", "enforcer"]
    elif roll <= 60:
        print("[ZOREXXIAN] Heavy Sentinels Incoming.")
        return ["sentinel", "sentinel", "sentinel"]
    elif roll <= 90:
        print("[ZOREXXIAN] Max Enforcer Assault!")
        return ["enforcer"] * 12
    else:
        print("[ZOREXXIAN] Signal Jammed. Dropship missed.")
        return []
