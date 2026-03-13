#!/usr/bin/env python3
import json
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'eras')
os.makedirs(BASE_DIR, exist_ok=True)

eras = [
    {
        "id": "ancient",
        "name": {"en": "Ancient", "es": "Antigüedad", "pt": "Antiguidade", "fr": "Antiquité", "de": "Antike", "zh": "古代", "hi": "प्राचीन काल", "ar": "العصور القديمة", "id": "Kuno", "ja": "古代"},
        "start_year": -3000,
        "end_year": -500,
        "description": {"en": "The earliest period of recorded human civilization, spanning the rise of Mesopotamia, Egypt, the Indus Valley, and early Chinese dynasties."}
    },
    {
        "id": "classical",
        "name": {"en": "Classical", "es": "Clásico", "pt": "Clássico", "fr": "Classique", "de": "Klassik", "zh": "古典时代", "hi": "शास्त्रीय काल", "ar": "العصر الكلاسيكي", "id": "Klasik", "ja": "古典期"},
        "start_year": -500,
        "end_year": 500,
        "description": {"en": "The age of Greek and Roman civilization, marked by foundational advances in philosophy, science, mathematics, and governance."}
    },
    {
        "id": "medieval",
        "name": {"en": "Medieval", "es": "Medieval", "pt": "Medieval", "fr": "Médiéval", "de": "Mittelalter", "zh": "中世纪", "hi": "मध्यकाल", "ar": "العصور الوسطى", "id": "Abad Pertengahan", "ja": "中世"},
        "start_year": 500,
        "end_year": 1300,
        "description": {"en": "The period between the fall of Rome and the Renaissance, characterized by feudalism in Europe and the Islamic Golden Age in the Middle East."}
    },
    {
        "id": "renaissance",
        "name": {"en": "Renaissance", "es": "Renacimiento", "pt": "Renascimento", "fr": "Renaissance", "de": "Renaissance", "zh": "文艺复兴", "hi": "पुनर्जागरण", "ar": "عصر النهضة", "id": "Renaisans", "ja": "ルネサンス"},
        "start_year": 1300,
        "end_year": 1600,
        "description": {"en": "A cultural movement that marked the transition from the Middle Ages to modernity, reviving interest in classical art, science, and humanism."}
    },
    {
        "id": "enlightenment",
        "name": {"en": "Enlightenment", "es": "Ilustración", "pt": "Iluminismo", "fr": "Siècle des Lumières", "de": "Aufklärung", "zh": "启蒙时代", "hi": "प्रबोधन काल", "ar": "عصر التنوير", "id": "Pencerahan", "ja": "啓蒙時代"},
        "start_year": 1600,
        "end_year": 1800,
        "description": {"en": "An intellectual movement emphasizing reason, science, and individual rights, laying the groundwork for modern democratic and scientific institutions."}
    },
    {
        "id": "industrial",
        "name": {"en": "Industrial", "es": "Industrial", "pt": "Industrial", "fr": "Industriel", "de": "Industriezeitalter", "zh": "工业时代", "hi": "औद्योगिक युग", "ar": "العصر الصناعي", "id": "Industri", "ja": "産業革命時代"},
        "start_year": 1800,
        "end_year": 1900,
        "description": {"en": "The era of rapid industrialization, technological innovation, and scientific breakthroughs in thermodynamics, electromagnetism, and chemistry."}
    },
    {
        "id": "modern",
        "name": {"en": "Modern", "es": "Moderno", "pt": "Moderno", "fr": "Moderne", "de": "Moderne", "zh": "现代", "hi": "आधुनिक काल", "ar": "العصر الحديث", "id": "Modern", "ja": "近代"},
        "start_year": 1900,
        "end_year": 1970,
        "description": {"en": "The age of relativity, quantum mechanics, nuclear energy, two world wars, and the space race, transforming science and global politics."}
    },
    {
        "id": "contemporary",
        "name": {"en": "Contemporary", "es": "Contemporáneo", "pt": "Contemporâneo", "fr": "Contemporain", "de": "Zeitgenössisch", "zh": "当代", "hi": "समकालीन", "ar": "العصر المعاصر", "id": "Kontemporer", "ja": "現代"},
        "start_year": 1970,
        "end_year": 2030,
        "description": {"en": "The current era defined by digital technology, globalization, the Standard Model of physics, and advances in cosmology and quantum computing."}
    },
]

count = 0
for e in eras:
    path = os.path.join(BASE_DIR, f"{e['id']}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(e, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f"Created {e['id']}.json")
    count += 1

print(f"\nTotal: {count} files generated.")
