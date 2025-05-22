
import time
import random
import time_module as drift

# Placeholder for external references
buy_function = None
get_drift_value = None

# Static catalog of possible items (base version)
catalog = {
    "penumbra_factory": {
        "price": {"archive_mastery": 1},
        "description": "Builds penumbra units passively. Max 5.",
        "rarity": "rare"
    },
    "zorrexian_challenge_charge": {
        "price": {"sacrifice": "all tactical units"},
        "description": "Summons 5 waves of hostile Zorrexian combatants.",
        "rarity": "uncommon"
    },
    "jump_charge forward": {
        "price": {"sirens": 5, "oso": 3},
        "description": "Adds 1 forward jump charge.",
        "rarity": "common"
    },
    "jump_charge retro": {
        "price": {"victory_points": 10, "ostriches": 3},
        "description": "Adds 1 retro jump charge.",
        "rarity": "uncommon"
    },
    "traverser_ship": {
        "price": {"archive_mastery": 5},
        "description": "Deployable quantum vessel for Era traversal.",
        "rarity": "legendary"
    },
    "traverser_retro_pass": {
        "price": {"victory_points": 20},
        "description": "Allows time travel to the past when onboard the Traverser.",
        "rarity": "legendary"
    },
    "cycle_pass": {
        "price": {"archive_mastery": 0},
        "description": "Allows re-entry at the moment of Cycle collapse (Traverser required).",
        "rarity": "rare"
    }
}

# Live shop inventory, rotates based on conditions
shop_inventory = {}

def set_interfaces(buy_func, drift_func):
    global buy_function, get_drift_value
    buy_function = buy_func
    get_drift_value = drift_func

def update_shop_inventory():
    drift_val = drift.get_drift_value()
    shop_inventory.clear()

    for item, info in catalog.items():
        if info["rarity"] == "common":
            shop_inventory[item] = info
        elif info["rarity"] == "uncommon" and drift_val > 1e10:
            shop_inventory[item] = info
        elif info["rarity"] == "rare" and drift_val > 1e20:
            shop_inventory[item] = info
        elif info["rarity"] == "legendary" and drift_val > 1e30:
            shop_inventory[item] = info

def show_shop():
    update_shop_inventory()
    if not shop_inventory:
        return "[SHOP] No items available at this time."

    lines = ["==[SHOP INVENTORY]=="]
    for item, info in shop_inventory.items():
        price_str = ', '.join(f"{v} {k}" for k, v in info["price"].items())
        lines.append(f"{item}: {info['description']} (Cost: {price_str})")
    return "\n".join(lines)

def attempt_purchase(item_name):
    update_shop_inventory()
    if item_name not in shop_inventory:
        return f"[SHOP] {item_name} is not currently available."
    return buy_function(item_name) if buy_function else "[SHOP] Buy function unavailable."
