#!/usr/bin/env python3
"""Generate 20 physicist JSON files for the Great People Engine (batch 3)."""

import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "people")

def i18n(en="", ja=""):
    return {"en": en, "es": "", "pt": "", "fr": "", "de": "", "zh": "", "hi": "", "ar": "", "id": "", "ja": ja}

def name_i18n(en, ja):
    return {"en": en, "es": "", "pt": "", "fr": "", "de": "", "zh": "", "hi": "", "ar": "", "id": "", "ja": ja}

PHYSICISTS = [
    {
        "id": "lise-meitner",
        "name": name_i18n("Lise Meitner", "リーゼ・マイトナー"),
        "birth_year": 1878,
        "death_year": 1968,
        "countries": ["at", "se"],
        "fields": ["physics"],
        "overview": i18n("Lise Meitner was an Austrian-Swedish physicist who contributed to the discovery of nuclear fission. She provided the first theoretical explanation of the fission process alongside her nephew Otto Frisch. Despite her pivotal role, she was overlooked for the Nobel Prize awarded to Otto Hahn."),
        "early_life": i18n("Meitner was born in Vienna, Austria, in 1878 into a Jewish family. She studied physics at the University of Vienna under Ludwig Boltzmann and became one of the first women in Austria to earn a doctorate in physics."),
        "impact": i18n("Meitner's theoretical explanation of nuclear fission fundamentally changed nuclear physics and paved the way for both nuclear energy and nuclear weapons. Element 109, meitnerium, was named in her honor. She remains a symbol of scientific contributions overlooked due to gender bias."),
        "timeline": [
            {"year": 1906, "event": i18n("Earned her doctorate in physics from the University of Vienna.")},
            {"year": 1912, "event": i18n("Began collaboration with Otto Hahn at the Kaiser Wilhelm Institute in Berlin.")},
            {"year": 1923, "event": i18n("Discovered the radiationless transition known as the Auger effect.")},
            {"year": 1938, "event": i18n("Fled Nazi Germany to Sweden due to her Jewish heritage.")},
            {"year": 1939, "event": i18n("Published the first theoretical explanation of nuclear fission with Otto Frisch.")},
        ],
        "famous_works": [
            {"title": i18n("Disintegration of Uranium by Neutrons: A New Type of Nuclear Reaction"), "year": 1939, "description": i18n("Landmark paper with Otto Frisch providing the theoretical framework for nuclear fission.")},
            {"title": i18n("Discovery of Protactinium"), "year": 1918, "description": i18n("Co-discovered the element protactinium-231 with Otto Hahn.")},
        ],
        "quotes": [
            {"text": i18n("Science makes people reach selflessly for truth and objectivity; it teaches people to accept reality, with wonder and admiration."), "source": "Lise Meitner, letter"},
            {"text": i18n("I will have nothing to do with a bomb!"), "source": "Lise Meitner, response to the Manhattan Project invitation"},
        ],
        "relations": [
            {"person": "otto-hahn", "type": "collaborator"},
            {"person": "otto-frisch", "type": "collaborator"},
            {"person": "niels-bohr", "type": "colleague"},
            {"person": "max-born", "type": "colleague"},
        ],
    },
    {
        "id": "niels-bohr",
        "name": name_i18n("Niels Bohr", "ニールス・ボーア"),
        "birth_year": 1885,
        "death_year": 1962,
        "countries": ["dk"],
        "fields": ["physics"],
        "overview": i18n("Niels Bohr was a Danish physicist who made foundational contributions to understanding atomic structure and quantum theory. He proposed the Bohr model of the atom, which introduced quantized electron orbits. He received the Nobel Prize in Physics in 1922."),
        "early_life": i18n("Bohr was born in Copenhagen, Denmark, to a prominent academic family. He studied physics at the University of Copenhagen and completed his doctorate in 1911 before traveling to England to work with J.J. Thomson and Ernest Rutherford."),
        "impact": i18n("Bohr's atomic model laid the groundwork for modern quantum mechanics and transformed our understanding of atomic physics. He founded the Institute for Theoretical Physics in Copenhagen, which became a world center for quantum research. His principle of complementarity remains a cornerstone of quantum interpretation."),
        "timeline": [
            {"year": 1913, "event": i18n("Published the Bohr model of the atom with quantized electron orbits.")},
            {"year": 1920, "event": i18n("Founded the Institute for Theoretical Physics at the University of Copenhagen.")},
            {"year": 1922, "event": i18n("Awarded the Nobel Prize in Physics for his work on atomic structure.")},
            {"year": 1927, "event": i18n("Introduced the principle of complementarity at the Solvay Conference.")},
            {"year": 1943, "event": i18n("Escaped from Nazi-occupied Denmark to Sweden and later to the United States.")},
        ],
        "famous_works": [
            {"title": i18n("On the Constitution of Atoms and Molecules"), "year": 1913, "description": i18n("Seminal paper introducing the Bohr model with quantized orbits for electrons.")},
            {"title": i18n("The Quantum Postulate and the Recent Development of Atomic Theory"), "year": 1928, "description": i18n("Paper presenting the complementarity principle in quantum mechanics.")},
            {"title": i18n("Atomic Physics and Human Knowledge"), "year": 1958, "description": i18n("Collection of essays on quantum mechanics and its philosophical implications.")},
        ],
        "quotes": [
            {"text": i18n("An expert is a person who has made all the mistakes that can be made in a very narrow field."), "source": "Attributed to Niels Bohr"},
            {"text": i18n("If quantum mechanics hasn't profoundly shocked you, you haven't understood it yet."), "source": "Attributed to Niels Bohr"},
        ],
        "relations": [
            {"person": "werner-heisenberg", "type": "mentor"},
            {"person": "albert-einstein", "type": "rival"},
            {"person": "ernest-rutherford", "type": "influenced_by"},
            {"person": "wolfgang-pauli", "type": "colleague"},
            {"person": "lise-meitner", "type": "colleague"},
        ],
    },
    {
        "id": "erwin-schrodinger",
        "name": name_i18n("Erwin Schrödinger", "エルヴィン・シュレーディンガー"),
        "birth_year": 1887,
        "death_year": 1961,
        "countries": ["at"],
        "fields": ["physics"],
        "overview": i18n("Erwin Schrödinger was an Austrian physicist who developed wave mechanics, a fundamental formulation of quantum mechanics. He is best known for the Schrödinger equation and his famous thought experiment, Schrödinger's cat. He shared the 1933 Nobel Prize in Physics with Paul Dirac."),
        "early_life": i18n("Schrödinger was born in Vienna, Austria, and was educated at the University of Vienna. He showed early talent in mathematics and physics, earning his doctorate in 1910 and serving in World War I before pursuing an academic career."),
        "impact": i18n("The Schrödinger equation became one of the most important equations in physics, governing the behavior of quantum systems. His wave mechanics formulation provided an alternative to matrix mechanics and is essential to modern chemistry and physics. Schrödinger's cat remains one of the most famous thought experiments in science."),
        "timeline": [
            {"year": 1926, "event": i18n("Published the Schrödinger equation, founding wave mechanics.")},
            {"year": 1933, "event": i18n("Awarded the Nobel Prize in Physics jointly with Paul Dirac.")},
            {"year": 1935, "event": i18n("Proposed the Schrödinger's cat thought experiment.")},
            {"year": 1944, "event": i18n("Published 'What Is Life?', influencing the development of molecular biology.")},
        ],
        "famous_works": [
            {"title": i18n("Quantization as an Eigenvalue Problem"), "year": 1926, "description": i18n("Series of papers introducing the Schrödinger equation and wave mechanics.")},
            {"title": i18n("What Is Life?"), "year": 1944, "description": i18n("Influential book exploring the physical basis of living systems, inspiring Watson and Crick.")},
            {"title": i18n("The Present Situation in Quantum Mechanics"), "year": 1935, "description": i18n("Paper introducing the Schrödinger's cat thought experiment.")},
        ],
        "quotes": [
            {"text": i18n("If we are going to stick to this damned quantum-jumping, then I regret that I ever had anything to do with quantum theory."), "source": "Erwin Schrödinger, in conversation at the Bohr Institute, 1926"},
            {"text": i18n("The task is not so much to see what no one has yet seen, but to think what nobody has yet thought about that which everybody sees."), "source": "Erwin Schrödinger"},
        ],
        "relations": [
            {"person": "paul-dirac", "type": "colleague"},
            {"person": "albert-einstein", "type": "friend"},
            {"person": "niels-bohr", "type": "rival"},
            {"person": "louis-de-broglie", "type": "influenced_by"},
        ],
    },
    {
        "id": "werner-heisenberg",
        "name": name_i18n("Werner Heisenberg", "ヴェルナー・ハイゼンベルク"),
        "birth_year": 1901,
        "death_year": 1976,
        "countries": ["de"],
        "fields": ["physics"],
        "overview": i18n("Werner Heisenberg was a German theoretical physicist and a key pioneer of quantum mechanics. He formulated the uncertainty principle and developed matrix mechanics, the first complete formulation of quantum mechanics. He received the Nobel Prize in Physics in 1932."),
        "early_life": i18n("Heisenberg was born in Würzburg, Germany, and studied physics at the University of Munich under Arnold Sommerfeld. He completed his doctorate at age 22 and soon began working with Niels Bohr in Copenhagen."),
        "impact": i18n("Heisenberg's uncertainty principle fundamentally changed the philosophy of science by establishing limits on what can be known about a quantum system. His matrix mechanics provided the first mathematically consistent formulation of quantum theory. He also led Germany's nuclear energy program during World War II."),
        "timeline": [
            {"year": 1925, "event": i18n("Developed matrix mechanics, the first formulation of quantum mechanics.")},
            {"year": 1927, "event": i18n("Published the uncertainty principle.")},
            {"year": 1932, "event": i18n("Awarded the Nobel Prize in Physics for the creation of quantum mechanics.")},
            {"year": 1941, "event": i18n("Became head of the German nuclear energy project during World War II.")},
            {"year": 1953, "event": i18n("Became president of the Alexander von Humboldt Foundation.")},
        ],
        "famous_works": [
            {"title": i18n("Quantum-Theoretical Re-interpretation of Kinematic and Mechanical Relations"), "year": 1925, "description": i18n("Foundational paper introducing matrix mechanics as the first formulation of quantum mechanics.")},
            {"title": i18n("On the Perceptual Content of Quantum Theoretical Kinematics and Mechanics"), "year": 1927, "description": i18n("Paper introducing the uncertainty principle.")},
            {"title": i18n("Physics and Philosophy"), "year": 1958, "description": i18n("Book exploring the philosophical implications of quantum mechanics.")},
        ],
        "quotes": [
            {"text": i18n("What we observe is not nature itself, but nature exposed to our method of questioning."), "source": "Werner Heisenberg, Physics and Philosophy"},
            {"text": i18n("The first gulp from the glass of natural sciences will turn you into an atheist, but at the bottom of the glass God is waiting for you."), "source": "Attributed to Werner Heisenberg"},
        ],
        "relations": [
            {"person": "niels-bohr", "type": "student"},
            {"person": "max-born", "type": "student"},
            {"person": "wolfgang-pauli", "type": "friend"},
            {"person": "albert-einstein", "type": "colleague"},
        ],
    },
    {
        "id": "max-born",
        "name": name_i18n("Max Born", "マックス・ボルン"),
        "birth_year": 1882,
        "death_year": 1970,
        "countries": ["de", "gb"],
        "fields": ["physics"],
        "overview": i18n("Max Born was a German-British physicist who was instrumental in the development of quantum mechanics. He is best known for his probabilistic interpretation of the wave function, known as the Born rule. He received the Nobel Prize in Physics in 1954."),
        "early_life": i18n("Born was born in Breslau, Germany (now Wroclaw, Poland), into an academic family. He studied at several German universities before completing his doctorate at the University of Göttingen, where he would later build a renowned physics department."),
        "impact": i18n("Born's statistical interpretation of the wave function became a fundamental pillar of quantum mechanics. His work at Göttingen created a world-leading center for theoretical physics that trained many future Nobel laureates. He also made important contributions to solid-state physics and optics."),
        "timeline": [
            {"year": 1921, "event": i18n("Appointed professor of theoretical physics at the University of Göttingen.")},
            {"year": 1925, "event": i18n("Collaborated with Heisenberg and Jordan to develop matrix mechanics.")},
            {"year": 1926, "event": i18n("Proposed the probabilistic interpretation of the wave function (Born rule).")},
            {"year": 1933, "event": i18n("Fled Nazi Germany and emigrated to Britain.")},
            {"year": 1954, "event": i18n("Awarded the Nobel Prize in Physics for his statistical interpretation of quantum mechanics.")},
        ],
        "famous_works": [
            {"title": i18n("On the Quantum Mechanics of Collisions"), "year": 1926, "description": i18n("Paper introducing the probabilistic interpretation of the wave function.")},
            {"title": i18n("On Quantum Mechanics"), "year": 1925, "description": i18n("Co-authored with Pascual Jordan, formalizing matrix mechanics.")},
            {"title": i18n("Principles of Optics"), "year": 1959, "description": i18n("Comprehensive textbook on optics co-authored with Emil Wolf, still widely used.")},
        ],
        "quotes": [
            {"text": i18n("I believe that ideas such as absolute certitude, absolute exactness, final truth, etc. are figments of the imagination which should not be admissible in any field of science."), "source": "Max Born, Nobel lecture, 1954"},
            {"text": i18n("The belief that there is only one truth, and that oneself is in possession of it, is the root of all evil in the world."), "source": "Max Born, My Life and My Views"},
        ],
        "relations": [
            {"person": "werner-heisenberg", "type": "mentor"},
            {"person": "wolfgang-pauli", "type": "mentor"},
            {"person": "albert-einstein", "type": "friend"},
            {"person": "j-robert-oppenheimer", "type": "mentor"},
        ],
    },
    {
        "id": "paul-dirac",
        "name": name_i18n("Paul Dirac", "ポール・ディラック"),
        "birth_year": 1902,
        "death_year": 1984,
        "countries": ["gb"],
        "fields": ["physics"],
        "overview": i18n("Paul Dirac was an English theoretical physicist who made fundamental contributions to quantum mechanics and quantum electrodynamics. He predicted the existence of antimatter through the Dirac equation. He shared the 1933 Nobel Prize in Physics with Erwin Schrödinger."),
        "early_life": i18n("Dirac was born in Bristol, England, to a Swiss father and English mother. He studied electrical engineering at the University of Bristol before switching to mathematics at the University of Cambridge, where he completed his PhD in 1926."),
        "impact": i18n("The Dirac equation unified quantum mechanics and special relativity, predicting the existence of antimatter before its experimental discovery. His formulation of quantum mechanics using bra-ket notation became standard in physics. He is widely regarded as one of the greatest theoretical physicists of the 20th century."),
        "timeline": [
            {"year": 1925, "event": i18n("Made key contributions to the new quantum mechanics independently of Heisenberg.")},
            {"year": 1928, "event": i18n("Published the Dirac equation, predicting the existence of antimatter.")},
            {"year": 1930, "event": i18n("Published 'The Principles of Quantum Mechanics', a foundational textbook.")},
            {"year": 1933, "event": i18n("Awarded the Nobel Prize in Physics jointly with Erwin Schrödinger.")},
        ],
        "famous_works": [
            {"title": i18n("The Quantum Theory of the Electron"), "year": 1928, "description": i18n("Paper introducing the Dirac equation, which predicted antimatter.")},
            {"title": i18n("The Principles of Quantum Mechanics"), "year": 1930, "description": i18n("Landmark textbook that became the standard reference for quantum mechanics.")},
            {"title": i18n("Quantised Singularities in the Electromagnetic Field"), "year": 1931, "description": i18n("Paper predicting the existence of magnetic monopoles.")},
        ],
        "quotes": [
            {"text": i18n("The laws of nature should be expressed in beautiful equations."), "source": "Paul Dirac"},
            {"text": i18n("Pick a flower on Earth and you move the farthest star."), "source": "Attributed to Paul Dirac"},
        ],
        "relations": [
            {"person": "erwin-schrodinger", "type": "colleague"},
            {"person": "niels-bohr", "type": "colleague"},
            {"person": "werner-heisenberg", "type": "colleague"},
            {"person": "richard-feynman", "type": "influenced"},
        ],
    },
    {
        "id": "wolfgang-pauli",
        "name": name_i18n("Wolfgang Pauli", "ヴォルフガング・パウリ"),
        "birth_year": 1900,
        "death_year": 1958,
        "countries": ["at", "us"],
        "fields": ["physics"],
        "overview": i18n("Wolfgang Pauli was an Austrian-American theoretical physicist known for his discovery of the exclusion principle, which explains the structure of atoms. He also postulated the existence of the neutrino. He received the Nobel Prize in Physics in 1945."),
        "early_life": i18n("Pauli was born in Vienna, Austria, and showed extraordinary talent from a young age. He studied under Arnold Sommerfeld in Munich and published a review of general relativity at age 21 that impressed Albert Einstein."),
        "impact": i18n("The Pauli exclusion principle is essential to understanding atomic structure, chemical bonding, and the stability of matter. His prediction of the neutrino opened an entire new field of particle physics. He was known for his sharp critical thinking, and the 'Pauli effect' became a humorous legend in physics."),
        "timeline": [
            {"year": 1921, "event": i18n("Published a comprehensive review of relativity theory at age 21.")},
            {"year": 1925, "event": i18n("Formulated the Pauli exclusion principle.")},
            {"year": 1930, "event": i18n("Postulated the existence of the neutrino to explain beta decay.")},
            {"year": 1940, "event": i18n("Proved the spin-statistics theorem.")},
            {"year": 1945, "event": i18n("Awarded the Nobel Prize in Physics for the exclusion principle.")},
        ],
        "famous_works": [
            {"title": i18n("On the Connexion between the Completion of Electron Groups in an Atom with the Complex Structure of Spectra"), "year": 1925, "description": i18n("Paper formulating the exclusion principle.")},
            {"title": i18n("The Connection Between Spin and Statistics"), "year": 1940, "description": i18n("Proof of the spin-statistics theorem.")},
        ],
        "quotes": [
            {"text": i18n("God made the bulk; surfaces were invented by the devil."), "source": "Wolfgang Pauli"},
            {"text": i18n("That is not only not right; it is not even wrong."), "source": "Wolfgang Pauli, on a colleague's imprecise paper"},
        ],
        "relations": [
            {"person": "niels-bohr", "type": "colleague"},
            {"person": "werner-heisenberg", "type": "friend"},
            {"person": "max-born", "type": "student"},
            {"person": "albert-einstein", "type": "colleague"},
        ],
    },
    {
        "id": "louis-de-broglie",
        "name": name_i18n("Louis de Broglie", "ルイ・ド・ブロイ"),
        "birth_year": 1892,
        "death_year": 1987,
        "countries": ["fr"],
        "fields": ["physics"],
        "overview": i18n("Louis de Broglie was a French physicist who proposed that particles of matter exhibit wave-like properties, a concept known as wave-particle duality. His doctoral thesis became one of the most important in the history of physics. He received the Nobel Prize in Physics in 1929."),
        "early_life": i18n("De Broglie was born into an aristocratic family in Dieppe, France. He initially studied history at the Sorbonne before turning to physics, inspired by his brother Maurice who was an experimental physicist."),
        "impact": i18n("De Broglie's hypothesis of matter waves became a cornerstone of quantum mechanics and directly inspired Schrödinger's wave equation. His work led to the development of electron diffraction experiments and ultimately to electron microscopy. His ideas remain central to modern physics."),
        "timeline": [
            {"year": 1924, "event": i18n("Submitted his doctoral thesis proposing wave-particle duality of matter.")},
            {"year": 1929, "event": i18n("Awarded the Nobel Prize in Physics for his discovery of the wave nature of electrons.")},
            {"year": 1933, "event": i18n("Appointed to the chair of theoretical physics at the University of Paris.")},
            {"year": 1952, "event": i18n("Awarded the first Kalinga Prize by UNESCO for popularizing science.")},
        ],
        "famous_works": [
            {"title": i18n("Recherches sur la théorie des quanta (Research on the Theory of Quanta)"), "year": 1924, "description": i18n("Doctoral thesis proposing that all matter has wave-like properties.")},
            {"title": i18n("An Introduction to the Study of Wave Mechanics"), "year": 1930, "description": i18n("Textbook expanding on his wave mechanics theories.")},
        ],
        "quotes": [
            {"text": i18n("After long reflection in solitude and meditation, I suddenly had the idea, during the year 1923, that the discovery made by Einstein in 1905 should be generalized by extending it to all material particles and notably to electrons."), "source": "Louis de Broglie, Nobel lecture, 1929"},
        ],
        "relations": [
            {"person": "albert-einstein", "type": "influenced_by"},
            {"person": "erwin-schrodinger", "type": "influenced"},
            {"person": "niels-bohr", "type": "colleague"},
        ],
    },
    {
        "id": "satyendra-nath-bose",
        "name": name_i18n("Satyendra Nath Bose", "サティエンドラ・ナート・ボース"),
        "birth_year": 1894,
        "death_year": 1974,
        "countries": ["in"],
        "fields": ["physics"],
        "overview": i18n("Satyendra Nath Bose was an Indian physicist who made fundamental contributions to quantum statistics. His work on the quantum statistics of photons, later extended by Einstein, led to the concept of Bose-Einstein statistics and the prediction of the Bose-Einstein condensate. The boson particle class is named after him."),
        "early_life": i18n("Bose was born in Calcutta, British India, and showed exceptional academic ability from an early age. He studied at Presidency College and later at the University of Calcutta, where he earned a master's degree in mixed mathematics."),
        "impact": i18n("Bose-Einstein statistics became one of the two fundamental types of quantum statistics, governing the behavior of integer-spin particles now called bosons. His work laid the theoretical foundation for the Bose-Einstein condensate, experimentally realized in 1995. The entire class of bosons, including photons and the Higgs boson, bear his name."),
        "timeline": [
            {"year": 1924, "event": i18n("Sent his paper on photon statistics to Albert Einstein, who recognized its significance.")},
            {"year": 1924, "event": i18n("Paper published with Einstein's support, establishing Bose-Einstein statistics.")},
            {"year": 1926, "event": i18n("Studied in Europe, meeting Einstein, de Broglie, and Marie Curie.")},
            {"year": 1945, "event": i18n("Appointed Khaira Professor of Physics at the University of Calcutta.")},
        ],
        "famous_works": [
            {"title": i18n("Planck's Law and the Hypothesis of Light Quanta"), "year": 1924, "description": i18n("Paper deriving Planck's radiation law using a novel counting method for photons.")},
        ],
        "quotes": [
            {"text": i18n("I have no intention of publishing any paper in English. I am determined that I shall write only in Bengali."), "source": "Satyendra Nath Bose, on his commitment to his mother tongue"},
        ],
        "relations": [
            {"person": "albert-einstein", "type": "collaborator"},
            {"person": "louis-de-broglie", "type": "colleague"},
            {"person": "cv-raman", "type": "colleague"},
        ],
    },
    {
        "id": "enrico-fermi",
        "name": name_i18n("Enrico Fermi", "エンリコ・フェルミ"),
        "birth_year": 1901,
        "death_year": 1954,
        "countries": ["it", "us"],
        "fields": ["physics"],
        "overview": i18n("Enrico Fermi was an Italian-American physicist known for creating the first nuclear reactor and for his contributions to quantum theory, nuclear and particle physics, and statistical mechanics. He was one of the few physicists who excelled in both theory and experiment. He received the Nobel Prize in Physics in 1938."),
        "early_life": i18n("Fermi was born in Rome, Italy, and showed precocious talent in physics and mathematics. He earned his doctorate from the Scuola Normale Superiore in Pisa at age 21 and quickly rose to prominence in Italian physics."),
        "impact": i18n("Fermi's creation of the first self-sustaining nuclear chain reaction ushered in the nuclear age. His work on beta decay theory and neutron-induced radioactivity advanced nuclear physics enormously. He trained a generation of physicists and his problem-solving approach remains legendary in the field."),
        "timeline": [
            {"year": 1926, "event": i18n("Developed Fermi-Dirac statistics for particles obeying the exclusion principle.")},
            {"year": 1934, "event": i18n("Developed the theory of beta decay.")},
            {"year": 1938, "event": i18n("Awarded the Nobel Prize in Physics for work on induced radioactivity.")},
            {"year": 1942, "event": i18n("Achieved the first self-sustaining nuclear chain reaction at the University of Chicago.")},
            {"year": 1949, "event": i18n("Co-proposed the Fermi-Ulam model for cosmic ray acceleration.")},
        ],
        "famous_works": [
            {"title": i18n("Tentative Theory of Beta Radiation"), "year": 1934, "description": i18n("Groundbreaking paper proposing the theory of beta decay involving the weak force.")},
            {"title": i18n("Chicago Pile-1"), "year": 1942, "description": i18n("First artificial self-sustaining nuclear chain reaction, a milestone in nuclear physics.")},
            {"title": i18n("Thermodynamics"), "year": 1937, "description": i18n("Classic textbook on thermodynamics that remains influential.")},
        ],
        "quotes": [
            {"text": i18n("There are two possible outcomes: if the result confirms the hypothesis, then you've made a measurement. If the result is contrary to the hypothesis, then you've made a discovery."), "source": "Attributed to Enrico Fermi"},
            {"text": i18n("It is no good to try to stop knowledge from going forward. Ignorance is never better than knowledge."), "source": "Enrico Fermi"},
        ],
        "relations": [
            {"person": "leo-szilard", "type": "collaborator"},
            {"person": "niels-bohr", "type": "colleague"},
            {"person": "paul-dirac", "type": "influenced_by"},
            {"person": "subrahmanyan-chandrasekhar", "type": "colleague"},
        ],
    },
    {
        "id": "emmy-noether",
        "name": name_i18n("Emmy Noether", "エミー・ネーター"),
        "birth_year": 1882,
        "death_year": 1935,
        "countries": ["de"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Emmy Noether was a German mathematician who made groundbreaking contributions to abstract algebra and theoretical physics. Her most famous result, Noether's theorem, establishes a profound connection between symmetries and conservation laws in physics. Einstein described her as the most important woman in the history of mathematics."),
        "early_life": i18n("Noether was born in Erlangen, Germany, into a mathematical family. She overcame significant barriers to women's education, auditing courses before women were officially admitted to universities, and earned her doctorate in mathematics in 1907."),
        "impact": i18n("Noether's theorem became one of the most important results in theoretical physics, underpinning modern particle physics and general relativity. Her work in abstract algebra revolutionized the field and established the foundations of modern algebraic thinking. She remains an icon of achievement in the face of gender discrimination in academia."),
        "timeline": [
            {"year": 1907, "event": i18n("Earned her doctorate in mathematics from the University of Erlangen.")},
            {"year": 1915, "event": i18n("Invited to the University of Göttingen by David Hilbert and Felix Klein.")},
            {"year": 1918, "event": i18n("Published Noether's theorem connecting symmetries and conservation laws.")},
            {"year": 1921, "event": i18n("Published foundational work on ideal theory in ring theory.")},
            {"year": 1933, "event": i18n("Fled Nazi Germany and joined Bryn Mawr College in the United States.")},
        ],
        "famous_works": [
            {"title": i18n("Invariante Variationsprobleme (Invariant Variation Problems)"), "year": 1918, "description": i18n("Paper proving Noether's theorem, linking symmetries to conservation laws.")},
            {"title": i18n("Idealtheorie in Ringbereichen (Ideal Theory in Rings)"), "year": 1921, "description": i18n("Foundational paper in abstract algebra establishing the theory of ideals.")},
        ],
        "quotes": [
            {"text": i18n("My methods are really methods of working and thinking; this is why they have crept in everywhere anonymously."), "source": "Attributed to Emmy Noether"},
        ],
        "relations": [
            {"person": "david-hilbert", "type": "colleague"},
            {"person": "albert-einstein", "type": "colleague"},
            {"person": "max-born", "type": "colleague"},
        ],
    },
    {
        "id": "cv-raman",
        "name": name_i18n("C.V. Raman", "チャンドラシェカール・ヴェンカタ・ラマン"),
        "birth_year": 1888,
        "death_year": 1970,
        "countries": ["in"],
        "fields": ["physics"],
        "overview": i18n("Chandrasekhara Venkata Raman was an Indian physicist who discovered the Raman effect, in which light changes wavelength when scattered by molecules. This discovery earned him the 1930 Nobel Prize in Physics, making him the first Asian to receive a Nobel Prize in science."),
        "early_life": i18n("Raman was born in Tiruchirappalli, British India, to a family of scholars. He excelled academically, completing his bachelor's degree at age 16, and initially worked in the Indian Finance Department before pursuing physics full-time."),
        "impact": i18n("The Raman effect became a powerful tool for identifying molecular structures and is now widely used in chemistry, materials science, and medicine through Raman spectroscopy. His Nobel Prize inspired generations of Indian scientists. He also founded the Indian Journal of Physics and the Indian Academy of Sciences."),
        "timeline": [
            {"year": 1917, "event": i18n("Resigned from government service to become professor of physics at the University of Calcutta.")},
            {"year": 1928, "event": i18n("Discovered the Raman effect, demonstrating inelastic scattering of light.")},
            {"year": 1930, "event": i18n("Awarded the Nobel Prize in Physics for his work on the scattering of light.")},
            {"year": 1934, "event": i18n("Founded the Indian Academy of Sciences.")},
            {"year": 1948, "event": i18n("Established the Raman Research Institute in Bangalore.")},
        ],
        "famous_works": [
            {"title": i18n("A New Type of Secondary Radiation"), "year": 1928, "description": i18n("Paper announcing the discovery of the Raman effect.")},
            {"title": i18n("Molecular Diffraction of Light"), "year": 1922, "description": i18n("Monograph on light scattering that laid groundwork for the Raman effect discovery.")},
        ],
        "quotes": [
            {"text": i18n("Ask the right questions, and nature will open the doors to her secrets."), "source": "C.V. Raman"},
            {"text": i18n("I am the master of my failure... If I never fail how will I ever learn."), "source": "C.V. Raman"},
        ],
        "relations": [
            {"person": "satyendra-nath-bose", "type": "colleague"},
            {"person": "subrahmanyan-chandrasekhar", "type": "mentor"},
            {"person": "niels-bohr", "type": "colleague"},
        ],
    },
    {
        "id": "subrahmanyan-chandrasekhar",
        "name": name_i18n("Subrahmanyan Chandrasekhar", "スブラマニアン・チャンドラセカール"),
        "birth_year": 1910,
        "death_year": 1995,
        "countries": ["in", "us"],
        "fields": ["physics", "astronomy"],
        "overview": i18n("Subrahmanyan Chandrasekhar was an Indian-American astrophysicist known for determining the mass limit for white dwarf stars, now called the Chandrasekhar limit. His work laid the foundation for the modern theory of stellar evolution. He received the Nobel Prize in Physics in 1983."),
        "early_life": i18n("Chandrasekhar was born in Lahore, British India, into a Tamil Brahmin family. His uncle C.V. Raman was a Nobel laureate. He studied at Presidency College in Madras and derived his famous limit while traveling to England for graduate study at age 19."),
        "impact": i18n("The Chandrasekhar limit fundamentally changed our understanding of stellar evolution, predicting that massive stars would collapse into neutron stars or black holes. His mathematical rigor set new standards in astrophysics. He made contributions across numerous areas including radiative transfer, stellar dynamics, and black hole physics."),
        "timeline": [
            {"year": 1930, "event": i18n("Calculated the maximum mass of a white dwarf star during his voyage to England.")},
            {"year": 1937, "event": i18n("Joined the University of Chicago, where he spent the rest of his career.")},
            {"year": 1952, "event": i18n("Published 'Radiative Transfer', a foundational work in the field.")},
            {"year": 1983, "event": i18n("Awarded the Nobel Prize in Physics for theoretical studies of stellar structure and evolution.")},
            {"year": 1995, "event": i18n("Published his final work on the mathematical theory of black holes.")},
        ],
        "famous_works": [
            {"title": i18n("An Introduction to the Study of Stellar Structure"), "year": 1939, "description": i18n("Comprehensive treatise on stellar physics including the Chandrasekhar limit.")},
            {"title": i18n("Radiative Transfer"), "year": 1950, "description": i18n("Foundational textbook on the theory of radiative transfer in stellar atmospheres.")},
            {"title": i18n("The Mathematical Theory of Black Holes"), "year": 1983, "description": i18n("Rigorous mathematical treatment of the physics of black holes.")},
        ],
        "quotes": [
            {"text": i18n("The pursuit of science has often been compared to the scaling of mountains, high and not so high."), "source": "Subrahmanyan Chandrasekhar, Nobel lecture, 1983"},
            {"text": i18n("I should like to be somewhat more precise in what I mean by beauty in science."), "source": "Subrahmanyan Chandrasekhar, Truth and Beauty"},
        ],
        "relations": [
            {"person": "cv-raman", "type": "influenced_by"},
            {"person": "arthur-eddington", "type": "rival"},
            {"person": "enrico-fermi", "type": "colleague"},
            {"person": "ralph-fowler", "type": "student"},
        ],
    },
    {
        "id": "hideki-yukawa",
        "name": name_i18n("Hideki Yukawa", "湯川秀樹"),
        "birth_year": 1907,
        "death_year": 1981,
        "countries": ["jp"],
        "fields": ["physics"],
        "overview": i18n("Hideki Yukawa was a Japanese theoretical physicist who predicted the existence of mesons as the carriers of the nuclear force. He became the first Japanese person to receive the Nobel Prize in Physics in 1949. His work was fundamental to the development of nuclear and particle physics."),
        "early_life": i18n("Yukawa was born in Tokyo, Japan, and grew up in Kyoto. He studied physics at Kyoto Imperial University and was deeply influenced by the emerging quantum mechanics from Europe. He adopted the surname Yukawa after marrying into the Yukawa family."),
        "impact": i18n("Yukawa's prediction of the meson was confirmed experimentally in 1947 and opened the door to understanding the strong nuclear force. His work inspired generations of Japanese physicists and helped establish Japan as a major center for theoretical physics. He was also an active advocate for nuclear disarmament."),
        "timeline": [
            {"year": 1935, "event": i18n("Published his theory predicting the existence of the meson particle.")},
            {"year": 1947, "event": i18n("The pi meson was experimentally discovered, confirming his prediction.")},
            {"year": 1949, "event": i18n("Awarded the Nobel Prize in Physics, the first Japanese laureate.")},
            {"year": 1953, "event": i18n("Founded the Research Institute for Fundamental Physics at Kyoto University.")},
        ],
        "famous_works": [
            {"title": i18n("On the Interaction of Elementary Particles"), "year": 1935, "description": i18n("Paper predicting the meson as the carrier of the strong nuclear force.")},
            {"title": i18n("Tabibito (The Traveler)"), "year": 1958, "description": i18n("Autobiography reflecting on his scientific journey and philosophy.")},
        ],
        "quotes": [
            {"text": i18n("Reality is cruel. All of the naivety is to be put aside. Reality is always changing, and it is always ahead of us."), "source": "Hideki Yukawa"},
            {"text": i18n("A good theoretical physicist today might find it useful to have a wide range of physical viewpoints and mathematical tools at his disposal."), "source": "Hideki Yukawa"},
        ],
        "relations": [
            {"person": "niels-bohr", "type": "influenced_by"},
            {"person": "werner-heisenberg", "type": "influenced_by"},
            {"person": "shin-ichiro-tomonaga", "type": "colleague"},
        ],
    },
    {
        "id": "leo-szilard",
        "name": name_i18n("Leo Szilard", "レオ・シラード"),
        "birth_year": 1898,
        "death_year": 1964,
        "countries": ["hu", "us"],
        "fields": ["physics"],
        "overview": i18n("Leo Szilard was a Hungarian-American physicist who conceived the nuclear chain reaction and was instrumental in the development of the atomic bomb. He drafted the famous Einstein-Szilard letter to President Roosevelt that initiated the Manhattan Project. He later became a prominent advocate for arms control."),
        "early_life": i18n("Szilard was born in Budapest, Hungary, into a Jewish family. He studied engineering and physics in Budapest and Berlin, where he worked with Albert Einstein on the design of a home refrigerator."),
        "impact": i18n("Szilard's conception of the nuclear chain reaction was the key insight that made nuclear weapons and nuclear power possible. His role in initiating the Manhattan Project shaped world history. After the war, he became one of the most vocal scientists advocating for arms control and peaceful uses of nuclear energy."),
        "timeline": [
            {"year": 1929, "event": i18n("Established the connection between information and thermodynamic entropy.")},
            {"year": 1933, "event": i18n("Conceived the idea of the nuclear chain reaction while crossing a London street.")},
            {"year": 1939, "event": i18n("Co-authored the Einstein-Szilard letter to President Roosevelt warning of atomic weapons.")},
            {"year": 1942, "event": i18n("Collaborated with Enrico Fermi on achieving the first nuclear chain reaction.")},
            {"year": 1945, "event": i18n("Circulated a petition opposing the use of atomic bombs on Japan.")},
        ],
        "famous_works": [
            {"title": i18n("Einstein-Szilard Letter"), "year": 1939, "description": i18n("Letter to President Roosevelt urging the development of atomic weapons before Nazi Germany.")},
            {"title": i18n("On the Decrease of Entropy in a Thermodynamic System by the Intervention of Intelligent Beings"), "year": 1929, "description": i18n("Pioneering paper connecting information theory to thermodynamics.")},
        ],
        "quotes": [
            {"text": i18n("If you want to succeed in this world, you don't have to be much cleverer than other people. You just have to be one day earlier."), "source": "Leo Szilard"},
            {"text": i18n("A scientist's aim in a discussion with his colleagues is not to persuade, but to clarify."), "source": "Leo Szilard"},
        ],
        "relations": [
            {"person": "albert-einstein", "type": "collaborator"},
            {"person": "enrico-fermi", "type": "collaborator"},
            {"person": "eugene-wigner", "type": "friend"},
        ],
    },
    {
        "id": "eugene-wigner",
        "name": name_i18n("Eugene Wigner", "ユージン・ウィグナー"),
        "birth_year": 1902,
        "death_year": 1995,
        "countries": ["hu", "us"],
        "fields": ["physics"],
        "overview": i18n("Eugene Wigner was a Hungarian-American theoretical physicist who made fundamental contributions to quantum mechanics and nuclear physics through the application of group theory. He received the Nobel Prize in Physics in 1963 for his work on the theory of the atomic nucleus and elementary particles."),
        "early_life": i18n("Wigner was born in Budapest, Hungary, and studied chemical engineering in Berlin, where he became interested in physics. He was influenced by discussions with fellow Hungarian physicists Leo Szilard and John von Neumann."),
        "impact": i18n("Wigner's application of group theory to quantum mechanics transformed theoretical physics and became an essential mathematical tool. His work on nuclear reactor theory was crucial to the Manhattan Project. He also raised profound philosophical questions about the role of consciousness in quantum measurement."),
        "timeline": [
            {"year": 1931, "event": i18n("Published 'Group Theory and Its Application to the Quantum Mechanics of Atomic Spectra'.")},
            {"year": 1936, "event": i18n("Developed the theory of neutron absorption in nuclear reactors.")},
            {"year": 1939, "event": i18n("Co-delivered the Einstein-Szilard letter to President Roosevelt.")},
            {"year": 1960, "event": i18n("Published 'The Unreasonable Effectiveness of Mathematics in the Natural Sciences'.")},
            {"year": 1963, "event": i18n("Awarded the Nobel Prize in Physics.")},
        ],
        "famous_works": [
            {"title": i18n("Group Theory and Its Application to the Quantum Mechanics of Atomic Spectra"), "year": 1931, "description": i18n("Foundational work applying group theory to quantum mechanics.")},
            {"title": i18n("The Unreasonable Effectiveness of Mathematics in the Natural Sciences"), "year": 1960, "description": i18n("Influential essay on why mathematics is so remarkably useful in physics.")},
            {"title": i18n("Symmetries and Reflections"), "year": 1967, "description": i18n("Collection of essays on science, philosophy, and the role of symmetry in physics.")},
        ],
        "quotes": [
            {"text": i18n("It is not at all natural that 'laws of nature' exist, much less that man is able to discover them."), "source": "Eugene Wigner, The Unreasonable Effectiveness of Mathematics"},
            {"text": i18n("The miracle of the appropriateness of the language of mathematics for the formulation of the laws of physics is a wonderful gift which we neither understand nor deserve."), "source": "Eugene Wigner"},
        ],
        "relations": [
            {"person": "leo-szilard", "type": "friend"},
            {"person": "john-von-neumann", "type": "friend"},
            {"person": "albert-einstein", "type": "colleague"},
            {"person": "enrico-fermi", "type": "colleague"},
        ],
    },
    {
        "id": "isidor-isaac-rabi",
        "name": name_i18n("Isidor Isaac Rabi", "イジドール・イザーク・ラービ"),
        "birth_year": 1898,
        "death_year": 1988,
        "countries": ["at", "us"],
        "fields": ["physics"],
        "overview": i18n("Isidor Isaac Rabi was an Austrian-American physicist who discovered nuclear magnetic resonance, a technique that later became the basis for MRI medical imaging. He received the Nobel Prize in Physics in 1944 and was an influential science advisor to the United States government."),
        "early_life": i18n("Rabi was born in Rymanów, Austria-Hungary (now Poland), and emigrated to the United States as an infant. He grew up in New York City and studied chemistry and physics at Cornell and Columbia universities."),
        "impact": i18n("Rabi's discovery of nuclear magnetic resonance revolutionized both physics and medicine, leading to the development of MRI technology. As a science advisor, he helped establish CERN and was instrumental in shaping postwar American science policy. He mentored several future Nobel laureates at Columbia University."),
        "timeline": [
            {"year": 1937, "event": i18n("Developed the magnetic resonance method for measuring nuclear magnetic properties.")},
            {"year": 1944, "event": i18n("Awarded the Nobel Prize in Physics for the resonance method.")},
            {"year": 1952, "event": i18n("Played a key role in the founding of CERN.")},
            {"year": 1957, "event": i18n("Served as chairman of the General Advisory Committee of the Atomic Energy Commission.")},
        ],
        "famous_works": [
            {"title": i18n("Space Quantization in a Gyrating Magnetic Field"), "year": 1937, "description": i18n("Paper describing the molecular beam magnetic resonance detection method.")},
            {"title": i18n("My Life and Times as a Physicist"), "year": 1960, "description": i18n("Memoir recounting his career and views on science and society.")},
        ],
        "quotes": [
            {"text": i18n("Who ordered that?"), "source": "Isidor Isaac Rabi, upon learning of the muon's discovery"},
            {"text": i18n("My mother made me a scientist without ever intending to. Every other Jewish mother in Brooklyn would ask her child after school: 'So? Did you learn anything today?' But not my mother. 'Izzy,' she would say, 'did you ask a good question today?'"), "source": "Isidor Isaac Rabi"},
        ],
        "relations": [
            {"person": "niels-bohr", "type": "influenced_by"},
            {"person": "werner-heisenberg", "type": "influenced_by"},
            {"person": "j-robert-oppenheimer", "type": "friend"},
            {"person": "enrico-fermi", "type": "colleague"},
        ],
    },
    {
        "id": "robert-millikan",
        "name": name_i18n("Robert Millikan", "ロバート・ミリカン"),
        "birth_year": 1868,
        "death_year": 1953,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Robert Millikan was an American experimental physicist who measured the charge of the electron using his famous oil drop experiment. He also verified Einstein's photoelectric equation and measured Planck's constant. He received the Nobel Prize in Physics in 1923."),
        "early_life": i18n("Millikan was born in Morrison, Illinois, and studied at Oberlin College before earning his doctorate at Columbia University. He spent time studying in Europe before joining the University of Chicago."),
        "impact": i18n("Millikan's precise measurement of the electron charge was a cornerstone of modern physics, confirming the quantized nature of electric charge. His verification of the photoelectric effect supported quantum theory. He also helped build Caltech into a world-renowned institution as its chairman."),
        "timeline": [
            {"year": 1909, "event": i18n("Began the oil drop experiment to measure the charge of the electron.")},
            {"year": 1913, "event": i18n("Published precise measurements confirming the quantized nature of electric charge.")},
            {"year": 1916, "event": i18n("Verified Einstein's photoelectric equation and measured Planck's constant.")},
            {"year": 1921, "event": i18n("Became chairman of the executive council at Caltech.")},
            {"year": 1923, "event": i18n("Awarded the Nobel Prize in Physics.")},
        ],
        "famous_works": [
            {"title": i18n("On the Elementary Electrical Charge and the Avogadro Constant"), "year": 1913, "description": i18n("Paper reporting precise measurements of the electron charge from the oil drop experiment.")},
            {"title": i18n("A Direct Photoelectric Determination of Planck's h"), "year": 1916, "description": i18n("Paper verifying Einstein's photoelectric equation and measuring Planck's constant.")},
        ],
        "quotes": [
            {"text": i18n("Science walks forward on two feet, namely theory and experiment."), "source": "Robert Millikan, Nobel lecture, 1924"},
        ],
        "relations": [
            {"person": "albert-einstein", "type": "colleague"},
            {"person": "arthur-compton", "type": "colleague"},
            {"person": "albert-michelson", "type": "influenced_by"},
        ],
    },
    {
        "id": "arthur-compton",
        "name": name_i18n("Arthur Compton", "アーサー・コンプトン"),
        "birth_year": 1892,
        "death_year": 1962,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Arthur Compton was an American physicist who demonstrated that X-rays and gamma rays have particle-like properties through the Compton scattering effect. His work provided key evidence for the quantum nature of electromagnetic radiation. He received the Nobel Prize in Physics in 1927."),
        "early_life": i18n("Compton was born in Wooster, Ohio, into an academic family. He studied at the College of Wooster and Princeton University, earning his doctorate in 1916. He initially worked on X-ray scattering at Washington University in St. Louis."),
        "impact": i18n("The Compton effect provided definitive evidence that light has particle properties, helping to establish wave-particle duality. His work was crucial in the acceptance of quantum mechanics. During World War II, he directed the Metallurgical Laboratory that contributed to the development of the first nuclear reactor."),
        "timeline": [
            {"year": 1922, "event": i18n("Discovered the Compton effect, demonstrating photon-electron scattering.")},
            {"year": 1927, "event": i18n("Awarded the Nobel Prize in Physics for the discovery of the Compton effect.")},
            {"year": 1941, "event": i18n("Appointed director of the Metallurgical Laboratory for the Manhattan Project.")},
            {"year": 1942, "event": i18n("Oversaw the first nuclear chain reaction experiment under Enrico Fermi.")},
            {"year": 1945, "event": i18n("Served on the Interim Committee advising on the use of atomic weapons.")},
        ],
        "famous_works": [
            {"title": i18n("A Quantum Theory of the Scattering of X-Rays by Light Elements"), "year": 1923, "description": i18n("Paper describing the Compton effect and providing evidence for the particle nature of light.")},
            {"title": i18n("X-Rays and Electrons"), "year": 1926, "description": i18n("Comprehensive treatise on X-ray physics and electron interactions.")},
        ],
        "quotes": [
            {"text": i18n("The scientist is not the person who always gives the right answers, but the one who asks the right questions."), "source": "Attributed to Arthur Compton"},
        ],
        "relations": [
            {"person": "enrico-fermi", "type": "colleague"},
            {"person": "robert-millikan", "type": "colleague"},
            {"person": "niels-bohr", "type": "colleague"},
        ],
    },
    {
        "id": "pieter-zeeman",
        "name": name_i18n("Pieter Zeeman", "ピーター・ゼーマン"),
        "birth_year": 1865,
        "death_year": 1943,
        "countries": ["nl"],
        "fields": ["physics"],
        "overview": i18n("Pieter Zeeman was a Dutch physicist who discovered the splitting of spectral lines in a magnetic field, known as the Zeeman effect. This discovery provided crucial evidence for the electron theory of matter. He shared the 1902 Nobel Prize in Physics with Hendrik Lorentz."),
        "early_life": i18n("Zeeman was born in Zonnemaire, Netherlands, a small village in Zeeland. He studied physics at the University of Leiden under Hendrik Lorentz and Heike Kamerlingh Onnes, completing his doctorate in 1893."),
        "impact": i18n("The Zeeman effect was instrumental in confirming the existence of electron spin and understanding atomic structure. It became a powerful tool in spectroscopy and astrophysics for measuring magnetic fields. His work supported the classical electron theory of Lorentz and paved the way for quantum mechanics."),
        "timeline": [
            {"year": 1896, "event": i18n("Discovered the splitting of spectral lines in a magnetic field (Zeeman effect).")},
            {"year": 1900, "event": i18n("Appointed professor of physics at the University of Amsterdam.")},
            {"year": 1902, "event": i18n("Awarded the Nobel Prize in Physics jointly with Hendrik Lorentz.")},
            {"year": 1923, "event": i18n("Became director of the newly built Zeeman Laboratory in Amsterdam.")},
        ],
        "famous_works": [
            {"title": i18n("On the Influence of Magnetism on the Nature of the Light Emitted by a Substance"), "year": 1897, "description": i18n("Paper describing the discovery of the Zeeman effect.")},
            {"title": i18n("Researches in Magneto-Optics"), "year": 1913, "description": i18n("Comprehensive account of his experimental work on the interaction of light and magnetism.")},
        ],
        "quotes": [
            {"text": i18n("It was in the autumn of 1896 that I conceived the idea of making an experiment to decide the question of the influence of magnetism on the nature of light."), "source": "Pieter Zeeman, Nobel lecture, 1902"},
        ],
        "relations": [
            {"person": "hendrik-lorentz", "type": "student"},
            {"person": "heike-kamerlingh-onnes", "type": "colleague"},
            {"person": "niels-bohr", "type": "influenced"},
        ],
    },
]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    skip = {"albert-einstein"}
    generated = 0

    for person in PHYSICISTS:
        pid = person["id"]
        if pid in skip:
            print(f"SKIP: {pid} (already exists)")
            continue

        filepath = os.path.join(OUTPUT_DIR, f"{pid}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(person, f, ensure_ascii=False, indent=2)
        print(f"CREATED: {filepath}")
        generated += 1

    print(f"\nDone. Generated {generated} files.")

if __name__ == "__main__":
    main()
