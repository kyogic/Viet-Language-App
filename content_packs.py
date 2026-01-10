#!/usr/bin/env python3
"""
Vietnamese Language Learning - Content Packs
Downloadable vocabulary modules for specialized reading
"""

# Content pack metadata
CONTENT_PACKS = {
    "manga_fiction": {
        "id": "manga_fiction",
        "name": "Manga, Fiction & Fantasy",
        "description": "500+ common words and onomatopoeia for reading Vietnamese manga, light novels, and fiction",
        "word_count": 520,
        "categories": ["Common Words", "Onomatopoeia", "Emotions", "Actions", "Fantasy Terms"],
        "icon": "📚"
    },
    "self_help": {
        "id": "self_help",
        "name": "Self-Help & Personal Development",
        "description": "Essential vocabulary for self-improvement books, motivation, and personal growth",
        "word_count": 300,
        "categories": ["Mindset", "Goals", "Habits", "Emotions", "Success"],
        "icon": "🎯"
    },
    "millennial": {
        "id": "millennial",
        "name": "Millennial Vocabulary",
        "description": "Authentic Vietnamese slang and expressions from the millennial generation",
        "word_count": 86,
        "categories": ["Slang", "Internet", "Lifestyle", "Emotions", "Social"],
        "icon": "📱"
    },
    "genz": {
        "id": "genz",
        "name": "Gen Z Vocabulary",
        "description": "Vietnamese text abbreviations, cute speech, and youth expressions",
        "word_count": 90,
        "categories": ["Abbreviations", "Cute Speech", "Internet", "Gaming", "Expressions"],
        "icon": "🔥"
    }
}

# ============================================================
# MANGA, FICTION & FANTASY PACK
# ============================================================

