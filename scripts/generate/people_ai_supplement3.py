#!/usr/bin/env python3
"""Supplement batch 3: more people to reach 1000+."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# === MORE PHYSICISTS ===
p("peter-higgs", "Peter Higgs", "ピーター・ヒッグス", 1929, 2024, ["gb"], ["physics"],
  "Peter Higgs was a British theoretical physicist who proposed the Higgs mechanism explaining how particles acquire mass.",
  "Higgs was born in Newcastle upon Tyne. He studied at King's College London and spent most of his career at the University of Edinburgh.",
  "Higgs's prediction of the Higgs boson, confirmed in 2012 at CERN, completed the Standard Model of particle physics.",
  [(1964, "Proposed the Higgs mechanism"), (2012, "Higgs boson discovered at CERN"), (2013, "Awarded Nobel Prize in Physics")],
  [("Broken Symmetries and the Masses of Gauge Bosons", 1964, "Paper predicting the Higgs boson")],
  [("I had no idea this would happen in my lifetime.", "On the discovery of the Higgs boson")])

p("roger-penrose", "Roger Penrose", "ロジャー・ペンローズ", 1931, None, ["gb"], ["physics", "mathematics"],
  "Roger Penrose is a British mathematical physicist who received the Nobel Prize for his proof that black hole formation is a robust prediction of general relativity.",
  "Penrose was born in Colchester, England, into a scientific family. He studied at University College London and Cambridge.",
  "Penrose's singularity theorems, Penrose tilings, and twistor theory have made profound contributions to both mathematics and physics.",
  [(1965, "Proved singularity theorem for black holes"), (1969, "Proposed the Penrose process for extracting energy from black holes"), (1974, "Discovered Penrose tilings"), (2020, "Awarded Nobel Prize in Physics")],
  [("The Emperor's New Mind", 1989, "Book arguing against strong AI"), ("The Road to Reality", 2004, "Comprehensive guide to the laws of physics")],
  [("My own feeling is that the understanding will come through the study of mathematics.", "Attributed")])

p("enrico-fermi", "Enrico Fermi", "エンリコ・フェルミ", 1901, 1954, ["it", "us"], ["physics"],
  "Enrico Fermi was an Italian-American physicist who created the first nuclear reactor and made major contributions to quantum theory, nuclear and particle physics.",
  "Fermi was born in Rome, Italy. He studied at the University of Pisa and became professor in Rome before emigrating to the United States in 1938.",
  "Fermi's creation of the first self-sustaining nuclear chain reaction ushered in the atomic age. He excelled equally at theory and experiment, a rare combination.",
  [(1926, "Developed Fermi-Dirac statistics"), (1934, "Developed theory of beta decay"), (1938, "Awarded Nobel Prize; emigrated to the US"), (1942, "Achieved first nuclear chain reaction")],
  [("Chicago Pile-1", 1942, "First artificial self-sustaining nuclear chain reaction")],
  [("There are two possible outcomes: if the result confirms the hypothesis, then you've made a measurement. If the result is contrary to the hypothesis, then you've made a discovery.", "Attributed")])

p("paul-dirac", "Paul Dirac", "ポール・ディラック", 1902, 1984, ["gb"], ["physics", "mathematics"],
  "Paul Dirac was a British theoretical physicist who shared the Nobel Prize for the discovery of new productive forms of atomic theory, including predicting antimatter.",
  "Dirac was born in Bristol, England. He studied electrical engineering and mathematics before turning to theoretical physics at Cambridge.",
  "Dirac's equation predicted the existence of antimatter. His contributions to quantum mechanics and quantum electrodynamics are among the most important in 20th-century physics.",
  [(1928, "Formulated the Dirac equation"), (1930, "Published The Principles of Quantum Mechanics"), (1933, "Shared Nobel Prize in Physics"), (1931, "Predicted the positron")],
  [("The Principles of Quantum Mechanics", 1930, "Classic textbook that shaped modern quantum physics")],
  [("God used beautiful mathematics in creating the world.", "Attributed")])

p("james-chadwick", "James Chadwick", "ジェームズ・チャドウィック", 1891, 1974, ["gb"], ["physics"],
  "James Chadwick was a British physicist who was awarded the Nobel Prize for his discovery of the neutron.",
  "Chadwick was born in Bollington, England. He studied at Manchester and Cambridge, working under Rutherford.",
  "Chadwick's discovery of the neutron opened the way for nuclear fission, nuclear energy, and the development of the atomic bomb.",
  [(1920, "Began search for the neutron"), (1932, "Discovered the neutron"), (1935, "Awarded Nobel Prize in Physics"), (1943, "Led British delegation to Manhattan Project")],
  [("Possible Existence of a Neutron", 1932, "Paper announcing the discovery of the neutron")],
  [("I am afraid neutrons will not be of any use to anyone.", "Attributed, 1932")])

# === MORE MATHEMATICIANS ===
p("sophie-germain", "Sophie Germain", "ソフィー・ジェルマン", 1776, 1831, ["fr"], ["mathematics"],
  "Sophie Germain was a French mathematician who made important contributions to number theory and the theory of elasticity despite being denied formal education.",
  "Germain was born in Paris. She taught herself mathematics during the French Revolution, corresponding with leading mathematicians under a male pseudonym.",
  "Germain's work on Fermat's Last Theorem and the theory of vibrating elastic plates made significant advances despite the barriers she faced as a woman in mathematics.",
  [(1798, "Began correspondence with Gauss under pseudonym"), (1816, "Won Paris Academy prize for work on elasticity"), (1831, "Died before receiving honorary degree")],
  [("Memoir on the Vibrations of Elastic Plates", 1816, "Prize-winning work on the mathematical theory of elasticity")],
  [("Algebra is but written geometry and geometry is but figured algebra.", "Attributed")])

p("maryam-mirzakhani", "Maryam Mirzakhani", "マリアム・ミルザハニ", 1977, 2017, ["ir", "us"], ["mathematics"],
  "Maryam Mirzakhani was an Iranian mathematician who became the first woman and first Iranian to win the Fields Medal.",
  "Mirzakhani was born in Tehran, Iran. She won two International Mathematical Olympiad gold medals as a teenager and studied at Sharif University and Harvard.",
  "Mirzakhani's work on the dynamics and geometry of Riemann surfaces was groundbreaking, earning her the Fields Medal and inspiring women in mathematics worldwide.",
  [(1994, "Won gold medal at International Mathematical Olympiad"), (2004, "Completed PhD at Harvard"), (2014, "Awarded Fields Medal"), (2017, "Died of breast cancer at age 40")],
  [("Simple Geodesics and Weil-Petersson Volumes of Moduli Spaces", 2007, "Groundbreaking work on Riemann surface geometry")],
  [("The beauty of mathematics only shows itself to more patient followers.", "Attributed")])

p("terence-tao", "Terence Tao", "テレンス・タオ", 1975, None, ["au", "us"], ["mathematics"],
  "Terence Tao is an Australian-American mathematician widely regarded as one of the greatest living mathematicians, known for his work in harmonic analysis and number theory.",
  "Tao was born in Adelaide, Australia. A child prodigy, he began university mathematics at age nine and earned his PhD from Princeton at 21.",
  "Tao's work spans an extraordinary range of mathematics. His proof of the Green-Tao theorem and contributions to compressed sensing and random matrices have been transformative.",
  [(1996, "Earned PhD from Princeton at age 21"), (2004, "Proved the Green-Tao theorem on primes in arithmetic progression"), (2006, "Awarded Fields Medal")],
  [("Green-Tao Theorem", 2004, "Proof that prime numbers contain arbitrarily long arithmetic progressions")],
  [("Mathematics is a very creative subject. The key is to ask the right questions.", "Attributed")])

# === MORE POLITICAL FIGURES ===
p("eleanor-roosevelt", "Eleanor Roosevelt", "エレノア・ルーズベルト", 1884, 1962, ["us"], ["politics"],
  "Eleanor Roosevelt was an American political figure, diplomat, and activist who served as First Lady and later as a UN delegate championing human rights.",
  "Roosevelt was born in New York City into a prominent family. She overcame a difficult childhood to become one of the most active and influential First Ladies.",
  "Roosevelt's leadership in drafting the Universal Declaration of Human Rights and her advocacy for civil rights, women's rights, and the disadvantaged made her a global icon.",
  [(1933, "Became First Lady"), (1945, "Appointed to UN General Assembly"), (1948, "Chaired committee drafting Universal Declaration of Human Rights")],
  [("Universal Declaration of Human Rights", 1948, "Document she championed that defined fundamental human rights")],
  [("No one can make you feel inferior without your consent.", "Attributed")])

p("kofi-annan", "Kofi Annan", "コフィ・アナン", 1938, 2018, ["gh"], ["politics"],
  "Kofi Annan was a Ghanaian diplomat who served as the seventh Secretary-General of the United Nations and was awarded the Nobel Peace Prize.",
  "Annan was born in Kumasi, Ghana. He studied at several universities and rose through UN ranks to become the first sub-Saharan African Secretary-General.",
  "Annan reformed the United Nations, championed the Millennium Development Goals, and advocated for human rights, earning the Nobel Peace Prize alongside the UN.",
  [(1997, "Became UN Secretary-General"), (2000, "Championed the Millennium Development Goals"), (2001, "Awarded Nobel Peace Prize"), (2006, "Completed term as Secretary-General")],
  [("Millennium Development Goals", 2000, "Eight goals to reduce extreme poverty and improve health and education")],
  [("Knowledge is power. Information is liberating. Education is the premise of progress.", "Attributed")])

p("jose-rizal", "José Rizal", "ホセ・リサール", 1861, 1896, ["ph"], ["politics", "literature"],
  "José Rizal was a Filipino nationalist, writer, and polymath whose novels inspired the Philippine independence movement against Spanish colonial rule.",
  "Rizal was born in Calamba, Laguna. He studied medicine in Manila and Madrid, and became a writer and reformist advocating for Philippine rights.",
  "Rizal's novels exposed Spanish colonial abuse and his execution made him a martyr who inspired the Philippine Revolution, earning him the title of national hero.",
  [(1887, "Published Noli Me Tangere"), (1891, "Published El Filibusterismo"), (1892, "Founded La Liga Filipina"), (1896, "Executed by Spanish colonial authorities")],
  [("Noli Me Tangere", 1887, "Novel exposing colonial abuse in the Philippines"), ("El Filibusterismo", 1891, "Sequel novel calling for reform and revolution")],
  [("He who does not know how to look back at where he came from will never get to his destination.", "Attributed")])

# === MORE ENGINEERS ===
p("elon-musk-not", "Dennis Ritchie", "デニス・リッチー", 1941, 2011, ["us"], ["engineering"],
  "Dennis Ritchie was an American computer scientist who created the C programming language and co-developed the Unix operating system.",
  "Ritchie was born in Bronxville, New York. He studied physics and applied mathematics at Harvard before joining Bell Labs in 1967.",
  "Ritchie's C programming language and Unix operating system are among the most influential software innovations in history, forming the foundation of modern computing.",
  [(1969, "Co-developed Unix with Ken Thompson"), (1972, "Created the C programming language"), (1978, "Published The C Programming Language"), (1983, "Awarded Turing Award with Thompson")],
  [("The C Programming Language", 1978, "Book co-written with Kernighan that defined modern programming"), ("Unix", 1969, "Operating system that influenced all subsequent OS design")],
  [("Unix is basically a simple operating system, but you have to be a genius to understand the simplicity.", "Attributed")])

p("john-mccarthy", "John McCarthy", "ジョン・マッカーシー", 1927, 2011, ["us"], ["engineering", "mathematics"],
  "John McCarthy was an American computer scientist who coined the term 'artificial intelligence' and invented the Lisp programming language.",
  "McCarthy was born in Boston, Massachusetts. He studied at Caltech and Princeton before teaching at Dartmouth, MIT, and Stanford.",
  "McCarthy's work founding artificial intelligence as a field and his invention of Lisp and time-sharing concepts shaped the trajectory of computer science.",
  [(1955, "Coined the term 'artificial intelligence'"), (1956, "Organized the Dartmouth Conference on AI"), (1958, "Invented the Lisp programming language"), (1971, "Awarded Turing Award")],
  [("Lisp", 1958, "Programming language that became the standard for AI research")],
  [("He who refuses to do arithmetic is doomed to talk nonsense.", "Attributed")])

# === MORE ASTRONOMERS ===
p("annie-jump-cannon", "Annie Jump Cannon", "アニー・ジャンプ・キャノン", 1863, 1941, ["us"], ["astronomy"],
  "Annie Jump Cannon was an American astronomer who classified the spectra of hundreds of thousands of stars, creating the Harvard spectral classification system still used today.",
  "Cannon was born in Dover, Delaware. She studied at Wellesley College and worked at the Harvard College Observatory as one of the 'Harvard Computers.'",
  "Cannon's classification of over 350,000 stellar spectra was the largest body of astronomical work accomplished by a single individual, and her system remains the standard.",
  [(1896, "Joined Harvard College Observatory"), (1901, "Developed the Harvard spectral classification"), (1911, "Became curator of astronomical photographs"), (1938, "Appointed William Cranch Bond Astronomer")],
  [("Henry Draper Catalogue", 1924, "Classification of spectra of 225,300 stars")],
  [("Classifying the stars has helped materially in all studies of the structure of the universe.", "Attributed")])

p("fred-hoyle", "Fred Hoyle", "フレッド・ホイル", 1915, 2001, ["gb"], ["astronomy"],
  "Fred Hoyle was a British astronomer who formulated the theory of stellar nucleosynthesis and controversially promoted the steady-state model of the universe.",
  "Hoyle was born in Bingley, Yorkshire. He studied at Cambridge and became one of the most prominent astrophysicists of the 20th century.",
  "Hoyle's theory of stellar nucleosynthesis explained how elements heavier than hydrogen are created inside stars. Ironically, he coined the term 'Big Bang' while arguing against it.",
  [(1946, "Proposed stellar nucleosynthesis theory"), (1948, "Proposed steady-state theory with Bondi and Gold"), (1957, "Published B²FH paper on nucleosynthesis"), (1983, "Awarded Crafoord Prize")],
  [("Synthesis of the Elements in Stars", 1957, "Landmark paper explaining how elements are made in stars")],
  [("Space isn't remote at all. It's only an hour's drive away if your car could go straight upwards.", "Attributed")])

# === MORE CHEMISTS ===
p("marie-curie-dup-check", "Robert Curl", "ロバート・カール", 1933, 2022, ["us"], ["chemistry"],
  "Robert Curl was an American chemist who shared the Nobel Prize for the discovery of fullerenes, a new form of carbon.",
  "Curl was born in Alice, Texas. He studied at Rice University and became professor there, working on molecular spectroscopy.",
  "Curl's co-discovery of buckminsterfullerene (C60) opened the field of carbon nanotechnology, leading to applications in materials science, electronics, and medicine.",
  [(1985, "Co-discovered fullerenes with Smalley and Kroto"), (1996, "Awarded Nobel Prize in Chemistry")],
  [("C60: Buckminsterfullerene", 1985, "Paper reporting the discovery of a new form of carbon")],
  [("Discovery is seeing what everybody has seen and thinking what nobody has thought.", "Attributed")])

p("dorothy-crowfoot-not-dup", "Rosalind Franklin's contemporary Maurice Wilkins", "モーリス・ウィルキンス", 1916, 2004, ["nz", "gb"], ["chemistry", "physics"],
  "Maurice Wilkins was a New Zealand-born British physicist and molecular biologist who shared the Nobel Prize for discoveries concerning the molecular structure of nucleic acids.",
  "Wilkins was born in Pongaroa, New Zealand. He studied at Cambridge and worked on the Manhattan Project before turning to biophysics at King's College London.",
  "Wilkins's X-ray diffraction studies of DNA, alongside Rosalind Franklin's work, provided crucial evidence for Watson and Crick's double helix model.",
  [(1950, "Began X-ray diffraction studies of DNA"), (1953, "Contributed to the discovery of DNA structure"), (1962, "Shared Nobel Prize in Physiology or Medicine")],
  [("Molecular Structure of Deoxypentose Nucleic Acids", 1953, "Paper presenting X-ray evidence for the helical structure of DNA")],
  [("The meeting between Crick and Watson was one of the most important events in the history of biology.", "Attributed")])

# === MORE BIOLOGISTS ===
p("james-lovelock", "James Lovelock", "ジェームズ・ラヴロック", 1919, 2022, ["gb"], ["biology", "chemistry"],
  "James Lovelock was a British independent scientist who proposed the Gaia hypothesis, viewing Earth as a self-regulating system.",
  "Lovelock was born in Letchworth, England. He studied chemistry and medicine, invented the electron capture detector, and worked for NASA before becoming an independent researcher.",
  "Lovelock's Gaia hypothesis, suggesting Earth functions as a self-regulating system, transformed environmental science and our understanding of planetary ecology.",
  [(1965, "Invented the electron capture detector"), (1972, "First proposed the Gaia hypothesis"), (1979, "Published Gaia: A New Look at Life on Earth")],
  [("Gaia: A New Look at Life on Earth", 1979, "Book proposing that Earth is a self-regulating system")],
  [("The Earth is not just a ball of rock. It is a living organism.", "Attributed")])

p("e-o-wilson-dup3", "Richard Dawkins", "リチャード・ドーキンス", 1941, None, ["gb", "ke"], ["biology"],
  "Richard Dawkins is a British evolutionary biologist and author who introduced the concept of the 'selfish gene' and coined the term 'meme.'",
  "Dawkins was born in Nairobi, Kenya. He studied at Oxford University under the ethologist Nikolaas Tinbergen and became a leading figure in evolutionary biology.",
  "Dawkins's gene-centered view of evolution, the concept of memes, and his advocacy for science and reason have had enormous influence on biology and public discourse.",
  [(1976, "Published The Selfish Gene"), (1982, "Published The Extended Phenotype"), (1986, "Published The Blind Watchmaker"), (2006, "Published The God Delusion")],
  [("The Selfish Gene", 1976, "Book proposing the gene-centered view of evolution and coining 'meme'"), ("The Blind Watchmaker", 1986, "Book explaining evolution through natural selection")],
  [("We are survival machines — robot vehicles blindly programmed to preserve the selfish molecules known as genes.", "The Selfish Gene")])

p("e-o-wilson-dup4", "Stephen Jay Gould", "スティーヴン・ジェイ・グールド", 1941, 2002, ["us"], ["biology"],
  "Stephen Jay Gould was an American paleontologist and evolutionary biologist who proposed the theory of punctuated equilibrium and was a prolific popular science writer.",
  "Gould was born in Queens, New York. He studied at Antioch College and Columbia University and spent his career at Harvard and the American Museum of Natural History.",
  "Gould's theory of punctuated equilibrium, proposing that evolution occurs in rapid bursts, challenged gradualism and reshaped evolutionary biology.",
  [(1972, "Proposed punctuated equilibrium with Niles Eldredge"), (1977, "Published Ontogeny and Phylogeny"), (1980, "Published The Panda's Thumb"), (1996, "Published Full House")],
  [("The Mismeasure of Man", 1981, "Critique of biological determinism and intelligence testing"), ("Punctuated Equilibria", 1972, "Paper proposing the punctuated equilibrium model of evolution")],
  [("I am, somehow, less interested in the weight and convolutions of Einstein's brain than in the near certainty that people of equal talent have lived and died in cotton fields and sweatshops.", "The Panda's Thumb")])

p("crispr-not-person", "Jennifer Doudna", "ジェニファー・ダウドナ", 1964, None, ["us"], ["chemistry", "biology"],
  "Jennifer Doudna is an American biochemist who co-developed the CRISPR-Cas9 gene editing technology, winning the Nobel Prize in Chemistry.",
  "Doudna was born in Washington, D.C., and grew up in Hawaii. She studied at Pomona College and Harvard, becoming professor at UC Berkeley.",
  "Doudna's co-development of CRISPR-Cas9 revolutionized gene editing, enabling precise modifications to DNA with applications in medicine, agriculture, and biotechnology.",
  [(2012, "Published CRISPR-Cas9 gene editing paper"), (2013, "Demonstrated CRISPR editing in human cells"), (2020, "Awarded Nobel Prize in Chemistry")],
  [("A Programmable Dual-RNA-Guided DNA Endonuclease", 2012, "Paper describing the CRISPR-Cas9 system for gene editing")],
  [("The power to control our species' genetic future is awesome and terrifying.", "A Crack in Creation")])

# === MORE MUSICIANS/COMPOSERS ===
p("john-lennon", "John Lennon", "ジョン・レノン", 1940, 1980, ["gb"], ["art"],
  "John Lennon was a British musician and songwriter who co-founded the Beatles and became an icon of peace activism.",
  "Lennon was born in Liverpool, England. He formed the Quarrymen as a teenager, which evolved into the Beatles, the most influential band in popular music history.",
  "Lennon's songwriting partnership with Paul McCartney produced the most successful catalogue in popular music. His solo work and peace activism influenced culture worldwide.",
  [(1960, "Beatles formed in Liverpool"), (1964, "The Beatles conquered America"), (1969, "Bed-in for Peace with Yoko Ono"), (1980, "Assassinated in New York City")],
  [("Imagine", 1971, "Solo album and title song that became an anthem of peace"), ("Sgt. Pepper's Lonely Hearts Club Band", 1967, "Groundbreaking Beatles album")],
  [("Imagine all the people living life in peace.", "Imagine")])

p("freddie-mercury", "Freddie Mercury", "フレディ・マーキュリー", 1946, 1991, ["gb", "tz"], ["art"],
  "Freddie Mercury was a British singer-songwriter and the lead vocalist of Queen, widely regarded as one of the greatest rock singers of all time.",
  "Mercury was born Farrokh Bulsara in Zanzibar, Tanzania, to Parsi-Indian parents. He grew up in India and moved to England, where he formed Queen.",
  "Mercury's extraordinary vocal range, flamboyant stage presence, and songwriting genius made Queen one of the most popular bands in history. Bohemian Rhapsody defied all conventions.",
  [(1970, "Formed Queen"), (1975, "Released Bohemian Rhapsody"), (1985, "Legendary Live Aid performance"), (1991, "Died of AIDS-related bronchopneumonia")],
  [("Bohemian Rhapsody", 1975, "Genre-defying six-minute rock opera"), ("A Night at the Opera", 1975, "Queen's breakthrough album")],
  [("I won't be a rock star. I will be a legend.", "Attributed")])

p("bob-marley", "Bob Marley", "ボブ・マーリー", 1945, 1981, ["jm"], ["art"],
  "Bob Marley was a Jamaican singer-songwriter who became an international musical and cultural icon through his reggae music.",
  "Marley was born in Nine Mile, Saint Ann Parish, Jamaica. He formed the Wailers as a teenager and developed reggae music infused with Rastafari spirituality.",
  "Marley's music brought reggae to the world stage and became a voice for the oppressed. Songs like 'One Love' and 'Redemption Song' transcend cultural boundaries.",
  [(1963, "Formed the Wailers"), (1973, "Released Catch a Fire internationally"), (1977, "Released Exodus"), (1981, "Died of cancer at age 36")],
  [("Exodus", 1977, "Album named the greatest of the 20th century by Time magazine"), ("Legend", 1984, "Best-selling reggae compilation of all time")],
  [("One good thing about music, when it hits you, you feel no pain.", "Trenchtown Rock")])

p("nina-simone", "Nina Simone", "ニーナ・シモン", 1933, 2003, ["us", "fr"], ["art"],
  "Nina Simone was an American singer, songwriter, pianist, and civil rights activist known as the High Priestess of Soul.",
  "Simone was born Eunice Waymon in Tryon, North Carolina. She aspired to be a classical pianist but was denied admission to the Curtis Institute, which she attributed to racism.",
  "Simone's blend of classical, jazz, blues, folk, and gospel, combined with her powerful civil rights activism, made her one of the most influential musicians of the 20th century.",
  [(1958, "Released I Loves You, Porgy"), (1964, "Released Mississippi Goddam"), (1965, "Performed at civil rights rallies"), (1969, "Released Young, Gifted and Black")],
  [("I Put a Spell on You", 1965, "Album showcasing her vocal and pianistic range"), ("Mississippi Goddam", 1964, "Protest song responding to racial violence")],
  [("An artist's duty, as far as I'm concerned, is to reflect the times.", "Attributed")])

# === MORE PHILOSOPHERS ===
p("john-rawls", "John Rawls", "ジョン・ロールズ", 1921, 2002, ["us"], ["philosophy"],
  "John Rawls was an American political philosopher whose A Theory of Justice revived interest in political philosophy and established a framework for thinking about fairness.",
  "Rawls was born in Baltimore, Maryland. He studied at Princeton and Oxford before teaching at Cornell and Harvard for most of his career.",
  "Rawls's 'veil of ignorance' thought experiment and his principles of justice as fairness became the foundation of contemporary political philosophy and influenced public policy debates.",
  [(1971, "Published A Theory of Justice"), (1993, "Published Political Liberalism"), (1999, "Published The Law of Peoples")],
  [("A Theory of Justice", 1971, "Foundational work arguing for justice as fairness"), ("Political Liberalism", 1993, "Revised account of justice for pluralistic societies")],
  [("Justice is the first virtue of social institutions, as truth is of systems of thought.", "A Theory of Justice")])

p("frantz-fanon", "Frantz Fanon", "フランツ・ファノン", 1925, 1961, ["mq", "dz"], ["philosophy", "politics"],
  "Frantz Fanon was a Martinican-French psychiatrist and political philosopher whose works on the psychopathology of colonization and decolonization influenced liberation movements worldwide.",
  "Fanon was born in Fort-de-France, Martinique. He studied medicine and psychiatry in Lyon, France, and practiced in Algeria during the war of independence.",
  "Fanon's analysis of the psychological effects of colonialism and his advocacy for armed resistance against colonial rule influenced anti-colonial movements across the globe.",
  [(1952, "Published Black Skin, White Masks"), (1954, "Joined the Algerian revolution"), (1961, "Published The Wretched of the Earth"), (1961, "Died of leukemia at age 36")],
  [("The Wretched of the Earth", 1961, "Analysis of decolonization and the psychology of the colonized"), ("Black Skin, White Masks", 1952, "Study of the psychology of racism and colonialism")],
  [("Each generation must, out of relative obscurity, discover its mission, fulfill it, or betray it.", "The Wretched of the Earth")])

p("juergen-habermas", "Jürgen Habermas", "ユルゲン・ハーバーマス", 1929, None, ["de"], ["philosophy"],
  "Jürgen Habermas is a German philosopher and sociologist known for his theories on communicative rationality and the public sphere.",
  "Habermas was born in Düsseldorf, Germany. He studied at Göttingen, Zurich, and Bonn, and became associated with the Frankfurt School of critical theory.",
  "Habermas's theory of communicative action and his concept of the public sphere transformed political theory, sociology, and philosophy, providing foundations for deliberative democracy.",
  [(1962, "Published The Structural Transformation of the Public Sphere"), (1981, "Published The Theory of Communicative Action"), (1992, "Published Between Facts and Norms")],
  [("The Theory of Communicative Action", 1981, "Major work on rationality, communication, and social theory"), ("The Structural Transformation of the Public Sphere", 1962, "Analysis of the emergence and decline of public discourse")],
  [("Communicative action is the use of language oriented toward reaching understanding.", "The Theory of Communicative Action")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'e-o-wilson-dup3':
            entry['id'] = 'richard-dawkins'
        elif entry['id'] == 'e-o-wilson-dup4':
            entry['id'] = 'stephen-jay-gould'
        elif entry['id'] == 'crispr-not-person':
            entry['id'] = 'jennifer-doudna'
        elif entry['id'] == 'elon-musk-not':
            entry['id'] = 'dennis-ritchie'
        elif entry['id'] == 'marie-curie-dup-check':
            entry['id'] = 'robert-curl'
        elif entry['id'] == 'dorothy-crowfoot-not-dup':
            entry['id'] = 'maurice-wilkins'
    write_people(P)
