
import pygame
import os
import random

# Global playlist and index state
playlist = []
playlist_index = 0

def set_music_volume(volume):
    pygame.mixer.music.set_volume(volume)

def load_playlist(folder="Media/Loops", reverse=False):
    global playlist, playlist_index
    if not os.path.exists(folder):
        print(f"[ERROR] Playlist folder '{folder}' not found.")
        playlist = []
        return []

    tracks = [f for f in os.listdir(folder) if f.endswith(".mp3")]
    if "Time Over Function.mp3" in tracks:
        tracks.remove("Time Over Function.mp3")
        random.shuffle(tracks)
        if reverse:
            tracks = list(reversed(tracks))
        tracks.insert(0, "Time Over Function.mp3")
    else:
        random.shuffle(tracks)
        if reverse:
            tracks = list(reversed(tracks))

    playlist = [os.path.join(folder, track) for track in tracks]
    playlist_index = 0
    return playlist

def play_current_track():
    global playlist, playlist_index
    if not playlist:
        print("[AUDIO] Playlist is empty.")
        return
    pygame.mixer.init()
    pygame.mixer.music.load(playlist[playlist_index])
    pygame.mixer.music.play()
    print(f"[AUDIO] Now playing: {os.path.basename(playlist[playlist_index])}")

def next_track():
    global playlist, playlist_index
    if playlist_index < len(playlist) - 1:
        playlist_index += 1
        play_current_track()
    else:
        print("[AUDIO] Reached end of playlist.")

def previous_track():
    global playlist, playlist_index
    if playlist_index > 0:
        playlist_index -= 1
        play_current_track()
    else:
        print("[AUDIO] Already at start of playlist.")

def show_playlist():
    print("[AUDIO] Playlist:")
    for i, track in enumerate(playlist):
        now = "<-- now playing" if i == playlist_index else ""
        print(f"  {i+1:02d}. {os.path.basename(track)} {now}")

def stop_playlist():
    pygame.mixer.music.stop()
    print("[AUDIO] Playlist stopped.")

def reverse_audio_file(filepath):
    try:
        from pydub import AudioSegment
        sound = AudioSegment.from_file(filepath)
        reversed_sound = sound.reverse()
        reversed_path = filepath.replace(".mp3", "_reversed.mp3")
        reversed_sound.export(reversed_path, format="mp3")
        return reversed_path
    except Exception as e:
        print(f"[ERROR] Reversing failed: {e}")
        return None

def play_reversed_song(song_name, folder="Media/Loops"):
    song_path = os.path.join(folder, song_name)
    if not os.path.exists(song_path):
        print(f"[ERROR] File '{song_name}' not found in {folder}.")
        return

    reversed_path = reverse_audio_file(song_path)
    if reversed_path:
        pygame.mixer.init()
        pygame.mixer.music.load(reversed_path)
        pygame.mixer.music.play()
        print(f"[AUDIO] Playing reversed: {song_name}")

shuffle_enabled = True

def toggle_shuffle():
    global shuffle_enabled
    shuffle_enabled = not shuffle_enabled
    print(f"[AUDIO] Shuffle {'enabled' if shuffle_enabled else 'disabled'}.")

def shuffle_playlist():
    global playlist, playlist_index
    random.shuffle(playlist)
    playlist_index = 0
    play_current_track()

