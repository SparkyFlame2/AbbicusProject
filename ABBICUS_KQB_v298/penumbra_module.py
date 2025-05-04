
# penumbra_module.py – Gift-based Penumbra Deployment Unit

import random

penumbra_charges = 0

def accrue_charge():
    global penumbra_charges
    penumbra_charges += 1
    print(f"[PENUMBRUM CHARGE] Current charges: {penumbra_charges}")

def get_charges():
    return penumbra_charges

# penumbra_module.py

import random

penumbra_charges = 0

def deploy_penumbra_units():
    units = []
    for _ in range(10):  # 10 deployment rolls
        if random.choice([True, False]):  # coin flip = heads
            roll = random.randint(1, 10)
            if roll == 1:
                units.append("ostrich")
            elif roll == 2:
                units.append("advanced_oso")
            elif roll == 3:
                units += ["ostrich", "ostrich"]
            elif roll in [4, 7]:
                units += ["siren", "siren", "siren"]
            elif roll in [5, 6, 9]:
                units += ["oso", "oso"]
            elif roll == 10:
                units += ["advanced_oso"] * 2 + ["siren"] * 3 + ["oso"] * 5 + ["ostrich"] * 5
    return units