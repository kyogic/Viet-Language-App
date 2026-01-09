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
    # === MONOPHTHONGS (Single Vowels) ===
    "a": {
        "description": "",
        "ipa": "/aː/",
        "category": "monophthong",
        "examples": [
            {"word": "ba", "meaning": "three / father", "sentence": "Ba người = Three people"},
            {"word": "cá", "meaning": "fish", "sentence": "Con cá = The fish"},
            {"word": "nhà", "meaning": "house / home", "sentence": "Nhà tôi = My house"},
            {"word": "là", "meaning": "is / to be", "sentence": "Đây là = This is"},
        ]
    },
    "ă": {
        "description": "",
        "ipa": "/a/",
        "category": "monophthong",
        "examples": [
            {"word": "ăn", "meaning": "to eat", "sentence": "Ăn cơm = Eat rice"},
            {"word": "bắt", "meaning": "to catch", "sentence": "Bắt cá = Catch fish"},
            {"word": "năm", "meaning": "year / five", "sentence": "Năm nay = This year"},
            {"word": "tắm", "meaning": "to bathe", "sentence": "Tắm rửa = To wash"},
        ]
    },
    "â": {
        "description": "",
        "ipa": "/ə/",
        "category": "monophthong",
        "examples": [
            {"word": "ân", "meaning": "grace / favor", "sentence": "Ân huệ = Favor"},
            {"word": "cấp", "meaning": "level / urgent", "sentence": "Cấp bách = Urgent"},
            {"word": "lần", "meaning": "time (occurrence)", "sentence": "Lần đầu = First time"},
            {"word": "sân", "meaning": "yard / court", "sentence": "Sân bay = Airport"},
        ]
    },
    "e": {
        "description": "",
        "ipa": "/ɛ/",
        "category": "monophthong",
        "examples": [
            {"word": "em", "meaning": "younger sibling / I (younger)", "sentence": "Em gái = Younger sister"},
            {"word": "đẹp", "meaning": "beautiful", "sentence": "Rất đẹp = Very beautiful"},
            {"word": "xe", "meaning": "vehicle", "sentence": "Xe máy = Motorbike"},
            {"word": "me", "meaning": "tamarind", "sentence": "Quả me = Tamarind fruit"},
        ]
    },
    "ê": {
        "description": "",
        "ipa": "/e/",
        "category": "monophthong",
        "examples": [
            {"word": "bê", "meaning": "calf (baby cow)", "sentence": "Con bê = The calf"},
            {"word": "đêm", "meaning": "night", "sentence": "Ban đêm = At night"},
            {"word": "lễ", "meaning": "ceremony / holiday", "sentence": "Ngày lễ = Holiday"},
            {"word": "tên", "meaning": "name", "sentence": "Tên tôi = My name"},
        ]
    },
    "i": {
        "description": "",
        "ipa": "/i/",
        "category": "monophthong",
        "examples": [
            {"word": "đi", "meaning": "to go", "sentence": "Đi học = Go to school"},
            {"word": "bí", "meaning": "squash / secret", "sentence": "Bí mật = Secret"},
            {"word": "khi", "meaning": "when", "sentence": "Khi nào = When"},
            {"word": "thi", "meaning": "to take exam", "sentence": "Thi cử = Examination"},
        ]
    },
    "o": {
        "description": "",
        "ipa": "/ɔ/",
        "category": "monophthong",
        "examples": [
            {"word": "con", "meaning": "child / animal classifier", "sentence": "Con chó = The dog"},
            {"word": "có", "meaning": "to have", "sentence": "Tôi có = I have"},
            {"word": "to", "meaning": "big", "sentence": "Rất to = Very big"},
            {"word": "cho", "meaning": "to give / for", "sentence": "Cho tôi = Give me"},
        ]
    },
    "ô": {
        "description": "",
        "ipa": "/o/",
        "category": "monophthong",
        "examples": [
            {"word": "cô", "meaning": "aunt / miss", "sentence": "Cô giáo = Teacher (female)"},
            {"word": "tô", "meaning": "bowl", "sentence": "Tô phở = Bowl of pho"},
            {"word": "đô", "meaning": "dollar / capital", "sentence": "Đô la = Dollar"},
            {"word": "hồ", "meaning": "lake", "sentence": "Hồ nước = Lake"},
        ]
    },
    "ơ": {
        "description": "",
        "ipa": "/əː/",
        "category": "monophthong",
        "examples": [
            {"word": "mơ", "meaning": "to dream / apricot", "sentence": "Giấc mơ = Dream"},
            {"word": "bơ", "meaning": "butter / avocado", "sentence": "Quả bơ = Avocado"},
            {"word": "cờ", "meaning": "flag / chess", "sentence": "Lá cờ = Flag"},
            {"word": "thơ", "meaning": "poetry", "sentence": "Bài thơ = Poem"},
        ]
    },
    "u": {
        "description": "",
        "ipa": "/u/",
        "category": "monophthong",
        "examples": [
            {"word": "mua", "meaning": "to buy", "sentence": "Mua sắm = Shopping"},
            {"word": "thu", "meaning": "autumn / to collect", "sentence": "Mùa thu = Autumn"},
            {"word": "du", "meaning": "to travel", "sentence": "Du lịch = Tourism"},
            {"word": "gấu", "meaning": "bear", "sentence": "Con gấu = The bear"},
        ]
    },
    "ư": {
        "description": "",
        "ipa": "/ɯ/",
        "category": "monophthong",
        "examples": [
            {"word": "từ", "meaning": "word / from", "sentence": "Từ điển = Dictionary"},
            {"word": "sữa", "meaning": "milk", "sentence": "Sữa tươi = Fresh milk"},
            {"word": "mưa", "meaning": "rain", "sentence": "Trời mưa = It's raining"},
            {"word": "thư", "meaning": "letter", "sentence": "Bức thư = A letter"},
        ]
    },
    "y": {
        "description": "",
        "ipa": "/i/",
        "category": "monophthong",
        "examples": [
            {"word": "ý", "meaning": "meaning / idea", "sentence": "Ý kiến = Opinion"},
            {"word": "hy", "meaning": "hope (in compounds)", "sentence": "Hy vọng = Hope"},
            {"word": "lý", "meaning": "reason / plum", "sentence": "Lý do = Reason"},
            {"word": "ty", "meaning": "company (short form)", "sentence": "Công ty = Company"},
        ]
    },
    # === DIPHTHONGS ===
    "ai": {
        "description": "",
        "ipa": "/aːj/",
        "category": "diphthong",
        "examples": [
            {"word": "hai", "meaning": "two", "sentence": "Hai người = Two people"},
            {"word": "mai", "meaning": "tomorrow", "sentence": "Ngày mai = Tomorrow"},
            {"word": "tai", "meaning": "ear", "sentence": "Đôi tai = Pair of ears"},
            {"word": "dài", "meaning": "long", "sentence": "Rất dài = Very long"},
        ]
    },
    "ao": {
        "description": "",
        "ipa": "/aːw/",
        "category": "diphthong",
        "examples": [
            {"word": "sao", "meaning": "star / why", "sentence": "Ngôi sao = Star"},
            {"word": "cao", "meaning": "tall / high", "sentence": "Rất cao = Very tall"},
            {"word": "báo", "meaning": "newspaper / leopard", "sentence": "Tờ báo = Newspaper"},
            {"word": "áo", "meaning": "shirt / clothes", "sentence": "Áo dài = Traditional dress"},
        ]
    },
    "au": {
        "description": "",
        "ipa": "/aw/",
        "category": "diphthong",
        "examples": [
            {"word": "sau", "meaning": "after / behind", "sentence": "Sau đó = After that"},
            {"word": "đau", "meaning": "pain / hurt", "sentence": "Đau đầu = Headache"},
            {"word": "màu", "meaning": "color", "sentence": "Màu đỏ = Red color"},
            {"word": "rau", "meaning": "vegetable", "sentence": "Rau xanh = Green vegetable"},
        ]
    },
    "ay": {
        "description": "",
        "ipa": "/aj/",
        "category": "diphthong",
        "examples": [
            {"word": "hay", "meaning": "or / interesting", "sentence": "Hay là = Or"},
            {"word": "tay", "meaning": "hand / arm", "sentence": "Bàn tay = Hand"},
            {"word": "bay", "meaning": "to fly", "sentence": "Bay đi = Fly away"},
            {"word": "ngay", "meaning": "immediately / straight", "sentence": "Ngay bây giờ = Right now"},
        ]
    },
    "ây": {
        "description": "",
        "ipa": "/əj/",
        "category": "diphthong",
        "examples": [
            {"word": "đây", "meaning": "here", "sentence": "Ở đây = Here"},
            {"word": "mây", "meaning": "cloud", "sentence": "Đám mây = Cloud"},
            {"word": "cây", "meaning": "tree / plant", "sentence": "Cây cối = Trees"},
            {"word": "đầy", "meaning": "full", "sentence": "Đầy đủ = Complete"},
        ]
    },
    "eo": {
        "description": "",
        "ipa": "/ɛw/",
        "category": "diphthong",
        "examples": [
            {"word": "kẹo", "meaning": "candy", "sentence": "Kẹo ngọt = Sweet candy"},
            {"word": "mèo", "meaning": "cat", "sentence": "Con mèo = The cat"},
            {"word": "đèo", "meaning": "mountain pass", "sentence": "Đèo cao = High pass"},
            {"word": "theo", "meaning": "to follow", "sentence": "Theo dõi = To follow"},
        ]
    },
    "êu": {
        "description": "",
        "ipa": "/ew/",
        "category": "diphthong",
        "examples": [
            {"word": "kêu", "meaning": "to call / cry", "sentence": "Kêu gọi = To call"},
            {"word": "nêu", "meaning": "to raise / state", "sentence": "Nêu lên = To raise"},
            {"word": "têu", "meaning": "playful", "sentence": "Nghịch têu = Mischievous"},
            {"word": "trêu", "meaning": "to tease", "sentence": "Trêu chọc = To tease"},
        ]
    },
    "ia": {
        "description": "",
        "ipa": "/iə/",
        "category": "diphthong",
        "examples": [
            {"word": "chia", "meaning": "to divide / share", "sentence": "Chia sẻ = To share"},
            {"word": "kia", "meaning": "that (over there)", "sentence": "Bên kia = Over there"},
            {"word": "mía", "meaning": "sugarcane", "sentence": "Cây mía = Sugarcane"},
            {"word": "tía", "meaning": "purple / dad (Southern)", "sentence": "Màu tía = Purple"},
        ]
    },
    "iu": {
        "description": "",
        "ipa": "/iw/",
        "category": "diphthong",
        "examples": [
            {"word": "dịu", "meaning": "gentle / mild", "sentence": "Dịu dàng = Gentle"},
            {"word": "chịu", "meaning": "to endure", "sentence": "Chịu đựng = To endure"},
            {"word": "kịu", "meaning": "creaking sound", "sentence": "Tiếng kịu = Creaking"},
            {"word": "hiu", "meaning": "desolate", "sentence": "Hiu quạnh = Desolate"},
        ]
    },
    "oi": {
        "description": "",
        "ipa": "/ɔj/",
        "category": "diphthong",
        "examples": [
            {"word": "nói", "meaning": "to speak", "sentence": "Nói chuyện = To talk"},
            {"word": "đói", "meaning": "hungry", "sentence": "Đói bụng = Hungry"},
            {"word": "rồi", "meaning": "already / then", "sentence": "Xong rồi = Done already"},
            {"word": "trời", "meaning": "sky / heaven", "sentence": "Bầu trời = Sky"},
        ]
    },
    "ôi": {
        "description": "",
        "ipa": "/oj/",
        "category": "diphthong",
        "examples": [
            {"word": "tôi", "meaning": "I / me", "sentence": "Tôi là = I am"},
            {"word": "đôi", "meaning": "pair / couple", "sentence": "Đôi giày = Pair of shoes"},
            {"word": "hối", "meaning": "to regret / rush", "sentence": "Hối hận = To regret"},
            {"word": "bồi", "meaning": "waiter / to nourish", "sentence": "Bồi dưỡng = To nourish"},
        ]
    },
    "ơi": {
        "description": "",
        "ipa": "/əːj/",
        "category": "diphthong",
        "examples": [
            {"word": "ơi", "meaning": "hey / oh (vocative)", "sentence": "Anh ơi = Hey brother"},
            {"word": "bơi", "meaning": "to swim", "sentence": "Bơi lội = Swimming"},
            {"word": "mới", "meaning": "new / just", "sentence": "Mới đến = Just arrived"},
            {"word": "gởi", "meaning": "to send", "sentence": "Gởi đi = Send away"},
        ]
    },
    "ua": {
        "description": "",
        "ipa": "/uə/",
        "category": "diphthong",
        "examples": [
            {"word": "mua", "meaning": "to buy", "sentence": "Mua hàng = To shop"},
            {"word": "cua", "meaning": "crab / to turn", "sentence": "Con cua = Crab"},
            {"word": "chùa", "meaning": "pagoda", "sentence": "Ngôi chùa = Pagoda"},
            {"word": "lúa", "meaning": "rice plant", "sentence": "Cánh đồng lúa = Rice field"},
        ]
    },
    "uê": {
        "description": "",
        "ipa": "/ue/",
        "category": "diphthong",
        "examples": [
            {"word": "huê", "meaning": "flower (classical)", "sentence": "Huê Kỳ = USA (old name)"},
            {"word": "quê", "meaning": "hometown / rural", "sentence": "Quê hương = Homeland"},
            {"word": "tuê", "meaning": "year of age (Sino-Vietnamese)", "sentence": "Tuế nguyệt = Time"},
            {"word": "xuê", "meaning": "to boast", "sentence": "Xuê xoa = To show off"},
        ]
    },
    "ui": {
        "description": "",
        "ipa": "/uj/",
        "category": "diphthong",
        "examples": [
            {"word": "núi", "meaning": "mountain", "sentence": "Ngọn núi = Mountain"},
            {"word": "mùi", "meaning": "smell / scent", "sentence": "Mùi thơm = Fragrance"},
            {"word": "túi", "meaning": "bag / pocket", "sentence": "Túi xách = Handbag"},
            {"word": "vui", "meaning": "happy / fun", "sentence": "Vui vẻ = Happy"},
        ]
    },
    "uo": {
        "description": "",
        "ipa": "/uə/",
        "category": "diphthong",
        "examples": [
            {"word": "cuộc", "meaning": "event / match", "sentence": "Cuộc sống = Life"},
            {"word": "muốn", "meaning": "to want", "sentence": "Tôi muốn = I want"},
            {"word": "buồn", "meaning": "sad", "sentence": "Buồn bã = Sad"},
            {"word": "chuối", "meaning": "banana", "sentence": "Quả chuối = Banana"},
        ]
    },
    "ưa": {
        "description": "",
        "ipa": "/ɯə/",
        "category": "diphthong",
        "examples": [
            {"word": "mưa", "meaning": "rain", "sentence": "Trời mưa = It's raining"},
            {"word": "chưa", "meaning": "not yet", "sentence": "Chưa xong = Not done yet"},
            {"word": "thưa", "meaning": "dear / sparse", "sentence": "Thưa ông = Dear sir"},
            {"word": "xưa", "meaning": "ancient / old", "sentence": "Ngày xưa = Once upon a time"},
        ]
    },
    "ưi": {
        "description": "",
        "ipa": "/ɯj/",
        "category": "diphthong",
        "examples": [
            {"word": "gửi", "meaning": "to send", "sentence": "Gửi thư = Send letter"},
            {"word": "tưởi", "meaning": "to water", "sentence": "Tưới cây = Water plants"},
            {"word": "cười", "meaning": "to laugh / smile", "sentence": "Cười vui = Laugh happily"},
            {"word": "mười", "meaning": "ten", "sentence": "Mười người = Ten people"},
        ]
    },
    "ưu": {
        "description": "",
        "ipa": "/ɯw/",
        "category": "diphthong",
        "examples": [
            {"word": "lưu", "meaning": "to save / keep", "sentence": "Lưu trữ = To store"},
            {"word": "cứu", "meaning": "to save / rescue", "sentence": "Cứu giúp = To help"},
            {"word": "mưu", "meaning": "scheme / plan", "sentence": "Mưu kế = Strategy"},
            {"word": "hưu", "meaning": "retired", "sentence": "Nghỉ hưu = Retire"},
        ]
    },
    # === TRIPHTHONGS ===
    "iêu": {
        "description": "",
        "ipa": "/iəw/",
        "category": "triphthong",
        "examples": [
            {"word": "nhiều", "meaning": "many / much", "sentence": "Rất nhiều = Very many"},
            {"word": "chiều", "meaning": "afternoon / direction", "sentence": "Buổi chiều = Afternoon"},
            {"word": "điều", "meaning": "thing / matter", "sentence": "Điều này = This thing"},
            {"word": "liều", "meaning": "to risk / dose", "sentence": "Liều lĩnh = Reckless"},
        ]
    },
    "yêu": {
        "description": "",
        "ipa": "/iəw/",
        "category": "triphthong",
        "examples": [
            {"word": "yêu", "meaning": "to love", "sentence": "Yêu thương = To love"},
            {"word": "yếu", "meaning": "weak", "sentence": "Yếu đuối = Weak"},
            {"word": "yểu", "meaning": "short-lived", "sentence": "Yểu mệnh = Short-lived"},
            {"word": "diêu", "meaning": "kite", "sentence": "Thả diều = Fly a kite"},
        ]
    },
    "oai": {
        "description": "",
        "ipa": "/waːj/",
        "category": "triphthong",
        "examples": [
            {"word": "hoài", "meaning": "always / in vain", "sentence": "Hoài niệm = Nostalgia"},
            {"word": "ngoài", "meaning": "outside", "sentence": "Bên ngoài = Outside"},
            {"word": "khoai", "meaning": "potato / tuber", "sentence": "Khoai tây = Potato"},
            {"word": "toại", "meaning": "satisfied", "sentence": "Mãn toại = Satisfied"},
        ]
    },
    "oay": {
        "description": "",
        "ipa": "/waj/",
        "category": "triphthong",
        "examples": [
            {"word": "xoay", "meaning": "to rotate / turn", "sentence": "Xoay vòng = Rotate"},
            {"word": "ngoáy", "meaning": "to stir / poke", "sentence": "Ngoáy tai = Clean ear"},
            {"word": "loay", "meaning": "to struggle", "sentence": "Loay hoay = To struggle"},
            {"word": "khoáy", "meaning": "whorl / to dig", "sentence": "Khoáy tóc = Hair whorl"},
        ]
    },
    "oao": {
        "description": "",
        "ipa": "/waːw/",
        "category": "triphthong",
        "examples": [
            {"word": "ngoao", "meaning": "meow", "sentence": "Mèo ngoao = Cat meows"},
            {"word": "khoáo", "meaning": "smooth talking", "sentence": "Nói khoáo = Smooth talk"},
            {"word": "soạo", "meaning": "sizzling sound", "sentence": "Tiếng soạo = Sizzle"},
            {"word": "hoào", "meaning": "rushing sound", "sentence": "Gió hoào = Wind rush"},
        ]
    },
    "oeo": {
        "description": "",
        "ipa": "/wɛw/",
        "category": "triphthong",
        "examples": [
            {"word": "ngoẹo", "meaning": "to tilt / slant", "sentence": "Ngoẹo đầu = Tilt head"},
            {"word": "khoèo", "meaning": "bowlegged", "sentence": "Chân khoèo = Bowlegged"},
            {"word": "ngoéo", "meaning": "to hook", "sentence": "Ngoéo tay = Hook finger"},
            {"word": "choèo", "meaning": "folk opera", "sentence": "Hát chèo = Cheo singing"},
        ]
    },
    "uây": {
        "description": "",
        "ipa": "/wəj/",
        "category": "triphthong",
        "examples": [
            {"word": "khuây", "meaning": "to distract / forget", "sentence": "Khuây khỏa = To distract"},
            {"word": "quây", "meaning": "to surround", "sentence": "Quây quần = Gather around"},
            {"word": "chuẩy", "meaning": "standard (variant)", "sentence": "Tiêu chuẩy = Standard"},
            {"word": "xuây", "meaning": "to build (variant)", "sentence": "Xây xuây = Build"},
        ]
    },
    "uôi": {
        "description": "",
        "ipa": "/uəj/",
        "category": "triphthong",
        "examples": [
            {"word": "đuôi", "meaning": "tail", "sentence": "Cái đuôi = The tail"},
            {"word": "chuối", "meaning": "banana", "sentence": "Quả chuối = Banana"},
            {"word": "muối", "meaning": "salt", "sentence": "Muối mặn = Salty"},
            {"word": "tuổi", "meaning": "age", "sentence": "Bao nhiêu tuổi = How old"},
        ]
    },
    "ươi": {
        "description": "",
        "ipa": "/ɯəj/",
        "category": "triphthong",
        "examples": [
            {"word": "tươi", "meaning": "fresh", "sentence": "Rau tươi = Fresh vegetables"},
            {"word": "cười", "meaning": "to laugh", "sentence": "Cười vui = Laugh happily"},
            {"word": "mười", "meaning": "ten", "sentence": "Mười lăm = Fifteen"},
            {"word": "người", "meaning": "person / people", "sentence": "Người Việt = Vietnamese person"},
        ]
    },
    "ươu": {
        "description": "",
        "ipa": "/ɯəw/",
        "category": "triphthong",
        "examples": [
            {"word": "rượu", "meaning": "alcohol / wine", "sentence": "Uống rượu = Drink alcohol"},
            {"word": "hươu", "meaning": "deer", "sentence": "Con hươu = Deer"},
            {"word": "bưởu", "meaning": "tumor / goiter", "sentence": "Bưởu cổ = Goiter"},
            {"word": "cướu", "meaning": "to study", "sentence": "Nghiên cướu = Research"},
        ]
    },
    "uya": {
        "description": "",
        "ipa": "/wiə/",
        "category": "triphthong",
        "examples": [
            {"word": "khuya", "meaning": "late night", "sentence": "Đêm khuya = Late at night"},
            {"word": "tuya", "meaning": "tube / nozzle", "sentence": "Ống tuya = Tube"},
            {"word": "chuya", "meaning": "shuttle", "sentence": "Con chuya = Shuttle"},
            {"word": "xuya", "meaning": "to penetrate", "sentence": "Xuyên xuya = Penetrate"},
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

    def reset_progress(self):
        """Reset all progress - move all cards back to box 1 and clear stats"""
        # Collect all cards from all boxes
        all_cards = []
        for box in self.boxes.values():
            all_cards.extend(box)

        # Reset boxes
        self.boxes = {1: all_cards, 2: [], 3: [], 4: [], 5: []}
        self.session_count = 0
        self.stats = {
            "total_reviews": 0,
            "correct_answers": 0,
            "wrong_answers": 0,
            "last_session": None
        }
        self.save_progress()

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

    # Steam-inspired dark theme colors
    COLORS = {
        'bg_dark': '#1b2838',        # Main background
        'bg_medium': '#2a475e',      # Secondary background
        'bg_light': '#3d5a73',       # Lighter elements
        'bg_card': '#1e3a4c',        # Card background
        'text_primary': '#c7d5e0',   # Main text
        'text_secondary': '#8b929a', # Secondary text
        'text_bright': '#ffffff',    # Bright text
        'accent_blue': '#1a9fff',    # Primary accent
        'accent_hover': '#67c1f5',   # Hover state
        'success': '#5c7e10',        # Green/success
        'success_hover': '#7cb318',  # Green hover
        'error': '#c23b22',          # Red/error
        'error_hover': '#e74c3c',    # Red hover
        'border': '#3d5a73',         # Border color
        'gold': '#ffc82c',           # Gold for mastered
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Vietnamese Vowels - Leitner Learning System")
        self.root.geometry("950x750")
        self.root.minsize(600, 500)
        self.root.configure(bg=self.COLORS['bg_dark'])

        # Make window responsive
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Initialize systems
        self.leitner = LeitnerSystem()
        self.leitner.initialize_cards(list(VOWELS_DATA.keys()))
        self.audio = AudioPlayer(root)
        self.audio.set_error_callback(self.show_audio_error)

        # Current state
        self.current_vowel = None
        self.current_word = None
        self.current_word_data = None
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
        """Setup Steam-like dark theme styles"""
        style = ttk.Style()
        style.theme_use('clam')

        c = self.COLORS

        # General frame styling
        style.configure('TFrame', background=c['bg_dark'])
        style.configure('Card.TFrame', background=c['bg_card'])

        # Label styles
        style.configure('TLabel',
            background=c['bg_dark'],
            foreground=c['text_primary'],
            font=('Segoe UI', 11))

        style.configure('Title.TLabel',
            background=c['bg_dark'],
            foreground=c['text_bright'],
            font=('Segoe UI', 28, 'bold'))

        style.configure('Subtitle.TLabel',
            background=c['bg_dark'],
            foreground=c['accent_blue'],
            font=('Segoe UI', 16, 'bold'))

        style.configure('Vowel.TLabel',
            background=c['bg_card'],
            foreground=c['accent_hover'],
            font=('Segoe UI', 72, 'bold'))

        style.configure('Word.TLabel',
            background=c['bg_card'],
            foreground=c['text_bright'],
            font=('Segoe UI', 42, 'bold'))

        style.configure('Description.TLabel',
            background=c['bg_dark'],
            foreground=c['text_secondary'],
            font=('Segoe UI', 12))

        style.configure('CardDesc.TLabel',
            background=c['bg_card'],
            foreground=c['text_secondary'],
            font=('Segoe UI', 12))

        style.configure('Stats.TLabel',
            background=c['bg_dark'],
            foreground=c['accent_hover'],
            font=('Segoe UI', 11))

        style.configure('Gold.TLabel',
            background=c['bg_dark'],
            foreground=c['gold'],
            font=('Segoe UI', 12, 'bold'))

        # Button styles - Steam blue
        style.configure('TButton',
            background=c['accent_blue'],
            foreground=c['text_bright'],
            font=('Segoe UI', 11, 'bold'),
            padding=(20, 10),
            borderwidth=0)
        style.map('TButton',
            background=[('active', c['accent_hover']), ('pressed', c['bg_light'])],
            foreground=[('active', c['text_bright'])])

        style.configure('Big.TButton',
            background=c['accent_blue'],
            foreground=c['text_bright'],
            font=('Segoe UI', 13, 'bold'),
            padding=(30, 15))
        style.map('Big.TButton',
            background=[('active', c['accent_hover']), ('pressed', c['bg_light'])])

        style.configure('Success.TButton',
            background=c['success'],
            foreground=c['text_bright'],
            font=('Segoe UI', 12, 'bold'),
            padding=(25, 12))
        style.map('Success.TButton',
            background=[('active', c['success_hover'])])

        style.configure('Danger.TButton',
            background=c['error'],
            foreground=c['text_bright'],
            font=('Segoe UI', 12, 'bold'),
            padding=(25, 12))
        style.map('Danger.TButton',
            background=[('active', c['error_hover'])])

        style.configure('Small.TButton',
            background=c['bg_medium'],
            foreground=c['text_primary'],
            font=('Segoe UI', 10),
            padding=(10, 5))
        style.map('Small.TButton',
            background=[('active', c['bg_light'])])

        # LabelFrame
        style.configure('TLabelframe',
            background=c['bg_card'],
            foreground=c['text_primary'],
            bordercolor=c['border'],
            borderwidth=2,
            relief='flat')
        style.configure('TLabelframe.Label',
            background=c['bg_card'],
            foreground=c['accent_hover'],
            font=('Segoe UI', 12, 'bold'))

        # Scrollbar
        style.configure('TScrollbar',
            background=c['bg_medium'],
            troughcolor=c['bg_dark'],
            borderwidth=0,
            arrowcolor=c['text_primary'])

    def create_widgets(self):
        """Create main widgets with Steam-like dark theme"""
        c = self.COLORS

        # Main container
        self.main_frame = tk.Frame(self.root, bg=c['bg_dark'], padx=30, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Header with gradient-like effect
        self.header_frame = tk.Frame(self.main_frame, bg=c['bg_dark'])
        self.header_frame.pack(fill=tk.X, pady=(0, 25))

        # Title with Vietnamese flag colors hint
        title_frame = tk.Frame(self.header_frame, bg=c['bg_dark'])
        title_frame.pack(side=tk.LEFT)

        self.title_label = tk.Label(
            title_frame,
            text="VIETNAMESE VOWELS",
            font=('Segoe UI', 24, 'bold'),
            fg=c['text_bright'],
            bg=c['bg_dark']
        )
        self.title_label.pack(side=tk.LEFT)

        # Accent bar under title
        accent_bar = tk.Frame(title_frame, bg=c['accent_blue'], height=3)
        accent_bar.pack(fill=tk.X, pady=(5, 0))

        # Stats display
        self.stats_label = tk.Label(
            self.header_frame,
            text="",
            font=('Segoe UI', 11),
            fg=c['text_secondary'],
            bg=c['bg_dark']
        )
        self.stats_label.pack(side=tk.RIGHT, pady=10)

        # Content frame
        self.content_frame = tk.Frame(self.main_frame, bg=c['bg_dark'])
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Navigation frame
        self.nav_frame = tk.Frame(self.main_frame, bg=c['bg_dark'])
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
        c = self.COLORS
        stats = self.leitner.get_progress_stats()
        self.stats_label.config(
            text=f"Mastered: {stats['mastered']}/{stats['total_cards']}  |  "
                 f"Accuracy: {stats['accuracy']:.0f}%  |  "
                 f"Sessions: {stats['sessions']}",
            fg=c['text_secondary']
        )

    def show_home(self):
        """Show home screen with Steam-like dark theme"""
        self.clear_content()
        self.clear_nav()
        self.in_review_mode = False
        c = self.COLORS

        # Main content container with some padding
        container = tk.Frame(self.content_frame, bg=c['bg_dark'])
        container.pack(fill=tk.BOTH, expand=True, padx=20)

        # Welcome section
        welcome = tk.Label(
            container,
            text="Learn Vietnamese Vowels",
            font=('Segoe UI', 32, 'bold'),
            fg=c['text_bright'],
            bg=c['bg_dark']
        )
        welcome.pack(pady=(20, 10))

        desc = tk.Label(
            container,
            text="Master the 12 Vietnamese vowels using spaced repetition.\nEach vowel comes with example words and native pronunciation.",
            font=('Segoe UI', 12),
            fg=c['text_secondary'],
            bg=c['bg_dark'],
            justify=tk.CENTER
        )
        desc.pack(pady=(0, 30))

        # Stats card with dark theme
        stats_card = tk.Frame(container, bg=c['bg_card'], padx=30, pady=20)
        stats_card.pack(fill=tk.X, pady=10)

        # Stats header
        stats_header = tk.Label(
            stats_card,
            text="YOUR PROGRESS",
            font=('Segoe UI', 14, 'bold'),
            fg=c['accent_hover'],
            bg=c['bg_card']
        )
        stats_header.pack(anchor=tk.W, pady=(0, 15))

        # Progress boxes in a row
        boxes_frame = tk.Frame(stats_card, bg=c['bg_card'])
        boxes_frame.pack(fill=tk.X)

        box_data = [
            ("BOX 1", "New", len(self.leitner.boxes[1]), c['text_primary']),
            ("BOX 2", "", len(self.leitner.boxes[2]), c['text_primary']),
            ("BOX 3", "", len(self.leitner.boxes[3]), c['text_primary']),
            ("BOX 4", "", len(self.leitner.boxes[4]), c['text_primary']),
            ("BOX 5", "Mastered", len(self.leitner.boxes[5]), c['gold']),
        ]

        for i, (box_name, subtitle, count, color) in enumerate(box_data):
            box_frame = tk.Frame(boxes_frame, bg=c['bg_medium'], padx=15, pady=10)
            box_frame.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

            tk.Label(
                box_frame,
                text=box_name,
                font=('Segoe UI', 10, 'bold'),
                fg=c['text_secondary'],
                bg=c['bg_medium']
            ).pack()

            tk.Label(
                box_frame,
                text=str(count),
                font=('Segoe UI', 24, 'bold'),
                fg=color,
                bg=c['bg_medium']
            ).pack()

            if subtitle:
                tk.Label(
                    box_frame,
                    text=subtitle,
                    font=('Segoe UI', 9),
                    fg=c['text_secondary'],
                    bg=c['bg_medium']
                ).pack()

        # Action buttons with Steam style
        btn_frame = tk.Frame(container, bg=c['bg_dark'])
        btn_frame.pack(pady=30)

        cards_due = len(self.leitner.get_cards_for_review())

        # Start Review button - prominent green
        review_btn = tk.Button(
            btn_frame,
            text=f"START REVIEW  ({cards_due} cards due)",
            font=('Segoe UI', 14, 'bold'),
            fg=c['text_bright'],
            bg=c['success'],
            activebackground=c['success_hover'],
            activeforeground=c['text_bright'],
            bd=0,
            padx=40,
            pady=15,
            cursor='hand2',
            command=self.start_review
        )
        review_btn.pack(pady=8)

        # Browse button - blue accent
        browse_btn = tk.Button(
            btn_frame,
            text="BROWSE ALL VOWELS",
            font=('Segoe UI', 12, 'bold'),
            fg=c['text_bright'],
            bg=c['accent_blue'],
            activebackground=c['accent_hover'],
            activeforeground=c['text_bright'],
            bd=0,
            padx=35,
            pady=12,
            cursor='hand2',
            command=self.show_browse
        )
        browse_btn.pack(pady=8)

        # Reset progress button
        reset_btn = tk.Button(
            btn_frame,
            text="RESET PROGRESS",
            font=('Segoe UI', 10, 'bold'),
            fg=c['text_secondary'],
            bg=c['bg_medium'],
            activebackground=c['error'],
            activeforeground=c['text_bright'],
            bd=0,
            padx=25,
            pady=8,
            cursor='hand2',
            command=self.confirm_reset_progress
        )
        reset_btn.pack(pady=8)

        # Leitner info card
        info_card = tk.Frame(container, bg=c['bg_card'], padx=25, pady=15)
        info_card.pack(fill=tk.X, pady=20)

        tk.Label(
            info_card,
            text="HOW THE LEITNER SYSTEM WORKS",
            font=('Segoe UI', 11, 'bold'),
            fg=c['accent_hover'],
            bg=c['bg_card']
        ).pack(anchor=tk.W, pady=(0, 10))

        info_text = (
            "✓  Correct answer → Card moves to next box (less frequent review)\n"
            "✗  Wrong answer → Card goes back to Box 1 (more practice needed)\n\n"
            "Box 1: Every session  |  Box 2: Every 2nd  |  Box 3: Every 4th\n"
            "Box 4: Every 8th  |  Box 5: Every 16th (mastered!)"
        )
        tk.Label(
            info_card,
            text=info_text,
            font=('Segoe UI', 11),
            fg=c['text_secondary'],
            bg=c['bg_card'],
            justify=tk.LEFT
        ).pack(anchor=tk.W)

        self.update_stats_display()

    def show_browse(self):
        """Show browsing mode - list all vowels with dark theme"""
        self.clear_content()
        self.clear_nav()
        self.in_review_mode = False
        c = self.COLORS

        # Title
        tk.Label(
            self.content_frame,
            text="Browse Vietnamese Vowels",
            font=('Segoe UI', 24, 'bold'),
            fg=c['text_bright'],
            bg=c['bg_dark']
        ).pack(pady=15)

        # Vowels grid container
        grid_frame = tk.Frame(self.content_frame, bg=c['bg_dark'])
        grid_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=10)

        # Grid of vowel cards
        vowels = list(VOWELS_DATA.keys())
        for i, vowel in enumerate(vowels):
            row = i // 4
            col = i % 4

            box = self.leitner.get_card_box(vowel)
            is_mastered = box == 5

            # Card frame
            card = tk.Frame(
                grid_frame,
                bg=c['bg_card'] if not is_mastered else c['bg_medium'],
                padx=10,
                pady=10
            )
            card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

            # Vowel button
            btn_color = c['gold'] if is_mastered else c['accent_blue']
            btn = tk.Button(
                card,
                text=vowel,
                font=('Segoe UI', 32, 'bold'),
                fg=c['text_bright'],
                bg=btn_color,
                activebackground=c['accent_hover'],
                activeforeground=c['text_bright'],
                bd=0,
                width=3,
                height=1,
                cursor='hand2',
                command=lambda v=vowel: self.show_vowel_detail(v)
            )
            btn.pack(pady=5)

            # Box indicator
            box_text = "★ MASTERED" if is_mastered else f"Box {box}"
            tk.Label(
                card,
                text=box_text,
                font=('Segoe UI', 9),
                fg=c['gold'] if is_mastered else c['text_secondary'],
                bg=c['bg_card'] if not is_mastered else c['bg_medium']
            ).pack()

        # Configure grid weights
        for col in range(4):
            grid_frame.columnconfigure(col, weight=1)

        # Navigation buttons
        back_btn = tk.Button(
            self.nav_frame,
            text="← BACK",
            font=('Segoe UI', 11, 'bold'),
            fg=c['text_primary'],
            bg=c['bg_medium'],
            activebackground=c['bg_light'],
            activeforeground=c['text_bright'],
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.show_home
        )
        back_btn.pack(side=tk.LEFT)

        home_btn = tk.Button(
            self.nav_frame,
            text="HOME",
            font=('Segoe UI', 11, 'bold'),
            fg=c['text_primary'],
            bg=c['bg_medium'],
            activebackground=c['bg_light'],
            activeforeground=c['text_bright'],
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.show_home
        )
        home_btn.pack(side=tk.RIGHT)

    def show_vowel_detail(self, vowel):
        """Show detailed view of a single vowel with dark theme"""
        self.clear_content()
        self.clear_nav()
        c = self.COLORS

        data = VOWELS_DATA[vowel]
        box = self.leitner.get_card_box(vowel)
        is_mastered = box == 5

        # Main card
        card = tk.Frame(self.content_frame, bg=c['bg_card'], padx=40, pady=30)
        card.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        # Vowel display
        tk.Label(
            card,
            text=vowel,
            font=('Segoe UI', 80, 'bold'),
            fg=c['gold'] if is_mastered else c['accent_hover'],
            bg=c['bg_card']
        ).pack(pady=(0, 5))

        tk.Label(
            card,
            text=data['ipa'],
            font=('Segoe UI', 16),
            fg=c['text_secondary'],
            bg=c['bg_card']
        ).pack()

        # Pronunciation button
        sound_btn = tk.Button(
            card,
            text="🔊  HEAR PRONUNCIATION",
            font=('Segoe UI', 12, 'bold'),
            fg=c['text_bright'],
            bg=c['accent_blue'],
            activebackground=c['accent_hover'],
            bd=0,
            padx=25,
            pady=10,
            cursor='hand2',
            command=lambda: self.audio.speak(vowel)
        )
        sound_btn.pack(pady=15)

        # Description
        tk.Label(
            card,
            text=data['description'],
            font=('Segoe UI', 14),
            fg=c['text_primary'],
            bg=c['bg_card'],
            wraplength=500
        ).pack(pady=10)

        # Status badge
        status_text = "★ MASTERED" if is_mastered else f"Box {box}"
        status_color = c['gold'] if is_mastered else c['accent_blue']
        tk.Label(
            card,
            text=status_text,
            font=('Segoe UI', 11, 'bold'),
            fg=status_color,
            bg=c['bg_medium'],
            padx=15,
            pady=5
        ).pack(pady=10)

        # Examples section
        examples_card = tk.Frame(card, bg=c['bg_medium'], padx=20, pady=15)
        examples_card.pack(fill=tk.X, pady=15)

        tk.Label(
            examples_card,
            text="EXAMPLE WORDS",
            font=('Segoe UI', 11, 'bold'),
            fg=c['accent_hover'],
            bg=c['bg_medium']
        ).pack(anchor=tk.W, pady=(0, 10))

        for example in data['examples']:
            ex_frame = tk.Frame(examples_card, bg=c['bg_medium'])
            ex_frame.pack(fill=tk.X, pady=4)

            word_btn = tk.Button(
                ex_frame,
                text=f"🔊 {example['word']}",
                font=('Segoe UI', 12, 'bold'),
                fg=c['text_bright'],
                bg=c['bg_light'],
                activebackground=c['accent_blue'],
                bd=0,
                padx=15,
                pady=5,
                cursor='hand2',
                command=lambda w=example['word']: self.audio.speak(w)
            )
            word_btn.pack(side=tk.LEFT)

            tk.Label(
                ex_frame,
                text=f"  =  {example['meaning']}",
                font=('Segoe UI', 12),
                fg=c['text_primary'],
                bg=c['bg_medium']
            ).pack(side=tk.LEFT, padx=10)

        # Navigation
        back_btn = tk.Button(
            self.nav_frame,
            text="← BACK TO BROWSE",
            font=('Segoe UI', 11, 'bold'),
            fg=c['text_primary'],
            bg=c['bg_medium'],
            activebackground=c['bg_light'],
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.show_browse
        )
        back_btn.pack(side=tk.LEFT)

        home_btn = tk.Button(
            self.nav_frame,
            text="HOME",
            font=('Segoe UI', 11, 'bold'),
            fg=c['text_primary'],
            bg=c['bg_medium'],
            activebackground=c['bg_light'],
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.show_home
        )
        home_btn.pack(side=tk.RIGHT)

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
        """Show the next card in review queue with dark theme"""
        self.clear_content()
        self.clear_nav()
        c = self.COLORS

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
        progress_frame = tk.Frame(self.content_frame, bg=c['bg_dark'])
        progress_frame.pack(fill=tk.X, pady=10)

        tk.Label(
            progress_frame,
            text=f"Cards remaining: {remaining + 1}",
            font=('Segoe UI', 11),
            fg=c['text_secondary'],
            bg=c['bg_dark']
        ).pack(side=tk.LEFT)

        # Progress bar visual
        progress_bar_bg = tk.Frame(progress_frame, bg=c['bg_medium'], height=6)
        progress_bar_bg.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(20, 0))
        total_cards = remaining + 1 + (12 - len(self.leitner.get_cards_for_review()) - remaining - 1)
        if total_cards > 0:
            progress_pct = (12 - remaining - 1) / 12
            progress_bar = tk.Frame(progress_bar_bg, bg=c['accent_blue'], height=6, width=int(400 * progress_pct))
            progress_bar.place(x=0, y=0)

        # Main card
        self.card_frame = tk.Frame(self.content_frame, bg=c['bg_card'], padx=50, pady=40)
        self.card_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=15)

        # Instruction
        tk.Label(
            self.card_frame,
            text="How do you pronounce this word?",
            font=('Segoe UI', 14),
            fg=c['text_secondary'],
            bg=c['bg_card']
        ).pack(pady=(0, 20))

        # Word display
        tk.Label(
            self.card_frame,
            text=self.current_word,
            font=('Segoe UI', 64, 'bold'),
            fg=c['text_bright'],
            bg=c['bg_card']
        ).pack(pady=10)

        tk.Label(
            self.card_frame,
            text=f"({self.current_word_data['meaning']})",
            font=('Segoe UI', 14),
            fg=c['text_secondary'],
            bg=c['bg_card']
        ).pack(pady=5)

        # Hint
        tk.Label(
            self.card_frame,
            text="Try to say it out loud, then check your pronunciation!",
            font=('Segoe UI', 12, 'italic'),
            fg=c['accent_hover'],
            bg=c['bg_card']
        ).pack(pady=20)

        # Answer frame (will be populated when answer is revealed)
        self.answer_frame = tk.Frame(self.card_frame, bg=c['bg_card'])
        self.answer_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Show Answer button
        show_btn = tk.Button(
            self.answer_frame,
            text="SHOW ANSWER",
            font=('Segoe UI', 14, 'bold'),
            fg=c['text_bright'],
            bg=c['accent_blue'],
            activebackground=c['accent_hover'],
            bd=0,
            padx=40,
            pady=15,
            cursor='hand2',
            command=self.reveal_answer
        )
        show_btn.pack(pady=20)

        # Navigation buttons
        end_btn = tk.Button(
            self.nav_frame,
            text="END SESSION",
            font=('Segoe UI', 11, 'bold'),
            fg=c['text_primary'],
            bg=c['error'],
            activebackground=c['error_hover'],
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.end_review
        )
        end_btn.pack(side=tk.LEFT)

        home_btn = tk.Button(
            self.nav_frame,
            text="HOME",
            font=('Segoe UI', 11, 'bold'),
            fg=c['text_primary'],
            bg=c['bg_medium'],
            activebackground=c['bg_light'],
            activeforeground=c['text_bright'],
            bd=0,
            padx=20,
            pady=8,
            cursor='hand2',
            command=self.show_home
        )
        home_btn.pack(side=tk.RIGHT)

    def reveal_answer(self):
        """Reveal the answer with dark theme styling"""
        for widget in self.answer_frame.winfo_children():
            widget.destroy()

        c = self.COLORS
        data = VOWELS_DATA[self.current_vowel]

        # Play the word pronunciation automatically
        self.root.after(100, lambda: self.audio.speak(self.current_word))

        # Divider line
        tk.Frame(self.answer_frame, bg=c['border'], height=2).pack(fill=tk.X, pady=10)

        # Correct pronunciation header
        tk.Label(
            self.answer_frame,
            text="CORRECT PRONUNCIATION",
            font=('Segoe UI', 11, 'bold'),
            fg=c['accent_hover'],
            bg=c['bg_card']
        ).pack(pady=(5, 10))

        # Word with replay button
        word_frame = tk.Frame(self.answer_frame, bg=c['bg_card'])
        word_frame.pack(pady=5)

        tk.Label(
            word_frame,
            text=self.current_word,
            font=('Segoe UI', 32, 'bold'),
            fg=c['text_bright'],
            bg=c['bg_card']
        ).pack(side=tk.LEFT, padx=10)

        replay_btn = tk.Button(
            word_frame,
            text="🔊 REPLAY",
            font=('Segoe UI', 10, 'bold'),
            fg=c['text_bright'],
            bg=c['bg_medium'],
            activebackground=c['accent_blue'],
            bd=0,
            padx=15,
            pady=5,
            cursor='hand2',
            command=lambda: self.audio.speak(self.current_word)
        )
        replay_btn.pack(side=tk.LEFT, padx=10)

        # Vowel info
        vowel_info = tk.Frame(self.answer_frame, bg=c['bg_medium'], padx=20, pady=10)
        vowel_info.pack(fill=tk.X, pady=10, padx=20)

        tk.Label(
            vowel_info,
            text=f"Contains vowel:  {self.current_vowel}",
            font=('Segoe UI', 14, 'bold'),
            fg=c['gold'],
            bg=c['bg_medium']
        ).pack(side=tk.LEFT)

        tk.Label(
            vowel_info,
            text=f"  {data['ipa']}  -  {data['description']}",
            font=('Segoe UI', 11),
            fg=c['text_secondary'],
            bg=c['bg_medium']
        ).pack(side=tk.LEFT, padx=10)

        # Button to hear just the vowel
        vowel_btn = tk.Button(
            self.answer_frame,
            text=f"🔊  HEAR VOWEL '{self.current_vowel}' BY ITSELF",
            font=('Segoe UI', 11, 'bold'),
            fg=c['text_bright'],
            bg=c['bg_light'],
            activebackground=c['accent_blue'],
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2',
            command=lambda: self.audio.speak(self.current_vowel)
        )
        vowel_btn.pack(pady=15)

        # Question
        tk.Label(
            self.answer_frame,
            text="Did you pronounce it correctly?",
            font=('Segoe UI', 13, 'bold'),
            fg=c['text_primary'],
            bg=c['bg_card']
        ).pack(pady=(10, 15))

        # Correct/Wrong/Repeat buttons
        btn_frame = tk.Frame(self.answer_frame, bg=c['bg_card'])
        btn_frame.pack(pady=10)

        wrong_btn = tk.Button(
            btn_frame,
            text="✗  WRONG",
            font=('Segoe UI', 12, 'bold'),
            fg=c['text_bright'],
            bg=c['error'],
            activebackground=c['error_hover'],
            bd=0,
            padx=25,
            pady=12,
            cursor='hand2',
            command=self.mark_wrong
        )
        wrong_btn.pack(side=tk.LEFT, padx=8)

        repeat_btn = tk.Button(
            btn_frame,
            text="↻  REPEAT",
            font=('Segoe UI', 12, 'bold'),
            fg=c['text_bright'],
            bg=c['accent_blue'],
            activebackground=c['accent_hover'],
            bd=0,
            padx=25,
            pady=12,
            cursor='hand2',
            command=self.add_back_to_deck
        )
        repeat_btn.pack(side=tk.LEFT, padx=8)

        correct_btn = tk.Button(
            btn_frame,
            text="✓  CORRECT",
            font=('Segoe UI', 12, 'bold'),
            fg=c['text_bright'],
            bg=c['success'],
            activebackground=c['success_hover'],
            bd=0,
            padx=25,
            pady=12,
            cursor='hand2',
            command=self.mark_correct
        )
        correct_btn.pack(side=tk.LEFT, padx=8)

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

    def add_back_to_deck(self):
        """Add current card back to the end of the review queue without scoring"""
        if self.current_vowel:
            self.review_queue.append(self.current_vowel)
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

    def confirm_reset_progress(self):
        """Ask for confirmation before resetting progress"""
        result = messagebox.askyesno(
            "Reset Progress",
            "Are you sure you want to reset ALL progress?\n\n"
            "This will:\n"
            "• Move all cards back to Box 1\n"
            "• Reset your session count to 0\n"
            "• Clear all statistics\n\n"
            "This action cannot be undone!"
        )
        if result:
            self.leitner.reset_progress()
            self.update_stats_display()
            messagebox.showinfo("Progress Reset", "All progress has been reset.")
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
