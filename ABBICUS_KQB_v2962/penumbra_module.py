
# penumbra_module.py – Gift-based Penumbra Deployment Unit

import random

penumbra_charges = 0

def accrue_charge():
    global penumbra_charges
    penumbra_charges += 1
    print(f"[PENUMBRUM CHARGE] Current charges: {penumbra_charges}")

def get_charges():
    return penumbra_charges

def deploy_payload():
    global penumbra_charges
    if penumbra_charges == 0:
        print("[PENUMBRUM] No charges to deploy.")
        return []

    penumbra_charges = 0
    print("[PENUMBRUM DEPLOYMENT] Reinforcement pod lands with a blast of hope.")

    result = ["siren"] * 5

    oso_bonus = random.choice([0, 1, 2])
    result += ["oso_advanced"] * oso_bonus

    oso_units = random.choice([1, 3, 6])
    result += ["oso"] * oso_units

    print(f"[PAYLOAD] +5 Sirens, +{oso_bonus} Advanced Oso, +{oso_units} Oso Units")
    return result
