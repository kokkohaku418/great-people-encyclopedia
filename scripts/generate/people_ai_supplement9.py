#!/usr/bin/env python3
"""Supplement batch 9: more people with dedup."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
PEOPLE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'people')
existing = {f.replace('.json', '') for f in os.listdir(PEOPLE_DIR) if f.endswith('.json')} if os.path.exists(PEOPLE_DIR) else set()
def add(id, *a, **k):
    if id not in existing:
        P.append(person(id, *a, **k))

# ── ANCIENT / MEDIEVAL THINKERS & LEADERS ──

add("thales", "Thales of Miletus", "タレス", -624, -546, ["gr"], ["philosophy"],
  "Thales of Miletus is widely regarded as the first Western philosopher, proposing that water is the fundamental substance of all matter.",
  "Born in Miletus, an ancient Greek city in Ionia. He was likely of Phoenician descent and traveled to Egypt where he studied geometry.",
  "Thales initiated the tradition of natural philosophy, seeking rational explanations for natural phenomena rather than mythological ones.",
  [(-585, "Predicted a solar eclipse"), (-600, "Proposed water as the fundamental substance")],
  [("On the Solstice", -580, "Lost work on astronomical observations")],
  [("Know thyself.", "Attributed by Diogenes Laërtius"), ("The most difficult thing in life is to know yourself.", "Attributed")])

add("democritus", "Democritus", "デモクリトス", -460, -370, ["gr"], ["philosophy"],
  "Democritus developed the atomic theory of the universe, proposing that all matter is composed of indivisible atoms.",
  "Born in Abdera, Thrace. He traveled extensively to Egypt, Persia, and possibly India, studying with various scholars.",
  "His atomic theory anticipated modern physics by over two millennia and influenced Epicurus and later scientific thought.",
  [(-440, "Developed atomic theory with Leucippus"), (-420, "Wrote extensively on ethics, physics, and mathematics")],
  [("The Great World-System", -420, "Treatise on cosmology and atomic theory")],
  [("Nothing exists except atoms and empty space; everything else is opinion.", "Attributed by Diogenes Laërtius")])

add("heraclitus", "Heraclitus", "ヘラクレイトス", -535, -475, ["gr"], ["philosophy"],
  "Heraclitus of Ephesus proposed that change is the fundamental nature of the universe, symbolized by ever-living fire.",
  "Born in Ephesus to an aristocratic family. He was known as 'the obscure' for his cryptic writing style.",
  "His doctrine of universal flux and the unity of opposites profoundly influenced Plato, Hegel, and modern process philosophy.",
  [(-500, "Wrote his major philosophical work"), (-504, "Declined the kingship of Ephesus")],
  [("On Nature", -500, "Fragments of his philosophical treatise on logos and flux")],
  [("No man ever steps in the same river twice.", "Fragment 91"), ("Character is destiny.", "Fragment 119")])

add("parmenides", "Parmenides", "パルメニデス", -515, -450, ["gr"], ["philosophy"],
  "Parmenides of Elea founded the Eleatic school and argued that reality is a single, unchanging, eternal being.",
  "Born in Elea, a Greek colony in southern Italy. He may have studied with Xenophanes and the Pythagoreans.",
  "His logical argumentation about the nature of being influenced Plato's theory of Forms and all subsequent Western metaphysics.",
  [(-480, "Wrote his philosophical poem On Nature"), (-450, "Met the young Socrates in Athens according to Plato")],
  [("On Nature", -480, "Philosophical poem presenting the Way of Truth and the Way of Opinion")],
  [("What is, is; and what is not, cannot be.", "On Nature")])

add("diogenes", "Diogenes of Sinope", "ディオゲネス", -412, -323, ["gr"], ["philosophy"],
  "Diogenes of Sinope was the most famous Cynic philosopher, advocating a life of virtue in accordance with nature.",
  "Born in Sinope on the Black Sea. He was exiled and moved to Athens where he lived in extreme poverty by choice.",
  "His radical rejection of social conventions and materialism inspired the Stoics and remains a symbol of philosophical freedom.",
  [(-340, "Famously told Alexander the Great to stand out of his sunlight"), (-350, "Lived in a ceramic jar in the Athenian marketplace")],
  [("Republic", -350, "Lost work advocating a cosmopolitan society without conventional institutions")],
  [("I am a citizen of the world.", "Attributed by Diogenes Laërtius"), ("It is the privilege of the gods to want nothing, and of godlike men to want little.", "Attributed")])

add("thucydides", "Thucydides", "トゥキュディデス", -460, -400, ["gr"], ["literature"],
  "Thucydides wrote the History of the Peloponnesian War, establishing rigorous standards of historical evidence and analysis.",
  "Born in Athens to a wealthy Thracian family. He served as an Athenian general but was exiled after failing to prevent the capture of Amphipolis.",
  "His systematic approach to historical inquiry, rejecting myths and seeking causes, made him the father of scientific history.",
  [(-424, "Exiled from Athens after military failure"), (-411, "Wrote the History of the Peloponnesian War")],
  [("History of the Peloponnesian War", -411, "Detailed account of the war between Athens and Sparta")],
  [("The strong do what they can and the weak suffer what they must.", "Melian Dialogue")])

add("herodotus", "Herodotus", "ヘロドトス", -484, -425, ["gr"], ["literature"],
  "Herodotus is called the Father of History for his systematic investigation of the Greco-Persian Wars and the cultures he encountered.",
  "Born in Halicarnassus in Caria. He traveled extensively throughout the Mediterranean and Near East gathering accounts.",
  "His Histories pioneered the genre of historical writing and provided invaluable ethnographic records of the ancient world.",
  [(-450, "Traveled through Egypt, Babylon, and Scythia"), (-440, "Composed The Histories")],
  [("The Histories", -440, "Nine-book account of the Greco-Persian Wars and the peoples of the known world")],
  [("Of all men's miseries the bitterest is this: to know so much and to have control over nothing.", "The Histories")])

add("sappho", "Sappho", "サッポー", -630, -570, ["gr"], ["literature"],
  "Sappho of Lesbos was one of the greatest lyric poets of antiquity, celebrated for her passionate and intimate verse.",
  "Born on the island of Lesbos. She ran a school for young women devoted to the Muses and Aphrodite.",
  "Her lyric poetry set the standard for personal expression in verse and influenced Roman poets and all subsequent Western lyric traditions.",
  [(-600, "Led a literary circle on Lesbos"), (-590, "Composed her major lyric works")],
  [("Ode to Aphrodite", -600, "The only fully surviving poem, a prayer to the goddess of love")],
  [("What is beautiful is good, and who is good will soon be beautiful.", "Fragment 101")])

add("aeschylus", "Aeschylus", "アイスキュロス", -525, -456, ["gr"], ["literature"],
  "Aeschylus is the father of Greek tragedy, introducing dialogue between characters and reducing the role of the chorus.",
  "Born in Eleusis near Athens. He fought at the Battle of Marathon and possibly Salamis.",
  "His dramatic innovations created the genre of tragedy as it is understood today, influencing all subsequent Western drama.",
  [(-484, "Won his first prize at the City Dionysia"), (-458, "Produced the Oresteia trilogy")],
  [("The Oresteia", -458, "Trilogy of tragedies exploring justice, vengeance, and the founding of Athenian democracy")],
  [("He who learns must suffer. And even in our sleep, pain that cannot forget falls drop by drop upon the heart.", "Agamemnon")])

add("sophocles", "Sophocles", "ソポクレス", -496, -406, ["gr"], ["literature"],
  "Sophocles was one of the three great tragedians of classical Athens, known for masterful character development and dramatic irony.",
  "Born in Colonus near Athens to a wealthy family. He won his first victory at the Dionysia at age 28, defeating Aeschylus.",
  "His plays, especially Oedipus Rex, set the standard for tragic drama and remain central to the Western literary canon.",
  [(-468, "Won first prize at the City Dionysia"), (-441, "Served as one of the ten Athenian generals")],
  [("Oedipus Rex", -429, "Tragedy considered the perfect example of dramatic structure by Aristotle")],
  [("The greatest griefs are those we cause ourselves.", "Oedipus Rex")])

add("euripides", "Euripides", "エウリピデス", -480, -406, ["gr"], ["literature"],
  "Euripides was the most modern of the three great Athenian tragedians, known for realistic characters and questioning traditional values.",
  "Born in Salamis. Unlike Aeschylus and Sophocles, he was somewhat reclusive and less involved in public life.",
  "His psychologically complex characters and willingness to challenge convention deeply influenced later drama, from Roman tragedy to modern theater.",
  [(-455, "Won his first prize at the Dionysia"), (-408, "Moved to the court of King Archelaus of Macedon")],
  [("Medea", -431, "Tragedy exploring the psychology of a betrayed woman who takes terrible revenge")],
  [("Whom the gods would destroy, they first make mad.", "Attributed")])

add("aristophanes", "Aristophanes", "アリストパネス", -446, -386, ["gr"], ["literature"],
  "Aristophanes was the greatest comic playwright of ancient Athens, known for sharp political satire and imaginative fantasy.",
  "Born in Athens. Little is known of his early life, but he began writing comedies as a young man.",
  "His comedies are the only surviving examples of Old Comedy and provide invaluable insight into Athenian social and political life.",
  [(-425, "Won first prize with The Acharnians"), (-405, "Produced The Frogs")],
  [("The Clouds", -423, "Satirical comedy mocking Socrates and the Sophists")],
  [("Open your mind before your mouth.", "Attributed")])

add("lucretius", "Lucretius", "ルクレティウス", -99, -55, ["it"], ["philosophy"],
  "Lucretius was a Roman poet and philosopher whose epic poem De Rerum Natura expounded Epicurean physics and philosophy.",
  "Very little is known about his life. He was likely a Roman aristocrat who devoted himself to philosophical poetry.",
  "De Rerum Natura preserved and transmitted Epicurean atomism, influencing the Scientific Revolution and modern materialism.",
  [(-60, "Composed De Rerum Natura"), (-55, "Died, possibly by suicide according to later tradition")],
  [("De Rerum Natura", -60, "Epic philosophical poem on the nature of the universe based on Epicurean atomism")],
  [("Nothing can be created out of nothing.", "De Rerum Natura, Book I")])

add("cicero", "Marcus Tullius Cicero", "キケロ", -106, -43, ["it"], ["philosophy", "politics"],
  "Cicero was Rome's greatest orator and a pivotal figure in transmitting Greek philosophy to the Latin-speaking world.",
  "Born in Arpinum to an equestrian family. He studied philosophy and rhetoric in Rome, Athens, and Rhodes.",
  "His speeches, letters, and philosophical works shaped Latin prose style and profoundly influenced the Renaissance and Enlightenment.",
  [(-63, "Suppressed the Catiline Conspiracy as consul"), (-43, "Executed on orders of Mark Antony")],
  [("De Re Publica", -51, "Philosophical dialogue on the ideal state and natural law")],
  [("A room without books is like a body without a soul.", "Attributed"), ("The safety of the people shall be the highest law.", "De Legibus")])

add("hammurabi", "Hammurabi", "ハンムラビ", -1810, -1750, ["iq"], ["politics"],
  "Hammurabi was the sixth king of the First Babylonian Dynasty, famous for one of the earliest known written legal codes.",
  "He inherited a small kingdom centered on Babylon and through military campaigns and diplomacy united most of Mesopotamia.",
  "The Code of Hammurabi established the principle of written law and influenced legal traditions throughout the ancient Near East.",
  [(-1792, "Became king of Babylon"), (-1754, "Promulgated the Code of Hammurabi")],
  [("Code of Hammurabi", -1754, "Collection of 282 laws inscribed on a stone stele")],
  [("If a man put out the eye of another man, his eye shall be put out.", "Code of Hammurabi, Law 196")])

# ── RENAISSANCE & EARLY MODERN FIGURES ──

add("machiavelli", "Niccolò Machiavelli", "ニッコロ・マキャヴェッリ", 1469, 1527, ["it"], ["philosophy", "politics"],
  "Machiavelli was a Florentine diplomat and political theorist whose works founded modern political science.",
  "Born in Florence to a modest noble family. He served as a senior official in the Florentine Republic.",
  "The Prince and Discourses on Livy established the study of politics as a pragmatic discipline separate from morality and theology.",
  [(1498, "Appointed Second Chancellor of the Republic of Florence"), (1513, "Wrote The Prince")],
  [("The Prince", 1513, "Treatise on political power and statecraft"), ("Discourses on Livy", 1517, "Analysis of republican government")],
  [("It is better to be feared than loved, if you cannot be both.", "The Prince")])

add("monteverdi", "Claudio Monteverdi", "クラウディオ・モンテヴェルディ", 1567, 1643, ["it"], ["art"],
  "Monteverdi was a revolutionary composer who bridged the Renaissance and Baroque periods and helped create the art of opera.",
  "Born in Cremona. He studied music under Marc'Antonio Ingegneri and entered the service of the Duke of Mantua.",
  "His operas and madrigals transformed Western music, establishing opera as a major art form and pioneering expressive dramatic music.",
  [(1607, "Premiered L'Orfeo, often considered the first great opera"), (1613, "Appointed maestro di cappella at St. Mark's Basilica, Venice")],
  [("L'Orfeo", 1607, "Opera retelling the myth of Orpheus, a landmark in music history")],
  [("The end of all good music is to affect the soul.", "Attributed")])

add("palestrina", "Giovanni Pierluigi da Palestrina", "パレストリーナ", 1525, 1594, ["it"], ["art"],
  "Palestrina was the foremost composer of Renaissance polyphony, whose works became the model for sacred music composition.",
  "Born in Palestrina near Rome. He served as a choirboy at the basilica of Santa Maria Maggiore in Rome.",
  "His smooth, flowing polyphonic style saved polyphonic church music from being banned by the Council of Trent and set standards for centuries.",
  [(1554, "Published his first book of Masses"), (1571, "Returned as choirmaster of the Sistine Chapel")],
  [("Missa Papae Marcelli", 1567, "Mass demonstrating that polyphony could serve liturgical text intelligibly")],
  [("Music is the art of the prophets and the gift of God.", "Attributed")])

add("christopher-wren", "Christopher Wren", "クリストファー・レン", 1632, 1723, ["gb"], ["engineering"],
  "Christopher Wren was England's greatest architect, who redesigned London after the Great Fire and built St Paul's Cathedral.",
  "Born in East Knoyle, Wiltshire. He was a brilliant mathematician and astronomer before turning to architecture.",
  "His architectural works defined the English Baroque style and reshaped the skyline of London for centuries.",
  [(1666, "Commissioned to rebuild London churches after the Great Fire"), (1675, "Began construction of St Paul's Cathedral")],
  [("St Paul's Cathedral", 1710, "Masterpiece of English Baroque architecture, completed after 35 years")],
  [("Architecture aims at Eternity.", "Parentalia")])

add("william-blake", "William Blake", "ウィリアム・ブレイク", 1757, 1827, ["gb"], ["art", "literature"],
  "William Blake was a visionary poet, painter, and printmaker whose works combined prophetic imagination with artistic innovation.",
  "Born in London to a hosier's family. He trained as an engraver and developed his unique method of illuminated printing.",
  "His poetry and art challenged Enlightenment rationalism and inspired the Romantic movement, Symbolism, and modern counterculture.",
  [(1789, "Published Songs of Innocence"), (1794, "Published Songs of Innocence and of Experience")],
  [("Songs of Innocence and of Experience", 1794, "Collection of illustrated poems exploring the two contrary states of the human soul")],
  [("To see a World in a Grain of Sand, and a Heaven in a Wild Flower.", "Auguries of Innocence")])

add("samuel-johnson", "Samuel Johnson", "サミュエル・ジョンソン", 1709, 1784, ["gb"], ["literature"],
  "Samuel Johnson was the dominant literary figure of mid-18th century England, famous for his dictionary and brilliant conversation.",
  "Born in Lichfield, Staffordshire. He attended Pembroke College, Oxford, but left without a degree due to lack of funds.",
  "His Dictionary of the English Language standardized English spelling and usage, and his literary criticism shaped English letters.",
  [(1755, "Published A Dictionary of the English Language"), (1763, "Met James Boswell, who would write his famous biography")],
  [("A Dictionary of the English Language", 1755, "Landmark English dictionary that took nine years to compile")],
  [("When a man is tired of London, he is tired of life.", "Recorded by Boswell")])

add("jonathan-swift", "Jonathan Swift", "ジョナサン・スウィフト", 1667, 1745, ["ie", "gb"], ["literature"],
  "Jonathan Swift was an Anglo-Irish satirist and essayist, best known for Gulliver's Travels, one of literature's greatest satires.",
  "Born in Dublin to English parents. He was educated at Trinity College Dublin and later ordained as an Anglican clergyman.",
  "His savage wit and satirical genius exposed political corruption and human folly, establishing satire as a powerful literary form.",
  [(1704, "Published A Tale of a Tub and The Battle of the Books"), (1726, "Published Gulliver's Travels")],
  [("Gulliver's Travels", 1726, "Satirical novel using fantastical voyages to critique human nature and society")],
  [("Satire is a sort of glass wherein beholders do generally discover everybody's face but their own.", "The Battle of the Books")])

add("daniel-defoe", "Daniel Defoe", "ダニエル・デフォー", 1660, 1731, ["gb"], ["literature"],
  "Daniel Defoe was an English writer and journalist, widely considered a founder of the English novel.",
  "Born in London to a family of Dissenters. He worked as a merchant and political pamphleteer before turning to fiction.",
  "Robinson Crusoe became one of the most widely published books in history and helped establish the novel as a literary form.",
  [(1719, "Published Robinson Crusoe"), (1722, "Published Moll Flanders and A Journal of the Plague Year")],
  [("Robinson Crusoe", 1719, "Novel about a castaway's survival on a remote island, often called the first English novel")],
  [("The soul is placed in the body like a rough diamond, and must be polished.", "Attributed")])

add("moliere", "Molière", "モリエール", 1622, 1673, ["fr"], ["literature"],
  "Molière was France's greatest comic playwright, whose satirical comedies remain central to world theater.",
  "Born Jean-Baptiste Poquelin in Paris. He abandoned a career in law to become an actor and playwright.",
  "His comedies of manners exposed hypocrisy and pretension, defining French classical comedy and influencing all subsequent European theater.",
  [(1659, "Achieved success with The Precious Ridicules"), (1664, "Performed Tartuffe, which was immediately banned")],
  [("Tartuffe", 1664, "Comedy satirizing religious hypocrisy"), ("The Misanthrope", 1666, "Comedy examining social dishonesty")],
  [("The duty of comedy is to correct men by amusing them.", "Attributed")])

add("jean-racine", "Jean Racine", "ジャン・ラシーヌ", 1639, 1699, ["fr"], ["literature"],
  "Jean Racine was the master of French classical tragedy, renowned for his elegant verse and psychological depth.",
  "Born in La Ferté-Milon. Orphaned young, he was educated by Jansenist monks at Port-Royal.",
  "His tragedies set the standard for French dramatic poetry and remain among the finest achievements of the French language.",
  [(1667, "Achieved fame with Andromaque"), (1677, "Wrote Phèdre, then retired from theater")],
  [("Phèdre", 1677, "Tragedy based on Euripides, considered the pinnacle of French classical drama")],
  [("There are no secrets that time does not reveal.", "Britannicus")])

add("pierre-corneille", "Pierre Corneille", "ピエール・コルネイユ", 1606, 1684, ["fr"], ["literature"],
  "Pierre Corneille was a founding figure of French classical tragedy, known for heroic dramas exploring duty and honor.",
  "Born in Rouen to a family of lawyers. He studied law before turning to playwriting.",
  "His tragedies established the conventions of French classical theater and explored the conflict between love and duty.",
  [(1637, "Premiered Le Cid, causing a literary controversy"), (1647, "Elected to the Académie française")],
  [("Le Cid", 1637, "Tragicomedy based on a Spanish hero, sparking debate over classical dramatic rules")],
  [("To conquer without risk is to triumph without glory.", "Le Cid")])

add("edmund-spenser", "Edmund Spenser", "エドマンド・スペンサー", 1552, 1599, ["gb"], ["literature"],
  "Edmund Spenser was one of the greatest English poets, whose allegorical epic The Faerie Queene influenced English verse for centuries.",
  "Born in London. He studied at Pembroke College, Cambridge, and later served as a colonial administrator in Ireland.",
  "The Faerie Queene established the Spenserian stanza and became a cornerstone of English Renaissance literature.",
  [(1579, "Published The Shepheardes Calender"), (1590, "Published the first three books of The Faerie Queene")],
  [("The Faerie Queene", 1590, "Allegorical epic poem celebrating the Tudor dynasty and Protestant virtues")],
  [("Sleep after toil, port after stormy seas, ease after war, death after life does greatly please.", "The Faerie Queene")])

add("john-milton", "John Milton", "ジョン・ミルトン", 1608, 1674, ["gb"], ["literature"],
  "John Milton was an English poet whose epic Paradise Lost is one of the supreme achievements of Western literature.",
  "Born in London to a prosperous family. He was educated at Christ's College, Cambridge and traveled in Italy.",
  "Paradise Lost reinvented the epic genre, and his political writings championed freedom of speech and republican government.",
  [(1644, "Published Areopagitica defending freedom of the press"), (1667, "Published Paradise Lost")],
  [("Paradise Lost", 1667, "Epic poem on the Fall of Man, exploring free will, temptation, and redemption")],
  [("The mind is its own place, and in itself can make a heaven of hell, a hell of heaven.", "Paradise Lost")])

add("ben-jonson", "Ben Jonson", "ベン・ジョンソン", 1572, 1637, ["gb"], ["literature"],
  "Ben Jonson was a major English playwright and poet, Shakespeare's chief rival, who championed classical dramatic principles.",
  "Born in London. He worked as a bricklayer and soldier before turning to acting and writing for the theater.",
  "His comedies of humours and critical writings shaped English drama and literary theory for generations.",
  [(1598, "Achieved fame with Every Man in His Humour"), (1616, "Published his collected Works, the first English playwright to do so")],
  [("Volpone", 1606, "Satirical comedy about greed and deception in Venice")],
  [("Drink to me only with thine eyes, and I will pledge with mine.", "To Celia")])

add("lope-de-vega", "Lope de Vega", "ロペ・デ・ベガ", 1562, 1635, ["es"], ["literature"],
  "Lope de Vega was Spain's most prolific dramatist, writing an estimated 1,800 plays and helping define the Spanish Golden Age theater.",
  "Born in Madrid to a modest family. His extraordinary literary talent was evident from childhood.",
  "He revolutionized Spanish drama by breaking classical rules and creating the comedia nueva, influencing European theater.",
  [(1598, "Published La Arcadia and La Dragontea"), (1609, "Published The New Art of Writing Plays, his dramatic manifesto")],
  [("Fuenteovejuna", 1619, "Play about a village uprising against a tyrannical commander")],
  [("Harmony is pure love, for love is complete agreement.", "Attributed")])

# ── SCIENTISTS & MATHEMATICIANS ──

add("joseph-fourier", "Joseph Fourier", "ジョゼフ・フーリエ", 1768, 1830, ["fr"], ["mathematics", "physics"],
  "Joseph Fourier developed Fourier analysis, showing that any function can be represented as a series of sines and cosines.",
  "Born in Auxerre to a tailor's family. Orphaned at age nine, he was educated at a military school run by Benedictines.",
  "Fourier analysis became indispensable across mathematics, physics, and engineering, from signal processing to quantum mechanics.",
  [(1807, "Presented his theory of heat conduction to the French Academy"), (1822, "Published Théorie analytique de la chaleur")],
  [("Théorie analytique de la chaleur", 1822, "Foundational work on heat conduction introducing Fourier series")],
  [("Mathematics compares the most diverse phenomena and discovers the secret analogies that unite them.", "Théorie analytique de la chaleur")])

add("simeon-denis-poisson", "Siméon Denis Poisson", "シメオン・ドニ・ポアソン", 1781, 1840, ["fr"], ["mathematics", "physics"],
  "Poisson made fundamental contributions to mathematical physics, probability theory, and pure mathematics.",
  "Born in Pithiviers. His father was a soldier. He studied at the École Polytechnique under Lagrange and Laplace.",
  "The Poisson distribution, Poisson's equation, and his work on elasticity remain cornerstones of applied mathematics.",
  [(1806, "Appointed professor at the École Polytechnique"), (1837, "Published Recherches sur la probabilité des jugements")],
  [("Recherches sur la probabilité des jugements", 1837, "Work introducing the Poisson distribution")],
  [("Life is good for only two things: discovering mathematics and teaching mathematics.", "Attributed")])

add("adrien-marie-legendre", "Adrien-Marie Legendre", "アドリアン＝マリ・ルジャンドル", 1752, 1833, ["fr"], ["mathematics"],
  "Legendre made major contributions to number theory, statistics, and analysis, including the method of least squares.",
  "Born in Paris to a wealthy family. He studied at the Collège Mazarin and taught at the École Militaire.",
  "Legendre polynomials, the Legendre transform, and his work on elliptic integrals remain fundamental across mathematics and physics.",
  [(1782, "Won the Berlin Academy prize for his work on projectile trajectories"), (1798, "Published his conjecture on the prime-counting function")],
  [("Essai sur la théorie des nombres", 1798, "Major treatise on number theory")],
  [("The method of least squares is applicable to the most varied investigations.", "Nouvelles méthodes pour la détermination des orbites des comètes")])

add("sophus-lie", "Sophus Lie", "ソフス・リー", 1842, 1899, ["no"], ["mathematics"],
  "Sophus Lie created the theory of continuous transformation groups, now called Lie groups, fundamental to modern mathematics and physics.",
  "Born in Nordfjordeid, Norway. He studied at the University of Christiania and was influenced by the geometers Plücker and Klein.",
  "Lie groups and Lie algebras became essential tools in differential equations, geometry, and theoretical physics, especially quantum mechanics.",
  [(1870, "Began developing the theory of continuous groups"), (1886, "Succeeded Felix Klein at the University of Leipzig")],
  [("Theorie der Transformationsgruppen", 1893, "Three-volume work establishing the theory of Lie groups")],
  [("Among all the mathematical disciplines, the theory of differential equations is the most important.", "Attributed")])

add("felix-hausdorff", "Felix Hausdorff", "フェリックス・ハウスドルフ", 1868, 1942, ["de"], ["mathematics"],
  "Felix Hausdorff was a pioneer of topology and set theory who introduced the concept of Hausdorff spaces and fractal dimension.",
  "Born in Breslau to a Jewish merchant family. He studied astronomy and mathematics at the University of Leipzig.",
  "His Grundzüge der Mengenlehre laid the foundations of general topology and measure theory, shaping modern mathematics.",
  [(1914, "Published Grundzüge der Mengenlehre"), (1942, "Took his own life to avoid deportation to a concentration camp")],
  [("Grundzüge der Mengenlehre", 1914, "Foundational textbook establishing general topology as a discipline")],
  [("The mathematician is not a discoverer but an inventor.", "Attributed")])

add("andre-weil", "André Weil", "アンドレ・ヴェイユ", 1906, 1998, ["fr", "us"], ["mathematics"],
  "André Weil was one of the most influential mathematicians of the 20th century and a founding member of the Bourbaki group.",
  "Born in Paris, brother of philosopher Simone Weil. He showed mathematical talent from childhood and studied at the École Normale Supérieure.",
  "His Weil conjectures inspired vast developments in algebraic geometry, and Bourbaki reshaped the organization of mathematics.",
  [(1934, "Co-founded the Bourbaki group"), (1949, "Formulated the Weil conjectures")],
  [("Foundations of Algebraic Geometry", 1946, "Landmark text reformulating algebraic geometry with modern rigor")],
  [("God exists since mathematics is consistent, and the Devil exists since we cannot prove it.", "Attributed")])

add("georges-lemaitre", "Georges Lemaître", "ジョルジュ・ルメートル", 1894, 1966, ["be"], ["physics", "astronomy"],
  "Georges Lemaître was a Belgian priest and physicist who first proposed the Big Bang theory of the origin of the universe.",
  "Born in Charleroi, Belgium. He served as an artillery officer in World War I, then studied physics and was ordained a Catholic priest.",
  "His hypothesis of the primeval atom anticipated the Big Bang theory, fundamentally changing our understanding of cosmology.",
  [(1927, "Published his theory of an expanding universe"), (1931, "Proposed the primeval atom hypothesis")],
  [("Un Univers homogène de masse constante et de rayon croissant", 1927, "Paper proposing the expansion of the universe")],
  [("The evolution of the world can be compared to a display of fireworks that has just ended.", "The Primeval Atom")])

add("meghnad-saha", "Meghnad Saha", "メーグナード・サーハー", 1893, 1956, ["in"], ["physics"],
  "Meghnad Saha developed the Saha ionization equation, which explains the physical and chemical conditions in stars.",
  "Born in Sheoratali, Bengal, to a poor shopkeeper's family. He overcame poverty to study at Presidency College, Calcutta.",
  "The Saha equation became a cornerstone of astrophysics, enabling the classification of stellar spectra by temperature.",
  [(1920, "Published the Saha ionization equation"), (1927, "Elected Fellow of the Royal Society")],
  [("On Ionization in the Solar Chromosphere", 1920, "Paper introducing the Saha ionization equation")],
  [("Science is the greatest collective human endeavour.", "Attributed")])

add("jagadish-chandra-bose", "Jagadish Chandra Bose", "ジャガディッシュ・チャンドラ・ボース", 1858, 1937, ["in"], ["physics", "biology"],
  "J.C. Bose was a pioneer of radio science and plant physiology who demonstrated that plants respond to stimuli.",
  "Born in Munshiganj, Bengal. He studied at St. Xavier's College, Calcutta, and the University of Cambridge.",
  "His work on radio waves preceded Marconi's, and his plant physiology research anticipated modern biophysics.",
  [(1895, "Demonstrated wireless communication using radio waves"), (1901, "Published Response in the Living and Non-Living")],
  [("Response in the Living and Non-Living", 1902, "Work demonstrating similarities between plant and animal tissue responses")],
  [("I shall devote my life to science for the benefit of humanity.", "Attributed")])

add("har-gobind-khorana", "Har Gobind Khorana", "ハー・ゴビンド・コラナ", 1922, 2011, ["in", "us"], ["chemistry", "biology"],
  "Har Gobind Khorana shared the Nobel Prize for deciphering the genetic code and synthesizing the first artificial gene.",
  "Born in Raipur, Punjab (now Pakistan), to a poor family. He studied at Punjab University and the University of Liverpool.",
  "His work on the genetic code and gene synthesis laid the groundwork for genetic engineering and molecular biology.",
  [(1968, "Shared the Nobel Prize in Physiology or Medicine"), (1970, "Synthesized the first artificial gene")],
  [("Polynucleotide Synthesis and the Genetic Code", 1968, "Nobel lecture on deciphering the genetic code")],
  [("My work is my life, and my life is my work.", "Attributed")])

add("vikram-sarabhai", "Vikram Sarabhai", "ヴィクラム・サラバイ", 1919, 1971, ["in"], ["physics", "engineering"],
  "Vikram Sarabhai was the father of the Indian space program and a pioneer in applying science to national development.",
  "Born in Ahmedabad to a prominent industrialist family. He studied at Cambridge under C.V. Raman and at the Cavendish Laboratory.",
  "He founded ISRO and the Physical Research Laboratory, establishing India as a space-faring nation.",
  [(1947, "Founded the Physical Research Laboratory in Ahmedabad"), (1969, "Founded the Indian Space Research Organisation")],
  [("Cosmic Ray Studies", 1947, "Research on cosmic rays and their relationship to solar activity")],
  [("There are some who question the relevance of space activities in a developing nation. To us, there is no ambiguity of purpose.", "Address on the Indian space program")])

add("apj-abdul-kalam", "A.P.J. Abdul Kalam", "A・P・J・アブドゥル・カラーム", 1931, 2015, ["in"], ["engineering"],
  "A.P.J. Abdul Kalam was India's Missile Man and 11th President, who led the development of India's ballistic missile and nuclear weapons programs.",
  "Born in Rameswaram, Tamil Nadu, to a boat owner's family. He studied aerospace engineering at MIT, Chennai.",
  "He transformed India's defense capabilities and inspired millions as a scientist-president dedicated to national development.",
  [(1980, "Successfully launched India's first satellite launch vehicle SLV-III"), (2002, "Elected 11th President of India")],
  [("Wings of Fire", 1999, "Autobiography tracing his rise from humble origins to leading India's missile program")],
  [("You have to dream before your dreams can come true.", "Wings of Fire")])

add("prasanta-chandra-mahalanobis", "Prasanta Chandra Mahalanobis", "プラサンタ・チャンドラ・マハラノビス", 1893, 1972, ["in"], ["mathematics"],
  "Mahalanobis founded the Indian Statistical Institute and developed the Mahalanobis distance, a key concept in multivariate statistics.",
  "Born in Calcutta to a prominent Bengali family. He studied physics at Presidency College and King's College, Cambridge.",
  "His statistical methods shaped India's economic planning, and the Mahalanobis distance remains fundamental in data science.",
  [(1931, "Founded the Indian Statistical Institute"), (1936, "Introduced the Mahalanobis distance")],
  [("On the Generalized Distance in Statistics", 1936, "Paper introducing the Mahalanobis distance measure")],
  [("Statistics must have a purpose. It must serve social needs.", "Attributed")])

add("jean-victor-poncelet", "Jean-Victor Poncelet", "ジャン＝ヴィクトル・ポンスレ", 1788, 1867, ["fr"], ["mathematics", "engineering"],
  "Poncelet was a founder of projective geometry who developed key concepts while imprisoned during Napoleon's Russian campaign.",
  "Born in Metz. He studied at the École Polytechnique and served as a military engineer under Napoleon.",
  "His Traité des propriétés projectives established projective geometry as a major branch of mathematics.",
  [(1822, "Published Traité des propriétés projectives des figures"), (1812, "Imprisoned in Russia after the Battle of Krasnoi")],
  [("Traité des propriétés projectives des figures", 1822, "Foundational text of modern projective geometry")],
  [("Geometry is the art of reasoning well from badly drawn figures.", "Attributed")])

add("joseph-louis-gay-lussac", "Joseph Louis Gay-Lussac", "ジョゼフ・ルイ・ゲイ＝リュサック", 1778, 1850, ["fr"], ["chemistry", "physics"],
  "Gay-Lussac discovered the law of combining gas volumes and made pioneering balloon ascents to study the atmosphere.",
  "Born in Saint-Léonard-de-Noblat. He studied at the École Polytechnique under Berthollet.",
  "His gas laws and volumetric analysis methods became fundamental to chemistry and atmospheric science.",
  [(1804, "Made record-breaking balloon ascent to 7,016 meters to study the atmosphere"), (1808, "Published the law of combining volumes")],
  [("Memoir on the Combination of Gaseous Substances", 1809, "Paper establishing the law of combining gas volumes")],
  [("In the sciences, we must be interested in things, not in persons.", "Attributed")])

add("max-von-laue", "Max von Laue", "マックス・フォン・ラウエ", 1879, 1960, ["de"], ["physics"],
  "Max von Laue discovered the diffraction of X-rays by crystals, proving both the wave nature of X-rays and the atomic structure of crystals.",
  "Born in Pfaffendorf, Germany. He studied under Max Planck at the University of Berlin.",
  "X-ray diffraction became the primary tool for determining crystal structures, enabling advances across chemistry, biology, and materials science.",
  [(1912, "Discovered X-ray diffraction by crystals"), (1914, "Awarded the Nobel Prize in Physics")],
  [("Concerning the Detection of X-ray Interferences", 1912, "Paper announcing the discovery of X-ray diffraction")],
  [("Science progresses through bold hypotheses and careful experiments.", "Attributed")])

add("james-franck", "James Franck", "ジェームズ・フランク", 1882, 1964, ["de", "us"], ["physics"],
  "James Franck, with Gustav Hertz, demonstrated the quantization of energy in atoms through electron-bombardment experiments.",
  "Born in Hamburg to a Jewish banking family. He studied at the University of Berlin.",
  "The Franck-Hertz experiment provided direct proof of quantum energy levels in atoms, confirming Bohr's atomic model.",
  [(1914, "Conducted the Franck-Hertz experiment"), (1925, "Awarded the Nobel Prize in Physics with Gustav Hertz")],
  [("On Collisions Between Electrons and Mercury Vapor Molecules", 1914, "Paper on the experiment confirming quantized atomic energy levels")],
  [("I could not lend my name to a cause which I did not believe would bring the desired result.", "Letter opposing use of atomic bomb, 1945")])

add("gustav-hertz-physicist", "Gustav Hertz", "グスタフ・ヘルツ", 1887, 1975, ["de"], ["physics"],
  "Gustav Hertz, with James Franck, performed the Franck-Hertz experiment confirming quantized energy levels in atoms.",
  "Born in Hamburg, nephew of Heinrich Hertz. He studied at the universities of Göttingen, Munich, and Berlin.",
  "The Franck-Hertz experiment was one of the first direct experimental confirmations of quantum theory.",
  [(1914, "Conducted the Franck-Hertz experiment with James Franck"), (1925, "Awarded the Nobel Prize in Physics")],
  [("On Collisions Between Electrons and Mercury Vapor Molecules", 1914, "Collaborative paper with Franck on quantized energy levels")],
  [("Experiment is the sole judge of scientific truth.", "Attributed")])

add("otto-stern", "Otto Stern", "オットー・シュテルン", 1888, 1969, ["de", "us"], ["physics"],
  "Otto Stern developed the molecular beam method and discovered the quantization of angular momentum in atoms.",
  "Born in Sohrau, Upper Silesia. He studied physical chemistry and worked with Einstein and Born.",
  "His molecular beam experiments directly demonstrated space quantization and measured the proton's magnetic moment.",
  [(1922, "Performed the Stern-Gerlach experiment with Walther Gerlach"), (1943, "Awarded the Nobel Prize in Physics")],
  [("A Method for the Experimental Verification of Space Quantization", 1921, "Paper proposing the Stern-Gerlach experiment")],
  [("Thinking is easy, but experimenting takes time.", "Attributed")])

# ── POLITICAL / HISTORICAL ──

add("ramesses-ii", "Ramesses II", "ラムセス2世", -1303, -1213, ["eg"], ["politics"],
  "Ramesses II was the most powerful pharaoh of ancient Egypt, ruling for 66 years and building some of Egypt's greatest monuments.",
  "Born as the grandson of Ramesses I, founder of the 19th Dynasty. He was groomed for kingship from an early age.",
  "His monumental building projects, military campaigns, and the first known peace treaty shaped the ancient Near East.",
  [(-1274, "Fought the Battle of Kadesh against the Hittites"), (-1258, "Signed the Egyptian-Hittite peace treaty, the first known in history")],
  [("Abu Simbel Temples", -1244, "Massive rock-cut temples in Nubia commemorating his reign")],
  [("I am Ramesses, the Great King, the King of Kings.", "Inscription at Abu Simbel")])

add("nebuchadnezzar-ii", "Nebuchadnezzar II", "ネブカドネザル2世", -634, -562, ["iq"], ["politics"],
  "Nebuchadnezzar II was the greatest king of the Neo-Babylonian Empire, rebuilding Babylon into one of the ancient world's most magnificent cities.",
  "He was the eldest son of Nabopolassar, founder of the Neo-Babylonian dynasty, and proved himself as a military commander early.",
  "He transformed Babylon into a wonder of the ancient world and his conquest of Jerusalem profoundly shaped Jewish history.",
  [(-605, "Became king of Babylon"), (-586, "Destroyed the Temple in Jerusalem")],
  [("Ishtar Gate", -575, "Monumental gate to the city of Babylon decorated with glazed brick reliefs")],
  [("Is not this great Babylon, that I have built?", "Book of Daniel 4:30")])

add("darius-the-great", "Darius the Great", "ダレイオス1世", -550, -486, ["ir"], ["politics"],
  "Darius I was the third king of the Achaemenid Empire who reorganized it into the largest empire the world had yet seen.",
  "He seized the throne after overthrowing the usurper Gaumata and consolidated power through military campaigns.",
  "His administrative reforms, including the satrap system and the Royal Road, created a model for governing vast empires.",
  [(-522, "Became King of Persia"), (-490, "Launched the first Persian invasion of Greece, defeated at Marathon")],
  [("Behistun Inscription", -520, "Monumental rock relief and inscription recording his rise to power in three languages")],
  [("You know that I did not make myself king by deceit.", "Behistun Inscription")])

add("philip-ii-of-macedon", "Philip II of Macedon", "ピリッポス2世", -382, -336, ["gr"], ["politics"],
  "Philip II transformed Macedon from a weak kingdom into the dominant power of Greece, setting the stage for Alexander's conquests.",
  "Born in Pella, the youngest son of King Amyntas III. He spent years as a hostage in Thebes where he learned military tactics.",
  "His military reforms and diplomatic skill unified Greece under Macedonian hegemony, enabling Alexander's empire.",
  [(-338, "Defeated Athens and Thebes at the Battle of Chaeronea"), (-337, "Formed the League of Corinth")],
  [("Macedonian Phalanx", -350, "Revolutionary military formation using the sarissa pike")],
  [("My son, ask for thyself another kingdom, for that which I leave is too small for thee.", "Attributed by Plutarch")])

add("hannibal-barca", "Hannibal Barca", "ハンニバル・バルカ", -247, -183, ["tn"], ["politics"],
  "Hannibal Barca was Carthage's greatest general, famous for crossing the Alps with elephants and nearly conquering Rome.",
  "Born in Carthage, son of the general Hamilcar Barca. His father made him swear eternal enmity against Rome as a child.",
  "His tactical genius, especially at the Battle of Cannae, is studied in military academies to this day.",
  [(-218, "Crossed the Alps with his army and war elephants"), (-216, "Destroyed a Roman army at the Battle of Cannae")],
  [("Alpine Crossing", -218, "One of the most audacious military feats in history")],
  [("We will either find a way, or make one.", "Attributed by Livy")])

add("scipio-africanus", "Scipio Africanus", "スキピオ・アフリカヌス", -236, -183, ["it"], ["politics"],
  "Scipio Africanus was the Roman general who defeated Hannibal at the Battle of Zama, ending the Second Punic War.",
  "Born into the patrician Cornelii Scipiones family. He survived the disaster at Cannae as a young military tribune.",
  "His victory over Hannibal established Roman dominance in the Western Mediterranean and made Rome a superpower.",
  [(-209, "Captured New Carthage in Spain"), (-202, "Defeated Hannibal at the Battle of Zama")],
  [("Battle of Zama", -202, "Decisive victory ending the Second Punic War")],
  [("I am not the sort of general who does not know what needs to be done until he has been told.", "Attributed by Livy")])

add("trajan", "Trajan", "トラヤヌス", 53, 117, ["it", "es"], ["politics"],
  "Trajan was a Roman emperor who expanded the empire to its greatest territorial extent and was revered as the best of emperors.",
  "Born in Italica, Hispania. He rose through the military ranks and was adopted by Emperor Nerva as his successor.",
  "Under Trajan, the Roman Empire reached its maximum extent, and his public works program transformed Rome.",
  [(98, "Became Roman Emperor"), (113, "Completed Trajan's Column commemorating his Dacian Wars")],
  [("Trajan's Column", 113, "Monumental column in Rome with a spiral frieze depicting the Dacian Wars")],
  [("I wish to be the kind of emperor that I would have wished for if I were a subject.", "Attributed by Cassius Dio")])

add("justinian-i", "Justinian I", "ユスティニアヌス1世", 482, 565, ["gr"], ["politics"],
  "Justinian I was the Byzantine emperor who reconquered much of the former Western Roman Empire and codified Roman law.",
  "Born in Tauresium, Illyria, to a peasant family. His uncle Justin I adopted him and he rose to become co-emperor.",
  "The Corpus Juris Civilis became the foundation of civil law in most of Europe, and Hagia Sophia remains an architectural wonder.",
  [(527, "Became Byzantine Emperor"), (534, "Promulgated the Corpus Juris Civilis")],
  [("Corpus Juris Civilis", 534, "Comprehensive codification of Roman law that became the basis of European civil law")],
  [("Justice is the constant and perpetual wish to render to every one his due.", "Institutes of Justinian")])

add("alfred-the-great", "Alfred the Great", "アルフレッド大王", 849, 899, ["gb"], ["politics"],
  "Alfred the Great was King of Wessex who defended England against the Vikings and promoted learning and law.",
  "Born in Wantage, Berkshire, the youngest son of King Æthelwulf. He was educated in Rome as a child.",
  "He preserved Anglo-Saxon civilization from Viking conquest and established the foundations of a unified English kingdom.",
  [(878, "Defeated the Vikings at the Battle of Edington"), (886, "Captured London and was recognized as king of all English not under Viking rule")],
  [("Anglo-Saxon Chronicle", 890, "Historical record commissioned by Alfred documenting English history")],
  [("It is not right that anyone should be made rich by his own wrongdoing.", "Laws of Alfred")])

add("william-the-conqueror", "William the Conqueror", "ウィリアム征服王", 1028, 1087, ["fr", "gb"], ["politics"],
  "William the Conqueror was the Duke of Normandy who invaded England in 1066, fundamentally transforming English society and governance.",
  "Born in Falaise, Normandy, as the illegitimate son of Robert I, Duke of Normandy. He fought to secure his duchy from childhood.",
  "The Norman Conquest reshaped English language, law, culture, and social structure, linking England permanently to continental Europe.",
  [(1066, "Won the Battle of Hastings and was crowned King of England"), (1086, "Commissioned the Domesday Book")],
  [("Domesday Book", 1086, "Comprehensive survey of English landholdings, a remarkable administrative achievement")],
  [("By the splendour of God I have taken possession of my realm.", "Attributed, upon landing in England")])

add("frederick-ii-hre", "Frederick II, Holy Roman Emperor", "フリードリヒ2世", 1194, 1250, ["de", "it"], ["politics"],
  "Frederick II was a Holy Roman Emperor called Stupor Mundi (Wonder of the World) for his extraordinary learning and ambition.",
  "Born in Jesi, Italy, to Emperor Henry VI. Orphaned young, he grew up in multicultural Sicily.",
  "His court was a center of science and culture, and he founded the University of Naples, the first state university.",
  [(1220, "Crowned Holy Roman Emperor"), (1224, "Founded the University of Naples")],
  [("De Arte Venandi cum Avibus", 1248, "Treatise on falconry demonstrating scientific observation of nature")],
  [("Nothing is more dangerous than a friend without discretion; even a prudent enemy is preferable.", "Attributed")])

add("richard-the-lionheart", "Richard the Lionheart", "リチャード獅子心王", 1157, 1199, ["gb", "fr"], ["politics"],
  "Richard I of England was a warrior-king renowned for his military leadership during the Third Crusade.",
  "Born in Oxford, son of Henry II and Eleanor of Aquitaine. He was raised primarily in Aquitaine and fought in France.",
  "His exploits during the Third Crusade made him a legendary figure, though he spent little of his reign in England.",
  [(1189, "Crowned King of England"), (1191, "Captured Acre and defeated Saladin at the Battle of Arsuf")],
  [("Third Crusade", 1192, "Military campaign that secured a truce allowing Christian pilgrims access to Jerusalem")],
  [("I would sell London itself if I could find a buyer.", "Attributed by Roger of Howden")])

add("tamerlane", "Tamerlane", "ティムール", 1336, 1405, ["uz"], ["politics"],
  "Tamerlane was a Turco-Mongol conqueror who founded the Timurid Empire spanning from Turkey to India.",
  "Born near Kesh (modern Shahrisabz, Uzbekistan) into a minor Barlas noble family. He was injured in his youth, leaving him lame.",
  "His conquests reshaped Central Asia, and the Timurid Renaissance he sparked produced some of Islamic civilization's greatest achievements.",
  [(1370, "Established the Timurid Empire with Samarkand as its capital"), (1398, "Invaded and sacked Delhi")],
  [("Samarkand", 1400, "Transformed into one of the world's most magnificent cities under his rule")],
  [("As there is but one God in heaven, there ought to be but one ruler on the earth.", "Attributed")])

# ── ARTISTS, WRITERS, MUSICIANS ──

add("aesop", "Aesop", "アイソーポス", -620, -564, ["gr"], ["literature"],
  "Aesop was a legendary Greek fabulist credited with a collection of fables that have become a foundation of Western moral literature.",
  "According to tradition, he was a slave on the island of Samos who gained his freedom through his storytelling skill.",
  "Aesop's fables have been translated into virtually every language and remain among the most widely known stories in the world.",
  [(-550, "His fables were widely known throughout Greece"), (-564, "Reportedly killed by the citizens of Delphi")],
  [("Aesop's Fables", -550, "Collection of moral tales using animal characters to illustrate human virtues and vices")],
  [("Slow and steady wins the race.", "The Tortoise and the Hare")])

add("horace", "Horace", "ホラティウス", -65, -8, ["it"], ["literature"],
  "Horace was one of Rome's greatest lyric poets, whose Odes, Satires, and Epistles set standards for Western poetry.",
  "Born in Venusia to a freedman father who ensured his son received an excellent education in Rome and Athens.",
  "His poetry defined the principles of classical balance, moderation, and craftsmanship that influenced European literature for centuries.",
  [(-35, "Published his first book of Satires"), (-23, "Published the first three books of Odes")],
  [("Odes", -23, "Four books of lyric poems considered masterpieces of Latin verse")],
  [("Carpe diem, quam minimum credula postero.", "Odes I.11"), ("Sapere aude! — Dare to know!", "Epistles I.2")])

add("hafez", "Hafez", "ハーフェズ", 1315, 1390, ["ir"], ["literature"],
  "Hafez was the greatest Persian lyric poet, whose ghazals are memorized and recited throughout the Persian-speaking world.",
  "Born Shams-ud-Din Muhammad in Shiraz. He memorized the Quran as a child, earning the name Hafez (one who has memorized).",
  "His poetry synthesized mystical Sufi themes with earthly beauty, becoming the supreme expression of Persian literary art.",
  [(1368, "Became court poet under Shah Shuja"), (1390, "Died in Shiraz; his tomb became a national shrine")],
  [("Divan-e-Hafez", 1390, "Collection of approximately 500 ghazals on love, mysticism, and beauty")],
  [("I have learned so much from God that I can no longer call myself a Christian, a Hindu, a Muslim, a Buddhist, a Jew.", "Attributed")])

add("saadi", "Saadi Shirazi", "サアディー", 1210, 1291, ["ir"], ["literature"],
  "Saadi was a major Persian poet and prose writer whose works on practical ethics and love are among the finest in Persian literature.",
  "Born in Shiraz. He traveled for thirty years throughout the Islamic world, gathering experiences that informed his writings.",
  "His Gulistan and Bustan are among the most widely read works in Persian literature and influenced moral thought across the Islamic world.",
  [(1258, "Published the Bustan"), (1259, "Published the Gulistan")],
  [("Gulistan", 1259, "Prose and verse collection of moral stories and practical wisdom")],
  [("The children of Adam are limbs of one body, having been created of one essence.", "Gulistan")])

add("ferdowsi", "Ferdowsi", "フェルドウスィー", 940, 1020, ["ir"], ["literature"],
  "Ferdowsi was the author of the Shahnameh, the Persian national epic, which preserved Persian identity after the Arab conquest.",
  "Born in Tus, Khorasan, to a family of landed gentry. He spent over 30 years composing the Shahnameh.",
  "The Shahnameh preserved the Persian language and cultural identity, and remains the longest epic poem written by a single author.",
  [(977, "Began composing the Shahnameh"), (1010, "Completed the Shahnameh after over 30 years of work")],
  [("Shahnameh", 1010, "Epic poem of 50,000 couplets recounting the mythical and historical past of Persia")],
  [("I suffered much in these thirty years, but I have revived the Persians with the Persian language.", "Shahnameh")])

add("kalidasa", "Kalidasa", "カーリダーサ", 350, 450, ["in"], ["literature"],
  "Kalidasa was ancient India's greatest poet and dramatist, often called the Shakespeare of Sanskrit literature.",
  "Little is certain about his life. He likely lived during the Gupta period and may have been associated with the court of Chandragupta II.",
  "His plays and poems represent the pinnacle of Sanskrit literature and have been translated into numerous languages worldwide.",
  [(400, "Composed Shakuntala, his most famous play"), (410, "Wrote Meghaduta, a lyric masterpiece")],
  [("Abhijnanasakuntalam", 400, "Drama about the love of King Dushyanta and Shakuntala, praised by Goethe")],
  [("Listen to the Exordium of Creation.", "Attributed")])

add("valmiki", "Valmiki", "ヴァールミーキ", -500, -400, ["in"], ["literature"],
  "Valmiki is revered as the first poet of Sanskrit literature and the author of the Ramayana, one of India's two great epics.",
  "According to tradition, he was a reformed bandit who became a sage through meditation and composed the Ramayana through divine inspiration.",
  "The Ramayana has shaped Indian culture, religion, and morality for over two millennia and has been adapted across all of South and Southeast Asia.",
  [(-500, "Composed the Ramayana"), (-450, "The Ramayana became widely known across the Indian subcontinent")],
  [("Ramayana", -500, "Epic poem of 24,000 verses recounting the life and adventures of Prince Rama")],
  [("There is no sin greater than cruelty, and no virtue higher than compassion.", "Ramayana")])

add("jean-philippe-rameau", "Jean-Philippe Rameau", "ジャン＝フィリップ・ラモー", 1683, 1764, ["fr"], ["art"],
  "Rameau was a leading French composer and music theorist who dominated French opera and established modern harmonic theory.",
  "Born in Dijon to a family of musicians. He was largely self-taught and worked as an organist before turning to composition.",
  "His Treatise on Harmony laid the theoretical foundations of Western tonal music, and his operas revitalized French lyric drama.",
  [(1722, "Published Traité de l'harmonie"), (1733, "Premiered his first opera Hippolyte et Aricie")],
  [("Traité de l'harmonie", 1722, "Theoretical work establishing the foundations of modern harmonic analysis")],
  [("Music is a science which should have definite rules.", "Traité de l'harmonie")])

add("christoph-willibald-gluck", "Christoph Willibald Gluck", "クリストフ・ヴィリバルト・グルック", 1714, 1787, ["de", "at"], ["art"],
  "Gluck reformed opera by emphasizing dramatic expression over vocal display, paving the way for Mozart and Wagner.",
  "Born in Erasbach, Bavaria. He studied in Prague and Milan before becoming a prominent opera composer across Europe.",
  "His operatic reforms stripped away Baroque excess to serve the drama, fundamentally reshaping the art of opera.",
  [(1762, "Premiered Orfeo ed Euridice, the first reform opera"), (1774, "Premiered Iphigénie en Aulide in Paris")],
  [("Orfeo ed Euridice", 1762, "Opera that launched the reform of opera seria through dramatic simplicity")],
  [("Simplicity, truth, and naturalness are the great principles of beauty in all productions of art.", "Preface to Alceste")])

add("domenico-scarlatti", "Domenico Scarlatti", "ドメニコ・スカルラッティ", 1685, 1757, ["it", "es", "pt"], ["art"],
  "Domenico Scarlatti was an Italian composer who spent most of his career in Spain, famous for his 555 keyboard sonatas.",
  "Born in Naples, son of the composer Alessandro Scarlatti. He studied with his father and other Neapolitan masters.",
  "His keyboard sonatas expanded the technical and expressive possibilities of the harpsichord and influenced all subsequent keyboard music.",
  [(1720, "Moved to Portugal as music master to the Princess Maria Barbara"), (1738, "Published the Essercizi per gravicembalo, 30 keyboard sonatas")],
  [("Essercizi per gravicembalo", 1738, "Collection of 30 keyboard sonatas showcasing innovative technique")],
  [("Show me a musician who does not listen, and I will show you one who does not learn.", "Attributed")])

add("georg-philipp-telemann", "Georg Philipp Telemann", "ゲオルク・フィリップ・テレマン", 1681, 1767, ["de"], ["art"],
  "Telemann was the most prolific major composer in history, whose works bridged the late Baroque and early Classical styles.",
  "Born in Magdeburg to an upper-middle-class family. He was largely self-taught in music and studied law at Leipzig.",
  "His enormous output and stylistic versatility made him the most famous German composer of his time, surpassing even Bach in contemporary fame.",
  [(1721, "Appointed Kantor of the Johanneum and music director in Hamburg"), (1728, "Founded one of the first music magazines, Der getreue Music-Meister")],
  [("Tafelmusik", 1733, "Collection of orchestral suites, concertos, and chamber music for entertainment")],
  [("A proper musician should be able to set to music any text.", "Attributed")])

add("giotto", "Giotto di Bondone", "ジョット・ディ・ボンドーネ", 1267, 1337, ["it"], ["art"],
  "Giotto was the founder of the central tradition of Western painting, breaking from Byzantine formalism to depict natural human emotion.",
  "Born near Florence, possibly in Vespignano. According to legend, Cimabue discovered him drawing sheep on a rock.",
  "His naturalistic style revolutionized painting and laid the groundwork for the Italian Renaissance, earning him the title father of European painting.",
  [(1305, "Completed the Scrovegni Chapel frescoes in Padua"), (1334, "Appointed chief architect of Florence Cathedral")],
  [("Scrovegni Chapel Frescoes", 1305, "Cycle of frescoes depicting the lives of the Virgin and Christ with unprecedented emotional realism")],
  [("Every painting is a voyage into a sacred harbour.", "Attributed")])

add("jan-van-eyck", "Jan van Eyck", "ヤン・ファン・エイク", 1390, 1441, ["be"], ["art"],
  "Jan van Eyck was a Flemish painter who perfected the technique of oil painting, achieving unprecedented realism and luminosity.",
  "Born probably in Maaseik in the Prince-Bishopric of Liège. He served as court painter to Philip the Good of Burgundy.",
  "His mastery of oil painting technique and his astonishing realism transformed Northern European art and influenced painters for centuries.",
  [(1432, "Completed the Ghent Altarpiece"), (1434, "Painted the Arnolfini Portrait")],
  [("Ghent Altarpiece", 1432, "Monumental polyptych altarpiece considered a masterpiece of European art")],
  [("As I can.", "His motto, inscribed on his paintings — 'Als ik kan'")])

add("donatello", "Donatello", "ドナテッロ", 1386, 1466, ["it"], ["art"],
  "Donatello was the greatest sculptor of the early Renaissance, whose works revived classical forms with unprecedented naturalism.",
  "Born Donato di Niccolò di Betto Bardi in Florence. He trained in the workshop of Ghiberti and studied classical sculpture.",
  "His revolutionary approach to the human figure established sculpture as a major Renaissance art form independent of architecture.",
  [(1408, "Completed his marble David for Florence Cathedral"), (1440, "Created the bronze David, the first freestanding nude male sculpture since antiquity")],
  [("David", 1440, "Bronze sculpture that revived the classical nude and became a symbol of Florence")],
  [("If I had told the peasants what it was worth, they would have broken it.", "Attributed, regarding a work's value")])

add("filippo-brunelleschi", "Filippo Brunelleschi", "フィリッポ・ブルネレスキ", 1377, 1446, ["it"], ["engineering", "art"],
  "Brunelleschi was the founding father of Renaissance architecture who engineered the dome of Florence Cathedral, a feat deemed impossible.",
  "Born in Florence to a notary. He trained as a goldsmith and sculptor before turning to architecture and engineering.",
  "His dome remains the largest masonry dome ever built, and his discovery of linear perspective transformed Western art.",
  [(1420, "Began construction of the dome of Florence Cathedral"), (1436, "Completed the dome of Florence Cathedral")],
  [("Dome of Florence Cathedral", 1436, "Engineering marvel built without a supporting framework, still the largest masonry dome in the world")],
  [("Do not share your inventions with many, share them only with the few who understand.", "Attributed")])

add("leon-battista-alberti", "Leon Battista Alberti", "レオン・バッティスタ・アルベルティ", 1404, 1472, ["it"], ["art", "engineering"],
  "Alberti was the archetypal Renaissance man — an architect, artist, author, poet, and philosopher who codified the principles of Renaissance art.",
  "Born in Genoa to an exiled Florentine noble family. He studied law at Bologna and became a papal secretary in Rome.",
  "His treatises on painting, sculpture, and architecture established theoretical foundations for Renaissance art and influenced artists for centuries.",
  [(1435, "Wrote De Pictura, codifying the principles of perspective painting"), (1452, "Wrote De Re Aedificatoria, the first modern architectural treatise")],
  [("De Pictura", 1435, "Treatise on painting that systematized linear perspective for artists")],
  [("A man can do all things if he but wills them.", "De Iciarchia")])

add("pindar", "Pindar", "ピンダロス", -518, -438, ["gr"], ["literature"],
  "Pindar was the greatest lyric poet of ancient Greece, famous for his odes celebrating victors at the Panhellenic games.",
  "Born in Cynoscephalae, Boeotia, near Thebes. He studied poetry in Athens and achieved fame throughout the Greek world.",
  "His victory odes set the standard for choral lyric poetry and influenced Horace, the English Romantics, and modern poets.",
  [(-498, "Composed his earliest surviving ode"), (-476, "Wrote his most famous ode for Hieron of Syracuse")],
  [("Olympian Odes", -476, "Choral odes celebrating victors at the Olympic Games")],
  [("Water is best, and gold, like a blazing fire in the night, stands out supreme of all lordly wealth.", "Olympian Ode 1")])

add("catullus", "Catullus", "カトゥルス", -84, -54, ["it"], ["literature"],
  "Catullus was a Roman lyric poet whose passionate, personal verse influenced all subsequent Western love poetry.",
  "Born in Verona to a prominent family. He moved to Rome as a young man and became part of the literary elite.",
  "His intensely personal poems, especially those to Lesbia, pioneered the tradition of confessional love poetry in Western literature.",
  [(-60, "Composed his poems to Lesbia"), (-54, "Died young, probably around age 30")],
  [("Carmina", -54, "Collection of 116 poems ranging from tender love lyrics to savage invective")],
  [("Let us live and love, and value at a penny all the talk of stern old men.", "Carmen 5")])

add("xenophon", "Xenophon", "クセノポン", -430, -354, ["gr"], ["literature", "philosophy"],
  "Xenophon was an Athenian soldier, historian, and student of Socrates whose writings are major sources for Greek history and philosophy.",
  "Born in Athens to an equestrian family. He was a devoted follower of Socrates and served as a mercenary commander in Persia.",
  "His Anabasis became a model of military memoir, and his Socratic writings provide an essential counterpart to Plato's dialogues.",
  [(-401, "Led the retreat of the Ten Thousand Greek mercenaries from Persia"), (-370, "Wrote the Anabasis")],
  [("Anabasis", -370, "Account of the march of 10,000 Greek mercenaries into and out of the Persian Empire")],
  [("The sea! The sea!", "Anabasis, upon the Greeks sighting the Black Sea")])

add("juvenal", "Juvenal", "ユウェナリス", 55, 130, ["it"], ["literature"],
  "Juvenal was the greatest Roman satirical poet, whose biting verse attacked the vices and follies of Roman society.",
  "Born in Aquinum. Little is certain about his life; he may have served in the military and been exiled.",
  "His satires coined enduring phrases and established the tradition of savage indignation in Western satirical literature.",
  [(100, "Began publishing his Satires"), (127, "Published his final book of Satires")],
  [("Satires", 127, "Sixteen verse satires attacking corruption, decadence, and hypocrisy in Roman society")],
  [("Who watches the watchmen?", "Satires VI"), ("A healthy mind in a healthy body.", "Satires X")])

add("robert-burns", "Robert Burns", "ロバート・バーンズ", 1759, 1796, ["gb"], ["literature"],
  "Robert Burns was Scotland's national poet, whose works in Scots dialect celebrated common humanity and inspired Romantic poetry.",
  "Born in Alloway, Ayrshire, to a tenant farming family. He was largely self-educated and began writing verse as a teenager.",
  "His poems and songs became symbols of Scottish identity, and Auld Lang Syne is sung worldwide every New Year's Eve.",
  [(1786, "Published Poems, Chiefly in the Scottish Dialect"), (1788, "Began collecting and adapting Scottish folk songs")],
  [("Poems, Chiefly in the Scottish Dialect", 1786, "His first collection, known as the Kilmarnock edition")],
  [("The best-laid schemes o' mice an' men gang aft agley.", "To a Mouse")])

add("josquin-des-prez", "Josquin des Prez", "ジョスカン・デ・プレ", 1450, 1521, ["fr", "be"], ["art"],
  "Josquin des Prez was the greatest composer of the Renaissance, whose mastery of polyphony earned him comparison to Michelangelo.",
  "Born probably in the Vermandois region. He sang in Milan Cathedral and served at the papal chapel in Rome.",
  "His music synthesized the Franco-Flemish tradition with Italian expressiveness, setting the standard for Renaissance sacred and secular composition.",
  [(1489, "Joined the papal chapel in Rome"), (1503, "Appointed maestro di cappella at the court of Ferrara")],
  [("Missa Pange Lingua", 1515, "Mass considered one of the greatest achievements of Renaissance polyphony")],
  [("Josquin is the master of the notes; they must do as he wills.", "Martin Luther, attributed")])

add("william-byrd", "William Byrd", "ウィリアム・バード", 1543, 1623, ["gb"], ["art"],
  "William Byrd was the greatest English composer of the Renaissance, excelling in sacred music, consort songs, and keyboard works.",
  "Born probably in London. He was a pupil of Thomas Tallis and became organist at Lincoln Cathedral at age 20.",
  "His music represents the pinnacle of English Renaissance composition, and he maintained his Catholic faith despite persecution.",
  [(1575, "Granted a monopoly on music printing with Tallis by Elizabeth I"), (1605, "Published the first volume of Gradualia")],
  [("Gradualia", 1605, "Collection of Catholic liturgical music composed under conditions of religious persecution")],
  [("Since singing is so good a thing, I wish all men would learn to sing.", "Psalmes, Sonets and Songs, preface")])

add("cnr-rao", "C.N.R. Rao", "C・N・R・ラオ", 1934, None, ["in"], ["chemistry"],
  "C.N.R. Rao is one of the world's foremost solid-state and materials chemists, with pioneering work on transition metal oxides and nanomaterials.",
  "Born in Bangalore. He studied at Mysore University and earned his PhD from Purdue University.",
  "His research on materials chemistry has advanced understanding of superconductors, nanomaterials, and two-dimensional materials.",
  [(1963, "Published a landmark textbook on solid-state chemistry"), (2013, "Awarded India's highest civilian honor, the Bharat Ratna")],
  [("New Directions in Solid State Chemistry", 1986, "Influential textbook on modern solid-state chemistry")],
  [("Do science for the sake of science, not for awards.", "Attributed")])

add("ole-romer", "Ole Rømer", "オーレ・レーマー", 1644, 1710, ["dk"], ["astronomy", "physics"],
  "Ole Rømer made the first quantitative measurement of the speed of light by observing the moons of Jupiter.",
  "Born in Aarhus, Denmark. He studied at the University of Copenhagen and worked at the Paris Observatory.",
  "His measurement of the speed of light was one of the most important discoveries in the history of physics and astronomy.",
  [(1676, "Demonstrated that light has a finite speed"), (1681, "Returned to Denmark as Royal Mathematician and Astronomer")],
  [("Demonstration Concerning the Movement of Light", 1676, "Paper presenting the first measurement of the speed of light")],
  [("Light requires time to travel from place to place.", "Demonstration Concerning the Movement of Light")])

add("robert-brown-botanist", "Robert Brown", "ロバート・ブラウン", 1773, 1858, ["gb"], ["biology"],
  "Robert Brown was a Scottish botanist who discovered Brownian motion and identified the cell nucleus as a fundamental structure.",
  "Born in Montrose, Scotland. He studied medicine at Edinburgh and served as a naturalist on Matthew Flinders' voyage to Australia.",
  "His discovery of the cell nucleus and observation of Brownian motion had lasting impact on biology and physics respectively.",
  [(1827, "Observed Brownian motion under the microscope"), (1831, "Identified the cell nucleus in plant cells")],
  [("A Brief Account of Microscopical Observations", 1828, "Paper describing the random motion of particles suspended in fluid")],
  [("The particles were evidently not affected by any current in the fluid.", "A Brief Account of Microscopical Observations")])

add("christoph-scheiner", "Christoph Scheiner", "クリストフ・シャイナー", 1573, 1650, ["de"], ["astronomy"],
  "Christoph Scheiner was a Jesuit astronomer who independently discovered sunspots and made detailed studies of solar phenomena.",
  "Born in Markt Wald, Swabia. He entered the Jesuit order and studied mathematics and astronomy at the University of Ingolstadt.",
  "His systematic observations of sunspots contributed to the revolution in understanding the Sun as a changing, imperfect body.",
  [(1611, "Independently discovered sunspots"), (1630, "Published Rosa Ursina, a comprehensive study of sunspots")],
  [("Rosa Ursina", 1630, "Monumental work on solar observations containing over 70 illustrations of sunspot activity")],
  [("The Sun itself is not without blemish.", "Rosa Ursina")])

add("petronius", "Petronius", "ペトロニウス", 27, 66, ["it"], ["literature"],
  "Petronius was a Roman courtier and author of the Satyricon, one of the earliest and most vivid novels in Western literature.",
  "He was likely Gaius Petronius Arbiter, Nero's 'arbiter of elegance,' who oversaw the emperor's entertainments.",
  "The Satyricon's realistic portrayal of Roman life pioneered the novel form and influenced picaresque literature for centuries.",
  [(60, "Composed the Satyricon"), (66, "Forced to commit suicide by Nero")],
  [("Satyricon", 60, "Picaresque novel depicting the adventures of freedmen in the Roman underworld")],
  [("A man who is always ready to believe what is told him will never do well.", "Satyricon")])

if __name__ == "__main__":
    write_people(P)
