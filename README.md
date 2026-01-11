# Vietnamese Vowels Learning App

A standalone application to learn Vietnamese vowels and tones using the **Leitner System** for spaced repetition learning.

## Features

- **48 Learning Cards**: Complete coverage of Vietnamese sounds
  - 6 Tones: ngang, sắc, huyền, hỏi, ngã, nặng
  - 12 Monophthongs (single vowels): a, ă, â, e, ê, i, o, ô, ơ, u, ư, y
  - 19 Diphthongs (vowel pairs): ai, ao, au, ay, ây, eo, êu, ia, iu, oi, ôi, ơi, ua, uê, ui, uo, ưa, ưi, ưu
  - 11 Triphthongs (triple vowels): iêu, yêu, oai, oay, oao, oeo, uây, uôi, ươi, ươu, uya
- **Tone Comparison**: See how the same syllable changes meaning with different tones
- **Example Words**: Each card comes with 4 common Vietnamese words and sentences
- **Audio Pronunciation**: Native Vietnamese pronunciation via Google TTS
- **Offline Audio Support**: Generate audio files once, use offline forever
- **Leitner System**: Scientifically proven spaced repetition for effective memorization
- **Progress Tracking**: Your progress is saved automatically
- **Reset Progress**: Start fresh anytime with the reset button
- **Responsive UI**: Works in both fullscreen and windowed mode with dynamic resizing
- **Steam-Inspired Dark Theme**: Easy on the eyes for extended study sessions
- **Animated Game-Style Buttons**: Smooth hover and press animations with color transitions
- **Customizable Study Sessions**: Set how many cards to review per session (5, 10, 15, 20, 25, 30, 50, or all)
- **Downloadable Content Packs**: Expand your vocabulary with specialized packs:
  - Manga, Fiction & Fantasy Pack (500+ words): Onomatopoeia, emotions, action words, fantasy terms
  - Self-Help & Personal Development Pack (300+ words): Mindset, goals, habits, productivity vocabulary
  - Doraemon Manga Pack (89 words): Essential vocabulary for reading Vietnamese Doraemon manga
  - Millennial Vocabulary Pack (86 words): Authentic Vietnamese slang and expressions
  - Gen Z Vocabulary Pack (90 words): Vietnamese abbreviations, cute speech, and youth expressions

## How It Works

1. **See a word** - A Vietnamese word appears on screen
2. **Guess the pronunciation** - Try to say it out loud
3. **Check your answer** - Click "Show Answer" to hear the correct pronunciation
4. **Rate yourself** - Three options:
   - **Wrong** - Card goes back to Box 1 for more practice
   - **Repeat** - Card goes to end of current deck (no scoring)
   - **Correct** - Card advances to the next box

## The Leitner System

The app uses the Leitner System with 5 boxes:

- **Box 1**: Review every session (new cards start here)
- **Box 2**: Review every 2 sessions
- **Box 3**: Review every 4 sessions
- **Box 4**: Review every 8 sessions
- **Box 5**: Review every 16 sessions (mastered!)

## Content Packs

Expand your vocabulary beyond vowels and tones with downloadable content packs:

### Available Packs

| Pack | Words | Description |
|------|-------|-------------|
| Manga, Fiction & Fantasy | 500+ | Onomatopoeia (bùm, xoẹt), exclamations (trời ơi!), action verbs, emotions, fantasy/manga terminology |
| Self-Help & Personal Development | 300+ | Mindset, goals, habits, productivity, relationships, finance vocabulary |
| Doraemon Manga | 89 | Gadgets (bảo bối, cửa thần kỳ), school life (bài tập, điểm kém), emotions (khóc, sợ), common phrases |
| Millennial Vocabulary | 86 | Authentic slang (gấu, thả thính, cẩu lương), internet terms (phốt, hóng, soi), expressions (đỉnh của chóp, xỉu) |
| Gen Z Vocabulary | 90 | Text abbreviations (bt, dc, ko, ny), cute speech (bùn, nhiu, hem), gaming terms (gánh, leo, rớt) |

