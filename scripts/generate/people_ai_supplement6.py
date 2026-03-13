#!/usr/bin/env python3
"""Supplement batch 6: final 200+ to reach 1000."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# === MIXED: MORE WRITERS, PHILOSOPHERS, POLITICAL FIGURES, SCIENTISTS ===
p("alexander-pushkin", "Alexander Pushkin", "アレクサンドル・プーシキン", 1799, 1837, ["ru"], ["literature"],
  "Alexander Pushkin was a Russian poet and writer who is considered the greatest Russian poet and the founder of modern Russian literature.",
  "Pushkin was born in Moscow into a noble family. He attended the Imperial Lyceum and published his first poem at age 15.",
  "Pushkin created the standard for modern Russian literary language. Eugene Onegin and his poetry are central to Russian cultural identity.",
  [(1820, "Published Ruslan and Ludmila"), (1825, "Completed Boris Godunov"), (1833, "Published Eugene Onegin"), (1837, "Killed in a duel at age 37")],
  [("Eugene Onegin", 1833, "Novel in verse that defined Russian literature")],
  [("I loved you; and perhaps I love you still.", "I Loved You")])

p("leo-tolstoy", "Leo Tolstoy", "レフ・トルストイ", 1828, 1910, ["ru"], ["literature", "philosophy"],
  "Leo Tolstoy was a Russian writer who is considered one of the greatest authors of all time, known for War and Peace and Anna Karenina.",
  "Tolstoy was born into an aristocratic family at Yasnaya Polyana. He served in the army and traveled before devoting himself to literature and later to moral philosophy.",
  "Tolstoy's novels are pinnacles of world literature. His later moral and religious philosophy of nonviolent resistance influenced Gandhi and Martin Luther King Jr.",
  [(1863, "Published War and Peace"), (1877, "Published Anna Karenina"), (1886, "Published The Death of Ivan Ilyich"), (1910, "Died at a railway station while fleeing his estate")],
  [("War and Peace", 1869, "Epic novel of Russian society during the Napoleonic Wars"), ("Anna Karenina", 1877, "Novel of love and society in Russian aristocracy")],
  [("All happy families are alike; each unhappy family is unhappy in its own way.", "Anna Karenina")])

p("anton-chekhov", "Anton Chekhov", "アントン・チェーホフ", 1860, 1904, ["ru"], ["literature"],
  "Anton Chekhov was a Russian playwright and short story writer, regarded as one of the greatest writers of short fiction and one of the greatest dramatists.",
  "Chekhov was born in Taganrog, Russia. He studied medicine and practiced as a doctor while writing stories and plays.",
  "Chekhov transformed drama and the short story with his subtle psychological insights and his rejection of conventional dramatic structure.",
  [(1888, "Published The Steppe"), (1896, "Premiered The Seagull"), (1901, "Premiered Three Sisters"), (1904, "Premiered The Cherry Orchard")],
  [("The Cherry Orchard", 1904, "Play about the decline of the Russian aristocracy"), ("The Seagull", 1896, "Play exploring art, love, and failure")],
  [("Medicine is my lawful wife and literature is my mistress.", "Letter, 1888")])

p("gustave-flaubert", "Gustave Flaubert", "ギュスターヴ・フローベール", 1821, 1880, ["fr"], ["literature"],
  "Gustave Flaubert was a French novelist considered one of the most influential Western novelists, known for his meticulous literary style.",
  "Flaubert was born in Rouen, France. He studied law in Paris but abandoned it for literature, spending years perfecting his prose.",
  "Flaubert's obsessive pursuit of le mot juste (the right word) and his objective narration in Madame Bovary established the modern novel.",
  [(1857, "Published Madame Bovary"), (1862, "Published Salammbô"), (1869, "Published Sentimental Education")],
  [("Madame Bovary", 1857, "Novel about a provincial doctor's wife that defined literary realism")],
  [("The art of writing is the art of discovering what you believe.", "Attributed")])

p("thomas-mann", "Thomas Mann", "トーマス・マン", 1875, 1955, ["de", "us"], ["literature"],
  "Thomas Mann was a German novelist and Nobel laureate whose works explored bourgeois life, art, and the German condition.",
  "Mann was born in Lübeck, Germany. He published Buddenbrooks at age 25 and became Germany's most prominent writer before fleeing the Nazis.",
  "Mann's novels, combining irony with philosophical depth, examined the tensions between art and life, sickness and health, and the crisis of European civilization.",
  [(1901, "Published Buddenbrooks"), (1924, "Published The Magic Mountain"), (1929, "Awarded Nobel Prize in Literature"), (1947, "Published Doctor Faustus")],
  [("Buddenbrooks", 1901, "Novel about the decline of a merchant family"), ("The Magic Mountain", 1924, "Novel set in a sanatorium exploring European intellectual life")],
  [("A writer is someone for whom writing is more difficult than it is for other people.", "Attributed")])

p("italo-calvino", "Italo Calvino", "イタロ・カルヴィーノ", 1923, 1985, ["it", "cu"], ["literature"],
  "Italo Calvino was an Italian journalist and writer of short stories and novels known for his imaginative fantasy and postmodern narratives.",
  "Calvino was born in Santiago de Las Vegas, Cuba, and grew up in Italy. He fought in the Italian Resistance and became one of Italy's most important postwar writers.",
  "Calvino's inventive fiction, blending fantasy, science, and literary experimentation, made him one of the most original writers of the 20th century.",
  [(1947, "Published The Path to the Nest of Spiders"), (1956, "Published Italian Folktales"), (1972, "Published Invisible Cities"), (1979, "Published If on a winter's night a traveler")],
  [("Invisible Cities", 1972, "Novel of imaginary cities described by Marco Polo to Kublai Khan"), ("If on a winter's night a traveler", 1979, "Postmodern novel about the act of reading")],
  [("A classic is a book that has never finished saying what it has to say.", "Why Read the Classics?")])

p("octavio-paz", "Octavio Paz", "オクタビオ・パス", 1914, 1998, ["mx"], ["literature"],
  "Octavio Paz was a Mexican poet and diplomat who won the Nobel Prize in Literature, known for his exploration of Mexican identity and culture.",
  "Paz was born in Mexico City. He studied law and literature and became involved in leftist politics before pursuing a diplomatic career.",
  "Paz's poetry and essays explored Mexican identity, love, and solitude. The Labyrinth of Solitude is essential reading for understanding Mexico.",
  [(1950, "Published The Labyrinth of Solitude"), (1957, "Published Sun Stone"), (1990, "Awarded Nobel Prize in Literature")],
  [("The Labyrinth of Solitude", 1950, "Essay on Mexican identity and culture"), ("Sun Stone", 1957, "Epic poem on Mexican history and the Aztec calendar")],
  [("Solitude is the profoundest fact of the human condition.", "The Labyrinth of Solitude")])

p("pablo-neruda", "Pablo Neruda", "パブロ・ネルーダ", 1904, 1973, ["cl"], ["literature"],
  "Pablo Neruda was a Chilean poet-diplomat and politician who won the Nobel Prize in Literature, considered one of the greatest Spanish-language poets.",
  "Neruda was born Neftalí Reyes Basoalto in Parral, Chile. He published his first poetry at age 13 and adopted the pen name Pablo Neruda.",
  "Neruda's poetry, spanning love lyrics, political verse, and surrealist imagery, made him one of the most widely read poets of the 20th century.",
  [(1924, "Published Twenty Love Poems and a Song of Despair"), (1950, "Published Canto General"), (1971, "Awarded Nobel Prize in Literature")],
  [("Twenty Love Poems and a Song of Despair", 1924, "Love poetry collection that became a global bestseller"), ("Canto General", 1950, "Epic poem about Latin American history")],
  [("I love you without knowing how, or when, or from where.", "Sonnet XVII")])

p("derek-walcott", "Derek Walcott", "デレク・ウォルコット", 1930, 2017, ["lc"], ["literature"],
  "Derek Walcott was a Saint Lucian poet and playwright who won the Nobel Prize in Literature for his luminous, multicultural body of work.",
  "Walcott was born in Castries, Saint Lucia. He studied at the University of the West Indies and spent his career between the Caribbean and the United States.",
  "Walcott's poetry fused Caribbean, African, and European traditions, creating a unique literary voice that captured the complexities of postcolonial identity.",
  [(1962, "Published In a Green Night"), (1990, "Published Omeros"), (1992, "Awarded Nobel Prize in Literature")],
  [("Omeros", 1990, "Epic poem reimagining Homer in the Caribbean")],
  [("The English language is nobody's special property. It is the property of the imagination.", "Attributed")])

# === MORE SCIENTISTS AND THINKERS ===
p("alfred-north-whitehead", "Alfred North Whitehead", "アルフレッド・ノース・ホワイトヘッド", 1861, 1947, ["gb", "us"], ["mathematics", "philosophy"],
  "Alfred North Whitehead was a British mathematician and philosopher who co-authored Principia Mathematica and developed process philosophy.",
  "Whitehead was born in Ramsgate, England. He studied and taught at Cambridge before moving to Harvard, where he developed his philosophical system.",
  "Whitehead's Principia Mathematica (with Russell) was a landmark in mathematical logic. His later process philosophy offered a new metaphysical framework.",
  [(1910, "Published Principia Mathematica with Russell"), (1924, "Joined Harvard's philosophy department"), (1929, "Published Process and Reality")],
  [("Principia Mathematica", 1910, "Monumental work in mathematical logic co-authored with Bertrand Russell"), ("Process and Reality", 1929, "Major work of process philosophy")],
  [("The art of progress is to preserve order amid change and to preserve change amid order.", "Attributed")])

p("bertrand-russell", "Bertrand Russell", "バートランド・ラッセル", 1872, 1970, ["gb"], ["mathematics", "philosophy"],
  "Bertrand Russell was a British philosopher, logician, and social critic who won the Nobel Prize in Literature and co-authored Principia Mathematica.",
  "Russell was born into the British aristocracy. He studied at Cambridge and became one of the most prominent intellectuals of the 20th century.",
  "Russell's work in mathematical logic and his advocacy for peace, civil liberties, and social justice made him one of the most influential thinkers of the 20th century.",
  [(1903, "Published The Principles of Mathematics"), (1910, "Published Principia Mathematica"), (1950, "Awarded Nobel Prize in Literature"), (1955, "Issued Russell-Einstein Manifesto")],
  [("Principia Mathematica", 1910, "Foundational work in mathematical logic"), ("A History of Western Philosophy", 1945, "Comprehensive survey of Western philosophical thought")],
  [("The good life is one inspired by love and guided by knowledge.", "What I Believe")])

p("karl-marx", "Karl Marx", "カール・マルクス", 1818, 1883, ["de", "gb"], ["philosophy", "politics"],
  "Karl Marx was a German philosopher, economist, and revolutionary socialist whose works formed the basis of communism.",
  "Marx was born in Trier, Prussia. He studied law and philosophy in Bonn and Berlin, became a journalist, and was exiled to London, where he spent the rest of his life.",
  "Marx's analysis of capitalism, historical materialism, and class struggle transformed politics, economics, and social thought. His ideas shaped the 20th century.",
  [(1848, "Published The Communist Manifesto with Engels"), (1867, "Published Volume 1 of Das Kapital"), (1883, "Died in London")],
  [("Das Kapital", 1867, "Comprehensive analysis of capitalism"), ("The Communist Manifesto", 1848, "Political pamphlet calling for workers' revolution")],
  [("Workers of the world, unite! You have nothing to lose but your chains.", "The Communist Manifesto")])

p("friedrich-nietzsche", "Friedrich Nietzsche", "フリードリヒ・ニーチェ", 1844, 1900, ["de"], ["philosophy"],
  "Friedrich Nietzsche was a German philosopher whose critiques of morality, religion, and contemporary culture have had a profound influence on modern intellectual history.",
  "Nietzsche was born in Röcken, Saxony. He studied at Bonn and Leipzig and became professor of philology at Basel at age 24.",
  "Nietzsche's concepts of the Übermensch, eternal recurrence, and the will to power challenged Western philosophy's foundations and influenced existentialism, postmodernism, and art.",
  [(1872, "Published The Birth of Tragedy"), (1883, "Published Thus Spoke Zarathustra"), (1886, "Published Beyond Good and Evil"), (1889, "Suffered mental collapse")],
  [("Thus Spoke Zarathustra", 1883, "Philosophical novel introducing the Übermensch"), ("Beyond Good and Evil", 1886, "Critique of traditional morality and philosophy")],
  [("He who has a why to live can bear almost any how.", "Twilight of the Idols")])

p("soren-kierkegaard", "Søren Kierkegaard", "セーレン・キェルケゴール", 1813, 1855, ["dk"], ["philosophy"],
  "Søren Kierkegaard was a Danish philosopher, theologian, and poet who is considered the first existentialist philosopher.",
  "Kierkegaard was born in Copenhagen. He studied theology at the University of Copenhagen and spent his short life writing prolifically.",
  "Kierkegaard's emphasis on individual existence, subjective experience, and the leap of faith laid the foundations for existentialism and influenced 20th-century philosophy and theology.",
  [(1843, "Published Either/Or and Fear and Trembling"), (1844, "Published The Concept of Anxiety"), (1849, "Published The Sickness Unto Death")],
  [("Either/Or", 1843, "Philosophical work exploring aesthetic and ethical ways of living"), ("Fear and Trembling", 1843, "Meditation on faith through the story of Abraham")],
  [("Life can only be understood backwards; but it must be lived forwards.", "Journals")])

p("georg-wilhelm-friedrich-hegel", "Georg Wilhelm Friedrich Hegel", "ゲオルク・ヴィルヘルム・フリードリヒ・ヘーゲル", 1770, 1831, ["de"], ["philosophy"],
  "Georg Wilhelm Friedrich Hegel was a German philosopher who developed a comprehensive philosophical framework of absolute idealism.",
  "Hegel was born in Stuttgart. He studied theology in Tübingen with Schelling and Hölderlin before becoming professor at Heidelberg and Berlin.",
  "Hegel's dialectical method and his philosophy of history influenced Marx, existentialism, and virtually all subsequent Western philosophy.",
  [(1807, "Published Phenomenology of Spirit"), (1812, "Published Science of Logic"), (1820, "Published Elements of the Philosophy of Right")],
  [("Phenomenology of Spirit", 1807, "Foundational work of German idealism"), ("Elements of the Philosophy of Right", 1820, "Political philosophy exploring freedom, morality, and the state")],
  [("The owl of Minerva spreads its wings only with the falling of the dusk.", "Elements of the Philosophy of Right")])

p("simone-weil", "Simone Weil", "シモーヌ・ヴェイユ", 1909, 1943, ["fr"], ["philosophy"],
  "Simone Weil was a French philosopher, mystic, and political activist whose posthumously published writings on suffering, attention, and justice have become profoundly influential.",
  "Weil was born in Paris into an intellectual family. She studied at the École Normale Supérieure and worked in factories and on farms to understand the condition of workers.",
  "Weil's writings on affliction, grace, and the roots of social obligation combine philosophical rigor with spiritual depth, making her one of the most original thinkers of the 20th century.",
  [(1934, "Worked in a Renault factory"), (1936, "Served in the Spanish Civil War"), (1942, "Wrote The Need for Roots"), (1943, "Died of tuberculosis and self-starvation at age 34")],
  [("Gravity and Grace", 1947, "Posthumous collection of philosophical aphorisms"), ("The Need for Roots", 1949, "Essay on the obligations of society to the individual")],
  [("Attention is the rarest and purest form of generosity.", "Letter")])

# === MORE ENGINEERS/SCIENTISTS ===
p("werner-heisenberg", "Werner Heisenberg", "ヴェルナー・ハイゼンベルク", 1901, 1976, ["de"], ["physics"],
  "Werner Heisenberg was a German theoretical physicist who is best known for the uncertainty principle and for his contributions to quantum mechanics.",
  "Heisenberg was born in Würzburg, Germany. He studied under Sommerfeld in Munich and Bohr in Copenhagen.",
  "Heisenberg's uncertainty principle and his matrix mechanics formulation of quantum mechanics were revolutionary contributions to 20th-century physics.",
  [(1925, "Developed matrix mechanics"), (1927, "Formulated the uncertainty principle"), (1932, "Awarded Nobel Prize in Physics")],
  [("Physics and Philosophy", 1958, "Philosophical exploration of quantum mechanics")],
  [("What we observe is not nature itself, but nature exposed to our method of questioning.", "Physics and Philosophy")])

p("erwin-schrodinger", "Erwin Schrödinger", "エルヴィン・シュレーディンガー", 1887, 1961, ["at", "ie"], ["physics"],
  "Erwin Schrödinger was an Austrian-Irish physicist who developed the wave equation that describes quantum mechanical behavior.",
  "Schrödinger was born in Vienna. He studied at the University of Vienna and held positions at several European universities before settling in Dublin.",
  "Schrödinger's wave equation provided a complete mathematical description of quantum mechanics. His thought experiment Schrödinger's cat illustrated quantum paradoxes.",
  [(1926, "Published the Schrödinger equation"), (1933, "Awarded Nobel Prize in Physics"), (1935, "Proposed Schrödinger's cat thought experiment"), (1944, "Published What Is Life?")],
  [("What Is Life?", 1944, "Book on the physical basis of living cells that influenced molecular biology")],
  [("If a man never contradicts himself, the reason must be that he virtually never says anything at all.", "Attributed")])

p("max-planck", "Max Planck", "マックス・プランク", 1858, 1947, ["de"], ["physics"],
  "Max Planck was a German theoretical physicist who originated quantum theory, fundamentally changing our understanding of atomic and subatomic processes.",
  "Planck was born in Kiel, Germany. He studied at Munich and Berlin and became professor of theoretical physics at the University of Berlin.",
  "Planck's quantum hypothesis, that energy is emitted in discrete packets, launched the quantum revolution and transformed physics.",
  [(1900, "Introduced the quantum hypothesis"), (1918, "Awarded Nobel Prize in Physics"), (1930, "Became president of the Kaiser Wilhelm Society")],
  [("On the Law of Distribution of Energy in the Normal Spectrum", 1901, "Paper introducing the quantum of action")],
  [("Science cannot solve the ultimate mystery of nature, because we ourselves are part of the mystery.", "Where Is Science Going?")])

p("marie-curie-physics", "Pierre Curie", "ピエール・キュリー", 1859, 1906, ["fr"], ["physics", "chemistry"],
  "Pierre Curie was a French physicist who pioneered crystallography, magnetism, and radioactivity research with his wife Marie.",
  "Curie was born in Paris. He studied at the Sorbonne and conducted groundbreaking research on crystallography and piezoelectricity before turning to radioactivity.",
  "Pierre Curie's work on piezoelectricity and his collaboration with Marie on radioactivity earned them the Nobel Prize and established nuclear physics.",
  [(1880, "Discovered piezoelectricity with his brother"), (1895, "Married Marie Sklodowska"), (1898, "Co-discovered polonium and radium"), (1903, "Shared Nobel Prize in Physics")],
  [("Piezoelectricity", 1880, "Discovery of electric charge generated by mechanical stress in crystals")],
  [("In science, we must be interested in things, not in persons.", "Attributed")])

p("emilie-du-chatelet", "Émilie du Châtelet", "エミリー・デュ・シャトレ", 1706, 1749, ["fr"], ["physics", "mathematics"],
  "Émilie du Châtelet was a French natural philosopher and mathematician who made foundational contributions to physics, including her French translation and commentary on Newton's Principia.",
  "Du Châtelet was born into Parisian aristocracy. She received an excellent education unusual for women and became one of the leading scientific minds of the Enlightenment.",
  "Du Châtelet's translation of Newton's Principia remains the standard French translation. Her work on kinetic energy and her advocacy for women's education were ahead of her time.",
  [(1737, "Published paper on the nature of fire"), (1740, "Published Institutions de Physique"), (1749, "Completed translation of Newton's Principia")],
  [("Institutions de Physique", 1740, "Comprehensive physics textbook synthesizing Newtonian and Leibnizian mechanics")],
  [("If I were king, I would reform an abuse which cuts off, so to speak, half the human race.", "Preface to her translation of Mandeville")])

# === MORE POLITICAL FIGURES ===
p("david-ben-gurion", "David Ben-Gurion", "ダヴィド・ベン＝グリオン", 1886, 1973, ["il", "pl"], ["politics"],
  "David Ben-Gurion was the primary founder of the State of Israel and its first Prime Minister.",
  "Ben-Gurion was born David Grün in Płońsk, Russian Empire. He emigrated to Ottoman Palestine in 1906 and became a leader of the Zionist movement.",
  "Ben-Gurion declared the establishment of the State of Israel in 1948 and led the country through its formative years, shaping its democratic institutions.",
  [(1906, "Emigrated to Palestine"), (1935, "Became head of the Jewish Agency"), (1948, "Declared Israeli independence"), (1953, "Retired to the Negev desert")],
  [("Declaration of Independence of Israel", 1948, "Founding document of the State of Israel")],
  [("In Israel, in order to be a realist you must believe in miracles.", "CBS interview, 1956")])

p("ho-chi-minh", "Ho Chi Minh", "ホー・チ・ミン", 1890, 1969, ["vn"], ["politics"],
  "Ho Chi Minh was a Vietnamese revolutionary and statesman who served as Prime Minister and President of North Vietnam.",
  "Ho Chi Minh was born Nguyễn Sinh Cung in Nghệ An Province. He traveled the world, lived in France, and became a communist revolutionary leader.",
  "Ho Chi Minh led Vietnam's struggle for independence from France and later against American intervention. He is a central figure in Vietnamese national identity.",
  [(1911, "Left Vietnam to travel the world"), (1930, "Founded the Indochinese Communist Party"), (1945, "Declared Vietnamese independence"), (1954, "Defeated France at Dien Bien Phu")],
  [("Declaration of Independence of Vietnam", 1945, "Document drawing on the American Declaration of Independence")],
  [("Nothing is more precious than independence and freedom.", "Attributed")])

p("fidel-castro", "Fidel Castro", "フィデル・カストロ", 1926, 2016, ["cu"], ["politics"],
  "Fidel Castro was a Cuban revolutionary and politician who served as Prime Minister and President of Cuba for nearly fifty years.",
  "Castro was born near Birán, Cuba. He studied law at the University of Havana and led the guerrilla movement that overthrew the Batista dictatorship.",
  "Castro transformed Cuba through socialist revolution, establishing universal healthcare and education while creating an authoritarian state. His impact on Cold War politics was immense.",
  [(1953, "Led the failed Moncada Barracks attack"), (1959, "Cuban Revolution succeeded"), (1961, "Survived Bay of Pigs invasion"), (1962, "Cuban Missile Crisis")],
  [("History Will Absolve Me", 1953, "Defense speech that became a manifesto of the revolution")],
  [("A revolution is not a bed of roses.", "Speech, 1961")])

p("deng-xiaoping", "Deng Xiaoping", "鄧小平", 1904, 1997, ["cn"], ["politics"],
  "Deng Xiaoping was a Chinese politician who led China's economic reforms and opening up, transforming it into a global economic power.",
  "Deng was born in Guang'an, Sichuan. He studied in France and the Soviet Union, joined the Communist Party, and survived multiple political purges.",
  "Deng's reform and opening up policy transformed China from a planned economy to a market economy, lifting hundreds of millions out of poverty.",
  [(1978, "Became paramount leader of China"), (1979, "Established Special Economic Zones"), (1984, "Expanded economic reforms"), (1989, "Tiananmen Square protests and crackdown")],
  [("Reform and Opening Up", 1978, "Economic modernization program that transformed China")],
  [("It doesn't matter whether a cat is black or white, as long as it catches mice.", "Attributed")])

p("lee-kuan-yew", "Lee Kuan Yew", "リー・クアンユー", 1923, 2015, ["sg"], ["politics"],
  "Lee Kuan Yew was the first Prime Minister of Singapore who transformed the city-state from a developing country into one of the wealthiest nations in the world.",
  "Lee was born in Singapore. He studied law at Cambridge and returned to enter politics, leading Singapore to independence and rapid development.",
  "Lee transformed Singapore into a prosperous, efficient city-state through pragmatic governance, earning both admiration and criticism for his authoritarian approach.",
  [(1959, "Became first Prime Minister of Singapore"), (1965, "Singapore became independent"), (1990, "Stepped down as Prime Minister")],
  [("From Third World to First", 2000, "Memoir describing Singapore's transformation")],
  [("We are pragmatists. We don't stick to any ideology.", "Attributed")])

# === A FEW MORE SCIENTISTS ===
p("dorothy-vaughan", "Dorothy Vaughan", "ドロシー・ヴォーン", 1910, 2008, ["us"], ["engineering", "mathematics"],
  "Dorothy Vaughan was an American mathematician and computer programmer who was one of the first African American supervisors at NACA (later NASA).",
  "Vaughan was born in Kansas City, Missouri. She taught mathematics before joining NACA's West Area Computing unit at Langley.",
  "Vaughan led the West Area Computers and became an expert programmer, contributing to NASA's space programs and breaking racial barriers in STEM.",
  [(1943, "Joined NACA at Langley"), (1949, "Became first African American supervisor at NACA"), (1958, "Joined NASA's Analysis and Computation Division")],
  [("FORTRAN Programming", 1958, "Self-taught expertise that she shared with her team at NASA")],
  [("I changed what I could, and what I couldn't, I endured.", "Attributed")])

p("mary-jackson-nasa", "Mary Jackson", "メアリー・ジャクソン", 1921, 2005, ["us"], ["engineering"],
  "Mary Jackson was an American mathematician and aerospace engineer who became NASA's first Black female engineer.",
  "Jackson was born in Hampton, Virginia. She studied mathematics and physical science, then joined NACA as a 'computer' before becoming an engineer.",
  "Jackson broke racial and gender barriers at NASA, becoming its first African American female engineer and later working to promote hiring and advancement of minorities and women.",
  [(1951, "Joined NACA as a research mathematician"), (1958, "Became NASA's first Black female engineer"), (1979, "Became manager of the Federal Women's Program at NASA")],
  [("Aerospace Engineering Career", 1958, "Broke barriers as NASA's first Black female engineer")],
  [("Every time we have a chance to get ahead, they move the finish line.", "Attributed in Hidden Figures")])

p("mae-jemison", "Mae Jemison", "メイ・ジェミソン", 1956, None, ["us"], ["engineering", "biology"],
  "Mae Jemison is an American engineer, physician, and former NASA astronaut who became the first African American woman to travel in space.",
  "Jemison was born in Decatur, Alabama, and grew up in Chicago. She studied chemical engineering and medicine before joining NASA's astronaut program.",
  "Jemison's historic spaceflight on the Space Shuttle Endeavour inspired generations of young people, particularly women and minorities, to pursue careers in STEM.",
  [(1987, "Selected by NASA as an astronaut"), (1992, "Flew aboard Space Shuttle Endeavour"), (1993, "Left NASA to pursue education and science literacy")],
  [("Space Shuttle Endeavour Mission STS-47", 1992, "First African American woman to travel in space")],
  [("Never limit yourself because of others' limited imagination.", "Attributed")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'marie-curie-physics':
            entry['id'] = 'pierre-curie'
        elif entry['id'] == 'mary-jackson-nasa':
            entry['id'] = 'mary-jackson'
    write_people(P)