MANGA_FICTION_PACK = {
    # === ONOMATOPOEIA (Sound Effects) ===
    "bùm": {
        "category": "onomatopoeia",
        "subcategory": "explosion",
        "examples": [
            {"word": "bùm", "meaning": "boom/explosion", "sentence": "Bùm! Cả tòa nhà nổ tung = Boom! The whole building exploded"},
        ]
    },
    "bốp": {
        "category": "onomatopoeia",
        "subcategory": "impact",
        "examples": [
            {"word": "bốp", "meaning": "slap/hit sound", "sentence": "Bốp! Một cái tát = Slap! A slap"},
        ]
    },
    "rầm": {
        "category": "onomatopoeia",
        "subcategory": "crash",
        "examples": [
            {"word": "rầm", "meaning": "crash/bang", "sentence": "Rầm! Cửa đóng sầm lại = Bang! The door slammed shut"},
        ]
    },
    "xoẹt": {
        "category": "onomatopoeia",
        "subcategory": "slash",
        "examples": [
            {"word": "xoẹt", "meaning": "slash/swish", "sentence": "Xoẹt! Kiếm chém qua = Swish! The sword slashed"},
        ]
    },
    "vèo": {
        "category": "onomatopoeia",
        "subcategory": "whoosh",
        "examples": [
            {"word": "vèo", "meaning": "whoosh/zoom", "sentence": "Vèo! Anh ta biến mất = Whoosh! He disappeared"},
        ]
    },
    "soạt": {
        "category": "onomatopoeia",
        "subcategory": "rustle",
        "examples": [
            {"word": "soạt", "meaning": "rustle/shuffle", "sentence": "Soạt soạt trong bụi cây = Rustling in the bushes"},
        ]
    },
    "rào rào": {
        "category": "onomatopoeia",
        "subcategory": "rain",
        "examples": [
            {"word": "rào rào", "meaning": "pattering rain", "sentence": "Mưa rơi rào rào = Rain pattering down"},
        ]
    },
    "đùng": {
        "category": "onomatopoeia",
        "subcategory": "gunshot",
        "examples": [
            {"word": "đùng", "meaning": "bang/gunshot", "sentence": "Đùng! Một tiếng súng = Bang! A gunshot"},
        ]
    },
    "phập": {
        "category": "onomatopoeia",
        "subcategory": "stab",
        "examples": [
            {"word": "phập", "meaning": "stab/pierce", "sentence": "Phập! Mũi kiếm đâm vào = Stab! The sword pierced"},
        ]
    },
    "xịt": {
        "category": "onomatopoeia",
        "subcategory": "spray",
        "examples": [
            {"word": "xịt", "meaning": "spray/hiss", "sentence": "Xịt! Khí phun ra = Hiss! Gas sprayed out"},
        ]
    },
    "ào": {
        "category": "onomatopoeia",
        "subcategory": "rush",
        "examples": [
            {"word": "ào", "meaning": "rushing water/wind", "sentence": "Nước ào ào chảy = Water rushing"},
        ]
    },
    "sầm": {
        "category": "onomatopoeia",
        "subcategory": "slam",
        "examples": [
            {"word": "sầm", "meaning": "slam/thud", "sentence": "Cửa đóng sầm = Door slammed"},
        ]
    },
    "rít": {
        "category": "onomatopoeia",
        "subcategory": "screech",
        "examples": [
            {"word": "rít", "meaning": "screech/squeal", "sentence": "Xe rít bánh = Car screeched"},
        ]
    },
    "vù": {
        "category": "onomatopoeia",
        "subcategory": "zoom",
        "examples": [
            {"word": "vù", "meaning": "zoom/speed", "sentence": "Xe phóng vù đi = Car zoomed away"},
        ]
    },
    "lách cách": {
        "category": "onomatopoeia",
        "subcategory": "clatter",
        "examples": [
            {"word": "lách cách", "meaning": "clatter/rattle", "sentence": "Tiếng lách cách = Clattering sound"},
        ]
    },
    "thình thịch": {
        "category": "onomatopoeia",
        "subcategory": "heartbeat",
        "examples": [
            {"word": "thình thịch", "meaning": "thump thump (heartbeat)", "sentence": "Tim đập thình thịch = Heart thumping"},
        ]
    },
    "hự": {
        "category": "onomatopoeia",
        "subcategory": "grunt",
        "examples": [
            {"word": "hự", "meaning": "grunt/ugh", "sentence": "Hự! Anh ta gầm lên = Ugh! He grunted"},
        ]
    },
    "ầm ầm": {
        "category": "onomatopoeia",
        "subcategory": "rumble",
        "examples": [
            {"word": "ầm ầm", "meaning": "rumbling/thunder", "sentence": "Sấm ầm ầm = Thunder rumbling"},
        ]
    },
    "lộp độp": {
        "category": "onomatopoeia",
        "subcategory": "patter",
        "examples": [
            {"word": "lộp độp", "meaning": "patter/tap", "sentence": "Mưa lộp độp = Rain pattering"},
        ]
    },
    "ríu rít": {
        "category": "onomatopoeia",
        "subcategory": "chirp",
        "examples": [
            {"word": "ríu rít", "meaning": "chirping/chattering", "sentence": "Chim ríu rít = Birds chirping"},
        ]
    },

    # === EXCLAMATIONS & INTERJECTIONS ===
    "trời ơi": {
        "category": "exclamation",
        "subcategory": "surprise",
        "examples": [
            {"word": "trời ơi", "meaning": "oh my god!", "sentence": "Trời ơi! Chuyện gì đây? = Oh my god! What's this?"},
        ]
    },
    "chết rồi": {
        "category": "exclamation",
        "subcategory": "shock",
        "examples": [
            {"word": "chết rồi", "meaning": "oh no!/I'm dead", "sentence": "Chết rồi! Tôi quên mất = Oh no! I forgot"},
        ]
    },
    "được rồi": {
        "category": "exclamation",
        "subcategory": "agreement",
        "examples": [
            {"word": "được rồi", "meaning": "okay/alright", "sentence": "Được rồi, tôi hiểu = Alright, I understand"},
        ]
    },
    "thôi nào": {
        "category": "exclamation",
        "subcategory": "pleading",
        "examples": [
            {"word": "thôi nào", "meaning": "come on/stop it", "sentence": "Thôi nào, đừng khóc = Come on, don't cry"},
        ]
    },
    "ơi": {
        "category": "exclamation",
        "subcategory": "calling",
        "examples": [
            {"word": "ơi", "meaning": "hey!/oh!", "sentence": "Anh ơi! = Hey brother!"},
        ]
    },
    "ối": {
        "category": "exclamation",
        "subcategory": "pain",
        "examples": [
            {"word": "ối", "meaning": "ouch/ow", "sentence": "Ối! Đau quá! = Ouch! It hurts!"},
        ]
    },
    "ái": {
        "category": "exclamation",
        "subcategory": "pain",
        "examples": [
            {"word": "ái", "meaning": "ouch/ow", "sentence": "Ái! Nóng quá = Ow! So hot"},
        ]
    },
    "ôi": {
        "category": "exclamation",
        "subcategory": "emotion",
        "examples": [
            {"word": "ôi", "meaning": "oh/alas", "sentence": "Ôi, đẹp quá! = Oh, so beautiful!"},
        ]
    },
    "chà": {
        "category": "exclamation",
        "subcategory": "impression",
        "examples": [
            {"word": "chà", "meaning": "wow/well", "sentence": "Chà, hay quá! = Wow, so good!"},
        ]
    },
    "ồ": {
        "category": "exclamation",
        "subcategory": "realization",
        "examples": [
            {"word": "ồ", "meaning": "oh/I see", "sentence": "Ồ, ra là vậy = Oh, I see"},
        ]
    },
    "á": {
        "category": "exclamation",
        "subcategory": "surprise",
        "examples": [
            {"word": "á", "meaning": "ah!/eek!", "sentence": "Á! Sợ quá! = Eek! So scary!"},
        ]
    },
    "hả": {
        "category": "exclamation",
        "subcategory": "question",
        "examples": [
            {"word": "hả", "meaning": "huh?/what?", "sentence": "Hả? Nói gì? = Huh? What did you say?"},
        ]
    },
    "ừ": {
        "category": "exclamation",
        "subcategory": "agreement",
        "examples": [
            {"word": "ừ", "meaning": "yeah/uh-huh", "sentence": "Ừ, tôi biết = Yeah, I know"},
        ]
    },
    "dạ": {
        "category": "exclamation",
        "subcategory": "polite_yes",
        "examples": [
            {"word": "dạ", "meaning": "yes (polite)", "sentence": "Dạ, thưa thầy = Yes, sir/teacher"},
        ]
    },
    "vâng": {
        "category": "exclamation",
        "subcategory": "formal_yes",
        "examples": [
            {"word": "vâng", "meaning": "yes (formal)", "sentence": "Vâng, tôi hiểu = Yes, I understand"},
        ]
    },

    # === COMMON VERBS (Action) ===
    "chạy": {
        "category": "verb",
        "subcategory": "movement",
        "examples": [
            {"word": "chạy", "meaning": "to run", "sentence": "Anh ta chạy rất nhanh = He runs very fast"},
            {"word": "chạy trốn", "meaning": "to escape/flee", "sentence": "Họ chạy trốn khỏi ngục = They escaped from prison"},
        ]
    },
    "đánh": {
        "category": "verb",
        "subcategory": "combat",
        "examples": [
            {"word": "đánh", "meaning": "to hit/fight", "sentence": "Hai người đánh nhau = Two people fighting"},
            {"word": "đánh bại", "meaning": "to defeat", "sentence": "Anh hùng đánh bại quái vật = The hero defeated the monster"},
        ]
    },
    "nhảy": {
        "category": "verb",
        "subcategory": "movement",
        "examples": [
            {"word": "nhảy", "meaning": "to jump", "sentence": "Cô ấy nhảy qua hàng rào = She jumped over the fence"},
        ]
    },
    "bay": {
        "category": "verb",
        "subcategory": "movement",
        "examples": [
            {"word": "bay", "meaning": "to fly", "sentence": "Rồng bay trên trời = The dragon flies in the sky"},
        ]
    },
    "biến mất": {
        "category": "verb",
        "subcategory": "magical",
        "examples": [
            {"word": "biến mất", "meaning": "to disappear", "sentence": "Pháp sư biến mất = The mage disappeared"},
        ]
    },
    "xuất hiện": {
        "category": "verb",
        "subcategory": "magical",
        "examples": [
            {"word": "xuất hiện", "meaning": "to appear", "sentence": "Ma quỷ xuất hiện = The demon appeared"},
        ]
    },
    "la hét": {
        "category": "verb",
        "subcategory": "voice",
        "examples": [
            {"word": "la hét", "meaning": "to scream/shout", "sentence": "Cô gái la hét = The girl screamed"},
        ]
    },
    "khóc": {
        "category": "verb",
        "subcategory": "emotion",
        "examples": [
            {"word": "khóc", "meaning": "to cry", "sentence": "Em bé khóc = The baby cried"},
        ]
    },
    "cười": {
        "category": "verb",
        "subcategory": "emotion",
        "examples": [
            {"word": "cười", "meaning": "to laugh/smile", "sentence": "Họ cười vui vẻ = They laughed happily"},
        ]
    },
    "chiến đấu": {
        "category": "verb",
        "subcategory": "combat",
        "examples": [
            {"word": "chiến đấu", "meaning": "to fight/battle", "sentence": "Chiến binh chiến đấu dũng cảm = The warrior fought bravely"},
        ]
    },
    "bảo vệ": {
        "category": "verb",
        "subcategory": "action",
        "examples": [
            {"word": "bảo vệ", "meaning": "to protect", "sentence": "Anh ấy bảo vệ cô gái = He protected the girl"},
        ]
    },
    "cứu": {
        "category": "verb",
        "subcategory": "action",
        "examples": [
            {"word": "cứu", "meaning": "to save/rescue", "sentence": "Anh hùng cứu thế giới = The hero saves the world"},
        ]
    },
    "giết": {
        "category": "verb",
        "subcategory": "combat",
        "examples": [
            {"word": "giết", "meaning": "to kill", "sentence": "Sát thủ giết mục tiêu = The assassin killed the target"},
        ]
    },
    "chết": {
        "category": "verb",
        "subcategory": "state",
        "examples": [
            {"word": "chết", "meaning": "to die", "sentence": "Nhân vật chính không chết = The main character didn't die"},
        ]
    },
    "sống": {
        "category": "verb",
        "subcategory": "state",
        "examples": [
            {"word": "sống", "meaning": "to live", "sentence": "Cô ấy sống sót = She survived"},
        ]
    },
    "yêu": {
        "category": "verb",
        "subcategory": "emotion",
        "examples": [
            {"word": "yêu", "meaning": "to love", "sentence": "Anh ấy yêu cô ấy = He loves her"},
        ]
    },
    "ghét": {
        "category": "verb",
        "subcategory": "emotion",
        "examples": [
            {"word": "ghét", "meaning": "to hate", "sentence": "Tôi ghét kẻ thù = I hate the enemy"},
        ]
    },
    "sợ": {
        "category": "verb",
        "subcategory": "emotion",
        "examples": [
            {"word": "sợ", "meaning": "to fear/be afraid", "sentence": "Cô bé sợ bóng tối = The girl fears the dark"},
        ]
    },
    "tin": {
        "category": "verb",
        "subcategory": "mental",
        "examples": [
            {"word": "tin", "meaning": "to believe/trust", "sentence": "Tôi tin bạn = I trust you"},
        ]
    },
    "phản bội": {
        "category": "verb",
        "subcategory": "action",
        "examples": [
            {"word": "phản bội", "meaning": "to betray", "sentence": "Hắn phản bội đồng đội = He betrayed his comrades"},
        ]
    },
    "tha thứ": {
        "category": "verb",
        "subcategory": "emotion",
        "examples": [
            {"word": "tha thứ", "meaning": "to forgive", "sentence": "Cô ấy tha thứ cho anh ta = She forgave him"},
        ]
    },
    "hứa": {
        "category": "verb",
        "subcategory": "speech",
        "examples": [
            {"word": "hứa", "meaning": "to promise", "sentence": "Tôi hứa sẽ trở về = I promise to return"},
        ]
    },
    "mơ": {
        "category": "verb",
        "subcategory": "mental",
        "examples": [
            {"word": "mơ", "meaning": "to dream", "sentence": "Anh ấy mơ thấy quá khứ = He dreamed of the past"},
        ]
    },
    "nhớ": {
        "category": "verb",
        "subcategory": "mental",
        "examples": [
            {"word": "nhớ", "meaning": "to remember/miss", "sentence": "Tôi nhớ cô ấy = I miss her"},
        ]
    },
    "quên": {
        "category": "verb",
        "subcategory": "mental",
        "examples": [
            {"word": "quên", "meaning": "to forget", "sentence": "Đừng quên tôi = Don't forget me"},
        ]
    },

    # === EMOTIONS & FEELINGS ===
    "vui": {
        "category": "emotion",
        "subcategory": "positive",
        "examples": [
            {"word": "vui", "meaning": "happy", "sentence": "Cô ấy rất vui = She is very happy"},
        ]
    },
    "buồn": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "buồn", "meaning": "sad", "sentence": "Anh ấy buồn lắm = He is very sad"},
        ]
    },
    "giận": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "giận", "meaning": "angry", "sentence": "Đừng giận tôi = Don't be angry with me"},
        ]
    },
    "tức giận": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "tức giận", "meaning": "furious/enraged", "sentence": "Anh ta tức giận điên cuồng = He was furiously enraged"},
        ]
    },
    "lo lắng": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "lo lắng", "meaning": "worried/anxious", "sentence": "Mẹ lo lắng cho con = Mother worried about her child"},
        ]
    },
    "hạnh phúc": {
        "category": "emotion",
        "subcategory": "positive",
        "examples": [
            {"word": "hạnh phúc", "meaning": "happiness/bliss", "sentence": "Họ sống hạnh phúc = They lived happily"},
        ]
    },
    "đau khổ": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "đau khổ", "meaning": "suffering/anguish", "sentence": "Nàng đau khổ vì mất người yêu = She suffered from losing her lover"},
        ]
    },
    "ngạc nhiên": {
        "category": "emotion",
        "subcategory": "neutral",
        "examples": [
            {"word": "ngạc nhiên", "meaning": "surprised", "sentence": "Tôi ngạc nhiên quá = I'm so surprised"},
        ]
    },
    "sốc": {
        "category": "emotion",
        "subcategory": "neutral",
        "examples": [
            {"word": "sốc", "meaning": "shocked", "sentence": "Cô ấy bị sốc = She was shocked"},
        ]
    },
    "xấu hổ": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "xấu hổ", "meaning": "embarrassed/ashamed", "sentence": "Anh ta xấu hổ đỏ mặt = He blushed with embarrassment"},
        ]
    },
    "ghen tị": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "ghen tị", "meaning": "jealous/envious", "sentence": "Cô ta ghen tị = She was jealous"},
        ]
    },
    "tự hào": {
        "category": "emotion",
        "subcategory": "positive",
        "examples": [
            {"word": "tự hào", "meaning": "proud", "sentence": "Tôi tự hào về bạn = I'm proud of you"},
        ]
    },
    "cô đơn": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "cô đơn", "meaning": "lonely", "sentence": "Anh ấy cô đơn = He is lonely"},
        ]
    },
    "kinh hãi": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "kinh hãi", "meaning": "terrified/horrified", "sentence": "Họ kinh hãi trước quái vật = They were horrified by the monster"},
        ]
    },
    "phấn khích": {
        "category": "emotion",
        "subcategory": "positive",
        "examples": [
            {"word": "phấn khích", "meaning": "excited", "sentence": "Bọn trẻ phấn khích = The kids were excited"},
        ]
    },
    "bình tĩnh": {
        "category": "emotion",
        "subcategory": "neutral",
        "examples": [
            {"word": "bình tĩnh", "meaning": "calm", "sentence": "Hãy bình tĩnh = Stay calm"},
        ]
    },
    "tuyệt vọng": {
        "category": "emotion",
        "subcategory": "negative",
        "examples": [
            {"word": "tuyệt vọng", "meaning": "desperate/hopeless", "sentence": "Anh ta tuyệt vọng = He was desperate"},
        ]
    },
    "hy vọng": {
        "category": "emotion",
        "subcategory": "positive",
        "examples": [
            {"word": "hy vọng", "meaning": "hope", "sentence": "Đừng mất hy vọng = Don't lose hope"},
        ]
    },

    # === FANTASY/MANGA TERMS ===
    "ma thuật": {
        "category": "fantasy",
        "subcategory": "magic",
        "examples": [
            {"word": "ma thuật", "meaning": "magic/sorcery", "sentence": "Cô ấy sử dụng ma thuật = She uses magic"},
        ]
    },
    "phép thuật": {
        "category": "fantasy",
        "subcategory": "magic",
        "examples": [
            {"word": "phép thuật", "meaning": "magic spell", "sentence": "Phép thuật mạnh mẽ = Powerful magic"},
        ]
    },
    "pháp sư": {
        "category": "fantasy",
        "subcategory": "character",
        "examples": [
            {"word": "pháp sư", "meaning": "mage/wizard", "sentence": "Pháp sư tung ra phép thuật = The mage cast a spell"},
        ]
    },
    "chiến binh": {
        "category": "fantasy",
        "subcategory": "character",
        "examples": [
            {"word": "chiến binh", "meaning": "warrior", "sentence": "Chiến binh dũng cảm = Brave warrior"},
        ]
    },
    "hiệp sĩ": {
        "category": "fantasy",
        "subcategory": "character",
        "examples": [
            {"word": "hiệp sĩ", "meaning": "knight", "sentence": "Hiệp sĩ cưỡi ngựa = Knight riding a horse"},
        ]
    },
    "anh hùng": {
        "category": "fantasy",
        "subcategory": "character",
        "examples": [
            {"word": "anh hùng", "meaning": "hero", "sentence": "Anh hùng cứu công chúa = The hero saves the princess"},
        ]
    },
    "ác nhân": {
        "category": "fantasy",
        "subcategory": "character",
        "examples": [
            {"word": "ác nhân", "meaning": "villain", "sentence": "Ác nhân bị đánh bại = The villain was defeated"},
        ]
    },
    "quái vật": {
        "category": "fantasy",
        "subcategory": "creature",
        "examples": [
            {"word": "quái vật", "meaning": "monster", "sentence": "Quái vật khổng lồ = Giant monster"},
        ]
    },
    "rồng": {
        "category": "fantasy",
        "subcategory": "creature",
        "examples": [
            {"word": "rồng", "meaning": "dragon", "sentence": "Rồng phun lửa = Dragon breathes fire"},
        ]
    },
    "ma quỷ": {
        "category": "fantasy",
        "subcategory": "creature",
        "examples": [
            {"word": "ma quỷ", "meaning": "demon/devil", "sentence": "Ma quỷ từ địa ngục = Demon from hell"},
        ]
    },
    "tiên": {
        "category": "fantasy",
        "subcategory": "creature",
        "examples": [
            {"word": "tiên", "meaning": "fairy/immortal", "sentence": "Nàng tiên xinh đẹp = Beautiful fairy"},
        ]
    },
    "yêu tinh": {
        "category": "fantasy",
        "subcategory": "creature",
        "examples": [
            {"word": "yêu tinh", "meaning": "demon/spirit", "sentence": "Yêu tinh biến hình = Shape-shifting demon"},
        ]
    },
    "hồn ma": {
        "category": "fantasy",
        "subcategory": "creature",
        "examples": [
            {"word": "hồn ma", "meaning": "ghost/spirit", "sentence": "Hồn ma ám ảnh = Haunting ghost"},
        ]
    },
    "kiếm": {
        "category": "fantasy",
        "subcategory": "weapon",
        "examples": [
            {"word": "kiếm", "meaning": "sword", "sentence": "Thanh kiếm huyền thoại = Legendary sword"},
        ]
    },
    "cung": {
        "category": "fantasy",
        "subcategory": "weapon",
        "examples": [
            {"word": "cung", "meaning": "bow", "sentence": "Cung và tên = Bow and arrow"},
        ]
    },
    "áo giáp": {
        "category": "fantasy",
        "subcategory": "equipment",
        "examples": [
            {"word": "áo giáp", "meaning": "armor", "sentence": "Áo giáp sắt = Iron armor"},
        ]
    },
    "bùa chú": {
        "category": "fantasy",
        "subcategory": "magic",
        "examples": [
            {"word": "bùa chú", "meaning": "spell/charm", "sentence": "Bùa chú bảo vệ = Protection charm"},
        ]
    },
    "sức mạnh": {
        "category": "fantasy",
        "subcategory": "power",
        "examples": [
            {"word": "sức mạnh", "meaning": "power/strength", "sentence": "Sức mạnh vô biên = Boundless power"},
        ]
    },
    "năng lượng": {
        "category": "fantasy",
        "subcategory": "power",
        "examples": [
            {"word": "năng lượng", "meaning": "energy", "sentence": "Năng lượng ma thuật = Magical energy"},
        ]
    },
    "trận chiến": {
        "category": "fantasy",
        "subcategory": "action",
        "examples": [
            {"word": "trận chiến", "meaning": "battle", "sentence": "Trận chiến cuối cùng = Final battle"},
        ]
    },
    "chiến thắng": {
        "category": "fantasy",
        "subcategory": "action",
        "examples": [
            {"word": "chiến thắng", "meaning": "victory", "sentence": "Chiến thắng vinh quang = Glorious victory"},
        ]
    },
    "thất bại": {
        "category": "fantasy",
        "subcategory": "action",
        "examples": [
            {"word": "thất bại", "meaning": "defeat/failure", "sentence": "Chấp nhận thất bại = Accept defeat"},
        ]
    },
    "nhiệm vụ": {
        "category": "fantasy",
        "subcategory": "quest",
        "examples": [
            {"word": "nhiệm vụ", "meaning": "mission/quest", "sentence": "Nhiệm vụ nguy hiểm = Dangerous mission"},
        ]
    },
    "kho báu": {
        "category": "fantasy",
        "subcategory": "quest",
        "examples": [
            {"word": "kho báu", "meaning": "treasure", "sentence": "Tìm kho báu = Find the treasure"},
        ]
    },
    "bí mật": {
        "category": "fantasy",
        "subcategory": "mystery",
        "examples": [
            {"word": "bí mật", "meaning": "secret", "sentence": "Bí mật cổ đại = Ancient secret"},
        ]
    },
    "lời nguyền": {
        "category": "fantasy",
        "subcategory": "magic",
        "examples": [
            {"word": "lời nguyền", "meaning": "curse", "sentence": "Lời nguyền đáng sợ = Terrible curse"},
        ]
    },
    "vương quốc": {
        "category": "fantasy",
        "subcategory": "place",
        "examples": [
            {"word": "vương quốc", "meaning": "kingdom", "sentence": "Vương quốc hùng mạnh = Powerful kingdom"},
        ]
    },
    "lâu đài": {
        "category": "fantasy",
        "subcategory": "place",
        "examples": [
            {"word": "lâu đài", "meaning": "castle", "sentence": "Lâu đài cổ kính = Ancient castle"},
        ]
    },
    "ngục tối": {
        "category": "fantasy",
        "subcategory": "place",
        "examples": [
            {"word": "ngục tối", "meaning": "dungeon", "sentence": "Ngục tối đáng sợ = Scary dungeon"},
        ]
    },

    # === COMMON NOUNS ===
    "người": {
        "category": "noun",
        "subcategory": "people",
        "examples": [
            {"word": "người", "meaning": "person/people", "sentence": "Nhiều người đến = Many people came"},
        ]
    },
    "đàn ông": {
        "category": "noun",
        "subcategory": "people",
        "examples": [
            {"word": "đàn ông", "meaning": "man", "sentence": "Đàn ông mạnh mẽ = Strong man"},
        ]
    },
    "phụ nữ": {
        "category": "noun",
        "subcategory": "people",
        "examples": [
            {"word": "phụ nữ", "meaning": "woman", "sentence": "Phụ nữ xinh đẹp = Beautiful woman"},
        ]
    },
    "bạn": {
        "category": "noun",
        "subcategory": "relationship",
        "examples": [
            {"word": "bạn", "meaning": "friend/you", "sentence": "Bạn thân nhất = Best friend"},
        ]
    },
    "kẻ thù": {
        "category": "noun",
        "subcategory": "relationship",
        "examples": [
            {"word": "kẻ thù", "meaning": "enemy", "sentence": "Kẻ thù nguy hiểm = Dangerous enemy"},
        ]
    },
    "đồng đội": {
        "category": "noun",
        "subcategory": "relationship",
        "examples": [
            {"word": "đồng đội", "meaning": "teammate/comrade", "sentence": "Đồng đội trung thành = Loyal comrade"},
        ]
    },
    "thế giới": {
        "category": "noun",
        "subcategory": "place",
        "examples": [
            {"word": "thế giới", "meaning": "world", "sentence": "Cứu thế giới = Save the world"},
        ]
    },
    "trái đất": {
        "category": "noun",
        "subcategory": "place",
        "examples": [
            {"word": "trái đất", "meaning": "Earth", "sentence": "Trái đất bị đe dọa = Earth is threatened"},
        ]
    },
    "cuộc sống": {
        "category": "noun",
        "subcategory": "abstract",
        "examples": [
            {"word": "cuộc sống", "meaning": "life", "sentence": "Cuộc sống mới = New life"},
        ]
    },
    "cái chết": {
        "category": "noun",
        "subcategory": "abstract",
        "examples": [
            {"word": "cái chết", "meaning": "death", "sentence": "Đối mặt cái chết = Face death"},
        ]
    },
    "tình yêu": {
        "category": "noun",
        "subcategory": "abstract",
        "examples": [
            {"word": "tình yêu", "meaning": "love", "sentence": "Tình yêu vĩnh cửu = Eternal love"},
        ]
    },
    "số phận": {
        "category": "noun",
        "subcategory": "abstract",
        "examples": [
            {"word": "số phận", "meaning": "fate/destiny", "sentence": "Số phận đã định = Fate has decided"},
        ]
    },
    "tương lai": {
        "category": "noun",
        "subcategory": "time",
        "examples": [
            {"word": "tương lai", "meaning": "future", "sentence": "Tương lai tươi sáng = Bright future"},
        ]
    },
    "quá khứ": {
        "category": "noun",
        "subcategory": "time",
        "examples": [
            {"word": "quá khứ", "meaning": "past", "sentence": "Quá khứ đau buồn = Sad past"},
        ]
    },
    "hiện tại": {
        "category": "noun",
        "subcategory": "time",
        "examples": [
            {"word": "hiện tại", "meaning": "present", "sentence": "Sống với hiện tại = Live in the present"},
        ]
    },

    # === ADJECTIVES ===
    "mạnh": {
        "category": "adjective",
        "subcategory": "strength",
        "examples": [
            {"word": "mạnh", "meaning": "strong", "sentence": "Anh ta rất mạnh = He is very strong"},
        ]
    },
    "yếu": {
        "category": "adjective",
        "subcategory": "strength",
        "examples": [
            {"word": "yếu", "meaning": "weak", "sentence": "Điểm yếu = Weak point"},
        ]
    },
    "nhanh": {
        "category": "adjective",
        "subcategory": "speed",
        "examples": [
            {"word": "nhanh", "meaning": "fast/quick", "sentence": "Nhanh lên! = Hurry up!"},
        ]
    },
    "chậm": {
        "category": "adjective",
        "subcategory": "speed",
        "examples": [
            {"word": "chậm", "meaning": "slow", "sentence": "Quá chậm = Too slow"},
        ]
    },
    "đẹp": {
        "category": "adjective",
        "subcategory": "appearance",
        "examples": [
            {"word": "đẹp", "meaning": "beautiful", "sentence": "Cô gái đẹp = Beautiful girl"},
        ]
    },
    "xấu": {
        "category": "adjective",
        "subcategory": "appearance",
        "examples": [
            {"word": "xấu", "meaning": "ugly/bad", "sentence": "Tình hình xấu = Bad situation"},
        ]
    },
    "tốt": {
        "category": "adjective",
        "subcategory": "quality",
        "examples": [
            {"word": "tốt", "meaning": "good", "sentence": "Rất tốt = Very good"},
        ]
    },
    "nguy hiểm": {
        "category": "adjective",
        "subcategory": "danger",
        "examples": [
            {"word": "nguy hiểm", "meaning": "dangerous", "sentence": "Rất nguy hiểm = Very dangerous"},
        ]
    },
    "an toàn": {
        "category": "adjective",
        "subcategory": "danger",
        "examples": [
            {"word": "an toàn", "meaning": "safe", "sentence": "Nơi an toàn = Safe place"},
        ]
    },
    "bí ẩn": {
        "category": "adjective",
        "subcategory": "mystery",
        "examples": [
            {"word": "bí ẩn", "meaning": "mysterious", "sentence": "Người đàn ông bí ẩn = Mysterious man"},
        ]
    },
    "cổ đại": {
        "category": "adjective",
        "subcategory": "time",
        "examples": [
            {"word": "cổ đại", "meaning": "ancient", "sentence": "Thời cổ đại = Ancient times"},
        ]
    },
    "huyền thoại": {
        "category": "adjective",
        "subcategory": "fantasy",
        "examples": [
            {"word": "huyền thoại", "meaning": "legendary", "sentence": "Nhân vật huyền thoại = Legendary figure"},
        ]
    },
    "vĩ đại": {
        "category": "adjective",
        "subcategory": "size",
        "examples": [
            {"word": "vĩ đại", "meaning": "great/grand", "sentence": "Chiến công vĩ đại = Great achievement"},
        ]
    },
    "khổng lồ": {
        "category": "adjective",
        "subcategory": "size",
        "examples": [
            {"word": "khổng lồ", "meaning": "giant/huge", "sentence": "Quái vật khổng lồ = Giant monster"},
        ]
    },
    "nhỏ bé": {
        "category": "adjective",
        "subcategory": "size",
        "examples": [
            {"word": "nhỏ bé", "meaning": "tiny/small", "sentence": "Cơ thể nhỏ bé = Tiny body"},
        ]
    },
    "đáng sợ": {
        "category": "adjective",
        "subcategory": "fear",
        "examples": [
            {"word": "đáng sợ", "meaning": "scary/terrifying", "sentence": "Khuôn mặt đáng sợ = Scary face"},
        ]
    },
    "dũng cảm": {
        "category": "adjective",
        "subcategory": "personality",
        "examples": [
            {"word": "dũng cảm", "meaning": "brave", "sentence": "Chiến binh dũng cảm = Brave warrior"},
        ]
    },
    "hèn nhát": {
        "category": "adjective",
        "subcategory": "personality",
        "examples": [
            {"word": "hèn nhát", "meaning": "cowardly", "sentence": "Kẻ hèn nhát = Coward"},
        ]
    },
    "trung thành": {
        "category": "adjective",
        "subcategory": "personality",
        "examples": [
            {"word": "trung thành", "meaning": "loyal", "sentence": "Người bạn trung thành = Loyal friend"},
        ]
    },
    "tàn nhẫn": {
        "category": "adjective",
        "subcategory": "personality",
        "examples": [
            {"word": "tàn nhẫn", "meaning": "cruel", "sentence": "Kẻ tàn nhẫn = Cruel person"},
        ]
    },

    # === TIME WORDS ===
    "bây giờ": {
        "category": "time",
        "subcategory": "present",
        "examples": [
            {"word": "bây giờ", "meaning": "now", "sentence": "Bây giờ! = Now!"},
        ]
    },
    "ngay": {
        "category": "time",
        "subcategory": "urgency",
        "examples": [
            {"word": "ngay", "meaning": "immediately", "sentence": "Đi ngay! = Go immediately!"},
        ]
    },
    "luôn": {
        "category": "time",
        "subcategory": "frequency",
        "examples": [
            {"word": "luôn", "meaning": "always", "sentence": "Tôi luôn ở đây = I'm always here"},
        ]
    },
    "không bao giờ": {
        "category": "time",
        "subcategory": "frequency",
        "examples": [
            {"word": "không bao giờ", "meaning": "never", "sentence": "Không bao giờ bỏ cuộc = Never give up"},
        ]
    },
    "cuối cùng": {
        "category": "time",
        "subcategory": "sequence",
        "examples": [
            {"word": "cuối cùng", "meaning": "finally/last", "sentence": "Cuối cùng đã đến = Finally arrived"},
        ]
    },
    "đột nhiên": {
        "category": "time",
        "subcategory": "sudden",
        "examples": [
            {"word": "đột nhiên", "meaning": "suddenly", "sentence": "Đột nhiên, anh ta biến mất = Suddenly, he disappeared"},
        ]
    },
    "từ từ": {
        "category": "time",
        "subcategory": "pace",
        "examples": [
            {"word": "từ từ", "meaning": "slowly/gradually", "sentence": "Từ từ thôi = Take it slow"},
        ]
    },

    # === CONNECTORS & COMMON PHRASES ===
    "nhưng": {
        "category": "connector",
        "subcategory": "contrast",
        "examples": [
            {"word": "nhưng", "meaning": "but", "sentence": "Mạnh nhưng chậm = Strong but slow"},
        ]
    },
    "và": {
        "category": "connector",
        "subcategory": "addition",
        "examples": [
            {"word": "và", "meaning": "and", "sentence": "Anh và em = You and me"},
        ]
    },
    "hoặc": {
        "category": "connector",
        "subcategory": "choice",
        "examples": [
            {"word": "hoặc", "meaning": "or", "sentence": "Sống hoặc chết = Live or die"},
        ]
    },
    "vì": {
        "category": "connector",
        "subcategory": "reason",
        "examples": [
            {"word": "vì", "meaning": "because", "sentence": "Vì tôi yêu cô ấy = Because I love her"},
        ]
    },
    "nên": {
        "category": "connector",
        "subcategory": "result",
        "examples": [
            {"word": "nên", "meaning": "so/therefore", "sentence": "Nên tôi phải đi = So I must go"},
        ]
    },
    "nếu": {
        "category": "connector",
        "subcategory": "condition",
        "examples": [
            {"word": "nếu", "meaning": "if", "sentence": "Nếu tôi chết = If I die"},
        ]
    },
    "khi": {
        "category": "connector",
        "subcategory": "time",
        "examples": [
            {"word": "khi", "meaning": "when", "sentence": "Khi tôi trở về = When I return"},
        ]
    },
    "tại sao": {
        "category": "question",
        "subcategory": "reason",
        "examples": [
            {"word": "tại sao", "meaning": "why", "sentence": "Tại sao? = Why?"},
        ]
    },
    "làm sao": {
        "category": "question",
        "subcategory": "method",
        "examples": [
            {"word": "làm sao", "meaning": "how", "sentence": "Làm sao đây? = What should I do?"},
        ]
    },
    "ở đâu": {
        "category": "question",
        "subcategory": "place",
        "examples": [
            {"word": "ở đâu", "meaning": "where", "sentence": "Cô ấy ở đâu? = Where is she?"},
        ]
    },
    "ai": {
        "category": "question",
        "subcategory": "person",
        "examples": [
            {"word": "ai", "meaning": "who", "sentence": "Ai đó? = Who's there?"},
        ]
    },
    "cái gì": {
        "category": "question",
        "subcategory": "thing",
        "examples": [
            {"word": "cái gì", "meaning": "what", "sentence": "Cái gì vậy? = What is that?"},
        ]
    },
}


