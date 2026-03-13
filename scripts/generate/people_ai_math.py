#!/usr/bin/env python3
"""Generate 100 mathematicians."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

p("euclid", "Euclid", "エウクレイデス", -325, -265, ["gr"], ["mathematics"],
  "Euclid was an ancient Greek mathematician often referred to as the father of geometry. His work Elements is one of the most influential texts in the history of mathematics.",
  "Little is known about Euclid's early life. He is believed to have studied at Plato's Academy in Athens before teaching mathematics in Alexandria, Egypt.",
  "Euclid's Elements served as the main textbook for teaching mathematics for over two thousand years. His axiomatic approach became the foundation of mathematical reasoning.",
  [(-300, "Published Elements in Alexandria"), (-280, "Established mathematical school in Alexandria")],
  [("Elements", -300, "A comprehensive compilation of Greek mathematics and geometry in 13 books")],
  [("The laws of nature are but the mathematical thoughts of God.", "Attributed")])

p("pythagoras", "Pythagoras", "ピタゴラス", -570, -495, ["gr"], ["mathematics", "philosophy"],
  "Pythagoras was an ancient Greek philosopher and mathematician, founder of the Pythagorean school. He is best known for the Pythagorean theorem relating the sides of a right triangle.",
  "Pythagoras was born on the island of Samos. He traveled widely, studying in Egypt and Babylon before founding his philosophical and mathematical school in Croton, southern Italy.",
  "Pythagoras established mathematics as a discipline of abstract reasoning. His ideas about numerical harmony influenced Western philosophy, music theory, and science for millennia.",
  [(-530, "Founded school in Croton"), (-520, "Developed theory of musical harmonics"), (-500, "Pythagorean theorem formalized")],
  [("Pythagorean Theorem", -520, "The fundamental relation in Euclidean geometry among the three sides of a right triangle")],
  [("Number is the ruler of forms and ideas.", "Attributed")])

p("leonhard-euler", "Leonhard Euler", "レオンハルト・オイラー", 1707, 1783, ["ch", "ru"], ["mathematics", "physics"],
  "Leonhard Euler was a Swiss mathematician and physicist who made fundamental contributions to almost every area of mathematics. He is one of the most prolific mathematicians in history.",
  "Euler was born in Basel, Switzerland. He studied under Johann Bernoulli at the University of Basel and showed extraordinary mathematical talent from an early age.",
  "Euler's contributions span calculus, graph theory, number theory, mechanics, and optics. His notation and terminology, including e, i, f(x), and sigma notation, remain standard today.",
  [(1727, "Joined the St. Petersburg Academy of Sciences"), (1736, "Solved the Seven Bridges of Königsberg problem"), (1748, "Published Introductio in analysin infinitorum"), (1766, "Returned to St. Petersburg, continued work despite blindness")],
  [("Introductio in analysin infinitorum", 1748, "A foundational text in mathematical analysis"), ("Mechanica", 1736, "Systematized Newtonian mechanics using analytical methods")],
  [("Read Euler, read Euler, he is the master of us all.", "Pierre-Simon Laplace")])

p("carl-friedrich-gauss", "Carl Friedrich Gauss", "カール・フリードリヒ・ガウス", 1777, 1855, ["de"], ["mathematics", "physics", "astronomy"],
  "Carl Friedrich Gauss was a German mathematician and physicist who made extraordinary contributions to number theory, algebra, statistics, analysis, and astronomy. He is often called the Prince of Mathematicians.",
  "Gauss was born in Brunswick to a poor family. A child prodigy, he reportedly summed integers from 1 to 100 instantly as a schoolboy. The Duke of Brunswick sponsored his education at the University of Göttingen.",
  "Gauss's work in number theory, differential geometry, and statistics shaped modern mathematics. The Gaussian distribution, Gauss's law, and the fundamental theorem of algebra bear his name.",
  [(1796, "Proved constructibility of the regular 17-gon"), (1799, "Proved the fundamental theorem of algebra"), (1801, "Published Disquisitiones Arithmeticae"), (1809, "Published Theoria Motus on celestial mechanics"), (1832, "Developed non-Euclidean geometry concepts")],
  [("Disquisitiones Arithmeticae", 1801, "A foundational work in number theory that shaped the field"), ("Theoria Motus", 1809, "Methods for determining orbits of celestial bodies")],
  [("Mathematics is the queen of the sciences and number theory is the queen of mathematics.", "Attributed")])

p("bernhard-riemann", "Bernhard Riemann", "ベルンハルト・リーマン", 1826, 1866, ["de"], ["mathematics"],
  "Bernhard Riemann was a German mathematician who made lasting contributions to analysis, number theory, and differential geometry. His work laid the mathematical foundation for general relativity.",
  "Riemann was born in Breselenz, Hanover. Shy and sickly as a child, he showed exceptional mathematical ability and studied under Gauss and Dirichlet at the University of Göttingen.",
  "Riemann's ideas on curved spaces became the basis for Einstein's general relativity. The Riemann hypothesis, concerning the distribution of prime numbers, remains one of the most important unsolved problems in mathematics.",
  [(1851, "Completed doctoral thesis on complex function theory"), (1854, "Delivered habilitation lecture on the foundations of geometry"), (1859, "Published paper on the distribution of primes containing the Riemann hypothesis")],
  [("On the Hypotheses Which Lie at the Foundations of Geometry", 1854, "Revolutionary lecture that introduced Riemannian geometry"), ("On the Number of Primes Less Than a Given Magnitude", 1859, "Introduced the Riemann zeta function and the famous hypothesis")],
  [("If only I had the theorems! Then I should find the proofs easily enough.", "Attributed")])

p("david-hilbert", "David Hilbert", "ダフィト・ヒルベルト", 1862, 1943, ["de"], ["mathematics"],
  "David Hilbert was a German mathematician and one of the most influential mathematicians of the 19th and 20th centuries. He formulated 23 unsolved problems that guided mathematical research for decades.",
  "Hilbert was born in Königsberg, Prussia. He studied at the University of Königsberg and became professor at the University of Göttingen, which he helped make a world center for mathematics.",
  "Hilbert's 23 problems shaped 20th-century mathematics. His work on invariant theory, algebraic number theory, functional analysis, and the foundations of geometry transformed multiple fields.",
  [(1897, "Published Zahlbericht on algebraic number theory"), (1899, "Published Foundations of Geometry"), (1900, "Presented 23 problems at the International Congress of Mathematicians"), (1926, "Work on foundations of mathematics and proof theory")],
  [("Foundations of Geometry", 1899, "A rigorous axiomatization of Euclidean geometry"), ("Mathematical Problems", 1900, "23 problems that shaped 20th-century mathematical research")],
  [("We must know. We will know.", "Radio address, 1930")])

p("srinivasa-ramanujan", "Srinivasa Ramanujan", "シュリニヴァーサ・ラマヌジャン", 1887, 1920, ["in", "gb"], ["mathematics"],
  "Srinivasa Ramanujan was an Indian mathematician who made extraordinary contributions to number theory, infinite series, and continued fractions, largely self-taught and working in isolation.",
  "Ramanujan was born in Erode, Tamil Nadu, India. With little formal training, he independently developed thousands of results. His talent was recognized after he wrote to G.H. Hardy at Cambridge.",
  "Ramanujan's intuitive genius produced results that mathematicians are still exploring today. His work on partition functions, mock theta functions, and infinite series opened new areas of research.",
  [(1904, "Began independent mathematical research"), (1913, "Wrote to G.H. Hardy at Cambridge"), (1914, "Traveled to Cambridge to work with Hardy"), (1918, "Elected Fellow of the Royal Society"), (1920, "Died in Kumbakonam at age 32")],
  [("Collected Papers", 1927, "Posthumous collection containing approximately 3,900 results"), ("Lost Notebook", 1976, "Discovered manuscript containing hundreds of new formulas")],
  [("An equation for me has no meaning unless it expresses a thought of God.", "Attributed")])

p("alan-turing", "Alan Turing", "アラン・チューリング", 1912, 1954, ["gb"], ["mathematics", "engineering"],
  "Alan Turing was a British mathematician and computer scientist who formalized the concepts of algorithm and computation with the Turing machine. He played a crucial role in breaking the Enigma code during World War II.",
  "Turing was born in London and showed early aptitude for science and mathematics. He studied at King's College, Cambridge, and later at Princeton University under Alonzo Church.",
  "Turing is considered the father of theoretical computer science and artificial intelligence. His work on computability, the Turing test, and code-breaking fundamentally shaped the modern world.",
  [(1936, "Published On Computable Numbers, introducing the Turing machine"), (1939, "Joined Bletchley Park to break German codes"), (1945, "Designed the Automatic Computing Engine"), (1950, "Published Computing Machinery and Intelligence, proposing the Turing test")],
  [("On Computable Numbers", 1936, "Introduced the concept of the Turing machine and proved limits of computation"), ("Computing Machinery and Intelligence", 1950, "Proposed the Turing test for machine intelligence")],
  [("We can only see a short distance ahead, but we can see plenty there that needs to be done.", "Computing Machinery and Intelligence, 1950")])

p("fibonacci", "Fibonacci", "フィボナッチ", 1170, 1250, ["it"], ["mathematics"],
  "Fibonacci, also known as Leonardo of Pisa, was an Italian mathematician who popularized the Hindu-Arabic numeral system in Europe and discovered the Fibonacci sequence.",
  "Fibonacci was born in Pisa and traveled extensively with his merchant father in North Africa, where he learned the Hindu-Arabic numeral system and Arab mathematical techniques.",
  "Fibonacci's Liber Abaci revolutionized European commerce and mathematics by introducing Hindu-Arabic numerals. The Fibonacci sequence appears throughout nature and remains central to mathematics.",
  [(1202, "Published Liber Abaci"), (1220, "Published Practica Geometriae"), (1225, "Published Liber Quadratorum")],
  [("Liber Abaci", 1202, "Introduced Hindu-Arabic numerals and the Fibonacci sequence to Europe"), ("Liber Quadratorum", 1225, "A study of Diophantine equations and number theory")],
  [("Without mathematics there is no art.", "Attributed")])

p("pierre-de-fermat", "Pierre de Fermat", "ピエール・ド・フェルマー", 1601, 1665, ["fr"], ["mathematics"],
  "Pierre de Fermat was a French mathematician who is considered one of the founders of modern number theory, analytic geometry, and probability theory.",
  "Fermat was born in Beaumont-de-Lomagne, France. A lawyer by profession, he pursued mathematics as an amateur, communicating his results through letters to other mathematicians.",
  "Fermat's Last Theorem, unsolved for 358 years until Andrew Wiles proved it in 1995, is one of the most famous problems in mathematics. His work co-founded probability theory with Pascal.",
  [(1629, "Developed methods of finding tangents and areas"), (1637, "Wrote his famous marginal note about Fermat's Last Theorem"), (1654, "Correspondence with Pascal founding probability theory")],
  [("Fermat's Last Theorem", 1637, "The conjecture that no three positive integers satisfy a^n + b^n = c^n for n > 2"), ("Adequality", 1629, "Method for finding maxima and minima, precursor to calculus")],
  [("I have discovered a truly marvelous proof of this, which this margin is too narrow to contain.", "Marginal note in Arithmetica, 1637")])

p("rene-descartes", "René Descartes", "ルネ・デカルト", 1596, 1650, ["fr", "nl"], ["mathematics", "philosophy"],
  "René Descartes was a French philosopher and mathematician who invented the Cartesian coordinate system, linking algebra and geometry. He is also considered the father of modern Western philosophy.",
  "Descartes was born in La Haye en Touraine, France. He was educated at the Jesuit college of La Flèche and later studied law at the University of Poitiers before devoting himself to philosophy and science.",
  "Descartes' coordinate system revolutionized mathematics by connecting algebra and geometry. His philosophical method of systematic doubt and his cogito ergo sum became foundations of modern philosophy.",
  [(1618, "Met Isaac Beeckman, inspiring his mathematical and scientific work"), (1628, "Began writing Rules for the Direction of the Mind"), (1637, "Published Discourse on the Method with La Géométrie"), (1641, "Published Meditations on First Philosophy"), (1649, "Moved to Stockholm at Queen Christina's invitation")],
  [("La Géométrie", 1637, "Founded analytic geometry by linking algebra and Euclidean geometry"), ("Discourse on the Method", 1637, "Introduced systematic doubt and the famous cogito ergo sum")],
  [("I think, therefore I am.", "Discourse on the Method, 1637")])

p("gottfried-wilhelm-leibniz", "Gottfried Wilhelm Leibniz", "ゴットフリート・ヴィルヘルム・ライプニッツ", 1646, 1716, ["de"], ["mathematics", "philosophy"],
  "Gottfried Wilhelm Leibniz was a German polymath who independently developed calculus and made major contributions to philosophy, logic, and mechanical calculation.",
  "Leibniz was born in Leipzig and was a child prodigy. He earned a doctorate in law and entered diplomatic service, while pursuing his mathematical and philosophical interests.",
  "Leibniz's notation for calculus became the standard used today. His philosophical works on monads and the principle of sufficient reason influenced Continental philosophy and formal logic.",
  [(1666, "Published De Arte Combinatoria"), (1673, "Built a mechanical calculator"), (1675, "Developed his version of calculus"), (1684, "Published first paper on differential calculus"), (1714, "Wrote Monadology")],
  [("Nova Methodus", 1684, "First published account of differential calculus with Leibniz notation"), ("Monadology", 1714, "Philosophical work describing the universe as composed of monads")],
  [("This is the best of all possible worlds.", "Théodicée, 1710")])

p("augustin-louis-cauchy", "Augustin-Louis Cauchy", "オーギュスタン＝ルイ・コーシー", 1789, 1857, ["fr"], ["mathematics"],
  "Augustin-Louis Cauchy was a French mathematician who pioneered rigorous foundations of calculus and made fundamental contributions to complex analysis and group theory.",
  "Cauchy was born in Paris during the French Revolution. He studied at the École Polytechnique and the École des Ponts et Chaussées, initially training as a civil engineer.",
  "Cauchy's rigorous approach to analysis established the modern foundations of calculus. His theorems in complex analysis, including Cauchy's integral theorem, remain fundamental to mathematics.",
  [(1814, "Submitted memoir on definite integrals to the French Academy"), (1821, "Published Cours d'analyse"), (1825, "Developed Cauchy integral theorem"), (1829, "Published Leçons sur le calcul différentiel")],
  [("Cours d'analyse", 1821, "Rigorous foundations for calculus and real analysis"), ("Mémoire sur les intégrales définies", 1827, "Foundation of complex function theory")],
  [("One must study them all, for none among them is without some truth.", "On mathematical methods")])

p("niels-henrik-abel", "Niels Henrik Abel", "ニールス・ヘンリック・アーベル", 1802, 1829, ["no"], ["mathematics"],
  "Niels Henrik Abel was a Norwegian mathematician who proved the impossibility of solving the general quintic equation algebraically and made groundbreaking contributions to elliptic functions.",
  "Abel was born in Nedstrand, Norway, to a poor family. His mathematical talent was recognized by his teacher Bernt Michael Holmboe, who supported his studies.",
  "Abel's proof of the unsolvability of the quintic equation was a landmark in algebra. His work on elliptic functions and Abelian integrals opened vast new areas of mathematics. He died of tuberculosis at 26.",
  [(1824, "Proved impossibility of solving the general quintic"), (1826, "Published work on elliptic functions"), (1828, "Published memoir on a general property of a class of transcendental functions")],
  [("Proof of the Impossibility of Algebraic Solution of General Equations", 1824, "Demonstrated that no general algebraic solution exists for polynomials of degree five or higher")],
  [("He has left mathematicians something to keep them busy for five hundred years.", "Charles Hermite, on Abel")])

p("evariste-galois", "Évariste Galois", "エヴァリスト・ガロア", 1811, 1832, ["fr"], ["mathematics"],
  "Évariste Galois was a French mathematician who founded group theory and Galois theory, establishing conditions under which polynomial equations can be solved. He died in a duel at age 20.",
  "Galois was born near Paris. A brilliant but troubled student, he was twice rejected by the École Polytechnique. He became involved in republican politics during a turbulent period in French history.",
  "Galois theory, developed from his manuscripts written the night before his fatal duel, fundamentally connects field theory and group theory. It provides the definitive answer to which polynomial equations are solvable by radicals.",
  [(1829, "Published first paper on continued fractions"), (1830, "Submitted memoirs to the French Academy, lost by Cauchy and Fourier"), (1831, "Arrested for political activities"), (1832, "Wrote mathematical testament the night before fatal duel")],
  [("Mémoire sur les conditions de résolubilité des équations par radicaux", 1831, "Foundational work establishing Galois theory and group theory")],
  [("I have not time. I have not time.", "Written the night before his death, 1832")])

p("georg-cantor", "Georg Cantor", "ゲオルク・カントール", 1845, 1918, ["de", "ru"], ["mathematics"],
  "Georg Cantor was a German mathematician who created set theory and established the concept of infinite numbers. His work proved that infinities come in different sizes.",
  "Cantor was born in St. Petersburg, Russia, to a German family and grew up in Germany. He studied at the University of Berlin under Weierstrass, Kummer, and Kronecker.",
  "Cantor's set theory became a fundamental part of modern mathematics. His proof that real numbers are uncountable and his theory of transfinite numbers revolutionized our understanding of infinity.",
  [(1874, "Published first paper on set theory"), (1878, "Proved the real line and n-dimensional space have equal cardinality"), (1883, "Published Grundlagen einer allgemeinen Mannigfaltigkeitslehre"), (1891, "Published the diagonal argument")],
  [("Grundlagen einer allgemeinen Mannigfaltigkeitslehre", 1883, "Foundations of set theory and transfinite numbers"), ("Diagonal Argument", 1891, "Proof that real numbers are uncountable")],
  [("The essence of mathematics lies in its freedom.", "Grundlagen, 1883")])

p("kurt-godel", "Kurt Gödel", "クルト・ゲーデル", 1906, 1978, ["at", "us"], ["mathematics", "philosophy"],
  "Kurt Gödel was an Austrian-American logician and mathematician who proved the incompleteness theorems, demonstrating fundamental limitations of formal mathematical systems.",
  "Gödel was born in Brünn, Austria-Hungary. He studied at the University of Vienna and became part of the Vienna Circle before emigrating to the United States in 1940.",
  "Gödel's incompleteness theorems are among the most important results in mathematical logic. They showed that any consistent formal system powerful enough to describe arithmetic contains true statements that cannot be proved within the system.",
  [(1931, "Published the incompleteness theorems"), (1940, "Emigrated to the United States, joined the Institute for Advanced Study"), (1949, "Discovered rotating universe solutions to Einstein's field equations")],
  [("On Formally Undecidable Propositions", 1931, "Proved that consistent mathematical systems contain true but unprovable statements")],
  [("Either mathematics is too big for the human mind, or the human mind is more than a machine.", "Attributed")])

p("john-von-neumann", "John von Neumann", "ジョン・フォン・ノイマン", 1903, 1957, ["hu", "us"], ["mathematics", "physics", "engineering"],
  "John von Neumann was a Hungarian-American mathematician who made major contributions to quantum mechanics, game theory, computer science, and nuclear physics. He was one of the greatest mathematicians of the 20th century.",
  "Von Neumann was born in Budapest to a wealthy Jewish family. A child prodigy, he could divide eight-digit numbers in his head by age six and mastered calculus by age eight.",
  "Von Neumann's contributions span an extraordinary range: the mathematical foundations of quantum mechanics, game theory, the von Neumann architecture for computers, and the development of nuclear weapons at Los Alamos.",
  [(1928, "Published minimax theorem founding game theory"), (1932, "Published Mathematical Foundations of Quantum Mechanics"), (1943, "Joined the Manhattan Project at Los Alamos"), (1945, "Described stored-program computer architecture"), (1944, "Published Theory of Games and Economic Behavior with Morgenstern")],
  [("Mathematical Foundations of Quantum Mechanics", 1932, "Rigorous mathematical framework for quantum mechanics"), ("Theory of Games and Economic Behavior", 1944, "Founded game theory as a mathematical discipline")],
  [("If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.", "Attributed")])

p("henri-poincare", "Henri Poincaré", "アンリ・ポアンカレ", 1854, 1912, ["fr"], ["mathematics", "physics"],
  "Henri Poincaré was a French mathematician, physicist, and philosopher of science who made fundamental contributions to topology, celestial mechanics, and the theory of dynamical systems.",
  "Poincaré was born in Nancy, France, to a prominent family. He showed mathematical genius early and studied at the École Polytechnique and the École des Mines.",
  "Poincaré is considered the last universalist in mathematics. He founded algebraic topology, contributed to the three-body problem, and anticipated aspects of special relativity and chaos theory.",
  [(1881, "Developed qualitative theory of differential equations"), (1895, "Published Analysis Situs, founding algebraic topology"), (1899, "Published Les Méthodes nouvelles de la mécanique céleste"), (1904, "Formulated the Poincaré conjecture"), (1905, "Published on the dynamics of the electron, anticipating relativity")],
  [("Analysis Situs", 1895, "Founded the field of algebraic topology"), ("Les Méthodes nouvelles de la mécanique céleste", 1892, "Revolutionary work on celestial mechanics and dynamical systems")],
  [("Mathematics is the art of giving the same name to different things.", "Science and Method, 1908")])

p("andrey-kolmogorov", "Andrey Kolmogorov", "アンドレイ・コルモゴロフ", 1903, 1987, ["ru"], ["mathematics"],
  "Andrey Kolmogorov was a Soviet mathematician who made fundamental contributions to probability theory, topology, turbulence, and algorithmic complexity.",
  "Kolmogorov was born in Tambov, Russia. Raised by his aunts, he entered Moscow State University at 17 and quickly demonstrated extraordinary mathematical talent.",
  "Kolmogorov's axiomatization of probability theory in 1933 established it as a rigorous branch of mathematics. His contributions to turbulence theory, complexity theory, and dynamical systems remain foundational.",
  [(1925, "Published first results on intuitionistic logic"), (1933, "Published Foundations of the Theory of Probability"), (1941, "Published theory of turbulence"), (1957, "Proved the KAM theorem with Arnold and Moser"), (1965, "Founded algorithmic complexity theory")],
  [("Foundations of the Theory of Probability", 1933, "Axiomatic foundation for probability theory using measure theory")],
  [("Every mathematician believes he is ahead over all others. The reason none of them state this publicly is because they are intelligent people.", "Attributed")])

p("paul-erdos", "Paul Erdős", "ポール・エルデシュ", 1913, 1996, ["hu"], ["mathematics"],
  "Paul Erdős was a Hungarian mathematician who was one of the most prolific mathematicians in history, publishing about 1,500 papers. He is known for his work in combinatorics, graph theory, and number theory.",
  "Erdős was born in Budapest to Jewish parents who were both mathematics teachers. A child prodigy, he proved Chebyshev's theorem at age 19.",
  "Erdős pioneered the fields of discrete mathematics, graph theory, and probabilistic number theory. The Erdős number, measuring collaborative distance, reflects his extraordinary network of over 500 co-authors.",
  [(1934, "Moved to Manchester after receiving his doctorate"), (1949, "Gave an elementary proof of the prime number theorem"), (1959, "Founded the probabilistic method in combinatorics"), (1983, "Won the Wolf Prize in Mathematics")],
  [("Probabilistic Method", 1947, "Revolutionary technique using probability to prove existence of mathematical structures")],
  [("A mathematician is a device for turning coffee into theorems.", "Attributed")])

p("alexander-grothendieck", "Alexander Grothendieck", "アレクサンドル・グロタンディーク", 1928, 2014, ["de", "fr"], ["mathematics"],
  "Alexander Grothendieck was a German-born French mathematician who revolutionized algebraic geometry and is considered one of the greatest mathematicians of the 20th century.",
  "Grothendieck was born in Berlin and had a tumultuous childhood during World War II. Stateless for much of his life, he studied in Montpellier before moving to Paris.",
  "Grothendieck's reconstruction of algebraic geometry through scheme theory transformed the field. His work on sheaves, cohomology, and topos theory profoundly influenced modern mathematics.",
  [(1957, "Published Tohoku paper revolutionizing homological algebra"), (1960, "Began writing Éléments de géométrie algébrique"), (1966, "Awarded Fields Medal but refused to attend ceremony in Moscow"), (1970, "Left IHÉS over military funding issues"), (1991, "Withdrew from mathematical community")],
  [("Éléments de géométrie algébrique", 1960, "Monumental work reconstructing the foundations of algebraic geometry")],
  [("The introduction of the cipher 0 or the group concept was general nonsense too, and mathematics was more or less stagnating for thousands of years because nobody was around to take such childish steps.", "Récoltes et Semailles")])

p("hypatia", "Hypatia", "ヒュパティア", 360, 415, ["eg"], ["mathematics", "philosophy"],
  "Hypatia of Alexandria was a Greek mathematician, astronomer, and philosopher. She is the first female mathematician whose life and work are reasonably well recorded.",
  "Hypatia was born in Alexandria, Egypt, daughter of the mathematician Theon. She was educated by her father and became head of the Neoplatonist school in Alexandria.",
  "Hypatia was a symbol of learning and science in late antiquity. Her murder by a Christian mob in 415 AD has made her an enduring symbol of intellectual freedom and the destruction of classical knowledge.",
  [(380, "Began teaching mathematics and philosophy in Alexandria"), (400, "Became head of the Neoplatonist school"), (415, "Murdered by a mob in Alexandria")],
  [("Commentary on Diophantus's Arithmetica", 400, "Expanded and clarified Diophantus's work on algebra"), ("Commentary on Apollonius's Conics", 400, "Made Apollonius's work on conic sections more accessible")],
  [("Reserve your right to think, for even to think wrongly is better than not to think at all.", "Attributed")])

p("ada-lovelace", "Ada Lovelace", "エイダ・ラブレス", 1815, 1852, ["gb"], ["mathematics", "engineering"],
  "Ada Lovelace was a British mathematician and writer, recognized as the first computer programmer for her work on Charles Babbage's Analytical Engine.",
  "Ada was born in London, the daughter of poet Lord Byron. Her mother promoted her study of mathematics and logic to counter any inheritance of her father's poetic temperament.",
  "Lovelace's notes on the Analytical Engine contain what is recognized as the first algorithm intended for machine processing. Her vision of computers going beyond mere calculation anticipated modern computing by a century.",
  [(1833, "Met Charles Babbage and saw his Difference Engine"), (1842, "Translated Luigi Menabrea's article on the Analytical Engine"), (1843, "Published her Notes, containing the first computer algorithm")],
  [("Notes on the Analytical Engine", 1843, "Contained the first published computer algorithm and visionary ideas about computing's potential")],
  [("The Analytical Engine weaves algebraic patterns just as the Jacquard loom weaves flowers and leaves.", "Notes on the Analytical Engine, 1843")])

p("sophie-germain", "Sophie Germain", "ソフィー・ジェルマン", 1776, 1831, ["fr"], ["mathematics", "physics"],
  "Sophie Germain was a French mathematician who made important contributions to number theory and elasticity theory, working in an era when women were excluded from formal scientific education.",
  "Germain was born in Paris. Fascinated by mathematics after reading about Archimedes, she taught herself from books in her father's library and corresponded with leading mathematicians under a male pseudonym.",
  "Germain's work on Fermat's Last Theorem was groundbreaking, proving a special case. Her theory of elastic surfaces won a prize from the French Academy of Sciences and influenced engineering.",
  [(1794, "Began corresponding with Lagrange under male pseudonym"), (1804, "Began correspondence with Gauss on number theory"), (1816, "Won the French Academy prize for theory of elasticity"), (1831, "Published work on mean curvature of surfaces")],
  [("Memoir on the Vibrations of Elastic Plates", 1816, "Prize-winning work on the mathematical theory of elasticity")],
  [("Algebra is but written geometry and geometry is but figured algebra.", "Attributed")])

p("maryam-mirzakhani", "Maryam Mirzakhani", "マリアム・ミルザハニ", 1977, 2017, ["ir", "us"], ["mathematics"],
  "Maryam Mirzakhani was an Iranian mathematician and the first woman to win the Fields Medal. Her work focused on the geometry and dynamics of Riemann surfaces.",
  "Mirzakhani was born in Tehran, Iran. She won gold medals at the International Mathematical Olympiad in 1994 and 1995, achieving a perfect score in 1995.",
  "Mirzakhani's Fields Medal in 2014 broke a historic barrier. Her work on moduli spaces of Riemann surfaces and their dynamics opened new connections between topology, geometry, and dynamical systems.",
  [(1999, "Graduated from Sharif University of Technology"), (2004, "Earned PhD from Harvard under Curtis McMullen"), (2008, "Became professor at Stanford University"), (2014, "Awarded the Fields Medal, the first woman to receive it"), (2017, "Died of breast cancer at age 40")],
  [("Simple Geodesics and Weil-Petersson Volumes of Moduli Spaces", 2007, "Groundbreaking work on counting simple closed geodesics on hyperbolic surfaces")],
  [("The beauty of mathematics only shows itself to more patient followers.", "Stanford University interview")])

p("terence-tao", "Terence Tao", "テレンス・タオ", 1975, None, ["au", "us"], ["mathematics"],
  "Terence Tao is an Australian-American mathematician widely regarded as one of the greatest living mathematicians. He has made contributions to harmonic analysis, partial differential equations, combinatorics, and number theory.",
  "Tao was born in Adelaide, Australia, to parents of Chinese descent. A child prodigy, he began taking university-level courses at age nine and earned his PhD from Princeton at 21.",
  "Tao's work spans an extraordinary range of mathematics. His proof with Ben Green that the primes contain arbitrarily long arithmetic progressions was a landmark result. He received the Fields Medal in 2006.",
  [(1992, "Won gold medal at IMO at age 16, the youngest ever"), (1996, "Earned PhD from Princeton University"), (2004, "Proved the Green-Tao theorem on primes in arithmetic progressions"), (2006, "Awarded the Fields Medal"), (2015, "Proved the Erdős discrepancy problem")],
  [("Green-Tao Theorem", 2004, "Proved that the set of prime numbers contains arbitrarily long arithmetic progressions")],
  [("It is not so much whether you are talented or not, but whether you work hard or not.", "UCLA lecture")])

p("andrew-wiles", "Andrew Wiles", "アンドリュー・ワイルズ", 1953, None, ["gb", "us"], ["mathematics"],
  "Andrew Wiles is a British mathematician who proved Fermat's Last Theorem in 1995, solving a problem that had been open for 358 years.",
  "Wiles was born in Cambridge, England. He became fascinated with Fermat's Last Theorem at age 10 after reading about it in a library book, and dedicated much of his career to solving it.",
  "Wiles's proof of Fermat's Last Theorem is one of the greatest achievements in the history of mathematics. His work connected modular forms and elliptic curves, opening new areas of number theory.",
  [(1974, "Earned PhD from Cambridge"), (1982, "Became professor at Princeton"), (1993, "Announced proof of Fermat's Last Theorem"), (1995, "Published corrected proof with Richard Taylor"), (2016, "Awarded the Abel Prize")],
  [("Modular Elliptic Curves and Fermat's Last Theorem", 1995, "Proved the modularity theorem for semistable elliptic curves, implying Fermat's Last Theorem")],
  [("I had this rare privilege of being able to pursue in my adult life what had been my childhood dream.", "PBS interview, 2000")])

p("pierre-simon-laplace", "Pierre-Simon Laplace", "ピエール＝シモン・ラプラス", 1749, 1827, ["fr"], ["mathematics", "physics", "astronomy"],
  "Pierre-Simon Laplace was a French mathematician and astronomer who made fundamental contributions to probability theory, celestial mechanics, and mathematical physics.",
  "Laplace was born in Beaumont-en-Auge, Normandy. His mathematical talent was recognized early and he moved to Paris, where he gained the patronage of d'Alembert.",
  "Laplace's Mécanique céleste synthesized the work of Newton and his successors into a complete theory of planetary motion. His work on probability theory laid the foundations for statistical inference.",
  [(1773, "Began work on celestial mechanics"), (1796, "Published Exposition du système du monde"), (1799, "Published first volume of Mécanique céleste"), (1812, "Published Théorie analytique des probabilités")],
  [("Mécanique céleste", 1799, "Comprehensive work on celestial mechanics synthesizing gravitational theory"), ("Théorie analytique des probabilités", 1812, "Foundation of modern probability theory")],
  [("I had no need of that hypothesis.", "Reply to Napoleon about God's role in his system")])

p("joseph-louis-lagrange", "Joseph-Louis Lagrange", "ジョゼフ＝ルイ・ラグランジュ", 1736, 1813, ["it", "fr"], ["mathematics", "physics"],
  "Joseph-Louis Lagrange was an Italian-French mathematician who made major contributions to number theory, analysis, and both classical and celestial mechanics.",
  "Lagrange was born in Turin, Sardinia. He became professor of mathematics at the Royal Artillery School in Turin at age 19 and later succeeded Euler at the Berlin Academy.",
  "Lagrange's reformulation of classical mechanics, his work on the calculus of variations, and Lagrange's theorem in group theory remain fundamental to mathematics and physics.",
  [(1755, "Appointed professor at Turin at age 19"), (1766, "Succeeded Euler at the Berlin Academy"), (1788, "Published Mécanique analytique"), (1797, "Published Théorie des fonctions analytiques")],
  [("Mécanique analytique", 1788, "Reformulated classical mechanics using purely analytical methods without diagrams"), ("Théorie des fonctions analytiques", 1797, "Attempted to put calculus on a rigorous algebraic foundation")],
  [("When we ask advice, we are usually looking for an accomplice.", "Attributed")])

p("jacob-bernoulli", "Jacob Bernoulli", "ヤコブ・ベルヌーイ", 1655, 1705, ["ch"], ["mathematics"],
  "Jacob Bernoulli was a Swiss mathematician and one of the founders of probability theory and the calculus of variations. He was the first of the prominent Bernoulli family of mathematicians.",
  "Bernoulli was born in Basel, Switzerland. Against his father's wishes for him to study theology, he pursued mathematics and astronomy, eventually becoming professor of mathematics at the University of Basel.",
  "Bernoulli's Ars Conjectandi, published posthumously, laid the foundations of probability theory. His discovery of the constant e and work on the calculus of variations influenced mathematics profoundly.",
  [(1687, "Published early work on probability"), (1690, "Coined the term integral"), (1695, "Solved the brachistochrone problem"), (1705, "Ars Conjectandi published posthumously in 1713")],
  [("Ars Conjectandi", 1713, "Foundational work in probability theory including the law of large numbers")],
  [("I recognize the lion by his claw.", "On reading an anonymous solution by Newton")])

p("nikolai-lobachevsky", "Nikolai Lobachevsky", "ニコライ・ロバチェフスキー", 1792, 1856, ["ru"], ["mathematics"],
  "Nikolai Lobachevsky was a Russian mathematician who independently developed non-Euclidean geometry, replacing Euclid's parallel postulate with an alternative axiom.",
  "Lobachevsky was born in Nizhny Novgorod. He studied at Kazan University and became its rector, while pursuing his revolutionary work on geometry.",
  "Lobachevsky's non-Euclidean geometry, initially met with skepticism, fundamentally changed the understanding of geometry and paved the way for Riemannian geometry and general relativity.",
  [(1826, "Presented first paper on non-Euclidean geometry"), (1829, "Published On the Principles of Geometry"), (1840, "Published Geometrical Researches on the Theory of Parallels")],
  [("On the Principles of Geometry", 1829, "First published work systematically developing hyperbolic geometry")],
  [("There is no branch of mathematics, however abstract, which may not some day be applied to phenomena of the real world.", "Attributed")])

p("emile-borel", "Émile Borel", "エミール・ボレル", 1871, 1956, ["fr"], ["mathematics"],
  "Émile Borel was a French mathematician who made important contributions to measure theory, probability, and game theory. He was a pioneer of modern probability theory.",
  "Borel was born in Saint-Affrique, France. He entered the École Normale Supérieure at age 18 and became one of the youngest professors at the Sorbonne.",
  "Borel's work on measure theory and the Borel sets provided essential foundations for modern analysis and probability. He also anticipated key ideas in game theory before von Neumann.",
  [(1894, "Published thesis on entire functions"), (1898, "Published Leçons sur la théorie des fonctions"), (1909, "Published work on the normal number theorem"), (1921, "Entered politics, served in French parliament")],
  [("Leçons sur la théorie des fonctions", 1898, "Introduced the concept of Borel sets and countable additivity")],
  [("The practical value of probability theory is considerable.", "Le Hasard, 1914")])

p("jean-pierre-serre", "Jean-Pierre Serre", "ジャン＝ピエール・セール", 1926, None, ["fr"], ["mathematics"],
  "Jean-Pierre Serre is a French mathematician who has made fundamental contributions to algebraic topology, algebraic geometry, and number theory. He is one of the youngest Fields Medal winners.",
  "Serre was born in Bages, France. He studied at the École Normale Supérieure and earned his doctorate under Henri Cartan at age 25.",
  "Serre's contributions bridge algebraic topology, algebraic geometry, and number theory. He won the Fields Medal at 27 and the Abel Prize at 77, the first person to receive both awards.",
  [(1954, "Awarded the Fields Medal at age 27"), (1956, "Published seminal paper on algebraic geometry GAGA"), (1962, "Published Cours d'arithmétique"), (2003, "Awarded the inaugural Abel Prize")],
  [("Faisceaux algébriques cohérents", 1955, "Foundational work applying sheaf theory to algebraic geometry"), ("Cours d'arithmétique", 1962, "Influential textbook on number theory")],
  [("Mathematics is not a spectator sport.", "Attributed")])

p("emmy-noether-math", "Emmy Noether", "エミー・ネーター", 1882, 1935, ["de", "us"], ["mathematics"],
  "Emmy Noether was a German mathematician who made groundbreaking contributions to abstract algebra and theoretical physics. Noether's theorem connects symmetries and conservation laws.",
  "Noether was born in Erlangen, Germany. Despite barriers against women in academia, she earned her doctorate and eventually lectured at the University of Göttingen, though initially without pay.",
  "Noether is considered the mother of modern algebra. Her work on ring theory, ideals, and Noether's theorem transformed abstract algebra and theoretical physics. Einstein called her the most important woman in the history of mathematics.",
  [(1907, "Earned doctorate from the University of Erlangen"), (1915, "Proved Noether's theorem connecting symmetries to conservation laws"), (1921, "Published Idealtheorie in Ringbereichen"), (1933, "Fled Nazi Germany to Bryn Mawr College in the US")],
  [("Noether's Theorem", 1915, "Proved the fundamental connection between symmetries and conservation laws in physics"), ("Idealtheorie in Ringbereichen", 1921, "Foundational paper in commutative algebra")],
  [("My methods are really methods of working and thinking; this is why they have crept in everywhere anonymously.", "Attributed")])

p("brahmagupta", "Brahmagupta", "ブラフマグプタ", 598, 668, ["in"], ["mathematics", "astronomy"],
  "Brahmagupta was an Indian mathematician and astronomer who was the first to formalize arithmetic rules for zero and negative numbers and made major contributions to algebra.",
  "Brahmagupta was born in Bhinmal, Rajasthan, India. He became the head of the astronomical observatory at Ujjain, the foremost mathematical center of ancient India.",
  "Brahmagupta's rules for arithmetic with zero and negative numbers were revolutionary. His formula for the area of cyclic quadrilaterals and work on Pell's equation influenced mathematics worldwide.",
  [(628, "Published Brahmasphutasiddhanta"), (665, "Published Khandakhadyaka on astronomy")],
  [("Brahmasphutasiddhanta", 628, "Major treatise establishing rules for zero, negative numbers, and algebra")],
  [("As the sun eclipses the stars by its brilliancy, so the man of knowledge will eclipse the fame of others.", "Brahmasphutasiddhanta")])

p("muhammad-al-khwarizmi", "Muhammad al-Khwarizmi", "フワーリズミー", 780, 850, ["iq"], ["mathematics", "astronomy"],
  "Muhammad al-Khwarizmi was a Persian mathematician whose works introduced Hindu-Arabic numerals and algebra to the Western world. The word 'algorithm' derives from his name.",
  "Al-Khwarizmi was born in Khwarezm, in present-day Uzbekistan. He worked at the House of Wisdom in Baghdad, the leading intellectual center of the Islamic Golden Age.",
  "Al-Khwarizmi's algebra textbook created a new mathematical discipline and his work on Hindu-Arabic numerals revolutionized mathematics. The words 'algebra' and 'algorithm' both derive from his work and name.",
  [(820, "Published The Compendious Book on Calculation by Completion and Balancing"), (825, "Published work on Hindu-Arabic numerals"), (830, "Published astronomical tables")],
  [("The Compendious Book on Calculation by Completion and Balancing", 820, "Founded algebra as an independent mathematical discipline")],
  [("When I consider what people generally want in calculating, I found that it always is a number.", "Al-Jabr, 820")])

p("omar-khayyam-math", "Omar Khayyam", "ウマル・ハイヤーム", 1048, 1131, ["ir"], ["mathematics", "astronomy", "literature"],
  "Omar Khayyam was a Persian polymath who made important contributions to algebra, geometry, and astronomy, and is also celebrated as a poet for his Rubaiyat.",
  "Khayyam was born in Nishapur, Persia. He studied under leading scholars and became renowned for his mathematical and astronomical abilities.",
  "Khayyam classified and solved cubic equations geometrically, reformed the Persian calendar to remarkable accuracy, and challenged Euclid's parallel postulate centuries before non-Euclidean geometry.",
  [(1070, "Wrote Treatise on Demonstration of Problems of Algebra"), (1079, "Led reform of the Persian calendar"), (1077, "Wrote Commentary on Euclid's Elements")],
  [("Treatise on Demonstration of Problems of Algebra", 1070, "Classified and solved cubic equations using conic section intersections")],
  [("Be happy for this moment. This moment is your life.", "Rubaiyat")])

p("giuseppe-peano", "Giuseppe Peano", "ジュゼッペ・ペアノ", 1858, 1932, ["it"], ["mathematics"],
  "Giuseppe Peano was an Italian mathematician who made foundational contributions to mathematical logic and set theory, including the Peano axioms for natural numbers.",
  "Peano was born in Spinetta, Piedmont, Italy. He studied at the University of Turin and spent most of his career there as a professor.",
  "Peano's axioms for natural numbers provided a rigorous foundation for arithmetic. His space-filling curves challenged intuitions about dimension and his symbolic logic influenced Bertrand Russell.",
  [(1889, "Published the Peano axioms for natural numbers"), (1890, "Discovered space-filling curves"), (1895, "Began publishing Formulario Mathematico")],
  [("Arithmetices principia", 1889, "Introduced the Peano axioms providing a rigorous foundation for natural numbers")],
  [("Definitions are abbreviations.", "Formulario Mathematico")])

p("felix-klein", "Felix Klein", "フェリックス・クライン", 1849, 1925, ["de"], ["mathematics"],
  "Felix Klein was a German mathematician known for his work in group theory, complex analysis, non-Euclidean geometry, and the Erlangen program classifying geometries by their symmetry groups.",
  "Klein was born in Düsseldorf, Prussia. He studied at the University of Bonn and became one of the leading mathematicians of his era.",
  "Klein's Erlangen program unified various geometries by characterizing each as the study of invariants under a group of transformations. The Klein bottle remains one of the most famous objects in topology.",
  [(1872, "Published the Erlangen program"), (1882, "Described the Klein bottle"), (1886, "Became professor at Göttingen"), (1908, "Published Elementary Mathematics from an Advanced Standpoint")],
  [("Erlangen Program", 1872, "Classified geometries by their underlying symmetry groups")],
  [("Everyone knows what a curve is, until he has studied enough mathematics to become confused through the countless number of possible exceptions.", "Attributed")])

p("hermann-weyl", "Hermann Weyl", "ヘルマン・ヴァイル", 1885, 1955, ["de", "us"], ["mathematics", "physics"],
  "Hermann Weyl was a German mathematician and physicist who made major contributions to group theory, differential geometry, and quantum mechanics.",
  "Weyl was born in Elmshorn, Germany. He studied under David Hilbert at Göttingen and held positions at ETH Zürich and the Institute for Advanced Study in Princeton.",
  "Weyl's work unified mathematics and physics through group theory and symmetry. His gauge theory ideas became fundamental to modern particle physics, and his mathematical writings remain influential.",
  [(1913, "Published Die Idee der Riemannschen Fläche"), (1918, "Introduced gauge theory"), (1928, "Published Gruppentheorie und Quantenmechanik"), (1933, "Emigrated to the Institute for Advanced Study")],
  [("The Classical Groups", 1939, "Major work connecting group theory, invariant theory, and quantum mechanics"), ("Symmetry", 1952, "Influential book on the role of symmetry in mathematics and nature")],
  [("My work always tried to unite the true with the beautiful.", "Attributed")])

p("stefan-banach", "Stefan Banach", "ステファン・バナッハ", 1892, 1945, ["pl", "ua"], ["mathematics"],
  "Stefan Banach was a Polish mathematician and one of the founders of functional analysis. Banach spaces, named after him, are fundamental objects in modern analysis.",
  "Banach was born in Kraków. Largely self-taught, he was discovered by Hugo Steinhaus in a Kraków park discussing Lebesgue integrals, which led to a lifelong collaboration.",
  "Banach's work established functional analysis as a major branch of mathematics. The Hahn-Banach theorem, Banach-Steinhaus theorem, and Banach fixed-point theorem are cornerstones of modern analysis.",
  [(1920, "Earned doctorate with a thesis on functional operations"), (1922, "Published foundational work on normed linear spaces"), (1929, "Co-founded the journal Studia Mathematica"), (1932, "Published Théorie des opérations linéaires")],
  [("Théorie des opérations linéaires", 1932, "Foundational monograph establishing functional analysis as a discipline")],
  [("A mathematician is a person who can find analogies between theorems; a better mathematician is one who can see analogies between proofs.", "Attributed")])

p("blaise-pascal-math", "Blaise Pascal", "ブレーズ・パスカル", 1623, 1662, ["fr"], ["mathematics", "philosophy", "physics"],
  "Blaise Pascal was a French mathematician, physicist, and philosopher who made fundamental contributions to projective geometry, probability theory, and the physics of fluids and pressure.",
  "Pascal was born in Clermont-Ferrand, France. A child prodigy, he wrote a significant treatise on projective geometry at age 16 and invented a mechanical calculator at 19.",
  "Pascal's contributions span mathematics, physics, and philosophy. Pascal's triangle, the Pascaline calculator, and his work on probability with Fermat laid foundations for multiple fields.",
  [(1640, "Published Essay on Conics at age 16"), (1642, "Invented the Pascaline mechanical calculator"), (1654, "Correspondence with Fermat founding probability theory"), (1656, "Published Provincial Letters"), (1670, "Pensées published posthumously")],
  [("Pensées", 1670, "Philosophical defense of Christianity containing Pascal's wager"), ("Provincial Letters", 1656, "Influential series of letters on theology and ethics")],
  [("The heart has its reasons which reason knows nothing of.", "Pensées, 1670")])

p("george-boole", "George Boole", "ジョージ・ブール", 1815, 1864, ["gb"], ["mathematics"],
  "George Boole was an English mathematician and logician who developed Boolean algebra, the basis for modern digital computer circuits and programming.",
  "Boole was born in Lincoln, England, to a working-class family. Largely self-taught in mathematics, he became the first professor of mathematics at Queen's College, Cork.",
  "Boolean algebra became the mathematical foundation of digital computing. Every modern computer uses Boolean logic gates, making Boole's work fundamental to the information age.",
  [(1847, "Published The Mathematical Analysis of Logic"), (1849, "Appointed professor at Queen's College, Cork"), (1854, "Published An Investigation of the Laws of Thought")],
  [("An Investigation of the Laws of Thought", 1854, "Foundational work establishing Boolean algebra and mathematical logic")],
  [("No general method for the solution of questions in the theory of probabilities can be established which does not explicitly recognise the connexion of the science with logic.", "Laws of Thought, 1854")])

p("carl-jacobi", "Carl Gustav Jacob Jacobi", "カール・グスタフ・ヤコブ・ヤコビ", 1804, 1851, ["de"], ["mathematics"],
  "Carl Jacobi was a German mathematician who made fundamental contributions to elliptic functions, dynamics, differential equations, and number theory.",
  "Jacobi was born in Potsdam, Prussia. He entered the University of Berlin at age 16 and earned his doctorate at 21, quickly becoming one of the leading mathematicians of his time.",
  "Jacobi's work on elliptic functions, the Jacobian determinant, and the Hamilton-Jacobi equation remain fundamental to mathematics and physics. He was one of the greatest computational mathematicians of his era.",
  [(1829, "Published Fundamenta nova theoriae functionum ellipticarum"), (1841, "Developed the theory of determinants including the Jacobian"), (1843, "Lectured on dynamics developing the Hamilton-Jacobi equation")],
  [("Fundamenta nova", 1829, "Major treatise developing the theory of elliptic functions")],
  [("Man must always invert.", "Attributed mathematical principle")])

p("karl-weierstrass", "Karl Weierstrass", "カール・ワイエルシュトラス", 1815, 1897, ["de"], ["mathematics"],
  "Karl Weierstrass was a German mathematician often called the father of modern analysis for his rigorous reformulation of calculus.",
  "Weierstrass was born in Ostenfelde, Westphalia. He spent years as a schoolteacher before his mathematical papers brought him recognition and a professorship in Berlin at age 40.",
  "Weierstrass provided the first rigorous definition of a limit using the epsilon-delta method, which became the standard foundation for calculus. His discovery of continuous but nowhere differentiable functions challenged mathematical intuition.",
  [(1854, "Published paper that brought academic recognition"), (1856, "Appointed professor at the University of Berlin"), (1872, "Presented his everywhere continuous, nowhere differentiable function")],
  [("Epsilon-delta definition of limits", 1861, "Rigorous foundation for mathematical analysis replacing intuitive notions of limits")],
  [("A mathematician who is not also something of a poet will never be a complete mathematician.", "Attributed")])

p("peter-gustav-lejeune-dirichlet", "Peter Gustav Lejeune Dirichlet", "ペーター・グスタフ・ディリクレ", 1805, 1859, ["de"], ["mathematics"],
  "Peter Gustav Lejeune Dirichlet was a German mathematician who made deep contributions to number theory, analysis, and mathematical physics.",
  "Dirichlet was born in Düren, Prussia. He studied in Paris, where he was influenced by Fourier and Laplace, and later succeeded Gauss at the University of Göttingen.",
  "Dirichlet's theorem on primes in arithmetic progressions and his work on Fourier series were landmarks in number theory and analysis. He brought new rigor to mathematical analysis.",
  [(1829, "Published conditions for convergence of Fourier series"), (1837, "Proved theorem on primes in arithmetic progressions"), (1855, "Succeeded Gauss at Göttingen")],
  [("Dirichlet's Theorem on Arithmetic Progressions", 1837, "Proved that any arithmetic progression with coprime first term and difference contains infinitely many primes")],
  [("In mathematics, the art of proposing a question must be held of higher value than solving it.", "Attributed")])

p("ernst-kummer", "Ernst Kummer", "エルンスト・クンマー", 1810, 1893, ["de"], ["mathematics"],
  "Ernst Kummer was a German mathematician who introduced ideal numbers and made important contributions to number theory and algebraic geometry.",
  "Kummer was born in Sorau, Brandenburg. He studied at the University of Halle and became a professor at the University of Berlin.",
  "Kummer's ideal numbers, introduced to address unique factorization failures, became the foundation for modern algebraic number theory. His work proved Fermat's Last Theorem for many cases.",
  [(1844, "Showed unique factorization fails in cyclotomic fields"), (1847, "Introduced ideal numbers to restore unique factorization"), (1857, "Proved Fermat's Last Theorem for all regular primes")],
  [("Theory of Ideal Numbers", 1847, "Introduced ideal numbers to restore unique factorization in algebraic number fields")],
  [("The problem of the higher reciprocity laws constitutes one of the most beautiful domains of pure mathematics.", "Attributed")])

p("charles-hermite", "Charles Hermite", "シャルル・エルミート", 1822, 1901, ["fr"], ["mathematics"],
  "Charles Hermite was a French mathematician who proved the transcendence of e and made important contributions to number theory, algebra, and analysis.",
  "Hermite was born in Dieuze, Lorraine. Despite struggling with formal education due to a physical disability, he became one of the leading mathematicians of the 19th century.",
  "Hermite proved that e is transcendental, established Hermitian matrices in linear algebra, and his methods inspired Lindemann's proof that pi is transcendental.",
  [(1858, "Solved the quintic equation using elliptic functions"), (1873, "Proved the transcendence of e"), (1870, "Introduced Hermitian forms and matrices")],
  [("Proof of the Transcendence of e", 1873, "Demonstrated that e is not a root of any polynomial equation with rational coefficients")],
  [("I turn aside with a shudder of horror from this lamentable plague of functions which have no derivatives.", "On Weierstrass's pathological functions")])

p("richard-dedekind", "Richard Dedekind", "リヒャルト・デデキント", 1831, 1916, ["de"], ["mathematics"],
  "Richard Dedekind was a German mathematician who made major contributions to abstract algebra and the foundations of the real number system through Dedekind cuts.",
  "Dedekind was born in Brunswick, Germany. He studied at the University of Göttingen under Gauss and later became a close collaborator of Dirichlet.",
  "Dedekind's construction of real numbers via Dedekind cuts provided a rigorous foundation for analysis. His work on ideals in ring theory was foundational for modern algebra.",
  [(1858, "Developed Dedekind cuts to construct real numbers"), (1871, "Introduced ideals in algebraic number theory"), (1888, "Published Was sind und was sollen die Zahlen?")],
  [("Was sind und was sollen die Zahlen?", 1888, "Rigorous foundation for natural numbers using set-theoretic methods")],
  [("Numbers are free creations of the human mind.", "Was sind und was sollen die Zahlen?, 1888")])

p("elie-cartan", "Élie Cartan", "エリー・カルタン", 1869, 1951, ["fr"], ["mathematics"],
  "Élie Cartan was a French mathematician who made fundamental contributions to differential geometry, Lie groups, and the theory of spinors.",
  "Cartan was born in Dolomieu, Isère, to a poor family. A scholarship allowed him to study at the École Normale Supérieure in Paris.",
  "Cartan's work on Lie groups, differential forms, and moving frames transformed differential geometry. His theory of symmetric spaces and spinors influenced both mathematics and theoretical physics.",
  [(1894, "Completed classification of semisimple Lie algebras"), (1913, "Developed theory of differential forms and exterior calculus"), (1926, "Introduced the theory of symmetric spaces"), (1938, "Published Leçons sur la théorie des spineurs")],
  [("Theory of Spinors", 1938, "Introduced spinors, later fundamental to quantum mechanics and general relativity")],
  [("The more I study mathematics, the more I realize the harmony between the different theories.", "Attributed")])

p("norbert-wiener", "Norbert Wiener", "ノーバート・ウィーナー", 1894, 1964, ["us"], ["mathematics", "engineering"],
  "Norbert Wiener was an American mathematician who founded cybernetics and made important contributions to stochastic processes and information theory.",
  "Wiener was born in Columbia, Missouri. A child prodigy, he entered Tufts College at 11, earned his PhD from Harvard at 18, and studied under Bertrand Russell and David Hilbert.",
  "Wiener's founding of cybernetics — the study of control and communication in animals and machines — profoundly influenced computer science, neuroscience, and control theory.",
  [(1914, "Earned PhD from Harvard at age 18"), (1919, "Joined MIT faculty"), (1923, "Developed rigorous theory of Brownian motion"), (1948, "Published Cybernetics")],
  [("Cybernetics", 1948, "Founded the interdisciplinary study of control and communication systems")],
  [("The best material model of a cat is another, or preferably the same, cat.", "Philosophy of Science, 1945")])

p("bertrand-russell", "Bertrand Russell", "バートランド・ラッセル", 1872, 1970, ["gb"], ["mathematics", "philosophy"],
  "Bertrand Russell was a British philosopher, logician, and mathematician who co-authored Principia Mathematica and made major contributions to mathematical logic and analytic philosophy.",
  "Russell was born into an aristocratic family in Monmouthshire, Wales. He studied at Trinity College, Cambridge, where he was influenced by Alfred North Whitehead.",
  "Russell's Principia Mathematica, co-written with Whitehead, attempted to derive all mathematics from logic. Russell's paradox exposed contradictions in naive set theory, revolutionizing mathematical foundations.",
  [(1901, "Discovered Russell's paradox"), (1910, "Published Principia Mathematica with Whitehead"), (1945, "Published A History of Western Philosophy"), (1950, "Awarded the Nobel Prize in Literature")],
  [("Principia Mathematica", 1910, "Monumental attempt to ground all mathematics in formal logic"), ("A History of Western Philosophy", 1945, "Influential survey of Western philosophical thought")],
  [("The whole problem with the world is that fools and fanatics are always so certain of themselves, and wiser people so full of doubts.", "Attributed")])

p("alfred-north-whitehead", "Alfred North Whitehead", "アルフレッド・ノース・ホワイトヘッド", 1861, 1947, ["gb", "us"], ["mathematics", "philosophy"],
  "Alfred North Whitehead was a British mathematician and philosopher who co-authored Principia Mathematica with Bertrand Russell and later developed process philosophy.",
  "Whitehead was born in Ramsgate, Kent. He studied at Trinity College, Cambridge, and taught mathematics there before moving to London and eventually Harvard.",
  "Whitehead's collaboration with Russell on Principia Mathematica was a landmark in mathematical logic. His later process philosophy influenced theology, ecology, and metaphysics.",
  [(1898, "Published A Treatise on Universal Algebra"), (1910, "Published Principia Mathematica with Russell"), (1924, "Moved to Harvard University"), (1929, "Published Process and Reality")],
  [("Principia Mathematica", 1910, "Co-authored attempt to ground all mathematics in formal logic"), ("Process and Reality", 1929, "Major work in process philosophy and metaphysics")],
  [("The art of progress is to preserve order amid change and to preserve change amid order.", "Process and Reality, 1929")])

p("john-nash", "John Forbes Nash Jr.", "ジョン・ナッシュ", 1928, 2015, ["us"], ["mathematics"],
  "John Nash was an American mathematician who made fundamental contributions to game theory, differential geometry, and partial differential equations. His life was depicted in the film A Beautiful Mind.",
  "Nash was born in Bluefield, West Virginia. He showed early mathematical aptitude and earned his PhD from Princeton at age 22 with a 28-page thesis on non-cooperative games.",
  "Nash's equilibrium concept revolutionized economics, political science, and evolutionary biology. Despite decades of schizophrenia, he recovered and shared the 1994 Nobel Prize in Economics.",
  [(1950, "Published PhD thesis introducing Nash equilibrium"), (1956, "Published embedding theorem in differential geometry"), (1958, "Diagnosed with schizophrenia"), (1994, "Awarded Nobel Prize in Economics"), (2015, "Awarded the Abel Prize")],
  [("Non-Cooperative Games", 1950, "Introduced Nash equilibrium, transforming game theory and economics")],
  [("People are always selling the idea that people with mental illness are suffering. I think madness can be an escape.", "A Beautiful Mind")])

p("grigori-perelman", "Grigori Perelman", "グリゴリー・ペレルマン", 1966, None, ["ru"], ["mathematics"],
  "Grigori Perelman is a Russian mathematician who proved the Poincaré conjecture and Thurston's geometrization conjecture, two of the most important problems in topology.",
  "Perelman was born in Leningrad. He showed exceptional talent at a young age, winning a gold medal at the 1982 International Mathematical Olympiad with a perfect score.",
  "Perelman's proof of the Poincaré conjecture, one of the seven Millennium Prize Problems, was one of the greatest achievements in mathematics. He famously declined both the Fields Medal and the million-dollar prize.",
  [(1982, "Won IMO gold medal with perfect score"), (1994, "Proved the soul conjecture in Riemannian geometry"), (2002, "Posted proof of the Poincaré conjecture on arXiv"), (2006, "Declined the Fields Medal"), (2010, "Declined the Millennium Prize")],
  [("Proof of the Poincaré Conjecture", 2002, "Proved the century-old conjecture using Ricci flow with surgery")],
  [("I don't want to be on display like an animal in a zoo.", "On declining awards")])

p("shiing-shen-chern", "Shiing-Shen Chern", "陳省身", 1911, 2004, ["cn", "us"], ["mathematics"],
  "Shiing-Shen Chern was a Chinese-American mathematician who made fundamental contributions to differential geometry and topology, including the Chern classes.",
  "Chern was born in Jiaxing, China. He studied at Nankai University and later at the University of Hamburg under Wilhelm Blaschke, earning his doctorate in 1936.",
  "Chern's work on characteristic classes and fiber bundles unified differential geometry and topology. The Chern-Gauss-Bonnet theorem and Chern classes are central to modern geometry and theoretical physics.",
  [(1936, "Earned PhD from University of Hamburg"), (1946, "Founded the Institute of Mathematics at Academia Sinica"), (1960, "Joined UC Berkeley"), (1984, "Won the Wolf Prize in Mathematics"), (2004, "Awarded the inaugural Shaw Prize in Mathematics")],
  [("Chern-Gauss-Bonnet Theorem", 1944, "Generalized the classical Gauss-Bonnet theorem to higher dimensions")],
  [("Do not worry about your difficulties in mathematics; I assure you that mine are greater.", "Attributed")])

write_people(P)
