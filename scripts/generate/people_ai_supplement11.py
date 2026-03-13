#!/usr/bin/env python3
"""Supplement batch 11: more people with dedup."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
PEOPLE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'people')
existing = {f.replace('.json', '') for f in os.listdir(PEOPLE_DIR) if f.endswith('.json')} if os.path.exists(PEOPLE_DIR) else set()
def add(id, *a, **k):
    if id not in existing:
        P.append(person(id, *a, **k))

# ===== ASIAN HISTORICAL FIGURES =====

add("xuanzang", "Xuanzang", "玄奘", 602, 664, ["cn"], ["philosophy"],
  "Xuanzang was a Chinese Buddhist monk who undertook an epic seventeen-year journey to India to obtain sacred Buddhist texts.", "Born in Luoyang, Henan, he became a monk at age thirteen and grew dissatisfied with the incomplete Chinese Buddhist scriptures.", "His translations of Sanskrit texts transformed Chinese Buddhism, and his travel account inspired the classic novel Journey to the West.",
  [(629, "Departed Chang'an on his journey to India"), (645, "Returned to China with 657 Buddhist texts"), (648, "Completed Great Tang Records on the Western Regions")],
  [("Great Tang Records on the Western Regions", 646, "Detailed account of his travels through Central and South Asia")],
  [("If I do not reach India, I will not turn back to the east.", "Attributed during his journey")])

add("zheng-he", "Zheng He", "鄭和", 1371, 1433, ["cn"], ["engineering"],
  "Zheng He was a Chinese mariner and explorer who led seven massive naval expeditions across the Indian Ocean during the Ming Dynasty.", "Born Ma He in Yunnan province to a Muslim family, he was captured as a boy and served in the court of the Prince of Yan, later the Yongle Emperor.", "His voyages demonstrated China's naval supremacy and established diplomatic and trade relations across Southeast Asia, India, Arabia, and East Africa.",
  [(1405, "Led first treasure fleet voyage to Southeast Asia and India"), (1407, "Second voyage reached Calicut and Cochin"), (1431, "Led seventh and final voyage, reaching East Africa")],
  [("Charts of Zheng He's Voyages", 1430, "Navigation charts documenting sea routes across the Indian Ocean")],
  [("We have traversed more than 100,000 li of immense water spaces and have beheld in the ocean huge waves like mountains rising in the sky.", "Inscription at Changle, Fujian")])

add("li-shimin", "Li Shimin (Tang Taizong)", "李世民（唐太宗）", 598, 649, ["cn"], ["politics"],
  "Li Shimin, known as Emperor Taizong of Tang, is regarded as one of China's greatest emperors who established the golden age of the Tang Dynasty.", "Born into an aristocratic family in Wugong, Shaanxi, he was instrumental in helping his father Li Yuan overthrow the Sui Dynasty.", "His reign set the standard for good governance in Chinese history, establishing systems of law, education, and meritocratic civil service that endured for centuries.",
  [(618, "Helped father establish the Tang Dynasty"), (626, "Became Emperor Taizong after the Xuanwu Gate Incident"), (630, "Defeated the Eastern Turkic Khaganate")],
  [("Zhenguan Zhengyao", 649, "Records of governance compiled from his discussions with ministers")],
  [("By using a mirror of bronze, you may see to adjust your cap; by using antiquity as a mirror, you may learn to foresee the rise and fall of empires.", "Attributed")])

add("wu-zetian", "Wu Zetian", "武則天", 624, 705, ["cn"], ["politics"],
  "Wu Zetian was the only woman in Chinese history to assume the title of Empress Regnant, ruling China during the Tang Dynasty and founding the brief Zhou Dynasty.", "Born into a wealthy and noble family in Wenshui, Shanxi, she entered the imperial court as a concubine of Emperor Taizong at age fourteen.", "She expanded the Chinese empire, reformed the civil service examination system, and promoted Buddhism, governing effectively for over four decades.",
  [(655, "Became Empress Consort of Emperor Gaozong"), (690, "Proclaimed herself Empress Regnant, establishing the Zhou Dynasty"), (705, "Abdicated in favor of her son, restoring the Tang Dynasty")],
  [("Wordless Stele", 705, "Her famously blank memorial stele, leaving history to judge her reign")],
  [("Let the generations after me judge my merits and faults.", "Attributed, regarding her wordless stele")])

add("kangxi-emperor", "Kangxi Emperor", "康熙帝", 1654, 1722, ["cn"], ["politics"],
  "The Kangxi Emperor was the longest-reigning emperor of China and one of the most capable rulers of the Qing Dynasty.", "Born Xuanye, he ascended to the throne at age seven after his father's death from smallpox and took personal control of the government at fifteen.", "He consolidated Qing rule over China, expanded the empire's borders, patronized arts and sciences, and compiled the monumental Kangxi Dictionary.",
  [(1673, "Suppressed the Revolt of the Three Feudatories"), (1683, "Conquered Taiwan under Zheng family control"), (1689, "Signed the Treaty of Nerchinsk with Russia")],
  [("Kangxi Dictionary", 1716, "Comprehensive Chinese character dictionary with over 47,000 entries")],
  [("One act of negligence may lead to a thousand years of regret.", "Imperial maxims")])

add("qianlong-emperor", "Qianlong Emperor", "乾隆帝", 1711, 1799, ["cn"], ["politics"],
  "The Qianlong Emperor presided over the zenith of Qing Dynasty prosperity and territorial expansion during one of the longest reigns in Chinese history.", "Born Hongli, he was the favorite grandson of the Kangxi Emperor and was carefully groomed for rule from childhood.", "He expanded Chinese territory to its greatest extent, patronized a massive literary compilation project, but his later reign saw the beginning of dynastic decline.",
  [(1735, "Ascended to the throne"), (1755, "Conquered Dzungaria, completing the incorporation of Xinjiang"), (1795, "Abdicated in favor of his son after sixty years of rule")],
  [("Siku Quanshu", 1782, "The largest collection of books in Chinese history, comprising over 36,000 volumes")],
  [("I have been on the throne for sixty years. Although I cannot compare to my grandfather's reign of sixty-one years, I should not surpass him.", "On his abdication")])

add("oda-nobunaga", "Oda Nobunaga", "織田信長", 1534, 1582, ["jp"], ["politics"],
  "Oda Nobunaga was the first of the three great unifiers of Japan who began the process of ending the Sengoku period of civil war.", "Born in Owari Province to a minor daimyo family, he was known as the 'Fool of Owari' in his youth for his eccentric behavior.", "He revolutionized Japanese warfare with firearms, destroyed the political power of Buddhist monasteries, and laid the groundwork for Japan's unification.",
  [(1560, "Defeated Imagawa Yoshimoto at the Battle of Okehazama"), (1568, "Entered Kyoto and installed Ashikaga Yoshiaki as shogun"), (1575, "Employed mass firearms tactics at the Battle of Nagashino"), (1582, "Died during the Honnoji Incident, betrayed by Akechi Mitsuhide")],
  [("Tenka Fubu", 1567, "His seal and political slogan meaning 'All the land under one sword'")],
  [("If the cuckoo does not sing, kill it.", "Traditional Japanese saying attributed to Nobunaga")])

add("toyotomi-hideyoshi", "Toyotomi Hideyoshi", "豊臣秀吉", 1537, 1598, ["jp"], ["politics"],
  "Toyotomi Hideyoshi rose from peasant origins to become the second great unifier of Japan, completing the work Oda Nobunaga had begun.", "Born to a poor peasant family in Owari Province, he entered Nobunaga's service as a sandal-bearer and rose through merit to become a top general.", "He unified all of Japan, implemented the land survey and sword hunt that solidified the class system, and launched ambitious but ultimately failed invasions of Korea.",
  [(1582, "Avenged Nobunaga by defeating Akechi Mitsuhide at Yamazaki"), (1585, "Appointed Kampaku (regent) by the Emperor"), (1590, "Completed the unification of Japan by conquering the Hojo clan"), (1592, "Launched the first invasion of Korea")],
  [("Taiko Kenchi", 1582, "Nationwide land survey that standardized taxation across Japan")],
  [("If the cuckoo does not sing, coax it.", "Traditional Japanese saying attributed to Hideyoshi")])

add("miyamoto-musashi", "Miyamoto Musashi", "宮本武蔵", 1584, 1645, ["jp"], ["philosophy"],
  "Miyamoto Musashi was Japan's most legendary swordsman and the author of The Book of Five Rings, a classic treatise on strategy and martial arts.", "Born in Harima Province, he fought his first duel at age thirteen and went on to be undefeated in over sixty duels throughout his life.", "His philosophical writings on strategy transcended martial arts to influence business, sports, and leadership worldwide.",
  [(1600, "Fought at the Battle of Sekigahara"), (1612, "Defeated his greatest rival Sasaki Kojiro on Ganryu Island"), (1645, "Completed The Book of Five Rings shortly before his death")],
  [("The Book of Five Rings", 1645, "Classic treatise on strategy, tactics, and philosophy"), ("Dokkodo", 1645, "The Path of Aloneness, his final philosophical work of 21 precepts")],
  [("Do nothing that is of no use.", "The Book of Five Rings"), ("The ultimate aim of martial arts is not having to use them.", "Attributed")])

add("kukai", "Kukai", "空海", 774, 835, ["jp"], ["philosophy"],
  "Kukai was a Japanese Buddhist monk who founded the Shingon school of esoteric Buddhism and is one of Japan's most revered cultural figures.", "Born on the island of Shikoku, he was a prodigious scholar who studied in China under the esoteric master Huiguo.", "He established Shingon Buddhism, created the kana syllabary that democratized Japanese literacy, and founded the pilgrimage route of the 88 temples of Shikoku.",
  [(804, "Traveled to China to study esoteric Buddhism"), (816, "Founded the monastery on Mount Koya"), (835, "Entered eternal meditation on Mount Koya")],
  [("Sangoshiiki", 797, "Treatise comparing Confucianism, Taoism, and Buddhism"), ("Tenrei Bansho Meigi", 830, "Dictionary of Sanskrit-Chinese translations")],
  [("Be master of mind rather than mastered by mind.", "Attributed")])

add("shotoku-taishi", "Shotoku Taishi", "聖徳太子", 574, 622, ["jp"], ["politics"],
  "Prince Shotoku was a semi-legendary regent of Japan who promoted Buddhism and Chinese political institutions, shaping the foundations of Japanese civilization.", "Born as Prince Umayado, he served as regent for Empress Suiko and was renowned for his intelligence and piety.", "He established Buddhism as a state religion, introduced the Chinese calendar and court ranks, and authored Japan's first constitution.",
  [(593, "Became regent for Empress Suiko"), (604, "Promulgated the Seventeen-Article Constitution"), (607, "Sent envoys to Sui Dynasty China")],
  [("Seventeen-Article Constitution", 604, "Japan's first written code of governance emphasizing harmony and Buddhist values")],
  [("Harmony is to be valued, and an avoidance of wanton opposition to be honored.", "Seventeen-Article Constitution, Article 1")])

add("minamoto-no-yoritomo", "Minamoto no Yoritomo", "源頼朝", 1147, 1199, ["jp"], ["politics"],
  "Minamoto no Yoritomo founded the Kamakura Shogunate, establishing the first military government in Japanese history.", "Born into the prestigious Minamoto clan, he was exiled as a teenager after his father's defeat in the Heiji Rebellion.", "He created the shogunate system of military government that would define Japanese politics for nearly seven centuries.",
  [(1180, "Raised an army against the Taira clan, beginning the Genpei War"), (1185, "Defeated the Taira at the naval Battle of Dan-no-ura"), (1192, "Appointed Seii Taishogun, establishing the Kamakura Shogunate")],
  [("Azuma Kagami", 1266, "Chronicle of the Kamakura Shogunate compiled under his successors")],
  [("A warrior who has lost his honor is like a tree that has lost its roots.", "Attributed")])

add("tokugawa-yoshimune", "Tokugawa Yoshimune", "徳川吉宗", 1684, 1751, ["jp"], ["politics"],
  "Tokugawa Yoshimune was the eighth shogun of the Tokugawa dynasty, known as the 'Rice Shogun' for his sweeping economic and administrative reforms.", "Born the fourth son of the lord of Kii Province, he unexpectedly became shogun after the deaths of his predecessors without heirs.", "His Kyoho Reforms revitalized the shogunate's finances, promoted Dutch learning that opened Japan to Western science, and established fire brigades in Edo.",
  [(1716, "Became the eighth Tokugawa shogun"), (1720, "Relaxed the ban on importing Western books"), (1722, "Implemented the Kyoho Reforms to address fiscal crisis")],
  [("Kyoho Reforms", 1722, "Comprehensive set of economic and administrative reforms to stabilize shogunate finances")],
  [("Good governance begins with listening to the people.", "Attributed")])

add("uesugi-kenshin", "Uesugi Kenshin", "上杉謙信", 1530, 1578, ["jp"], ["politics"],
  "Uesugi Kenshin was a daimyo of Echigo Province renowned as the 'God of War' and the legendary rival of Takeda Shingen during Japan's Sengoku period.", "Born Nagao Kagetora, he took control of Echigo Province at a young age and was a devout follower of Bishamonten, the Buddhist god of war.", "He is celebrated as one of the most skilled military commanders in Japanese history, known for his honorable conduct in warfare.",
  [(1553, "First Battle of Kawanakajima against Takeda Shingen"), (1561, "Fourth Battle of Kawanakajima, the most famous engagement"), (1576, "Defeated Oda Nobunaga's forces at the Battle of Tedorigawa")],
  [("Military campaigns of Echigo", 1560, "Records of Uesugi military campaigns during the Sengoku period")],
  [("Those who cling to life die, and those who defy death live.", "Attributed")])

add("takeda-shingen", "Takeda Shingen", "武田信玄", 1521, 1573, ["jp"], ["politics"],
  "Takeda Shingen was a powerful daimyo of Kai Province, famous for his innovative cavalry tactics and his rivalry with Uesugi Kenshin.", "Born Takeda Harunobu, he overthrew his father to become lord of Kai and built one of the most formidable military forces of the Sengoku period.", "His military innovations, especially in cavalry tactics and the use of the Furinkazan banner, influenced Japanese warfare profoundly.",
  [(1541, "Became lord of Kai Province after deposing his father"), (1553, "Began the series of battles of Kawanakajima against Uesugi Kenshin"), (1572, "Defeated Tokugawa Ieyasu at the Battle of Mikatagahara")],
  [("Koyo Gunkan", 1616, "Military chronicle of the Takeda clan compiled after Shingen's time")],
  [("Swift as the wind, silent as a forest, fierce as fire, immovable as a mountain.", "Furinkazan banner, adapted from Sun Tzu")])

add("sen-no-rikyu", "Sen no Rikyu", "千利休", 1522, 1591, ["jp"], ["art"],
  "Sen no Rikyu was the most influential figure in the Japanese tea ceremony, perfecting the wabi-cha aesthetic of simplicity and rusticity.", "Born in Sakai to a wealthy merchant family, he studied tea under Takeno Joo and became tea master to both Oda Nobunaga and Toyotomi Hideyoshi.", "He transformed the tea ceremony into a profound artistic and philosophical practice that influenced Japanese aesthetics, architecture, and ceramics for centuries.",
  [(1579, "Became tea master to Oda Nobunaga"), (1585, "Performed a grand tea ceremony for Emperor Ogimachi"), (1591, "Ordered to commit ritual suicide by Toyotomi Hideyoshi")],
  [("Nanporoku", 1593, "Posthumous compilation of his tea teachings by his disciple Nanbo Sokei")],
  [("Though many people drink tea, if you do not know the Way of Tea, tea will drink you.", "Attributed"), ("In the small room, one finds infinity.", "Attributed")])

add("chikamatsu-monzaemon", "Chikamatsu Monzaemon", "近松門左衛門", 1653, 1725, ["jp"], ["literature"],
  "Chikamatsu Monzaemon is considered the greatest dramatist in Japanese literature, often called the 'Shakespeare of Japan' for his bunraku puppet plays and kabuki works.", "Born into a samurai family, he abandoned that life to pursue writing and became the principal playwright for the famous chanter Takemoto Gidayu.", "He elevated Japanese drama to a literary art form, pioneering the domestic tragedy genre that depicted the conflicts between duty and human emotion.",
  [(1683, "Wrote his first major kabuki play"), (1703, "Wrote The Love Suicides at Sonezaki, pioneering the domestic tragedy genre"), (1715, "Wrote The Battles of Coxinga, his most popular history play")],
  [("The Love Suicides at Sonezaki", 1703, "Groundbreaking domestic tragedy about forbidden love"), ("The Battles of Coxinga", 1715, "Epic history play about Zheng Chenggong's exploits")],
  [("Art is something that lies in the slender margin between the real and the unreal.", "Naniwa Miyage")])

add("ihara-saikaku", "Ihara Saikaku", "井原西鶴", 1642, 1693, ["jp"], ["literature"],
  "Ihara Saikaku was a pioneering Japanese novelist and poet who created the ukiyo-zoshi genre of realistic fiction depicting the lives of townspeople.", "Born in Osaka to a merchant family, he first gained fame as a haikai poet before turning to prose fiction.", "He established the novel as a major literary form in Japan, influencing all subsequent Japanese prose with his vivid depictions of urban life, love, and commerce.",
  [(1682, "Published The Life of an Amorous Man, launching the ukiyo-zoshi genre"), (1686, "Published Five Women Who Loved Love"), (1688, "Published The Japanese Family Storehouse, depicting merchant life")],
  [("The Life of an Amorous Man", 1682, "Picaresque novel following a man's romantic adventures"), ("The Japanese Family Storehouse", 1688, "Collection of stories about merchants gaining and losing wealth")],
  [("There is always something to be gained from every experience, whether good or bad.", "Attributed")])

add("yosa-buson", "Yosa Buson", "与謝蕪村", 1716, 1784, ["jp"], ["literature", "art"],
  "Yosa Buson was a major Japanese poet and painter who revived the haiku tradition and is considered one of the four great haiku masters alongside Basho, Issa, and Shiki.", "Born near Osaka, he moved to Edo as a young man and studied haiku in the tradition of Matsuo Basho while also training as a painter.", "He unified poetry and painting in a way that profoundly influenced Japanese aesthetics, and his vivid, painterly haiku remain widely admired.",
  [(1751, "Began establishing himself as a haiku master in Kyoto"), (1771, "Became head of the Yahantei poetry school"), (1776, "Published his influential haiku collection")],
  [("Shin Hanatsumi", 1797, "Posthumous collection of his haiku"), ("Oku no Hosomichi Emaki", 1778, "Illustrated scroll based on Basho's Narrow Road")],
  [("The old pond / A frog jumps in / The sound of water — I too write in Basho's shadow.", "Attributed")])

add("kobayashi-issa", "Kobayashi Issa", "小林一茶", 1763, 1828, ["jp"], ["literature"],
  "Kobayashi Issa was one of Japan's four great haiku masters, beloved for his compassionate, humorous, and deeply human poetry.", "Born into a farming family in Shinano Province, he endured a difficult childhood after his mother's death and his stepmother's cruelty, eventually leaving home to study haiku in Edo.", "His poetry, marked by empathy for small creatures and the downtrodden, democratized haiku by bringing warmth and accessibility to the form.",
  [(1792, "Began his wandering years, traveling and composing haiku"), (1813, "Returned to his hometown after inheriting his father's property"), (1819, "Published Oraga Haru, his masterwork")],
  [("Oraga Haru", 1819, "Autobiographical haiku collection blending poetry, prose, and personal reflection")],
  [("O snail, climb Mount Fuji, but slowly, slowly!", "Oraga Haru"), ("In this world of ours, even the flies and mosquitoes seem lonely.", "Attributed")])

# ===== AFRICAN & MIDDLE EASTERN FIGURES =====

add("sundiata-keita", "Sundiata Keita", "スンジャタ・ケイタ", 1217, 1255, ["ml"], ["politics"],
  "Sundiata Keita was the founder of the Mali Empire and is celebrated as one of the greatest heroes of West African history.", "Born a prince of the Mandinka people, he was crippled as a child and exiled, but overcame his disability to reclaim his kingdom.", "He established the Mali Empire and promulgated the Kouroukan Fouga, one of the earliest known constitutions, laying foundations for centuries of West African prosperity.",
  [(1235, "Defeated Sumanguru Kante at the Battle of Kirina"), (1240, "Established the Mali Empire with Niani as its capital")],
  [("Kouroukan Fouga", 1236, "Charter of the Mandinka people establishing governance principles and human rights")],
  [("I am the heir of my ancestors. I have come to restore the dignity of my people.", "Oral tradition")])

add("menelik-ii", "Menelik II", "メネリク2世", 1844, 1913, ["et"], ["politics"],
  "Menelik II was Emperor of Ethiopia who preserved his nation's independence by defeating Italy at the Battle of Adwa, one of the most significant African victories against European colonialism.", "Born Sahle Maryam in Ankober, Shewa, he was captured as a youth by Emperor Tewodros II but eventually escaped and became King of Shewa.", "His victory at Adwa ensured Ethiopia remained the only African nation never colonized and inspired anti-colonial movements across Africa and the diaspora.",
  [(1889, "Became Emperor of Ethiopia and signed the Treaty of Wuchale"), (1896, "Defeated Italy at the Battle of Adwa"), (1897, "Established Addis Ababa as the permanent capital")],
  [("Treaty of Wuchale", 1889, "Treaty with Italy whose disputed interpretation led to the First Italo-Ethiopian War")],
  [("Ethiopia stretches her hands unto God.", "Psalm 68:31, frequently invoked by Menelik")])

add("samori-ture", "Samori Ture", "サモリ・トゥーレ", 1830, 1900, ["gn"], ["politics"],
  "Samori Ture was the founder of the Wassoulou Empire in West Africa and one of the most effective African leaders in resisting French colonial expansion.", "Born in present-day Guinea to a Dyula trading family, he built a powerful state through military skill and diplomatic acumen.", "He resisted French colonialism for nearly two decades with innovative military tactics, becoming a symbol of African resistance.",
  [(1878, "Established the Wassoulou Empire"), (1882, "Began resistance against French colonial forces"), (1898, "Captured by the French and exiled to Gabon")],
  [("Wassoulou Empire Constitution", 1878, "Administrative system organizing his empire into provinces")],
  [("I will never submit to the French. My people shall remain free.", "Attributed")])

add("yaa-asantewaa", "Yaa Asantewaa", "ヤア・アサンテワア", 1840, 1921, ["gh"], ["politics"],
  "Yaa Asantewaa was the Queen Mother of Ejisu in the Ashanti Empire who led the final major war against British colonialism in Ghana.", "Born into the Ashanti royal family, she became Queen Mother of Ejisu and was known for her strong will and political influence.", "Her rebellion, the War of the Golden Stool, became a powerful symbol of African resistance to colonialism and of women's leadership.",
  [(1896, "Became Queen Mother of Ejisu after the British exiled King Prempeh I"), (1900, "Led the War of the Golden Stool against the British")],
  [("War of the Golden Stool", 1900, "The uprising she led against British attempts to seize the Ashanti Golden Stool")],
  [("If you, the men of Ashanti, will not go forward, then we will. I shall call upon my fellow women.", "Speech rallying the Ashanti chiefs")])

add("cetshwayo", "Cetshwayo kaMpande", "セチュワヨ・カムパンデ", 1826, 1884, ["za"], ["politics"],
  "Cetshwayo was the last great king of the independent Zulu Kingdom who inflicted a devastating defeat on the British at the Battle of Isandlwana.", "Born a prince of the Zulu royal house, he fought and won a civil war against his brother to secure the throne.", "His victory at Isandlwana was the worst defeat suffered by the British against indigenous forces and demonstrated the effectiveness of Zulu military organization.",
  [(1873, "Crowned King of the Zulu Nation"), (1879, "Zulu forces defeated the British at the Battle of Isandlwana"), (1879, "Defeated and captured after the Battle of Ulundi")],
  [("Zulu Military Reforms", 1873, "Reorganization of the Zulu military system inherited from Shaka")],
  [("I have done nothing wrong. I have committed no fault against the British.", "Statement during his exile")])

add("moshoeshoe-i", "Moshoeshoe I", "モショエショエ1世", 1786, 1870, ["ls"], ["politics"],
  "Moshoeshoe I was the founder and first king of Basotho nation (modern Lesotho), renowned for his diplomatic skill in preserving his people's independence.", "Born Lepoqo in the Drakensberg Mountains, he gathered displaced peoples during the upheavals of the Mfecane into a unified nation.", "He skillfully used diplomacy to protect his people from both Zulu expansion and Boer encroachment, establishing Lesotho as an enduring nation.",
  [(1822, "Founded the Basotho nation at Thaba Bosiu"), (1831, "Repelled Ndebele attacks at Thaba Bosiu"), (1868, "Secured British protection against Boer expansion")],
  [("Diplomatic correspondence with Cape Colony", 1843, "Letters establishing diplomatic relations with the British")],
  [("Peace is like rain. It waters the land and makes it fertile.", "Attributed")])

add("nzinga-of-ndongo", "Nzinga of Ndongo", "ンジンガ女王", 1583, 1663, ["ao"], ["politics"],
  "Queen Nzinga was a fearless ruler of the Ndongo and Matamba kingdoms in present-day Angola who fiercely resisted Portuguese colonialism.", "Born a princess of the Ndongo kingdom, she served as a diplomat for her brother before seizing power and becoming queen.", "She fought the Portuguese for over three decades, forming alliances with the Dutch and neighboring kingdoms, and became an enduring symbol of African resistance.",
  [(1624, "Became Queen of Ndongo"), (1626, "Conquered the Kingdom of Matamba"), (1657, "Negotiated a peace treaty with the Portuguese")],
  [("Treaty with Portugal", 1657, "Peace agreement ending decades of conflict with the Portuguese")],
  [("I am the Queen of Matamba and Ndongo, and I bow to no foreign power.", "Attributed")])

add("amina-of-zaria", "Amina of Zaria", "アミナ・オブ・ザリア", 1533, 1610, ["ng"], ["politics"],
  "Queen Amina was a warrior queen of the Hausa city-state of Zazzau (Zaria) in present-day Nigeria, celebrated for her military conquests and fortification-building.", "Born a princess of Zazzau, she trained in warfare from childhood and proved herself a formidable warrior before ascending to power.", "She expanded Zazzau's territory to its greatest extent and built the famous Amina walls, earthen fortifications that still partially stand today.",
  [(1576, "Became Queen of Zazzau"), (1580, "Expanded Zazzau territory through military campaigns southward")],
  [("Amina Walls", 1580, "System of defensive earthen walls built around conquered cities")],
  [("A woman is never too old to fight for her people.", "Oral tradition")])

add("ahmad-shah-durrani", "Ahmad Shah Durrani", "アフマド・シャー・ドゥッラーニー", 1722, 1772, ["af"], ["politics"],
  "Ahmad Shah Durrani was the founder of the Durrani Empire and is considered the father of modern Afghanistan.", "Born in Multan to an Afghan chief of the Abdali tribe, he served as a cavalry commander under Nader Shah of Persia.", "He united the Pashtun tribes into a single polity that became the foundation of the modern Afghan state and built one of the largest empires of the 18th century.",
  [(1747, "Founded the Durrani Empire after the assassination of Nader Shah"), (1757, "Captured Delhi and Lahore"), (1761, "Defeated the Marathas at the Third Battle of Panipat")],
  [("Durrani Empire Administration", 1747, "Administrative system organizing tribal confederacy into a centralized state")],
  [("By the sword we gained our kingdom, by justice we shall keep it.", "Attributed")])

add("gamal-abdel-nasser", "Gamal Abdel Nasser", "ガマール・アブドゥル＝ナーセル", 1918, 1970, ["eg"], ["politics"],
  "Gamal Abdel Nasser was the second President of Egypt and the leading figure of Arab nationalism who transformed Egypt and inspired anti-colonial movements across the Middle East.", "Born in Alexandria, he became an army officer and led the Free Officers Movement that overthrew King Farouk in 1952.", "He nationalized the Suez Canal, championed pan-Arabism, and implemented land reforms that fundamentally reshaped Egyptian society.",
  [(1952, "Led the Egyptian Revolution overthrowing King Farouk"), (1956, "Nationalized the Suez Canal, provoking the Suez Crisis"), (1958, "Formed the United Arab Republic with Syria")],
  [("The Philosophy of the Revolution", 1955, "Political manifesto outlining his vision for Egypt and the Arab world")],
  [("We shall not repeat the past. We shall liquidate it.", "Speech on nationalization of the Suez Canal")])

add("anwar-sadat", "Anwar Sadat", "アンワル・サダト", 1918, 1981, ["eg"], ["politics"],
  "Anwar Sadat was the President of Egypt who made the historic peace with Israel, winning the Nobel Peace Prize and fundamentally altering Middle Eastern politics.", "Born in Mit Abu al-Kum, he was a career military officer who participated in the 1952 revolution and served as Nasser's vice president.", "His visit to Jerusalem and the Camp David Accords broke the cycle of Arab-Israeli wars and established the framework for Middle Eastern peace negotiations.",
  [(1970, "Became President of Egypt after Nasser's death"), (1973, "Launched the October War against Israel"), (1977, "Made historic visit to Jerusalem"), (1978, "Signed the Camp David Accords with Israel")],
  [("In Search of Identity", 1978, "Autobiography detailing his life and political philosophy")],
  [("Peace is much more precious than a piece of land.", "Speech to the Israeli Knesset, 1977")])

add("king-faisal-i", "Faisal I of Iraq", "ファイサル1世", 1885, 1933, ["iq"], ["politics"],
  "Faisal I was the first King of Iraq who played a key role in the Arab Revolt against the Ottoman Empire and helped establish the modern state of Iraq.", "Born in Mecca as a son of Sharif Hussein, he was educated in Istanbul and became a leader of the Arab nationalist movement.", "He led the Arab forces in the revolt against the Ottomans and, as king, worked to build a unified Iraqi nation from diverse ethnic and religious groups.",
  [(1916, "Led Arab forces in the Great Arab Revolt against the Ottomans"), (1920, "Briefly proclaimed King of Syria before being expelled by the French"), (1921, "Crowned King of Iraq under the British Mandate")],
  [("Correspondence with T.E. Lawrence", 1916, "Wartime communications coordinating the Arab Revolt")],
  [("We are one people with one heart, and we have one aim: the freedom of the Arab nation.", "Attributed")])

add("reza-shah-pahlavi", "Reza Shah Pahlavi", "レザー・シャー・パフラヴィー", 1878, 1944, ["ir"], ["politics"],
  "Reza Shah Pahlavi was the founder of the Pahlavi dynasty who transformed Iran from a feudal state into a modern centralized nation.", "Born Reza Khan in Mazandaran Province, he rose through the military ranks of the Persian Cossack Brigade to become the most powerful man in Iran.", "He modernized Iran's infrastructure, education, and legal system, banned the veil, and established Iran's first university and railroad.",
  [(1921, "Led a coup d'etat that overthrew the Qajar government"), (1925, "Became Shah of Iran, founding the Pahlavi dynasty"), (1935, "Officially changed the country's name from Persia to Iran"), (1941, "Abdicated under Anglo-Soviet pressure during World War II")],
  [("Modernization Reforms", 1928, "Series of reforms including the Uniform Dress Law and establishment of Tehran University")],
  [("Iran must move forward. We cannot remain in the past while the world advances.", "Attributed")])

add("mohammad-mosaddegh", "Mohammad Mosaddegh", "モハンマド・モサッデグ", 1882, 1967, ["ir"], ["politics"],
  "Mohammad Mosaddegh was the democratically elected Prime Minister of Iran who nationalized the country's oil industry, challenging British imperial interests.", "Born into a prominent aristocratic family, he was educated in Europe and became a leading figure in the Iranian constitutional movement.", "His nationalization of Iranian oil inspired resource nationalism worldwide, and his overthrow in a CIA-MI6 coup became a defining event in Iranian and Middle Eastern politics.",
  [(1951, "Became Prime Minister and nationalized the Anglo-Iranian Oil Company"), (1952, "Named TIME magazine's Person of the Year"), (1953, "Overthrown in a CIA and MI6-backed coup")],
  [("Oil Nationalization Act", 1951, "Legislation nationalizing Iran's oil industry from British control")],
  [("I am fighting against imperialism and for the sovereignty of my country.", "Statement during the oil crisis")])

# ===== LATIN AMERICAN FIGURES =====

add("sor-juana-ines-de-la-cruz", "Sor Juana Ines de la Cruz", "ソル・フアナ・イネス・デ・ラ・クルス", 1648, 1695, ["mx"], ["literature"],
  "Sor Juana Ines de la Cruz was a Mexican nun, scholar, and poet considered the greatest literary figure of colonial Latin America.", "Born an illegitimate child in San Miguel Nepantla, she was a prodigy who learned to read at age three and entered a convent to pursue her intellectual life.", "She championed women's right to education centuries before the feminist movement and produced poetry and philosophical works of enduring brilliance.",
  [(1669, "Entered the Convent of San Jeronimo in Mexico City"), (1689, "Published Inundacion Castalida, her first collected works"), (1691, "Wrote Respuesta a Sor Filotea, her famous defense of women's education")],
  [("Respuesta a Sor Filotea", 1691, "Landmark defense of women's intellectual rights"), ("Primero Sueno", 1692, "Epic philosophical poem exploring the quest for knowledge")],
  [("One can perfectly well philosophize while cooking supper.", "Respuesta a Sor Filotea")])

add("jose-de-san-martin", "Jose de San Martin", "ホセ・デ・サン・マルティン", 1778, 1850, ["ar"], ["politics"],
  "Jose de San Martin was an Argentine general who led the liberation of Argentina, Chile, and Peru from Spanish rule, earning the title 'Liberator of the South.'", "Born in Yapeyu in the Viceroyalty of the Rio de la Plata, he was trained as a military officer in Spain before returning to South America to fight for independence.", "He is venerated as the national hero of Argentina, Chile, and Peru for his role in their independence from Spain.",
  [(1812, "Returned to Argentina to join the independence movement"), (1817, "Led his army across the Andes to liberate Chile"), (1821, "Declared the independence of Peru")],
  [("Maximas para Remedios", 1825, "Moral maxims written for his daughter")],
  [("You shall be what you must be, or else you shall be nothing.", "Letter to his daughter")])

add("bernardo-ohiggins", "Bernardo O'Higgins", "ベルナルド・オイギンス", 1778, 1842, ["cl"], ["politics"],
  "Bernardo O'Higgins was the Chilean independence leader and first Supreme Director of Chile, known as the 'Father of the Nation.'", "Born the illegitimate son of the Irish-born Spanish colonial governor Ambrosio O'Higgins, he was educated in England where he was influenced by Francisco de Miranda's independence ideas.", "He led Chile to independence from Spain and established the foundations of the Chilean state, including its first constitution and navy.",
  [(1814, "Led Chilean forces at the disastrous Battle of Rancagua"), (1817, "Returned with San Martin to defeat the Spanish at the Battle of Chacabuco"), (1818, "Proclaimed Chilean independence and became Supreme Director")],
  [("Chilean Declaration of Independence", 1818, "Document formally declaring Chile's independence from Spain")],
  [("Live with honor, or die with glory. The coward does neither.", "Attributed")])

add("dom-pedro-i", "Dom Pedro I", "ドン・ペドロ1世", 1798, 1834, ["br"], ["politics"],
  "Dom Pedro I was the founder and first Emperor of Brazil who declared the country's independence from Portugal in 1822.", "Born in Lisbon as the son of King Joao VI of Portugal, he came to Brazil as a child when the royal family fled Napoleon's invasion.", "He declared Brazilian independence with the famous 'Cry of Ipiranga' and established Brazil as an independent constitutional monarchy.",
  [(1822, "Declared Brazilian independence with the Cry of Ipiranga"), (1824, "Promulgated Brazil's first constitution"), (1831, "Abdicated in favor of his young son Pedro II")],
  [("Brazilian Constitution of 1824", 1824, "Brazil's first constitution establishing a constitutional monarchy")],
  [("Independence or death!", "The Cry of Ipiranga, September 7, 1822")])

add("getulio-vargas", "Getulio Vargas", "ジェトゥリオ・ヴァルガス", 1882, 1954, ["br"], ["politics"],
  "Getulio Vargas was the longest-serving President of Brazil who modernized the country's economy and labor system during the Estado Novo era.", "Born in Sao Borja, Rio Grande do Sul, he was a lawyer and politician who rose to power through the Revolution of 1930.", "He transformed Brazil from an agrarian oligarchy into an urban industrial power, established labor rights and social security, and remains one of the most consequential figures in Brazilian history.",
  [(1930, "Came to power through the Revolution of 1930"), (1937, "Established the authoritarian Estado Novo regime"), (1943, "Enacted the Consolidation of Labor Laws"), (1954, "Committed suicide while serving as elected president")],
  [("Consolidation of Labor Laws", 1943, "Comprehensive labor code establishing workers' rights in Brazil")],
  [("I leave life to enter history.", "Suicide note, 1954")])

add("juan-peron", "Juan Peron", "フアン・ペロン", 1895, 1974, ["ar"], ["politics"],
  "Juan Peron was a three-time President of Argentina whose populist movement, Peronism, fundamentally reshaped Argentine politics and society.", "Born in Lobos, Buenos Aires Province, he was a career military officer who gained political influence as Secretary of Labor.", "Peronism became the most enduring political movement in Argentine history, combining labor rights, economic nationalism, and social welfare programs.",
  [(1946, "Elected President of Argentina for the first time"), (1949, "Enacted a new constitution expanding social rights"), (1955, "Overthrown by military coup and went into exile"), (1973, "Returned from exile and elected president for the third time")],
  [("The Twenty Truths of Justicialism", 1950, "Foundational principles of the Peronist movement")],
  [("The year 2000 will find us either united or dominated.", "Political speech")])

add("eva-peron", "Eva Peron", "エバ・ペロン", 1919, 1952, ["ar"], ["politics"],
  "Eva Peron, known as Evita, was the First Lady of Argentina and a powerful political figure who championed workers' rights and women's suffrage.", "Born into poverty in Los Toldos, she moved to Buenos Aires as a teenager to pursue an acting career and married Juan Peron in 1945.", "She became the most powerful woman in Latin American history, establishing the Eva Peron Foundation for social welfare and securing women's suffrage in Argentina.",
  [(1947, "Embarked on the Rainbow Tour of Europe"), (1947, "Championed women's suffrage, enacted in Argentina"), (1948, "Founded the Eva Peron Foundation for social aid")],
  [("My Mission in Life", 1951, "Autobiography detailing her political beliefs and social vision")],
  [("I will return and I will be millions.", "Attributed, widely quoted")])

add("jose-vasconcelos", "Jose Vasconcelos", "ホセ・バスコンセロス", 1882, 1959, ["mx"], ["philosophy"],
  "Jose Vasconcelos was a Mexican philosopher, educator, and politician who served as Mexico's Secretary of Education and championed a vision of mestizo cultural identity.", "Born in Oaxaca, he was educated in law and philosophy and became deeply involved in the Mexican Revolution.", "He transformed Mexican education by establishing rural schools and libraries nationwide, and his concept of 'La Raza Cosmica' profoundly influenced Latin American identity.",
  [(1920, "Appointed Secretary of Public Education by President Obregon"), (1925, "Published La Raza Cosmica"), (1929, "Ran for president of Mexico")],
  [("La Raza Cosmica", 1925, "Philosophical essay proposing that the mixing of races in Latin America would create a superior 'cosmic race'")],
  [("I am Mexican not by birth, but by conviction.", "Attributed")])

add("augusto-sandino", "Augusto Cesar Sandino", "アウグスト・セサル・サンディーノ", 1895, 1934, ["ni"], ["politics"],
  "Augusto Cesar Sandino was a Nicaraguan revolutionary who led a guerrilla war against the United States occupation of Nicaragua.", "Born in Niquinohomo to a landowner father and indigenous mother, he worked in mines and on plantations across Central America before returning to fight for Nicaraguan sovereignty.", "His guerrilla campaign forced the withdrawal of U.S. Marines from Nicaragua and his legacy inspired the later Sandinista movement.",
  [(1927, "Began guerrilla war against U.S. Marines in Nicaragua"), (1933, "U.S. Marines withdrew from Nicaragua"), (1934, "Assassinated by National Guard under Anastasio Somoza")],
  [("Political Manifesto", 1927, "Declaration of principles for Nicaraguan sovereignty and Latin American unity")],
  [("Free homeland or death.", "Political slogan")])

add("emiliano-zapata", "Emiliano Zapata", "エミリアーノ・サパタ", 1879, 1919, ["mx"], ["politics"],
  "Emiliano Zapata was a leading figure in the Mexican Revolution who championed agrarian reform and the rights of Mexico's indigenous peasants.", "Born in Anenecuilco, Morelos, to a peasant family, he became a local leader fighting for the return of communal lands stolen by hacienda owners.", "His cry of 'Tierra y Libertad' (Land and Liberty) and the Plan de Ayala became foundational to Mexican agrarian reform and indigenous rights movements.",
  [(1911, "Joined the Revolution against Porfirio Diaz"), (1911, "Proclaimed the Plan de Ayala demanding agrarian reform"), (1919, "Assassinated in an ambush at Chinameca")],
  [("Plan de Ayala", 1911, "Revolutionary manifesto demanding redistribution of land to peasants")],
  [("It is better to die on your feet than to live on your knees.", "Attributed"), ("The land belongs to those who work it.", "Political slogan")])

# ===== EUROPEAN ENLIGHTENMENT/MODERN THINKERS =====

add("denis-diderot", "Denis Diderot", "ドゥニ・ディドロ", 1713, 1784, ["fr"], ["philosophy"],
  "Denis Diderot was a French Enlightenment philosopher and chief editor of the Encyclopedie, one of the most ambitious intellectual projects in history.", "Born in Langres to a master cutler, he was educated by the Jesuits and spent years as a struggling writer in Paris before embarking on the Encyclopedie.", "The Encyclopedie he co-edited became the defining work of the Enlightenment, democratizing knowledge and challenging religious and political authority.",
  [(1746, "Began work on the Encyclopedie"), (1751, "Published the first volume of the Encyclopedie"), (1773, "Visited Catherine the Great in Russia")],
  [("Encyclopedie", 1772, "Massive reference work of 28 volumes aiming to collect all human knowledge"), ("Jacques the Fatalist", 1796, "Philosophical novel questioning free will and determinism")],
  [("There is only one step from fanaticism to barbarism.", "Essai sur le merite et la vertu")])

add("jean-le-rond-dalembert", "Jean le Rond d'Alembert", "ジャン・ル・ロン・ダランベール", 1717, 1783, ["fr"], ["mathematics", "philosophy"],
  "Jean le Rond d'Alembert was a French mathematician and philosopher who co-edited the Encyclopedie and made foundational contributions to mathematical physics.", "Abandoned as an infant on the steps of the Saint-Jean-le-Rond church in Paris, he was raised by a foster mother and educated himself into the leading mathematician of his age.", "His d'Alembert principle in mechanics and his co-editorship of the Encyclopedie made him central to both the Scientific Revolution and the Enlightenment.",
  [(1743, "Published Traite de dynamique, introducing d'Alembert's principle"), (1751, "Wrote the Preliminary Discourse to the Encyclopedie"), (1754, "Elected to the French Academy")],
  [("Traite de dynamique", 1743, "Treatise establishing d'Alembert's principle in classical mechanics"), ("Preliminary Discourse to the Encyclopedie", 1751, "Influential essay mapping the history and classification of human knowledge")],
  [("Nothing is more indisputable than the existence of our sensations.", "Preliminary Discourse to the Encyclopedie")])

add("marquis-de-condorcet", "Marquis de Condorcet", "コンドルセ侯爵", 1743, 1794, ["fr"], ["mathematics", "philosophy"],
  "The Marquis de Condorcet was a French mathematician and political philosopher who championed reason, human rights, and the idea of human progress.", "Born into an aristocratic family in Ribemont, he became a renowned mathematician before turning to social and political philosophy.", "He pioneered social mathematics, advocated for women's rights and the abolition of slavery, and articulated the Enlightenment idea of inevitable human progress.",
  [(1785, "Published Essai sur l'application de l'analyse, introducing the Condorcet method"), (1791, "Proposed a plan for public education to the French National Assembly"), (1794, "Died in prison during the Terror after being arrested")],
  [("Sketch for a Historical Picture of the Progress of the Human Mind", 1795, "Posthumous work outlining a theory of inevitable human progress through reason")],
  [("The perfection of the human race is indefinite.", "Sketch for a Historical Picture")])

add("cesare-beccaria", "Cesare Beccaria", "チェーザレ・ベッカリーア", 1738, 1794, ["it"], ["philosophy"],
  "Cesare Beccaria was an Italian Enlightenment thinker whose work On Crimes and Punishments laid the foundation for modern criminal justice reform.", "Born into a Milanese aristocratic family, he was educated by Jesuits and influenced by the French philosophes, especially Montesquieu and Helvetius.", "His arguments against torture and capital punishment and for proportional sentencing influenced criminal law reform worldwide, including the United States Constitution.",
  [(1764, "Published On Crimes and Punishments"), (1768, "Appointed to a chair of law and economics in Milan")],
  [("On Crimes and Punishments", 1764, "Groundbreaking treatise arguing for criminal justice reform, proportional punishment, and abolition of torture")],
  [("It is better to prevent crimes than to punish them.", "On Crimes and Punishments")])

add("jeremy-bentham", "Jeremy Bentham", "ジェレミー・ベンサム", 1748, 1832, ["gb"], ["philosophy"],
  "Jeremy Bentham was an English philosopher and jurist who founded utilitarianism, the ethical theory that actions should maximize the greatest happiness for the greatest number.", "Born in London to a wealthy family, he was a child prodigy who attended Oxford at age twelve and trained as a lawyer but never practiced.", "His utilitarian philosophy reshaped law, economics, and public policy, and his ideas on individual liberty, animal rights, and prison reform were centuries ahead of their time.",
  [(1776, "Published A Fragment on Government, critiquing Blackstone"), (1789, "Published An Introduction to the Principles of Morals and Legislation"), (1791, "Designed the Panopticon, an innovative prison concept")],
  [("An Introduction to the Principles of Morals and Legislation", 1789, "Foundational text of utilitarian philosophy")],
  [("The greatest happiness of the greatest number is the foundation of morals and legislation.", "An Introduction to the Principles of Morals and Legislation"), ("The question is not, Can they reason?, nor Can they talk?, but, Can they suffer?", "On animal rights")])

add("herbert-spencer", "Herbert Spencer", "ハーバート・スペンサー", 1820, 1903, ["gb"], ["philosophy"],
  "Herbert Spencer was an English philosopher and sociologist who developed an all-encompassing evolutionary philosophy and coined the phrase 'survival of the fittest.'", "Born in Derby, he was largely self-educated and worked as a railway engineer and journalist before devoting himself to philosophy.", "His synthetic philosophy attempted to unify all knowledge under evolutionary principles and profoundly influenced sociology, though his social Darwinism remains controversial.",
  [(1851, "Published Social Statics"), (1857, "Coined the term 'survival of the fittest' in Principles of Biology"), (1862, "Published First Principles, beginning his Synthetic Philosophy series")],
  [("First Principles", 1862, "Foundation of his Synthetic Philosophy applying evolution to all domains"), ("The Principles of Sociology", 1876, "Systematic treatment of sociology as a science")],
  [("The great aim of education is not knowledge but action.", "Education: Intellectual, Moral, and Physical")])

add("auguste-comte", "Auguste Comte", "オーギュスト・コント", 1798, 1857, ["fr"], ["philosophy"],
  "Auguste Comte was a French philosopher who founded positivism and sociology, establishing the scientific study of society as an academic discipline.", "Born in Montpellier, he studied at the Ecole Polytechnique and became secretary to Henri de Saint-Simon before developing his own philosophical system.", "He established sociology as a distinct discipline and his positivist philosophy, emphasizing empirical observation over metaphysical speculation, profoundly shaped modern science.",
  [(1830, "Began publishing the Course of Positive Philosophy"), (1838, "Coined the term 'sociology'"), (1842, "Completed the six-volume Course of Positive Philosophy")],
  [("Course of Positive Philosophy", 1842, "Six-volume work establishing positivism and the hierarchy of sciences"), ("System of Positive Polity", 1854, "Work on the application of positivism to society")],
  [("Know yourself to improve yourself.", "Course of Positive Philosophy")])

add("alexis-de-tocqueville", "Alexis de Tocqueville", "アレクシ・ド・トクヴィル", 1805, 1859, ["fr"], ["philosophy", "politics"],
  "Alexis de Tocqueville was a French political thinker and historian whose Democracy in America remains the most penetrating analysis of American democratic society ever written.", "Born into a Norman aristocratic family, he traveled to America in 1831 ostensibly to study the prison system but used the trip to examine American democracy broadly.", "His insights on democracy, equality, civic association, and the tyranny of the majority remain essential to political science and democratic theory worldwide.",
  [(1831, "Traveled to the United States to study democracy"), (1835, "Published the first volume of Democracy in America"), (1856, "Published The Old Regime and the Revolution")],
  [("Democracy in America", 1840, "Two-volume masterwork analyzing American democratic institutions and society"), ("The Old Regime and the Revolution", 1856, "Analysis of the French Revolution's origins in the ancien regime")],
  [("In a democracy, the people get the government they deserve.", "Democracy in America"), ("The American Republic will endure until the day Congress discovers that it can bribe the public with the public's money.", "Attributed")])

add("max-weber", "Max Weber", "マックス・ヴェーバー", 1864, 1920, ["de"], ["philosophy"],
  "Max Weber was a German sociologist and political economist whose ideas on bureaucracy, authority, and the Protestant ethic profoundly shaped modern social science.", "Born in Erfurt to a wealthy and politically active family, he studied law and history and became a professor before suffering a severe mental breakdown.", "His concept of the 'iron cage' of bureaucracy, ideal types methodology, and analysis of the relationship between religion and capitalism became foundational to sociology.",
  [(1895, "Appointed professor of economics at the University of Freiburg"), (1905, "Published The Protestant Ethic and the Spirit of Capitalism"), (1919, "Delivered the lectures 'Science as a Vocation' and 'Politics as a Vocation'")],
  [("The Protestant Ethic and the Spirit of Capitalism", 1905, "Seminal work linking Protestant religious values to the development of capitalism"), ("Economy and Society", 1922, "Posthumous magnum opus on sociology of religion, law, and authority")],
  [("Politics is a strong and slow boring of hard boards.", "Politics as a Vocation")])

add("emile-durkheim", "Emile Durkheim", "エミール・デュルケーム", 1858, 1917, ["fr"], ["philosophy"],
  "Emile Durkheim was a French sociologist who established sociology as a formal academic discipline and developed the concept of social facts.", "Born in Epinal to a family of rabbis, he broke with tradition to pursue secular academic study at the Ecole Normale Superieure.", "He established the first European department of sociology, and his studies of suicide, religion, and the division of labor became foundational texts in social science.",
  [(1893, "Published The Division of Labour in Society"), (1895, "Published The Rules of Sociological Method"), (1897, "Published Suicide, pioneering sociological analysis of individual behavior")],
  [("Suicide", 1897, "Groundbreaking study demonstrating that suicide rates are influenced by social factors"), ("The Elementary Forms of the Religious Life", 1912, "Analysis of religion as a fundamentally social phenomenon")],
  [("Social facts must be studied as things, that is, as realities external to the individual.", "The Rules of Sociological Method")])

add("georg-simmel", "Georg Simmel", "ゲオルク・ジンメル", 1858, 1918, ["de"], ["philosophy"],
  "Georg Simmel was a German sociologist and philosopher who pioneered the study of social interaction, urban life, and the philosophy of money.", "Born in Berlin to a Jewish family that had converted to Christianity, he studied philosophy and history at the University of Berlin.", "His microsociological approach to studying social forms and interactions influenced the Chicago School of sociology and modern urban studies.",
  [(1900, "Published The Philosophy of Money"), (1903, "Published The Metropolis and Mental Life"), (1908, "Published Soziologie, his major sociological work")],
  [("The Philosophy of Money", 1900, "Analysis of how money transforms social relationships and culture"), ("The Metropolis and Mental Life", 1903, "Influential essay on the psychological effects of urban life")],
  [("The deepest problems of modern life derive from the claim of the individual to preserve the autonomy and individuality of his existence.", "The Metropolis and Mental Life")])

add("ferdinand-de-saussure", "Ferdinand de Saussure", "フェルディナン・ド・ソシュール", 1857, 1913, ["ch"], ["philosophy"],
  "Ferdinand de Saussure was a Swiss linguist whose ideas on the structure of language founded modern structural linguistics and influenced the entire field of semiotics.", "Born in Geneva to a prominent scientific family, he published a groundbreaking work on Indo-European vowels at age twenty-one.", "His distinction between langue and parole, the concept of the sign as signifier and signified, and the synchronic approach to language study revolutionized linguistics and influenced structuralism across all humanities.",
  [(1878, "Published Memoir on the Primitive System of Vowels in Indo-European Languages at age 21"), (1906, "Began teaching the courses on general linguistics at the University of Geneva")],
  [("Course in General Linguistics", 1916, "Posthumous compilation of his lectures that founded modern structural linguistics")],
  [("In language there are only differences without positive terms.", "Course in General Linguistics")])

add("claude-levi-strauss", "Claude Levi-Strauss", "クロード・レヴィ＝ストロース", 1908, 2009, ["fr"], ["philosophy"],
  "Claude Levi-Strauss was a French anthropologist who founded structural anthropology and transformed the understanding of human cultures through the analysis of myths, kinship, and classification systems.", "Born in Brussels and raised in Paris, he studied philosophy and law before traveling to Brazil as a professor, where fieldwork with indigenous peoples transformed his thinking.", "His structural approach to myth, kinship, and culture revealed universal patterns of human thought and profoundly influenced anthropology, philosophy, and literary theory.",
  [(1949, "Published The Elementary Structures of Kinship"), (1955, "Published Tristes Tropiques, his memoir of fieldwork in Brazil"), (1962, "Published The Savage Mind"), (1964, "Began publishing the four-volume Mythologiques")],
  [("Tristes Tropiques", 1955, "Philosophical memoir reflecting on travel, anthropology, and civilization"), ("The Savage Mind", 1962, "Analysis of how non-Western peoples think systematically about the natural world")],
  [("The scientist is not a person who gives the right answers, he is one who asks the right questions.", "The Raw and the Cooked")])

add("roland-barthes", "Roland Barthes", "ロラン・バルト", 1915, 1980, ["fr"], ["philosophy", "literature"],
  "Roland Barthes was a French literary theorist and philosopher whose work on semiotics, structuralism, and the nature of authorship profoundly influenced modern criticism.", "Born in Cherbourg, he was raised by his mother after his father's death in World War I and struggled with tuberculosis throughout his youth.", "His concept of the 'death of the author' and his semiotic analyses of culture from wrestling to photography revolutionized how texts and cultural phenomena are interpreted.",
  [(1957, "Published Mythologies, analyzing modern French cultural myths"), (1967, "Published the essay The Death of the Author"), (1970, "Published S/Z, a detailed analysis of a Balzac short story"), (1980, "Published Camera Lucida, his meditation on photography")],
  [("Mythologies", 1957, "Collection of essays analyzing the hidden ideological meanings in everyday French culture"), ("Camera Lucida", 1980, "Meditation on photography and mourning, written after his mother's death")],
  [("The birth of the reader must be at the cost of the death of the Author.", "The Death of the Author")])

add("umberto-eco", "Umberto Eco", "ウンベルト・エーコ", 1932, 2016, ["it"], ["philosophy", "literature"],
  "Umberto Eco was an Italian semiotician, philosopher, and novelist whose works bridged academic semiotics and popular fiction.", "Born in Alessandria, Piedmont, he studied at the University of Turin and became a leading figure in semiotics before achieving worldwide fame as a novelist.", "He demonstrated that intellectually rigorous fiction could reach a mass audience, and his semiotic theories influenced communication studies, aesthetics, and cultural criticism.",
  [(1962, "Published The Open Work, a pioneering study of interpretive openness in art"), (1976, "Published A Theory of Semiotics"), (1980, "Published The Name of the Rose, his first and most acclaimed novel")],
  [("The Name of the Rose", 1980, "Medieval mystery novel exploring semiotics, theology, and the politics of knowledge"), ("A Theory of Semiotics", 1976, "Systematic framework for the study of signs and meaning")],
  [("Books are not made to be believed, but to be subjected to inquiry.", "The Name of the Rose")])

# ===== ENGINEERS/INVENTORS =====

add("eli-whitney", "Eli Whitney", "イーライ・ホイットニー", 1765, 1825, ["us"], ["engineering"],
  "Eli Whitney was an American inventor who created the cotton gin and pioneered the concept of interchangeable parts in manufacturing.", "Born in Westborough, Massachusetts, he graduated from Yale and traveled south where he observed the labor-intensive process of separating cotton seeds from fiber.", "The cotton gin transformed the American South's economy, and his system of interchangeable parts for musket manufacture laid the foundation for the American system of manufacturing.",
  [(1793, "Invented the cotton gin"), (1798, "Secured a government contract to manufacture muskets using interchangeable parts")],
  [("Cotton Gin Patent", 1794, "Patent for the machine that efficiently separated cotton fibers from seeds")],
  [("One of my primary objects is to form the tools so the tools themselves shall fashion the work.", "Letter regarding interchangeable parts")])

add("samuel-morse", "Samuel Morse", "サミュエル・モース", 1791, 1872, ["us"], ["engineering"],
  "Samuel Morse was an American inventor and painter who developed the electric telegraph and the Morse code, revolutionizing long-distance communication.", "Born in Charlestown, Massachusetts, he was initially a successful portrait painter who became interested in electromagnetism after a personal tragedy during which delayed news of his wife's death arrived too late.", "The telegraph system he developed transformed global communication, enabling near-instantaneous long-distance messaging and laying the groundwork for modern telecommunications.",
  [(1838, "Demonstrated the telegraph to President Van Buren"), (1844, "Sent the first telegraph message 'What hath God wrought' from Washington to Baltimore")],
  [("Morse Code", 1838, "System of dots and dashes for encoding text messages in telegraph communication")],
  [("What hath God wrought!", "First telegraph message, May 24, 1844")])

add("cyrus-mccormick", "Cyrus McCormick", "サイラス・マコーミック", 1809, 1884, ["us"], ["engineering"],
  "Cyrus McCormick was an American inventor and businessman who developed the mechanical reaper, transforming agriculture worldwide.", "Born on a farm in Rockbridge County, Virginia, he inherited his father's unfinished work on a mechanical grain reaper and perfected the design.", "His mechanical reaper revolutionized farming, allowing vast expansion of grain production on the American prairies and contributing to the North's advantage in the Civil War.",
  [(1831, "Successfully demonstrated the first mechanical reaper"), (1847, "Established the McCormick Harvesting Machine Company in Chicago"), (1851, "Won the Grand Medal at the Crystal Palace Exhibition in London")],
  [("Mechanical Reaper Patent", 1834, "Patent for the horse-drawn grain-cutting machine")],
  [("Invent, or be content to be the slave of invention.", "Attributed")])

add("george-stephenson", "George Stephenson", "ジョージ・スティーブンソン", 1781, 1848, ["gb"], ["engineering"],
  "George Stephenson was the 'Father of Railways' who built the first public inter-city railway line and established the standard gauge used worldwide.", "Born in Wylam, Northumberland, to an illiterate family of colliery workers, he taught himself to read at age eighteen and became an expert on steam engines.", "He established railways as the dominant mode of transportation, setting the standard gauge of 4 feet 8.5 inches that is still used by most of the world's railways.",
  [(1814, "Built his first locomotive, Blucher, for hauling coal"), (1825, "Opened the Stockton and Darlington Railway, the first public railway"), (1829, "His locomotive Rocket won the Rainhill Trials for the Liverpool and Manchester Railway")],
  [("The Rocket", 1829, "Pioneering locomotive that proved the viability of steam-powered rail transport")],
  [("I have fought for the railway system against the most tremendous odds.", "Attributed")])

add("george-pullman", "George Pullman", "ジョージ・プルマン", 1831, 1897, ["us"], ["engineering"],
  "George Pullman was an American industrialist who revolutionized rail travel by developing the luxury sleeping car and founding the Pullman Palace Car Company.", "Born in Brocton, New York, he worked as a cabinetmaker before moving to Chicago where he began converting rail cars into sleepers.", "His Pullman sleeping cars transformed long-distance rail travel and his company town experiment, though ultimately controversial, influenced urban planning discussions.",
  [(1863, "Built his first Pullman sleeping car"), (1867, "Founded the Pullman Palace Car Company"), (1880, "Built the planned company town of Pullman, Illinois")],
  [("Pullman Sleeping Car", 1865, "Luxury railroad sleeping car that transformed American rail travel")],
  [("The worker who gets the best return is the one who makes his employer prosperous.", "Attributed")])

add("gottlieb-daimler", "Gottlieb Daimler", "ゴットリープ・ダイムラー", 1834, 1900, ["de"], ["engineering"],
  "Gottlieb Daimler was a German engineer and industrialist who pioneered the high-speed internal combustion engine and the modern automobile.", "Born in Schorndorf, Wurttemberg, he trained as a gunsmith and engineer before working with Nikolaus Otto on gas engines and later partnering with Wilhelm Maybach.", "His high-speed petrol engine powered the first motorcycle and one of the first automobiles, and his company eventually merged with Benz to form Daimler-Benz.",
  [(1883, "Developed the first high-speed internal combustion engine with Maybach"), (1885, "Created the Reitwagen, the first motorcycle"), (1890, "Founded Daimler-Motoren-Gesellschaft")],
  [("Reitwagen", 1885, "The world's first motorcycle, powered by a petrol engine")],
  [("The best or nothing.", "Company motto, later adopted by Mercedes-Benz")])

add("karl-benz", "Karl Benz", "カール・ベンツ", 1844, 1929, ["de"], ["engineering"],
  "Karl Benz was a German engine designer and automobile engineer who created the first practical automobile powered by an internal combustion engine.", "Born in Muhlburg, Baden, he studied mechanical engineering at the University of Karlsruhe and dedicated himself to creating a motorized vehicle.", "His Patent-Motorwagen of 1886 is widely regarded as the first true automobile, and his wife Bertha's famous long-distance drive proved its practicality to the world.",
  [(1886, "Patented the Benz Patent-Motorwagen, the first automobile"), (1888, "Bertha Benz drove the Patent-Motorwagen on the first long-distance automobile trip"), (1926, "Benz & Cie merged with Daimler to form Daimler-Benz")],
  [("Benz Patent-Motorwagen", 1886, "The world's first automobile powered by an internal combustion engine")],
  [("Nothing in this world is more powerful than an idea whose time has come.", "Attributed")])

add("ferdinand-von-zeppelin", "Ferdinand von Zeppelin", "フェルディナント・フォン・ツェッペリン", 1838, 1917, ["de"], ["engineering"],
  "Ferdinand von Zeppelin was a German general and aircraft manufacturer who developed the rigid airship that bears his name.", "Born into an aristocratic family in Konstanz, he served as a military officer and first observed balloons during the American Civil War as a volunteer observer for the Union Army.", "His Zeppelin airships pioneered commercial air travel and represented the cutting edge of aviation technology before the rise of heavier-than-air aircraft.",
  [(1900, "Launched the first Zeppelin airship, LZ 1, over Lake Constance"), (1909, "Founded the Zeppelin Company for airship construction"), (1910, "Zeppelin airships began regular commercial passenger service")],
  [("LZ 1", 1900, "The first rigid airship, launched from a floating hangar on Lake Constance")],
  [("One must have the courage to see things through.", "Attributed")])

add("igor-sikorsky", "Igor Sikorsky", "イーゴリ・シコルスキー", 1889, 1972, ["ua", "us"], ["engineering"],
  "Igor Sikorsky was a Russian-American aviation pioneer who designed the first successful helicopter and the first multi-engine fixed-wing aircraft.", "Born in Kiev, he was inspired by Leonardo da Vinci's helicopter drawings and Jules Verne's novels, studying engineering in Russia before emigrating to the United States.", "He built the first practical helicopter that could hover, take off vertically, and fly in any direction, establishing the helicopter as a vital tool for rescue, military, and civilian use.",
  [(1913, "Designed and flew the first multi-engine airplane, the Ilya Muromets"), (1939, "Flew the VS-300, the first practical helicopter"), (1943, "Produced the R-4, the world's first mass-produced helicopter")],
  [("VS-300", 1939, "The first practical single-rotor helicopter")],
  [("The work of the individual still remains the spark that moves mankind ahead.", "Attributed")])

add("willy-messerschmitt", "Willy Messerschmitt", "ヴィリー・メッサーシュミット", 1898, 1978, ["de"], ["engineering"],
  "Willy Messerschmitt was a German aircraft designer whose planes, particularly the Bf 109 and Me 262, were among the most significant military aircraft of the 20th century.", "Born in Frankfurt, he became fascinated with aviation as a teenager and began designing gliders while still a student.", "He designed the Bf 109, the most-produced fighter aircraft in history, and the Me 262, the world's first operational jet-powered fighter aircraft.",
  [(1934, "Designed the Bf 109, which became the Luftwaffe's primary fighter"), (1941, "The Me 262 jet fighter made its maiden flight"), (1944, "Me 262 entered operational service as the world's first jet fighter")],
  [("Bf 109", 1935, "The most-produced fighter aircraft in history with over 34,000 built"), ("Me 262", 1944, "The world's first operational jet-powered fighter aircraft")],
  [("The future of aviation lies in speed.", "Attributed")])

add("john-ericsson", "John Ericsson", "ジョン・エリクソン", 1803, 1889, ["se", "us"], ["engineering"],
  "John Ericsson was a Swedish-American inventor and mechanical engineer who designed the ironclad warship USS Monitor, revolutionizing naval warfare.", "Born in Langbanshyttan, Sweden, he showed early engineering talent and moved to the United States where he focused on marine propulsion and warship design.", "His Monitor design and its battle with the CSS Virginia marked the end of wooden warships and the beginning of the modern iron and steel navy.",
  [(1836, "Patented the screw propeller for ships"), (1862, "The USS Monitor fought the CSS Virginia in the first battle of ironclad warships"), (1868, "Developed early solar-powered engines")],
  [("USS Monitor", 1862, "Revolutionary ironclad warship with a rotating gun turret")],
  [("In mechanics, as in the universe, nothing is wasted.", "Attributed")])

add("ferdinand-de-lesseps", "Ferdinand de Lesseps", "フェルディナン・ド・レセップス", 1805, 1894, ["fr"], ["engineering"],
  "Ferdinand de Lesseps was a French diplomat and entrepreneur who supervised the construction of the Suez Canal, one of the greatest engineering feats of the 19th century.", "Born in Versailles to a distinguished diplomatic family, he served as a French consul in Egypt where he developed the idea for a sea-level canal connecting the Mediterranean and Red Sea.", "The Suez Canal he built fundamentally transformed global trade by eliminating the need to navigate around Africa, though his later Panama Canal attempt ended in scandal.",
  [(1854, "Obtained a concession from Egypt to build the Suez Canal"), (1869, "Suez Canal opened to navigation"), (1881, "Began work on the Panama Canal, which ended in financial disaster")],
  [("Suez Canal", 1869, "163-kilometer ship canal connecting the Mediterranean and Red Seas")],
  [("The names of those who in their lives fought for life, who wore at their hearts the fire's center.", "Attributed")])

add("john-roebling", "John Augustus Roebling", "ジョン・ローブリング", 1806, 1869, ["de", "us"], ["engineering"],
  "John Roebling was a German-American civil engineer who designed the Brooklyn Bridge, one of the greatest engineering achievements of the 19th century.", "Born in Muhlhausen, Prussia, he studied engineering under Hegel at the Royal Polytechnic Institute before emigrating to America.", "He pioneered the use of wire rope in suspension bridge construction and designed the Brooklyn Bridge, which was the longest suspension bridge in the world when completed.",
  [(1845, "Completed the first wire-rope suspension aqueduct over the Allegheny River"), (1855, "Completed the Niagara Falls Suspension Bridge"), (1867, "Began designing the Brooklyn Bridge"), (1869, "Died from tetanus after his foot was crushed during bridge survey work")],
  [("Brooklyn Bridge", 1883, "Iconic suspension bridge completed posthumously by his son Washington Roebling")],
  [("The great engineer must be a man of imagination.", "Attributed")])

add("joseph-bazalgette", "Joseph Bazalgette", "ジョセフ・バザルゲット", 1819, 1891, ["gb"], ["engineering"],
  "Joseph Bazalgette was a British civil engineer who designed London's sewer system, one of the greatest public health engineering achievements in history.", "Born in Enfield, Middlesex, he trained as a civil engineer and became chief engineer of London's Metropolitan Board of Works.", "His revolutionary sewer system ended London's cholera epidemics and is considered one of the most important infrastructure projects of the 19th century, saving countless lives.",
  [(1858, "The Great Stink prompted Parliament to fund his sewer plan"), (1865, "Completed the southern sewer outfall at Crossness"), (1875, "Completed the Victoria Embankment along the Thames")],
  [("London Main Drainage System", 1875, "Network of 1,100 miles of sewers beneath London that eliminated cholera from the city")],
  [("Well, we're only going to do this once and there's always the unforeseen.", "On oversizing the sewer tunnels, which proved prescient")])

add("nikolaus-otto", "Nikolaus Otto", "ニコラウス・オットー", 1832, 1891, ["de"], ["engineering"],
  "Nikolaus Otto was a German engineer who developed the first practical internal combustion engine using the four-stroke cycle that still powers most cars today.", "Born in Holzhausen, he was self-educated and worked as a traveling salesman before becoming obsessed with building a gas-powered engine.", "The four-stroke Otto cycle engine became the basis for nearly all internal combustion engines, making possible the automobile revolution.",
  [(1864, "Founded N.A. Otto & Cie, the world's first engine manufacturing company"), (1876, "Built the first practical four-stroke internal combustion engine"), (1884, "Lost his patent after prior art by Alphonse Beau de Rochas was discovered")],
  [("Otto Engine", 1876, "The first practical four-stroke internal combustion engine")],
  [("The silent engine is my greatest achievement.", "Attributed, referring to the smooth operation of the four-stroke engine")])

add("rudolf-diesel", "Rudolf Diesel", "ルドルフ・ディーゼル", 1858, 1913, ["de"], ["engineering"],
  "Rudolf Diesel was a German engineer who invented the diesel engine, a more efficient alternative to the steam and gasoline engines of his era.", "Born in Paris to Bavarian immigrants, he studied engineering at the Royal Bavarian Polytechnic in Munich and became obsessed with creating a more efficient engine.", "The diesel engine he invented became the dominant power source for heavy transport, shipping, and industry, and his vision of running engines on plant oils anticipated modern biofuels.",
  [(1893, "Published the theory of the diesel engine"), (1897, "Built the first successful diesel engine in Augsburg"), (1913, "Mysteriously disappeared from a ship crossing the English Channel")],
  [("Theory and Construction of a Rational Heat-Motor", 1893, "Technical paper describing the principles of the diesel engine")],
  [("The use of plant oils as engine fuels may seem insignificant today, but such oils may become in the course of time as important as petroleum.", "On biofuels, 1912")])

# ===== BIOLOGISTS/MEDICAL =====

add("hippocrates", "Hippocrates", "ヒポクラテス", -460, -370, ["gr"], ["biology"],
  "Hippocrates was an ancient Greek physician known as the 'Father of Medicine' who established medicine as a discipline separate from philosophy and superstition.", "Born on the island of Kos, he came from a family of physicians and studied under his father before traveling widely in Greece.", "He established the ethical foundations of medical practice through the Hippocratic Oath and pioneered clinical observation and systematic diagnosis.",
  [(-400, "Established a medical school on Kos"), (-380, "Hippocratic Corpus compiled by his followers")],
  [("Hippocratic Corpus", -400, "Collection of medical texts establishing principles of clinical medicine and ethics")],
  [("First, do no harm.", "Attributed, paraphrasing the Hippocratic tradition"), ("Healing is a matter of time, but it is sometimes also a matter of opportunity.", "Precepts")])

add("galen", "Galen", "ガレノス", 129, 216, ["gr"], ["biology"],
  "Galen was a Greek physician and philosopher whose medical theories dominated Western medicine for over 1,300 years.", "Born in Pergamon to a wealthy architect father, he studied medicine across the Greek world and became physician to the Roman gladiators.", "His anatomical writings and medical theories were the unchallenged authority in medicine from antiquity through the Renaissance.",
  [(157, "Became physician to the gladiators of Pergamon"), (162, "Moved to Rome and became physician to Emperor Marcus Aurelius"), (170, "Wrote his major anatomical and medical works")],
  [("On the Usefulness of the Parts of the Body", 170, "Comprehensive anatomical treatise describing the function of bodily organs"), ("On the Natural Faculties", 175, "Work on physiology explaining bodily functions")],
  [("The chief merit of language is clearness, and we know that nothing detracts so much from this as do unfamiliar terms.", "On the Natural Faculties")])

add("paracelsus", "Paracelsus", "パラケルスス", 1493, 1541, ["ch"], ["chemistry", "biology"],
  "Paracelsus was a Swiss-German physician and alchemist who pioneered the use of chemicals and minerals in medicine, founding the field of toxicology.", "Born Theophrastus von Hohenheim near Zurich, he wandered across Europe learning folk medicine and alchemy before challenging the medical establishment.", "He revolutionized medicine by introducing chemical remedies, establishing the dose-response principle of toxicology, and challenging the ancient authority of Galen.",
  [(1527, "Appointed professor of medicine in Basel, where he publicly burned Galen's works"), (1530, "Wrote his major works on surgery and diseases of miners")],
  [("Die grosse Wundarzney", 1536, "Major surgical text that established his reputation across Europe")],
  [("The dose makes the poison.", "Attributed, foundational principle of toxicology"), ("Medicine is not only a science; it is also an art.", "Attributed")])

add("ambroise-pare", "Ambroise Pare", "アンブロワーズ・パレ", 1510, 1590, ["fr"], ["biology"],
  "Ambroise Pare was a French barber-surgeon who is considered the father of modern surgery for his revolutionary techniques in wound treatment and surgical practice.", "Born in Bourg-Hersent, he trained as a barber-surgeon in Paris and gained his surgical experience on the battlefields of the Italian Wars.", "He replaced the brutal practice of cauterizing wounds with boiling oil with gentler ligature techniques and prosthetic design, transforming surgical practice.",
  [(1545, "Published his first work on treating gunshot wounds"), (1552, "Became surgeon to King Henry II of France"), (1575, "Published his collected surgical works")],
  [("Les Oeuvres", 1575, "Comprehensive collected works on surgery and wound treatment")],
  [("I dressed him and God healed him.", "On treating a wounded soldier")])

add("ignaz-semmelweis", "Ignaz Semmelweis", "イグナーツ・ゼンメルワイス", 1818, 1865, ["hu"], ["biology"],
  "Ignaz Semmelweis was a Hungarian physician who discovered that handwashing by doctors dramatically reduced the incidence of childbed fever, pioneering antiseptic medicine.", "Born in Buda to a German-speaking family, he studied medicine in Vienna and became an assistant at the Vienna General Hospital's maternity clinic.", "His discovery that hand disinfection could prevent puerperal fever saved countless lives, though his ideas were rejected during his lifetime in one of medicine's greatest tragedies.",
  [(1847, "Introduced mandatory handwashing with chlorinated lime at the Vienna maternity clinic"), (1850, "Published data showing dramatic reduction in maternal mortality"), (1861, "Published The Etiology, Concept, and Prophylaxis of Childbed Fever")],
  [("The Etiology, Concept, and Prophylaxis of Childbed Fever", 1861, "Book documenting his evidence for hand disinfection in preventing puerperal fever")],
  [("When I look back upon the past, I can only dispel the sadness which falls upon me by gazing into that happy future when the infection will be banished.", "The Etiology, Concept, and Prophylaxis of Childbed Fever")])

add("florence-nightingale", "Florence Nightingale", "フローレンス・ナイチンゲール", 1820, 1910, ["gb"], ["biology"],
  "Florence Nightingale was the founder of modern nursing who transformed hospital sanitation and established nursing as a respected profession.", "Born into a wealthy British family in Florence, Italy, she defied her family's expectations by pursuing nursing, which was then considered a disreputable occupation.", "She established nursing as a scientific profession, pioneered the use of statistical graphics in public health, and her reforms saved countless lives in military and civilian hospitals.",
  [(1854, "Led a team of nurses to the Crimean War, drastically reducing mortality"), (1858, "Published Notes on Matters Affecting the Health of the British Army"), (1860, "Founded the Nightingale Training School at St Thomas' Hospital")],
  [("Notes on Nursing", 1860, "Foundational text of modern nursing practice")],
  [("I attribute my success to this: I never gave or took any excuse.", "Attributed")])

add("elizabeth-blackwell", "Elizabeth Blackwell", "エリザベス・ブラックウェル", 1821, 1910, ["gb", "us"], ["biology"],
  "Elizabeth Blackwell was the first woman to receive a medical degree in the United States, breaking the gender barrier in Western medicine.", "Born in Bristol, England, she emigrated to America with her family and decided to pursue medicine after a dying friend said she would have been spared embarrassment by a female physician.", "She opened doors for women in medicine by establishing the New York Infirmary for Indigent Women and Children and a medical college for women.",
  [(1849, "Became the first woman to receive a medical degree in the United States from Geneva Medical College"), (1857, "Founded the New York Infirmary for Indigent Women and Children"), (1868, "Established a medical college for women")],
  [("Pioneer Work in Opening the Medical Profession to Women", 1895, "Autobiography describing her struggle to enter medicine")],
  [("It is not easy to be a pioneer, but oh, it is fascinating!", "Pioneer Work in Opening the Medical Profession to Women")])

add("mary-seacole", "Mary Seacole", "メアリー・シーコール", 1805, 1881, ["jm", "gb"], ["biology"],
  "Mary Seacole was a Jamaican-British nurse and businesswoman who provided care to wounded soldiers during the Crimean War despite racial prejudice.", "Born Mary Jane Grant in Kingston, Jamaica, she learned traditional medicine and nursing from her mother and gained experience treating cholera and other diseases across the Caribbean.", "She overcame racial barriers to provide frontline medical care during the Crimean War and her autobiography became an important document of Black British history.",
  [(1854, "Traveled to Crimea at her own expense after being rejected by the War Office"), (1855, "Established the 'British Hotel' near the front lines to treat wounded soldiers"), (1857, "Published her autobiography, Wonderful Adventures of Mrs. Seacole")],
  [("Wonderful Adventures of Mrs. Seacole in Many Lands", 1857, "Autobiography describing her travels and medical work in the Crimean War")],
  [("I trust I have made the reader understand that I did not only nurse the sick, but I was a doctress.", "Wonderful Adventures of Mrs. Seacole")])

add("walter-reed", "Walter Reed", "ウォルター・リード", 1851, 1902, ["us"], ["biology"],
  "Walter Reed was an American army physician who proved that yellow fever is transmitted by mosquitoes, enabling the control of one of the most devastating tropical diseases.", "Born in Belroi, Virginia, he earned his medical degree at age seventeen and served as a military physician across the American frontier.", "His proof of mosquito transmission of yellow fever enabled the construction of the Panama Canal and saved millions of lives in tropical regions.",
  [(1900, "Led the Yellow Fever Board in Cuba to investigate disease transmission"), (1901, "Confirmed mosquito transmission of yellow fever through controlled experiments")],
  [("The Etiology of Yellow Fever", 1901, "Paper proving that Aedes aegypti mosquitoes transmit yellow fever")],
  [("The prayer that has been mine for twenty years, that I might be permitted to do something to alleviate human suffering, has been granted.", "Letter to his wife, 1900")])

add("gerhard-domagk", "Gerhard Domagk", "ゲルハルト・ドーマク", 1895, 1964, ["de"], ["biology", "chemistry"],
  "Gerhard Domagk was a German pathologist and bacteriologist who discovered sulfonamide, the first commercially available antibiotic, saving millions of lives.", "Born in Lagow, Brandenburg, he served as a medic in World War I and was profoundly affected by the infections that killed wounded soldiers.", "His discovery of Prontosil launched the sulfonamide drug revolution that was the first effective treatment for bacterial infections, preceding penicillin.",
  [(1932, "Discovered the antibacterial properties of Prontosil"), (1935, "Published results showing Prontosil's effectiveness against streptococcal infections"), (1939, "Awarded the Nobel Prize in Physiology or Medicine but forced by the Nazis to decline it")],
  [("Prontosil", 1935, "The first commercially available antibacterial drug")],
  [("I have dedicated my life to finding weapons against the invisible enemies that cause so much suffering.", "Attributed")])

add("selman-waksman", "Selman Waksman", "セルマン・ワクスマン", 1888, 1973, ["ua", "us"], ["biology"],
  "Selman Waksman was a Ukrainian-American microbiologist who discovered streptomycin, the first antibiotic effective against tuberculosis.", "Born in Novaya Priluka, Ukraine, he emigrated to the United States and studied soil microbiology at Rutgers University.", "His systematic search for antibiotics in soil microorganisms led to the discovery of streptomycin, saving millions from tuberculosis and coining the word 'antibiotic.'",
  [(1940, "Coined the term 'antibiotic'"), (1943, "His lab discovered streptomycin, the first effective treatment for tuberculosis"), (1952, "Awarded the Nobel Prize in Physiology or Medicine")],
  [("Streptomycin", 1943, "The first antibiotic effective against tuberculosis")],
  [("The earth will still keep its secret.", "On the vast untapped potential of soil microorganisms")])

add("albert-schweitzer", "Albert Schweitzer", "アルベルト・シュヴァイツァー", 1875, 1965, ["fr", "de"], ["biology", "philosophy"],
  "Albert Schweitzer was an Alsatian-German theologian, philosopher, musician, and physician who devoted his life to medical missionary work in Africa.", "Born in Kaysersberg, Alsace, he was a renowned organist and Bach scholar who shocked his peers by deciding at age thirty to study medicine and serve in Africa.", "He established a hospital in Lambarene, Gabon, developed the ethic of 'Reverence for Life,' and won the Nobel Peace Prize for his humanitarian work.",
  [(1913, "Founded a hospital in Lambarene, French Equatorial Africa"), (1923, "Published The Philosophy of Civilization, articulating his ethic of Reverence for Life"), (1952, "Awarded the Nobel Peace Prize")],
  [("The Quest of the Historical Jesus", 1906, "Landmark work of biblical scholarship"), ("The Philosophy of Civilization", 1923, "Philosophical work developing the ethic of Reverence for Life")],
  [("Until he extends the circle of his compassion to all living things, man will not himself find peace.", "The Philosophy of Civilization")])

add("christiaan-barnard", "Christiaan Barnard", "クリスチャン・バーナード", 1922, 2001, ["za"], ["biology"],
  "Christiaan Barnard was a South African cardiac surgeon who performed the world's first successful human-to-human heart transplant.", "Born in Beaufort West, Cape Province, he studied medicine at the University of Cape Town and trained in cardiac surgery at the University of Minnesota.", "His pioneering heart transplant opened the era of organ transplantation and transformed cardiac surgery from an experimental field into a life-saving practice.",
  [(1967, "Performed the world's first human-to-human heart transplant at Groote Schuur Hospital"), (1974, "Performed the first heterotopic heart transplant")],
  [("One Life", 1969, "Autobiography describing his path to the first heart transplant")],
  [("It is infinitely better to transplant a heart than to bury it to be devoured by worms.", "Press conference after the first heart transplant")])

add("michael-debakey", "Michael DeBakey", "マイケル・ドゥベイキー", 1908, 2008, ["us"], ["biology", "engineering"],
  "Michael DeBakey was an American cardiac surgeon and medical inventor who pioneered many cardiovascular surgical procedures and devices.", "Born in Lake Charles, Louisiana, to Lebanese immigrant parents, he studied at Tulane University and developed a roller pump as a medical student that later became a key component of the heart-lung machine.", "He performed the first successful carotid endarterectomy, developed artificial hearts and ventricular assist devices, and trained two generations of cardiac surgeons.",
  [(1953, "Performed the first successful carotid endarterectomy"), (1964, "Performed the first successful coronary artery bypass surgery"), (1966, "Implanted the first ventricular assist device in a patient")],
  [("Roller Pump", 1932, "Blood pump that became essential to heart-lung machines and open-heart surgery")],
  [("The pursuit of excellence is a never-ending process.", "Attributed")])

add("albert-sabin", "Albert Sabin", "アルバート・セービン", 1906, 1993, ["pl", "us"], ["biology"],
  "Albert Sabin was a Polish-American medical researcher who developed the oral polio vaccine that became the primary tool in the global eradication of poliomyelitis.", "Born in Bialystok, Poland, he emigrated to the United States as a teenager and studied medicine at New York University.", "His oral polio vaccine, easier to administer than the Salk injectable vaccine, became the standard worldwide and was instrumental in nearly eradicating polio globally.",
  [(1955, "Developed the oral polio vaccine using attenuated live virus"), (1959, "Oral polio vaccine tested successfully on millions in the Soviet Union"), (1961, "Oral polio vaccine licensed for use in the United States")],
  [("Oral Polio Vaccine", 1955, "Live attenuated vaccine administered orally, enabling mass immunization campaigns worldwide")],
  [("A scientist who is also a human being cannot rest while knowledge which might be used to reduce suffering rests on a shelf.", "Attributed")])

if __name__ == "__main__":
    write_people(P)