# ============================================================
# SELF-HELP & PERSONAL DEVELOPMENT PACK
# ============================================================

SELF_HELP_PACK = {
    # === MINDSET & THINKING ===
    "tư duy": {
        "category": "mindset",
        "subcategory": "thinking",
        "examples": [
            {"word": "tư duy", "meaning": "mindset/thinking", "sentence": "Thay đổi tư duy = Change your mindset"},
        ]
    },
    "suy nghĩ": {
        "category": "mindset",
        "subcategory": "thinking",
        "examples": [
            {"word": "suy nghĩ", "meaning": "thought/think", "sentence": "Suy nghĩ tích cực = Think positively"},
        ]
    },
    "niềm tin": {
        "category": "mindset",
        "subcategory": "belief",
        "examples": [
            {"word": "niềm tin", "meaning": "belief/faith", "sentence": "Niềm tin vào bản thân = Belief in yourself"},
        ]
    },
    "tự tin": {
        "category": "mindset",
        "subcategory": "confidence",
        "examples": [
            {"word": "tự tin", "meaning": "confident/self-assured", "sentence": "Hãy tự tin hơn = Be more confident"},
        ]
    },
    "quyết tâm": {
        "category": "mindset",
        "subcategory": "determination",
        "examples": [
            {"word": "quyết tâm", "meaning": "determination", "sentence": "Quyết tâm thành công = Determined to succeed"},
        ]
    },
    "kiên trì": {
        "category": "mindset",
        "subcategory": "persistence",
        "examples": [
            {"word": "kiên trì", "meaning": "persistent/perseverance", "sentence": "Kiên trì theo đuổi = Persist in pursuing"},
        ]
    },
    "tích cực": {
        "category": "mindset",
        "subcategory": "attitude",
        "examples": [
            {"word": "tích cực", "meaning": "positive", "sentence": "Thái độ tích cực = Positive attitude"},
        ]
    },
    "tiêu cực": {
        "category": "mindset",
        "subcategory": "attitude",
        "examples": [
            {"word": "tiêu cực", "meaning": "negative", "sentence": "Tránh suy nghĩ tiêu cực = Avoid negative thinking"},
        ]
    },
    "lạc quan": {
        "category": "mindset",
        "subcategory": "outlook",
        "examples": [
            {"word": "lạc quan", "meaning": "optimistic", "sentence": "Luôn lạc quan = Always be optimistic"},
        ]
    },
    "bi quan": {
        "category": "mindset",
        "subcategory": "outlook",
        "examples": [
            {"word": "bi quan", "meaning": "pessimistic", "sentence": "Đừng bi quan = Don't be pessimistic"},
        ]
    },
    "cân bằng": {
        "category": "mindset",
        "subcategory": "balance",
        "examples": [
            {"word": "cân bằng", "meaning": "balance", "sentence": "Cân bằng cuộc sống = Life balance"},
        ]
    },
    "tập trung": {
        "category": "mindset",
        "subcategory": "focus",
        "examples": [
            {"word": "tập trung", "meaning": "focus/concentrate", "sentence": "Tập trung vào mục tiêu = Focus on goals"},
        ]
    },
    "sáng tạo": {
        "category": "mindset",
        "subcategory": "creativity",
        "examples": [
            {"word": "sáng tạo", "meaning": "creative/creativity", "sentence": "Tư duy sáng tạo = Creative thinking"},
        ]
    },
    "học hỏi": {
        "category": "mindset",
        "subcategory": "learning",
        "examples": [
            {"word": "học hỏi", "meaning": "learn/learning", "sentence": "Không ngừng học hỏi = Never stop learning"},
        ]
    },
    "phát triển": {
        "category": "mindset",
        "subcategory": "growth",
        "examples": [
            {"word": "phát triển", "meaning": "develop/growth", "sentence": "Phát triển bản thân = Self-development"},
        ]
    },

    # === GOALS & SUCCESS ===
    "mục tiêu": {
        "category": "goals",
        "subcategory": "target",
        "examples": [
            {"word": "mục tiêu", "meaning": "goal/objective", "sentence": "Đặt mục tiêu rõ ràng = Set clear goals"},
        ]
    },
    "ước mơ": {
        "category": "goals",
        "subcategory": "dream",
        "examples": [
            {"word": "ước mơ", "meaning": "dream", "sentence": "Theo đuổi ước mơ = Pursue your dreams"},
        ]
    },
    "tầm nhìn": {
        "category": "goals",
        "subcategory": "vision",
        "examples": [
            {"word": "tầm nhìn", "meaning": "vision", "sentence": "Tầm nhìn dài hạn = Long-term vision"},
        ]
    },
    "kế hoạch": {
        "category": "goals",
        "subcategory": "plan",
        "examples": [
            {"word": "kế hoạch", "meaning": "plan", "sentence": "Lập kế hoạch = Make a plan"},
        ]
    },
    "chiến lược": {
        "category": "goals",
        "subcategory": "strategy",
        "examples": [
            {"word": "chiến lược", "meaning": "strategy", "sentence": "Chiến lược thông minh = Smart strategy"},
        ]
    },
    "thành công": {
        "category": "goals",
        "subcategory": "success",
        "examples": [
            {"word": "thành công", "meaning": "success/succeed", "sentence": "Bí quyết thành công = Secret to success"},
        ]
    },
    "thành tựu": {
        "category": "goals",
        "subcategory": "achievement",
        "examples": [
            {"word": "thành tựu", "meaning": "achievement", "sentence": "Thành tựu lớn = Great achievement"},
        ]
    },
    "tiến bộ": {
        "category": "goals",
        "subcategory": "progress",
        "examples": [
            {"word": "tiến bộ", "meaning": "progress", "sentence": "Tiến bộ mỗi ngày = Progress every day"},
        ]
    },
    "cải thiện": {
        "category": "goals",
        "subcategory": "improvement",
        "examples": [
            {"word": "cải thiện", "meaning": "improve", "sentence": "Cải thiện liên tục = Continuous improvement"},
        ]
    },
    "đột phá": {
        "category": "goals",
        "subcategory": "breakthrough",
        "examples": [
            {"word": "đột phá", "meaning": "breakthrough", "sentence": "Tạo ra đột phá = Create a breakthrough"},
        ]
    },
    "hoàn thành": {
        "category": "goals",
        "subcategory": "completion",
        "examples": [
            {"word": "hoàn thành", "meaning": "complete/accomplish", "sentence": "Hoàn thành mục tiêu = Accomplish goals"},
        ]
    },

    # === HABITS & DISCIPLINE ===
    "thói quen": {
        "category": "habits",
        "subcategory": "habit",
        "examples": [
            {"word": "thói quen", "meaning": "habit", "sentence": "Thói quen tốt = Good habits"},
        ]
    },
    "kỷ luật": {
        "category": "habits",
        "subcategory": "discipline",
        "examples": [
            {"word": "kỷ luật", "meaning": "discipline", "sentence": "Tự kỷ luật = Self-discipline"},
        ]
    },
    "kiên nhẫn": {
        "category": "habits",
        "subcategory": "patience",
        "examples": [
            {"word": "kiên nhẫn", "meaning": "patient/patience", "sentence": "Hãy kiên nhẫn = Be patient"},
        ]
    },
    "chăm chỉ": {
        "category": "habits",
        "subcategory": "diligence",
        "examples": [
            {"word": "chăm chỉ", "meaning": "hardworking/diligent", "sentence": "Làm việc chăm chỉ = Work hard"},
        ]
    },
    "nỗ lực": {
        "category": "habits",
        "subcategory": "effort",
        "examples": [
            {"word": "nỗ lực", "meaning": "effort", "sentence": "Nỗ lực hết mình = Give your best effort"},
        ]
    },
    "rèn luyện": {
        "category": "habits",
        "subcategory": "practice",
        "examples": [
            {"word": "rèn luyện", "meaning": "train/practice", "sentence": "Rèn luyện mỗi ngày = Practice every day"},
        ]
    },
    "luyện tập": {
        "category": "habits",
        "subcategory": "exercise",
        "examples": [
            {"word": "luyện tập", "meaning": "practice/exercise", "sentence": "Luyện tập thường xuyên = Practice regularly"},
        ]
    },
    "thức dậy sớm": {
        "category": "habits",
        "subcategory": "morning",
        "examples": [
            {"word": "thức dậy sớm", "meaning": "wake up early", "sentence": "Thức dậy sớm mỗi ngày = Wake up early every day"},
        ]
    },
    "thiền": {
        "category": "habits",
        "subcategory": "mindfulness",
        "examples": [
            {"word": "thiền", "meaning": "meditate/meditation", "sentence": "Thiền mỗi sáng = Meditate every morning"},
        ]
    },
    "đọc sách": {
        "category": "habits",
        "subcategory": "learning",
        "examples": [
            {"word": "đọc sách", "meaning": "read books", "sentence": "Đọc sách mỗi ngày = Read books every day"},
        ]
    },
    "viết nhật ký": {
        "category": "habits",
        "subcategory": "reflection",
        "examples": [
            {"word": "viết nhật ký", "meaning": "write journal", "sentence": "Viết nhật ký hàng ngày = Write daily journal"},
        ]
    },

    # === EMOTIONS & WELL-BEING ===
    "hạnh phúc": {
        "category": "wellbeing",
        "subcategory": "happiness",
        "examples": [
            {"word": "hạnh phúc", "meaning": "happiness/happy", "sentence": "Tìm kiếm hạnh phúc = Seek happiness"},
        ]
    },
    "bình an": {
        "category": "wellbeing",
        "subcategory": "peace",
        "examples": [
            {"word": "bình an", "meaning": "peace/peaceful", "sentence": "Tâm bình an = Peaceful mind"},
        ]
    },
    "biết ơn": {
        "category": "wellbeing",
        "subcategory": "gratitude",
        "examples": [
            {"word": "biết ơn", "meaning": "grateful/gratitude", "sentence": "Sống biết ơn = Live with gratitude"},
        ]
    },
    "yêu thương": {
        "category": "wellbeing",
        "subcategory": "love",
        "examples": [
            {"word": "yêu thương", "meaning": "love/affection", "sentence": "Yêu thương bản thân = Love yourself"},
        ]
    },
    "chấp nhận": {
        "category": "wellbeing",
        "subcategory": "acceptance",
        "examples": [
            {"word": "chấp nhận", "meaning": "accept/acceptance", "sentence": "Chấp nhận bản thân = Accept yourself"},
        ]
    },
    "buông bỏ": {
        "category": "wellbeing",
        "subcategory": "letting_go",
        "examples": [
            {"word": "buông bỏ", "meaning": "let go", "sentence": "Học cách buông bỏ = Learn to let go"},
        ]
    },
    "căng thẳng": {
        "category": "wellbeing",
        "subcategory": "stress",
        "examples": [
            {"word": "căng thẳng", "meaning": "stress/stressed", "sentence": "Giảm căng thẳng = Reduce stress"},
        ]
    },
    "thư giãn": {
        "category": "wellbeing",
        "subcategory": "relaxation",
        "examples": [
            {"word": "thư giãn", "meaning": "relax/relaxation", "sentence": "Thời gian thư giãn = Relaxation time"},
        ]
    },
    "năng lượng": {
        "category": "wellbeing",
        "subcategory": "energy",
        "examples": [
            {"word": "năng lượng", "meaning": "energy", "sentence": "Năng lượng tích cực = Positive energy"},
        ]
    },
    "sức khỏe": {
        "category": "wellbeing",
        "subcategory": "health",
        "examples": [
            {"word": "sức khỏe", "meaning": "health", "sentence": "Sức khỏe là vàng = Health is gold"},
        ]
    },
    "tự do": {
        "category": "wellbeing",
        "subcategory": "freedom",
        "examples": [
            {"word": "tự do", "meaning": "freedom/free", "sentence": "Tự do tài chính = Financial freedom"},
        ]
    },

    # === RELATIONSHIPS ===
    "giao tiếp": {
        "category": "relationships",
        "subcategory": "communication",
        "examples": [
            {"word": "giao tiếp", "meaning": "communicate/communication", "sentence": "Kỹ năng giao tiếp = Communication skills"},
        ]
    },
    "lắng nghe": {
        "category": "relationships",
        "subcategory": "listening",
        "examples": [
            {"word": "lắng nghe", "meaning": "listen", "sentence": "Học cách lắng nghe = Learn to listen"},
        ]
    },
    "thấu hiểu": {
        "category": "relationships",
        "subcategory": "understanding",
        "examples": [
            {"word": "thấu hiểu", "meaning": "understand deeply", "sentence": "Thấu hiểu người khác = Understand others"},
        ]
    },
    "tôn trọng": {
        "category": "relationships",
        "subcategory": "respect",
        "examples": [
            {"word": "tôn trọng", "meaning": "respect", "sentence": "Tôn trọng lẫn nhau = Respect each other"},
        ]
    },
    "hợp tác": {
        "category": "relationships",
        "subcategory": "cooperation",
        "examples": [
            {"word": "hợp tác", "meaning": "cooperate/cooperation", "sentence": "Tinh thần hợp tác = Spirit of cooperation"},
        ]
    },
    "chia sẻ": {
        "category": "relationships",
        "subcategory": "sharing",
        "examples": [
            {"word": "chia sẻ", "meaning": "share", "sentence": "Chia sẻ kinh nghiệm = Share experiences"},
        ]
    },
    "giúp đỡ": {
        "category": "relationships",
        "subcategory": "helping",
        "examples": [
            {"word": "giúp đỡ", "meaning": "help", "sentence": "Giúp đỡ người khác = Help others"},
        ]
    },
    "cảm thông": {
        "category": "relationships",
        "subcategory": "empathy",
        "examples": [
            {"word": "cảm thông", "meaning": "empathy/sympathize", "sentence": "Biết cảm thông = Be empathetic"},
        ]
    },

    # === ACTION & MOTIVATION ===
    "hành động": {
        "category": "action",
        "subcategory": "action",
        "examples": [
            {"word": "hành động", "meaning": "action/act", "sentence": "Hành động ngay = Act now"},
        ]
    },
    "bắt đầu": {
        "category": "action",
        "subcategory": "start",
        "examples": [
            {"word": "bắt đầu", "meaning": "start/begin", "sentence": "Bắt đầu từ hôm nay = Start from today"},
        ]
    },
    "thay đổi": {
        "category": "action",
        "subcategory": "change",
        "examples": [
            {"word": "thay đổi", "meaning": "change", "sentence": "Thay đổi bản thân = Change yourself"},
        ]
    },
    "vượt qua": {
        "category": "action",
        "subcategory": "overcome",
        "examples": [
            {"word": "vượt qua", "meaning": "overcome/get through", "sentence": "Vượt qua khó khăn = Overcome difficulties"},
        ]
    },
    "đối mặt": {
        "category": "action",
        "subcategory": "face",
        "examples": [
            {"word": "đối mặt", "meaning": "face/confront", "sentence": "Đối mặt với sợ hãi = Face your fears"},
        ]
    },
    "quyết định": {
        "category": "action",
        "subcategory": "decision",
        "examples": [
            {"word": "quyết định", "meaning": "decide/decision", "sentence": "Quyết định quan trọng = Important decision"},
        ]
    },
    "lựa chọn": {
        "category": "action",
        "subcategory": "choice",
        "examples": [
            {"word": "lựa chọn", "meaning": "choose/choice", "sentence": "Lựa chọn đúng đắn = Right choice"},
        ]
    },
    "cố gắng": {
        "category": "action",
        "subcategory": "try",
        "examples": [
            {"word": "cố gắng", "meaning": "try/effort", "sentence": "Cố gắng hết sức = Try your best"},
        ]
    },
    "không bỏ cuộc": {
        "category": "action",
        "subcategory": "persistence",
        "examples": [
            {"word": "không bỏ cuộc", "meaning": "don't give up", "sentence": "Không bao giờ bỏ cuộc = Never give up"},
        ]
    },
    "dám": {
        "category": "action",
        "subcategory": "dare",
        "examples": [
            {"word": "dám", "meaning": "dare", "sentence": "Dám ước mơ lớn = Dare to dream big"},
        ]
    },

    # === CHALLENGES & GROWTH ===
    "thử thách": {
        "category": "challenges",
        "subcategory": "challenge",
        "examples": [
            {"word": "thử thách", "meaning": "challenge", "sentence": "Đón nhận thử thách = Embrace challenges"},
        ]
    },
    "khó khăn": {
        "category": "challenges",
        "subcategory": "difficulty",
        "examples": [
            {"word": "khó khăn", "meaning": "difficulty/hardship", "sentence": "Vượt qua khó khăn = Overcome hardships"},
        ]
    },
    "thất bại": {
        "category": "challenges",
        "subcategory": "failure",
        "examples": [
            {"word": "thất bại", "meaning": "failure/fail", "sentence": "Thất bại là mẹ thành công = Failure is the mother of success"},
        ]
    },
    "sai lầm": {
        "category": "challenges",
        "subcategory": "mistake",
        "examples": [
            {"word": "sai lầm", "meaning": "mistake", "sentence": "Học từ sai lầm = Learn from mistakes"},
        ]
    },
    "bài học": {
        "category": "challenges",
        "subcategory": "lesson",
        "examples": [
            {"word": "bài học", "meaning": "lesson", "sentence": "Bài học quý giá = Valuable lesson"},
        ]
    },
    "cơ hội": {
        "category": "challenges",
        "subcategory": "opportunity",
        "examples": [
            {"word": "cơ hội", "meaning": "opportunity", "sentence": "Nắm bắt cơ hội = Seize opportunities"},
        ]
    },
    "giới hạn": {
        "category": "challenges",
        "subcategory": "limit",
        "examples": [
            {"word": "giới hạn", "meaning": "limit", "sentence": "Phá vỡ giới hạn = Break limits"},
        ]
    },
    "vùng an toàn": {
        "category": "challenges",
        "subcategory": "comfort_zone",
        "examples": [
            {"word": "vùng an toàn", "meaning": "comfort zone", "sentence": "Ra khỏi vùng an toàn = Get out of comfort zone"},
        ]
    },

    # === TIME & PRODUCTIVITY ===
    "thời gian": {
        "category": "productivity",
        "subcategory": "time",
        "examples": [
            {"word": "thời gian", "meaning": "time", "sentence": "Quản lý thời gian = Time management"},
        ]
    },
    "ưu tiên": {
        "category": "productivity",
        "subcategory": "priority",
        "examples": [
            {"word": "ưu tiên", "meaning": "priority/prioritize", "sentence": "Xác định ưu tiên = Set priorities"},
        ]
    },
    "hiệu quả": {
        "category": "productivity",
        "subcategory": "effectiveness",
        "examples": [
            {"word": "hiệu quả", "meaning": "effective/efficiency", "sentence": "Làm việc hiệu quả = Work effectively"},
        ]
    },
    "năng suất": {
        "category": "productivity",
        "subcategory": "productivity",
        "examples": [
            {"word": "năng suất", "meaning": "productivity", "sentence": "Tăng năng suất = Increase productivity"},
        ]
    },
    "tổ chức": {
        "category": "productivity",
        "subcategory": "organization",
        "examples": [
            {"word": "tổ chức", "meaning": "organize/organization", "sentence": "Tổ chức công việc = Organize work"},
        ]
    },

    # === MONEY & FINANCE ===
    "tiền": {
        "category": "finance",
        "subcategory": "money",
        "examples": [
            {"word": "tiền", "meaning": "money", "sentence": "Quản lý tiền bạc = Manage money"},
        ]
    },
    "tiết kiệm": {
        "category": "finance",
        "subcategory": "saving",
        "examples": [
            {"word": "tiết kiệm", "meaning": "save/saving", "sentence": "Tiết kiệm tiền = Save money"},
        ]
    },
    "đầu tư": {
        "category": "finance",
        "subcategory": "investment",
        "examples": [
            {"word": "đầu tư", "meaning": "invest/investment", "sentence": "Đầu tư vào bản thân = Invest in yourself"},
        ]
    },
    "giàu có": {
        "category": "finance",
        "subcategory": "wealth",
        "examples": [
            {"word": "giàu có", "meaning": "wealthy/rich", "sentence": "Tư duy giàu có = Wealthy mindset"},
        ]
    },
    "thu nhập": {
        "category": "finance",
        "subcategory": "income",
        "examples": [
            {"word": "thu nhập", "meaning": "income", "sentence": "Tăng thu nhập = Increase income"},
        ]
    },
}


