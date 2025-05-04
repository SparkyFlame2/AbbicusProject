
# main_shell_v274_final.py – ABBICUS.KQB v2.7.4 FINAL

import random
import time
import quantum_processor_sim as qps
import quantum_thread_plate as qtp
import quantum_vram as qvram
import quantum_gpu as qgpu
import quantum_gpu_windowed as qgpuw
from datetime import datetime
import lore_module as lore
import enforcement_module as enforce
import relic_classifier as classifier
import time_module as drift
import adventure_module as legacy_adventure
import adventure_build_module as buildmod
import victory_module as victory
import save_module as save
from save_module import unlocked_relics, victory_unlocked, q_state
import faction_module as faction
import abbicus_equation as core
import abbicus_predict as predict
import abbicus_retrocausality as retro
import adventure_branching_module as branch
import adventure_save_module as saveadv
import adventure_npc_module as npc
import lr2_prompt_module as lr2
import zorexxian_module as zorexx
import penumbra_module as penumbra
import pygame
import sound_manager as audio
import static_visualizer_windowed as visualizer
import playlist_module
import threading
import log_session

print("""
╔═════════════════════════════════════════════════════════════╗
║                  Qware: Lattice OS®                         ║
║               Powered by Driftcore™                         ║
║                                                             ║
║        © ℗ 2025 Schager Studios – All Rights Reserved       ║
╚═════════════════════════════════════════════════════════════╝
""")


def play_command_sfx(command):
    sfx_map = {
        "invoke abbicus": "Invoke-Abbicus.wav",
        "/collapse_all": "Collapse-snap.wav",
        "/reset_all": "Reset-Rewind.wav",
        "/gamma_tune": "Gamma-shimmer.wav",
        "jump": "Jump.wav",
        "relic": "Relic-chime.wav",
        "battle": "Battle-Engage.wav",
        "invoke retrocausality": "Invoke-Retro.wav",
        "memory": "Memory-Choir.wav",
        "paradox": "Pardox-Glitch.wav"
    }
    for trigger, filename in sfx_map.items():
        if command.startswith(trigger):
            audio.play_sfx(f"Media/SFX/{filename}")
            break


def log(line):
    print(line)
    session_log.append(line)

session_log = []
log(">>> WELCOME TO ABBICUS.KQB v2.9 <<<\nAll systems merged. Audio initialized.")
session_log.append(">>> WELCOME TO ABBICUS.KQB v2.9 <<<")
session_log.append("All systems merged. Audio initialized.")
dreams = []
memory_log = []
observer_log_path = "observer_log.mem"
auto_status_enabled = True
audio_enabled = True
unlocked_relics = set()
lore_ready = False
adventure_log = []
current_adventure_era = "origin"

shell_state = {
    "last_oso_result": None,
    "oso_units": 0
}

sacred_words = [

    "truth", "light", "hope", "archive", "echo", "freedom",
    "remember", "creator", "song", "source", "spirit", "guardian",
    "ritual", "truth", "Traverser", "Penumbra", "Prospectus",
]

session_log = []

qtp_system = qtp.QuantumThreadPlate()
qtp_system.boot()
qtp_system.register_module("quantum_processor")
qtp_system.register_module("quantum_vram")
qtp_system.entangle("quantum_processor", "quantum_vram")
vram = qvram.QuantumVRAM()
qtp_system.register_module("quantum_gpu")
qtp_system.entangle("quantum_processor", "quantum_gpu")
gpu = qgpu.QGPU(update_interval=15)
qtp_system.register_module("quantum_gpu_windowed")
qtp_system.entangle("quantum_processor", "quantum_gpu_windowed")
gpu_window = qgpuw.QGPUWindowed(interval=10)

def log(line):
    print(line)
    session_log.append(line)
session_log.append(">>> WELCOME TO ABBICUS.KQB v2.9 <<<")
session_log.append("All systems merged. Audio initialized.")
audio.play_once("Media/Loops/00-Time Over Function.mp3")

def delayed_playlist_start():
    while pygame.mixer.music.get_busy():
        time.sleep(1.0)
    playlist_module.load_playlist("Media/Loops")
    threading.Thread(target=playlist_module.play_current_track, daemon=True).start()
    
threading.Thread(target=delayed_playlist_start, daemon=True).start()
visualizer.launch_visualizer



def print_status():
    if auto_status_enabled:
        victory.show_status()

