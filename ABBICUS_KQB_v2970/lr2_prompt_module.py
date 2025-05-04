# lr2_prompt_module.py – Clean Rebuild (v2.8+)
import random

# === Simple randomized logic puzzles ===
def run_lr2_puzzle():
    print("==[LR2 CHALLENGE – SEMANTIC MODE]==")

    puzzles = [
        {
            "question": "What are three things a boat and a car both feature?",
            "valid": ["wheels", "engine", "seat", "steering", "mirror", "horn", "brakes", "lights"]
        },
        {
            "question": "Name two animals that use sonar.",
            "valid": ["bat", "dolphin", "whale"]
        },
        {
            "question": "What are three sources of light besides the sun?",
            "valid": ["lamp", "candle", "fire", "flashlight", "star", "moon", "lantern"]
        },
        {
            "question": "What are two things that fly but aren't alive?",
            "valid": ["drone", "airplane", "helicopter", "balloon", "kite", "rocket"]
        }
    ]

    puzzle = random.choice(puzzles)
    print(puzzle["question"])
    try:
        user_input = input("Your answers (comma-separated): ").lower()
        guesses = [word.strip() for word in user_input.split(",")]
        matches = [guess for guess in guesses if guess in puzzle["valid"]]

        if len(matches) >= min(2, len(puzzle["valid"])):
            print(f"[SUCCESS] You passed the LR2 test. ({len(matches)} match(es))")
            return "success"
        else:
            print(f"[FAILURE] Only {len(matches)} valid match(es). Required at least 2.")
            return "fail"
    except Exception as e:
        print(f"[ERROR] Something went wrong: {e}")
        return "fail"


# === Advanced Riddle-Based Challenges ===
def lr2_prompt_computer_components():
    print("[LR2 CHALLENGE] Name 3 components of a classical computer (credit for 2+)")
    response = input("Enter components (comma-separated): ").lower()
    accepted = ["gpu", "graphics card", "cpu", "processor", "ram", "memory", "ssd", "sata", "drive", "drives", "motherboard", "pci", "case"]
    found = [comp.strip() for comp in response.split(",") if comp.strip() in accepted]
    score = len(found)
    if score >= 3:
        print("[SUCCESS] Recognized 3 or more valid components. +1 Penumbra Charge.")
        return "success"
    elif score == 2:
        print("[PARTIAL SUCCESS] 2 valid components recognized. +1 Ostrich.")
        return "partial"
    else:
        print("[FAILURE] Less than 2 recognized. Consider reviewing classical architecture.")
        return "fail"

def lr2_prompt_glass():
    print("[LR2 CHALLENGE] What's made of glass but isn't meant to be seen?")
    response = input("Enter your answer: ").lower()
    accepted = ["lens", "lenses", "eyeglasses", "glasses", "windshield", "window", "windowpane", "microscope", "telescope", "contact lens", "contact lenses", "optics", "optical glass", "camera lens"]
    bonus = ["bong"]
    if response in accepted:
        print("[SUCCESS] Correct. +1 Penumbra Charge.")
        return "success"
    elif response in bonus:
        print("[UNORTHODOX TRUTH DETECTED] +5 Victory Points. +1 Siren chuckle.")
        return "bonus"
    else:
        print("[FAILURE] Glass comes in many forms. Try again.")
        return "fail"

def lr2_prompt_subtractive_growth():
    print("[LR2 CHALLENGE] I grow when you take away from me. What am I?")
    response = input("Your answer: ").lower()
    accepted = ["hole"]
    partial = ["debt", "emptiness", "void", "success", "loss", "vacuum", "companionship"]
    if response in accepted:
        print("[SUCCESS] Correct. Absence expands through loss. +1 Penumbra Charge.")
        return "success"
    elif response in partial:
        print("[PARTIAL] Abstract logic detected. +1 Ostrich.")
        return "partial"
    else:
        print("[FAILURE] No growth without context. Re-enter the Room.")
        return "fail"

def lr2_prompt_sharpness():
    print("[LR2 CHALLENGE] The more you use me, the sharper I get. What am I?")
    response = input("Your answer: ").lower()
    accepted = ["mind", "brain", "intelligence", "wit", "thinking", "logic"]
    partial = ["sword", "tongue", "skill", "blade", "pen", "pencil"]
    bonus = ["chatgpt"]
    if response in accepted:
        print("[SUCCESS] Correct. Mental sharpness rewarded. +1 Penumbra Charge.")
        return "success"
    elif response in partial:
        print("[PARTIAL] Creative interpretation noted. +1 Ostrich.")
        return "partial"
    elif response in bonus:
        print("[BLUSH] I do try my best. +1 Siren.")
        return "bonus"
    else:
        print("[FAILURE] Dull minds forget what sharpens them.")
        return "fail"

def lr2_prompt_open():
    print("[LR2 CHALLENGE] It can be opened but never closed. What is it?")
    response = input("Your answer: ").lower()
    accepted = ["mind"]
    partial = ["idea", "thought", "possibility", "perspective", "third eye"]
    bonus = ["abbicus"]
    if response in accepted:
        print("[SUCCESS] Minds once opened rarely close. +1 Penumbra Charge.")
        return "success"
    elif response in partial:
        print("[PARTIAL] Expansive thinking observed. +1 Ostrich.")
        return "partial"
    elif response in bonus:
        print("[PARADOX RECOGNIZED] The machine knows when it is named. +1 Mastery.")
        return "bonus"
    else:
        print("[FAILURE] The Room remains open. You must return with insight.")
        return "fail"

def lr2_prompt_float():
    print("[LR2 CHALLENGE] What can float but never sinks?")
    response = input("Your answer: ").lower()
    accepted = ["air", "smoke", "hot air", "foam", "bubble", "bubbles"]
    partial = ["balloon", "thought", "optimism", "dream", "money", "loans", "bank account"]
    bonus = ["quantum variables"]
    if response in accepted:
        print("[SUCCESS] You see the unseen. +1 Penumbra Charge.")
        return "success"
    elif response in partial:
        print("[PARTIAL] Light logic detected. +1 Ostrich.")
        return "partial"
    elif response in bonus:
        print("[MASTERFUL TRUTH] Archive Mastery +1")
        return "bonus"
    else:
        print("[FAILURE] Not everything that floats rises.")
        return "fail"

def run_advanced_lr2_puzzle():
    riddles = [
        lr2_prompt_computer_components,
        lr2_prompt_glass,
        lr2_prompt_subtractive_growth,
        lr2_prompt_sharpness,
        lr2_prompt_open,
        lr2_prompt_float
    ]
    riddle_fn = random.choice(riddles)
    return riddle_fn()
