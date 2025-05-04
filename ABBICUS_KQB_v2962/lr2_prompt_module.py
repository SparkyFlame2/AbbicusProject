
# lr2_prompt_module.py – Clean Rebuild (v2.8+)

import random

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
