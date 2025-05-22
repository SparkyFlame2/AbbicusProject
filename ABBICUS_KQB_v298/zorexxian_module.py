# zorexxian_module.py – Oversees orbital Zorexxian Dropships

import random

zorexxian_charges = 0

def accrue_charge():
    global zorexxian_charges
    zorexxian_charges += 1
    print(f"[ZOREXXIAN CHARGE] Current charges: {zorexxian_charges}")

def get_charges():
    return zorexxian_charges

def deploy_zorexxian_units():
    units = []

    for _ in range(10):  # 10 flips
        if random.choice([True, False]):  # Heads
            roll = random.randint(1, 10)
            if roll == 1:
                pass  # no unit
            elif roll in (2, 3, 4, 5, 6, 7, 8):
                units.append("enforcer")
            elif roll == 9:
                units.append("sentinel")
            elif roll == 10:
                units.extend(["sentinel"] * 2 + ["enforcer"] * 5)

    return units


import time

zorrexian_challenge_ready_at = 0
zorrexian_waves_remaining = 0

def start_challenge():
    global zorrexian_challenge_ready_at, zorrexian_waves_remaining
    now = time.time()
    if now >= zorrexian_challenge_ready_at and zorrexian_waves_remaining == 5:
        return "[CHALLENGE] Challenge already initialized. Use 'challenge continue'."
    if now < zorrexian_challenge_ready_at:
        return "[CHALLENGE] Challenge not ready yet. Please wait."
    zorrexian_challenge_ready_at = now
    zorrexian_waves_remaining = 5
    return "[CHALLENGE] Zorrexian Challenge begun. Type 'challenge continue' to face the first wave."

def continue_challenge():
    global zorrexian_waves_remaining
    if zorrexian_waves_remaining <= 0:
        return "[CHALLENGE] No remaining waves. Purchase a new charge to continue."
    deploy_zorexxian_units()
    zorrexian_waves_remaining -= 1
    return f"[CHALLENGE] Wave launched. {zorrexian_waves_remaining} waves remain."

def challenge_all():
    global zorrexian_waves_remaining
    if zorrexian_waves_remaining <= 0:
        return "[CHALLENGE] No remaining waves. Purchase a new charge to continue."
    results = []
    while zorrexian_waves_remaining > 0:
        deploy_zorexxian_units()
        zorrexian_waves_remaining -= 1
        results.append(f"[CHALLENGE] Wave launched. {zorrexian_waves_remaining} waves remain.")
    return "\n".join(results)

def surrender_challenge():
    global zorrexian_waves_remaining
    zorrexian_waves_remaining = 0
    return "[CHALLENGE] Zorrexian Challenge aborted. Waves cleared."

def get_challenge_status():
    remaining = max(0, int(zorrexian_challenge_ready_at - time.time()))
    return f"Challenge Ready In: {remaining}s | Waves Remaining: {zorrexian_waves_remaining}"
