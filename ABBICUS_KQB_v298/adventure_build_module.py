
# adventure_build_module.py

import os
import random
from datetime import datetime

def build_from_file(filename, word_target=1500):
    path = os.path.join("lore", filename)
    if not os.path.exists(path):
        print(f"[ERROR] Lore file '{filename}' not found in /lore/")
        return

    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if len(line.strip()) > 40]

    if not lines:
        print(f"[NOTICE] File '{filename}' contained no usable narrative lines.")
        return

    random.shuffle(lines)
    selected_lines = []
    word_total = 0

    for line in lines:
        word_total += len(line.split())
        selected_lines.append(line)
        if word_total >= word_target:
            break

    print(f"==[ADVENTURE BUILD FROM: {filename.upper()}]==")
    print(f"Total scenes: {len(selected_lines)} | Estimated read time: {word_total // 100} minutes")
    print("=" * 50)

    for i, line in enumerate(selected_lines):
        stamp = datetime.now().strftime("%H:%M:%S")
        print(f"--- SCENE {i+1} [{stamp}] ---")
        print(line + "\n")
        input("[ENTER to continue...]")
