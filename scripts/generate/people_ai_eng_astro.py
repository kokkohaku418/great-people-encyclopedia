#!/usr/bin/env python3
"""Generate ~100 engineers and astronomers."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# === ASTRONOMERS ===

p("nicolaus-copernicus", "Nicolaus Copernicus", "ニコラウス・コペルニクス", 1473, 1543, ["pl"], ["astronomy"],
  "Nicolaus Copernicus was a Renaissance-era polymath who formulated a model of the universe that placed the Sun rather than the Earth at the center.",
  "Copernicus was born in Toruń, Royal Prussia. He studied at the University of Kraków and in Italy before returning to Poland as a church canon.",
  "Copernicus's heliocentric model initiated the Scientific Revolution, fundamentally changing humanity's understanding of its place in the universe.",
  [(1503, "Returned to Poland after studies in Italy"), (1514, "Circulated Commentariolus with heliocentric ideas"), (1543, "Published De revolutionibus orbium coelestium")],
  [("De revolutionibus orbium coelestium", 1543, "Proposed the heliocentric model of the solar system")],
  [("To know that we know what we know, and to know that we do not know what we do not know, that is true knowledge.", "Attributed")])

p("galileo-galilei", "Galileo Galilei", "ガリレオ・ガリレイ", 1564, 1642, ["it"], ["astronomy", "physics"],
  "Galileo Galilei was an Italian astronomer, physicist, and engineer, often called the father of modern observational astronomy and modern physics.",
  "Galileo was born in Pisa, Italy. He studied at the University of Pisa and became professor of mathematics at Padua, where he made his most important discoveries.",
  "Galileo's telescopic discoveries confirmed the Copernican system and his experimental methods established modern physics. His conflict with the Church symbolizes the clash between science and authority.",
  [(1589, "Became professor at the University of Pisa"), (1609, "Built improved telescope; observed the heavens"), (1610, "Published Sidereus Nuncius with telescopic discoveries"), (1633, "Tried by the Inquisition; placed under house arrest")],
  [("Sidereus Nuncius", 1610, "Report of telescopic observations including Jupiter's moons"), ("Dialogue Concerning the Two Chief World Systems", 1632, "Defense of the Copernican system")],
  [("And yet it moves.", "Attributed, after recanting heliocentrism")])

p("johannes-kepler", "Johannes Kepler", "ヨハネス・ケプラー", 1571, 1630, ["de"], ["astronomy", "mathematics"],
  "Johannes Kepler was a German astronomer who discovered three major laws of planetary motion, providing the mathematical foundation for the Copernican system.",
  "Kepler was born in Weil der Stadt, Germany. He studied at the University of Tübingen and became an assistant to Tycho Brahe in Prague.",
  "Kepler's laws of planetary motion replaced circular orbits with ellipses, transforming astronomy and providing the foundation for Newton's law of gravitation.",
  [(1596, "Published Mysterium Cosmographicum"), (1600, "Became Tycho Brahe's assistant in Prague"), (1609, "Published Astronomia Nova with first two laws"), (1619, "Published Harmonices Mundi with third law")],
  [("Astronomia Nova", 1609, "Introduced the first two laws of planetary motion"), ("Harmonices Mundi", 1619, "Described the third law of planetary motion")],
  [("I much prefer the sharpest criticism of a single intelligent man to the thoughtless approval of the masses.", "Attributed")])

p("tycho-brahe", "Tycho Brahe", "ティコ・ブラーエ", 1546, 1601, ["dk"], ["astronomy"],
  "Tycho Brahe was a Danish nobleman and astronomer who made the most precise astronomical observations of his time before the invention of the telescope.",
  "Brahe was born in Knudstrup, Denmark. He became fascinated with astronomy after observing a solar eclipse at age 14 and was granted the island of Hven to build his observatory.",
  "Brahe's precise observations, particularly of Mars, enabled Kepler to discover the laws of planetary motion. His data was the foundation of the Copernican revolution.",
  [(1572, "Observed and published about a supernova"), (1576, "Built Uraniborg observatory on Hven"), (1597, "Left Denmark for Prague"), (1600, "Hired Kepler as assistant")],
  [("De nova stella", 1573, "Study of a supernova that proved the heavens could change")],
  [("Let me not seem to have lived in vain.", "Attributed deathbed words")])

p("edwin-hubble", "Edwin Hubble", "エドウィン・ハッブル", 1889, 1953, ["us"], ["astronomy"],
  "Edwin Hubble was an American astronomer who played a crucial role in establishing the field of extragalactic astronomy and demonstrated that the universe is expanding.",
  "Hubble was born in Marshfield, Missouri. He studied astronomy at the University of Chicago and law at Oxford before returning to astronomy at Mount Wilson Observatory.",
  "Hubble proved that galaxies exist beyond the Milky Way and discovered that the universe is expanding, fundamentally transforming our understanding of the cosmos.",
  [(1924, "Proved the existence of other galaxies"), (1929, "Discovered the expanding universe (Hubble's law)"), (1936, "Published The Realm of the Nebulae")],
  [("The Realm of the Nebulae", 1936, "Comprehensive account of extragalactic astronomy and the expanding universe")],
  [("Equipped with his five senses, man explores the universe around him and calls the adventure Science.", "The Nature of Science")])

p("carl-sagan", "Carl Sagan", "カール・セーガン", 1934, 1996, ["us"], ["astronomy"],
  "Carl Sagan was an American astronomer, planetary scientist, and science communicator who became one of the most well-known scientists in the world.",
  "Sagan was born in Brooklyn, New York. He studied at the University of Chicago and became a professor at Cornell University, contributing to planetary science.",
  "Sagan's Cosmos television series and books made astronomy accessible to millions worldwide. His advocacy for scientific thinking influenced public understanding of science.",
  [(1966, "Published Intelligent Life in the Universe"), (1972, "Designed Pioneer plaque"), (1980, "Premiered Cosmos: A Personal Voyage"), (1990, "Proposed the Pale Blue Dot photograph")],
  [("Cosmos: A Personal Voyage", 1980, "Television series that brought astronomy to a global audience"), ("Pale Blue Dot", 1994, "Reflections on Earth's place in the cosmos")],
  [("Somewhere, something incredible is waiting to be known.", "Attributed")])

p("vera-rubin", "Vera Rubin", "ヴェラ・ルービン", 1928, 2016, ["us"], ["astronomy"],
  "Vera Rubin was an American astronomer who pioneered work on galaxy rotation rates, providing strong evidence for the existence of dark matter.",
  "Rubin was born in Philadelphia. She studied at Vassar and Cornell, where she faced discrimination as a woman in science, before joining the Carnegie Institution.",
  "Rubin's observations of galaxy rotation curves provided the first strong evidence for dark matter, suggesting that most of the universe's mass is invisible.",
  [(1965, "Began studying galaxy rotation curves"), (1970, "Published evidence for dark matter in Andromeda"), (1978, "Extended dark matter findings to many galaxies"), (1993, "Awarded National Medal of Science")],
  [("Galaxy Rotation Curves", 1970, "Observations providing strong evidence for the existence of dark matter")],
  [("In a spiral galaxy, the weights of my observations show that the weights of the masses do not correspond to the light.", "Attributed")])

p("henrietta-swan-leavitt", "Henrietta Swan Leavitt", "ヘンリエッタ・スワン・リーヴィット", 1868, 1921, ["us"], ["astronomy"],
  "Henrietta Swan Leavitt was an American astronomer who discovered the period-luminosity relationship of Cepheid variables, enabling measurement of cosmic distances.",
  "Leavitt was born in Lancaster, Massachusetts. She graduated from Radcliffe College and worked as a 'computer' at the Harvard College Observatory.",
  "Leavitt's discovery that the brightness of Cepheid variable stars correlates with their period of variation became the key to measuring distances in the universe.",
  [(1893, "Began work at Harvard College Observatory"), (1908, "Published findings on Cepheid variable stars"), (1912, "Established the period-luminosity relationship")],
  [("Periods of 25 Variable Stars in the Small Magellanic Cloud", 1912, "Paper establishing the period-luminosity relationship for Cepheid variables")],
  [("The brighter variables have the longer periods.", "1912 paper")])

p("cecilia-payne-gaposchkin", "Cecilia Payne-Gaposchkin", "セシリア・ペイン＝ガポシュキン", 1900, 1979, ["gb", "us"], ["astronomy"],
  "Cecilia Payne-Gaposchkin was a British-American astronomer who first proposed that stars are composed primarily of hydrogen and helium.",
  "Payne was born in Wendover, England. She studied at Cambridge but could not receive a degree as a woman, so she moved to Harvard, where she earned the first PhD in astronomy.",
  "Payne's doctoral thesis, described as 'the most brilliant PhD thesis ever written in astronomy,' correctly determined the chemical composition of stars, revolutionizing astrophysics.",
  [(1925, "Completed doctoral thesis at Harvard"), (1934, "Married Sergei Gaposchkin"), (1956, "Became first woman to head a department at Harvard")],
  [("Stellar Atmospheres", 1925, "Doctoral thesis proving stars are made primarily of hydrogen and helium")],
  [("The reward of the young scientist is the emotional thrill of being the first person in the history of the world to see something or to understand something.", "Attributed")])

p("giovanni-cassini", "Giovanni Cassini", "ジョヴァンニ・カッシーニ", 1625, 1712, ["it", "fr"], ["astronomy"],
  "Giovanni Cassini was an Italian-French astronomer who discovered four of Saturn's moons and the gap in Saturn's rings that bears his name.",
  "Cassini was born in Perinaldo, Italy. He studied at the University of Bologna and became director of the Paris Observatory at the invitation of King Louis XIV.",
  "Cassini's discoveries of Saturn's moons and ring divisions, and his measurements of planetary distances, advanced understanding of the solar system.",
  [(1665, "Determined rotation periods of Jupiter and Mars"), (1669, "Became director of the Paris Observatory"), (1672, "Determined distance to Mars"), (1675, "Discovered the Cassini Division in Saturn's rings")],
  [("Cassini Division", 1675, "Discovery of the gap in Saturn's rings")],
  [("Observation is the foundation of all true astronomy.", "Attributed")])

p("william-herschel", "William Herschel", "ウィリアム・ハーシェル", 1738, 1822, ["de", "gb"], ["astronomy"],
  "William Herschel was a German-born British astronomer who discovered Uranus and made fundamental contributions to understanding the structure of the Milky Way.",
  "Herschel was born in Hanover, Germany. He moved to England as a musician and taught himself astronomy, building the largest telescopes of his era.",
  "Herschel's discovery of Uranus was the first new planet found since antiquity. His systematic surveys of the sky laid the foundation for stellar astronomy.",
  [(1781, "Discovered Uranus"), (1783, "Discovered the motion of the solar system through space"), (1789, "Built 40-foot telescope"), (1800, "Discovered infrared radiation")],
  [("Discovery of Uranus", 1781, "First planet discovered in modern times")],
  [("The undevout astronomer is mad.", "Attributed")])

p("caroline-herschel", "Caroline Herschel", "カロライン・ハーシェル", 1750, 1848, ["de", "gb"], ["astronomy"],
  "Caroline Herschel was a German-born British astronomer who was the first woman to discover a comet and the first woman to receive a salary as a scientist.",
  "Herschel was born in Hanover, Germany. She assisted her brother William Herschel and became an accomplished astronomer in her own right.",
  "Caroline Herschel's catalog of nebulae and her discovery of eight comets established her as a pioneering woman in science. She was the first woman to receive the Royal Astronomical Society's Gold Medal.",
  [(1786, "Discovered her first comet"), (1787, "Received first salary as a female scientist"), (1797, "Submitted catalog of star clusters and nebulae"), (1828, "Awarded Gold Medal of the Royal Astronomical Society")],
  [("Catalogue of Stars", 1798, "Comprehensive catalog of nebulae and star clusters")],
  [("I did nothing for my brother but what a well-trained puppy dog would have done.", "Memoir, characteristically modest")])

p("subrahmanyan-chandrasekhar", "Subrahmanyan Chandrasekhar", "スブラマニアン・チャンドラセカール", 1910, 1995, ["in", "us"], ["astronomy", "physics"],
  "Subrahmanyan Chandrasekhar was an Indian-American astrophysicist who won the Nobel Prize for his theoretical studies of the physical processes important to the structure and evolution of stars.",
  "Chandrasekhar was born in Lahore, British India. He studied at the University of Madras and Cambridge before joining the University of Chicago.",
  "Chandrasekhar's limit — the maximum mass of a stable white dwarf star — was a landmark discovery that explained stellar evolution and the formation of black holes.",
  [(1930, "Calculated the Chandrasekhar limit"), (1937, "Joined the University of Chicago"), (1983, "Awarded Nobel Prize in Physics")],
  [("An Introduction to the Study of Stellar Structure", 1939, "Foundational work on the physics of stars")],
  [("I should like to feel at the end that I had done all I could with the talent that God gave me.", "Attributed")])

p("stephen-hawking", "Stephen Hawking", "スティーヴン・ホーキング", 1942, 2018, ["gb"], ["astronomy", "physics"],
  "Stephen Hawking was a British theoretical physicist whose work on black holes and cosmology made him one of the most famous scientists of the modern era.",
  "Hawking was born in Oxford, England. He studied at Oxford and Cambridge, where he was diagnosed with motor neurone disease at age 21 but continued his groundbreaking work.",
  "Hawking's discovery of Hawking radiation, showing that black holes emit radiation, unified quantum mechanics and general relativity. A Brief History of Time made cosmology accessible to millions.",
  [(1966, "Completed doctoral thesis on singularities"), (1974, "Proposed Hawking radiation"), (1979, "Became Lucasian Professor at Cambridge"), (1988, "Published A Brief History of Time")],
  [("A Brief History of Time", 1988, "Popular science book on cosmology that sold over 25 million copies"), ("Hawking Radiation", 1974, "Theoretical prediction that black holes emit radiation")],
  [("Remember to look up at the stars and not down at your feet.", "Attributed")])

p("jocelyn-bell-burnell", "Jocelyn Bell Burnell", "ジョスリン・ベル・バーネル", 1943, None, ["gb"], ["astronomy"],
  "Jocelyn Bell Burnell is a Northern Irish astrophysicist who, as a graduate student, discovered the first radio pulsars.",
  "Bell Burnell was born in Lurgan, Northern Ireland. She studied at the University of Glasgow and Cambridge, where she made her groundbreaking discovery.",
  "Bell Burnell's discovery of pulsars was one of the most important astronomical discoveries of the 20th century, though the Nobel Prize went to her supervisor.",
  [(1967, "Discovered first radio pulsars"), (1968, "Discovery announced in Nature"), (2018, "Awarded Special Breakthrough Prize in Fundamental Physics")],
  [("Observation of a Rapidly Pulsating Radio Source", 1968, "Paper announcing the discovery of pulsars")],
  [("I believe it would demean Nobel Prizes if they were awarded to research students.", "Attributed")])

# === ENGINEERS ===

p("nikola-tesla", "Nikola Tesla", "ニコラ・テスラ", 1856, 1943, ["hr", "us"], ["engineering", "physics"],
  "Nikola Tesla was a Serbian-American inventor and electrical engineer who designed the modern alternating current electricity supply system.",
  "Tesla was born in Smiljan, Croatia. He studied engineering in Austria and worked in Budapest and Paris before emigrating to the United States to work with Thomas Edison.",
  "Tesla's AC motor and power transmission system enabled the electrification of the world. His inventions in radio, X-ray, and remote control were decades ahead of their time.",
  [(1884, "Emigrated to the United States"), (1888, "Patented AC motor"), (1893, "Demonstrated AC power at World's Columbian Exposition"), (1899, "Conducted experiments in Colorado Springs")],
  [("AC Motor Patent", 1888, "Patent for the polyphase alternating current motor that powers the modern world")],
  [("The present is theirs; the future, for which I really worked, is mine.", "Attributed")])

p("thomas-edison", "Thomas Edison", "トーマス・エジソン", 1847, 1931, ["us"], ["engineering"],
  "Thomas Edison was an American inventor and businessman who developed many devices including the phonograph, the motion picture camera, and the practical incandescent light bulb.",
  "Edison was born in Milan, Ohio. He was partially deaf and largely self-educated. He established the world's first industrial research laboratory in Menlo Park, New Jersey.",
  "Edison held over 1,000 patents and created the first practical electric lighting system. His invention of the industrial research lab established the model for modern R&D.",
  [(1877, "Invented the phonograph"), (1879, "Developed practical incandescent light bulb"), (1882, "Opened first commercial power station"), (1891, "Patented the kinetoscope")],
  [("Incandescent Light Bulb", 1879, "Practical electric light that transformed daily life"), ("Phonograph", 1877, "First device to record and reproduce sound")],
  [("Genius is one percent inspiration and ninety-nine percent perspiration.", "Harper's Monthly, 1932")])

p("james-watt", "James Watt", "ジェームズ・ワット", 1736, 1819, ["gb"], ["engineering"],
  "James Watt was a Scottish inventor and mechanical engineer whose improvements to the steam engine were fundamental to the Industrial Revolution.",
  "Watt was born in Greenock, Scotland. He trained as an instrument maker and was asked to repair a Newcomen steam engine at the University of Glasgow.",
  "Watt's separate condenser dramatically improved steam engine efficiency, powering the Industrial Revolution. The unit of power — the watt — is named in his honor.",
  [(1765, "Conceived the separate condenser"), (1769, "Patented the separate condenser"), (1776, "First commercial Watt engines installed"), (1782, "Introduced the double-acting engine")],
  [("Watt Steam Engine", 1769, "Improved steam engine with separate condenser that powered the Industrial Revolution")],
  [("I can think of nothing else but this machine.", "Letter, 1765")])

p("isambard-kingdom-brunel", "Isambard Kingdom Brunel", "イザムバード・キングダム・ブルネル", 1806, 1859, ["gb"], ["engineering"],
  "Isambard Kingdom Brunel was a British civil engineer who built bridges, tunnels, railway lines, and steamships that transformed 19th-century Britain.",
  "Brunel was born in Portsmouth, England. He was educated in France and England and became chief engineer of the Great Western Railway at age 27.",
  "Brunel's Great Western Railway, Clifton Suspension Bridge, and transatlantic steamships demonstrated engineering on an unprecedented scale, transforming transportation.",
  [(1833, "Appointed chief engineer of the Great Western Railway"), (1838, "Launched SS Great Western"), (1843, "Launched SS Great Britain"), (1864, "Clifton Suspension Bridge completed posthumously")],
  [("SS Great Eastern", 1858, "Largest ship ever built at the time"), ("Great Western Railway", 1841, "Railway with innovative broad gauge design")],
  [("I am opposed to the laying down of rules or conditions to be observed in the construction of bridges.", "Letter")])

p("gustave-eiffel", "Gustave Eiffel", "ギュスターヴ・エッフェル", 1832, 1923, ["fr"], ["engineering"],
  "Gustave Eiffel was a French civil engineer who designed the Eiffel Tower and the internal structure of the Statue of Liberty.",
  "Eiffel was born in Dijon, France. He studied at the École Centrale des Arts et Manufactures and specialized in metallic structures and bridge construction.",
  "Eiffel's tower became the most recognizable structure in the world and a symbol of modern engineering. His pioneering work in aerodynamics later contributed to aviation.",
  [(1858, "Designed his first iron bridge"), (1884, "Designed internal structure of the Statue of Liberty"), (1889, "Completed the Eiffel Tower for the World's Fair"), (1903, "Began aerodynamics research")],
  [("Eiffel Tower", 1889, "Iron lattice tower that became the symbol of Paris and modern engineering")],
  [("I ought to be jealous of the tower. She is more famous than I am.", "Attributed")])

p("wright-brothers-wilbur", "Wilbur Wright", "ウィルバー・ライト", 1867, 1912, ["us"], ["engineering"],
  "Wilbur Wright, together with his brother Orville, invented, built, and flew the first successful motor-operated airplane.",
  "Wilbur was born in Millville, Indiana. He and his brother Orville ran a bicycle shop in Dayton, Ohio, while developing their flying machines.",
  "The Wright brothers' achievement of powered, controlled flight transformed transportation and warfare. Their systematic engineering approach to aviation was groundbreaking.",
  [(1899, "Began studying aeronautics"), (1900, "Began glider experiments at Kitty Hawk"), (1903, "First powered flight at Kitty Hawk"), (1908, "Demonstrated flights in Europe")],
  [("Wright Flyer", 1903, "First successful heavier-than-air powered aircraft")],
  [("It is possible to fly without motors, but not without knowledge and skill.", "Attributed")])

p("wright-brothers-orville", "Orville Wright", "オーヴィル・ライト", 1871, 1948, ["us"], ["engineering"],
  "Orville Wright, together with his brother Wilbur, invented, built, and flew the first successful motor-operated airplane.",
  "Orville was born in Dayton, Ohio. With his brother Wilbur, he ran a printing business and then a bicycle shop while pursuing their aviation experiments.",
  "The Wright brothers' methodical approach — building wind tunnels, testing wing shapes, and developing control systems — created the science of aeronautical engineering.",
  [(1899, "Built first kite to test wing warping"), (1901, "Built wind tunnel for aerodynamic testing"), (1903, "Piloted first powered flight"), (1908, "Demonstrated airplane to U.S. Army")],
  [("First Powered Flight", 1903, "12-second flight that changed the world")],
  [("If we worked on the assumption that what is accepted as true really is true, then there would be little hope for advance.", "Attributed")])

p("henry-ford", "Henry Ford", "ヘンリー・フォード", 1863, 1947, ["us"], ["engineering"],
  "Henry Ford was an American industrialist and founder of the Ford Motor Company who pioneered the assembly line method of mass production.",
  "Ford was born in Dearborn, Michigan. He worked as an engineer before founding the Ford Motor Company and developing the Model T automobile.",
  "Ford's assembly line revolutionized manufacturing, making automobiles affordable for the middle class and transforming modern industry and society.",
  [(1896, "Built his first automobile, the Quadricycle"), (1903, "Founded Ford Motor Company"), (1908, "Introduced the Model T"), (1913, "Implemented moving assembly line")],
  [("Model T", 1908, "Affordable automobile that put America on wheels"), ("Assembly Line", 1913, "Moving assembly line that revolutionized manufacturing")],
  [("Whether you think you can, or you think you can't — you're right.", "Attributed")])

p("wernher-von-braun", "Wernher von Braun", "ヴェルナー・フォン・ブラウン", 1912, 1977, ["de", "us"], ["engineering", "astronomy"],
  "Wernher von Braun was a German-American aerospace engineer who was the chief architect of the Saturn V rocket that launched humans to the Moon.",
  "Von Braun was born in Wirsitz, Germany. He developed rockets for Nazi Germany's V-2 program before surrendering to American forces and joining NASA.",
  "Von Braun's Saturn V rocket remains the most powerful rocket ever flown successfully. He was the driving force behind the Apollo program that landed humans on the Moon.",
  [(1944, "V-2 rocket became first human-made object to reach space"), (1945, "Surrendered to American forces"), (1960, "Became director of NASA's Marshall Space Flight Center"), (1969, "Saturn V launched Apollo 11 to the Moon")],
  [("Saturn V", 1967, "The rocket that took humans to the Moon")],
  [("Research is what I'm doing when I don't know what I'm doing.", "Attributed")])

p("alan-turing", "Alan Turing", "アラン・チューリング", 1912, 1954, ["gb"], ["engineering", "mathematics"],
  "Alan Turing was a British mathematician and computer scientist who is considered the father of theoretical computer science and artificial intelligence.",
  "Turing was born in London. He studied at Cambridge and Princeton, where he developed the concept of the Turing machine, a foundational model of computation.",
  "Turing's theoretical work established computer science as a discipline. His code-breaking at Bletchley Park during WWII is estimated to have shortened the war by two years.",
  [(1936, "Published 'On Computable Numbers' introducing the Turing machine"), (1939, "Began code-breaking work at Bletchley Park"), (1950, "Proposed the Turing test for artificial intelligence"), (1952, "Convicted under anti-homosexuality laws")],
  [("On Computable Numbers", 1936, "Paper introducing the concept of the universal computing machine"), ("Computing Machinery and Intelligence", 1950, "Paper proposing the Turing test")],
  [("We can only see a short distance ahead, but we can see plenty there that needs to be done.", "Computing Machinery and Intelligence")])

p("grace-hopper", "Grace Hopper", "グレース・ホッパー", 1906, 1992, ["us"], ["engineering", "mathematics"],
  "Grace Hopper was an American computer scientist and United States Navy rear admiral who was a pioneer of computer programming.",
  "Hopper was born in New York City. She studied mathematics at Vassar and Yale and joined the Navy during World War II, working on the Mark I computer.",
  "Hopper developed the first compiler, popularized the idea of machine-independent programming languages, and led the development of COBOL, one of the first high-level programming languages.",
  [(1944, "Began programming the Harvard Mark I"), (1952, "Developed first compiler"), (1959, "Led development of COBOL"), (1986, "Retired from Navy as rear admiral")],
  [("COBOL", 1959, "Common Business-Oriented Language, one of the first high-level programming languages")],
  [("The most dangerous phrase in the language is: We've always done it this way.", "Attributed")])

p("tim-berners-lee", "Tim Berners-Lee", "ティム・バーナーズ＝リー", 1955, None, ["gb"], ["engineering"],
  "Tim Berners-Lee is a British computer scientist who invented the World Wide Web, fundamentally changing how humanity communicates and accesses information.",
  "Berners-Lee was born in London. He studied at Oxford and worked at CERN in Switzerland, where he proposed the World Wide Web.",
  "Berners-Lee's invention of the Web — combining hypertext with the internet — transformed global communication, commerce, education, and culture.",
  [(1989, "Proposed the World Wide Web at CERN"), (1990, "Created first web browser and server"), (1991, "First website went live"), (1994, "Founded the World Wide Web Consortium")],
  [("World Wide Web", 1990, "System of interlinked hypertext documents accessed via the internet")],
  [("The Web as I envisaged it, we have not seen it yet. The future is still so much bigger than the past.", "Attributed")])

p("guglielmo-marconi", "Guglielmo Marconi", "グリエルモ・マルコーニ", 1874, 1937, ["it"], ["engineering", "physics"],
  "Guglielmo Marconi was an Italian inventor and electrical engineer who developed the first practical long-distance wireless telegraphy system.",
  "Marconi was born in Bologna, Italy. He was educated privately and became interested in radio waves after reading about Heinrich Hertz's experiments.",
  "Marconi's development of practical radio communication transformed global communications, enabling ship-to-shore communication, broadcasting, and ultimately modern wireless technology.",
  [(1895, "Conducted first radio transmissions"), (1899, "Sent wireless signals across the English Channel"), (1901, "Transmitted signals across the Atlantic"), (1909, "Awarded Nobel Prize in Physics")],
  [("Transatlantic Radio Transmission", 1901, "First wireless signal sent across the Atlantic Ocean")],
  [("Every day sees humanity more victorious in the struggle with space and time.", "Nobel lecture, 1909")])

p("alexander-graham-bell", "Alexander Graham Bell", "アレクサンダー・グラハム・ベル", 1847, 1922, ["gb", "ca", "us"], ["engineering"],
  "Alexander Graham Bell was a Scottish-born inventor, scientist, and engineer who is credited with patenting the first practical telephone.",
  "Bell was born in Edinburgh, Scotland. His family's work with the deaf influenced his studies of sound and speech, leading to his invention of the telephone.",
  "Bell's telephone revolutionized global communication. His work also advanced aviation, hydrofoils, and telecommunications technology.",
  [(1871, "Moved to Canada, then the United States"), (1876, "Patented the telephone"), (1877, "Founded the Bell Telephone Company"), (1898, "Became president of the National Geographic Society")],
  [("Telephone Patent", 1876, "Patent for the apparatus for transmitting vocal sounds")],
  [("When one door closes, another opens.", "Attributed")])

p("john-von-neumann", "John von Neumann", "ジョン・フォン・ノイマン", 1903, 1957, ["hu", "us"], ["engineering", "mathematics"],
  "John von Neumann was a Hungarian-American mathematician and polymath who made major contributions to mathematics, physics, economics, computing, and statistics.",
  "Von Neumann was born in Budapest, Hungary. A child prodigy, he studied in Berlin, Zurich, and Göttingen before moving to Princeton.",
  "Von Neumann's architecture for stored-program computers became the basis for virtually all modern computers. His contributions span game theory, quantum mechanics, and nuclear physics.",
  [(1928, "Published minimax theorem in game theory"), (1932, "Published Mathematical Foundations of Quantum Mechanics"), (1944, "Published Theory of Games and Economic Behavior"), (1945, "Described stored-program computer architecture")],
  [("Theory of Games and Economic Behavior", 1944, "Foundational work in game theory"), ("First Draft of a Report on the EDVAC", 1945, "Description of the stored-program computer architecture")],
  [("If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.", "Attributed")])

p("robert-stephenson", "George Stephenson", "ジョージ・スティーブンソン", 1781, 1848, ["gb"], ["engineering"],
  "George Stephenson was a British civil engineer and mechanical engineer known as the 'Father of Railways' who built the first public inter-city railway.",
  "Stephenson was born in Wylam, Northumberland. He was illiterate until age 18, when he taught himself to read. He worked in coal mines and developed steam locomotives.",
  "Stephenson's railways transformed transportation, commerce, and society. His standard gauge of 4 feet 8.5 inches became the world standard for most railways.",
  [(1814, "Built his first locomotive, Blücher"), (1825, "Opened the Stockton and Darlington Railway"), (1829, "Rocket won the Rainhill Trials"), (1830, "Opened the Liverpool and Manchester Railway")],
  [("Rocket", 1829, "Locomotive that demonstrated the viability of steam railways")],
  [("The locomotive is a wonderful machine; it has power, it has speed, and it can do the work of many horses.", "Attributed")])

p("ada-lovelace", "Ada Lovelace", "エイダ・ラブレス", 1815, 1852, ["gb"], ["engineering", "mathematics"],
  "Ada Lovelace was a British mathematician and writer, often regarded as the first computer programmer for her work on Charles Babbage's Analytical Engine.",
  "Lovelace was born in London, the daughter of Lord Byron. She was educated in mathematics and science, unusual for women of her era, and became fascinated by Babbage's computing machines.",
  "Lovelace's notes on the Analytical Engine contained what is recognized as the first algorithm designed for implementation on a machine, making her a pioneer of computing.",
  [(1833, "Met Charles Babbage"), (1843, "Published notes on the Analytical Engine"), (1843, "Described the first computer algorithm")],
  [("Notes on the Analytical Engine", 1843, "Contained the first published computer algorithm")],
  [("The Analytical Engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves.", "Notes on the Analytical Engine")])

p("charles-babbage", "Charles Babbage", "チャールズ・バベッジ", 1791, 1871, ["gb"], ["engineering", "mathematics"],
  "Charles Babbage was an English polymath who originated the concept of a digital programmable computer with his Difference Engine and Analytical Engine designs.",
  "Babbage was born in London. He studied at Cambridge and became Lucasian Professor of Mathematics. He devoted much of his life to building his computing machines.",
  "Babbage's designs for mechanical computing engines anticipated modern computers by over a century. Though never completed in his lifetime, they established the principles of programmable computation.",
  [(1822, "Began design of the Difference Engine"), (1833, "Conceived the Analytical Engine"), (1837, "Published first description of the Analytical Engine")],
  [("Difference Engine", 1822, "Mechanical calculator designed to compute polynomial functions"), ("Analytical Engine", 1837, "Design for a general-purpose programmable computer")],
  [("Errors using inadequate data are much less than those using no data at all.", "Attributed")])

p("robert-goddard", "Robert H. Goddard", "ロバート・ゴダード", 1882, 1945, ["us"], ["engineering", "astronomy"],
  "Robert H. Goddard was an American engineer, professor, physicist, and inventor who is credited with creating and building the world's first liquid-fueled rocket.",
  "Goddard was born in Worcester, Massachusetts. He studied at Worcester Polytechnic Institute and Clark University, where he spent most of his career.",
  "Goddard's pioneering work with liquid-fueled rockets laid the foundation for the Space Age. His patents and experiments in rocketry made space travel possible.",
  [(1919, "Published A Method of Reaching Extreme Altitudes"), (1926, "Launched first liquid-fueled rocket"), (1935, "Launched rocket faster than the speed of sound")],
  [("First Liquid-Fueled Rocket", 1926, "Launch of the world's first liquid-fueled rocket in Auburn, Massachusetts")],
  [("It is difficult to say what is impossible, for the dream of yesterday is the hope of today and the reality of tomorrow.", "Attributed")])

p("norbert-wiener", "Norbert Wiener", "ノーバート・ウィーナー", 1894, 1964, ["us"], ["engineering", "mathematics"],
  "Norbert Wiener was an American mathematician and philosopher who established the science of cybernetics, the study of communication and control in animals and machines.",
  "Wiener was born in Columbia, Missouri. A child prodigy, he entered Tufts University at age 11 and earned his PhD from Harvard at age 18.",
  "Wiener's cybernetics — the study of feedback, communication, and control — influenced computer science, artificial intelligence, neuroscience, and systems theory.",
  [(1948, "Published Cybernetics"), (1950, "Published The Human Use of Human Beings"), (1960, "Continued work on stochastic processes")],
  [("Cybernetics", 1948, "Foundational work on communication and control in animals and machines")],
  [("The best material model of a cat is another, or preferably the same, cat.", "Cybernetics")])

p("claude-shannon", "Claude Shannon", "クロード・シャノン", 1916, 2001, ["us"], ["engineering", "mathematics"],
  "Claude Shannon was an American mathematician, electrical engineer, and cryptographer known as the father of information theory.",
  "Shannon was born in Petoskey, Michigan. He studied at the University of Michigan and MIT, where his master's thesis applied Boolean algebra to electrical circuits.",
  "Shannon's information theory provided the mathematical foundation for digital communication and computing. His work enabled the digital revolution.",
  [(1937, "Applied Boolean algebra to circuit design in master's thesis"), (1948, "Published A Mathematical Theory of Communication"), (1949, "Published Communication Theory of Secrecy Systems")],
  [("A Mathematical Theory of Communication", 1948, "Paper founding information theory")],
  [("Information is the resolution of uncertainty.", "A Mathematical Theory of Communication")])

p("hedy-lamarr", "Hedy Lamarr", "ヘディ・ラマー", 1914, 2000, ["at", "us"], ["engineering"],
  "Hedy Lamarr was an Austrian-American actress and inventor who co-developed a radio guidance system using frequency-hopping spread spectrum technology.",
  "Lamarr was born in Vienna, Austria. She became a famous Hollywood actress while also pursuing her interest in invention and engineering.",
  "Lamarr's frequency-hopping invention, initially designed for torpedo guidance, became the basis for modern wireless communications including Wi-Fi, Bluetooth, and GPS.",
  [(1933, "Starred in the controversial film Ecstasy"), (1937, "Fled Nazi-allied Austria for America"), (1942, "Patented frequency-hopping spread spectrum"), (1997, "Recognized by the Electronic Frontier Foundation")],
  [("Frequency-Hopping Spread Spectrum Patent", 1942, "Technology that became the basis for modern wireless communications")],
  [("Any girl can be glamorous. All you have to do is stand still and look stupid.", "Attributed")])

p("archimedes", "Archimedes", "アルキメデス", -287, -212, ["gr"], ["engineering", "mathematics", "physics"],
  "Archimedes was an ancient Greek mathematician, physicist, engineer, and astronomer, widely considered the greatest mathematician and scientist of antiquity.",
  "Archimedes was born in Syracuse, Sicily. He studied in Alexandria, Egypt, and returned to Syracuse, where he served King Hiero II as a scientist and engineer.",
  "Archimedes' discoveries in mathematics, physics, and engineering — including the lever, buoyancy principle, and the screw — form foundations of modern science.",
  [(-250, "Discovered the principle of buoyancy"), (-240, "Invented the Archimedes screw"), (-214, "Designed war machines to defend Syracuse"), (-212, "Killed during the Roman siege of Syracuse")],
  [("On Floating Bodies", -250, "Work establishing the principles of hydrostatics"), ("The Method of Mechanical Theorems", -250, "Application of mechanics to solve geometric problems")],
  [("Give me a lever long enough and a fulcrum on which to place it, and I shall move the world.", "Attributed by Pappus")])

p("konrad-zuse", "Konrad Zuse", "コンラート・ツーゼ", 1910, 1995, ["de"], ["engineering"],
  "Konrad Zuse was a German civil engineer, inventor, and computer pioneer who built the world's first programmable computer.",
  "Zuse was born in Berlin. He studied civil engineering and was frustrated by the tedious calculations required, motivating him to build computing machines.",
  "Zuse's Z3, completed in 1941, was the world's first working programmable, fully automatic digital computer. He also designed the first high-level programming language, Plankalkül.",
  [(1936, "Began building the Z1 computer"), (1941, "Completed the Z3, first programmable computer"), (1945, "Designed Plankalkül programming language"), (1949, "Founded Zuse KG computer company")],
  [("Z3 Computer", 1941, "World's first working programmable, fully automatic digital computer")],
  [("The belief in computing machines as the only form of machine intelligence is a fallacy.", "Attributed")])

p("katherine-johnson", "Katherine Johnson", "キャサリン・ジョンソン", 1918, 2020, ["us"], ["engineering", "mathematics"],
  "Katherine Johnson was an American mathematician whose calculations of orbital mechanics were critical to the success of the first U.S. crewed spaceflights.",
  "Johnson was born in White Sulphur Springs, West Virginia. A math prodigy, she graduated from college at 18 and joined NACA (later NASA) as a 'computer.'",
  "Johnson's trajectory calculations for the Mercury and Apollo programs were essential to putting Americans in space and on the Moon. Her story highlighted the contributions of Black women in STEM.",
  [(1953, "Joined NACA's all-black computing pool"), (1961, "Calculated trajectory for Alan Shepard's spaceflight"), (1962, "Verified computer calculations for John Glenn's orbit"), (1969, "Calculated trajectory for Apollo 11")],
  [("Apollo 11 Trajectory Calculations", 1969, "Orbital mechanics calculations that helped land humans on the Moon")],
  [("I counted everything. I counted the steps to the road, the steps up to church, the number of dishes and silverware I washed.", "Attributed")])

p("james-clerk-maxwell", "James Clerk Maxwell", "ジェームズ・クラーク・マクスウェル", 1831, 1879, ["gb"], ["physics", "engineering"],
  "James Clerk Maxwell was a Scottish mathematical physicist who formulated the classical theory of electromagnetic radiation, unifying electricity, magnetism, and light.",
  "Maxwell was born in Edinburgh, Scotland. He studied at the University of Edinburgh and Cambridge, where he was recognized as one of the most brilliant students ever.",
  "Maxwell's equations unified electricity, magnetism, and optics into a single framework, paving the way for radio, television, and all modern communications technology.",
  [(1855, "Published On Faraday's Lines of Force"), (1861, "Produced the first color photograph"), (1865, "Published A Dynamical Theory of the Electromagnetic Field"), (1873, "Published A Treatise on Electricity and Magnetism")],
  [("A Treatise on Electricity and Magnetism", 1873, "Comprehensive work presenting Maxwell's equations")],
  [("The scientific importance of a concept is not measured by the number of previous problems it solves but by the new problems it raises.", "Attributed")])

if __name__ == '__main__':
    write_people(P)
