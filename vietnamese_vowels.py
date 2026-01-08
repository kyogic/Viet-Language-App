#!/usr/bin/env python3
"""
Vietnamese Vowels Learning App
Uses the Leitner System for spaced repetition learning
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import sys
import random
import tempfile
import threading
from datetime import datetime, timedelta
from pathlib import Path

# Try to import audio libraries
try:
    from gtts import gTTS
    import pygame
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False

# Vietnamese vowels data with example words and pronunciations
VOWELS_DATA = {
    "a": {
        "description": "Like 'a' in 'father', but shorter",
        "ipa": "/aː/",
        "examples": [
            {"word": "ba", "meaning": "three / father", "sentence": "Ba người = Three people"},
            {"word": "cá", "meaning": "fish", "sentence": "Con cá = The fish"},
            {"word": "nhà", "meaning": "house / home", "sentence": "Nhà tôi = My house"},
            {"word": "là", "meaning": "is / to be", "sentence": "Đây là = This is"},
        ]
    },
    "ă": {
        "description": "Short 'a' sound, like 'u' in 'cut'",
        "ipa": "/a/",
        "examples": [
            {"word": "ăn", "meaning": "to eat", "sentence": "Ăn cơm = Eat rice"},
            {"word": "bắt", "meaning": "to catch", "sentence": "Bắt cá = Catch fish"},
            {"word": "năm", "meaning": "year / five", "sentence": "Năm nay = This year"},
            {"word": "tắm", "meaning": "to bathe", "sentence": "Tắm rửa = To wash"},
        ]
    },
    "â": {
        "description": "Like 'u' in 'but', very short",
        "ipa": "/ə/",
        "examples": [
            {"word": "ân", "meaning": "grace / favor", "sentence": "Ân huệ = Favor"},
            {"word": "cấp", "meaning": "level / urgent", "sentence": "Cấp bách = Urgent"},
            {"word": "lần", "meaning": "time (occurrence)", "sentence": "Lần đầu = First time"},
            {"word": "sân", "meaning": "yard / court", "sentence": "Sân bay = Airport"},
        ]
    },
    "e": {
        "description": "Like 'e' in 'bed'",
        "ipa": "/ɛ/",
        "examples": [
            {"word": "em", "meaning": "younger sibling / I (younger)", "sentence": "Em gái = Younger sister"},
            {"word": "đẹp", "meaning": "beautiful", "sentence": "Rất đẹp = Very beautiful"},
            {"word": "xe", "meaning": "vehicle", "sentence": "Xe máy = Motorbike"},
            {"word": "me", "meaning": "tamarind", "sentence": "Quả me = Tamarind fruit"},
        ]
    },
    "ê": {
        "description": "Like 'ay' in 'say' but without the glide",
        "ipa": "/e/",
        "examples": [
            {"word": "bê", "meaning": "calf (baby cow)", "sentence": "Con bê = The calf"},
            {"word": "đêm", "meaning": "night", "sentence": "Ban đêm = At night"},
            {"word": "lễ", "meaning": "ceremony / holiday", "sentence": "Ngày lễ = Holiday"},
            {"word": "tên", "meaning": "name", "sentence": "Tên tôi = My name"},
        ]
    },
    "i": {
        "description": "Like 'ee' in 'see'",
        "ipa": "/i/",
        "examples": [
            {"word": "đi", "meaning": "to go", "sentence": "Đi học = Go to school"},
            {"word": "bí", "meaning": "squash / secret", "sentence": "Bí mật = Secret"},
            {"word": "khi", "meaning": "when / monkey", "sentence": "Khi nào = When"},
            {"word": "thi", "meaning": "to take exam", "sentence": "Thi cử = Examination"},
        ]
    },
    "o": {
        "description": "Like 'o' in 'hot' (British English)",
        "ipa": "/ɔ/",
        "examples": [
            {"word": "con", "meaning": "child / animal classifier", "sentence": "Con chó = The dog"},
            {"word": "có", "meaning": "to have", "sentence": "Tôi có = I have"},
            {"word": "to", "meaning": "big", "sentence": "Rất to = Very big"},
            {"word": "cho", "meaning": "to give / for", "sentence": "Cho tôi = Give me"},
        ]
    },
    "ô": {
        "description": "Like 'o' in 'go' but without the glide",
        "ipa": "/o/",
        "examples": [
            {"word": "cô", "meaning": "aunt / miss", "sentence": "Cô giáo = Teacher (female)"},
            {"word": "tô", "meaning": "bowl", "sentence": "Tô phở = Bowl of pho"},
            {"word": "đô", "meaning": "dollar / capital", "sentence": "Đô la = Dollar"},
            {"word": "hồ", "meaning": "lake", "sentence": "Hồ nước = Lake"},
        ]
    },
    "ơ": {
        "description": "Like 'u' in 'fur' without the 'r'",
        "ipa": "/əː/",
        "examples": [
            {"word": "mơ", "meaning": "to dream / apricot", "sentence": "Giấc mơ = Dream"},
            {"word": "bơ", "meaning": "butter / avocado", "sentence": "Quả bơ = Avocado"},
            {"word": "cờ", "meaning": "flag / chess", "sentence": "Lá cờ = Flag"},
            {"word": "thơ", "meaning": "poetry", "sentence": "Bài thơ = Poem"},
        ]
    },
    "u": {
        "description": "Like 'oo' in 'food'",
        "ipa": "/u/",
        "examples": [
            {"word": "mua", "meaning": "to buy", "sentence": "Mua sắm = Shopping"},
            {"word": "thu", "meaning": "autumn / to collect", "sentence": "Mùa thu = Autumn"},
            {"word": "du", "meaning": "to travel", "sentence": "Du lịch = Tourism"},
            {"word": "gấu", "meaning": "bear", "sentence": "Con gấu = The bear"},
        ]
    },
    "ư": {
        "description": "Like 'oo' but with lips unrounded (smile while saying 'oo')",
        "ipa": "/ɯ/",
        "examples": [
            {"word": "từ", "meaning": "word / from", "sentence": "Từ điển = Dictionary"},
            {"word": "sữa", "meaning": "milk", "sentence": "Sữa tươi = Fresh milk"},
            {"word": "mưa", "meaning": "rain", "sentence": "Trời mưa = It's raining"},
            {"word": "thư", "meaning": "letter", "sentence": "Bức thư = A letter"},
        ]
    },
    "y": {
        "description": "Like 'ee' in 'see' (same as 'i')",
        "ipa": "/i/",
        "examples": [
            {"word": "ý", "meaning": "meaning / idea", "sentence": "Ý kiến = Opinion"},
            {"word": "hy", "meaning": "hope (in compounds)", "sentence": "Hy vọng = Hope"},
            {"word": "lý", "meaning": "reason / plum", "sentence": "Lý do = Reason"},
            {"word": "ty", "meaning": "company (short form)", "sentence": "Công ty = Company"},
        ]
    },
}


class LeitnerSystem:
    """
    Implements the Leitner System for spaced repetition.

    Box 1: Review every session (new or failed cards)
    Box 2: Review every 2 sessions
    Box 3: Review every 4 sessions
    Box 4: Review every 8 sessions
    Box 5: Review every 16 sessions (mastered)
    """

    def __init__(self, save_file="vowels_progress.json"):
        self.save_file = save_file
        self.boxes = {1: [], 2: [], 3: [], 4: [], 5: []}
        self.session_count = 0
        self.stats = {
            "total_reviews": 0,
            "correct_answers": 0,
            "wrong_answers": 0,
            "last_session": None
        }
        self.load_progress()

    def get_save_path(self):
        """Get the path for saving progress"""
        # Try to save in user's home directory
        home = Path.home()
        save_dir = home / ".vietnamese_vowels"
        try:
            save_dir.mkdir(exist_ok=True)
            return save_dir / self.save_file
        except:
            # Fallback to current directory
            return Path(self.save_file)

    def load_progress(self):
        """Load progress from file"""
        save_path = self.get_save_path()
        try:
            if save_path.exists():
                with open(save_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.boxes = {int(k): v for k, v in data.get('boxes', {}).items()}
                    self.session_count = data.get('session_count', 0)
                    self.stats = data.get('stats', self.stats)
        except Exception as e:
            print(f"Could not load progress: {e}")

    def save_progress(self):
        """Save progress to file"""
        save_path = self.get_save_path()
        try:
            data = {
                'boxes': self.boxes,
                'session_count': self.session_count,
                'stats': self.stats
            }
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Could not save progress: {e}")

    def initialize_cards(self, vowels):
        """Initialize all vowels in box 1 if not already present"""
        all_cards = set()
        for box in self.boxes.values():
            all_cards.update(box)

        for vowel in vowels:
            if vowel not in all_cards:
                self.boxes[1].append(vowel)

        self.save_progress()

    def get_cards_for_review(self):
        """Get cards due for review based on Leitner intervals"""
        cards_to_review = []

        # Box 1: Every session
        cards_to_review.extend(self.boxes[1])

        # Box 2: Every 2 sessions
        if self.session_count % 2 == 0:
            cards_to_review.extend(self.boxes[2])

        # Box 3: Every 4 sessions
        if self.session_count % 4 == 0:
            cards_to_review.extend(self.boxes[3])

        # Box 4: Every 8 sessions
        if self.session_count % 8 == 0:
            cards_to_review.extend(self.boxes[4])

        # Box 5: Every 16 sessions
        if self.session_count % 16 == 0:
            cards_to_review.extend(self.boxes[5])

        random.shuffle(cards_to_review)
        return cards_to_review

    def card_correct(self, card):
        """Move card to next box (correct answer)"""
        self.stats["total_reviews"] += 1
        self.stats["correct_answers"] += 1

        current_box = self.get_card_box(card)
        if current_box and current_box < 5:
            self.boxes[current_box].remove(card)
            self.boxes[current_box + 1].append(card)

        self.save_progress()

    def card_wrong(self, card):
        """Move card back to box 1 (wrong answer)"""
        self.stats["total_reviews"] += 1
        self.stats["wrong_answers"] += 1

        current_box = self.get_card_box(card)
        if current_box and current_box > 1:
            self.boxes[current_box].remove(card)
            self.boxes[1].append(card)

        self.save_progress()

    def get_card_box(self, card):
        """Find which box a card is in"""
        for box_num, cards in self.boxes.items():
            if card in cards:
                return box_num
        return None

    def start_session(self):
        """Start a new study session"""
        self.session_count += 1
        self.stats["last_session"] = datetime.now().isoformat()
        self.save_progress()

    def get_progress_stats(self):
        """Get progress statistics"""
        total_cards = sum(len(cards) for cards in self.boxes.values())
        mastered = len(self.boxes[5])
        learning = sum(len(self.boxes[i]) for i in range(2, 5))
        new = len(self.boxes[1])

        accuracy = 0
        if self.stats["total_reviews"] > 0:
            accuracy = (self.stats["correct_answers"] / self.stats["total_reviews"]) * 100

        return {
            "total_cards": total_cards,
            "mastered": mastered,
            "learning": learning,
            "new": new,
            "accuracy": accuracy,
            "total_reviews": self.stats["total_reviews"],
            "sessions": self.session_count
        }


class AudioPlayer:
    """Handles text-to-speech for Vietnamese pronunciation"""

    def __init__(self, root=None):
        self.root = root
        self.pygame_initialized = False
        self.error_callback = None
        self.audio_dir = self._find_audio_dir()
        if AUDIO_AVAILABLE:
            try:
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
                self.pygame_initialized = True
            except Exception as e:
                print(f"Pygame init error: {e}")

    def _find_audio_dir(self):
        """Find the audio directory (works for both dev and bundled app)"""
        # Try relative to script location
        script_dir = Path(__file__).parent
        audio_dir = script_dir / "audio"
        if audio_dir.exists():
            return audio_dir

        # Try PyInstaller bundle location
        if hasattr(sys, '_MEIPASS'):
            bundle_dir = Path(sys._MEIPASS) / "audio"
            if bundle_dir.exists():
                return bundle_dir

        # Try current working directory
        cwd_audio = Path.cwd() / "audio"
        if cwd_audio.exists():
            return cwd_audio

        return None

    def _get_local_audio_path(self, text):
        """Get path to local audio file if it exists"""
        if not self.audio_dir:
            return None
        audio_file = self.audio_dir / f"{text}.mp3"
        if audio_file.exists() and audio_file.stat().st_size > 0:
            return audio_file
        return None

    def set_error_callback(self, callback):
        """Set callback function for error reporting"""
        self.error_callback = callback

    def show_error(self, message):
        """Show error to user"""
        if self.error_callback:
            self.error_callback(message)
        else:
            print(f"Audio error: {message}")

    def speak(self, text, on_complete=None):
        """Play audio - uses local file if available, otherwise TTS"""
        if not AUDIO_AVAILABLE:
            self.show_error(f"Audio libraries not installed.\nInstall with: pip install gtts pygame")
            return

        if not self.pygame_initialized:
            try:
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
                self.pygame_initialized = True
            except Exception as e:
                self.show_error(f"Could not initialize audio: {e}")
                return

        # Check for local audio file first
        local_file = self._get_local_audio_path(text)

        def play_audio():
            temp_path = None
            audio_path = None
            try:
                if local_file:
                    # Use local file (no internet needed)
                    audio_path = str(local_file)
                else:
                    # Generate speech from Google TTS (requires internet)
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                        temp_path = fp.name
                    tts = gTTS(text=text, lang='vi', slow=False)
                    tts.save(temp_path)
                    audio_path = temp_path

                # Stop any currently playing audio
                pygame.mixer.music.stop()

                # Play the audio
                pygame.mixer.music.load(audio_path)
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play()

                # Wait for playback to finish
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                if on_complete:
                    on_complete()

            except Exception as e:
                error_msg = str(e)
                if "No address associated" in error_msg or "getaddrinfo" in error_msg or "Failed to connect" in error_msg:
                    self.show_error("No internet connection.\nRun generate_audio.py first to create offline audio files,\nor connect to the internet.")
                else:
                    self.show_error(f"Audio error: {error_msg}")
            finally:
                if temp_path:
                    try:
                        pygame.mixer.music.unload()
                        os.unlink(temp_path)
                    except:
                        pass

        thread = threading.Thread(target=play_audio)
        thread.daemon = True
        thread.start()


class VietnameseVowelsApp:
    """Main application class"""

    def __init__(self, root):
        self.root = root
        self.root.title("Vietnamese Vowels - Leitner Learning System")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)

        # Initialize systems
        self.leitner = LeitnerSystem()
        self.leitner.initialize_cards(list(VOWELS_DATA.keys()))
        self.audio = AudioPlayer(root)
        self.audio.set_error_callback(self.show_audio_error)

        # Current state
        self.current_vowel = None
        self.current_word = None  # The example word being shown
        self.current_word_data = None  # Full data for current word
        self.review_queue = []
        self.in_review_mode = False
        self.show_answer = False

        # Setup UI
        self.setup_styles()
        self.create_widgets()
        self.show_home()

    def show_audio_error(self, message):
        """Display audio error to user"""
        messagebox.showwarning("Audio Error", message)

    def setup_styles(self):
        """Setup ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configure styles
        style.configure('Title.TLabel', font=('Helvetica', 24, 'bold'))
        style.configure('Vowel.TLabel', font=('Helvetica', 72, 'bold'))
        style.configure('Description.TLabel', font=('Helvetica', 14))
        style.configure('Word.TLabel', font=('Helvetica', 18))
        style.configure('Big.TButton', font=('Helvetica', 14), padding=10)
        style.configure('Correct.TButton', font=('Helvetica', 14, 'bold'))
        style.configure('Wrong.TButton', font=('Helvetica', 14, 'bold'))

    def create_widgets(self):
        """Create main widgets"""
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))

        self.title_label = ttk.Label(
            self.header_frame,
            text="🇻🇳 Vietnamese Vowels",
            style='Title.TLabel'
        )
        self.title_label.pack(side=tk.LEFT)

        # Stats display
        self.stats_label = ttk.Label(self.header_frame, text="")
        self.stats_label.pack(side=tk.RIGHT)

        # Content frame (changes based on mode)
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Navigation buttons
        self.nav_frame = ttk.Frame(self.main_frame)
        self.nav_frame.pack(fill=tk.X, pady=(20, 0))

        self.update_stats_display()

    def clear_content(self):
        """Clear the content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def clear_nav(self):
        """Clear navigation frame"""
        for widget in self.nav_frame.winfo_children():
            widget.destroy()

    def update_stats_display(self):
        """Update the stats display in header"""
        stats = self.leitner.get_progress_stats()
        self.stats_label.config(
            text=f"📊 Mastered: {stats['mastered']}/{stats['total_cards']} | "
                 f"Accuracy: {stats['accuracy']:.0f}% | "
                 f"Sessions: {stats['sessions']}"
        )

    def show_home(self):
        """Show home screen"""
        self.clear_content()
        self.clear_nav()
        self.in_review_mode = False

        # Welcome message
        welcome = ttk.Label(
            self.content_frame,
            text="Learn Vietnamese Vowels",
            style='Title.TLabel'
        )
        welcome.pack(pady=20)

        # Description
        desc = ttk.Label(
            self.content_frame,
            text="Master the 12 Vietnamese vowels using the Leitner spaced repetition system.\n"
                 "Each vowel comes with example words and pronunciation.",
            style='Description.TLabel',
            justify=tk.CENTER
        )
        desc.pack(pady=10)

        # Stats card
        stats = self.leitner.get_progress_stats()
        stats_frame = ttk.LabelFrame(self.content_frame, text="Your Progress", padding=20)
        stats_frame.pack(pady=20, padx=50, fill=tk.X)

        stats_grid = ttk.Frame(stats_frame)
        stats_grid.pack()

        labels = [
            ("📦 Box 1 (New)", len(self.leitner.boxes[1])),
            ("📦 Box 2", len(self.leitner.boxes[2])),
            ("📦 Box 3", len(self.leitner.boxes[3])),
            ("📦 Box 4", len(self.leitner.boxes[4])),
            ("⭐ Box 5 (Mastered)", len(self.leitner.boxes[5])),
        ]

        for i, (label, count) in enumerate(labels):
            ttk.Label(stats_grid, text=label).grid(row=i, column=0, sticky=tk.W, padx=10, pady=2)
            ttk.Label(stats_grid, text=str(count)).grid(row=i, column=1, sticky=tk.E, padx=10, pady=2)

        # Action buttons
        btn_frame = ttk.Frame(self.content_frame)
        btn_frame.pack(pady=30)

        cards_due = len(self.leitner.get_cards_for_review())

        review_btn = ttk.Button(
            btn_frame,
            text=f"📚 Start Review ({cards_due} cards due)",
            style='Big.TButton',
            command=self.start_review
        )
        review_btn.pack(pady=5)

        browse_btn = ttk.Button(
            btn_frame,
            text="📖 Browse All Vowels",
            style='Big.TButton',
            command=self.show_browse
        )
        browse_btn.pack(pady=5)

        # Leitner info
        info_frame = ttk.LabelFrame(self.content_frame, text="How the Leitner System Works", padding=15)
        info_frame.pack(pady=20, padx=50, fill=tk.X)

        info_text = (
            "• Correct answer: Card moves to next box (less frequent review)\n"
            "• Wrong answer: Card goes back to Box 1 (more practice needed)\n"
            "• Box 1: Every session | Box 2: Every 2nd | Box 3: Every 4th\n"
            "• Box 4: Every 8th | Box 5: Every 16th (mastered!)"
        )
        ttk.Label(info_frame, text=info_text, justify=tk.LEFT).pack()

        self.update_stats_display()

    def show_browse(self):
        """Show browsing mode - list all vowels"""
        self.clear_content()
        self.clear_nav()
        self.in_review_mode = False

        # Title
        ttk.Label(
            self.content_frame,
            text="Browse Vietnamese Vowels",
            style='Title.TLabel'
        ).pack(pady=10)

        # Scrollable frame for vowels
        canvas = tk.Canvas(self.content_frame)
        scrollbar = ttk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Grid of vowel buttons
        vowels = list(VOWELS_DATA.keys())
        for i, vowel in enumerate(vowels):
            row = i // 4
            col = i % 4

            box = self.leitner.get_card_box(vowel)
            box_indicator = "⭐" if box == 5 else f"📦{box}"

            btn = ttk.Button(
                scrollable_frame,
                text=f"{vowel}\n{box_indicator}",
                style='Big.TButton',
                command=lambda v=vowel: self.show_vowel_detail(v)
            )
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        canvas.pack(side="left", fill="both", expand=True, padx=20)
        scrollbar.pack(side="right", fill="y")

        # Back button
        ttk.Button(
            self.nav_frame,
            text="← Back to Home",
            command=self.show_home
        ).pack(side=tk.LEFT)

    def show_vowel_detail(self, vowel):
        """Show detailed view of a single vowel"""
        self.clear_content()
        self.clear_nav()

        data = VOWELS_DATA[vowel]

        # Vowel display
        vowel_frame = ttk.Frame(self.content_frame)
        vowel_frame.pack(pady=20)

        ttk.Label(vowel_frame, text=vowel, style='Vowel.TLabel').pack()
        ttk.Label(vowel_frame, text=data['ipa'], style='Description.TLabel').pack()

        # Pronunciation button
        sound_btn = ttk.Button(
            vowel_frame,
            text="🔊 Hear Pronunciation",
            style='Big.TButton',
            command=lambda: self.audio.speak(vowel)
        )
        sound_btn.pack(pady=10)

        # Description
        ttk.Label(
            self.content_frame,
            text=data['description'],
            style='Description.TLabel',
            wraplength=600
        ).pack(pady=10)

        # Examples
        examples_frame = ttk.LabelFrame(self.content_frame, text="Example Words", padding=15)
        examples_frame.pack(pady=20, padx=30, fill=tk.X)

        for example in data['examples']:
            ex_frame = ttk.Frame(examples_frame)
            ex_frame.pack(fill=tk.X, pady=5)

            word_btn = ttk.Button(
                ex_frame,
                text=f"🔊 {example['word']}",
                command=lambda w=example['word']: self.audio.speak(w)
            )
            word_btn.pack(side=tk.LEFT)

            ttk.Label(
                ex_frame,
                text=f"  =  {example['meaning']}",
                style='Word.TLabel'
            ).pack(side=tk.LEFT, padx=10)

            # Sentence with sound
            sent_frame = ttk.Frame(examples_frame)
            sent_frame.pack(fill=tk.X, pady=2, padx=20)

            sentence_word = example['sentence'].split('=')[0].strip()
            sent_btn = ttk.Button(
                sent_frame,
                text="🔊",
                width=3,
                command=lambda s=sentence_word: self.audio.speak(s)
            )
            sent_btn.pack(side=tk.LEFT)

            ttk.Label(
                sent_frame,
                text=f"  {example['sentence']}",
                font=('Helvetica', 11, 'italic')
            ).pack(side=tk.LEFT)

        # Current box status
        box = self.leitner.get_card_box(vowel)
        status_text = "⭐ Mastered!" if box == 5 else f"📦 Currently in Box {box}"
        ttk.Label(
            self.content_frame,
            text=status_text,
            style='Description.TLabel'
        ).pack(pady=20)

        # Navigation
        ttk.Button(
            self.nav_frame,
            text="← Back to Browse",
            command=self.show_browse
        ).pack(side=tk.LEFT)

        ttk.Button(
            self.nav_frame,
            text="🏠 Home",
            command=self.show_home
        ).pack(side=tk.RIGHT)

    def start_review(self):
        """Start a review session"""
        self.leitner.start_session()
        self.review_queue = self.leitner.get_cards_for_review()
        self.in_review_mode = True

        if not self.review_queue:
            messagebox.showinfo(
                "No Cards Due",
                "Great job! No cards are due for review right now.\n"
                "Come back later or browse the vowels to study."
            )
            self.show_home()
            return

        self.show_next_card()

    def show_next_card(self):
        """Show the next card in review queue - shows a WORD first, then reveals the vowel"""
        self.clear_content()
        self.clear_nav()

        if not self.review_queue:
            self.end_review()
            return

        self.current_vowel = self.review_queue.pop(0)
        self.show_answer = False

        # Pick a random example word for this vowel
        data = VOWELS_DATA[self.current_vowel]
        self.current_word_data = random.choice(data['examples'])
        self.current_word = self.current_word_data['word']

        # Progress indicator
        remaining = len(self.review_queue)
        ttk.Label(
            self.content_frame,
            text=f"Cards remaining: {remaining + 1}",
            style='Description.TLabel'
        ).pack(pady=5)

        # Card frame
        card_frame = ttk.Frame(self.content_frame, relief="raised", borderwidth=2)
        card_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)

        # Instruction - user should guess pronunciation first
        ttk.Label(
            card_frame,
            text="How do you pronounce this word?",
            style='Description.TLabel'
        ).pack(pady=(20, 10))

        # Word display (question side) - show the word with its meaning
        ttk.Label(
            card_frame,
            text=self.current_word,
            style='Vowel.TLabel'
        ).pack(pady=10)

        ttk.Label(
            card_frame,
            text=f"({self.current_word_data['meaning']})",
            style='Description.TLabel'
        ).pack(pady=5)

        # Hint about the vowel
        ttk.Label(
            card_frame,
            text="Try to say it out loud, then check your pronunciation!",
            style='Description.TLabel',
            font=('Helvetica', 12, 'italic')
        ).pack(pady=15)

        # Show Answer button
        self.answer_frame = ttk.Frame(card_frame)
        self.answer_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        show_btn = ttk.Button(
            self.answer_frame,
            text="Show Answer",
            style='Big.TButton',
            command=self.reveal_answer
        )
        show_btn.pack(pady=20)

        # Navigation
        ttk.Button(
            self.nav_frame,
            text="❌ End Session",
            command=self.end_review
        ).pack(side=tk.LEFT)

    def reveal_answer(self):
        """Reveal the answer - plays the word and shows the vowel"""
        for widget in self.answer_frame.winfo_children():
            widget.destroy()

        data = VOWELS_DATA[self.current_vowel]

        # Play the word pronunciation automatically when answer is revealed
        self.root.after(100, lambda: self.audio.speak(self.current_word))

        # Header showing correct pronunciation
        ttk.Label(
            self.answer_frame,
            text="Correct pronunciation:",
            style='Description.TLabel'
        ).pack(pady=(5, 0))

        # The word with replay button
        word_frame = ttk.Frame(self.answer_frame)
        word_frame.pack(pady=10)

        ttk.Label(
            word_frame,
            text=self.current_word,
            font=('Helvetica', 36, 'bold')
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            word_frame,
            text="🔊 Replay",
            command=lambda: self.audio.speak(self.current_word)
        ).pack(side=tk.LEFT, padx=5)

        # Show which vowel it contains
        ttk.Label(
            self.answer_frame,
            text=f"Contains the vowel: {self.current_vowel}",
            style='Description.TLabel'
        ).pack(pady=5)

        # IPA and description
        ttk.Label(
            self.answer_frame,
            text=f"{data['ipa']} - {data['description']}",
            style='Description.TLabel',
            wraplength=500
        ).pack(pady=5)

        # Button to hear JUST the vowel sound
        vowel_btn = ttk.Button(
            self.answer_frame,
            text=f"🔊 Hear vowel '{self.current_vowel}' by itself",
            style='Big.TButton',
            command=lambda: self.audio.speak(self.current_vowel)
        )
        vowel_btn.pack(pady=10)

        # Did you get it right?
        ttk.Label(
            self.answer_frame,
            text="Did you pronounce it correctly?",
            style='Description.TLabel',
            font=('Helvetica', 12, 'bold')
        ).pack(pady=(10, 5))

        # Correct/Wrong buttons
        btn_frame = ttk.Frame(self.answer_frame)
        btn_frame.pack(pady=10)

        wrong_btn = tk.Button(
            btn_frame,
            text="❌ Wrong",
            font=('Helvetica', 14, 'bold'),
            bg='#ff6b6b',
            fg='white',
            width=12,
            height=2,
            command=self.mark_wrong
        )
        wrong_btn.pack(side=tk.LEFT, padx=10)

        correct_btn = tk.Button(
            btn_frame,
            text="✓ Correct",
            font=('Helvetica', 14, 'bold'),
            bg='#51cf66',
            fg='white',
            width=12,
            height=2,
            command=self.mark_correct
        )
        correct_btn.pack(side=tk.LEFT, padx=10)

    def mark_correct(self):
        """Mark current card as correct"""
        if self.current_vowel:
            self.leitner.card_correct(self.current_vowel)
            self.update_stats_display()
        self.show_next_card()

    def mark_wrong(self):
        """Mark current card as wrong"""
        if self.current_vowel:
            self.leitner.card_wrong(self.current_vowel)
            self.update_stats_display()
        self.show_next_card()

    def end_review(self):
        """End the review session"""
        self.in_review_mode = False
        stats = self.leitner.get_progress_stats()

        messagebox.showinfo(
            "Session Complete",
            f"Great work!\n\n"
            f"Total Reviews: {stats['total_reviews']}\n"
            f"Accuracy: {stats['accuracy']:.1f}%\n"
            f"Cards Mastered: {stats['mastered']}/{stats['total_cards']}"
        )

        self.show_home()


def main():
    """Main entry point"""
    root = tk.Tk()

    # Set icon if available
    try:
        # Create a simple icon
        root.iconname("Vietnamese Vowels")
    except:
        pass

    app = VietnameseVowelsApp(root)

    # Handle close
    def on_closing():
        app.leitner.save_progress()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