# ============================================================
# MILLENNIAL VOCABULARY PACK
# ============================================================

MILLENNIAL_PACK = {
    # Relationships
    "gấu": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "gấu", "meaning": "boyfriend/girlfriend (slang, literally 'bear')", "sentence": "Gấu của tao đâu rồi? = Where's my boyfriend/girlfriend?"},
        ]
    },
    "cưng": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "cưng", "meaning": "sweetheart/darling", "sentence": "Cưng ơi, đi đâu vậy? = Darling, where are you going?"},
        ]
    },
    "bồ": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "bồ", "meaning": "partner/significant other", "sentence": "Bồ tao đẹp lắm = My partner is very beautiful"},
        ]
    },
    "ế": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "ế", "meaning": "single/unmarried (often humorous)", "sentence": "Ế quá trời luôn = So hopelessly single"},
        ]
    },
    "thả thính": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "thả thính", "meaning": "to flirt (literally 'drop bait')", "sentence": "Đừng thả thính nữa = Stop flirting"},
        ]
    },
    "cẩu lương": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "cẩu lương", "meaning": "PDA/couple being sweet (literally 'dog food')", "sentence": "Ăn cẩu lương no rồi = Had enough of watching couples"},
        ]
    },
    "người ấy": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "người ấy", "meaning": "that special person/crush", "sentence": "Người ấy có người yêu chưa? = Does that person have a partner yet?"},
        ]
    },
    "tình cảm": {
        "category": "slang",
        "subcategory": "relationships",
        "examples": [
            {"word": "tình cảm", "meaning": "romantic feelings/affectionate", "sentence": "Hai đứa có tình cảm với nhau = They have feelings for each other"},
        ]
    },
    # Internet and Social
    "lướt": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "lướt", "meaning": "to scroll/browse", "sentence": "Lướt mạng cả ngày = Browsing online all day"},
        ]
    },
    "phốt": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "phốt", "meaning": "scandal/drama/expose", "sentence": "Bị phốt trên mạng = Got exposed online"},
        ]
    },
    "hóng": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "hóng", "meaning": "to eagerly wait for news/gossip", "sentence": "Hóng chuyện gì vậy? = What gossip are you waiting for?"},
        ]
    },
    "soi": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "soi", "meaning": "to investigate/stalk online", "sentence": "Soi trang cá nhân = Stalk their profile"},
        ]
    },
    "ảo": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "ảo", "meaning": "fake/virtual/not real", "sentence": "Sống ảo quá = Living a fake online life"},
        ]
    },
    "ảo tung chảo": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "ảo tung chảo", "meaning": "extremely fake/over the top fake", "sentence": "Ảnh ảo tung chảo = Photos are extremely edited"},
        ]
    },
    "bay màu": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "bay màu", "meaning": "account got banned/deleted", "sentence": "Tài khoản bay màu rồi = Account got banned"},
        ]
    },
    "câu": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "câu", "meaning": "to fish for (likes, attention)", "sentence": "Câu tương tác = Fishing for engagement"},
        ]
    },
    # Lifestyle and Emotions
    "đỉnh": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "đỉnh", "meaning": "awesome/peak/top tier", "sentence": "Đỉnh quá xá = Absolutely awesome"},
        ]
    },
    "đỉnh của chóp": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "đỉnh của chóp", "meaning": "the absolute peak/best of the best", "sentence": "Món này đỉnh của chóp = This dish is the absolute best"},
        ]
    },
    "xỉu": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "xỉu", "meaning": "to faint/I'm dying (figuratively)", "sentence": "Xỉu ngang xỉu dọc = I'm completely done"},
        ]
    },
    "phê": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "phê", "meaning": "satisfying/pleasurable", "sentence": "Phê quá đi = So satisfying"},
        ]
    },
    "ngầu": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "ngầu", "meaning": "cool/badass", "sentence": "Ngầu lắm luôn = So cool"},
        ]
    },
    "chanh sả": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "chanh sả", "meaning": "fancy/luxurious (playful)", "sentence": "Sống chanh sả ghê = Living so fancy"},
        ]
    },
    "sang chảnh": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "sang chảnh", "meaning": "luxurious/upscale", "sentence": "Quán này sang chảnh quá = This place is so fancy"},
        ]
    },
    "trầm cảm": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "trầm cảm", "meaning": "depressed/down", "sentence": "Hơi trầm cảm mấy hôm nay = Feeling a bit down lately"},
        ]
    },
    "bùn": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "bùn", "meaning": "sad (cute spelling of buồn)", "sentence": "Bùn ghê á = So sad"},
        ]
    },
    "vui vẻ": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "vui vẻ", "meaning": "happy/cheerful", "sentence": "Vui vẻ lên nào = Cheer up"},
        ]
    },
    "mệt": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "mệt", "meaning": "tired/exhausted (often dramatic)", "sentence": "Mệt với mày lắm = I'm so tired of you"},
        ]
    },
    "tức": {
        "category": "slang",
        "subcategory": "emotions",
        "examples": [
            {"word": "tức", "meaning": "annoyed/frustrated", "sentence": "Tức chết đi được = So frustrated I could die"},
        ]
    },
    # Work and Life
    "cày": {
        "category": "slang",
        "subcategory": "work",
        "examples": [
            {"word": "cày", "meaning": "to grind/work intensively", "sentence": "Cày phim cả đêm = Binge-watched all night"},
        ]
    },
    "cày cuốc": {
        "category": "slang",
        "subcategory": "work",
        "examples": [
            {"word": "cày cuốc", "meaning": "to work hard/toil", "sentence": "Cày cuốc kiếm tiền = Working hard to earn money"},
        ]
    },
    "nghỉ xả hơi": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "nghỉ xả hơi", "meaning": "to take a break/relax", "sentence": "Nghỉ xả hơi đi = Take a break"},
        ]
    },
    "bận": {
        "category": "slang",
        "subcategory": "work",
        "examples": [
            {"word": "bận", "meaning": "busy", "sentence": "Bận quá trời = Super busy"},
        ]
    },
    "rảnh": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "rảnh", "meaning": "free/available", "sentence": "Rảnh hông đi chơi? = Are you free to hang out?"},
        ]
    },
    "làm thêm": {
        "category": "slang",
        "subcategory": "work",
        "examples": [
            {"word": "làm thêm", "meaning": "to work overtime/part-time job", "sentence": "Phải làm thêm giờ = Have to work overtime"},
        ]
    },
    # Money and Going Out
    "cháy túi": {
        "category": "slang",
        "subcategory": "money",
        "examples": [
            {"word": "cháy túi", "meaning": "broke/out of money", "sentence": "Cuối tháng cháy túi = Broke at month end"},
        ]
    },
    "kẹt tiền": {
        "category": "slang",
        "subcategory": "money",
        "examples": [
            {"word": "kẹt tiền", "meaning": "short on cash", "sentence": "Đang kẹt tiền quá = Really short on cash"},
        ]
    },
    "nhậu": {
        "category": "slang",
        "subcategory": "food",
        "examples": [
            {"word": "nhậu", "meaning": "to drink alcohol socially", "sentence": "Đi nhậu không? = Wanna go drinking?"},
        ]
    },
    "ăn uống": {
        "category": "slang",
        "subcategory": "food",
        "examples": [
            {"word": "ăn uống", "meaning": "to eat and drink/dine", "sentence": "Đi ăn uống gì đi = Let's go eat something"},
        ]
    },
    "quẩy": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "quẩy", "meaning": "to party/have fun", "sentence": "Tối nay đi quẩy = Let's party tonight"},
        ]
    },
    "tụ tập": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "tụ tập", "meaning": "to gather/hang out", "sentence": "Tụ tập cuối tuần = Hang out on weekend"},
        ]
    },
    "thưởng thức": {
        "category": "slang",
        "subcategory": "food",
        "examples": [
            {"word": "thưởng thức", "meaning": "to enjoy/savor", "sentence": "Thưởng thức món ngon = Savor the delicious food"},
        ]
    },
    "lai rai": {
        "category": "slang",
        "subcategory": "food",
        "examples": [
            {"word": "lai rai", "meaning": "to drink casually/little by little", "sentence": "Lai rai vài ly = Have a few casual drinks"},
        ]
    },
    # Common Expressions
    "vậy á": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "vậy á", "meaning": "really?/is that so?", "sentence": "Vậy á? Thiệt hông? = Really? For real?"},
        ]
    },
    "thật hả": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "thật hả", "meaning": "really?/for real?", "sentence": "Thật hả? Không tin = Really? Can't believe it"},
        ]
    },
    "ơ kìa": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ơ kìa", "meaning": "oh look/hey there", "sentence": "Ơ kìa, ai đây? = Oh, who's this?"},
        ]
    },
    "biết chết liền": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "biết chết liền", "meaning": "I have absolutely no idea", "sentence": "Hỏi tao biết chết liền = Ask me, I have no clue"},
        ]
    },
    "chịu": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "chịu", "meaning": "I give up/I don't know", "sentence": "Chịu luôn, không biết = Give up, don't know"},
        ]
    },
    "kệ": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "kệ", "meaning": "don't care/let it be", "sentence": "Kệ nó đi = Let it be"},
        ]
    },
    "cũng được": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "cũng được", "meaning": "it's okay/sure/whatever", "sentence": "Cũng được thôi = It's fine"},
        ]
    },
    "hên xui": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "hên xui", "meaning": "depends on luck/hit or miss", "sentence": "Hên xui thôi = Just depends on luck"},
        ]
    },
    "may mắn": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "may mắn", "meaning": "lucky/fortunate", "sentence": "May mắn ghê = So lucky"},
        ]
    },
    "xui": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "xui", "meaning": "unlucky/bad luck", "sentence": "Xui quá trời = So unlucky"},
        ]
    },
    "bó tay": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "bó tay", "meaning": "give up/can't do anything", "sentence": "Bó tay với mày = I give up with you"},
        ]
    },
    "hết hồn": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "hết hồn", "meaning": "scared out of one's wits", "sentence": "Hết hồn luôn = Scared me to death"},
        ]
    },
    # Compliments and Descriptions
    "xinh": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "xinh", "meaning": "pretty/cute", "sentence": "Xinh quá vậy = So pretty"},
        ]
    },
    "đẹp trai": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "đẹp trai", "meaning": "handsome", "sentence": "Đẹp trai ghê = So handsome"},
        ]
    },
    "dễ thương": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "dễ thương", "meaning": "adorable/lovable/cute", "sentence": "Dễ thương quá đi = So adorable"},
        ]
    },
    "ngon": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "ngon", "meaning": "delicious/attractive", "sentence": "Ngon lành = Great/Perfect"},
        ]
    },
    "chất": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "chất", "meaning": "stylish/quality/cool", "sentence": "Chất quá xá = So cool/stylish"},
        ]
    },
    "xịn": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "xịn", "meaning": "premium/high quality/legit", "sentence": "Hàng xịn đó = That's legit stuff"},
        ]
    },
    "xịn xò": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "xịn xò", "meaning": "very premium/top quality", "sentence": "Xịn xò lắm nha = Very high quality"},
        ]
    },
    "giỏi": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "giỏi", "meaning": "skilled/good at", "sentence": "Giỏi quá ta = So skilled"},
        ]
    },
    "tài": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "tài", "meaning": "talented/skilled", "sentence": "Tài ghê = So talented"},
        ]
    },
    # Negative Expressions
    "dở": {
        "category": "slang",
        "subcategory": "negative",
        "examples": [
            {"word": "dở", "meaning": "bad/poor quality", "sentence": "Dở ẹc = Really bad"},
        ]
    },
    "nhạt": {
        "category": "slang",
        "subcategory": "negative",
        "examples": [
            {"word": "nhạt", "meaning": "boring/bland/uninteresting", "sentence": "Nhạt nhẽo quá = So boring"},
        ]
    },
    "chán": {
        "category": "slang",
        "subcategory": "negative",
        "examples": [
            {"word": "chán", "meaning": "bored/boring", "sentence": "Chán chết đi được = Bored to death"},
        ]
    },
    "kỳ": {
        "category": "slang",
        "subcategory": "negative",
        "examples": [
            {"word": "kỳ", "meaning": "weird/strange", "sentence": "Kỳ quá vậy = So weird"},
        ]
    },
    "lạ": {
        "category": "slang",
        "subcategory": "negative",
        "examples": [
            {"word": "lạ", "meaning": "strange/unfamiliar", "sentence": "Lạ lắm = Very strange"},
        ]
    },
    "lầy": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "lầy", "meaning": "cheeky/shameless/mischievous", "sentence": "Lầy quá mày = You're so cheeky"},
        ]
    },
    "lầy lội": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "lầy lội", "meaning": "very cheeky/shameless", "sentence": "Lầy lội vừa thôi = Don't be too shameless"},
        ]
    },
    "dìm hàng": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "dìm hàng", "meaning": "to make someone look bad (in photos)", "sentence": "Đừng dìm hàng tao = Don't make me look bad"},
        ]
    },
    "khen đểu": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "khen đểu", "meaning": "backhanded compliment", "sentence": "Khen đểu hoài à = Always giving backhanded compliments"},
        ]
    },
    "độc": {
        "category": "slang",
        "subcategory": "negative",
        "examples": [
            {"word": "độc", "meaning": "mean/harsh (of words)", "sentence": "Miệng độc quá = So sharp-tongued"},
        ]
    },
    # More lifestyle
    "tám": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "tám", "meaning": "to gossip/chat", "sentence": "Tám chuyện cả buổi = Gossiping all day"},
        ]
    },
    "buôn": {
        "category": "slang",
        "subcategory": "lifestyle",
        "examples": [
            {"word": "buôn", "meaning": "to chat/gossip (Southern)", "sentence": "Buôn dưa lê = Idle chatter"},
        ]
    },
    "sến": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "sến", "meaning": "cheesy/corny/tacky", "sentence": "Sến súa quá = So cheesy"},
        ]
    },
    "chảnh": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "chảnh", "meaning": "arrogant/stuck up/snobbish", "sentence": "Chảnh chọe quá = So stuck up"},
        ]
    },
    "soái ca": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "soái ca", "meaning": "prince charming/hot guy", "sentence": "Soái ca của em = My prince charming"},
        ]
    },
    "nữ thần": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "nữ thần", "meaning": "goddess (for beautiful women)", "sentence": "Nữ thần trong tim = Goddess in my heart"},
        ]
    },
    "trai đẹp": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "trai đẹp", "meaning": "handsome guy", "sentence": "Trai đẹp kìa = There's a handsome guy"},
        ]
    },
    "gái xinh": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "gái xinh", "meaning": "pretty girl", "sentence": "Gái xinh quá = Such a pretty girl"},
        ]
    },
    "điên": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "điên", "meaning": "crazy (can be positive or negative)", "sentence": "Điên quá mày = You're crazy"},
        ]
    },
    "khùng": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "khùng", "meaning": "crazy/nuts", "sentence": "Khùng rồi hả = Are you crazy?"},
        ]
    },
    "ghê": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ghê", "meaning": "impressive/scary/very (intensifier)", "sentence": "Giỏi ghê = So impressive"},
        ]
    },
    "quá trời": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "quá trời", "meaning": "so much/extremely", "sentence": "Đông quá trời = So crowded"},
        ]
    },
    "quá xá": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "quá xá", "meaning": "extremely/too much (Southern)", "sentence": "Ngon quá xá = Extremely delicious"},
        ]
    },
}


