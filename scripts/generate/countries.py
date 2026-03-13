#!/usr/bin/env python3
import json
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'countries')
os.makedirs(BASE_DIR, exist_ok=True)

countries = [
    {
        "id": "us",
        "name": {"en": "United States", "es": "Estados Unidos", "pt": "Estados Unidos", "fr": "États-Unis", "de": "Vereinigte Staaten", "zh": "美国", "hi": "संयुक्त राज्य", "ar": "الولايات المتحدة", "id": "Amerika Serikat", "ja": "アメリカ合衆国"},
        "region": "north-america",
        "description": {"en": "A federal republic in North America, a global superpower known for its cultural, economic, and scientific influence."}
    },
    {
        "id": "de",
        "name": {"en": "Germany", "es": "Alemania", "pt": "Alemanha", "fr": "Allemagne", "de": "Deutschland", "zh": "德国", "hi": "जर्मनी", "ar": "ألمانيا", "id": "Jerman", "ja": "ドイツ"},
        "region": "western-europe",
        "description": {"en": "A central European country with a rich history in science, philosophy, music, and engineering."}
    },
    {
        "id": "fr",
        "name": {"en": "France", "es": "Francia", "pt": "França", "fr": "France", "de": "Frankreich", "zh": "法国", "hi": "फ़्रांस", "ar": "فرنسا", "id": "Prancis", "ja": "フランス"},
        "region": "western-europe",
        "description": {"en": "A western European nation known for its contributions to art, philosophy, science, and political thought."}
    },
    {
        "id": "gb",
        "name": {"en": "United Kingdom", "es": "Reino Unido", "pt": "Reino Unido", "fr": "Royaume-Uni", "de": "Vereinigtes Königreich", "zh": "英国", "hi": "यूनाइटेड किंगडम", "ar": "المملكة المتحدة", "id": "Britania Raya", "ja": "イギリス"},
        "region": "western-europe",
        "description": {"en": "An island nation in northwestern Europe with a profound legacy in science, literature, and global governance."}
    },
    {
        "id": "it",
        "name": {"en": "Italy", "es": "Italia", "pt": "Itália", "fr": "Italie", "de": "Italien", "zh": "意大利", "hi": "इटली", "ar": "إيطاليا", "id": "Italia", "ja": "イタリア"},
        "region": "southern-europe",
        "description": {"en": "A southern European country and cradle of the Roman Empire and the Renaissance, renowned for art, science, and culture."}
    },
    {
        "id": "es",
        "name": {"en": "Spain", "es": "España", "pt": "Espanha", "fr": "Espagne", "de": "Spanien", "zh": "西班牙", "hi": "स्पेन", "ar": "إسبانيا", "id": "Spanyol", "ja": "スペイン"},
        "region": "southern-europe",
        "description": {"en": "A southern European country with a rich history in exploration, art, and literature."}
    },
    {
        "id": "pt",
        "name": {"en": "Portugal", "es": "Portugal", "pt": "Portugal", "fr": "Portugal", "de": "Portugal", "zh": "葡萄牙", "hi": "पुर्तगाल", "ar": "البرتغال", "id": "Portugal", "ja": "ポルトガル"},
        "region": "southern-europe",
        "description": {"en": "A southwestern European country known for its Age of Discovery and maritime exploration heritage."}
    },
    {
        "id": "nl",
        "name": {"en": "Netherlands", "es": "Países Bajos", "pt": "Países Baixos", "fr": "Pays-Bas", "de": "Niederlande", "zh": "荷兰", "hi": "नीदरलैंड", "ar": "هولندا", "id": "Belanda", "ja": "オランダ"},
        "region": "western-europe",
        "description": {"en": "A northwestern European country known for its contributions to optics, trade, painting, and scientific innovation."}
    },
    {
        "id": "be",
        "name": {"en": "Belgium", "es": "Bélgica", "pt": "Bélgica", "fr": "Belgique", "de": "Belgien", "zh": "比利时", "hi": "बेल्जियम", "ar": "بلجيكا", "id": "Belgia", "ja": "ベルギー"},
        "region": "western-europe",
        "description": {"en": "A western European country at the crossroads of Germanic and Latin cultures, home to major international institutions."}
    },
    {
        "id": "ch",
        "name": {"en": "Switzerland", "es": "Suiza", "pt": "Suíça", "fr": "Suisse", "de": "Schweiz", "zh": "瑞士", "hi": "स्विट्ज़रलैंड", "ar": "سويسرا", "id": "Swiss", "ja": "スイス"},
        "region": "western-europe",
        "description": {"en": "A central European country known for neutrality, precision engineering, banking, and world-class research institutions."}
    },
    {
        "id": "at",
        "name": {"en": "Austria", "es": "Austria", "pt": "Áustria", "fr": "Autriche", "de": "Österreich", "zh": "奥地利", "hi": "ऑस्ट्रिया", "ar": "النمسا", "id": "Austria", "ja": "オーストリア"},
        "region": "western-europe",
        "description": {"en": "A central European country with a distinguished legacy in music, philosophy, and physics."}
    },
    {
        "id": "se",
        "name": {"en": "Sweden", "es": "Suecia", "pt": "Suécia", "fr": "Suède", "de": "Schweden", "zh": "瑞典", "hi": "स्वीडन", "ar": "السويد", "id": "Swedia", "ja": "スウェーデン"},
        "region": "northern-europe",
        "description": {"en": "A Scandinavian country known for the Nobel Prizes, innovation, and contributions to science and social policy."}
    },
    {
        "id": "no",
        "name": {"en": "Norway", "es": "Noruega", "pt": "Noruega", "fr": "Norvège", "de": "Norwegen", "zh": "挪威", "hi": "नॉर्वे", "ar": "النرويج", "id": "Norwegia", "ja": "ノルウェー"},
        "region": "northern-europe",
        "description": {"en": "A Scandinavian country known for its exploration heritage, natural resources, and contributions to peace and science."}
    },
    {
        "id": "dk",
        "name": {"en": "Denmark", "es": "Dinamarca", "pt": "Dinamarca", "fr": "Danemark", "de": "Dänemark", "zh": "丹麦", "hi": "डेनमार्क", "ar": "الدنمارك", "id": "Denmark", "ja": "デンマーク"},
        "region": "northern-europe",
        "description": {"en": "A Scandinavian country known for contributions to physics, philosophy, and literature."}
    },
    {
        "id": "fi",
        "name": {"en": "Finland", "es": "Finlandia", "pt": "Finlândia", "fr": "Finlande", "de": "Finnland", "zh": "芬兰", "hi": "फ़िनलैंड", "ar": "فنلندا", "id": "Finlandia", "ja": "フィンランド"},
        "region": "northern-europe",
        "description": {"en": "A Nordic country known for its education system, technology innovation, and contributions to mathematics and design."}
    },
    {
        "id": "pl",
        "name": {"en": "Poland", "es": "Polonia", "pt": "Polônia", "fr": "Pologne", "de": "Polen", "zh": "波兰", "hi": "पोलैंड", "ar": "بولندا", "id": "Polandia", "ja": "ポーランド"},
        "region": "eastern-europe",
        "description": {"en": "A central-eastern European country with notable contributions to astronomy, mathematics, and literature."}
    },
    {
        "id": "cz",
        "name": {"en": "Czech Republic", "es": "República Checa", "pt": "República Tcheca", "fr": "République tchèque", "de": "Tschechien", "zh": "捷克", "hi": "चेक गणराज्य", "ar": "التشيك", "id": "Republik Ceko", "ja": "チェコ"},
        "region": "eastern-europe",
        "description": {"en": "A central European country with a rich history in science, literature, and music."}
    },
    {
        "id": "hu",
        "name": {"en": "Hungary", "es": "Hungría", "pt": "Hungria", "fr": "Hongrie", "de": "Ungarn", "zh": "匈牙利", "hi": "हंगरी", "ar": "المجر", "id": "Hungaria", "ja": "ハンガリー"},
        "region": "eastern-europe",
        "description": {"en": "A central European country that produced many influential physicists and mathematicians of the 20th century."}
    },
    {
        "id": "gr",
        "name": {"en": "Greece", "es": "Grecia", "pt": "Grécia", "fr": "Grèce", "de": "Griechenland", "zh": "希腊", "hi": "यूनान", "ar": "اليونان", "id": "Yunani", "ja": "ギリシャ"},
        "region": "southern-europe",
        "description": {"en": "The birthplace of Western philosophy, democracy, and foundational contributions to mathematics and science."}
    },
    {
        "id": "tr",
        "name": {"en": "Turkey", "es": "Turquía", "pt": "Turquia", "fr": "Turquie", "de": "Türkei", "zh": "土耳其", "hi": "तुर्की", "ar": "تركيا", "id": "Turki", "ja": "トルコ"},
        "region": "middle-east",
        "description": {"en": "A transcontinental country bridging Europe and Asia with a rich history spanning the Ottoman and Byzantine empires."}
    },
    {
        "id": "ru",
        "name": {"en": "Russia", "es": "Rusia", "pt": "Rússia", "fr": "Russie", "de": "Russland", "zh": "俄罗斯", "hi": "रूस", "ar": "روسيا", "id": "Rusia", "ja": "ロシア"},
        "region": "eastern-europe",
        "description": {"en": "The world's largest country, with significant contributions to physics, mathematics, literature, and space exploration."}
    },
    {
        "id": "ua",
        "name": {"en": "Ukraine", "es": "Ucrania", "pt": "Ucrânia", "fr": "Ukraine", "de": "Ukraine", "zh": "乌克兰", "hi": "यूक्रेन", "ar": "أوكرانيا", "id": "Ukraina", "ja": "ウクライナ"},
        "region": "eastern-europe",
        "description": {"en": "An eastern European country with contributions to science, aerospace, and mathematics."}
    },
    {
        "id": "il",
        "name": {"en": "Israel", "es": "Israel", "pt": "Israel", "fr": "Israël", "de": "Israel", "zh": "以色列", "hi": "इज़राइल", "ar": "إسرائيل", "id": "Israel", "ja": "イスラエル"},
        "region": "middle-east",
        "description": {"en": "A Middle Eastern country known for its advanced technology sector and scientific research institutions."}
    },
    {
        "id": "eg",
        "name": {"en": "Egypt", "es": "Egipto", "pt": "Egito", "fr": "Égypte", "de": "Ägypten", "zh": "埃及", "hi": "मिस्र", "ar": "مصر", "id": "Mesir", "ja": "エジプト"},
        "region": "north-africa",
        "description": {"en": "A North African country with one of the oldest civilizations, renowned for ancient engineering, mathematics, and astronomy."}
    },
    {
        "id": "ir",
        "name": {"en": "Iran", "es": "Irán", "pt": "Irã", "fr": "Iran", "de": "Iran", "zh": "伊朗", "hi": "ईरान", "ar": "إيران", "id": "Iran", "ja": "イラン"},
        "region": "middle-east",
        "description": {"en": "A Middle Eastern country with a rich Persian heritage and major historical contributions to mathematics, astronomy, and medicine."}
    },
    {
        "id": "iq",
        "name": {"en": "Iraq", "es": "Irak", "pt": "Iraque", "fr": "Irak", "de": "Irak", "zh": "伊拉克", "hi": "इराक़", "ar": "العراق", "id": "Irak", "ja": "イラク"},
        "region": "middle-east",
        "description": {"en": "A Middle Eastern country in Mesopotamia, the cradle of civilization, with foundational contributions to writing, mathematics, and astronomy."}
    },
    {
        "id": "sa",
        "name": {"en": "Saudi Arabia", "es": "Arabia Saudita", "pt": "Arábia Saudita", "fr": "Arabie saoudite", "de": "Saudi-Arabien", "zh": "沙特阿拉伯", "hi": "सऊदी अरब", "ar": "المملكة العربية السعودية", "id": "Arab Saudi", "ja": "サウジアラビア"},
        "region": "middle-east",
        "description": {"en": "A Middle Eastern country on the Arabian Peninsula, birthplace of Islam and a major geopolitical power."}
    },
    {
        "id": "in",
        "name": {"en": "India", "es": "India", "pt": "Índia", "fr": "Inde", "de": "Indien", "zh": "印度", "hi": "भारत", "ar": "الهند", "id": "India", "ja": "インド"},
        "region": "south-asia",
        "description": {"en": "A South Asian country with ancient traditions in mathematics, astronomy, philosophy, and a rapidly growing scientific community."}
    },
    {
        "id": "pk",
        "name": {"en": "Pakistan", "es": "Pakistán", "pt": "Paquistão", "fr": "Pakistan", "de": "Pakistan", "zh": "巴基斯坦", "hi": "पाकिस्तान", "ar": "باكستان", "id": "Pakistan", "ja": "パキスタン"},
        "region": "south-asia",
        "description": {"en": "A South Asian country that produced the first Muslim Nobel laureate in physics and has a growing scientific infrastructure."}
    },
    {
        "id": "bd",
        "name": {"en": "Bangladesh", "es": "Bangladés", "pt": "Bangladesh", "fr": "Bangladesh", "de": "Bangladesch", "zh": "孟加拉国", "hi": "बांग्लादेश", "ar": "بنغلاديش", "id": "Bangladesh", "ja": "バングラデシュ"},
        "region": "south-asia",
        "description": {"en": "A South Asian country with a growing presence in technology and social innovation."}
    },
    {
        "id": "cn",
        "name": {"en": "China", "es": "China", "pt": "China", "fr": "Chine", "de": "China", "zh": "中国", "hi": "चीन", "ar": "الصين", "id": "Tiongkok", "ja": "中国"},
        "region": "east-asia",
        "description": {"en": "An East Asian country with one of the world's oldest civilizations and foundational inventions in science and technology."}
    },
    {
        "id": "jp",
        "name": {"en": "Japan", "es": "Japón", "pt": "Japão", "fr": "Japon", "de": "Japan", "zh": "日本", "hi": "जापान", "ar": "اليابان", "id": "Jepang", "ja": "日本"},
        "region": "east-asia",
        "description": {"en": "An East Asian island nation known for its technological innovation, scientific research, and cultural heritage."}
    },
    {
        "id": "kr",
        "name": {"en": "South Korea", "es": "Corea del Sur", "pt": "Coreia do Sul", "fr": "Corée du Sud", "de": "Südkorea", "zh": "韩国", "hi": "दक्षिण कोरिया", "ar": "كوريا الجنوبية", "id": "Korea Selatan", "ja": "韓国"},
        "region": "east-asia",
        "description": {"en": "An East Asian country known for rapid technological advancement and scientific research."}
    },
    {
        "id": "mn",
        "name": {"en": "Mongolia", "es": "Mongolia", "pt": "Mongólia", "fr": "Mongolie", "de": "Mongolei", "zh": "蒙古", "hi": "मंगोलिया", "ar": "منغوليا", "id": "Mongolia", "ja": "モンゴル"},
        "region": "east-asia",
        "description": {"en": "A landlocked East Asian country known for the Mongol Empire and its nomadic cultural heritage."}
    },
    {
        "id": "th",
        "name": {"en": "Thailand", "es": "Tailandia", "pt": "Tailândia", "fr": "Thaïlande", "de": "Thailand", "zh": "泰国", "hi": "थाईलैंड", "ar": "تايلاند", "id": "Thailand", "ja": "タイ"},
        "region": "southeast-asia",
        "description": {"en": "A Southeast Asian country known for its cultural heritage, Buddhist traditions, and growing scientific community."}
    },
    {
        "id": "vn",
        "name": {"en": "Vietnam", "es": "Vietnam", "pt": "Vietnã", "fr": "Viêt Nam", "de": "Vietnam", "zh": "越南", "hi": "वियतनाम", "ar": "فيتنام", "id": "Vietnam", "ja": "ベトナム"},
        "region": "southeast-asia",
        "description": {"en": "A Southeast Asian country with a long history and growing contributions to science and technology."}
    },
    {
        "id": "id",
        "name": {"en": "Indonesia", "es": "Indonesia", "pt": "Indonésia", "fr": "Indonésie", "de": "Indonesien", "zh": "印度尼西亚", "hi": "इंडोनेशिया", "ar": "إندونيسيا", "id": "Indonesia", "ja": "インドネシア"},
        "region": "southeast-asia",
        "description": {"en": "The world's largest archipelago nation in Southeast Asia, with diverse cultures and a growing research sector."}
    },
    {
        "id": "my",
        "name": {"en": "Malaysia", "es": "Malasia", "pt": "Malásia", "fr": "Malaisie", "de": "Malaysia", "zh": "马来西亚", "hi": "मलेशिया", "ar": "ماليزيا", "id": "Malaysia", "ja": "マレーシア"},
        "region": "southeast-asia",
        "description": {"en": "A Southeast Asian country known for its multicultural society and growing technology sector."}
    },
    {
        "id": "sg",
        "name": {"en": "Singapore", "es": "Singapur", "pt": "Singapura", "fr": "Singapour", "de": "Singapur", "zh": "新加坡", "hi": "सिंगापुर", "ar": "سنغافورة", "id": "Singapura", "ja": "シンガポール"},
        "region": "southeast-asia",
        "description": {"en": "A Southeast Asian city-state known for its advanced economy, technology hub status, and world-class research."}
    },
    {
        "id": "ph",
        "name": {"en": "Philippines", "es": "Filipinas", "pt": "Filipinas", "fr": "Philippines", "de": "Philippinen", "zh": "菲律宾", "hi": "फ़िलीपींस", "ar": "الفلبين", "id": "Filipina", "ja": "フィリピン"},
        "region": "southeast-asia",
        "description": {"en": "A Southeast Asian archipelago with a diverse cultural heritage and growing contributions to science and education."}
    },
    {
        "id": "au",
        "name": {"en": "Australia", "es": "Australia", "pt": "Austrália", "fr": "Australie", "de": "Australien", "zh": "澳大利亚", "hi": "ऑस्ट्रेलिया", "ar": "أستراليا", "id": "Australia", "ja": "オーストラリア"},
        "region": "oceania",
        "description": {"en": "A continent-nation in the Southern Hemisphere known for its unique biodiversity and strong scientific research institutions."}
    },
    {
        "id": "nz",
        "name": {"en": "New Zealand", "es": "Nueva Zelanda", "pt": "Nova Zelândia", "fr": "Nouvelle-Zélande", "de": "Neuseeland", "zh": "新西兰", "hi": "न्यूज़ीलैंड", "ar": "نيوزيلندا", "id": "Selandia Baru", "ja": "ニュージーランド"},
        "region": "oceania",
        "description": {"en": "An island nation in the southwestern Pacific known for pioneering nuclear physics research and environmental leadership."}
    },
    {
        "id": "za",
        "name": {"en": "South Africa", "es": "Sudáfrica", "pt": "África do Sul", "fr": "Afrique du Sud", "de": "Südafrika", "zh": "南非", "hi": "दक्षिण अफ़्रीका", "ar": "جنوب أفريقيا", "id": "Afrika Selatan", "ja": "南アフリカ"},
        "region": "sub-saharan-africa",
        "description": {"en": "A southern African country with a diverse society and notable contributions to science and medicine."}
    },
    {
        "id": "ng",
        "name": {"en": "Nigeria", "es": "Nigeria", "pt": "Nigéria", "fr": "Nigéria", "de": "Nigeria", "zh": "尼日利亚", "hi": "नाइजीरिया", "ar": "نيجيريا", "id": "Nigeria", "ja": "ナイジェリア"},
        "region": "sub-saharan-africa",
        "description": {"en": "Africa's most populous country, with a growing technology ecosystem and contributions to literature and the arts."}
    },
    {
        "id": "ke",
        "name": {"en": "Kenya", "es": "Kenia", "pt": "Quênia", "fr": "Kenya", "de": "Kenia", "zh": "肯尼亚", "hi": "केन्या", "ar": "كينيا", "id": "Kenya", "ja": "ケニア"},
        "region": "sub-saharan-africa",
        "description": {"en": "An East African country known for its wildlife, innovation in mobile technology, and growing scientific research."}
    },
    {
        "id": "et",
        "name": {"en": "Ethiopia", "es": "Etiopía", "pt": "Etiópia", "fr": "Éthiopie", "de": "Äthiopien", "zh": "埃塞俄比亚", "hi": "इथियोपिया", "ar": "إثيوبيا", "id": "Ethiopia", "ja": "エチオピア"},
        "region": "sub-saharan-africa",
        "description": {"en": "One of the oldest nations in the world, located in the Horn of Africa, with a unique cultural and historical heritage."}
    },
    {
        "id": "br",
        "name": {"en": "Brazil", "es": "Brasil", "pt": "Brasil", "fr": "Brésil", "de": "Brasilien", "zh": "巴西", "hi": "ब्राज़ील", "ar": "البرازيل", "id": "Brasil", "ja": "ブラジル"},
        "region": "south-america",
        "description": {"en": "The largest country in South America, known for its biodiversity and growing contributions to physics and aerospace research."}
    },
    {
        "id": "ar",
        "name": {"en": "Argentina", "es": "Argentina", "pt": "Argentina", "fr": "Argentine", "de": "Argentinien", "zh": "阿根廷", "hi": "अर्जेंटीना", "ar": "الأرجنتين", "id": "Argentina", "ja": "アルゼンチン"},
        "region": "south-america",
        "description": {"en": "A South American country with notable contributions to nuclear physics, medicine, and literature."}
    },
    {
        "id": "mx",
        "name": {"en": "Mexico", "es": "México", "pt": "México", "fr": "Mexique", "de": "Mexiko", "zh": "墨西哥", "hi": "मेक्सिको", "ar": "المكسيك", "id": "Meksiko", "ja": "メキシコ"},
        "region": "north-america",
        "description": {"en": "A North American country with a rich pre-Columbian heritage and growing scientific research infrastructure."}
    },
    {
        "id": "cl",
        "name": {"en": "Chile", "es": "Chile", "pt": "Chile", "fr": "Chili", "de": "Chile", "zh": "智利", "hi": "चिली", "ar": "تشيلي", "id": "Chili", "ja": "チリ"},
        "region": "south-america",
        "description": {"en": "A South American country known for its astronomical observatories and contributions to literature and science."}
    },
]

count = 0
for c in countries:
    path = os.path.join(BASE_DIR, f"{c['id']}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(c, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f"Created {c['id']}.json")
    count += 1

print(f"\nTotal: {count} files generated.")