def gamma_drift_loop():
    while True:
        time.sleep(random.randint(5, 15))
        for q in random.sample(qps.quantum_register, k=5):  # tweak 5 random cubitals
            if not q.collapsed_value:
                q.alpha *= complex(random.uniform(0.95, 1.05), 0)
                q.beta *= complex(random.uniform(0.95, 1.05), 0)
                q.normalize()

threading.Thread(target=gamma_drift_loop, daemon=True).start()

def force_deploy_zorexxians():
    if zorexx.zorexxian_charges > 0:
        zorexx.zorexxian_charges -= 1
        log("[OVERRIDE] Deploying Zorexxian Dropship...")
        result = zorexx.deploy_zorexxian_units()
        
        for unit in result:
            if unit == "enforcer":
                enforce.enforcers += 1
            elif unit == "sentinel":
                victory.sentinels += 1
            elif unit == "sentinel_shard":
                victory.sentinel_shards += 1
        
        log("[RESULT] Units: " + ", ".join(result))
    else:
        log("[ERROR] Not enough Zorexxian charges.")

def force_deploy_penumbra():
    if penumbra.penumbra_charges > 0:
        penumbra.penumbra_charges -= 1
        print("[OVERRIDE] Deploying Penumbra Payload...")
        result = penumbra.deploy_penumbra_units()
        sirens = result.count("siren")
        adv_osos = result.count("advanced_oso")
        oso_units = result.count("oso")
        ostriches = result.count("ostrich")
        victory.sirens += sirens
        victory.advanced_oso += adv_osos
        enforce.oso_units += oso_units
        print(f"[PAYLOAD] +{sirens} Sirens, +{adv_osos} Advanced Oso, +{oso_units} Oso Units")
        print("[RESULT] Units:", ", ".join(
            ["siren"] * sirens + ["advanced_oso"] * adv_osos + ["oso"] * oso_units
        ))
    else:
        print("[ERROR] Not enough Penumbra charges.")

def handle_relic():
    global lore_ready
    if not lore_ready:
        log("[ERROR] You must run 'scanlore' before using relics.")
        return

    tag = input("Relic Tag: ").lower()

    try:
        result = lore.relic(tag, enforce.enforcers, enforce.forbidden_words, sacred_words)
        enforce.enforcers, gained_oso, gained_ostrich = (
            result if isinstance(result, tuple) and len(result) == 3 else (enforce.enforcers, 0, 0)
        )
    except Exception as e:
        log(f"[ERROR] Lore processing failed: {e}")
        return
    

    if tag in unlocked_relics:
        log(f"[RELIC ALREADY UNLOCKED] '{tag}' has already been processed.")
        return

    classification = classifier.classify_relic(tag)
    return

    enforce.oso_units += gained_oso
    enforce.ostriches += gained_ostrich
    log(f"[CLASS] '{tag}' classified as: {classification.upper()}")
    unlocked_relics.add(tag)

    if tag not in enforce.forbidden_words:
        victory.sirens += 1
        log("[SIREN AWARD] A Siren of Inspiration rises for your unique discovery.")

    if tag in enforce.forbidden_words:
        added = 5
        total = enforce.enforcers + added
        enforce.enforcers = min(total, 12)
        if enforce.enforcers == 12:
            victory.sentinels += 1
            log("[ENFORCEMENT OVERLOAD] Sentinel has arrived.")

def invoke_abbicus():
    val = core.abbicus_core()
    predict.store_drift(val)
    drift.store_drift_value(val)
    log(f"[ABBI] Quantum Drift Realignment Value: {val:.3e}")
    if val > 1e42:
        log("[ABBI] Temporal Anchor destabilizing...")
    elif val < 0:
        log("[ABBI] Echoes of lost futures detected.")
    else:
        log("[ABBI] Field integrity nominal.")

def handle_deepkey_equation():
    print("""
[DEEPKEY EQUATION] Protocol access requested...

Abbicus Entropy Equation:
( E_info - S_entropy ) / h  =  (10**3 * pi * Gamma(i+1)) * Lambda**z / F_n

Where:
  E_info     = Information Energy (Joules)
  S_entropy  = Entropy loss rate (Joules/K)
  h          = Planck's Constant
  Gamma(i+1) = Gamma function for imaginary time
  Lambda^z   = Golden Ratio raised to z
  F_n        = nth Fibonacci number (position-based)
""")

