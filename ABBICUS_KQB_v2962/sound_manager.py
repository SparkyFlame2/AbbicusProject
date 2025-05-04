
import os
import random
import pygame

try:
    pygame.mixer.init()
    print("[AUDIO] Pygame mixer initialized successfully.")
except Exception as e:
    print(f"[AUDIO ERROR] Failed to initialize pygame mixer: {e}")

playlist = []
current_index = 0
repeat = False
shuffle = False

# Volume state
music_volume = 1.0
sfx_volume = 1.0
music_muted = False
sfx_muted = False

def load_playlist(folder, ext='.mp3'):
    global playlist, current_index
    try:
        playlist = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(ext)]
        current_index = 0
        print(f"[AUDIO] Loaded playlist with {len(playlist)} track(s) from {folder}")
        if shuffle:
            random.shuffle(playlist)
    except Exception as e:
        print(f"[AUDIO ERROR] Could not load playlist: {e}")

def play_current():
    if not playlist:
        print("[AUDIO] Playlist is empty.")
        return
    try:
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.set_volume(0.0 if music_muted else music_volume)
        pygame.mixer.music.play()
        print(f"[AUDIO] Now playing: {playlist[current_index]}")
    except Exception as e:
        print(f"[AUDIO ERROR] Failed to play current track: {e}")

def play_once(path):
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.0 if music_muted else music_volume)
        pygame.mixer.music.play()
        print(f"[AUDIO] Playing once: {path}")
    except Exception as e:
        print(f"[AUDIO ERROR] Failed to play: {path} | {e}")

def play_sfx(path):
    try:
        sfx = pygame.mixer.Sound(path)
        sfx.set_volume(0.0 if sfx_muted else sfx_volume)
        sfx.play()
        print(f"[SFX] Playing: {path}")
    except Exception as e:
        print(f"[SFX ERROR] {e}")

def set_music_volume(level):
    global music_volume
    music_volume = max(0.0, min(1.0, float(level)))
    if music_muted:
        print(f"[AUDIO] Music is muted. Volume set internally to {music_volume}")
    else:
        pygame.mixer.music.set_volume(music_volume)
        print(f"[AUDIO] Music volume now: {music_volume}")

def set_sfx_volume(level):
    global sfx_volume
    sfx_volume = max(0.0, min(1.0, float(level)))
    print(f"[SFX] Volume set to {sfx_volume} (applies to next SFX)")

def mute_music():
    global music_muted
    music_muted = True
    pygame.mixer.music.set_volume(0.0)
    print("[AUDIO] Music muted.")

def unmute_music():
    global music_muted
    music_muted = False
    pygame.mixer.music.set_volume(music_volume)
    print("[AUDIO] Music unmuted.")

def mute_sfx():
    global sfx_muted
    sfx_muted = True
    print("[SFX] SFX muted.")

def unmute_sfx():
    global sfx_muted
    sfx_muted = False
    print("[SFX] SFX unmuted.")

def next_track():
    global current_index
    if not playlist:
        print("[AUDIO] No playlist loaded.")
        return
    current_index = (current_index + 1) % len(playlist)
    play_current()

def prev_track():
    global current_index
    if not playlist:
        print("[AUDIO] No playlist loaded.")
        return
    current_index = (current_index - 1 + len(playlist)) % len(playlist)
    play_current()

def toggle_repeat():
    global repeat
    repeat = not repeat
    print(f"[AUDIO] Repeat is now {'ON' if repeat else 'OFF'}.")

def toggle_shuffle():
    global shuffle
    shuffle = not shuffle
    print(f"[AUDIO] Shuffle is now {'ON' if shuffle else 'OFF'}.")
    if shuffle:
        random.shuffle(playlist)

def stop_playback():
    pygame.mixer.music.stop()
    print("[AUDIO] Playback stopped.")

def stop():
    """Stops all currently playing music."""
    pygame.mixer.music.stop()
    print("[AUDIO] All audio stopped.")

def handle_command(cmd, arg=None):
    cmd = cmd.lower().strip()
    if cmd == "-next":
        next_track()
    elif cmd == "-prev":
        prev_track()
    elif cmd == "-repeat":
        toggle_repeat()
    elif cmd == "-shuffle":
        toggle_shuffle()
    elif cmd == "-stop playback":
        stop_playback()
    elif cmd == "-mute music":
        mute_music()
    elif cmd == "-unmute music":
        unmute_music()
    elif cmd == "-mute sfx":
        mute_sfx()
    elif cmd == "-unmute sfx":
        unmute_sfx()
    elif cmd == "-set music volume" and arg is not None:
        set_music_volume(arg)
    elif cmd == "-set sfx volume" and arg is not None:
        set_sfx_volume(arg)
    else:
        print("[AUDIO] Unknown command.")
