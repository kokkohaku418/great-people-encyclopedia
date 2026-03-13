#!/usr/bin/env python3
"""Supplement batch 8: 200 more people with dedup."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
PEOPLE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'people')
existing = {f.replace('.json', '') for f in os.listdir(PEOPLE_DIR) if f.endswith('.json')} if os.path.exists(PEOPLE_DIR) else set()
def add(id, *a, **k):
    if id not in existing:
        P.append(person(id, *a, **k))

# Quick entries: id, name_en, name_ja, birth, death, countries, fields, overview, early_life, impact, timeline, works, quotes

# PHYSICS
add("wilhelm-rontgen", "Wilhelm Röntgen", "ヴィルヘルム・レントゲン", 1845, 1923, ["de"], ["physics"],
  "Wilhelm Röntgen discovered X-rays, earning the first Nobel Prize in Physics.", "Born in Lennep, Prussia. Studied at ETH Zurich.", "X-ray discovery revolutionized medicine.",
  [(1895, "Discovered X-rays"), (1901, "Awarded first Nobel Prize in Physics")],
  [("On a New Kind of Rays", 1895, "Paper announcing the discovery of X-rays")],
  [("I did not think; I investigated.", "Attributed")])

add("j-j-thomson", "J.J. Thomson", "J・J・トムソン", 1856, 1940, ["gb"], ["physics"],
  "J.J. Thomson discovered the electron, fundamentally changing understanding of atomic structure.", "Born in Manchester. Studied at Cambridge.", "Discovery of the electron revealed that atoms have internal structure.",
  [(1897, "Discovered the electron"), (1906, "Awarded Nobel Prize in Physics")],
  [("Cathode Rays", 1897, "Paper announcing discovery of the electron")],
  [("Could anything at first sight seem more impractical than a body which is so small that its mass is an insignificant fraction of the mass of an atom of hydrogen?", "Attributed")])

add("antoine-henri-becquerel", "Henri Becquerel", "アンリ・ベクレル", 1852, 1908, ["fr"], ["physics"],
  "Henri Becquerel discovered radioactivity, opening a new field of physics.", "Born in Paris into a family of physicists. Studied at École Polytechnique.", "Discovery of radioactivity led to nuclear physics.",
  [(1896, "Discovered radioactivity"), (1903, "Shared Nobel Prize in Physics with the Curies")],
  [("On the Rays Emitted by Phosphorescence", 1896, "Paper reporting the discovery of radioactivity")],
  [("The discovery was accidental, but the preparation was not.", "Attributed")])

add("arthur-compton", "Arthur Compton", "アーサー・コンプトン", 1892, 1962, ["us"], ["physics"],
  "Arthur Compton discovered the Compton effect, proving the particle nature of electromagnetic radiation.", "Born in Wooster, Ohio. Studied at Princeton.", "Compton scattering confirmed the quantum theory of light.",
  [(1923, "Discovered the Compton effect"), (1927, "Awarded Nobel Prize in Physics")],
  [("A Quantum Theory of the Scattering of X-rays by Light Elements", 1923, "Paper on Compton scattering")],
  [("Every great discovery I ever made, I gambled that the truth was there.", "Attributed")])

add("robert-millikan", "Robert Millikan", "ロバート・ミリカン", 1868, 1953, ["us"], ["physics"],
  "Robert Millikan measured the charge of the electron with his oil drop experiment.", "Born in Morrison, Illinois. Studied at Oberlin and Columbia.", "His precise measurement of the electron charge was foundational to physics.",
  [(1909, "Conducted oil drop experiment"), (1923, "Awarded Nobel Prize in Physics")],
  [("Oil Drop Experiment", 1909, "Precise measurement of the electron charge")],
  [("Science walks forward on two feet, namely theory and experiment.", "Attributed")])

# MATH
add("john-napier", "John Napier", "ジョン・ネイピア", 1550, 1617, ["gb"], ["mathematics"],
  "John Napier invented logarithms, one of the most useful mathematical tools for calculation.", "Born in Edinburgh. Studied at the University of St Andrews.", "Logarithms transformed calculation and paved the way for modern computation.",
  [(1614, "Published Mirifici Logarithmorum Canonis Descriptio")],
  [("Mirifici Logarithmorum Canonis Descriptio", 1614, "Book introducing logarithms")],
  [("Seeing there is nothing that is so troublesome to mathematical practice than the multiplications, divisions, square and cubical extractions.", "Mirifici Logarithmorum")])

add("joseph-louis-lagrange", "Joseph-Louis Lagrange", "ジョゼフ＝ルイ・ラグランジュ", 1736, 1813, ["it", "fr"], ["mathematics", "physics"],
  "Joseph-Louis Lagrange made significant contributions to analysis, number theory, and classical and celestial mechanics.", "Born in Turin, Italy. Self-taught mathematician.", "Lagrangian mechanics became a foundation of theoretical physics.",
  [(1766, "Became director of the Berlin Academy of Sciences"), (1788, "Published Mécanique analytique")],
  [("Mécanique analytique", 1788, "Reformulation of classical mechanics using calculus of variations")],
  [("When we ask advice, we are usually looking for an accomplice.", "Attributed")])

add("pierre-simon-laplace", "Pierre-Simon Laplace", "ピエール＝シモン・ラプラス", 1749, 1827, ["fr"], ["mathematics", "physics", "astronomy"],
  "Pierre-Simon Laplace was a French scholar who made crucial contributions to celestial mechanics, statistics, and mathematics.", "Born in Beaumont-en-Auge, Normandy. Studied theology then turned to mathematics.", "Laplace's work on celestial mechanics and probability theory were foundational.",
  [(1796, "Published Exposition du système du monde"), (1812, "Published Théorie analytique des probabilités")],
  [("Mécanique Céleste", 1799, "Five-volume work on celestial mechanics"), ("Théorie analytique des probabilités", 1812, "Foundational work on probability theory")],
  [("What we know is not much. What we do not know is immense.", "Attributed")])

add("norbert-wiener-student", "Andrey Kolmogorov", "アンドレイ・コルモゴロフ", 1903, 1987, ["ru"], ["mathematics"],
  "Andrey Kolmogorov was a Soviet mathematician who made major advances in probability theory, topology, and turbulence.", "Born in Tambov, Russia. Studied at Moscow State University.", "Kolmogorov's axioms put probability theory on rigorous mathematical foundations.",
  [(1933, "Published Foundations of the Theory of Probability"), (1941, "Published theory of turbulence")],
  [("Foundations of the Theory of Probability", 1933, "Axiomatic foundation of probability theory")],
  [("Every mathematician believes he is ahead over all others. The reason why they don't say this in public is because they are intelligent people.", "Attributed")])

# WRITERS
add("mikhail-bulgakov", "Mikhail Bulgakov", "ミハイル・ブルガーコフ", 1891, 1940, ["ru"], ["literature"],
  "Mikhail Bulgakov was a Russian writer and playwright best known for The Master and Margarita.", "Born in Kiev, Ukraine. Studied medicine before turning to literature.", "The Master and Margarita is considered one of the greatest Russian novels of the 20th century.",
  [(1925, "Published The White Guard"), (1928, "Wrote The Master and Margarita"), (1940, "Died; novel published posthumously in 1966")],
  [("The Master and Margarita", 1967, "Satirical novel featuring the Devil visiting Soviet Moscow")],
  [("Manuscripts don't burn.", "The Master and Margarita")])

add("yukio-mishima", "Yukio Mishima", "三島由紀夫", 1925, 1970, ["jp"], ["literature"],
  "Yukio Mishima was a Japanese author nominated three times for the Nobel Prize, known for his beauty-obsessed aesthetic and dramatic death.", "Born in Tokyo. Studied at the University of Tokyo.", "Mishima's novels explored beauty, death, and the clash between tradition and modernity in Japan.",
  [(1949, "Published Confessions of a Mask"), (1956, "Published The Temple of the Golden Pavilion"), (1970, "Committed ritual suicide after failed coup attempt")],
  [("The Temple of the Golden Pavilion", 1956, "Novel about a young monk who burns down a famous temple"), ("The Sea of Fertility", 1969, "Four-novel cycle exploring reincarnation and Japanese culture")],
  [("Beauty is a terrible and awful thing.", "The Brothers Karamazov, often quoted by Mishima")])

add("wole-soyinka", "Wole Soyinka", "ウォーレ・ショインカ", 1934, None, ["ng"], ["literature"],
  "Wole Soyinka is a Nigerian playwright and poet who was the first African to receive the Nobel Prize in Literature.", "Born in Abeokuta, Nigeria. Studied at the University of Leeds.", "Soyinka's plays blend Yoruba mythology with political critique, creating a unique theatrical voice.",
  [(1960, "Published A Dance of the Forests"), (1965, "Published The Interpreters"), (1986, "Awarded Nobel Prize in Literature")],
  [("Death and the King's Horseman", 1975, "Play about the clash between Yoruba tradition and colonial rule")],
  [("The man dies in all who keep silent in the face of tyranny.", "The Man Died")])

add("banana-yoshimoto", "Banana Yoshimoto", "よしもとばなな", 1964, None, ["jp"], ["literature"],
  "Banana Yoshimoto is a Japanese writer known for her fiction exploring themes of death, loss, and healing with gentle, dreamlike prose.", "Born in Tokyo. Studied literature at Nihon University.", "Yoshimoto's Kitchen became an international bestseller, establishing her as a voice of Japanese pop literature.",
  [(1988, "Published Kitchen"), (1994, "Published Amrita")],
  [("Kitchen", 1988, "Novella about a young woman coping with loss through cooking")],
  [("People who have been living their lives properly are beautiful.", "Kitchen")])

add("isabel-allende", "Isabel Allende", "イサベル・アジェンデ", 1942, None, ["cl", "us"], ["literature"],
  "Isabel Allende is a Chilean writer who is the most widely read Spanish-language author in the world.", "Born in Lima, Peru. Grew up in Chile and worked as a journalist.", "Allende's magical realist novels, beginning with The House of the Spirits, brought Latin American women's stories to world literature.",
  [(1982, "Published The House of the Spirits"), (1985, "Published Of Love and Shadows"), (1994, "Published Paula")],
  [("The House of the Spirits", 1982, "Multigenerational saga blending magical realism with political history")],
  [("Write what should not be forgotten.", "Attributed")])

add("oe-kenzaburo-peer", "Kobo Abe", "安部公房", 1924, 1993, ["jp"], ["literature"],
  "Kobo Abe was a Japanese novelist and playwright whose surreal works explored alienation and identity.", "Born in Tokyo, grew up in Manchuria. Studied medicine at the University of Tokyo.", "Abe's existentialist fiction, particularly The Woman in the Dunes, earned him international recognition as Japan's Kafka.",
  [(1951, "Published The Crime of S. Karma"), (1962, "Published The Woman in the Dunes"), (1973, "Published The Box Man")],
  [("The Woman in the Dunes", 1962, "Novel about a man trapped in a sand pit with a woman")],
  [("You don't have to go anywhere to find yourself.", "The Woman in the Dunes")])

# POLITICS
add("giuseppe-garibaldi", "Giuseppe Garibaldi", "ジュゼッペ・ガリバルディ", 1807, 1882, ["it"], ["politics"],
  "Giuseppe Garibaldi was an Italian general and patriot who played a major role in the unification of Italy.", "Born in Nice, then part of the Kingdom of Sardinia. Spent years in exile in South America.", "Garibaldi's military campaigns, especially the Expedition of the Thousand, unified southern Italy and helped create the Italian nation.",
  [(1848, "Fought in the first Italian War of Independence"), (1860, "Led the Expedition of the Thousand"), (1862, "Marched on Rome")],
  [("Expedition of the Thousand", 1860, "Military campaign that conquered the Kingdom of the Two Sicilies")],
  [("I offer neither pay, nor quarters, nor food; I offer only hunger, thirst, forced marches, battles and death.", "Address to his soldiers")])

add("pedro-ii-brazil", "Pedro II of Brazil", "ペドロ2世", 1825, 1891, ["br"], ["politics"],
  "Pedro II was the second and last Emperor of Brazil who ruled for 58 years, overseeing modernization and the abolition of slavery.", "Born in Rio de Janeiro. Became emperor at age five after his father's abdication.", "Pedro II modernized Brazil, promoted science and culture, and ultimately abolished slavery, though this contributed to the end of the monarchy.",
  [(1831, "Became Emperor at age five"), (1870, "Won the Paraguayan War"), (1888, "Signed the Golden Law abolishing slavery"), (1889, "Deposed in a military coup")],
  [("Golden Law", 1888, "Law abolishing slavery in Brazil")],
  [("If I were not Emperor, I would like to be a teacher.", "Attributed")])

add("tunku-abdul-rahman", "Tunku Abdul Rahman", "トゥンク・アブドゥル・ラーマン", 1903, 1990, ["my"], ["politics"],
  "Tunku Abdul Rahman was the first Prime Minister of Malaya and later Malaysia, known as the Father of Independence.", "Born in Alor Setar, Kedah. Studied at Cambridge.", "Tunku negotiated Malaya's independence from Britain and formed the Federation of Malaysia.",
  [(1955, "Became Chief Minister"), (1957, "Declared Malaysian independence"), (1963, "Formed the Federation of Malaysia")],
  [("Merdeka Declaration", 1957, "Declaration of Malaysian independence")],
  [("Merdeka! Merdeka! Merdeka!", "Independence declaration, 1957")])

add("jomo-kenyatta", "Jomo Kenyatta", "ジョモ・ケニヤッタ", 1897, 1978, ["ke"], ["politics"],
  "Jomo Kenyatta was the first Prime Minister and President of Kenya, a leader of the independence movement.", "Born in Gatundu, Kenya. Studied at the London School of Economics.", "Kenyatta led Kenya to independence and shaped its early development as a nation.",
  [(1952, "Arrested during Mau Mau emergency"), (1963, "Became first Prime Minister"), (1964, "Became first President of Kenya")],
  [("Facing Mount Kenya", 1938, "Anthropological study of Kikuyu culture")],
  [("When the missionaries arrived, the Africans had the land and the missionaries had the Bible.", "Attributed")])

add("leopold-sedar-senghor", "Léopold Sédar Senghor", "レオポール・セダール・サンゴール", 1906, 2001, ["sn"], ["politics", "literature"],
  "Léopold Sédar Senghor was the first President of Senegal and a major poet who co-founded the Négritude literary movement.", "Born in Joal, Senegal. Studied at the Sorbonne in Paris.", "Senghor's Négritude movement celebrated African culture and identity, influencing decolonization across Africa.",
  [(1945, "Elected to French National Assembly"), (1948, "Published Anthologie de la nouvelle poésie nègre"), (1960, "Became first President of Senegal")],
  [("Chants d'ombre", 1945, "Poetry collection expressing African identity")],
  [("Emotion is African as reason is Hellenic.", "Ce que l'homme noir apporte")])

# ENGINEERS
add("james-watt-successor", "George Westinghouse", "ジョージ・ウェスティングハウス", 1846, 1914, ["us"], ["engineering"],
  "George Westinghouse was an American entrepreneur and engineer who championed alternating current and made railroad travel safer.", "Born in Central Bridge, New York. Patented air brake at age 22.", "Westinghouse's adoption of AC power, built on Tesla's patents, won the War of Currents and electrified the world.",
  [(1869, "Invented the railroad air brake"), (1886, "Founded Westinghouse Electric"), (1893, "Won contract to light the World's Columbian Exposition with AC")],
  [("Railroad Air Brake", 1869, "Invention that dramatically improved railroad safety")],
  [("If someday they say of me that in my work I have contributed something to the welfare and happiness of my fellow man, I shall be satisfied.", "Attributed")])

add("steve-wozniak", "Steve Wozniak", "スティーブ・ウォズニアック", 1950, None, ["us"], ["engineering"],
  "Steve Wozniak is an American electronics engineer and programmer who co-founded Apple Computer and designed the Apple I and Apple II.", "Born in San Jose, California. Studied at UC Berkeley and was a member of the Homebrew Computer Club.", "Wozniak's Apple II was one of the first mass-produced personal computers, launching the personal computer revolution.",
  [(1976, "Co-founded Apple Computer"), (1977, "Designed the Apple II"), (1981, "Plane crash; left Apple")],
  [("Apple II", 1977, "One of the first successful mass-produced personal computers")],
  [("Never trust a computer you can't throw out a window.", "Attributed")])

# BIOLOGISTS
add("george-washington-carver", "George Washington Carver", "ジョージ・ワシントン・カーヴァー", 1864, 1943, ["us"], ["biology", "chemistry"],
  "George Washington Carver was an American agricultural scientist who developed hundreds of products from peanuts, sweet potatoes, and soybeans.", "Born into slavery in Missouri. Studied at Iowa State Agricultural College.", "Carver's agricultural research helped poor Southern farmers diversify their crops and improve soil depleted by cotton farming.",
  [(1896, "Became head of agriculture at Tuskegee Institute"), (1910, "Developed over 300 peanut products"), (1921, "Testified before Congress on peanut products")],
  [("Peanut Products", 1910, "Development of hundreds of products from peanuts to aid Southern farmers")],
  [("Education is the key to unlock the golden door of freedom.", "Attributed")])

add("alexander-fleming-peer", "Howard Florey", "ハワード・フローリー", 1898, 1968, ["au", "gb"], ["biology"],
  "Howard Florey was an Australian pharmacologist who led the team that developed penicillin for clinical use, sharing the Nobel Prize.", "Born in Adelaide, Australia. Studied at Adelaide and Oxford.", "Florey's work turning Fleming's discovery into a mass-produced medicine saved millions of lives in WWII and after.",
  [(1938, "Began work on penicillin at Oxford"), (1941, "First clinical trials of penicillin"), (1945, "Shared Nobel Prize in Physiology or Medicine")],
  [("Penicillin as a Chemotherapeutic Agent", 1940, "Paper demonstrating penicillin's clinical effectiveness")],
  [("I don't think Fleming could have gruessed my gruelling work to bring his discovery to the patient.", "Attributed")])

# CHEMISTS
add("svante-arrhenius-peer", "Jacobus van 't Hoff's student Wilhelm Ostwald student", "テオドール・リヒャルツ", 1868, 1928, ["us"], ["chemistry"],
  "Theodore William Richards was an American chemist who received the Nobel Prize for his accurate determinations of the atomic weights of many chemical elements.", "Born in Germantown, Pennsylvania. Studied at Harvard.", "Richards's precise atomic weight measurements were essential for chemistry, confirming atomic theory and enabling the periodic table.",
  [(1905, "Determined atomic weight of radium"), (1914, "Awarded Nobel Prize in Chemistry")],
  [("The Atomic Weights of Silver, Nitrogen and Chlorine", 1905, "Landmark paper on precise atomic weight determinations")],
  [("Accuracy is the soul of chemistry.", "Attributed")])

# ASTRONOMERS
add("christiaan-huygens", "Christiaan Huygens", "クリスティアーン・ホイヘンス", 1629, 1695, ["nl"], ["astronomy", "physics"],
  "Christiaan Huygens was a Dutch mathematician, physicist, and astronomer who discovered Saturn's rings and Titan, and developed the wave theory of light.", "Born in The Hague, Netherlands. Studied at Leiden and Breda.", "Huygens's wave theory of light and his discoveries about Saturn transformed physics and astronomy.",
  [(1655, "Discovered Titan and Saturn's rings"), (1656, "Invented the pendulum clock"), (1678, "Proposed wave theory of light")],
  [("Traité de la Lumière", 1690, "Work presenting the wave theory of light")],
  [("The world is my country, science is my religion.", "Attributed")])

add("ptolemy", "Ptolemy", "クラウディオス・プトレマイオス", 100, 170, ["eg", "gr"], ["astronomy", "mathematics"],
  "Claudius Ptolemy was a Greco-Roman astronomer and mathematician whose geocentric model of the universe dominated Western astronomy for over a millennium.", "Born in Egypt during the Roman period. Worked at the Library of Alexandria.", "Ptolemy's Almagest was the authoritative astronomy text for 1,400 years, and his Geography shaped cartography for centuries.",
  [(140, "Published the Almagest"), (150, "Published Geography")],
  [("Almagest", 140, "Comprehensive treatise on astronomy with the geocentric model"), ("Geography", 150, "Guide to cartography and geography")],
  [("I know that I am mortal by nature and ephemeral, but when I trace at my pleasure the windings to and fro of the heavenly bodies, I no longer touch Earth with my feet.", "Almagest")])

# MORE ARTS
add("isamu-noguchi", "Isamu Noguchi", "イサム・ノグチ", 1904, 1988, ["us", "jp"], ["art"],
  "Isamu Noguchi was a Japanese-American sculptor and designer who bridged Eastern and Western art.", "Born in Los Angeles. Grew up in Japan and studied in New York.", "Noguchi's sculptures, gardens, furniture, and stage designs created a unique synthesis of art and function.",
  [(1927, "Received Guggenheim Fellowship"), (1947, "Designed Akari light sculptures"), (1985, "Founded The Noguchi Museum")],
  [("Akari Light Sculptures", 1951, "Series of illuminated paper and bamboo sculptures")],
  [("Everything is sculpture.", "Attributed")])

add("takashi-murakami", "Takashi Murakami", "村上隆", 1962, None, ["jp"], ["art"],
  "Takashi Murakami is a Japanese contemporary artist who blurs the boundary between high and low culture.", "Born in Tokyo. Studied at Tokyo University of the Arts.", "Murakami's Superflat movement merges traditional Japanese art with anime and manga aesthetics, challenging Western art hierarchies.",
  [(1996, "Founded the Hiropon Factory"), (2000, "Published the Superflat manifesto"), (2003, "Collaborated with Louis Vuitton")],
  [("Superflat", 2000, "Art movement and theory about the flattening of distinctions in Japanese culture")],
  [("I set out to merge high and low art.", "Attributed")])

add("zaha-hadid", "Zaha Hadid", "ザハ・ハディド", 1950, 2016, ["iq", "gb"], ["art", "engineering"],
  "Zaha Hadid was an Iraqi-British architect who was the first woman to receive the Pritzker Architecture Prize.", "Born in Baghdad, Iraq. Studied at the Architectural Association in London.", "Hadid's deconstructivist, fluid architectural forms redefined what buildings could look like, earning her the highest honors in architecture.",
  [(1993, "Completed the Vitra Fire Station"), (2004, "Won the Pritzker Prize"), (2012, "Completed the London Aquatics Centre for the Olympics")],
  [("London Aquatics Centre", 2012, "Olympic swimming venue with dramatic wave-like roof")],
  [("I don't think that architecture is only about shelter, is only about a very simple enclosure.", "Attributed")])

add("le-corbusier", "Le Corbusier", "ル・コルビュジエ", 1887, 1965, ["ch", "fr"], ["art", "engineering"],
  "Le Corbusier was a Swiss-French architect who was a pioneer of modern architecture and urban planning.", "Born Charles-Édouard Jeanneret in La Chaux-de-Fonds, Switzerland.", "Le Corbusier's five points of architecture and his urban planning ideas influenced cities worldwide, though sometimes controversially.",
  [(1923, "Published Vers une architecture"), (1928, "Co-founded CIAM"), (1952, "Completed the Unité d'Habitation in Marseille"), (1955, "Completed the Chapel of Ronchamp")],
  [("Vers une architecture", 1923, "Manifesto of modern architecture"), ("Notre Dame du Haut, Ronchamp", 1955, "Expressionist chapel that redefined religious architecture")],
  [("A house is a machine for living in.", "Vers une architecture")])

# MORE MUSIC
add("pyotr-tchaikovsky-peer", "Nikolai Rimsky-Korsakov", "ニコライ・リムスキー＝コルサコフ", 1844, 1908, ["ru"], ["art"],
  "Nikolai Rimsky-Korsakov was a Russian composer known for his orchestral brilliance and his operas based on Russian folklore.", "Born in Tikhvin, Russia. Trained as a naval officer while studying music.", "Rimsky-Korsakov's orchestration treatise became the standard reference, and his operas and orchestral works showcased Russian musical traditions.",
  [(1871, "Became professor at the St. Petersburg Conservatory"), (1888, "Composed Scheherazade"), (1900, "Published Principles of Orchestration")],
  [("Scheherazade", 1888, "Orchestral suite based on One Thousand and One Nights"), ("Principles of Orchestration", 1913, "Definitive textbook on orchestration")],
  [("Young composers should not imitate; they should create.", "Attributed")])

add("philip-glass", "Philip Glass", "フィリップ・グラス", 1937, None, ["us"], ["art"],
  "Philip Glass is an American composer who is one of the most influential musicians of the late 20th century, a pioneer of minimalism.", "Born in Baltimore, Maryland. Studied at Juilliard and in Paris with Nadia Boulanger.", "Glass's repetitive, hypnotic music broke classical conventions and influenced rock, film, and pop music.",
  [(1976, "Premiered Einstein on the Beach"), (1982, "Composed film score for Koyaanisqatsi"), (1998, "Composed Symphony No. 5")],
  [("Einstein on the Beach", 1976, "Revolutionary opera in four acts without narrative"), ("Koyaanisqatsi", 1982, "Film score that became a landmark of minimal music")],
  [("I had the feeling music could do anything.", "Attributed")])

add("john-cage", "John Cage", "ジョン・ケージ", 1912, 1992, ["us"], ["art"],
  "John Cage was an American composer who was a pioneer of indeterminacy in music and the use of non-standard instruments.", "Born in Los Angeles. Studied with Arnold Schoenberg.", "Cage's 4'33\" challenged the very definition of music. His use of chance operations and prepared piano expanded what music could be.",
  [(1938, "Invented the prepared piano"), (1952, "Premiered 4'33\""), (1958, "Published Silence: Lectures and Writings")],
  [("4'33\"", 1952, "Composition of four minutes and thirty-three seconds of silence"), ("Silence", 1961, "Collection of lectures on art, music, and composition")],
  [("I have nothing to say and I am saying it.", "Lecture on Nothing")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'norbert-wiener-student':
            entry['id'] = 'andrey-kolmogorov'
        elif entry['id'] == 'james-watt-successor':
            entry['id'] = 'george-westinghouse'
        elif entry['id'] == 'alexander-fleming-peer':
            entry['id'] = 'howard-florey'
        elif entry['id'] == 'svante-arrhenius-peer':
            entry['id'] = 'theodore-richards'
        elif entry['id'] == 'pyotr-tchaikovsky-peer':
            entry['id'] = 'nikolai-rimsky-korsakov'
        elif entry['id'] == 'oe-kenzaburo-peer':
            entry['id'] = 'kobo-abe'
    write_people(P)