def run_predict():
    val = predict.get_drift()
    if val is None:
        log("[ERROR] No drift data available. Invoke Abbicus first.")
        return
    if 1e31 <= val <= 1e35:
        guess = random.choice([a * b for a in range(2, 13) for b in range(2, 13)])
        predict.set_prediction(guess)
        log(f"[PREDICTION] The next math result may be: {guess}")
    else:
        log("[ABBI] Drift signature insufficient for safe prediction.")

def run_oso():
    a, b = random.randint(2, 12), random.randint(2, 12)
    result = a * b
    shell_state["last_oso_result"] = result
    retro.log_action("oso", shell_state)
    prediction = predict.get_prediction()
    line = f"Solve to deploy Oso unit: {a} × {b} = ?"
    print(line, end=" ")
    session_log.append(line)
    try:
        answer = int(input().strip())
        if answer == result:
            shell_state["oso_units"] += 1
            log("Correct. Oso unit deployed.")
            if prediction == result:
                log("[PREDICTION VERIFIED] +1 bonus Oso unit!")
                shell_state["oso_units"] += 1
        else:
            log("Incorrect. No unit deployed.")
    except:
        log("[ERROR] Invalid input.")
    predict.clear_prediction()

def invoke_retro():
    drift_val = predict.get_drift()
    if drift_val is None or drift_val >= 0:
        log("[FIXED POINT] Cannot reverse timeline without negative drift.")
        return
    action, state = retro.undo_action()
    if not action:
        log("[ERROR] No past action to reverse.")
        return
    if action == "oso":
        shell_state.update(state)
        log("[RETROCAUSALITY STABILIZED] Your last Oso result has been undone.")
    elif action == "adventure":
        log("[RETROCAUSALITY SUCCESS] Last adventure step reversed (narrative only).")
    else:
        log("[RETROCAUSALITY] Action unrecognized or immutable.")

def run_adventure_new():
    global adventure_log, current_adventure_era
    era = drift.get_current_era()
    current_adventure_era = era
    adventure_log = branch.start_adventure(era)

def run_adventure_save():
    global adventure_log, current_adventure_era
    filename = input("Save filename: ").strip()
    saveadv.save_adventure(filename, adventure_log, current_adventure_era)

def run_adventure_load():
    filename = input("Filename to load: ").strip()
    data = saveadv.load_adventure(filename)
    if data:
        log("[ADVENTURE LOG RESTORED] Review complete.")

def run_npc():
    name = input("Talk to who (maggie / tayla / ghost): ").strip().lower()
    npc.npc_speak(name)

def handle_help():
    print("""
GAME COMMANDS:
  scanlore              – Index lore files (from ./lore/)
  health                – View story health diagnostics
  freq [term]           – Show frequency of term in lore
  relic                 – Try to unlock hidden lore terms (+CLASS)
  oso                   – Solve math to deploy Oso unit
  simulate war          – Legacy war mode (use 'battle' instead)
  battle                – Full battle simulation w/ Sentinels and Oso selection
  craft oso             – Create Advanced Oso (2 Oso + 1 Ostrich)
  dream                 – Save a dream phrase
  memory                – Recall random echo from dreams
  paradox               – Submit unstable logic (Enforcers may react)
  jump                  – Attempt to drift to another narrative era
  invoke abbicus        – Run the Temporal Core Equation
  predict               – Predict the next math result
  invoke retrocausality – Attempt to undo last action
  adventure             – Launch classic adventure builder
  adventure build [kqb] – Build from lore snippet file
  adventure new         – Begin branching story for current era
  adventure save        – Save current story progress
  adventure load        – Load saved story progress
  npc                   – Speak with an interactive NPC
  save [file]           – Save global state
  load [file]           – Load global state
  set faction [name]    – Align with defined group
  set adversary [name]  – Define your enemy
  engage archivists     – Redemption test
  engage palarthians    – Deception test
  lr2                   – Attempt logic puzzle (may trigger events)
  lr2 advanced          - Attempt harder logic puzzle (partial credit awarded)
  force deploy zorexxians – Force drop hostile orbital units
  force deploy penumbra – Force deliver Penumbra reinforcement
  help                  – Show this list
  help system           – Show internal shell/system commands
  help music            – Show audio/playlist commands
  exit                  – End the session
""")