# ============================================================
# GEN Z VOCABULARY PACK
# ============================================================

GENZ_PACK = {
    # Vietnamese Text Abbreviations (very common in texting)
    "bt": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "bt", "meaning": "bình thường (normal/usual)", "sentence": "Bt thôi, không có gì = Just normal, nothing special"},
        ]
    },
    "dc": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "dc", "meaning": "được (okay/can)", "sentence": "Dc mà, đừng lo = It's okay, don't worry"},
        ]
    },
    "ko": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "ko", "meaning": "không (no/not)", "sentence": "Ko có đâu = Don't have it"},
        ]
    },
    "k": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "k", "meaning": "không (no)", "sentence": "K dc = Can't/Not okay"},
        ]
    },
    "nc": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "nc", "meaning": "nói chuyện (to chat)", "sentence": "Nc với tao đi = Chat with me"},
        ]
    },
    "vk": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "vk", "meaning": "vợ (wife)", "sentence": "Vk tao đẹp lắm = My wife is very pretty"},
        ]
    },
    "ck": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "ck", "meaning": "chồng (husband)", "sentence": "Ck em giỏi lắm = My husband is very skilled"},
        ]
    },
    "ny": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "ny", "meaning": "người yêu (lover/partner)", "sentence": "Ny mới hả? = New partner?"},
        ]
    },
    "ns": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "ns", "meaning": "nói sao (what to say)", "sentence": "Ns sao giờ? = What to say now?"},
        ]
    },
    "cx": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "cx", "meaning": "cũng (also)", "sentence": "Tao cx vậy = Me too"},
        ]
    },
    "vs": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "vs", "meaning": "với (with)", "sentence": "Đi vs tao = Go with me"},
        ]
    },
    "trc": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "trc", "meaning": "trước (before)", "sentence": "Gặp trc đi = Meet first"},
        ]
    },
    "sau": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "sau", "meaning": "sau (after/later)", "sentence": "Nc sau nha = Talk later okay"},
        ]
    },
    "r": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "r", "meaning": "rồi (already)", "sentence": "Xong r = Done already"},
        ]
    },
    "lm": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "lm", "meaning": "làm (to do)", "sentence": "Lm gì đó? = Doing what?"},
        ]
    },
    "hok": {
        "category": "slang",
        "subcategory": "abbreviations",
        "examples": [
            {"word": "hok", "meaning": "học (to study)", "sentence": "Đi hok chưa? = Gone to school yet?"},
        ]
    },
    # Exclamations and Particles
    "ủa": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ủa", "meaning": "huh?/wait what?", "sentence": "Ủa sao kỳ vậy? = Wait, why is that weird?"},
        ]
    },
    "á": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "á", "meaning": "exclamation/huh?", "sentence": "Gì á? = What?"},
        ]
    },
    "hả": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "hả", "meaning": "huh?/what?", "sentence": "Cái gì hả? = What is it?"},
        ]
    },
    "nha": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "nha", "meaning": "okay?/alright? (sentence ender)", "sentence": "Đi học nha = Go study, okay?"},
        ]
    },
    "nè": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "nè", "meaning": "hey/here (Southern)", "sentence": "Nè, nhìn đây = Hey, look here"},
        ]
    },
    "nghe": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "nghe", "meaning": "you hear?/okay? (Southern sentence ender)", "sentence": "Về sớm nghe = Come home early, okay?"},
        ]
    },
    "ui": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ui", "meaning": "oh!/oops!", "sentence": "Ui da, đau quá = Ouch, that hurts"},
        ]
    },
    "ôi": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ôi", "meaning": "oh my", "sentence": "Ôi trời ơi = Oh my god"},
        ]
    },
    "trời ơi": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "trời ơi", "meaning": "oh my god", "sentence": "Trời ơi đất hỡi = Oh heavens"},
        ]
    },
    "ê": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ê", "meaning": "hey!", "sentence": "Ê, đợi tao = Hey, wait for me"},
        ]
    },
    "ây da": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ây da", "meaning": "oh dear/oops", "sentence": "Ây da, quên mất = Oh dear, I forgot"},
        ]
    },
    "ối": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ối", "meaning": "oh no/oops", "sentence": "Ối giời ơi = Oh my goodness"},
        ]
    },
    # Cute/Playful Speech (nói nhõng nhẽo)
    "bùn": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "bùn", "meaning": "sad (cute form of buồn)", "sentence": "Bùn ghê á = So sad"},
        ]
    },
    "nhiu": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "nhiu", "meaning": "how much (cute form of nhiêu)", "sentence": "Yêu nhiu = Love how much"},
        ]
    },
    "hem": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "hem", "meaning": "no (cute form of không)", "sentence": "Hem có = Don't have"},
        ]
    },
    "hông": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "hông", "meaning": "no/not (Southern cute)", "sentence": "Hông biết = Don't know"},
        ]
    },
    "dạ": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "dạ", "meaning": "yes (polite/cute)", "sentence": "Dạ, em biết = Yes, I know"},
        ]
    },
    "ạ": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "ạ", "meaning": "polite particle (cute)", "sentence": "Cảm ơn ạ = Thank you (polite)"},
        ]
    },
    "nhen": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "nhen", "meaning": "okay? (cute form of nha)", "sentence": "Nhớ em nhen = Remember me, okay?"},
        ]
    },
    # Modern Vietnamese Slang
    "đu": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "đu", "meaning": "to follow/be a fan of", "sentence": "Đu theo người nổi tiếng = Follow a celebrity"},
        ]
    },
    "đu đưa": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "đu đưa", "meaning": "to go along with/hop on trend", "sentence": "Đu đưa theo mọi người = Follow along with everyone"},
        ]
    },
    "trẻ trâu": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "trẻ trâu", "meaning": "immature/childish person", "sentence": "Đừng trẻ trâu nữa = Stop being so immature"},
        ]
    },
    "gà": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "gà", "meaning": "noob/inexperienced (literally 'chicken')", "sentence": "Gà quá mày = You're such a noob"},
        ]
    },
    "gà mờ": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "gà mờ", "meaning": "total noob/clueless", "sentence": "Gà mờ lắm = So clueless"},
        ]
    },
    "chuẩn": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "chuẩn", "meaning": "correct/accurate/spot on", "sentence": "Chuẩn luôn = Exactly right"},
        ]
    },
    "chuẩn không cần chỉnh": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "chuẩn không cần chỉnh", "meaning": "perfectly correct/no need to adjust", "sentence": "Chuẩn không cần chỉnh = Absolutely perfect"},
        ]
    },
    "bá đạo": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "bá đạo", "meaning": "awesome/dominating", "sentence": "Bá đạo quá mày = You're so awesome"},
        ]
    },
    "bá cháy": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "bá cháy", "meaning": "super awesome/on fire", "sentence": "Bá cháy luôn = Absolutely killing it"},
        ]
    },
    "khủng": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "khủng", "meaning": "massive/impressive", "sentence": "Khủng quá = So impressive"},
        ]
    },
    "siêu": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "siêu", "meaning": "super/extremely", "sentence": "Siêu ngầu = Super cool"},
        ]
    },
    "max": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "max", "meaning": "maximum/extremely (Vietnamese usage)", "sentence": "Max buồn = Extremely sad"},
        ]
    },
    "cực": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "cực", "meaning": "extremely/very", "sentence": "Cực kỳ đẹp = Extremely beautiful"},
        ]
    },
    # Reactions and Responses
    "bé cái lầm": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "bé cái lầm", "meaning": "you're mistaken/that's wrong", "sentence": "Bé cái lầm rồi = You got it wrong"},
        ]
    },
    "bé cái nhầm": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "bé cái nhầm", "meaning": "you're confused/mistaken", "sentence": "Bé cái nhầm đó = That's a mistake"},
        ]
    },
    "đỉnh nóc kịch trần": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "đỉnh nóc kịch trần", "meaning": "absolutely peak/the highest level", "sentence": "Đỉnh nóc kịch trần luôn = Absolutely the peak"},
        ]
    },
    "toang": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "toang", "meaning": "failed/ruined/done for", "sentence": "Toang rồi = It's ruined/We're done"},
        ]
    },
    "toang cmnr": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "toang cmnr", "meaning": "completely ruined (emphatic)", "sentence": "Toang cmnr = Totally ruined"},
        ]
    },
    "ảo ma": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ảo ma", "meaning": "unbelievable/surreal", "sentence": "Ảo ma quá = So unbelievable"},
        ]
    },
    "ảo lòi": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ảo lòi", "meaning": "extremely fake/unreal", "sentence": "Ảo lòi luôn = Totally fake"},
        ]
    },
    "ngáo": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ngáo", "meaning": "dumb/out of it/zoned out", "sentence": "Ngáo quá mày = You're so out of it"},
        ]
    },
    "ngáo ngơ": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "ngáo ngơ", "meaning": "clueless/spacey", "sentence": "Sao ngáo ngơ vậy? = Why are you so spacey?"},
        ]
    },
    # Social Media/Internet Culture (Vietnamese terms)
    "hot": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "hot", "meaning": "trending/popular (Viet-ified)", "sentence": "Hot quá xá = Super trending"},
        ]
    },
    "nổi": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "nổi", "meaning": "famous/trending", "sentence": "Nổi rồi kìa = You're famous now"},
        ]
    },
    "nổi tiếng": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "nổi tiếng", "meaning": "famous/well-known", "sentence": "Nổi tiếng ghê = So famous"},
        ]
    },
    "đám đông": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "đám đông", "meaning": "the crowd/masses", "sentence": "Theo đám đông = Follow the crowd"},
        ]
    },
    "cộng đồng mạng": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "cộng đồng mạng", "meaning": "internet community/netizens", "sentence": "Cộng đồng mạng phẫn nộ = Netizens are angry"},
        ]
    },
    "bình luận": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "bình luận", "meaning": "comment", "sentence": "Bình luận đi = Leave a comment"},
        ]
    },
    "chia sẻ": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "chia sẻ", "meaning": "share (content)", "sentence": "Chia sẻ bài này = Share this post"},
        ]
    },
    "thích": {
        "category": "slang",
        "subcategory": "internet",
        "examples": [
            {"word": "thích", "meaning": "like (social media)", "sentence": "Thích bài đi = Like the post"},
        ]
    },
    # Gaming Terms (Vietnamese)
    "chơi": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "chơi", "meaning": "to play", "sentence": "Chơi game đi = Let's play games"},
        ]
    },
    "đánh": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "đánh", "meaning": "to play/fight (in games)", "sentence": "Đánh trận này = Play this match"},
        ]
    },
    "trận": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "trận", "meaning": "match/game round", "sentence": "Một trận nữa = One more match"},
        ]
    },
    "thắng": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "thắng", "meaning": "win", "sentence": "Thắng rồi! = We won!"},
        ]
    },
    "thua": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "thua", "meaning": "lose", "sentence": "Thua rồi = We lost"},
        ]
    },
    "leo": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "leo", "meaning": "to climb (rank)", "sentence": "Leo hạng = Climb rank"},
        ]
    },
    "rớt": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "rớt", "meaning": "to drop (rank)", "sentence": "Rớt hạng rồi = Dropped rank"},
        ]
    },
    "bắn": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "bắn", "meaning": "to shoot (in games)", "sentence": "Bắn chuẩn quá = Nice aim"},
        ]
    },
    "dame": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "dame", "meaning": "damage (Viet-ified)", "sentence": "Dame cao quá = High damage"},
        ]
    },
    "gánh": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "gánh", "meaning": "to carry (the team)", "sentence": "Gánh team = Carry the team"},
        ]
    },
    "cõng": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "cõng", "meaning": "to carry/boost", "sentence": "Cõng tao đi = Carry me"},
        ]
    },
    "phá": {
        "category": "slang",
        "subcategory": "gaming",
        "examples": [
            {"word": "phá", "meaning": "to troll/sabotage", "sentence": "Đừng phá game = Don't troll"},
        ]
    },
    # Youth Expressions
    "cháy": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "cháy", "meaning": "lit/exciting/broke", "sentence": "Cháy quá = So lit / So broke"},
        ]
    },
    "quẩy banh": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "quẩy banh", "meaning": "party hard/go crazy", "sentence": "Quẩy banh nóc = Party like crazy"},
        ]
    },
    "điên cuồng": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "điên cuồng", "meaning": "crazy/wild", "sentence": "Điên cuồng luôn = Going wild"},
        ]
    },
    "quậy": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "quậy", "meaning": "to make trouble/be rowdy", "sentence": "Quậy quá mày = You're so rowdy"},
        ]
    },
    "phá ngang": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "phá ngang", "meaning": "to interrupt/ruin", "sentence": "Đừng phá ngang = Don't interrupt"},
        ]
    },
    "gây": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "gây", "meaning": "to start/cause (trouble)", "sentence": "Gây chuyện hoài = Always causing trouble"},
        ]
    },
    # Describing People
    "ngọt": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "ngọt", "meaning": "sweet/smooth", "sentence": "Nói ngọt quá = Such sweet talk"},
        ]
    },
    "mặn": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "mặn", "meaning": "salty/bitter (personality)", "sentence": "Mặn quá mày = You're so salty"},
        ]
    },
    "lạnh": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "lạnh", "meaning": "cold (personality)", "sentence": "Lạnh lùng quá = So cold"},
        ]
    },
    "gắt": {
        "category": "slang",
        "subcategory": "expressions",
        "examples": [
            {"word": "gắt", "meaning": "fierce/savage/intense", "sentence": "Gắt quá = So savage"},
        ]
    },
    "mlem": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "mlem", "meaning": "yummy/cute (from tongue sound)", "sentence": "Mlem mlem = Yummy yummy"},
        ]
    },
    "cưng xỉu": {
        "category": "slang",
        "subcategory": "cute_speech",
        "examples": [
            {"word": "cưng xỉu", "meaning": "so cute I could die", "sentence": "Cưng xỉu luôn = So adorable"},
        ]
    },
    "dễ cưng": {
        "category": "slang",
        "subcategory": "compliments",
        "examples": [
            {"word": "dễ cưng", "meaning": "cute/adorable", "sentence": "Dễ cưng quá = So cute"},
        ]
    },
}


def get_pack_data(pack_id):
    """Get the vocabulary data for a specific pack"""
    if pack_id == "manga_fiction":
        return MANGA_FICTION_PACK
    elif pack_id == "self_help":
        return SELF_HELP_PACK
    elif pack_id == "millennial":
        return MILLENNIAL_PACK
    elif pack_id == "genz":
        return GENZ_PACK
    return {}


def get_pack_info(pack_id):
    """Get metadata for a specific pack"""
    return CONTENT_PACKS.get(pack_id, {})
