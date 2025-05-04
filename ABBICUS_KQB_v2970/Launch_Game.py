
import time
import os
import ascii_title_module as art
import sound_manager as audio


def show_title_text():
    print("""
    ==========================================
              THE A.B.B.I.C.U.S.
    Acute Binary Batch Integer Causality Utilization System

    A word-based math and combat challenge.
    ==========================================
    """)

def show_credits():
    print("""
    ==========================================
        Developed by Winston J. Lyle
        With cosmic assistance from ChatGPT-4o
        Voice of Abbi, keeper of echoes
        Special thanks to the Archivists
    ==========================================
    """)

def main():
    print("[ABBI] Initializing title sequence...\n")
    audio.play_once("Media/SFX/Title clicks.mp3")
    art.display_ascii_title()
    time.sleep(5)

    print("\n[ABBI] Clarifying text overlay...\n")
    audio.play_once("Media/SFX/Title clicks.mp3")
    show_title_text()
    time.sleep(10)

    print("\n[ABBI] Displaying credits...")
    audio.play_once("Media/SFX/Title clicks.mp3")
    show_credits()
    time.sleep(10)

    input("\n[ PRESS ENTER TO CONTINUE ]")
    print("\n[ABBI] Launching core interface...")
    os.system("py main_shell.py")

if __name__ == "__main__":
    main()