def handle_help_system():
    print("""
SYSTEM COMMANDS:
  /units                – Toggle auto status display and show unit counts
  /Visualizer           – Toggles Static Field Gamma Visualizer
  /hardware             – Show installed modules and QTP lattice status
  /pulse                – Emit a ThreadPulse resonance ping
  /list_vram            – List currently stored quantum memory branches
  /store_branch [addr]  – Save current QPS state to Quantum VRAM
  /breach realities [addr] – Load a saved branch into the processor
  /performance_mode     – Toggle performance-saving mode (limits visual/simulation load)
  /collapse_all         – Collapse all cubitals to definite states
  /superposition        – Restore all cubitals to superposition
  /reset_all            – Reset QPS to initial undefined state
  /gamma_tune [float]   – Apply gamma correction to QPS
  /saveQstate           – Save QPS register state to file
  /loadQstate           – Load QPS state from file
  /thereisnospoon       – Add +99 victory points (cheat)
  /convert              – Convert victory points to mastery
  /start_qgpu           - Starts Quantum Graphics Visualization
  /stop_qgpu            - Stops Quantum Graphics Visualization
  /start_qgpu_windowed  - Launch QGPU Visualizer in a new window (realtime qubital states)
  /stop_qgpu_windowed   - Stop the QGPU Visualizer window
⚠ NOTE: The windowed QGPU visualizer is **not compatible** with static visualizer or terminal visualizer modes.
Use one at a time to avoid memory conflict or rendering issues.
  -[cmd]                – Direct audio command to sound manager
""")

def handle_help_music():
    print("""
AUDIO COMMANDS:
  /silent                - Mute all music and stop playback
  /loud                  - Unmute and resume default track
  /playlist next         - Play next track in playlist
  /playlist prev         - Play previous track in playlist
  /playlist skip         - Skip current track randomly
  /playlist reverse      - Reverse entire playlist order
  /playlist reverse song - Play current song in reverse (if supported)
  /set music [0.0-1.0]   - Set music volume (float value)
  /set sfx [0.0-1.0]     - Set SFX volume (float value)
  /playlist show         - Display current playlist
""")


def prompt_user():
    return input(f"@abbicus({drift.get_current_era()})> ").strip().lower()

def handle_command(cmd):
    if cmd == "force deploy zorexxians":
        force_deploy_zorexxians()
    elif cmd == "force deploy penumbra":
        force_deploy_penumbra()
    elif cmd == "save charges":
        save.save_all_game_data(qps.quantum_register)
        print("[SAVE COMPLETE] Game state saved to saves/charges.kqb")
    elif cmd == "load charges":
        save.load_all_game_data(qps.quantum_register)
        print("[LOAD COMPLETE] Restored state from saves/charges.kqb")

