#!/usr/bin/env python3
"""
Generate offline audio files for Vietnamese Vowels App
Run this once to create all audio files, then they're bundled with the app.
"""

import os
from gtts import gTTS

# All Vietnamese vowels and example words
AUDIO_DATA = {
    # Vowels
    "a": None, "ă": None, "â": None, "e": None, "ê": None, "i": None,
    "o": None, "ô": None, "ơ": None, "u": None, "ư": None, "y": None,
    # Example words
    "ba": None, "cá": None, "nhà": None, "là": None,
    "ăn": None, "bắt": None, "năm": None, "tắm": None,
    "ân": None, "cấp": None, "lần": None, "sân": None,
    "em": None, "đẹp": None, "xe": None, "me": None,
    "bê": None, "đêm": None, "lễ": None, "tên": None,
    "đi": None, "bí": None, "khi": None, "thi": None,
    "con": None, "có": None, "to": None, "cho": None,
    "cô": None, "tô": None, "đô": None, "hồ": None,
    "mơ": None, "bơ": None, "cờ": None, "thơ": None,
    "mua": None, "thu": None, "du": None, "gấu": None,
    "từ": None, "sữa": None, "mưa": None, "thư": None,
    "ý": None, "hy": None, "lý": None, "ty": None,
}

def generate_audio_files():
    """Generate all audio files"""
    audio_dir = os.path.join(os.path.dirname(__file__), "audio")
    os.makedirs(audio_dir, exist_ok=True)

    total = len(AUDIO_DATA)
    for i, word in enumerate(AUDIO_DATA.keys(), 1):
        # Create safe filename
        filename = f"{word}.mp3"
        filepath = os.path.join(audio_dir, filename)

        if os.path.exists(filepath):
            print(f"[{i}/{total}] Skipping {word} (already exists)")
            continue

        print(f"[{i}/{total}] Generating: {word}")
        try:
            tts = gTTS(text=word, lang='vi', slow=False)
            tts.save(filepath)
        except Exception as e:
            print(f"  Error: {e}")

    print(f"\nDone! Audio files saved to: {audio_dir}")
    print(f"Total files: {len(os.listdir(audio_dir))}")

if __name__ == "__main__":
    generate_audio_files()
