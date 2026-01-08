# Vietnamese Vowels Learning App

A standalone application to learn Vietnamese vowels using the **Leitner System** for spaced repetition learning.

## Features

- **12 Vietnamese Vowels**: Learn all Vietnamese vowels (a, ă, â, e, ê, i, o, ô, ơ, u, ư, y)
- **Example Words**: Each vowel comes with common Vietnamese words
- **Audio Pronunciation**: Click to hear native pronunciation (requires internet for Google TTS)
- **Leitner System**: Scientifically proven spaced repetition for effective memorization
- **Progress Tracking**: Your progress is saved automatically

## The Leitner System

The app uses the Leitner System with 5 boxes:

- **Box 1**: Review every session (new cards start here)
- **Box 2**: Review every 2 sessions
- **Box 3**: Review every 4 sessions
- **Box 4**: Review every 8 sessions
- **Box 5**: Review every 16 sessions (mastered!)

- ✓ **Correct answer**: Card moves to the next box
- ✗ **Wrong answer**: Card goes back to Box 1

## Running the App

### Option 1: Run from Source

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python vietnamese_vowels.py
```

### Option 2: Build Standalone Executable

```bash
# Build the executable
python build.py

# The executable will be in the 'dist' folder
# On Windows: dist/VietnameseVowels.exe
# On Linux/Mac: dist/VietnameseVowels
```

## Requirements

- Python 3.8+
- tkinter (usually included with Python)
- gtts (Google Text-to-Speech)
- pygame (for audio playback)

## Vietnamese Vowels Chart

| Vowel | IPA | Sound Like |
|-------|-----|------------|
| a | /aː/ | 'a' in father |
| ă | /a/ | 'u' in cut (short) |
| â | /ə/ | 'u' in but (very short) |
| e | /ɛ/ | 'e' in bed |
| ê | /e/ | 'ay' in say (no glide) |
| i/y | /i/ | 'ee' in see |
| o | /ɔ/ | 'o' in hot (British) |
| ô | /o/ | 'o' in go (no glide) |
| ơ | /əː/ | 'u' in fur (no r) |
| u | /u/ | 'oo' in food |
| ư | /ɯ/ | 'oo' with unrounded lips |

## Progress Storage

Your learning progress is saved to:
- **Linux/Mac**: `~/.vietnamese_vowels/vowels_progress.json`
- **Windows**: `C:\Users\<you>\.vietnamese_vowels\vowels_progress.json`

## License

Free for personal and educational use.