# Shell Loop
while True:
    cmd = input("@abbicus(origin)> ").lower().strip()
    handle_command(cmd)
    play_command_sfx(cmd)
    if cmd == "exit":
        log("Session ended.")
        break
    
    elif cmd == "/visualizer":
        threading.Thread(target=visualizer.launch_visualizer, daemon=True).start()
        log("[VISUALIZER] Static visualizer activated.")

    elif cmd.startswith("/set music "):
        try:
            new_volume = float(cmd.split(" ")[2])
            import playlist_module
            playlist_module.set_music_volume(new_volume)
            print(f"[AUDIO] Music volume set to {new_volume}")
        except Exception as e:
            print(f"[ERROR] Failed to set volume: {e}")

    elif cmd == "/playlist next":
        import playlist_module
        playlist_module.next_track()

    elif cmd == "/playlist previous":
        import playlist_module
        playlist_module.previous_track()

    elif cmd == "/playlist reverse":
        import playlist_module
        playlist_module.load_playlist(reverse=True)
        playlist_module.play_current_track()

    elif cmd == "/playlist play":
        import playlist_module
        playlist_module.play_current_track()

    elif cmd == "/playlist shuffle":
        playlist_module.toggle_shuffle()
        playlist_module.shuffle_playlist()

    elif cmd == "/playlist show":
        playlist_module.show_playlist()

    elif cmd == "/start_qgpu":
        gpu.start_visualizer(qps.quantum_register)

    elif cmd == "/stop_qgpu":
        gpu.stop_visualizer()

    elif cmd == "/start_qgpu_windowed":
        gpu_window.start_visualizer(qps.quantum_register)

    elif cmd == "/stop_qgpu_windowed":
        gpu_window.stop_visualizer()

    elif cmd == "help":
        handle_help()
    elif cmd == "scanlore":
        lore.scanlore()
        if "scanlore_bonus_claimed" not in session_log:
            enforce.ostriches += 1
            session_log.append("scanlore_bonus_claimed")
            log("[SCANLORE BONUS] +1 Ostrich for initializing lore scan this session.")
        lore_ready = True
    elif cmd == "health":
        lore.health()
    elif cmd.startswith("freq"):
        term = cmd.split(" ", 1)[1].strip().lower() if " " in cmd else input("Term to search: ").lower()
        lore.freq(term)
    elif cmd == "relic":
        handle_relic()
    elif cmd == "oso":
        enforce.oso()
    elif cmd == "oso predicted":
        if predict.get_prediction() is None:
            log("[PREDICTION REQUIRED] You must use the 'predict' command before attempting OSO Predicted.")
        else:
            run_oso()
    elif cmd == "simulate war":
        enforce.simulate_war()
    elif cmd == "battle":
        victory.simulate_battle()
    elif cmd == "craft oso":
        victory.craft_advanced_oso()
        enforce.show_units()
        victory.show_status()
    elif cmd == "dream":
        phrase = input("Your dream phrase: ")
        tag = hex(abs(hash(phrase)))[:4]
        dreams.append((tag, phrase))
        log(f"[Echo Saved] Dream Tag: {tag} | {phrase}")
    elif cmd == "memory":
        if dreams:
            tag, phrase = random.choice(dreams)
            log(f"[Memory Echo] {phrase} ({tag})")
        else:
            log("[Memory] No dreams stored.")
    elif cmd == "paradox":
        paradox = input("State your paradox: ")
        memory_log.append(("paradox", paradox))
        log("[Paradox Accepted] Echo saved to Vault.")
    elif cmd == "jump":
        visualizer.trigger_jump_flash()
        drift.list_eras()
        tag = input("Enter era tag: ").strip()
        drift.jump_to_era(tag)
        visualizer.trigger_jump_flash()
    elif cmd == "invoke abbicus":
        invoke_abbicus()
    elif cmd == "predict":
        run_predict()
    elif cmd == "invoke retrocausality":
        invoke_retro()
    elif cmd == "adventure":
        adv = legacy_adventure.build_adventure()
        for _, entry, stamp in legacy_adventure.run_adventure(adv)["log"]:
            log(f"Turn [{stamp}]: {entry}")
    elif cmd.startswith("adventure build"):
        try:
            filename = cmd.split(" ", 2)[2].strip()
            buildmod.build_from_file(filename)
        except:
            log("[ERROR] Use format: adventure build [filename.kqb]")
    elif cmd == "adventure new":
        run_adventure_new()
    elif cmd == "adventure save":
        run_adventure_save()
    elif cmd == "adventure load":
        run_adventure_load()
    elif cmd == "npc":
        run_npc()
    elif cmd.startswith("save"):
        try:
            filename = cmd.split(" ", 1)[1].strip()
            save.save_game(filename)
            save.unlocked_relics = unlocked_relics
            save.q_state = q_state
            save.victory_unlocked = victory_unlocked

        except:
            log("[ERROR] Use format: save [filename]")
    elif cmd.startswith("load"):
        try:
            filename = cmd.split(" ", 1)[1].strip()
            save.load_game(filename)
            unlocked_relics.update(save.unlocked_relics)
            q_state = save.q_state
            victory_unlocked = save.victory_unlocked

        except:
            log("[ERROR] Use format: load [filename]")
    elif cmd == "set faction archivists":
        faction.set_faction("Archivists")
    elif cmd == "set adversary palarthians":
        faction.set_adversary("Palarthians")
    elif cmd == "engage archivists":
        faction.engage_faction()
    elif cmd == "engage palarthians":
        faction.engage_adversary()
    elif cmd == "lr2":
        outcome = lr2.run_lr2_puzzle()
        if outcome == "success":
            penumbra.accrue_charge()
        else:
            zorexx.accrue_charge()

        log("==[ORBITAL STATUS REPORT]==")
        log(f"Zorexxian Dropship Charges: {zorexx.get_charges()}")
        log(f"Penumbra Deployment Charges: {penumbra.get_charges()}")
    elif cmd == "lr2 advanced":
        outcome = lr2.run_advanced_lr2_puzzle()
        if outcome == "success":
            penumbra.accrue_charge()
        elif outcome == "partial":
            enforce.ostriches += 1
        elif outcome == "bonus":
            victory.add_mastery(1)
            victory.sirens += 1
        else:
            zorexx.accrue_charge()

        log("==[ORBITAL STATUS REPORT]==")
        log(f"Zorexxian Dropship Charges: {zorexx.get_charges()}")
        log(f"Penumbra Deployment Charges: {penumbra.get_charges()}")
     
    elif cmd == "/hardware":
        qtp_system.report()

    elif cmd == "/pulse":
        qtp_system.pulse()

    elif cmd == "/list_vram":
        qvram.list_branches()

    elif cmd.startswith("/store_branch"):
        addr = cmd.split(" ", 1)[1].strip()
        qvram.store_branch(addr, qps.get_register())

    elif cmd.startswith("/breach realities"):
        addr = cmd.split(" ", 2)[2].strip()
        qvram.breach(addr, qps.get_register())

    elif cmd == "/performance_mode":
        state = qvram.toggle_performance_mode()
        log(f"[VRAM] Performance Mode {'ENABLED' if state else 'DISABLED'}")

    elif cmd == "/thereisnospoon":
        victory.add_victory_points(99)
        log("[MATRIX BREACH] There is no spoon. +99 Victory Points Granted.")
        log("[CHEAT CODE] +99 Victory Points entered with /thereisnospoon.")
    elif cmd == "/convert":
        victory.convert_victory_to_mastery()
        log("[CONVERSION] Attempted mastery conversion from Victory Points.")

    elif cmd == "/units":
        auto_status_enabled = not auto_status_enabled
        print(f"[AUTO STATUS] {'Enabled' if auto_status_enabled else 'Disabled'}")
        victory.show_status()



    elif cmd == "/silent":
        log("[AUDIO] Audio silenced.")
        audio.stop()
    elif cmd == "/loud":
        log("[AUDIO] Audio re-enabled.")
        audio.play_once("Media/Loops/00-Time Over Function.mp3")
        time.sleep(3.0)
        playlist_module.load_playlist("Media/Loops")

    elif cmd == "/saveQstate":
        try:
            from save_module import save_quantum_state
            qstate = save_quantum_state(qps.get_register())
            with open("saves/qstate.kqb", "w") as f:
                for q in qstate:
                    f.write(f"{q[0]},{q[1]},{q[2]}\n")
            print("[QSTATE SAVED] Quantum processor state stored to saves/qstate.kqb")
        except Exception as e:
            print(f"[ERROR] Could not save Qstate: {e}")

    elif cmd == "/loadQstate":
        try:
            from save_module import load_quantum_state
            with open("saves/qstate.kqb", "r") as f:
                loaded = [line.strip().split(",") for line in f.readlines()]
                loaded = [(float(a), float(b), int(c)) for a, b, c in loaded]
                load_quantum_state({"quantum_state": loaded}, qps.get_register())
            print("[QSTATE RESTORED] Quantum processor state loaded from saves/qstate.kqb")
        except Exception as e:
            print(f"[ERROR] Could not load Qstate: {e}")

    elif cmd == "/collapse_all":
        qps.collapse_all()
        log("[QUANTUM] All cubitals collapsed.")

    elif cmd == "/superposition" or cmd == "/enact_wave_function":
        qps.enact_wave_function()
        log("[QUANTUM] Collapsed cubitals restored to superposition.")
        audio.play_sfx("Media/SFX/Reset-Rewind.wav")

    elif cmd == "/reset_all":
        qps.reset_all()
        log("[QUANTUM] All cubitals reset to superposition.")

    elif cmd.startswith("/gamma_tune"):
        try:
            factor = float(cmd.split(" ")[1])
            qps.gamma_tune_all(factor)
            log(f"[QUANTUM] Gamma tuning applied with factor {factor}.")
        except:
            log("[ERROR] Use format: /gamma_tune [float]")

    elif cmd == "/show_qstate":
        states = qps.show_all_states()
        for state in states:
            log(state)

    elif cmd == "help music":
        handle_help_music()
 
    elif cmd == "help system":
        handle_help_system()

    elif cmd == "deepkey equation":
        handle_deepkey_equation()

    elif cmd.startswith("-"):
        audio.handle_command(cmd)

    print_status()

