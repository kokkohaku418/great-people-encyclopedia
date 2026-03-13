#!/usr/bin/env python3
"""Supplement batch 12: more people with dedup."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
PEOPLE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'people')
existing = {f.replace('.json', '') for f in os.listdir(PEOPLE_DIR) if f.endswith('.json')} if os.path.exists(PEOPLE_DIR) else set()
def add(id, *a, **k):
    if id not in existing:
        P.append(person(id, *a, **k))

# ============================================================
# ANCIENT GREEK / ROMAN THINKERS (~15)
# ============================================================

add("thales-of-miletus", "Thales of Miletus", "タレス", -624, -546, ["gr"], ["philosophy"],
  "Thales of Miletus is regarded as the first Western philosopher and one of the Seven Sages of Greece.", "Born in Miletus, Ionia. Reportedly traveled to Egypt where he studied geometry.", "Thales initiated the tradition of natural philosophy, seeking explanations in nature rather than mythology.",
  [(-585, "Predicted a solar eclipse"), (-600, "Proposed water as the fundamental substance")],
  [("On the Solstice", -580, "Lost work on astronomical observations")],
  [("Know thyself.", "Attributed by Diogenes Laertius")])

add("democritus", "Democritus", "デモクリトス", -460, -370, ["gr"], ["philosophy"],
  "Democritus developed the atomic theory of the universe, proposing that all matter consists of indivisible particles.", "Born in Abdera, Thrace. Traveled widely to study under scholars in Egypt, Persia, and India.", "His atomic theory anticipated modern physics by over two millennia.",
  [(-440, "Developed atomic theory with Leucippus"), (-420, "Wrote extensively on ethics, physics, and mathematics")],
  [("The Great World-System", -420, "Treatise on cosmology and atomic theory")],
  [("Nothing exists except atoms and empty space; everything else is opinion.", "Fragment")])

add("heraclitus", "Heraclitus", "ヘラクレイトス", -535, -475, ["gr"], ["philosophy"],
  "Heraclitus was a pre-Socratic philosopher known for his doctrine of change and the concept of the Logos.", "Born in Ephesus to an aristocratic family. He was largely self-taught and reclusive.", "His emphasis on flux and the unity of opposites profoundly influenced later philosophy.",
  [(-500, "Composed his philosophical work On Nature"), (-490, "Became known as 'The Obscure' for his cryptic style")],
  [("On Nature", -500, "Fragmentary philosophical treatise on change and the Logos")],
  [("No man ever steps in the same river twice.", "Fragment 91")])

add("parmenides", "Parmenides", "パルメニデス", -515, -450, ["gr"], ["philosophy"],
  "Parmenides of Elea founded the Eleatic school and argued that change is an illusion.", "Born in Elea, a Greek colony in southern Italy. Said to have been a student of Xenophanes.", "His arguments about the nature of being deeply influenced Plato and all subsequent metaphysics.",
  [(-485, "Composed the philosophical poem On Nature"), (-450, "Visited Athens and met the young Socrates according to Plato")],
  [("On Nature", -485, "Philosophical poem arguing that reality is unchanging and indivisible")],
  [("What is, is; what is not, is not.", "On Nature, Fragment 2")])

add("diogenes-of-sinope", "Diogenes of Sinope", "ディオゲネス", -412, -323, ["gr"], ["philosophy"],
  "Diogenes of Sinope was the most famous Cynic philosopher, known for living in extreme simplicity.", "Born in Sinope on the Black Sea. Exiled to Athens where he became a student of Antisthenes.", "He embodied the Cynic ideal of virtue through action rather than theory, challenging social conventions.",
  [(-380, "Began living as an ascetic in Athens"), (-336, "Reportedly met Alexander the Great in Corinth")],
  [("Republic", -370, "Lost work proposing a society based on virtue rather than convention")],
  [("I am looking for an honest man.", "Attributed by Diogenes Laertius")])

add("xenophon", "Xenophon", "クセノフォン", -431, -354, ["gr"], ["literature", "philosophy"],
  "Xenophon was an Athenian historian, soldier, and student of Socrates.", "Born in Athens to a wealthy family. Joined the expedition of Cyrus the Younger to Persia.", "His historical and philosophical writings provided key accounts of Socrates and Greek military life.",
  [(-401, "Led the retreat of the Ten Thousand from Persia"), (-370, "Wrote Memorabilia on Socrates")],
  [("Anabasis", -370, "Account of the Greek mercenary expedition into Persia and the famous retreat"), ("Memorabilia", -371, "Recollections of Socrates")],
  [("Excess of grief for the dead is madness; for it is an injury to the living.", "Attributed")])

add("thucydides", "Thucydides", "トゥキュディデス", -460, -400, ["gr"], ["literature"],
  "Thucydides wrote the History of the Peloponnesian War, considered a masterpiece of historical writing.", "Born in Athens to a wealthy family. Served as an Athenian general before being exiled.", "He is considered the father of scientific history for his rigorous evidence-based approach.",
  [(-424, "Exiled from Athens after the fall of Amphipolis"), (-411, "History breaks off, likely due to his death")],
  [("History of the Peloponnesian War", -411, "Detailed account of the war between Athens and Sparta")],
  [("The strong do what they can and the weak suffer what they must.", "Melian Dialogue")])

add("herodotus", "Herodotus", "ヘロドトス", -484, -425, ["gr"], ["literature"],
  "Herodotus is called the Father of History for his Histories, the first great narrative history in Western literature.", "Born in Halicarnassus, Caria. Traveled extensively through the Mediterranean and Near East.", "He established the genre of historical writing and preserved invaluable ethnographic information.",
  [(-450, "Traveled through Egypt, Babylon, and Scythia"), (-440, "Composed the Histories")],
  [("The Histories", -440, "Nine-book account of the Greco-Persian Wars and the peoples of the known world")],
  [("Of all men's miseries the bitterest is this: to know so much and to have control over nothing.", "Histories, Book 9")])

add("sappho", "Sappho", "サッポー", -630, -570, ["gr"], ["literature"],
  "Sappho was a lyric poet from Lesbos, one of the greatest poets of the ancient world.", "Born on the island of Lesbos. Led a circle of young women devoted to poetry and the arts.", "Her intimate lyric poetry influenced the entire Western literary tradition and gave the word 'sapphic' to the language.",
  [(-600, "Composed lyric poetry on Lesbos"), (-590, "Briefly exiled to Sicily")],
  [("Ode to Aphrodite", -600, "The only complete surviving poem by Sappho"), ("Fragment 31", -600, "Famous poem describing the physical effects of love")],
  [("What is beautiful is good, and who is good will soon be beautiful.", "Fragment 101")])

add("aeschylus", "Aeschylus", "アイスキュロス", -525, -456, ["gr"], ["literature"],
  "Aeschylus is the father of tragedy who expanded the art form by introducing a second actor and reducing the chorus.", "Born in Eleusis near Athens. Fought at the Battle of Marathon.", "He established the conventions of Greek tragedy and explored profound themes of justice and divine will.",
  [(-490, "Fought at the Battle of Marathon"), (-458, "Premiered the Oresteia trilogy")],
  [("The Oresteia", -458, "Trilogy of tragedies on justice and the founding of Athenian law"), ("Prometheus Bound", -460, "Tragedy about Prometheus's punishment by Zeus")],
  [("He who learns must suffer.", "Agamemnon")])

add("sophocles", "Sophocles", "ソフォクレス", -496, -406, ["gr"], ["literature"],
  "Sophocles was a master tragedian who introduced the third actor and wrote over 120 plays.", "Born in Colonus near Athens to a wealthy family. Won his first dramatic competition at age 28.", "His tragedies, especially Oedipus Rex, are considered the pinnacle of Greek dramatic art.",
  [(-468, "Won first prize at the Dionysia"), (-441, "Elected one of the ten strategoi of Athens")],
  [("Oedipus Rex", -429, "Tragedy of Oedipus discovering he killed his father and married his mother"), ("Antigone", -441, "Tragedy of moral duty versus state law")],
  [("What people believe prevails over the truth.", "Fragment")])

add("euripides", "Euripides", "エウリピデス", -480, -406, ["gr"], ["literature"],
  "Euripides was a tragedian known for his realistic characters and questioning of social conventions.", "Born on Salamis. Less popular in his lifetime than Aeschylus or Sophocles, but hugely influential later.", "He humanized Greek tragedy by giving voice to women, slaves, and the marginalized.",
  [(-455, "First competed at the Dionysia"), (-408, "Left Athens for Macedonia")],
  [("Medea", -431, "Tragedy about Medea's revenge on her unfaithful husband"), ("The Bacchae", -405, "Tragedy about the god Dionysus and the dangers of denying the irrational")],
  [("Whom the gods would destroy, they first make mad.", "Fragment")])

add("aristophanes", "Aristophanes", "アリストファネス", -446, -386, ["gr"], ["literature"],
  "Aristophanes was the greatest comic playwright of ancient Athens, known for biting political satire.", "Born in Athens. Little is known of his early life.", "His comedies are the only surviving examples of Old Comedy and offer vivid portraits of Athenian society.",
  [(-425, "Won first prize with The Acharnians"), (-405, "Produced The Frogs")],
  [("The Clouds", -423, "Comedy satirizing Socrates and the Sophists"), ("Lysistrata", -411, "Comedy in which women withhold sex to end the Peloponnesian War")],
  [("Open your mind before your mouth.", "Attributed")])

add("lucretius", "Lucretius", "ルクレティウス", -99, -55, ["it"], ["philosophy"],
  "Lucretius was a Roman poet and philosopher who expounded Epicurean philosophy in verse.", "Born in Rome. Almost nothing is known of his personal life.", "De Rerum Natura preserved Epicurean atomism and profoundly influenced the Scientific Revolution.",
  [(-60, "Composed De Rerum Natura"), (-55, "Died, reportedly before completing the final revision")],
  [("De Rerum Natura", -55, "Six-book poem explaining Epicurean physics, atomism, and the mortality of the soul")],
  [("Nothing can be created out of nothing.", "De Rerum Natura, Book I")])

add("cicero", "Cicero", "キケロ", -106, -43, ["it"], ["philosophy", "politics"],
  "Marcus Tullius Cicero was Rome's greatest orator and a leading philosopher and statesman.", "Born in Arpinum to an equestrian family. Studied law, rhetoric, and philosophy in Rome and Greece.", "His writings preserved Greek philosophy for the Latin world and shaped Western rhetoric and political thought.",
  [(-63, "Suppressed the Catiline conspiracy as consul"), (-43, "Executed on orders of Mark Antony during the proscriptions")],
  [("De Republica", -51, "Dialogue on the ideal state and natural law"), ("De Officiis", -44, "Treatise on moral duties")],
  [("A room without books is like a body without a soul.", "Attributed")])

# ============================================================
# SOUTH / SOUTHEAST ASIAN FIGURES (~15)
# ============================================================

add("chandragupta-maurya", "Chandragupta Maurya", "チャンドラグプタ・マウリヤ", -340, -298, ["in"], ["politics"],
  "Chandragupta Maurya founded the Maurya Empire, the first empire to unify most of the Indian subcontinent.", "Born into modest circumstances. Mentored by the strategist Chanakya.", "He created the largest empire in Indian history at that time and established a centralized administration.",
  [(-322, "Overthrew the Nanda dynasty and founded the Maurya Empire"), (-305, "Defeated Seleucus Nicator and gained territory in the northwest")],
  [("Arthashastra", -300, "Political treatise attributed to his advisor Chanakya describing statecraft under the Mauryas")],
  [("A person should not be too honest. Straight trees are cut first.", "Attributed via Chanakya")])

add("samudragupta", "Samudragupta", "サムドラグプタ", 315, 380, ["in"], ["politics"],
  "Samudragupta expanded the Gupta Empire through military conquest and is called the Napoleon of India.", "Son of Chandragupta I. Selected as heir for his exceptional abilities.", "His conquests ushered in the Golden Age of India under the Gupta dynasty.",
  [(335, "Ascended to the Gupta throne"), (350, "Conducted extensive military campaigns across India as recorded in the Allahabad Pillar inscription")],
  [("Allahabad Pillar Inscription", 350, "Prasasti composed by Harishena detailing Samudragupta's conquests")],
  [("He who has prowess wins the world.", "Allahabad Inscription paraphrase")])

add("harsha", "Harsha", "ハルシャ", 590, 647, ["in"], ["politics", "literature"],
  "Emperor Harsha of Kannauj was one of the last great rulers of ancient India, known for his patronage of arts and Buddhism.", "Born into the Pushyabhuti dynasty. Became king at age 16 after the deaths of his father and brother.", "He unified much of northern India and promoted religious tolerance and learning.",
  [(606, "Ascended to the throne of Kannauj"), (641, "Received the Chinese pilgrim Xuanzang at his court")],
  [("Nagananda", 620, "Sanskrit drama about the Bodhisattva Jimutavahana"), ("Ratnavali", 620, "Sanskrit romantic comedy")],
  [("Dharma is the foundation of the state.", "Attributed")])

add("aryabhata", "Aryabhata", "アーリヤバタ", 476, 550, ["in"], ["mathematics", "astronomy"],
  "Aryabhata was an Indian mathematician and astronomer who made groundbreaking contributions to both fields.", "Born in Kusumapura (modern Patna). Studied at the ancient university of Nalanda.", "He introduced the concept of zero as a placeholder, calculated pi to remarkable accuracy, and proposed that the Earth rotates on its axis.",
  [(499, "Composed the Aryabhatiya at age 23"), (510, "Led the astronomical observatory at Nalanda")],
  [("Aryabhatiya", 499, "Treatise on mathematics and astronomy covering arithmetic, algebra, and spherical astronomy")],
  [("Add four to one hundred, multiply by eight, and add sixty-two thousand; the result is approximately the circumference of a circle of diameter twenty thousand.", "Aryabhatiya")])

add("ramanuja", "Ramanuja", "ラーマーヌジャ", 1017, 1137, ["in"], ["philosophy"],
  "Ramanuja was a Hindu theologian and philosopher who developed Vishishtadvaita (qualified non-dualism).", "Born in Sriperumbudur, Tamil Nadu. Studied under Yadava Prakasha before breaking with him.", "His philosophy provided the theological foundation for the Sri Vaishnava tradition and devotional Hinduism.",
  [(1077, "Became head of the Srirangam temple"), (1100, "Composed Sri Bhashya, his commentary on the Brahma Sutras")],
  [("Sri Bhashya", 1100, "Commentary on the Brahma Sutras establishing Vishishtadvaita Vedanta")],
  [("The soul is distinct from God yet inseparable, as the body is from the soul.", "Sri Bhashya paraphrase")])

add("adi-shankara", "Adi Shankara", "シャンカラ", 788, 820, ["in"], ["philosophy"],
  "Adi Shankara was an Indian philosopher who consolidated the doctrine of Advaita Vedanta (non-dualism).", "Born in Kaladi, Kerala. Became a sannyasi at a very young age and traveled across India.", "He revitalized Hindu philosophy, established four mathas (monasteries), and is one of India's greatest thinkers.",
  [(800, "Composed commentaries on the Upanishads, Brahma Sutras, and Bhagavad Gita"), (810, "Established the four mathas at Sringeri, Puri, Dwaraka, and Jyotirmath")],
  [("Vivekachudamani", 800, "Philosophical poem on the discrimination between the real and the unreal")],
  [("Brahman is the only truth, the world is illusion, and there is ultimately no difference between Brahman and the individual self.", "Attributed")])

add("guru-nanak", "Guru Nanak", "グル・ナーナク", 1469, 1539, ["in"], ["philosophy"],
  "Guru Nanak was the founder of Sikhism and the first of the ten Sikh Gurus.", "Born in Talwandi (now Nankana Sahib, Pakistan). Showed spiritual inclinations from childhood.", "He founded one of the world's major religions, emphasizing equality, devotion, and honest living.",
  [(1499, "Had a spiritual revelation and began teaching"), (1520, "Established the town of Kartarpur as a center for the Sikh community")],
  [("Japji Sahib", 1500, "Opening prayer of the Guru Granth Sahib, the central scripture of Sikhism")],
  [("There is no Hindu, there is no Muslim.", "Attributed upon emerging from the river")])

add("kabir", "Kabir", "カビール", 1398, 1518, ["in"], ["literature", "philosophy"],
  "Kabir was a mystic poet-saint whose verses transcended Hindu and Muslim boundaries.", "Born in Varanasi, likely into a Muslim weaver family. Influenced by both Hindu and Sufi traditions.", "His poetry profoundly influenced the Bhakti movement and remains central to Indian spiritual literature.",
  [(1440, "Began composing devotional poetry and songs"), (1495, "His teachings attracted both Hindu and Muslim followers")],
  [("Bijak", 1500, "Collection of Kabir's poems and songs compiled by followers")],
  [("Do not go to the garden of flowers! O friend! Go not there; in your body is the garden of flowers.", "Bijak")])

add("mirabai", "Mirabai", "ミーラーバーイー", 1498, 1546, ["in"], ["literature"],
  "Mirabai was a Rajput princess and mystic poet devoted to Lord Krishna, one of the most beloved Bhakti saints.", "Born into a royal Rajput family in Merta, Rajasthan. Married the crown prince of Mewar.", "Her devotional songs are sung across India to this day and embody the intensity of Bhakti love poetry.",
  [(1516, "Married Bhoj Raj, crown prince of Mewar"), (1535, "Left the royal court to become a wandering devotee")],
  [("Mira Ke Pad", 1540, "Collection of devotional songs to Krishna")],
  [("I have felt the swaying of the elephant's shoulders; and now you want me to climb on a jackass? Try to be serious.", "Devotional poem")])

add("tulsidas", "Tulsidas", "トゥルシーダース", 1532, 1623, ["in"], ["literature"],
  "Tulsidas was a Hindu poet-saint best known for the Ramcharitmanas, a retelling of the Ramayana in Awadhi.", "Born in Rajapur, Uttar Pradesh. Orphaned young and raised by a sadhu.", "The Ramcharitmanas became the most popular version of the Rama story in northern India and shaped Hindi literary culture.",
  [(1574, "Began composing the Ramcharitmanas in Ayodhya"), (1623, "Died in Varanasi")],
  [("Ramcharitmanas", 1574, "Epic retelling of the Ramayana in Awadhi Hindi")],
  [("The root of religion is compassion.", "Ramcharitmanas")])

add("suryavarman-ii", "Suryavarman II", "スーリヤヴァルマン2世", 1094, 1150, ["kh"], ["politics"],
  "Suryavarman II was the Khmer king who built Angkor Wat, the largest religious monument in the world.", "Rose to power by unifying the fractured Khmer kingdom through political and military prowess.", "He created one of humanity's greatest architectural achievements and expanded the Khmer Empire to its greatest extent.",
  [(1113, "Ascended to the Khmer throne"), (1122, "Commenced construction of Angkor Wat")],
  [("Angkor Wat", 1150, "Massive temple complex dedicated to Vishnu, later converted to a Buddhist temple")],
  [("Let this temple stand as testament to the glory of the gods and the kingdom.", "Traditional attribution")])

add("rama-v-thailand", "King Chulalongkorn (Rama V)", "ラーマ5世（チュラーロンコーン）", 1853, 1910, ["th"], ["politics"],
  "King Chulalongkorn modernized Siam and preserved its independence during the era of European colonialism.", "Born in Bangkok as the eldest son of King Mongkut. Educated by both Thai and Western tutors.", "He abolished slavery, reformed the government, and kept Thailand as the only Southeast Asian country never colonized.",
  [(1868, "Ascended to the throne"), (1905, "Abolished slavery throughout Siam")],
  [("Royal Decree on Slavery Abolition", 1905, "Decree completing the gradual abolition of slavery in Siam")],
  [("The progress of a nation depends on its people's education.", "Attributed")])

add("emilio-aguinaldo", "Emilio Aguinaldo", "エミリオ・アギナルド", 1869, 1964, ["ph"], ["politics"],
  "Emilio Aguinaldo was the first president of the Philippines and a leader of the Philippine Revolution.", "Born in Cavite to a wealthy family. Became a municipal leader before joining the revolution.", "He led the struggle for Philippine independence from both Spain and the United States.",
  [(1898, "Declared Philippine independence from Spain on June 12"), (1901, "Captured by American forces, ending the Philippine-American War resistance")],
  [("Philippine Declaration of Independence", 1898, "Document declaring independence from Spain, read at Kawit, Cavite")],
  [("I have always preferred the freedom of my country above all else.", "Attributed")])

add("aung-san", "Aung San", "アウンサン", 1915, 1947, ["mm"], ["politics"],
  "Aung San was the founder of modern Burma (Myanmar) and the chief architect of Burmese independence.", "Born in Natmauk, central Burma. Studied at Rangoon University where he became a student leader.", "He negotiated Burma's independence from Britain and is revered as the father of the nation.",
  [(1942, "Led the Burma Independence Army alongside the Japanese"), (1947, "Negotiated independence from Britain but was assassinated on July 19")],
  [("Panglong Agreement", 1947, "Agreement uniting Burma's ethnic groups toward independence")],
  [("It is not the mere existence of a parliament that makes a country democratic.", "Speech, 1946")])

add("sukarno", "Sukarno", "スカルノ", 1901, 1970, ["id"], ["politics"],
  "Sukarno was the first president of Indonesia and a leader of the Indonesian independence movement.", "Born in Surabaya, Java. Studied engineering and became involved in the nationalist movement.", "He proclaimed Indonesian independence and led the country through its formative years as a nation.",
  [(1945, "Proclaimed Indonesian independence on August 17"), (1955, "Hosted the Bandung Conference of Asian and African nations")],
  [("Pancasila Speech", 1945, "Speech outlining the five principles as the philosophical foundation of Indonesia")],
  [("Give me a thousand old men and I will pull out Mount Semeru by its roots. Give me ten youths and I will shake the world.", "Attributed")])

# ============================================================
# 20TH CENTURY SCIENTISTS (~15)
# ============================================================

add("max-von-laue", "Max von Laue", "マックス・フォン・ラウエ", 1879, 1960, ["de"], ["physics"],
  "Max von Laue discovered the diffraction of X-rays by crystals, proving their wave nature.", "Born in Pfaffendorf, Germany. Studied under Max Planck in Berlin.", "His discovery founded the field of X-ray crystallography, enabling determination of crystal and molecular structures.",
  [(1912, "Discovered X-ray diffraction by crystals"), (1914, "Awarded Nobel Prize in Physics")],
  [("Concerning the Detection of X-ray Interferences", 1912, "Paper demonstrating X-ray diffraction by crystals")],
  [("Science knows no country, because knowledge belongs to humanity.", "Attributed")])

add("james-franck", "James Franck", "ジェームズ・フランク", 1882, 1964, ["de", "us"], ["physics"],
  "James Franck, with Gustav Hertz, confirmed quantum theory through the Franck-Hertz experiment.", "Born in Hamburg, Germany. Studied at the University of Heidelberg and Berlin.", "The Franck-Hertz experiment provided direct evidence for quantized energy levels in atoms.",
  [(1914, "Conducted the Franck-Hertz experiment"), (1925, "Awarded Nobel Prize in Physics")],
  [("On Collisions between Electrons and Mercury Atoms", 1914, "Paper describing the Franck-Hertz experiment")],
  [("Science is not just a collection of facts but a way of thinking.", "Attributed")])

add("gustav-hertz-physicist", "Gustav Hertz", "グスタフ・ヘルツ", 1887, 1975, ["de"], ["physics"],
  "Gustav Hertz shared the Nobel Prize for the Franck-Hertz experiment demonstrating quantized atomic energy levels.", "Born in Hamburg to a prominent family (nephew of Heinrich Hertz). Studied in Gottingen, Munich, and Berlin.", "His experimental confirmation of quantum energy levels was pivotal for the development of quantum mechanics.",
  [(1914, "Conducted the Franck-Hertz experiment with James Franck"), (1925, "Shared Nobel Prize in Physics with Franck")],
  [("On Collisions between Electrons and Mercury Atoms", 1914, "Co-authored paper on quantized energy transfer in atoms")],
  [("Experiment is the sole judge of the validity of any idea.", "Attributed")])

add("otto-stern", "Otto Stern", "オットー・シュテルン", 1888, 1969, ["de", "us"], ["physics"],
  "Otto Stern developed the molecular beam method and discovered the quantization of angular momentum.", "Born in Sohrau, Upper Silesia. Studied physical chemistry in Breslau.", "His molecular beam experiments provided direct evidence for space quantization and measured the proton magnetic moment.",
  [(1922, "Conducted the Stern-Gerlach experiment with Walther Gerlach"), (1943, "Awarded Nobel Prize in Physics")],
  [("A Method for Experimentally Testing the Directional Quantization in a Magnetic Field", 1921, "Paper proposing the Stern-Gerlach experiment")],
  [("Thinking is cheap, but experiment is expensive.", "Attributed")])

add("polykarp-kusch", "Polykarp Kusch", "ポリカプ・クッシュ", 1911, 1993, ["de", "us"], ["physics"],
  "Polykarp Kusch precisely measured the magnetic moment of the electron, confirming quantum electrodynamics.", "Born in Blankenburg, Germany. Emigrated to the US as a child and studied at Case Institute and University of Illinois.", "His precision measurement of the electron's anomalous magnetic moment validated QED theory.",
  [(1947, "Measured the anomalous magnetic moment of the electron"), (1955, "Awarded Nobel Prize in Physics")],
  [("The Magnetic Moment of the Electron", 1948, "Paper presenting precision measurement of the electron magnetic moment")],
  [("Precision is not merely a virtue of measurement but a gateway to understanding.", "Attributed")])

add("charles-townes", "Charles Townes", "チャールズ・タウンズ", 1915, 2015, ["us"], ["physics"],
  "Charles Townes invented the maser and contributed fundamental work leading to the laser.", "Born in Greenville, South Carolina. Studied at Furman University and Caltech.", "His invention of the maser and theoretical work on the laser transformed communications, medicine, and science.",
  [(1953, "Built the first maser"), (1964, "Awarded Nobel Prize in Physics")],
  [("Infrared and Optical Masers", 1958, "Paper with Arthur Schawlow proposing the optical maser (laser)")],
  [("It's like the beaver told the rabbit as they stared at the Hoover Dam: No, I didn't build it myself. But it's based on an idea of mine.", "Attributed")])

add("nikolay-basov", "Nikolay Basov", "ニコライ・バソフ", 1922, 2001, ["ru"], ["physics"],
  "Nikolay Basov independently developed the maser-laser principle and shared the Nobel Prize for quantum electronics.", "Born in Usman, Russia. Served in World War II before studying at the Moscow Engineering Physics Institute.", "His work on quantum electronics was essential to the development of lasers.",
  [(1954, "Proposed the three-level laser concept with Prokhorov"), (1964, "Shared Nobel Prize in Physics with Townes and Prokhorov")],
  [("Application of Molecular Beams for Radiospectroscopy", 1954, "Paper on the principles of quantum amplification")],
  [("Science is the most reliable method of knowing the world.", "Attributed")])

add("alexander-prokhorov", "Alexander Prokhorov", "アレクサンドル・プロホロフ", 1916, 2002, ["ru"], ["physics"],
  "Alexander Prokhorov co-developed the theoretical basis for the maser and laser.", "Born in Atherton, Australia to Russian emigrant parents. Returned to the USSR and studied at Leningrad State University.", "His fundamental contributions to quantum electronics enabled the laser revolution.",
  [(1954, "Proposed the maser principle with Basov"), (1964, "Shared Nobel Prize in Physics")],
  [("Molecular Oscillator and Its Possible Applications", 1954, "Paper co-authored with Basov on quantum amplification")],
  [("The laser is a solution looking for problems, and it keeps finding them.", "Attributed")])

add("hans-dehmelt", "Hans Dehmelt", "ハンス・デーメルト", 1922, 2017, ["de", "us"], ["physics"],
  "Hans Dehmelt developed the ion trap technique, enabling precision measurements of individual particles.", "Born in Gorlitz, Germany. Served in World War II before studying at Gottingen.", "His ion trap technique allowed the first isolation and observation of a single electron, revolutionizing precision measurement.",
  [(1959, "Developed the Penning trap for isolating ions"), (1989, "Awarded Nobel Prize in Physics")],
  [("Experiments with an Isolated Subatomic Particle at Rest", 1989, "Nobel lecture on ion trap techniques")],
  [("A single electron in a trap is the simplest thing I can think of. One electron, one trap, one physicist.", "Attributed")])

add("wolfgang-ketterle", "Wolfgang Ketterle", "ヴォルフガング・ケターレ", 1957, None, ["de", "us"], ["physics"],
  "Wolfgang Ketterle achieved Bose-Einstein condensation in dilute gases of alkali atoms.", "Born in Heidelberg, Germany. Studied at the Technical University of Munich and the Max Planck Institute.", "His creation of Bose-Einstein condensates opened a new field of ultracold atomic physics.",
  [(1995, "Achieved Bose-Einstein condensation of sodium atoms at MIT"), (2001, "Awarded Nobel Prize in Physics")],
  [("Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor", 1995, "Paper reporting BEC in sodium")],
  [("At absolute zero, atoms march in lockstep like soldiers on parade.", "Public lecture")])

add("eric-cornell", "Eric Cornell", "エリック・コーネル", 1961, None, ["us"], ["physics"],
  "Eric Cornell, with Carl Wieman, first achieved Bose-Einstein condensation in a dilute gas.", "Born in Palo Alto, California. Studied at Stanford and MIT.", "His experimental realization of Bose-Einstein condensation confirmed a prediction made 70 years earlier.",
  [(1995, "Achieved Bose-Einstein condensation in rubidium with Carl Wieman"), (2001, "Awarded Nobel Prize in Physics")],
  [("Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor", 1995, "Landmark paper on BEC in rubidium gas")],
  [("We were trying to make the coldest stuff in the universe. That turned out to be pretty cool.", "Interview")])

add("carl-wieman", "Carl Wieman", "カール・ワイマン", 1951, None, ["us"], ["physics"],
  "Carl Wieman co-produced the first true Bose-Einstein condensate and later became a leader in physics education.", "Born in Corvallis, Oregon. Studied at MIT and Stanford.", "Beyond his Nobel-winning BEC work, he transformed physics education through evidence-based teaching methods.",
  [(1995, "Produced Bose-Einstein condensate with Eric Cornell"), (2001, "Awarded Nobel Prize in Physics")],
  [("Observation of Bose-Einstein Condensation in a Dilute Atomic Vapor", 1995, "Paper on BEC in rubidium")],
  [("The way we teach physics is fundamentally broken, and we can fix it with the same rigor we use in research.", "Public lecture")])

add("serge-haroche", "Serge Haroche", "セルジュ・アロシュ", 1944, None, ["fr"], ["physics"],
  "Serge Haroche developed methods to measure and manipulate individual quantum systems.", "Born in Casablanca, Morocco. Studied at the Ecole Normale Superieure in Paris.", "His techniques for trapping photons enabled direct observation of quantum decoherence.",
  [(2006, "Demonstrated quantum non-demolition measurement of photons"), (2012, "Awarded Nobel Prize in Physics")],
  [("Exploring the Quantum", 2006, "Book on quantum physics experiments with individual atoms and photons")],
  [("We can now play with Schrodinger's cat and watch it lose its quantum properties in real time.", "Nobel lecture")])

add("david-wineland", "David Wineland", "デイヴィッド・ワインランド", 1944, None, ["us"], ["physics"],
  "David Wineland pioneered techniques for trapping and manipulating individual ions with laser light.", "Born in Milwaukee, Wisconsin. Studied at the University of California, Berkeley.", "His ion trap methods enabled the most precise clocks ever made and laid groundwork for quantum computing.",
  [(1978, "First laser cooling of ions"), (2012, "Awarded Nobel Prize in Physics")],
  [("Laser Cooling of Atoms", 1979, "Seminal paper on laser cooling and trapping of ions")],
  [("We can now make clocks so precise that they would not gain or lose a second in the age of the universe.", "Public lecture")])

# ============================================================
# PHILOSOPHERS NOT YET INCLUDED (~10)
# ============================================================

add("plotinus", "Plotinus", "プロティノス", 204, 270, ["eg", "it"], ["philosophy"],
  "Plotinus was the founder of Neoplatonism, one of the most influential philosophical systems in Western and Islamic thought.", "Born in Lycopolis, Egypt. Studied in Alexandria under Ammonius Saccas for eleven years.", "His philosophy of the One, emanation, and the soul's return deeply influenced Christian, Islamic, and Jewish theology.",
  [(244, "Settled in Rome and began teaching philosophy"), (270, "His student Porphyry later compiled his writings as the Enneads")],
  [("Enneads", 270, "Collection of 54 treatises on metaphysics, ethics, and aesthetics compiled by Porphyry")],
  [("Withdraw into yourself and look.", "Enneads I.6")])

add("boethius", "Boethius", "ボエティウス", 480, 524, ["it"], ["philosophy"],
  "Boethius wrote The Consolation of Philosophy, one of the most widely read books of the Middle Ages.", "Born in Rome to an aristocratic family. Served as consul and magister officiorum under the Ostrogothic king Theodoric.", "He transmitted Greek philosophy to the medieval Latin West and wrote the most influential philosophical work of the early Middle Ages.",
  [(510, "Served as consul of Rome"), (524, "Executed by Theodoric; wrote Consolation of Philosophy while imprisoned")],
  [("The Consolation of Philosophy", 524, "Dialogue between the author and Lady Philosophy on fortune, happiness, and divine providence")],
  [("In other living creatures the ignorance of themselves is nature, but in men it is a vice.", "The Consolation of Philosophy")])

add("peter-abelard", "Peter Abelard", "ピエール・アベラール", 1079, 1142, ["fr"], ["philosophy"],
  "Peter Abelard was a medieval French philosopher and theologian known for his method of dialectical reasoning.", "Born in Le Pallet, Brittany. Studied under leading masters in Paris and became a renowned teacher.", "His Sic et Non method of juxtaposing contradictory authorities transformed medieval scholastic inquiry.",
  [(1115, "Began his famous love affair with Heloise"), (1121, "Condemned at the Council of Soissons for his theological writings")],
  [("Sic et Non", 1120, "Collection of contradictory statements from Church authorities, intended to provoke critical inquiry")],
  [("By doubting we come to inquiry, and by inquiry we arrive at truth.", "Sic et Non, Prologue")])

add("william-of-ockham", "William of Ockham", "オッカムのウィリアム", 1287, 1347, ["gb"], ["philosophy"],
  "William of Ockham was a Franciscan friar and philosopher best known for Ockham's Razor.", "Born in Ockham, Surrey. Studied at the University of Oxford.", "Ockham's Razor - the principle of parsimony - became a fundamental principle of scientific reasoning.",
  [(1320, "Composed the Summa Logicae"), (1328, "Fled to the court of Emperor Louis IV after disputes with Pope John XXII")],
  [("Summa Logicae", 1323, "Comprehensive treatise on logic and philosophy of language")],
  [("Entities should not be multiplied beyond necessity.", "Attributed, paraphrase of his principle")])

add("duns-scotus", "Duns Scotus", "ドゥンス・スコトゥス", 1266, 1308, ["gb"], ["philosophy"],
  "Duns Scotus was a Franciscan philosopher-theologian known for his subtle and rigorous arguments.", "Born in Duns, Scotland. Studied and taught at Oxford, Paris, and Cologne.", "His concept of haecceity (individual essence) and univocity of being were major contributions to metaphysics.",
  [(1300, "Lectured on the Sentences of Peter Lombard at Oxford and Paris"), (1308, "Died in Cologne; beatified in 1993")],
  [("Ordinatio", 1300, "Major theological and philosophical commentary on the Sentences of Peter Lombard")],
  [("The will is the supreme faculty.", "Ordinatio paraphrase")])

add("nicholas-of-cusa", "Nicholas of Cusa", "ニコラウス・クザーヌス", 1401, 1464, ["de"], ["philosophy"],
  "Nicholas of Cusa was a philosopher, theologian, and cardinal who anticipated many modern ideas.", "Born in Kues on the Moselle River. Studied at Heidelberg, Padua, and Cologne.", "His concept of learned ignorance and the coincidence of opposites influenced later philosophy and theology.",
  [(1440, "Published De Docta Ignorantia"), (1448, "Created a cardinal by Pope Nicholas V")],
  [("De Docta Ignorantia", 1440, "Philosophical treatise on the limits of human knowledge and the infinity of God")],
  [("The more we learn of our own ignorance, the closer we come to truth.", "De Docta Ignorantia paraphrase")])

add("giambattista-vico", "Giambattista Vico", "ジャンバッティスタ・ヴィーコ", 1668, 1744, ["it"], ["philosophy"],
  "Giambattista Vico was an Italian philosopher who pioneered the philosophy of history.", "Born in Naples. Spent most of his life as a professor of rhetoric at the University of Naples.", "His cyclical theory of history and emphasis on culture and language anticipated modern social science.",
  [(1725, "Published the first edition of Scienza Nuova"), (1730, "Published the revised second edition of Scienza Nuova")],
  [("Scienza Nuova", 1725, "Groundbreaking work on the philosophy of history and the development of civilizations")],
  [("Men first feel necessity, then look for utility, next attend to comfort, still later amuse themselves with pleasure.", "Scienza Nuova")])

add("johann-gottlieb-fichte", "Johann Gottlieb Fichte", "ヨハン・ゴットリープ・フィヒテ", 1762, 1814, ["de"], ["philosophy"],
  "Johann Gottlieb Fichte was a German philosopher who developed the foundation of German idealism.", "Born in Rammenau, Saxony to a poor family. His talent was recognized by a patron who funded his education.", "His philosophy of the self-positing ego influenced Hegel, Schelling, and the development of German nationalism.",
  [(1794, "Published the Wissenschaftslehre (Science of Knowledge)"), (1807, "Delivered the Addresses to the German Nation during Napoleonic occupation")],
  [("Wissenschaftslehre", 1794, "Foundational work attempting to derive all knowledge from a single principle: the self-positing I")],
  [("What sort of philosophy one chooses depends on what sort of man one is.", "First Introduction to the Wissenschaftslehre")])

add("friedrich-schelling", "Friedrich Schelling", "フリードリヒ・シェリング", 1775, 1854, ["de"], ["philosophy"],
  "Friedrich Schelling was a central figure in German idealism who developed a philosophy of nature and art.", "Born in Leonberg, Wurttemberg. A prodigy who entered the Tubinger Stift seminary at age 15 alongside Hegel and Holderlin.", "His Naturphilosophie influenced Romantic science, and his philosophy of identity anticipated later developments in metaphysics.",
  [(1797, "Published Ideas for a Philosophy of Nature"), (1800, "Published System of Transcendental Idealism")],
  [("System of Transcendental Idealism", 1800, "Attempt to unite nature and spirit through a philosophy of art")],
  [("Architecture is frozen music.", "Attributed via Schelling's Philosophie der Kunst")])

add("benedetto-croce", "Benedetto Croce", "ベネデット・クローチェ", 1866, 1952, ["it"], ["philosophy"],
  "Benedetto Croce was an Italian idealist philosopher, historian, and prominent anti-fascist intellectual.", "Born in Pescasseroli, Abruzzo. Orphaned by an earthquake at age 17 and raised by a cousin in Rome.", "His aesthetic philosophy and historicism dominated Italian intellectual life for half a century.",
  [(1902, "Published Aesthetics as Science of Expression and General Linguistic"), (1925, "Published the Manifesto of the Anti-Fascist Intellectuals")],
  [("Aesthetics as Science of Expression and General Linguistic", 1902, "Major work arguing that art is intuitive expression of individual emotion")],
  [("All history is contemporary history.", "Theory and History of Historiography")])

# ============================================================
# MODERN POLITICAL LEADERS (~15)
# ============================================================

add("vallabhbhai-patel", "Vallabhbhai Patel", "ヴァッラブバーイー・パテール", 1875, 1950, ["in"], ["politics"],
  "Sardar Vallabhbhai Patel unified India by integrating over 500 princely states into the Indian Union.", "Born in Nadiad, Gujarat. Studied law in England and became a successful barrister.", "He is called the Iron Man of India for his decisive role in creating a united Indian state.",
  [(1928, "Led the Bardoli Satyagraha"), (1947, "As Deputy Prime Minister, integrated princely states into India")],
  [("Integration of Indian States", 1947, "His political campaign to unite over 500 princely states into the Indian republic")],
  [("Every Indian should now forget that he is a Rajput, a Sikh, or a Jat. He must remember that he is an Indian.", "Speech, 1947")])

add("br-ambedkar", "B.R. Ambedkar", "B・R・アンベードカル", 1891, 1956, ["in"], ["politics", "philosophy"],
  "B.R. Ambedkar was the chief architect of the Indian Constitution and a champion of the rights of Dalits.", "Born into a Dalit family in Mhow. Overcame severe discrimination to earn doctorates from Columbia and the London School of Economics.", "He transformed Indian society by fighting caste discrimination and drafting the world's longest written constitution.",
  [(1927, "Led the Mahad Satyagraha for Dalit rights to public water"), (1949, "Presented the draft Constitution to the Constituent Assembly")],
  [("Annihilation of Caste", 1936, "Undelivered speech that became a foundational text against the caste system")],
  [("I measure the progress of a community by the degree of progress which women have achieved.", "Constituent Assembly speech")])

add("subhas-chandra-bose", "Subhas Chandra Bose", "スバス・チャンドラ・ボース", 1897, 1945, ["in"], ["politics"],
  "Subhas Chandra Bose was an Indian nationalist leader who sought independence through armed struggle.", "Born in Cuttack, Orissa. Studied at Cambridge and passed the Indian Civil Service exam but resigned.", "His Indian National Army challenged British rule militarily and accelerated Indian independence.",
  [(1943, "Formed the Azad Hind government and led the Indian National Army"), (1944, "Led the INA in the Imphal campaign against British India")],
  [("The Indian Struggle", 1935, "Book on the Indian independence movement")],
  [("Give me blood, and I shall give you freedom.", "Speech to the INA, 1944")])

add("rajendra-prasad", "Rajendra Prasad", "ラージェーンドラ・プラサード", 1884, 1963, ["in"], ["politics"],
  "Rajendra Prasad was the first President of India and a prominent independence leader.", "Born in Ziradei, Bihar. Studied law and became a successful lawyer before joining the freedom movement.", "He served as president of the Constituent Assembly and later as India's first head of state.",
  [(1934, "Elected president of the Indian National Congress"), (1950, "Became the first President of independent India")],
  [("India Divided", 1946, "Book analyzing the problem of partition")],
  [("We must hold together and work together as one people.", "Inaugural address, 1950")])

add("muhammad-ali-jinnah", "Muhammad Ali Jinnah", "ムハンマド・アリー・ジンナー", 1876, 1948, ["pk"], ["politics"],
  "Muhammad Ali Jinnah was the founder of Pakistan and its first Governor-General.", "Born in Karachi. Studied law at Lincoln's Inn in London and returned to practice in Bombay.", "He led the movement for a separate Muslim state, resulting in the creation of Pakistan in 1947.",
  [(1940, "Supported the Lahore Resolution calling for a separate Muslim state"), (1947, "Became the first Governor-General of Pakistan on August 14")],
  [("Lahore Resolution", 1940, "Political resolution calling for independent Muslim states in India")],
  [("With faith, discipline, and selfless devotion to duty, there is nothing worthwhile that you cannot achieve.", "Address to the Constituent Assembly of Pakistan, 1947")])

add("zulfikar-ali-bhutto", "Zulfikar Ali Bhutto", "ズルフィカール・アリー・ブットー", 1928, 1979, ["pk"], ["politics"],
  "Zulfikar Ali Bhutto was the founder of the Pakistan Peoples Party and Prime Minister of Pakistan.", "Born in Larkana, Sindh to a powerful feudal family. Studied at UC Berkeley and Oxford.", "He gave Pakistan its 1973 Constitution and pursued nationalization and land reform policies.",
  [(1967, "Founded the Pakistan Peoples Party"), (1973, "Became Prime Minister and enacted the new constitution")],
  [("The Myth of Independence", 1969, "Book on Pakistan's foreign policy and the need for independent diplomacy")],
  [("Islam is our faith, democracy is our polity, socialism is our economy.", "PPP founding manifesto")])

add("benazir-bhutto", "Benazir Bhutto", "ベーナズィール・ブットー", 1953, 2007, ["pk"], ["politics"],
  "Benazir Bhutto was the first woman to head a democratic government in a Muslim-majority country.", "Born in Karachi. Daughter of Zulfikar Ali Bhutto. Studied at Harvard and Oxford.", "She broke barriers as a female leader in the Muslim world and fought for democracy in Pakistan.",
  [(1988, "Became Prime Minister of Pakistan"), (2007, "Assassinated during a campaign rally in Rawalpindi")],
  [("Daughter of the East", 1988, "Autobiography detailing her life and political struggle")],
  [("Democracy is the best revenge.", "Attributed")])

add("sheikh-mujibur-rahman", "Sheikh Mujibur Rahman", "シェイク・ムジブル・ラフマン", 1920, 1975, ["bd"], ["politics"],
  "Sheikh Mujibur Rahman was the founding father of Bangladesh and its first president.", "Born in Tungipara, Bengal. Studied at the University of Dhaka and became a political activist.", "He led the Bengali independence movement, resulting in the creation of Bangladesh in 1971.",
  [(1971, "Declared the independence of Bangladesh on March 26"), (1972, "Became the first Prime Minister of Bangladesh")],
  [("March 7 Speech", 1971, "Historic speech calling for non-cooperation and independence from Pakistan")],
  [("The struggle this time is for our freedom. The struggle this time is for independence.", "March 7 Speech, 1971")])

add("sirimavo-bandaranaike", "Sirimavo Bandaranaike", "シリマヴォ・バンダラナイケ", 1916, 2000, ["lk"], ["politics"],
  "Sirimavo Bandaranaike was the world's first female prime minister.", "Born in Ratnapura, Ceylon to a wealthy Sinhalese family. Entered politics after the assassination of her husband.", "She proved that women could lead nations at the highest level, serving three terms as prime minister.",
  [(1960, "Became the world's first female prime minister"), (1972, "Transformed Ceylon into the republic of Sri Lanka")],
  [("Republic of Sri Lanka Constitution", 1972, "New constitution enacted under her leadership transforming Ceylon into Sri Lanka")],
  [("I am firm in my belief that a woman can serve her country as well as a man.", "Attributed")])

add("park-chung-hee", "Park Chung-hee", "朴正煕", 1917, 1979, ["kr"], ["politics"],
  "Park Chung-hee was the president of South Korea who led its rapid economic industrialization.", "Born in Gumi, North Gyeongsang Province. Attended military academies in Japan and Korea.", "He oversaw South Korea's transformation from a poor agricultural country into an industrial powerhouse.",
  [(1961, "Seized power through a military coup"), (1972, "Declared the Yushin Constitution, extending his rule")],
  [("Saemaul Undong", 1970, "New Village Movement that modernized rural Korea")],
  [("In human life, economics precedes politics or culture.", "Attributed")])

add("syngman-rhee", "Syngman Rhee", "李承晩", 1875, 1965, ["kr"], ["politics"],
  "Syngman Rhee was the first president of South Korea and a lifelong independence activist.", "Born in Haeju, Hwanghae Province. Studied at George Washington University, Harvard, and Princeton.", "He led the Korean independence movement in exile and became South Korea's founding president.",
  [(1919, "Elected president of the Korean Provisional Government in exile"), (1948, "Became the first president of the Republic of Korea")],
  [("The Spirit of Independence", 1904, "Book written in prison advocating Korean independence and modernization")],
  [("The day will come when Korea shall be free and independent.", "The Spirit of Independence")])

add("kim-il-sung", "Kim Il-sung", "金日成", 1912, 1994, ["kp"], ["politics"],
  "Kim Il-sung was the founder and first leader of North Korea, ruling for nearly five decades.", "Born in Mangyongdae near Pyongyang. Fought as a guerrilla against Japanese occupation in Manchuria.", "He established the North Korean state and the Juche ideology, creating one of the most isolated nations on earth.",
  [(1948, "Became premier of the Democratic People's Republic of Korea"), (1950, "Launched the Korean War by invading South Korea")],
  [("On the Juche Idea", 1982, "Treatise on North Korea's self-reliance ideology")],
  [("The people are my God.", "Attributed")])

add("ferdinand-marcos", "Ferdinand Marcos", "フェルディナンド・マルコス", 1917, 1989, ["ph"], ["politics"],
  "Ferdinand Marcos was the president of the Philippines who imposed martial law and was overthrown by a people's revolution.", "Born in Sarrat, Ilocos Norte. Studied law at the University of the Philippines.", "His authoritarian rule and subsequent overthrow through the EDSA People Power Revolution became a model for nonviolent democratic change.",
  [(1965, "Elected president of the Philippines"), (1986, "Overthrown by the People Power Revolution and fled to Hawaii")],
  [("Proclamation No. 1081", 1972, "Declaration of martial law across the Philippines")],
  [("Leadership is the other side of the coin of loneliness.", "Attributed")])

add("suharto", "Suharto", "スハルト", 1921, 2008, ["id"], ["politics"],
  "Suharto was the second president of Indonesia, ruling for 31 years during the New Order era.", "Born in Kemusuk, Java. Rose through the ranks of the Indonesian military.", "He oversaw significant economic development but also widespread corruption and human rights abuses.",
  [(1967, "Became acting president after the ouster of Sukarno"), (1998, "Resigned after mass protests during the Asian financial crisis")],
  [("Supersemar", 1966, "Letter of authority from Sukarno that Suharto used to assume power")],
  [("Development is the foundation of national stability.", "Attributed")])

# ============================================================
# MODERN ARTISTS / MUSICIANS / WRITERS (~20)
# ============================================================

add("william-butler-yeats", "William Butler Yeats", "ウィリアム・バトラー・イェイツ", 1865, 1939, ["ie"], ["literature"],
  "W.B. Yeats was an Irish poet and one of the foremost figures of 20th-century literature.", "Born in Sandymount, Dublin. Grew up between Dublin and London in an artistic family.", "He was central to the Irish Literary Revival and won the Nobel Prize in Literature.",
  [(1889, "Published The Wanderings of Oisin"), (1923, "Awarded Nobel Prize in Literature")],
  [("The Tower", 1928, "Poetry collection containing some of his finest work including 'Sailing to Byzantium'"), ("A Vision", 1925, "Mystical system explaining history and human personality")],
  [("The best lack all conviction, while the worst are full of passionate intensity.", "The Second Coming")])

add("ts-eliot", "T.S. Eliot", "T・S・エリオット", 1888, 1965, ["us", "gb"], ["literature"],
  "T.S. Eliot was a modernist poet whose works defined 20th-century poetry.", "Born in St. Louis, Missouri. Studied at Harvard, the Sorbonne, and Oxford before settling in England.", "The Waste Land revolutionized English-language poetry and he shaped literary criticism through his essays.",
  [(1922, "Published The Waste Land"), (1948, "Awarded Nobel Prize in Literature")],
  [("The Waste Land", 1922, "Landmark modernist poem on spiritual desolation in post-war Europe"), ("Four Quartets", 1943, "Meditative poems on time, eternity, and redemption")],
  [("April is the cruellest month.", "The Waste Land")])

add("ezra-pound", "Ezra Pound", "エズラ・パウンド", 1885, 1972, ["us"], ["literature"],
  "Ezra Pound was an expatriate American poet and critic who was a driving force behind literary modernism.", "Born in Hailey, Idaho. Studied at Hamilton College and the University of Pennsylvania.", "He shaped modernist poetry through the Imagist movement and his editorial influence on Eliot and other poets.",
  [(1912, "Founded the Imagist movement in London"), (1920, "Published Hugh Selwyn Mauberley and moved to Paris")],
  [("The Cantos", 1970, "Epic poem composed over decades, weaving together history, economics, and literature"), ("Personae", 1909, "Early collection of poems establishing his reputation")],
  [("Make it new.", "Attributed, became the slogan of modernism")])

add("wh-auden", "W.H. Auden", "W・H・オーデン", 1907, 1973, ["gb", "us"], ["literature"],
  "W.H. Auden was one of the greatest poets of the 20th century, known for his technical mastery and moral intelligence.", "Born in York, England. Studied at Oxford where he became the leader of a circle of poets.", "His poetry addressed the political, social, and psychological crises of his time with unmatched formal skill.",
  [(1930, "Published his first major collection, Poems"), (1948, "Won the Pulitzer Prize for The Age of Anxiety")],
  [("The Age of Anxiety", 1947, "Long poem on modern alienation that won the Pulitzer Prize"), ("Another Time", 1940, "Collection containing 'September 1, 1939' and 'Musee des Beaux Arts'")],
  [("We must love one another or die.", "September 1, 1939")])

add("sylvia-plath", "Sylvia Plath", "シルヴィア・プラス", 1932, 1963, ["us"], ["literature"],
  "Sylvia Plath was an American poet and novelist whose confessional poetry explored identity, suffering, and death.", "Born in Boston, Massachusetts. Studied at Smith College and Cambridge on a Fulbright scholarship.", "Her posthumous collection Ariel established her as one of the most powerful poets of the 20th century.",
  [(1960, "Published The Colossus, her first poetry collection"), (1963, "Published The Bell Jar; died in February")],
  [("Ariel", 1965, "Posthumous poetry collection of intense, confessional poems"), ("The Bell Jar", 1963, "Semi-autobiographical novel about a young woman's mental breakdown")],
  [("I took a deep breath and listened to the old brag of my heart. I am, I am, I am.", "The Bell Jar")])

add("allen-ginsberg", "Allen Ginsberg", "アレン・ギンズバーグ", 1926, 1997, ["us"], ["literature"],
  "Allen Ginsberg was a Beat poet whose Howl became a landmark of American countercultural literature.", "Born in Newark, New Jersey. Studied at Columbia University where he befriended Jack Kerouac and William Burroughs.", "Howl challenged censorship and opened American poetry to radical new subjects and forms.",
  [(1955, "Read Howl at the Six Gallery in San Francisco"), (1957, "Howl obscenity trial resulted in a landmark free speech ruling")],
  [("Howl and Other Poems", 1956, "Poetry collection beginning with the famous line 'I saw the best minds of my generation destroyed by madness'")],
  [("I saw the best minds of my generation destroyed by madness.", "Howl")])

add("jack-kerouac", "Jack Kerouac", "ジャック・ケルアック", 1922, 1969, ["us"], ["literature"],
  "Jack Kerouac was a novelist and poet who defined the Beat Generation with his spontaneous prose.", "Born in Lowell, Massachusetts to French-Canadian parents. Attended Columbia University on a football scholarship.", "On the Road became the defining novel of the Beat Generation and inspired decades of countercultural writing.",
  [(1957, "Published On the Road"), (1958, "Published The Dharma Bums")],
  [("On the Road", 1957, "Novel of cross-country travels that defined the Beat Generation"), ("The Dharma Bums", 1958, "Novel exploring Buddhism and outdoor life in 1950s America")],
  [("The only people for me are the mad ones.", "On the Road")])

add("langston-hughes", "Langston Hughes", "ラングストン・ヒューズ", 1901, 1967, ["us"], ["literature"],
  "Langston Hughes was a central figure of the Harlem Renaissance who gave voice to the Black American experience.", "Born in Joplin, Missouri. Grew up moving frequently and studied briefly at Columbia University.", "He was the first African American to earn a living solely from writing and shaped the literary expression of Black identity.",
  [(1926, "Published his first poetry collection, The Weary Blues"), (1930, "Published his first novel, Not Without Laughter")],
  [("The Weary Blues", 1926, "Poetry collection blending jazz rhythms with lyric poetry"), ("Montage of a Dream Deferred", 1951, "Poetry sequence capturing the rhythms and frustrations of Harlem life")],
  [("What happens to a dream deferred?", "Harlem")])

add("zora-neale-hurston", "Zora Neale Hurston", "ゾラ・ニール・ハーストン", 1891, 1960, ["us"], ["literature"],
  "Zora Neale Hurston was a novelist and anthropologist who celebrated Black Southern culture.", "Born in Notasulga, Alabama and raised in Eatonville, Florida, one of the first all-Black towns in America.", "Her masterpiece Their Eyes Were Watching God was rediscovered through Alice Walker's advocacy and became a classic.",
  [(1937, "Published Their Eyes Were Watching God"), (1938, "Published Tell My Horse on Haitian and Jamaican folklore")],
  [("Their Eyes Were Watching God", 1937, "Novel about a Black woman's journey to self-realization in the rural South")],
  [("If you are silent about your pain, they'll kill you and say you enjoyed it.", "Attributed")])

add("james-baldwin", "James Baldwin", "ジェイムズ・ボールドウィン", 1924, 1987, ["us"], ["literature"],
  "James Baldwin was an American writer whose novels and essays explored race, sexuality, and identity in America.", "Born in Harlem, New York. Moved to Paris in 1948 to escape racial discrimination.", "His writing on race in America remains among the most powerful and relevant in the national literature.",
  [(1953, "Published Go Tell It on the Mountain"), (1963, "Published The Fire Next Time during the civil rights movement")],
  [("The Fire Next Time", 1963, "Essay collection on race relations in America"), ("Go Tell It on the Mountain", 1953, "Semi-autobiographical novel about a young man's coming of age in Harlem")],
  [("Not everything that is faced can be changed, but nothing can be changed until it is faced.", "Attributed")])

add("ralph-ellison", "Ralph Ellison", "ラルフ・エリソン", 1913, 1994, ["us"], ["literature"],
  "Ralph Ellison wrote Invisible Man, one of the most important American novels of the 20th century.", "Born in Oklahoma City, Oklahoma. Studied music at Tuskegee Institute before turning to writing.", "Invisible Man gave definitive literary expression to the African American experience of social invisibility.",
  [(1952, "Published Invisible Man"), (1953, "Won the National Book Award for Invisible Man")],
  [("Invisible Man", 1952, "Novel about a Black man navigating American society where his identity is constantly denied")],
  [("I am invisible, understand, simply because people refuse to see me.", "Invisible Man")])

add("richard-wright", "Richard Wright", "リチャード・ライト", 1908, 1960, ["us"], ["literature"],
  "Richard Wright was an American author whose Native Son brought African American literature to a mainstream audience.", "Born on a plantation near Natchez, Mississippi. Grew up in poverty and largely self-educated.", "Native Son forced white America to confront the reality of Black life and inspired generations of Black writers.",
  [(1940, "Published Native Son"), (1945, "Published the autobiography Black Boy")],
  [("Native Son", 1940, "Novel about Bigger Thomas, a young Black man trapped by poverty and racism in Chicago"), ("Black Boy", 1945, "Autobiography of growing up Black in the Jim Crow South")],
  [("The impulse to dream was slowly beaten out of me by experience.", "Black Boy")])

add("maya-angelou", "Maya Angelou", "マヤ・アンジェロウ", 1928, 2014, ["us"], ["literature"],
  "Maya Angelou was an American poet and memoirist whose works celebrated resilience and the human spirit.", "Born in St. Louis, Missouri. Endured a traumatic childhood but found solace in literature.", "I Know Why the Caged Bird Sings became a classic of American autobiography and inspired millions.",
  [(1969, "Published I Know Why the Caged Bird Sings"), (1993, "Read 'On the Pulse of Morning' at President Clinton's inauguration")],
  [("I Know Why the Caged Bird Sings", 1969, "Autobiography of her childhood, one of the first by an African American woman to reach a wide audience")],
  [("There is no greater agony than bearing an untold story inside you.", "I Know Why the Caged Bird Sings")])

add("gwendolyn-brooks", "Gwendolyn Brooks", "グウェンドリン・ブルックス", 1917, 2000, ["us"], ["literature"],
  "Gwendolyn Brooks was the first African American to win the Pulitzer Prize.", "Born in Topeka, Kansas and raised in Chicago. Published her first poem at age 13.", "She brought the lives of ordinary Black Americans into the canon of American poetry.",
  [(1950, "Won the Pulitzer Prize for Annie Allen"), (1968, "Became more politically engaged, embracing the Black Arts Movement")],
  [("Annie Allen", 1949, "Poetry collection tracing a Black woman's life in Chicago"), ("A Street in Bronzeville", 1945, "Poetry collection depicting life in Chicago's Black neighborhoods")],
  [("We are each other's harvest; we are each other's business; we are each other's magnitude and bond.", "Paul Robeson")])

add("rita-dove", "Rita Dove", "リタ・ダヴ", 1952, None, ["us"], ["literature"],
  "Rita Dove is an American poet who served as the youngest and first African American U.S. Poet Laureate.", "Born in Akron, Ohio. Studied at Miami University and the Iowa Writers' Workshop.", "She broadened the scope of American poetry by combining lyrical craft with historical and personal narratives.",
  [(1987, "Won the Pulitzer Prize for Thomas and Beulah"), (1993, "Appointed U.S. Poet Laureate")],
  [("Thomas and Beulah", 1986, "Poetry cycle based on her grandparents' lives, winner of the Pulitzer Prize")],
  [("Poetry is language at its most distilled and most powerful.", "Interview")])

add("naomi-shihab-nye", "Naomi Shihab Nye", "ナオミ・シハブ・ナイ", 1952, None, ["us"], ["literature"],
  "Naomi Shihab Nye is a Palestinian-American poet known for her poems about heritage, peace, and daily life.", "Born in St. Louis, Missouri to a Palestinian father and American mother. Lived in Jerusalem as a teenager.", "Her poetry bridges cultures and advocates for peace, making her one of the most beloved contemporary American poets.",
  [(1980, "Published her first poetry collection"), (2019, "Named Young People's Poet Laureate by the Poetry Foundation")],
  [("Words Under the Words", 1995, "Selected poems drawing on her Arab-American experience")],
  [("Before you know kindness as the deepest thing inside, you must know sorrow as the other deepest thing.", "Kindness")])

add("joy-harjo", "Joy Harjo", "ジョイ・ハージョ", 1951, None, ["us"], ["literature"],
  "Joy Harjo is a Muscogee (Creek) Nation member who served as the first Native American U.S. Poet Laureate.", "Born in Tulsa, Oklahoma. Studied at the University of New Mexico and the Iowa Writers' Workshop.", "She brought Indigenous perspectives and traditions to the center of American literary culture.",
  [(1990, "Published In Mad Love and War"), (2019, "Appointed the first Native American U.S. Poet Laureate")],
  [("In Mad Love and War", 1990, "Poetry collection blending personal and political themes with Indigenous mythology")],
  [("Remember the sky that you were born under, know each of the star's stories.", "Remember")])

add("louise-erdrich", "Louise Erdrich", "ルイーズ・アードリック", 1954, None, ["us"], ["literature"],
  "Louise Erdrich is an Ojibwe author whose novels chronicle Native American life in the northern Midwest.", "Born in Little Falls, Minnesota. Grew up in Wahpeton, North Dakota and studied at Dartmouth and Johns Hopkins.", "Her interconnected novels created a vast literary landscape of Native American experience comparable to Faulkner's Yoknapatawpha.",
  [(1984, "Published Love Medicine, her debut novel"), (2021, "Won the Pulitzer Prize for Fiction for The Night Watchman")],
  [("Love Medicine", 1984, "Interconnected stories of Ojibwe families on a North Dakota reservation"), ("The Night Watchman", 2020, "Novel based on her grandfather's fight against Native American termination policy")],
  [("Life will break you. But you get to choose what grows in the cracks.", "The Painted Drum")])

add("amy-tan", "Amy Tan", "エイミー・タン", 1952, None, ["us"], ["literature"],
  "Amy Tan is a Chinese-American novelist best known for The Joy Luck Club.", "Born in Oakland, California to Chinese immigrant parents. Studied at San Jose State University.", "Her novels gave voice to the Chinese-American immigrant experience and became international bestsellers.",
  [(1989, "Published The Joy Luck Club"), (1991, "Published The Kitchen God's Wife")],
  [("The Joy Luck Club", 1989, "Novel about the relationships between Chinese immigrant mothers and their American-born daughters")],
  [("If you can't change your fate, change your attitude.", "The Joy Luck Club")])

add("sandra-cisneros", "Sandra Cisneros", "サンドラ・シスネロス", 1954, None, ["us"], ["literature"],
  "Sandra Cisneros is a Chicana writer best known for The House on Mango Street.", "Born in Chicago to a Mexican father and Mexican-American mother. Studied at Loyola University and the Iowa Writers' Workshop.", "The House on Mango Street became one of the most widely taught works in American schools, giving voice to Latina experience.",
  [(1984, "Published The House on Mango Street"), (1991, "Published Woman Hollering Creek and Other Stories")],
  [("The House on Mango Street", 1984, "Coming-of-age novel about a young Latina girl growing up in a Chicago barrio")],
  [("I am the one nobody comes for and nobody knows.", "The House on Mango Street")])

add("chinua-achebe", "Chinua Achebe", "チヌア・アチェベ", 1930, 2013, ["ng"], ["literature"],
  "Chinua Achebe was a Nigerian novelist whose Things Fall Apart is the most widely read book in modern African literature.", "Born in Ogidi, Nigeria. Studied at the University of Ibadan.", "He is called the father of African literature in English and challenged Western portrayals of Africa.",
  [(1958, "Published Things Fall Apart"), (2007, "Awarded the Man Booker International Prize")],
  [("Things Fall Apart", 1958, "Novel about the impact of colonialism on Igbo society")],
  [("Until the lions have their own historians, the history of the hunt will always glorify the hunter.", "Attributed")])

add("wole-soyinka", "Wole Soyinka", "ウォーレ・ショインカ", 1934, None, ["ng"], ["literature"],
  "Wole Soyinka is a Nigerian playwright and the first African to win the Nobel Prize in Literature.", "Born in Abeokuta, Nigeria. Studied at the University of Ibadan and the University of Leeds.", "His plays and political activism established African drama on the world stage.",
  [(1965, "Published The Interpreters, his first novel"), (1986, "Awarded Nobel Prize in Literature")],
  [("Death and the King's Horseman", 1975, "Play based on a real event exploring the clash between Yoruba and colonial cultures")],
  [("The man dies in all who keep silent in the face of tyranny.", "The Man Died")])

if __name__ == "__main__":
    write_people(P)
