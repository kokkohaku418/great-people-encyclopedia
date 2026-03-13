#!/usr/bin/env python3
"""Supplement batch 5: 150+ more unique people to reach 700+."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# === PHYSICISTS ===
p("sheldon-glashow", "Sheldon Glashow", "シェルドン・グラショー", 1932, None, ["us"], ["physics"],
  "Sheldon Glashow is an American theoretical physicist who contributed to the electroweak unification theory.",
  "Glashow was born in New York City. He studied at Cornell and Harvard, working on gauge theories and particle physics.",
  "Glashow's electroweak theory unified the electromagnetic and weak nuclear forces, a key component of the Standard Model.",
  [(1961, "Proposed electroweak unification"), (1979, "Awarded Nobel Prize in Physics")],
  [("A Partial-Symmetries of Weak Interactions", 1961, "Paper proposing electroweak unification")],
  [("The universe is not only queerer than we suppose, but queerer than we can suppose.", "Attributed")])

p("luis-alvarez", "Luis Walter Alvarez", "ルイス・ウォルター・アルバレス", 1911, 1988, ["us"], ["physics"],
  "Luis Alvarez was an American experimental physicist who won the Nobel Prize and co-proposed the asteroid impact theory for dinosaur extinction.",
  "Alvarez was born in San Francisco. He studied at the University of Chicago and worked at the Radiation Laboratory at MIT during WWII.",
  "Alvarez's contributions to particle physics earned him the Nobel Prize. His asteroid impact hypothesis, developed with his son, revolutionized paleontology.",
  [(1947, "Discovered resonance particles"), (1968, "Awarded Nobel Prize in Physics"), (1980, "Proposed asteroid impact theory for dinosaur extinction")],
  [("Extraterrestrial Cause for the Cretaceous-Tertiary Extinction", 1980, "Paper proposing asteroid impact caused dinosaur extinction")],
  [("There is no democracy in physics.", "Attributed")])

p("kip-thorne", "Kip Thorne", "キップ・ソーン", 1940, None, ["us"], ["physics", "astronomy"],
  "Kip Thorne is an American theoretical physicist who won the Nobel Prize for his contributions to the detection of gravitational waves.",
  "Thorne was born in Logan, Utah. He studied at Caltech and Princeton and spent his career at Caltech working on general relativity and gravitational physics.",
  "Thorne's theoretical work on gravitational waves enabled the LIGO detection in 2015, confirming Einstein's prediction and opening a new window on the universe.",
  [(1973, "Co-authored Gravitation textbook"), (1994, "Published Black Holes and Time Warps"), (2015, "LIGO detected gravitational waves"), (2017, "Awarded Nobel Prize in Physics")],
  [("Gravitation", 1973, "Definitive textbook on general relativity")],
  [("The warped side of the universe — black holes, wormholes, time warps — is a playground for physicists.", "Attributed")])

p("lisa-randall", "Lisa Randall", "リサ・ランドール", 1962, None, ["us"], ["physics"],
  "Lisa Randall is an American theoretical physicist whose research includes particle physics and cosmology, particularly extra dimensions of space.",
  "Randall was born in Queens, New York. She studied at Harvard and became the first woman to receive tenure in the physics departments at MIT and Harvard.",
  "Randall's Randall-Sundrum models of extra dimensions offered new approaches to the hierarchy problem in physics and influenced theoretical particle physics.",
  [(1999, "Published Randall-Sundrum model"), (2005, "Published Warped Passages"), (2011, "Published Knocking on Heaven's Door")],
  [("Warped Passages", 2005, "Popular book on extra dimensions and particle physics")],
  [("The ability to ask the right questions is more than half the battle.", "Attributed")])

p("chien-shiung-wu", "Chien-Shiung Wu", "呉健雄", 1912, 1997, ["cn", "us"], ["physics"],
  "Chien-Shiung Wu was a Chinese-American experimental physicist who disproved the conservation of parity, one of the most important experiments in particle physics.",
  "Wu was born in Liuhe, China. She studied at Nanjing University and the University of California, Berkeley, then worked at Columbia University.",
  "Wu's elegant experiment disproving parity conservation confirmed Yang and Lee's theory. She was called the 'First Lady of Physics' but was controversially excluded from the Nobel Prize.",
  [(1944, "Worked on the Manhattan Project"), (1956, "Conducted parity violation experiment"), (1957, "Experiment confirmed parity non-conservation"), (1975, "Became first female president of the American Physical Society")],
  [("Experimental Test of Parity Conservation in Beta Decay", 1957, "Landmark experiment disproving parity conservation")],
  [("It is shameful that there are so few women in science.", "Attributed")])

# === MORE MATHEMATICIANS ===
p("evariste-galois", "Évariste Galois", "エヴァリスト・ガロア", 1811, 1832, ["fr"], ["mathematics"],
  "Évariste Galois was a French mathematician who laid the foundations of group theory and Galois theory while still a teenager.",
  "Galois was born in Bourg-la-Reine, France. A political revolutionary, he was twice imprisoned and died in a duel at age 20.",
  "Galois's work, written the night before his fatal duel, established group theory and solved the centuries-old problem of which polynomial equations are solvable by radicals.",
  [(1829, "Submitted first papers to the Academy"), (1830, "Participated in the July Revolution"), (1832, "Killed in a duel at age 20")],
  [("Sur les conditions de résolubilité des équations par radicaux", 1831, "Paper founding Galois theory")],
  [("Do not cry, Alfred! I need all my courage to die at twenty.", "Attributed last words to his brother")])

p("niels-henrik-abel", "Niels Henrik Abel", "ニールス・ヘンリック・アーベル", 1802, 1829, ["no"], ["mathematics"],
  "Niels Henrik Abel was a Norwegian mathematician who proved the impossibility of solving the general quintic equation by radicals.",
  "Abel was born in Nedstrand, Norway, into a poor family. He showed extraordinary mathematical talent and studied at the University of Christiania.",
  "Abel's proof of the unsolvability of the quintic and his work on elliptic functions were landmark achievements. He died of tuberculosis at age 26.",
  [(1824, "Proved the impossibility of solving the quintic"), (1826, "Published work on elliptic functions"), (1829, "Died of tuberculosis at age 26")],
  [("Proof of the Impossibility of Generally Solving Algebraic Equations of Degree Higher than Four", 1824, "Landmark proof in algebra")],
  [("Abel has left mathematicians enough to keep them busy for 500 years.", "Hermite, about Abel")])

p("emmy-noether-dup-check", "Sofia Kovalevskaya", "ソフィア・コワレフスカヤ", 1850, 1891, ["ru", "se"], ["mathematics"],
  "Sofia Kovalevskaya was a Russian mathematician who was the first woman to obtain a doctorate in mathematics and the first woman appointed to a full professorship in Europe.",
  "Kovalevskaya was born in Moscow. She entered a marriage of convenience to travel abroad for education, studying under Weierstrass in Berlin.",
  "Kovalevskaya made important contributions to analysis, partial differential equations, and mechanics, breaking barriers for women in mathematics and academia.",
  [(1874, "Earned doctorate from University of Göttingen"), (1884, "Appointed professor at Stockholm University"), (1888, "Won Prix Bordin from the French Academy of Sciences")],
  [("On the Rotation of a Solid Body about a Fixed Point", 1888, "Prize-winning work on the mathematics of rotating bodies")],
  [("It is impossible to be a mathematician without being a poet in soul.", "Attributed")])

p("ramanujan-dup-check", "G.H. Hardy", "G・H・ハーディ", 1877, 1947, ["gb"], ["mathematics"],
  "G.H. Hardy was an English mathematician known for his work in number theory and mathematical analysis, and for his collaboration with Ramanujan.",
  "Hardy was born in Cranleigh, Surrey. He studied at Cambridge and became a leading pure mathematician, championing the aesthetic value of mathematics.",
  "Hardy's collaboration with Ramanujan produced groundbreaking results in number theory. His essay A Mathematician's Apology is a classic defense of pure mathematics.",
  [(1908, "Published A Course of Pure Mathematics"), (1913, "Began collaboration with Ramanujan"), (1940, "Published A Mathematician's Apology")],
  [("A Mathematician's Apology", 1940, "Classic essay on the beauty and importance of pure mathematics")],
  [("A mathematician, like a painter or a poet, is a maker of patterns.", "A Mathematician's Apology")])

# === MORE WRITERS ===
p("ernest-hemingway", "Ernest Hemingway", "アーネスト・ヘミングウェイ", 1899, 1961, ["us"], ["literature"],
  "Ernest Hemingway was an American novelist and journalist whose economical writing style influenced 20th-century fiction.",
  "Hemingway was born in Oak Park, Illinois. He served as an ambulance driver in World War I, an experience that shaped his writing.",
  "Hemingway's spare, declarative prose style revolutionized American fiction. His novels and stories exploring courage under pressure defined a literary generation.",
  [(1926, "Published The Sun Also Rises"), (1929, "Published A Farewell to Arms"), (1952, "Published The Old Man and the Sea"), (1954, "Awarded Nobel Prize in Literature")],
  [("The Old Man and the Sea", 1952, "Novella about an aging fisherman's epic struggle"), ("A Farewell to Arms", 1929, "Novel about love and war in World War I")],
  [("All you have to do is write one true sentence.", "A Moveable Feast")])

p("william-faulkner", "William Faulkner", "ウィリアム・フォークナー", 1897, 1962, ["us"], ["literature"],
  "William Faulkner was an American writer known for his novels set in the fictional Yoknapatawpha County, Mississippi.",
  "Faulkner was born in New Albany, Mississippi. He grew up in Oxford, Mississippi, and drew on Southern history and culture for his fiction.",
  "Faulkner's experimental narrative techniques and his exploration of Southern history, race, and family created a body of work unmatched in American literature.",
  [(1929, "Published The Sound and the Fury"), (1930, "Published As I Lay Dying"), (1936, "Published Absalom, Absalom!"), (1949, "Awarded Nobel Prize in Literature")],
  [("The Sound and the Fury", 1929, "Novel told through multiple perspectives including a mentally disabled narrator"), ("Absalom, Absalom!", 1936, "Complex novel about the rise and fall of a Southern dynasty")],
  [("The past is never dead. It's not even past.", "Requiem for a Nun")])

p("samuel-beckett", "Samuel Beckett", "サミュエル・ベケット", 1906, 1989, ["ie", "fr"], ["literature"],
  "Samuel Beckett was an Irish novelist, playwright, and poet who won the Nobel Prize in Literature for his work that explored the destitution of modern man.",
  "Beckett was born in Foxrock, Dublin. He studied at Trinity College Dublin and moved to Paris, where he became associated with James Joyce.",
  "Beckett's Waiting for Godot revolutionized theater. His minimalist works stripped away conventional narrative to reveal the essential absurdity and suffering of human existence.",
  [(1938, "Settled permanently in Paris"), (1953, "Premiered Waiting for Godot"), (1957, "Published Endgame"), (1969, "Awarded Nobel Prize in Literature")],
  [("Waiting for Godot", 1953, "Play about two men waiting for someone who never comes"), ("Endgame", 1957, "Play about the end of the world")],
  [("Ever tried. Ever failed. No matter. Try again. Fail again. Fail better.", "Worstward Ho")])

p("gabriel-mistral", "Gabriela Mistral", "ガブリエラ・ミストラル", 1889, 1957, ["cl"], ["literature"],
  "Gabriela Mistral was a Chilean poet, diplomat, and educator who was the first Latin American author to receive a Nobel Prize in Literature.",
  "Mistral was born Lucila Godoy Alcayaga in Vicuña, Chile. She worked as a teacher and school administrator while writing poetry.",
  "Mistral's poetry of love, sorrow, and nature made her an icon of Latin American literature. She championed education reform and children's rights throughout her life.",
  [(1914, "Won Chilean national poetry prize"), (1922, "Published Desolación"), (1945, "Awarded Nobel Prize in Literature")],
  [("Desolación", 1922, "First poetry collection exploring love, loss, and nature")],
  [("Many things we need can wait. The child cannot. Now is the time.", "Attributed")])

p("wislawa-szymborska", "Wisława Szymborska", "ヴィスワヴァ・シンボルスカ", 1923, 2012, ["pl"], ["literature"],
  "Wisława Szymborska was a Polish poet who won the Nobel Prize in Literature for poetry that combined ironic precision with philosophical depth.",
  "Szymborska was born in Kórnik, Poland. She lived most of her life in Kraków, working quietly while producing some of the most admired poetry of the 20th century.",
  "Szymborska's deceptively simple poems explored the everyday with philosophical wonder, earning her the Nobel Prize and a devoted worldwide readership.",
  [(1952, "Published first collection"), (1976, "Published A Large Number"), (1996, "Awarded Nobel Prize in Literature")],
  [("View with a Grain of Sand", 1995, "English-language collection of her poetry")],
  [("Whatever inspiration is, it's born from a continuous 'I don't know.'", "Nobel lecture")])

p("yasunari-kawabata", "Yasunari Kawabata", "川端康成", 1899, 1972, ["jp"], ["literature"],
  "Yasunari Kawabata was a Japanese novelist who was the first Japanese author to receive the Nobel Prize in Literature.",
  "Kawabata was born in Osaka, Japan. Orphaned as a young child, he studied at Tokyo Imperial University and became a leading figure in Japanese literature.",
  "Kawabata's lyrical, spare prose captured the beauty and melancholy of Japanese culture. His novels bridge traditional Japanese aesthetics and modern literature.",
  [(1935, "Published Snow Country"), (1949, "Published Thousand Cranes"), (1961, "Published The Old Capital"), (1968, "Awarded Nobel Prize in Literature")],
  [("Snow Country", 1935, "Novel set in a remote hot spring town, exploring love and beauty"), ("The Old Capital", 1962, "Novel about twin sisters in Kyoto")],
  [("The beauty of the snow country was a beauty that seemed to flow back and forth between the two of them.", "Snow Country")])

p("kenzaburo-oe", "Kenzaburō Ōe", "大江健三郎", 1935, 2023, ["jp"], ["literature"],
  "Kenzaburō Ōe was a Japanese novelist who won the Nobel Prize in Literature for creating an imagined world where life and myth condense.",
  "Ōe was born in a small village in Shikoku. He studied French literature at the University of Tokyo and was influenced by Sartre and Rabelais.",
  "Ōe's novels, deeply personal and politically engaged, explored postwar Japan, disability, and the relationship between the individual and society.",
  [(1958, "Published Nip the Buds, Shoot the Kids"), (1964, "Published A Personal Matter"), (1994, "Awarded Nobel Prize in Literature")],
  [("A Personal Matter", 1964, "Novel about a father coming to terms with his brain-damaged son")],
  [("The new man will find his way to the light.", "Attributed")])

# === MORE POLITICAL FIGURES ===
p("akbar-the-great", "Akbar the Great", "アクバル大帝", 1542, 1605, ["in"], ["politics"],
  "Akbar the Great was the third Mughal Emperor who expanded the empire across most of the Indian subcontinent and promoted religious tolerance.",
  "Akbar was born in Umerkot, Sindh. He ascended to the throne at age 13 and ruled for nearly 50 years through military conquests and administrative reforms.",
  "Akbar's policy of religious tolerance, his administrative reforms, and his patronage of arts and culture marked the golden age of the Mughal Empire.",
  [(1556, "Became Mughal Emperor at age 13"), (1575, "Built Fatehpur Sikri"), (1579, "Issued the Infallibility Decree"), (1582, "Founded the Din-i-Ilahi religious movement")],
  [("Ain-i-Akbari", 1595, "Administrative document describing the Mughal government system")],
  [("A king should always be intent on conquest, otherwise his neighbors will rise in arms against him.", "Attributed")])

p("shaka-zulu", "Shaka Zulu", "シャカ・ズールー", 1787, 1828, ["za"], ["politics"],
  "Shaka Zulu was the founder of the Zulu Kingdom and a military innovator who transformed warfare in southern Africa.",
  "Shaka was born the illegitimate son of the Zulu chief Senzangakhona. He was raised in exile and became a warrior in the Mthethwa confederation.",
  "Shaka's military innovations, including the short stabbing spear and the bull-horn formation, created a powerful Zulu state that dominated southeastern Africa.",
  [(1816, "Became chief of the Zulu"), (1818, "Introduced military reforms"), (1820, "Expanded Zulu territory dramatically"), (1828, "Assassinated by his half-brothers")],
  [("Zulu Military System", 1818, "Revolutionary military organization and tactics")],
  [("Strike an enemy once and for all.", "Attributed")])

p("suleiman-the-magnificent", "Suleiman the Magnificent", "スレイマン1世", 1494, 1566, ["tr"], ["politics"],
  "Suleiman the Magnificent was the tenth and longest-reigning Sultan of the Ottoman Empire, during which it reached the peak of its power.",
  "Suleiman was born in Trabzon, Turkey. He became Sultan at age 25 and embarked on military campaigns that expanded the empire across three continents.",
  "Under Suleiman, the Ottoman Empire reached its golden age in law, literature, art, and architecture. His legal reforms earned him the title 'The Lawgiver.'",
  [(1520, "Became Sultan"), (1529, "Siege of Vienna"), (1534, "Conquered Baghdad"), (1566, "Died during the Siege of Szigetvár")],
  [("Kanuni (The Lawgiver)", 1520, "Legal reform of the Ottoman Empire")],
  [("The people think of wealth and power as the greatest fate, but in this world a spell of health is the best state.", "Attributed")])

p("mansa-musa", "Mansa Musa", "マンサ・ムーサ", 1280, 1337, ["ml"], ["politics"],
  "Mansa Musa was the ruler of the Mali Empire who is considered one of the wealthiest people in history.",
  "Musa was born into the ruling dynasty of the Mali Empire. He became mansa (emperor) and expanded the empire to encompass much of West Africa.",
  "Musa's famous pilgrimage to Mecca in 1324 displayed such extraordinary wealth that it disrupted gold markets. He made Timbuktu a center of Islamic learning.",
  [(1312, "Became Mansa of the Mali Empire"), (1324, "Pilgrimage to Mecca"), (1327, "Built the Djinguereber Mosque in Timbuktu")],
  [("Pilgrimage to Mecca", 1324, "Legendary journey that displayed the wealth of the Mali Empire")],
  [("I will build mosques and schools to spread knowledge.", "Attributed")])

p("sejong-the-great", "Sejong the Great", "世宗大王", 1397, 1450, ["kr"], ["politics"],
  "Sejong the Great was the fourth king of the Joseon dynasty of Korea who created the Korean alphabet Hangul and promoted science and culture.",
  "Sejong was born in Seoul. He ascended to the throne in 1418 and ruled during a golden age of Korean culture and scientific achievement.",
  "Sejong's creation of Hangul, one of the most scientific writing systems in the world, was his greatest achievement, enabling literacy for common Koreans.",
  [(1418, "Became King of Joseon"), (1432, "Established the Hall of Worthies"), (1443, "Created Hangul alphabet"), (1446, "Promulgated Hangul")],
  [("Hunminjeongeum", 1446, "Document introducing the Hangul alphabet to the Korean people")],
  [("A wise man creates what an ordinary man cannot even imagine.", "Attributed")])

p("haile-selassie", "Haile Selassie", "ハイレ・セラシエ", 1892, 1975, ["et"], ["politics"],
  "Haile Selassie was the Emperor of Ethiopia from 1930 to 1974, a major figure in African politics, and is revered as the messiah in the Rastafari movement.",
  "Born Tafari Makonnen in Ejersa Goro, Ethiopia, he rose through aristocratic ranks to become regent and then emperor.",
  "Selassie modernized Ethiopia, led resistance against Italian invasion, and was a founding figure of the Organization of African Unity. He became a symbol of African independence.",
  [(1930, "Crowned Emperor of Ethiopia"), (1936, "Appealed to League of Nations against Italian invasion"), (1941, "Restored to throne after liberation"), (1963, "Helped found the Organization of African Unity")],
  [("Address to the League of Nations", 1936, "Appeal against Italian aggression that became a landmark speech")],
  [("Until the philosophy which holds one race superior and another inferior is finally and permanently discredited and abandoned, there will be war.", "UN Address, 1963")])

# === MORE ENGINEERS ===
p("nikola-tesla-radio", "Lee De Forest", "リー・ド・フォレスト", 1873, 1961, ["us"], ["engineering"],
  "Lee De Forest was an American inventor who invented the Audion (triode vacuum tube), the foundation of electronic amplification.",
  "De Forest was born in Council Bluffs, Iowa. He studied at Yale and became a prolific inventor with over 300 patents.",
  "De Forest's triode vacuum tube enabled the amplification of electrical signals, making radio broadcasting, long-distance telephony, and early computers possible.",
  [(1906, "Invented the Audion (triode) vacuum tube"), (1910, "First radio broadcast from the Metropolitan Opera"), (1920, "Began work on talking motion pictures")],
  [("Audion Tube", 1906, "Triode vacuum tube that enabled electronic amplification")],
  [("I have discovered an invisible empire of the air.", "Attributed")])

p("vannevar-bush", "Vannevar Bush", "ヴァネヴァー・ブッシュ", 1890, 1974, ["us"], ["engineering"],
  "Vannevar Bush was an American engineer and science administrator who organized the scientific war effort during WWII and envisioned hypertext.",
  "Bush was born in Everett, Massachusetts. He studied at Tufts, Harvard, and MIT, becoming dean of engineering at MIT.",
  "Bush directed the U.S. Office of Scientific Research and Development during WWII. His essay 'As We May Think' envisioned hypertext and the World Wide Web decades before their creation.",
  [(1931, "Built the differential analyzer"), (1940, "Headed the National Defense Research Committee"), (1945, "Published 'As We May Think'")],
  [("As We May Think", 1945, "Essay proposing a machine for organizing knowledge, foreshadowing hypertext")],
  [("Science has a simple faith, which transcends utility.", "Attributed")])

p("jack-kilby", "Jack Kilby", "ジャック・キルビー", 1923, 2005, ["us"], ["engineering"],
  "Jack Kilby was an American electrical engineer who co-invented the integrated circuit, one of the most important innovations of the 20th century.",
  "Kilby was born in Jefferson City, Missouri. He studied at the University of Illinois and Wisconsin before joining Texas Instruments.",
  "Kilby's invention of the integrated circuit miniaturized electronics, enabling the computer revolution, smartphones, and the modern digital world.",
  [(1958, "Invented the integrated circuit at Texas Instruments"), (1967, "Invented the handheld calculator"), (2000, "Awarded Nobel Prize in Physics")],
  [("Integrated Circuit", 1958, "Miniaturized electronic circuit on a single semiconductor chip")],
  [("What we didn't realize then was that the integrated circuit would reduce the cost of electronic functions by a factor of a million to one.", "Nobel lecture")])

# === MORE BIOLOGISTS ===
p("alexander-von-humboldt-dup", "Alfred Wegener", "アルフレート・ヴェーゲナー", 1880, 1930, ["de"], ["biology", "astronomy"],
  "Alfred Wegener was a German meteorologist and geophysicist who proposed the theory of continental drift.",
  "Wegener was born in Berlin. He studied astronomy, meteorology, and physics, and participated in expeditions to Greenland.",
  "Wegener's theory of continental drift, initially ridiculed, was eventually vindicated by plate tectonics and revolutionized our understanding of Earth's history.",
  [(1912, "Proposed continental drift theory"), (1915, "Published The Origin of Continents and Oceans"), (1930, "Died on an expedition to Greenland")],
  [("The Origin of Continents and Oceans", 1915, "Book proposing that continents were once joined together")],
  [("Scientists still do not appear to understand sufficiently that all earth sciences must contribute evidence toward unveiling the state of our planet.", "Attributed")])

p("francis-collins", "Francis Collins", "フランシス・コリンズ", 1950, None, ["us"], ["biology"],
  "Francis Collins is an American physician-geneticist who led the Human Genome Project and later served as director of the National Institutes of Health.",
  "Collins was born in Staunton, Virginia. He studied at the University of Virginia and Yale, then led the Human Genome Project at the NIH.",
  "Collins led the successful completion of the Human Genome Project, mapping all human genes and opening the era of genomic medicine.",
  [(1993, "Became director of the Human Genome Project"), (2003, "Human Genome Project completed"), (2009, "Became director of the NIH")],
  [("Human Genome Project", 2003, "Complete mapping of all human genes")],
  [("The God of the Bible is also the God of the genome. He can be worshipped in the cathedral or in the laboratory.", "The Language of God")])

# === MORE CHEMISTS ===
p("ahmed-zewail-dup", "Linus Pauling's student Ahmed Hassan Zewail", "マリー・キュリーの後継者イレーヌ", 1900, 1980, ["fr"], ["chemistry"],
  "Frédéric Joliot-Curie was a French physicist who, with his wife Irène, received the Nobel Prize in Chemistry for the discovery of artificial radioactivity.",
  "Joliot was born in Paris. He studied at the École de Physique et Chimie and became an assistant to Marie Curie at the Radium Institute, where he met Irène Curie.",
  "The Joliot-Curies' discovery of artificial radioactivity opened the door to nuclear medicine and the production of radioactive isotopes for research and treatment.",
  [(1934, "Discovered artificial radioactivity with Irène"), (1935, "Awarded Nobel Prize in Chemistry"), (1939, "Demonstrated possibility of nuclear chain reactions")],
  [("Artificial Production of a New Kind of Radio-Element", 1934, "Paper announcing the creation of artificial radioactive isotopes")],
  [("Science for the service of humanity.", "Attributed")])

# === MORE ARTISTS ===
p("tamara-de-lempicka", "Tamara de Lempicka", "タマラ・ド・レンピッカ", 1898, 1980, ["pl", "us"], ["art"],
  "Tamara de Lempicka was a Polish painter who was the most prominent Art Deco painter, famous for her polished portraits of the wealthy and fashionable.",
  "De Lempicka was born in Warsaw, Poland. She fled the Russian Revolution and settled in Paris, where she became a leading Art Deco artist.",
  "De Lempicka's glamorous, highly stylized portraits defined Art Deco painting and captured the spirit of the 1920s and 1930s.",
  [(1925, "First major exhibition in Milan"), (1929, "Painted Autoportrait (Tamara in the Green Bugatti)"), (1939, "Moved to the United States")],
  [("Autoportrait", 1929, "Self-portrait on the cover of a German fashion magazine that became an icon of Art Deco")],
  [("I live life in the margins of society, and the rules of normal society don't apply to those who live on the fringe.", "Attributed")])

p("keith-haring", "Keith Haring", "キース・ヘリング", 1958, 1990, ["us"], ["art"],
  "Keith Haring was an American artist whose pop art and graffiti-like work grew out of the New York City street culture of the 1980s.",
  "Haring was born in Reading, Pennsylvania. He studied at the School of Visual Arts in New York and began drawing in the subway system.",
  "Haring's bold lines and active figures became internationally recognized symbols. His art addressed social issues including AIDS awareness, drugs, and apartheid.",
  [(1980, "Began subway chalk drawings"), (1982, "First solo exhibition"), (1986, "Opened Pop Shop in SoHo"), (1990, "Died of AIDS-related illness at age 31")],
  [("Crack Is Wack", 1986, "Public mural addressing the crack epidemic"), ("Subway Drawings", 1980, "Chalk drawings on blank subway advertising panels")],
  [("Art is for everybody.", "Attributed")])

p("louise-bourgeois", "Louise Bourgeois", "ルイーズ・ブルジョワ", 1911, 2010, ["fr", "us"], ["art"],
  "Louise Bourgeois was a French-American artist known for her large-scale sculpture and installation art, exploring themes of the body, memory, and the unconscious.",
  "Bourgeois was born in Paris. She studied mathematics and art before emigrating to New York in 1938, where she developed her distinctive sculptural practice.",
  "Bourgeois's monumental spider sculptures and psychologically charged installations made her one of the most important artists of the late 20th century.",
  [(1945, "First solo exhibition in New York"), (1982, "First woman to receive a retrospective at MoMA"), (1999, "Created Maman, the giant spider sculpture")],
  [("Maman", 1999, "Giant spider sculpture symbolizing motherhood and protection")],
  [("Art is a guarantee of sanity.", "Attributed")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'emmy-noether-dup-check':
            entry['id'] = 'sofia-kovalevskaya'
        elif entry['id'] == 'ramanujan-dup-check':
            entry['id'] = 'g-h-hardy'
        elif entry['id'] == 'alexander-von-humboldt-dup':
            entry['id'] = 'alfred-wegener'
        elif entry['id'] == 'ahmed-zewail-dup':
            entry['id'] = 'frederic-joliot-curie'
        elif entry['id'] == 'nikola-tesla-radio':
            entry['id'] = 'lee-de-forest'
    write_people(P)
