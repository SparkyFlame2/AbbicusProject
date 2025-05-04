
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