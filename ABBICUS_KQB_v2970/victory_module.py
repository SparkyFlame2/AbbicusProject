
# victory_module.py

import time
import random
import enforcement_module as enforce
import zorexxian_module as zorexx
import penumbra_module as penumbra
import relic_classifier as relics
import lore_module as lore

reward_milestones = set()

# Game state trackers
victory_points = 0
time_jail_count = 0
wanted_level = 0
last_milestone = 0
sentinels = 0
sentinel_shards = 0
advanced_oso = 0
sirens = 0
ostriches= 0
archive_mastery = 0

def add_victory_points(amount=1):
    global victory_points
    victory_points += amount
    print(f"[VICTORY] Gained {amount} Victory Point(s). Total: {victory_points}")


def deduct_victory_points(amount=1):
    global victory_points
    victory_points = max(0, victory_points - amount)
    print(f"[VICTORY] Lost {amount} Victory Point(s). Total: {victory_points}")


def add_mastery(amount=1):
    global archive_mastery
    archive_mastery += amount
    print(f"[MASTERY] Archive Mastery increased by {amount}. Total: {archive_mastery}")


def convert_victory_to_mastery():
    global archive_mastery, victory_points
    converted = 0
    while victory_points >= 100:
        archive_mastery += 1
        victory_points -= 100
        converted += 1
    if converted:
        print(f"[CONVERSION] Converted {converted * 100} Victory Points into {converted} Mastery Point(s).")
    else:
        print("[CONVERSION] Not enough Victory Points to convert. Minimum: 100")

def award_victory_points(enforcers_defeated):
    global victory_points
    if 5 <= enforcers_defeated <= 8:
        victory_points += 1
        print("[VICTORY] +1 Victory Point earned!")
    elif 9 <= enforcers_defeated <= 12:
        victory_points += 2
        print("[VICTORY] +2 Victory Points earned!")
    check_victory()

def check_victory():
    if victory_points >= 100:
        print(">>> YOU HAVE WON THE WAR <<<")
        print("But the Archivists know: peace is never permanent...")

def simulate_time_jail():
    global time_jail_count, wanted_level, last_milestone
    time_jail_count += 1
    victory.deduct_victory_points(1)
    print("[-1 VICTORY] Entering Time Jail... Drift was penalized.")

    # Enforce wanted level tiers only on milestone crossing
    milestone_checkpoints = [15, 30, 50, 100]
    for milestone in milestone_checkpoints:
        if time_jail_count >= milestone > last_milestone:
            wanted_level = max(wanted_level, milestone_checkpoints.index(milestone) + 1)
            last_milestone = milestone
            print(f"[WANTED] Your wanted level has increased! ★ {wanted_level}")

    countdown = 120
    while countdown > 0:
        print(f"Time Jail: {countdown} seconds remaining.")
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        print(f"Solve to reduce sentence ({a} × {b} = ?): ", end="")
        try:
            answer = int(input().strip())
            if answer == a * b:
                countdown -= 15
                print("-15 seconds")
            else:
                countdown -= 5
                print("-5 seconds")
        except:
            countdown -= 5
            print("[ERROR] Invalid input. -5 seconds")
        time.sleep(0.5)
    print("[RELEASED] You are free to continue.")

def craft_advanced_oso():
    global advanced_oso
    if enforce.oso_units >= 2 and enforce.ostriches >= 1:
        enforce.oso_units -= 2
        enforce.ostriches -= 1
        advanced_oso += 1
        print("[CRAFTED] Advanced Oso Unit created!")
    else:
        print("Not enough Oso or Ostriches to craft.")

def add_sentinel_shards(amount):
    global sentinel_shards, sentinels
    sentinel_shards += amount
    if sentinel_shards >= 5:
        new_sentinels = sentinel_shards // 5
        if new_sentinels > 0:
            sentinels += new_sentinels
            sentinel_shards %= 5
            print(f"[ALERT] {new_sentinels} Sentinel(s) born from the shards.")