### How to Use Content Packs

1. Click **CONTENT PACKS** on the home screen
2. Browse available packs and click **DOWNLOAD & INSTALL**
3. Click **STUDY NOW** to start learning pack vocabulary
4. Toggle packs on/off or reset progress as needed

Each pack has its own Leitner box system, so your progress is tracked separately.

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

## Audio Setup

The app supports two audio modes:

### Online Mode (Default)
- Uses Google Text-to-Speech
- Requires internet connection
- Works out of the box

### Offline Mode (Recommended)
Generate audio files once, then use offline forever:

```bash
# Generate all audio files (requires internet once)
python generate_audio.py

# This creates an 'audio' folder with .mp3 files
# The app will automatically use these files
```

When building the executable, audio files are bundled automatically if they exist.

## Requirements

- Python 3.8+
- tkinter (usually included with Python)
- gtts (Google Text-to-Speech)
- pygame (for audio playback)

## Vietnamese Reference

### The 6 Tones

| Tone | Mark | Pitch | Example |
|------|------|-------|---------|
| Ngang | (none) | mid-level | ma (ghost) |
| Sắc | ́ | rising | má (mother) |
| Huyền | ̀ | falling | mà (but) |
| Hỏi | ̉ | dipping-rising | mả (grave) |
| Ngã | ̃ | broken-rising | mã (horse) |
| Nặng | ̣ | low-falling | mạ (rice seedling) |

### Monophthongs (Single Vowels)

| Vowel | IPA |
|-------|-----|
| a | /aː/ |
| ă | /a/ |
| â | /ə/ |
| e | /ɛ/ |
| ê | /e/ |
| i/y | /i/ |
| o | /ɔ/ |
| ô | /o/ |
| ơ | /əː/ |
| u | /u/ |
| ư | /ɯ/ |

### Diphthongs (Vowel Pairs)

| Vowel | IPA | Example |
|-------|-----|---------|
| ai | /aːj/ | hai (two) |
| ao | /aːw/ | sao (star) |
| au | /aw/ | sau (after) |
| ay | /aj/ | tay (hand) |
| ây | /əj/ | đây (here) |
| eo | /ɛw/ | mèo (cat) |
| êu | /ew/ | kêu (to call) |
| ia | /iə/ | chia (to share) |
| iu | /iw/ | dịu (gentle) |
| oi | /ɔj/ | nói (to speak) |
| ôi | /oj/ | tôi (I/me) |
| ơi | /əːj/ | mới (new) |
| ua | /uə/ | mua (to buy) |
| uê | /ue/ | quê (hometown) |
| ui | /uj/ | vui (happy) |
| ưa | /ɯə/ | mưa (rain) |
| ưi | /ɯj/ | gửi (to send) |
| ưu | /ɯw/ | lưu (to save) |

### Triphthongs (Triple Vowels)

| Vowel | IPA | Example |
|-------|-----|---------|
| iêu | /iəw/ | nhiều (many) |
| yêu | /iəw/ | yêu (to love) |
| oai | /waːj/ | ngoài (outside) |
| oay | /waj/ | xoay (to rotate) |
| uôi | /uəj/ | đuôi (tail) |
| ươi | /ɯəj/ | người (person) |
| ươu | /ɯəw/ | rượu (alcohol) |
| uya | /wiə/ | khuya (late night) |

## Progress Storage

Your learning progress is saved to:
- **Linux/Mac**: `~/.vietnamese_vowels/vowels_progress.json`
- **Windows**: `C:\Users\<you>\.vietnamese_vowels\vowels_progress.json`

Content pack progress is saved separately in `content_packs_state.json` in the same directory.
Settings (like study limit) are saved in `settings.json` in the same directory.

Use the **Reset Progress** button on the home screen to start fresh (vowels/tones only).
Use the **Reset** button in Content Packs to reset individual pack progress.

## License

Free for personal and educational use.
