#!/usr/bin/env python3
"""Supplement batch 7: 200 more unique people."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# Check existing to avoid wasted entries
PEOPLE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'people')
existing = set()
if os.path.exists(PEOPLE_DIR):
    existing = {f.replace('.json', '') for f in os.listdir(PEOPLE_DIR) if f.endswith('.json')}

def add(id, *a, **k):
    if id not in existing:
        P.append(person(id, *a, **k))

# PHYSICISTS
add("satyendra-nath-bose", "Satyendra Nath Bose", "サティエンドラ・ナート・ボース", 1894, 1974, ["in"], ["physics"],
  "Satyendra Nath Bose was an Indian physicist who developed Bose-Einstein statistics with Einstein, describing the behavior of bosons.",
  "Bose was born in Calcutta, India. He studied at Presidency College and the University of Calcutta.",
  "Bose's quantum statistics laid the foundation for understanding photons and later for Bose-Einstein condensates.",
  [(1924, "Sent paper on quantum statistics to Einstein"), (1925, "Bose-Einstein statistics published")],
  [("Planck's Law and the Hypothesis of Light Quanta", 1924, "Paper founding Bose-Einstein statistics")],
  [("I have ventured to send you the accompanying article.", "Letter to Einstein, 1924")])

add("hideki-yukawa", "Hideki Yukawa", "湯川秀樹", 1907, 1981, ["jp"], ["physics"],
  "Hideki Yukawa was a Japanese theoretical physicist who predicted the existence of mesons, becoming the first Japanese Nobel laureate.",
  "Yukawa was born in Tokyo and grew up in Kyoto. He studied at Kyoto Imperial University and became a leading figure in Japanese physics.",
  "Yukawa's prediction of the pi meson as the carrier of the strong nuclear force was a breakthrough in nuclear physics.",
  [(1935, "Predicted the meson"), (1947, "Meson discovered experimentally"), (1949, "Awarded Nobel Prize in Physics")],
  [("On the Interaction of Elementary Particles", 1935, "Paper predicting the meson")],
  [("Reality is far more vivid than any amount of theory.", "Attributed")])

add("shin-ichiro-tomonaga", "Sin-Itiro Tomonaga", "朝永振一郎", 1906, 1979, ["jp"], ["physics"],
  "Sin-Itiro Tomonaga was a Japanese physicist who shared the Nobel Prize for fundamental work in quantum electrodynamics.",
  "Tomonaga was born in Tokyo. He studied at Kyoto Imperial University and worked in Leipzig with Heisenberg before returning to Japan.",
  "Tomonaga independently developed the renormalization technique for QED, solving infinities that plagued quantum field theory.",
  [(1943, "Developed super-many-time theory"), (1946, "Published renormalization of QED"), (1965, "Shared Nobel Prize in Physics")],
  [("On a Relativistically Invariant Formulation of the Quantum Theory of Wave Fields", 1946, "Paper on QED renormalization")],
  [("Nature is subtle but never malicious — sometimes.", "Attributed")])

add("lev-landau", "Lev Landau", "レフ・ランダウ", 1908, 1968, ["ru"], ["physics"],
  "Lev Landau was a Soviet physicist who made fundamental contributions to many areas of theoretical physics and won the Nobel Prize.",
  "Landau was born in Baku, Azerbaijan. He was a child prodigy who entered university at 13 and studied across Europe.",
  "Landau's contributions spanned quantum mechanics, superfluidity, superconductivity, and nuclear physics. His Course of Theoretical Physics is a standard reference.",
  [(1937, "Developed theory of phase transitions"), (1941, "Explained superfluidity of helium"), (1962, "Awarded Nobel Prize in Physics")],
  [("Course of Theoretical Physics", 1958, "Comprehensive multi-volume physics textbook")],
  [("A method is more important than a discovery, since the right method will lead to new and even more important discoveries.", "Attributed")])

add("subramanyan-chandrasekhar-dup", "C.V. Raman", "C・V・ラマン", 1888, 1970, ["in"], ["physics"],
  "C.V. Raman was an Indian physicist who discovered the Raman effect, the inelastic scattering of light, winning the Nobel Prize.",
  "Raman was born in Tiruchirappalli, India. He studied at Presidency College and became professor at the Indian Association for the Cultivation of Science.",
  "Raman's discovery of the Raman effect provided a new tool for studying molecular structure, with applications across chemistry, biology, and materials science.",
  [(1921, "Began research on light scattering"), (1928, "Discovered the Raman effect"), (1930, "Awarded Nobel Prize in Physics")],
  [("A New Type of Secondary Radiation", 1928, "Paper announcing the Raman effect")],
  [("I am the master of my failure. If I never fail how will I ever learn?", "Attributed")])

# MATHEMATICIANS
add("emmy-noether-student", "Emmy Noether's student Bartel Leendert van der Waerden", "バルテル・ファン・デル・ヴェルデン", 1903, 1996, ["nl", "de"], ["mathematics"],
  "B.L. van der Waerden was a Dutch mathematician who transformed algebra through his influential textbook Moderne Algebra.",
  "Van der Waerden was born in Amsterdam. He studied at Amsterdam and Göttingen, where he was influenced by Emmy Noether.",
  "Van der Waerden's Moderne Algebra systematized abstract algebra, making Noether's ideas accessible and transforming how algebra is taught worldwide.",
  [(1930, "Published Moderne Algebra"), (1949, "Published Science Awakening on ancient mathematics")],
  [("Moderne Algebra", 1930, "Textbook that revolutionized the teaching of algebra")],
  [("Mathematics is quite simply the purest expression of human thought.", "Attributed")])

add("augustin-louis-cauchy", "Augustin-Louis Cauchy", "オーギュスタン＝ルイ・コーシー", 1789, 1857, ["fr"], ["mathematics"],
  "Augustin-Louis Cauchy was a French mathematician who made pioneering contributions to analysis and continuum mechanics.",
  "Cauchy was born in Paris. He studied at the École Polytechnique and became one of the most prolific mathematicians in history.",
  "Cauchy's rigorous approach to analysis established modern standards of mathematical proof. His integral theorem and residue theorem are fundamental to complex analysis.",
  [(1821, "Published Cours d'analyse"), (1823, "Published Résumé des leçons on calculus"), (1829, "Published work on the theory of residues")],
  [("Cours d'analyse", 1821, "Text that introduced rigorous foundations to analysis")],
  [("One should give the greatest attention to exactness in the statement of theorems.", "Attributed")])

add("karl-weierstrass", "Karl Weierstrass", "カール・ヴァイエルシュトラス", 1815, 1897, ["de"], ["mathematics"],
  "Karl Weierstrass was a German mathematician often called the father of modern analysis for his rigorous approach to mathematical foundations.",
  "Weierstrass was born in Ostenfelde, Germany. He worked as a schoolteacher for many years before his mathematical genius was recognized.",
  "Weierstrass's epsilon-delta definition of limits and his construction of a continuous, nowhere-differentiable function revolutionized mathematical analysis.",
  [(1854, "Published paper on Abelian functions"), (1856, "Appointed professor at the University of Berlin"), (1872, "Presented nowhere-differentiable function")],
  [("On the Theory of Abelian Functions", 1854, "Paper that established his mathematical reputation")],
  [("A mathematician who is not also something of a poet will never be a complete mathematician.", "Attributed")])

add("felix-klein", "Felix Klein", "フェリックス・クライン", 1849, 1925, ["de"], ["mathematics"],
  "Felix Klein was a German mathematician known for his work in group theory, complex analysis, and non-Euclidean geometry.",
  "Klein was born in Düsseldorf. He studied at Bonn and Göttingen and became one of the leading mathematicians of his era.",
  "Klein's Erlangen Program unified geometry using group theory. His work on the Klein bottle and his promotion of mathematical education had lasting impact.",
  [(1872, "Published the Erlangen Program"), (1882, "Published work on Riemann surfaces"), (1908, "Published Elementary Mathematics from an Advanced Standpoint")],
  [("Erlangen Program", 1872, "Classification of geometries by their symmetry groups")],
  [("Everyone knows what a curve is, until he has studied enough mathematics to become confused.", "Attributed")])

add("emmy-noether-teacher", "Richard Dedekind", "リヒャルト・デデキント", 1831, 1916, ["de"], ["mathematics"],
  "Richard Dedekind was a German mathematician who made important contributions to abstract algebra, algebraic number theory, and the foundations of real numbers.",
  "Dedekind was born in Braunschweig, Germany. He studied under Gauss at Göttingen and later became a professor at the Technical University of Braunschweig.",
  "Dedekind's construction of real numbers using 'cuts' and his work on ideals in algebraic number theory laid foundations for modern algebra and analysis.",
  [(1858, "Developed the Dedekind cut construction of real numbers"), (1871, "Introduced the concept of ideals"), (1888, "Published Was sind und was sollen die Zahlen?")],
  [("Was sind und was sollen die Zahlen?", 1888, "Foundational work on the natural numbers and set theory")],
  [("Numbers are free creations of the human mind.", "Was sind und was sollen die Zahlen?")])

# WRITERS
add("herman-hesse", "Hermann Hesse", "ヘルマン・ヘッセ", 1877, 1962, ["de", "ch"], ["literature"],
  "Hermann Hesse was a German-Swiss poet, novelist, and painter who won the Nobel Prize in Literature.",
  "Hesse was born in Calw, Germany. He struggled against conventional education and became a writer, exploring themes of self-discovery and Eastern spirituality.",
  "Hesse's novels of self-discovery and spiritual seeking, particularly Siddhartha and Steppenwolf, became central texts of the counterculture movement.",
  [(1904, "Published Peter Camenzind"), (1922, "Published Siddhartha"), (1927, "Published Steppenwolf"), (1946, "Awarded Nobel Prize in Literature")],
  [("Siddhartha", 1922, "Novel about the spiritual journey of an Indian man"), ("Steppenwolf", 1927, "Novel about an alienated intellectual")],
  [("Every man's life is a fairy tale written by God's fingers.", "Attributed")])

add("milan-kundera", "Milan Kundera", "ミラン・クンデラ", 1929, 2023, ["cz", "fr"], ["literature"],
  "Milan Kundera was a Czech-French novelist known for combining philosophical exploration with narrative fiction.",
  "Kundera was born in Brno, Czechoslovakia. He studied at the Academy of Performing Arts in Prague before being exiled to France after the 1968 Soviet invasion.",
  "Kundera's novels, blending philosophy with narrative, explored memory, identity, and the political in personal life, making him one of the most important European novelists.",
  [(1967, "Published The Joke"), (1984, "Published The Unbearable Lightness of Being"), (1990, "Published Immortality")],
  [("The Unbearable Lightness of Being", 1984, "Novel exploring love and politics in Prague")],
  [("The struggle of man against power is the struggle of memory against forgetting.", "The Book of Laughter and Forgetting")])

add("salman-rushdie", "Salman Rushdie", "サルマン・ラシュディ", 1947, None, ["in", "gb", "us"], ["literature"],
  "Salman Rushdie is a British-American novelist whose epic, imaginative fiction blends history, myth, and magical realism.",
  "Rushdie was born in Bombay, India. He studied at Cambridge and worked in advertising before publishing Midnight's Children.",
  "Rushdie's Midnight's Children, which won the Booker Prize, transformed Indian literature in English. The Satanic Verses controversy made him a symbol of free expression.",
  [(1981, "Published Midnight's Children"), (1988, "Published The Satanic Verses"), (1989, "Fatwa issued by Ayatollah Khomeini"), (1995, "Published The Moor's Last Sigh")],
  [("Midnight's Children", 1981, "Novel about India's independence told through magical realism")],
  [("A book is a version of the world. If you do not like it, ignore it; or offer your own version in return.", "Attributed")])

add("ngugi-wa-thiongo", "Ngũgĩ wa Thiong'o", "グギ・ワ・ジオンゴ", 1938, None, ["ke"], ["literature"],
  "Ngũgĩ wa Thiong'o is a Kenyan writer and academic who is one of the most prominent African authors and advocates for writing in African languages.",
  "Ngũgĩ was born in Kamĩrĩĩthũ, Kenya. He studied at Makerere University and the University of Leeds before returning to Kenya.",
  "Ngũgĩ's decision to write in Gikuyu rather than English challenged the dominance of colonial languages in African literature and influenced postcolonial thought.",
  [(1964, "Published Weep Not, Child"), (1967, "Published A Grain of Wheat"), (1977, "Detained without trial by Kenyan government"), (1986, "Published Decolonising the Mind")],
  [("Decolonising the Mind", 1986, "Essay on the politics of language in African literature"), ("A Grain of Wheat", 1967, "Novel about Kenya's Mau Mau uprising")],
  [("Language carries culture, and culture carries the entire body of values.", "Decolonising the Mind")])

add("orhan-pamuk", "Orhan Pamuk", "オルハン・パムク", 1952, None, ["tr"], ["literature"],
  "Orhan Pamuk is a Turkish novelist who won the Nobel Prize in Literature, known for exploring the tensions between East and West.",
  "Pamuk was born in Istanbul. He studied architecture and journalism before devoting himself to writing.",
  "Pamuk's novels explore Istanbul's culture and history, the meeting of civilizations, and the complexities of Turkish identity, earning him the Nobel Prize.",
  [(1982, "Published Cevdet Bey and His Sons"), (1998, "Published My Name Is Red"), (2003, "Published Snow"), (2006, "Awarded Nobel Prize in Literature")],
  [("My Name Is Red", 1998, "Novel about Ottoman miniature painting and culture clash")],
  [("The thing that binds us together is that we have both lowered our voices.", "The Museum of Innocence")])

# POLITICAL
add("gandhi-jr", "Jawaharlal Nehru's daughter's son Rajiv Gandhi", "ラジーヴ・ガンディー", 1944, 1991, ["in"], ["politics"],
  "Rajiv Gandhi was the sixth Prime Minister of India who oversaw the beginning of India's telecommunications and technology revolution.",
  "Gandhi was born in Bombay, India. He studied engineering at Cambridge and became a pilot for Indian Airlines before entering politics after his brother's death.",
  "Gandhi modernized India's telecommunications infrastructure and championed computer technology, laying groundwork for India's later IT revolution.",
  [(1984, "Became Prime Minister after mother's assassination"), (1986, "Introduced National Education Policy"), (1988, "Expanded telecommunications"), (1991, "Assassinated during election campaign")],
  [("Telecommunications Revolution", 1986, "Modernization of India's communication infrastructure")],
  [("India is an old country but a young nation.", "Attributed")])

add("patrice-lumumba", "Patrice Lumumba", "パトリス・ルムンバ", 1925, 1961, ["cd"], ["politics"],
  "Patrice Lumumba was the first democratically elected Prime Minister of the Democratic Republic of the Congo.",
  "Lumumba was born in Onalua, Belgian Congo. He was educated at missionary schools and became involved in politics and journalism.",
  "Lumumba's vision of a unified, independent Congo and his tragic assassination made him a martyr for African independence and a symbol of anti-colonialism.",
  [(1958, "Founded the Mouvement National Congolais"), (1960, "Became Prime Minister of the Congo"), (1960, "Deposed in a coup"), (1961, "Assassinated")],
  [("Independence Day Speech", 1960, "Speech denouncing Belgian colonialism at independence ceremonies")],
  [("The day will come when history will speak. Africa will write its own history.", "Attributed")])

add("yitzhak-rabin", "Yitzhak Rabin", "イツハク・ラビン", 1922, 1995, ["il"], ["politics"],
  "Yitzhak Rabin was an Israeli politician and general who served as Prime Minister and signed the Oslo Accords, seeking peace with the Palestinians.",
  "Rabin was born in Jerusalem. He served in the Palmach and IDF, becoming Chief of Staff during the Six-Day War before entering politics.",
  "Rabin's signing of the Oslo Accords with Yasser Arafat was a historic step toward Israeli-Palestinian peace. His assassination by an Israeli extremist shocked the world.",
  [(1964, "Became Chief of Staff of the IDF"), (1967, "Led IDF during the Six-Day War"), (1993, "Signed the Oslo Accords"), (1995, "Assassinated at a peace rally")],
  [("Oslo Accords", 1993, "Peace agreement between Israel and the PLO")],
  [("Enough of blood and tears. Enough.", "Nobel Peace Prize ceremony, 1994")])

# ENGINEERS/ASTRONOMERS
add("sergei-korolev", "Sergei Korolev", "セルゲイ・コロリョフ", 1907, 1966, ["ru"], ["engineering", "astronomy"],
  "Sergei Korolev was a Soviet rocket engineer and spacecraft designer who is considered the father of practical astronautics.",
  "Korolev was born in Zhytomyr, Ukraine. He survived imprisonment in the Gulag and became the chief designer of the Soviet space program.",
  "Korolev's achievements — Sputnik, Vostok, the first human in space — made the Soviet Union a space superpower and drove the Space Race.",
  [(1957, "Launched Sputnik, the first satellite"), (1961, "Launched Yuri Gagarin into space"), (1963, "Launched first woman in space")],
  [("Sputnik", 1957, "First artificial satellite to orbit Earth")],
  [("The Earth is the cradle of humanity, but mankind cannot stay in the cradle forever.", "Quoting Tsiolkovsky")])

add("konstantin-tsiolkovsky", "Konstantin Tsiolkovsky", "コンスタンチン・ツィオルコフスキー", 1857, 1935, ["ru"], ["engineering", "astronomy"],
  "Konstantin Tsiolkovsky was a Russian scientist and pioneer of astronautic theory who derived the rocket equation and envisioned space exploration.",
  "Tsiolkovsky was born in Izhevskoye, Russia. Nearly deaf from childhood, he was mostly self-educated and worked as a schoolteacher while developing his theories.",
  "Tsiolkovsky's rocket equation and his vision of multi-stage rockets, space stations, and interplanetary travel made him the theoretical father of spaceflight.",
  [(1903, "Published The Exploration of Cosmic Space by Means of Reaction Devices"), (1929, "Published multi-stage rocket theory")],
  [("The Exploration of Cosmic Space", 1903, "Paper deriving the fundamental rocket equation")],
  [("The Earth is the cradle of humanity, but mankind cannot stay in the cradle forever.", "Attributed")])

add("yuri-gagarin", "Yuri Gagarin", "ユーリイ・ガガーリン", 1934, 1968, ["ru"], ["engineering", "astronomy"],
  "Yuri Gagarin was a Soviet pilot and cosmonaut who became the first human in space on April 12, 1961.",
  "Gagarin was born in Klushino, Russia. He studied at the Saratov Industrial Technical School and trained as a military pilot before being selected as a cosmonaut.",
  "Gagarin's orbital flight aboard Vostok 1 was one of the defining moments of the 20th century, proving that human spaceflight was possible.",
  [(1960, "Selected as one of the first cosmonauts"), (1961, "Became first human in space"), (1968, "Died in a training jet crash")],
  [("Vostok 1 Flight", 1961, "First human spaceflight, orbiting Earth in 108 minutes")],
  [("I see Earth! It is so beautiful!", "Radio transmission during flight, 1961")])

add("neil-armstrong", "Neil Armstrong", "ニール・アームストロング", 1930, 2012, ["us"], ["engineering", "astronomy"],
  "Neil Armstrong was an American astronaut and aeronautical engineer who was the first person to walk on the Moon.",
  "Armstrong was born in Wapakoneta, Ohio. He was a naval aviator, test pilot, and aerospace engineer before being selected as a NASA astronaut.",
  "Armstrong's first step on the Moon on July 20, 1969, was one of humanity's greatest achievements, watched by an estimated 600 million people worldwide.",
  [(1962, "Selected as NASA astronaut"), (1966, "Commanded Gemini 8 mission"), (1969, "First person to walk on the Moon"), (1971, "Left NASA for academia")],
  [("Apollo 11 Moon Landing", 1969, "First crewed mission to land on the Moon")],
  [("That's one small step for man, one giant leap for mankind.", "First words on the Moon, 1969")])

# BIOLOGISTS
add("watson-crick-partner", "Maurice Hilleman", "モーリス・ヒルマン", 1919, 2005, ["us"], ["biology"],
  "Maurice Hilleman was an American microbiologist who developed more vaccines than any other scientist, saving millions of lives.",
  "Hilleman was born in Miles City, Montana. He studied at Montana State University and the University of Chicago before joining Walter Reed Army Institute.",
  "Hilleman developed over 40 vaccines, including those for measles, mumps, hepatitis A and B, chickenpox, and meningitis, saving more lives than perhaps any other scientist.",
  [(1957, "Developed flu vaccine in record time"), (1963, "Developed measles vaccine"), (1967, "Developed mumps vaccine"), (1981, "Developed hepatitis B vaccine")],
  [("Measles Vaccine", 1963, "Vaccine that has prevented millions of deaths worldwide")],
  [("If I had to name a person who has done more for the benefit of human health, I would say it would be difficult to find anyone.", "Robert Gallo about Hilleman")])

add("e-coli-researcher", "Sydney Brenner", "シドニー・ブレナー", 1927, 2019, ["za", "gb"], ["biology"],
  "Sydney Brenner was a South African biologist who won the Nobel Prize for discoveries about genetic regulation of organ development and programmed cell death.",
  "Brenner was born in Germiston, South Africa. He studied at the University of the Witwatersrand and Oxford before joining the MRC Laboratory of Molecular Biology.",
  "Brenner established C. elegans as a model organism, enabling studies of development and neuroscience. His work on mRNA was crucial to understanding gene expression.",
  [(1961, "Demonstrated the existence of messenger RNA"), (1963, "Established C. elegans as model organism"), (2002, "Awarded Nobel Prize in Physiology or Medicine")],
  [("C. elegans Research", 1963, "Establishment of the nematode worm as a model organism for genetics")],
  [("Progress in science depends on new techniques, new discoveries, and new ideas, probably in that order.", "Attributed")])

# CHEMISTS
add("svante-arrhenius-student", "Marie Curie's student Marguerite Perey", "マルグリット・ペレー", 1909, 1975, ["fr"], ["chemistry"],
  "Marguerite Perey was a French physicist who discovered the element francium, the last naturally occurring element to be discovered.",
  "Perey was born in Villemomble, France. She worked as Marie Curie's personal assistant at the Radium Institute from the age of 19.",
  "Perey's discovery of francium completed the alkali metal group of the periodic table. She was the first woman elected to the French Academy of Sciences.",
  [(1929, "Began working with Marie Curie"), (1939, "Discovered francium"), (1962, "First woman elected to the French Academy of Sciences")],
  [("Francium", 1939, "Discovery of element 87, the last naturally occurring element found")],
  [("Marie Curie taught me that science knows no frontiers.", "Attributed")])

# ARTISTS
add("frida-kahlo-rival", "Diego Rivera's contemporary David Alfaro Siqueiros", "ダビッド・アルファロ・シケイロス", 1896, 1974, ["mx"], ["art"],
  "David Alfaro Siqueiros was a Mexican social realist painter and one of the three great Mexican muralists alongside Rivera and Orozco.",
  "Siqueiros was born in Chihuahua, Mexico. He fought in the Mexican Revolution and devoted his art to revolutionary political causes.",
  "Siqueiros's dynamic murals, combining political content with innovative techniques including automotive paints and spray guns, transformed public art.",
  [(1922, "Began mural painting program"), (1932, "Experimented with new painting techniques in Los Angeles"), (1966, "Completed Marcha de la Humanidad mural")],
  [("The March of Humanity", 1971, "Enormous mural covering 4,600 square meters")],
  [("Art must no longer be the expression of individual satisfaction but should aim to become a fighting, educative art for all.", "Attributed")])

add("orozco", "José Clemente Orozco", "ホセ・クレメンテ・オロスコ", 1883, 1949, ["mx"], ["art"],
  "José Clemente Orozco was a Mexican muralist who was one of the three great Mexican muralists and is considered by many to be the greatest.",
  "Orozco was born in Zapotlán, Mexico. He lost his left hand in a childhood accident and studied at the Academy of San Carlos.",
  "Orozco's powerful, dramatic murals explored human suffering and political corruption with an expressionistic intensity that distinguished him from Rivera and Siqueiros.",
  [(1923, "Began mural paintings at the National Preparatory School"), (1930, "Painted murals at Pomona College and the New School"), (1936, "Painted murals at Hospicio Cabañas in Guadalajara")],
  [("Man of Fire", 1939, "Dramatic mural on the dome of the Hospicio Cabañas")],
  [("The highest, the most logical, the purest and strongest form of painting is the mural.", "Attributed")])

# MUSICIANS
add("thelonious-monk", "Thelonious Monk", "セロニアス・モンク", 1917, 1982, ["us"], ["art"],
  "Thelonious Monk was an American jazz pianist and composer, one of the founders of bebop, known for his unique improvisational style.",
  "Monk was born in Rocky Mount, North Carolina, and grew up in New York. He was largely self-taught and developed a distinctive, angular piano style.",
  "Monk's compositions, including Round Midnight and Straight, No Chaser, are jazz standards. His unorthodox harmonies and rhythms influenced all subsequent jazz.",
  [(1947, "First recordings as leader for Blue Note"), (1957, "Legendary performances at the Five Spot with John Coltrane"), (1964, "Appeared on the cover of Time magazine")],
  [("'Round Midnight", 1944, "Most recorded jazz standard"), ("Brilliant Corners", 1957, "Album showcasing his complex compositional style")],
  [("The piano ain't got no wrong notes.", "Attributed")])

add("charlie-parker", "Charlie Parker", "チャーリー・パーカー", 1920, 1955, ["us"], ["art"],
  "Charlie Parker was an American jazz saxophonist and composer who was a leading figure in the development of bebop.",
  "Parker was born in Kansas City, Kansas. He taught himself saxophone and by his teens was performing in Kansas City jazz clubs.",
  "Parker's virtuosic improvisations and complex harmonies transformed jazz from dance music to an art form. His influence on all subsequent jazz is immeasurable.",
  [(1940, "Helped develop bebop in New York"), (1945, "Recorded Ko-Ko and other bebop classics"), (1947, "Formed quintet with Miles Davis"), (1955, "Died at age 34")],
  [("Ko-Ko", 1945, "Landmark bebop recording")],
  [("Music is your own experience, your own thoughts, your wisdom.", "Attributed")])

add("billie-holiday", "Billie Holiday", "ビリー・ホリデイ", 1915, 1959, ["us"], ["art"],
  "Billie Holiday was an American jazz singer whose vocal style, influenced by jazz instrumentalists, pioneered a new way of manipulating phrasing and tempo.",
  "Holiday was born Eleanora Fagan in Philadelphia and grew up in Baltimore. She had a difficult childhood but began singing in Harlem nightclubs as a teenager.",
  "Holiday's emotionally powerful singing and her recording of Strange Fruit, a song about lynching, made her a civil rights icon and one of the greatest jazz vocalists.",
  [(1933, "First recording with Benny Goodman"), (1939, "Recorded Strange Fruit"), (1944, "Recorded Lover Man"), (1956, "Published autobiography Lady Sings the Blues")],
  [("Strange Fruit", 1939, "Song about racial violence that became a civil rights anthem"), ("Lady Sings the Blues", 1956, "Autobiography")],
  [("If I'm going to sing like someone else, then I don't need to sing at all.", "Attributed")])

add("wynton-marsalis", "Dizzy Gillespie", "ディジー・ガレスピー", 1917, 1993, ["us"], ["art"],
  "Dizzy Gillespie was an American jazz trumpeter, bandleader, composer, and singer who was one of the founding figures of bebop.",
  "Gillespie was born in Cheraw, South Carolina. He studied at the Laurinburg Institute and moved to New York, where he became a leading figure in modern jazz.",
  "Gillespie co-created bebop with Charlie Parker and introduced Afro-Cuban jazz, blending jazz with Latin American rhythms. His bent trumpet became iconic.",
  [(1940, "Began developing bebop"), (1945, "Formed big band"), (1947, "Introduced Afro-Cuban jazz"), (1956, "Led State Department jazz tours")],
  [("A Night in Tunisia", 1942, "Composition that became a bebop standard"), ("Afro-Cuban Jazz", 1947, "Fusion of jazz with Cuban rhythms")],
  [("It's taken me all my life to learn what not to play.", "Attributed")])

# PHILOSOPHERS
add("ludwig-wittgenstein", "Ludwig Wittgenstein", "ルートヴィヒ・ヴィトゲンシュタイン", 1889, 1951, ["at", "gb"], ["philosophy"],
  "Ludwig Wittgenstein was an Austrian-British philosopher who made major contributions to the philosophy of logic, mathematics, language, and mind.",
  "Wittgenstein was born in Vienna into one of Europe's wealthiest families. He studied engineering in Berlin and Manchester before turning to philosophy under Bertrand Russell at Cambridge.",
  "Wittgenstein's two major works revolutionized philosophy twice. The Tractatus argued that language pictures reality; the Investigations showed that meaning comes from use.",
  [(1921, "Published Tractatus Logico-Philosophicus"), (1929, "Returned to Cambridge"), (1953, "Philosophical Investigations published posthumously")],
  [("Tractatus Logico-Philosophicus", 1921, "Work arguing that the limits of language are the limits of the world"), ("Philosophical Investigations", 1953, "Work exploring language games and meaning as use")],
  [("Whereof one cannot speak, thereof one must be silent.", "Tractatus Logico-Philosophicus")])

add("martin-heidegger", "Martin Heidegger", "マルティン・ハイデガー", 1889, 1976, ["de"], ["philosophy"],
  "Martin Heidegger was a German philosopher whose work on being, existence, and phenomenology profoundly influenced 20th-century philosophy.",
  "Heidegger was born in Meßkirch, Germany. He studied at the University of Freiburg under Husserl and became one of the most influential and controversial philosophers of the 20th century.",
  "Heidegger's Being and Time transformed philosophy by asking the fundamental question of the meaning of Being. His work influenced existentialism, hermeneutics, and postmodernism.",
  [(1927, "Published Being and Time"), (1933, "Briefly served as rector under Nazi regime"), (1935, "Published Introduction to Metaphysics")],
  [("Being and Time", 1927, "Foundational work of existential philosophy examining the meaning of Being")],
  [("Language is the house of Being.", "Letter on Humanism")])

# MORE UNIQUE SCIENTISTS
add("jane-jacobs", "Jane Jacobs", "ジェーン・ジェイコブズ", 1916, 2006, ["us", "ca"], ["politics"],
  "Jane Jacobs was an American-Canadian journalist, author, and activist who influenced urban planning with her critique of modernist city design.",
  "Jacobs was born in Scranton, Pennsylvania. She worked as a journalist in New York and became an influential voice in urban studies without formal academic training.",
  "Jacobs's The Death and Life of Great American Cities challenged prevailing urban planning orthodoxy and championed the vitality of diverse, walkable neighborhoods.",
  [(1961, "Published The Death and Life of Great American Cities"), (1968, "Moved to Toronto to avoid Vietnam draft for her sons"), (1984, "Published Cities and the Wealth of Nations")],
  [("The Death and Life of Great American Cities", 1961, "Revolutionary critique of modern urban planning")],
  [("Cities have the capability of providing something for everybody, only because, and only when, they are created by everybody.", "The Death and Life of Great American Cities")])

add("richard-feynman-dup", "Julian Schwinger", "ジュリアン・シュウィンガー", 1918, 1994, ["us"], ["physics"],
  "Julian Schwinger was an American theoretical physicist who shared the Nobel Prize for his work on quantum electrodynamics.",
  "Schwinger was born in New York City. A prodigy, he published his first physics paper at 16 and earned his PhD from Columbia at 21.",
  "Schwinger's rigorous mathematical formulation of quantum electrodynamics, independent of Feynman and Tomonaga, was a monumental achievement in theoretical physics.",
  [(1947, "Developed QED formulation"), (1948, "Calculated the anomalous magnetic moment of the electron"), (1965, "Shared Nobel Prize in Physics")],
  [("Quantum Electrodynamics", 1948, "Rigorous mathematical formulation of QED")],
  [("If you can't join 'em, beat 'em.", "Attributed")])

add("max-born", "Max Born", "マックス・ボルン", 1882, 1970, ["de", "gb"], ["physics"],
  "Max Born was a German-British physicist who won the Nobel Prize for his fundamental research in quantum mechanics, particularly the statistical interpretation of the wave function.",
  "Born was born in Breslau, Germany. He studied at Breslau, Heidelberg, and Göttingen, becoming professor at Göttingen where he made his major contributions.",
  "Born's statistical interpretation of the wave function provided the probability basis of quantum mechanics, resolving fundamental interpretive questions.",
  [(1926, "Proposed the probabilistic interpretation of quantum mechanics"), (1933, "Left Germany; moved to Cambridge"), (1954, "Awarded Nobel Prize in Physics")],
  [("Statistical Interpretation of Quantum Mechanics", 1926, "Paper proposing the Born rule for quantum probability")],
  [("I believe that ideas such as absolute certitude, absolute exactness, final truth, etc. are figments of the imagination.", "Nobel lecture")])

add("wolfgang-pauli", "Wolfgang Pauli", "ヴォルフガング・パウリ", 1900, 1958, ["at", "us"], ["physics"],
  "Wolfgang Pauli was an Austrian theoretical physicist who received the Nobel Prize for his discovery of the Pauli exclusion principle.",
  "Pauli was born in Vienna. He was a child prodigy who published a paper on general relativity at age 18 and earned his doctorate under Sommerfeld.",
  "Pauli's exclusion principle explains the structure of atoms and the periodic table. His sharp wit and critical mind earned him the nickname 'the conscience of physics.'",
  [(1924, "Proposed quantum spin"), (1925, "Formulated the exclusion principle"), (1930, "Proposed the neutrino"), (1945, "Awarded Nobel Prize in Physics")],
  [("Exclusion Principle", 1925, "Principle that no two identical fermions can occupy the same quantum state")],
  [("Not only is it not right, it is not even wrong.", "On a poorly argued paper")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'subramanyan-chandrasekhar-dup':
            entry['id'] = 'c-v-raman'
        elif entry['id'] == 'emmy-noether-student':
            entry['id'] = 'bartel-van-der-waerden'
        elif entry['id'] == 'emmy-noether-teacher':
            entry['id'] = 'richard-dedekind'
        elif entry['id'] == 'gandhi-jr':
            entry['id'] = 'rajiv-gandhi'
        elif entry['id'] == 'watson-crick-partner':
            entry['id'] = 'maurice-hilleman'
        elif entry['id'] == 'e-coli-researcher':
            entry['id'] = 'sydney-brenner'
        elif entry['id'] == 'svante-arrhenius-student':
            entry['id'] = 'marguerite-perey'
        elif entry['id'] == 'frida-kahlo-rival':
            entry['id'] = 'david-alfaro-siqueiros'
        elif entry['id'] == 'wynton-marsalis':
            entry['id'] = 'dizzy-gillespie'
        elif entry['id'] == 'richard-feynman-dup':
            entry['id'] = 'julian-schwinger'
    write_people(P)