def simulate_battle():
    global advanced_oso, sentinels, sirens

    print("\nChoose your battlefield:")
    print("  1. Fight Sentinels")
    print("  2. Fight Enforcers")
    print("  3. Fight Both")
    choice = input("Battle type (1/2/3): ").strip()

    if choice == "1" and sentinels > 0:
        print(f"You are facing {sentinels} Sentinel(s).")
        print(f"Advanced Oso: {advanced_oso} | Sirens: {sirens}")
        use = input("Use Advanced Oso (A), Sirens (S), or None (N)? ").strip().lower()
        if use == "a" and advanced_oso >= sentinels:
            advanced_oso -= sentinels
            print("[VICTORY] Sentinels neutralized by Advanced Oso.")
            sentinels = 0
        elif use == "s" and sirens >= (3 * sentinels):
            sirens -= 3 * sentinels
            print("[VICTORY] Sentinels silenced by Sirens of Inspiration.")
            sentinels = 0
        else:
            print("[DEFEAT] Your strike failed.")
            simulate_time_jail()
        return

    elif choice == "2" and enforce.enforcers > 0:
        print(f"You are facing {enforce.enforcers} Enforcer(s).")
        print(f"Oso: {enforce.oso_units} | Advanced Oso: {advanced_oso}")
        use = input("Use Advanced Oso (A), Basic Oso (B), or None (N)? ").strip().lower()
        if use == "a" and advanced_oso * 5 >= enforce.enforcers:
            lost = (enforce.enforcers + 4) // 5
            advanced_oso -= lost
            award_victory_points(enforce.enforcers)
            enforce.enforcers = 0
        elif use == "b" and enforce.oso_units >= (enforce.enforcers + 1) // 2:
            lost = (enforce.enforcers + 1) // 2
            enforce.oso_units -= lost
            award_victory_points(enforce.enforcers)
            enforce.enforcers = 0
        else:
            print("[DEFEAT] The Enforcers were too strong.")
            simulate_time_jail()
        return

    elif choice == "3" and sentinels + enforce.enforcers > 0:
        print(f"You are fighting {enforce.enforcers} Enforcers and {sentinels} Sentinels.")
        simulate_battle_type("2")  # Enforcers
        simulate_battle_type("1")  # Sentinels
    else:
        print("No enemies to fight.")

def check_relic_rewards():
    filtered = [r for r in relics.unlocked_relics if relics.relic_tags.get(r) not in ["sacred", "forbidden"]]
    count = len(filtered)

    # Every 5
    if count >= 5 and count % 5 == 0 and count not in reward_milestones:
        reward_milestones.add(count)
        victory.sirens += 1
        enforce.oso_units += 1
        print(f"[RELIC REWARD] {count} relics unlocked → +1 Siren, +1 Oso")

    # Every 20
    if count % 20 == 0 and count >= 20 and count not in reward_milestones:
        reward_milestones.add(count)
        penumbra.penumbra_charges += 1
        print(f"[RELIC REWARD] {count} relics unlocked → +1 Penumbra Charge")

    # 100
    if count == 100 and count not in reward_milestones:
        reward_milestones.add(count)
        victory.add_victory_points(20)
        penumbra.penumbra_charges += 1
        enforce.oso_units += 1
        victory.sirens += 1
        print("[RELIC MILESTONE] 100 relics unlocked! +20 Victory, +1 of all key units")

    # 500
    if count == 500 and count not in reward_milestones:
        reward_milestones.add(count)
        victory.add_mastery(1)
        print("[RELIC MILESTONE] 500 relics unlocked! +1 Archive Mastery")

    # 1000
    if count == 1000 and count not in reward_milestones:
        reward_milestones.add(count)
        victory.add_mastery(2)
        print("[RELIC MILESTONE] 1000 relics unlocked! +2 Mastery. Cutscene pending...")



def show_status():
    print("\n==[TACTICAL STATUS REPORT]==")
    print(f"Victory Points: {victory_points}")
    print(f"Time Jail Trips: {time_jail_count}")
    print(f"Wanted Level: {'★' * wanted_level if wanted_level > 0 else 'None'}")
    print(f"Sentinels: {sentinels}")
    print(f"Sentinel Shards: {sentinel_shards}")
    print(f"Enforcers: {enforce.enforcers}")
    print(f"Advanced Oso Units: {advanced_oso}")
    print(f"Oso Units: {enforce.oso_units}")
    print(f"Sirens: {sirens}")
    print(f"Ostriches: {enforce.ostriches} (scouting)")
    print(f"Archive Mastery: {archive_mastery}")
    print(f"Relics Unlocked: {len(relics.unlocked_relics)}")
    print("\n==[ORBITAL STATUS REPORT]==")    
    print(f"Zorexxian Dropship Charges: {zorexx.zorexxian_charges}")
    print(f"Penumbra Deployment Charges: {penumbra.penumbra_charges}")
