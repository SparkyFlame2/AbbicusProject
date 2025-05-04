
# orbital_auto_trigger.py – Fixed for v2.8+ with required imports

import random
import victory_module as victory
import enforcement_module as enforce
import zorexxian_module as zorexxian
import penumbra_module as penumbra

def check_orbital_events():
    triggered = False

    if victory.sentinels >= 3 and zorexxian.get_charges() > 0:
        if random.random() < 0.33:
            print("[ZOREXXIAN OVERRIDE] Dropship deploying due to Sentinel escalation!")
            result = zorexxian.deploy_dropship()
            for unit in result:
                if unit == "enforcer":
                    enforce.enforcers = min(enforce.enforcers + 1, 12)
                elif unit == "sentinel":
                    victory.sentinels += 1
            triggered = True

    if victory.sirens >= 6 and penumbra.get_charges() > 0:
        if random.random() < 0.5:
            print("[PENUMBRUM ALLIANCE] Deployment pod arriving with hope...")
            result = penumbra.deploy_payload()
            for unit in result:
                if unit == "siren":
                    victory.sirens += 1
                elif unit == "oso":
                    enforce.oso_units += 1
                elif unit == "oso_advanced":
                    victory.advanced_oso_units += 1
            triggered = True

    if triggered:
        print("[ORBITAL UPDATE COMPLETE]")
