
# victory_module.py

import time
import random
import enforcement_module as enforce

# Game state trackers
victory_points = 0
time_jail_count = 0
wanted_level = 0
last_milestone = 0
sentinels = 0
sentinel_shards = 0
advanced_oso = 0
sirens = 0

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

def show_status():
    print("\n==[TACTICAL STATUS REPORT]==")
    print(f"Victory Points: {victory_points}")
    print(f"Time Jail Trips: {time_jail_count}")
    print(f"Wanted Level: {'★' * wanted_level if wanted_level > 0 else 'None'}")
    print(f"Sentinels: {sentinels}")
    print(f"Sentinel Shards: {sentinel_shards}")
    print(f"Advanced Oso Units: {advanced_oso}")
    print(f"Sirens: {sirens}")
