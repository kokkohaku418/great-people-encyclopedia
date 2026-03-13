#!/usr/bin/env python3
"""Batch 4: Generate 20 physicist JSON files (Mid 20th Century)."""

import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "people")

LANGS = ["en", "es", "pt", "fr", "de", "zh", "hi", "ar", "id", "ja"]


def i18n(en="", ja=""):
    """Create an i18n dict with en and ja filled, rest empty."""
    d = {lang: "" for lang in LANGS}
    d["en"] = en
    d["ja"] = ja
    return d


def name_i18n(en, ja):
    return i18n(en, ja)


def event(year, en):
    return {"year": year, "event": i18n(en)}


def work(title_en, year, desc_en):
    return {"title": i18n(title_en), "year": year, "description": i18n(desc_en)}


def quote(text_en, source):
    return {"text": i18n(text_en), "source": source}


def rel(person, rtype):
    return {"person": person, "type": rtype}


PEOPLE = [
    {
        "id": "j-robert-oppenheimer",
        "name": name_i18n("J. Robert Oppenheimer", "J・ロバート・オッペンハイマー"),
        "birth_year": 1904,
        "death_year": 1967,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("J. Robert Oppenheimer was an American theoretical physicist who led the Manhattan Project during World War II. Known as the 'father of the atomic bomb,' he made significant contributions to quantum mechanics, nuclear physics, and astrophysics."),
        "early_life": i18n("Oppenheimer was born in New York City to a wealthy family and showed early intellectual brilliance. He studied at Harvard, Cambridge, and the University of Göttingen, where he earned his doctorate in physics under Max Born."),
        "impact": i18n("Oppenheimer's leadership of the Manhattan Project resulted in the development of the first nuclear weapons, fundamentally altering global geopolitics. His later advocacy for arms control and his opposition to the hydrogen bomb led to his controversial security hearing in 1954."),
        "timeline": [
            event(1925, "Graduated summa cum laude from Harvard University"),
            event(1927, "Earned PhD from the University of Göttingen under Max Born"),
            event(1942, "Appointed scientific director of the Manhattan Project at Los Alamos"),
            event(1945, "First nuclear weapon successfully tested at Trinity site in New Mexico"),
            event(1954, "Security clearance revoked after controversial hearing"),
        ],
        "famous_works": [
            work("Born-Oppenheimer Approximation", 1927, "A foundational method in quantum chemistry for separating nuclear and electronic motion in molecules."),
            work("Oppenheimer-Snyder Model", 1939, "Theoretical prediction of gravitational collapse leading to what would later be called black holes."),
            work("Manhattan Project Leadership", 1945, "Directed the scientific effort that produced the first nuclear weapons at Los Alamos Laboratory."),
        ],
        "quotes": [
            quote("Now I am become Death, the destroyer of worlds.", "Quoting the Bhagavad Gita after the Trinity test, 1945"),
            quote("The physicists have known sin; and this is a knowledge which they cannot lose.", "Lecture at MIT, 1947"),
        ],
        "relations": [
            rel("niels-bohr", "influenced_by"),
            rel("max-born", "mentor"),
            rel("edward-teller", "colleague"),
            rel("hans-bethe", "colleague"),
            rel("richard-feynman", "colleague"),
        ],
    },
    {
        "id": "hans-bethe",
        "name": name_i18n("Hans Bethe", "ハンス・ベーテ"),
        "birth_year": 1906,
        "death_year": 2005,
        "countries": ["de", "us"],
        "fields": ["physics"],
        "overview": i18n("Hans Bethe was a German-American nuclear physicist who won the Nobel Prize in Physics in 1967 for his work on stellar nucleosynthesis. He explained the nuclear reactions that power the sun and stars, and also made major contributions to quantum electrodynamics and solid-state physics."),
        "early_life": i18n("Bethe was born in Strasbourg, then part of the German Empire, and studied physics at the University of Frankfurt and the University of Munich. He fled Nazi Germany in 1933 and eventually settled in the United States, joining Cornell University."),
        "impact": i18n("Bethe's theory of stellar nucleosynthesis explained the energy source of stars and became a cornerstone of astrophysics. He also played a key role in the Manhattan Project as head of the Theoretical Division and later became a prominent advocate for nuclear arms control."),
        "timeline": [
            event(1928, "Received PhD from the University of Munich under Arnold Sommerfeld"),
            event(1935, "Joined the faculty at Cornell University"),
            event(1939, "Published groundbreaking paper on energy production in stars"),
            event(1943, "Became head of the Theoretical Division at Los Alamos"),
            event(1967, "Awarded the Nobel Prize in Physics for stellar nucleosynthesis theory"),
        ],
        "famous_works": [
            work("Energy Production in Stars", 1939, "Identified the CNO cycle and proton-proton chain as the nuclear reactions powering stars."),
            work("Bethe Bible", 1936, "A comprehensive three-part review of nuclear physics that became the standard reference in the field."),
            work("Lamb Shift Calculation", 1947, "Provided the first successful theoretical explanation of the Lamb shift in hydrogen."),
        ],
        "quotes": [
            quote("If we fight a war and win it with H-bombs, what history will remember is not the ideals we were fighting for but the methods we used to accomplish them.", "Bulletin of the Atomic Scientists, 1950"),
            quote("I have sometimes been asked whether I would agree that the tragedy of the scientist is that he is able to bring about great advances in our knowledge, which mankind may then use for purposes of destruction.", "Nobel Lecture, 1967"),
        ],
        "relations": [
            rel("j-robert-oppenheimer", "colleague"),
            rel("richard-feynman", "mentor"),
            rel("edward-teller", "colleague"),
            rel("arnold-sommerfeld", "student"),
        ],
    },
    {
        "id": "lev-landau",
        "name": name_i18n("Lev Landau", "レフ・ランダウ"),
        "birth_year": 1908,
        "death_year": 1968,
        "countries": ["ru"],
        "fields": ["physics"],
        "overview": i18n("Lev Landau was a Soviet theoretical physicist who won the Nobel Prize in Physics in 1962 for his theory of superfluidity. He made fundamental contributions to nearly every area of theoretical physics, from condensed matter to quantum field theory and plasma physics."),
        "early_life": i18n("Landau was born in Baku, Azerbaijan, then part of the Russian Empire, to a family of engineers. He was a child prodigy who entered university at age 13 and completed his studies at Leningrad State University by age 19."),
        "impact": i18n("Landau's work on superfluidity and phase transitions transformed condensed matter physics. His ten-volume Course of Theoretical Physics, co-authored with Evgeny Lifshitz, remains one of the most influential and widely used textbook series in physics."),
        "timeline": [
            event(1927, "Graduated from Leningrad State University at age 19"),
            event(1929, "Traveled to Europe, meeting Bohr, Heisenberg, and Pauli"),
            event(1937, "Became head of the theoretical department at the Institute for Physical Problems in Moscow"),
            event(1941, "Published theory of superfluidity of helium-4"),
            event(1962, "Awarded the Nobel Prize in Physics for superfluidity theory"),
        ],
        "famous_works": [
            work("Theory of Superfluidity", 1941, "Explained the superfluid behavior of liquid helium-4 using the concept of quasiparticles."),
            work("Course of Theoretical Physics", 1938, "A monumental ten-volume textbook series covering all areas of theoretical physics, co-authored with Lifshitz."),
            work("Landau Theory of Phase Transitions", 1937, "A general phenomenological theory describing continuous phase transitions using an order parameter."),
        ],
        "quotes": [
            quote("A method is more important than a discovery, since the right method will lead to new and even more important discoveries.", "Attributed"),
            quote("Cosmologists are often in error, but never in doubt.", "Attributed remark"),
        ],
        "relations": [
            rel("niels-bohr", "influenced_by"),
            rel("pyotr-kapitsa", "colleague"),
            rel("werner-heisenberg", "influenced_by"),
            rel("andrei-sakharov", "colleague"),
        ],
    },
    {
        "id": "edward-teller",
        "name": name_i18n("Edward Teller", "エドワード・テラー"),
        "birth_year": 1908,
        "death_year": 2003,
        "countries": ["hu", "us"],
        "fields": ["physics"],
        "overview": i18n("Edward Teller was a Hungarian-American theoretical physicist known as the 'father of the hydrogen bomb.' He made important contributions to nuclear and molecular physics, spectroscopy, and surface physics."),
        "early_life": i18n("Teller was born in Budapest, Hungary, to a Jewish family. He studied in Germany under Werner Heisenberg and earned his PhD in physics from the University of Leipzig in 1930 before emigrating to the United States in 1935."),
        "impact": i18n("Teller was instrumental in the development of thermonuclear weapons and was a key advocate for a strong nuclear deterrent during the Cold War. His advocacy for the hydrogen bomb and his testimony against Oppenheimer made him a controversial figure in the scientific community."),
        "timeline": [
            event(1930, "Earned PhD from the University of Leipzig under Werner Heisenberg"),
            event(1935, "Emigrated to the United States and joined George Washington University"),
            event(1943, "Joined the Manhattan Project at Los Alamos"),
            event(1952, "First hydrogen bomb (Ivy Mike) successfully tested"),
            event(1954, "Testified against Oppenheimer at the security hearing"),
        ],
        "famous_works": [
            work("Teller-Ulam Design", 1951, "Co-invented the staged radiation implosion design that made thermonuclear weapons practical."),
            work("Jahn-Teller Effect", 1937, "Co-discovered the geometric distortion of non-linear molecular systems in certain electronic states."),
            work("Gamow-Teller Transitions", 1936, "Co-formulated selection rules for nuclear beta decay transitions."),
        ],
        "quotes": [
            quote("Two paradoxes are better than one; they may even suggest a solution.", "The Legacy of Hiroshima, 1962"),
            quote("The science of today is the technology of tomorrow.", "Attributed"),
        ],
        "relations": [
            rel("j-robert-oppenheimer", "rival"),
            rel("george-gamow", "collaborator"),
            rel("hans-bethe", "colleague"),
            rel("werner-heisenberg", "student"),
            rel("enrico-fermi", "colleague"),
        ],
    },
    {
        "id": "george-gamow",
        "name": name_i18n("George Gamow", "ジョージ・ガモフ"),
        "birth_year": 1904,
        "death_year": 1968,
        "countries": ["ua", "us"],
        "fields": ["physics"],
        "overview": i18n("George Gamow was a Ukrainian-American theoretical physicist and cosmologist who proposed the Big Bang nucleosynthesis theory. He also made important contributions to nuclear physics, molecular biology, and science popularization."),
        "early_life": i18n("Gamow was born in Odessa, then part of the Russian Empire, and studied at the University of Leningrad. He defected from the Soviet Union in 1933 and eventually settled in the United States, joining George Washington University."),
        "impact": i18n("Gamow's prediction of cosmic microwave background radiation and his work on Big Bang nucleosynthesis laid the foundations of modern cosmology. He was also a gifted science communicator whose popular books inspired generations of scientists."),
        "timeline": [
            event(1928, "Developed the theory of quantum tunneling to explain alpha decay"),
            event(1934, "Emigrated to the United States and joined George Washington University"),
            event(1948, "Published the Alpher-Bethe-Gamow paper on Big Bang nucleosynthesis"),
            event(1948, "Predicted the existence of cosmic microwave background radiation"),
            event(1954, "Proposed that the genetic code uses triplet codons"),
        ],
        "famous_works": [
            work("Alpha Decay and Quantum Tunneling", 1928, "First successful application of quantum mechanics to nuclear physics, explaining radioactive alpha decay through quantum tunneling."),
            work("Alpher-Bethe-Gamow Paper", 1948, "Proposed the theory of Big Bang nucleosynthesis explaining the origin of light elements in the early universe."),
            work("One Two Three... Infinity", 1947, "A classic popular science book exploring concepts in mathematics, biology, physics, and cosmology."),
        ],
        "quotes": [
            quote("There was a young fellow from Trinity / Who took the square root of infinity / But the number of digits / Gave him the fidgets / He dropped Math and took up Divinity.", "One Two Three... Infinity, 1947"),
            quote("If and when all the laws governing physical phenomena are finally discovered, and all the empirical constants occurring in these laws are finally expressed through the four independent basic constants, we will be able to say that physical science has reached its end.", "Mr Tompkins in Wonderland, 1940"),
        ],
        "relations": [
            rel("edward-teller", "collaborator"),
            rel("niels-bohr", "influenced_by"),
            rel("ralph-alpher", "mentor"),
            rel("alexander-friedmann", "student"),
        ],
    },
    {
        "id": "sin-itiro-tomonaga",
        "name": name_i18n("Sin-Itiro Tomonaga", "朝永振一郎"),
        "birth_year": 1906,
        "death_year": 1979,
        "countries": ["jp"],
        "fields": ["physics"],
        "overview": i18n("Sin-Itiro Tomonaga was a Japanese theoretical physicist who shared the 1965 Nobel Prize in Physics for his independent development of quantum electrodynamics. Working largely in isolation in wartime Japan, he developed a relativistically covariant formulation of QED."),
        "early_life": i18n("Tomonaga was born in Tokyo and grew up in Kyoto, where his father was a professor of philosophy. He studied at Kyoto Imperial University alongside Hideki Yukawa and later worked with Werner Heisenberg in Leipzig."),
        "impact": i18n("Tomonaga's renormalization technique in quantum electrodynamics, developed independently of Schwinger and Feynman, was crucial for making QED a consistent and predictive theory. He also mentored a generation of Japanese theoretical physicists."),
        "timeline": [
            event(1929, "Graduated from Kyoto Imperial University"),
            event(1937, "Worked with Werner Heisenberg at the University of Leipzig"),
            event(1943, "Published his covariant formulation of quantum electrodynamics"),
            event(1948, "Completed renormalization of QED independently"),
            event(1965, "Awarded the Nobel Prize in Physics jointly with Schwinger and Feynman"),
        ],
        "famous_works": [
            work("Super-Many-Time Theory", 1943, "A relativistically covariant formulation of quantum field theory using multiple time variables for each particle."),
            work("Renormalization of QED", 1948, "Independently developed the renormalization procedure to remove infinities from quantum electrodynamics calculations."),
        ],
        "quotes": [
            quote("There is no expedient to which a man will not resort to avoid the real labor of thinking.", "Attributed, paraphrasing Joshua Reynolds"),
        ],
        "relations": [
            rel("hideki-yukawa", "colleague"),
            rel("werner-heisenberg", "influenced_by"),
            rel("julian-schwinger", "colleague"),
            rel("richard-feynman", "colleague"),
        ],
    },
    {
        "id": "julian-schwinger",
        "name": name_i18n("Julian Schwinger", "ジュリアン・シュウィンガー"),
        "birth_year": 1918,
        "death_year": 1994,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Julian Schwinger was an American theoretical physicist who shared the 1965 Nobel Prize in Physics for his contributions to quantum electrodynamics. He developed a rigorous, operator-based formulation of QED and made fundamental contributions to many areas of theoretical physics."),
        "early_life": i18n("Schwinger was born in New York City and showed extraordinary mathematical ability from an early age. He published his first physics paper at age 16 and earned his PhD from Columbia University at age 21 under Isidor Isaac Rabi."),
        "impact": i18n("Schwinger's formulation of quantum electrodynamics provided the most rigorous mathematical framework for the theory and influenced generations of theoretical physicists. His development of source theory and effective action methods had lasting impact on quantum field theory."),
        "timeline": [
            event(1934, "Published first physics paper at age 16"),
            event(1939, "Earned PhD from Columbia University under I.I. Rabi"),
            event(1947, "Calculated the anomalous magnetic moment of the electron"),
            event(1948, "Presented his formulation of quantum electrodynamics"),
            event(1965, "Awarded the Nobel Prize in Physics jointly with Tomonaga and Feynman"),
        ],
        "famous_works": [
            work("Anomalous Magnetic Moment of the Electron", 1948, "First calculation of the electron's anomalous magnetic moment, confirming QED predictions to extraordinary precision."),
            work("Schwinger-Dyson Equations", 1951, "Derived the fundamental equations of motion for quantum field theories relating Green's functions."),
            work("Schwinger Effect", 1951, "Predicted the creation of electron-positron pairs from vacuum in the presence of strong electric fields."),
        ],
        "quotes": [
            quote("If you can't join 'em, beat 'em.", "On his independent approach to QED, attributed"),
            quote("Is the purpose of theoretical physics to be no more than a cataloging of all the things that can happen when particles interact with each other and separate?", "Nobel Lecture, 1965"),
        ],
        "relations": [
            rel("richard-feynman", "rival"),
            rel("sin-itiro-tomonaga", "colleague"),
            rel("freeman-dyson", "colleague"),
            rel("isidor-isaac-rabi", "student"),
        ],
    },
    {
        "id": "richard-feynman",
        "name": name_i18n("Richard Feynman", "リチャード・ファインマン"),
        "birth_year": 1918,
        "death_year": 1988,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Richard Feynman was an American theoretical physicist who shared the 1965 Nobel Prize in Physics for his contributions to quantum electrodynamics. He developed the path integral formulation of quantum mechanics, Feynman diagrams, and the parton model, and was renowned as an exceptional teacher and science communicator."),
        "early_life": i18n("Feynman was born in Queens, New York City, and showed an early aptitude for mathematics and science. He earned his bachelor's degree from MIT and his PhD from Princeton University under John Archibald Wheeler."),
        "impact": i18n("Feynman's path integral formulation and diagrammatic techniques revolutionized quantum field theory and became standard tools in theoretical physics. His Feynman Lectures on Physics became one of the most celebrated physics textbooks, and his popular books inspired countless people to appreciate science."),
        "timeline": [
            event(1942, "Earned PhD from Princeton University under John Archibald Wheeler"),
            event(1943, "Joined the Manhattan Project at Los Alamos"),
            event(1948, "Developed the path integral formulation and Feynman diagrams for QED"),
            event(1965, "Awarded the Nobel Prize in Physics jointly with Tomonaga and Schwinger"),
            event(1986, "Investigated the Space Shuttle Challenger disaster on the Rogers Commission"),
        ],
        "famous_works": [
            work("Feynman Diagrams", 1948, "Invented a pictorial representation of particle interactions that became the universal language of quantum field theory."),
            work("The Feynman Lectures on Physics", 1964, "A three-volume introductory physics textbook based on his legendary Caltech lectures, widely regarded as a masterpiece of science education."),
            work("Surely You're Joking, Mr. Feynman!", 1985, "A bestselling collection of autobiographical anecdotes that captured his adventurous spirit and love of science."),
        ],
        "quotes": [
            quote("I think I can safely say that nobody understands quantum mechanics.", "The Character of Physical Law, 1965"),
            quote("What I cannot create, I do not understand.", "Written on his blackboard at the time of his death, 1988"),
            quote("The first principle is that you must not fool yourself — and you are the easiest person to fool.", "Caltech commencement address, 1974"),
        ],
        "relations": [
            rel("julian-schwinger", "rival"),
            rel("john-wheeler", "student"),
            rel("hans-bethe", "influenced_by"),
            rel("freeman-dyson", "colleague"),
            rel("murray-gell-mann", "colleague"),
        ],
    },
    {
        "id": "john-bardeen",
        "name": name_i18n("John Bardeen", "ジョン・バーディーン"),
        "birth_year": 1908,
        "death_year": 1991,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("John Bardeen was an American physicist and the only person to win the Nobel Prize in Physics twice: in 1956 for the invention of the transistor and in 1972 for the BCS theory of superconductivity. His work transformed both electronics and condensed matter physics."),
        "early_life": i18n("Bardeen was born in Madison, Wisconsin, and was a child prodigy who graduated from high school at age 15. He studied electrical engineering at the University of Wisconsin and later earned his PhD in mathematical physics from Princeton University."),
        "impact": i18n("Bardeen's co-invention of the transistor launched the semiconductor revolution that underpins modern electronics and computing. His BCS theory provided the first microscopic explanation of superconductivity, solving one of the great puzzles of 20th-century physics."),
        "timeline": [
            event(1936, "Earned PhD from Princeton University"),
            event(1947, "Co-invented the point-contact transistor at Bell Labs with Brattain"),
            event(1951, "Joined the University of Illinois at Urbana-Champaign"),
            event(1956, "Awarded the Nobel Prize in Physics for the transistor"),
            event(1957, "Published the BCS theory of superconductivity with Cooper and Schrieffer"),
            event(1972, "Awarded a second Nobel Prize in Physics for BCS theory"),
        ],
        "famous_works": [
            work("Invention of the Transistor", 1947, "Co-invented the point-contact transistor at Bell Labs, launching the semiconductor revolution."),
            work("BCS Theory of Superconductivity", 1957, "Developed a comprehensive microscopic theory explaining superconductivity through Cooper pair formation."),
        ],
        "quotes": [
            quote("The combined results of several people working together is often much more effective than could be that of an individual scientist working alone.", "Nobel Lecture, 1956"),
        ],
        "relations": [
            rel("william-shockley", "colleague"),
            rel("walter-brattain", "collaborator"),
            rel("leon-cooper", "collaborator"),
            rel("eugene-wigner", "influenced_by"),
        ],
    },
    {
        "id": "william-shockley",
        "name": name_i18n("William Shockley", "ウィリアム・ショックレー"),
        "birth_year": 1910,
        "death_year": 1989,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("William Shockley was an American physicist who shared the 1956 Nobel Prize in Physics for the invention of the transistor. He later invented the junction transistor, which became the basis for modern semiconductor technology."),
        "early_life": i18n("Shockley was born in London to American parents and grew up in Palo Alto, California. He earned his PhD from MIT in 1936 and joined Bell Telephone Laboratories, where he would lead the semiconductor research group."),
        "impact": i18n("Shockley's invention of the junction transistor and his founding of Shockley Semiconductor Laboratory in Silicon Valley helped create the modern electronics industry. His laboratory produced many of the founders of Silicon Valley's major semiconductor companies."),
        "timeline": [
            event(1936, "Earned PhD from MIT"),
            event(1947, "Co-received credit for the transistor invention at Bell Labs"),
            event(1948, "Invented the junction transistor"),
            event(1956, "Awarded the Nobel Prize in Physics for the transistor"),
            event(1956, "Founded Shockley Semiconductor Laboratory in Mountain View, California"),
        ],
        "famous_works": [
            work("Junction Transistor", 1948, "Invented the bipolar junction transistor, which became the dominant transistor type for decades."),
            work("Electrons and Holes in Semiconductors", 1950, "Authored the definitive textbook on semiconductor physics that trained a generation of engineers."),
        ],
        "quotes": [
            quote("The will to think is a factor in the process of discovery.", "Attributed"),
        ],
        "relations": [
            rel("john-bardeen", "colleague"),
            rel("walter-brattain", "colleague"),
            rel("robert-noyce", "mentor"),
        ],
    },
    {
        "id": "john-wheeler",
        "name": name_i18n("John Archibald Wheeler", "ジョン・アーチボルド・ホイーラー"),
        "birth_year": 1911,
        "death_year": 2008,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("John Archibald Wheeler was an American theoretical physicist who made major contributions to general relativity and quantum gravity. He coined the terms 'black hole,' 'wormhole,' and 'quantum foam,' and mentored many of the most influential physicists of the 20th century."),
        "early_life": i18n("Wheeler was born in Jacksonville, Florida, and earned his PhD from Johns Hopkins University at age 21. He studied with Niels Bohr in Copenhagen and collaborated with Bohr on the liquid drop model of nuclear fission."),
        "impact": i18n("Wheeler revitalized the study of general relativity in the United States and trained a generation of leading physicists including Richard Feynman, Kip Thorne, and Hugh Everett. His conceptual insights into the nature of spacetime and quantum mechanics continue to inspire foundational physics research."),
        "timeline": [
            event(1933, "Earned PhD from Johns Hopkins University"),
            event(1939, "Co-authored the Bohr-Wheeler theory of nuclear fission"),
            event(1955, "Developed the concept of quantum foam and spacetime geometry"),
            event(1957, "Supervised Hugh Everett's many-worlds interpretation thesis"),
            event(1967, "Coined the term 'black hole' at a conference"),
        ],
        "famous_works": [
            work("Bohr-Wheeler Theory of Fission", 1939, "Co-developed with Niels Bohr the liquid drop model explaining nuclear fission."),
            work("Geometrodynamics", 1957, "Developed the program of describing physics in terms of the geometry of spacetime, introducing quantum foam."),
            work("Geons, Black Holes, and Quantum Foam", 1998, "An autobiography detailing his life and contributions to physics."),
        ],
        "quotes": [
            quote("Time is what prevents everything from happening at once.", "Attributed"),
            quote("We live on an island surrounded by a sea of ignorance. As our island of knowledge grows, so does the shore of our ignorance.", "Scientific American, 1992"),
        ],
        "relations": [
            rel("richard-feynman", "mentor"),
            rel("niels-bohr", "collaborator"),
            rel("albert-einstein", "colleague"),
            rel("kip-thorne", "mentor"),
        ],
    },
    {
        "id": "freeman-dyson",
        "name": name_i18n("Freeman Dyson", "フリーマン・ダイソン"),
        "birth_year": 1923,
        "death_year": 2020,
        "countries": ["gb", "us"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Freeman Dyson was a British-American theoretical physicist and mathematician who unified the competing formulations of quantum electrodynamics by Schwinger, Tomonaga, and Feynman. He made wide-ranging contributions to physics, mathematics, and futuristic engineering concepts."),
        "early_life": i18n("Dyson was born in Crowthorne, England, and studied mathematics at the University of Cambridge. He moved to the United States in 1947 to study at Cornell University, where he worked with Hans Bethe and Richard Feynman."),
        "impact": i18n("Dyson's proof that the Feynman and Schwinger-Tomonaga approaches to QED were equivalent was a landmark in theoretical physics. His concept of the Dyson sphere became iconic in science fiction and the search for extraterrestrial intelligence."),
        "timeline": [
            event(1945, "Graduated from the University of Cambridge in mathematics"),
            event(1949, "Published the proof unifying QED formulations by Feynman, Schwinger, and Tomonaga"),
            event(1953, "Joined the Institute for Advanced Study in Princeton permanently"),
            event(1960, "Proposed the concept of the Dyson sphere"),
            event(2000, "Awarded the Templeton Prize for contributions bridging science and religion"),
        ],
        "famous_works": [
            work("Unification of QED Formulations", 1949, "Proved the mathematical equivalence of Feynman's and Schwinger-Tomonaga's approaches to quantum electrodynamics."),
            work("Dyson Sphere Concept", 1960, "Proposed a megastructure enclosing a star to capture its energy output, stimulating SETI research."),
            work("Disturbing the Universe", 1979, "An autobiographical work blending science, ethics, and reflections on nuclear weapons and space exploration."),
        ],
        "quotes": [
            quote("It is better to be wrong than to be vague.", "Attributed"),
            quote("God is what mind becomes when it has passed beyond the scale of our comprehension.", "Infinite in All Directions, 1988"),
        ],
        "relations": [
            rel("richard-feynman", "colleague"),
            rel("julian-schwinger", "colleague"),
            rel("hans-bethe", "influenced_by"),
            rel("sin-itiro-tomonaga", "colleague"),
        ],
    },
    {
        "id": "pyotr-kapitsa",
        "name": name_i18n("Pyotr Kapitsa", "ピョートル・カピッツァ"),
        "birth_year": 1894,
        "death_year": 1984,
        "countries": ["ru"],
        "fields": ["physics"],
        "overview": i18n("Pyotr Kapitsa was a Soviet physicist who won the 1978 Nobel Prize in Physics for his fundamental discoveries in low-temperature physics. He discovered the superfluidity of liquid helium and made pioneering contributions to high-magnetic-field research."),
        "early_life": i18n("Kapitsa was born in Kronstadt, Russia, and studied at the Petrograd Polytechnic Institute. He worked in Ernest Rutherford's Cavendish Laboratory at Cambridge from 1921 to 1934, before being detained in the Soviet Union during a visit."),
        "impact": i18n("Kapitsa's discovery of superfluidity opened a major new field in condensed matter physics. He also founded the Institute for Physical Problems in Moscow, which became one of the leading physics research centers in the world."),
        "timeline": [
            event(1921, "Began working at the Cavendish Laboratory under Ernest Rutherford"),
            event(1934, "Detained in the Soviet Union and prevented from returning to Cambridge"),
            event(1937, "Appointed director of the newly founded Institute for Physical Problems"),
            event(1938, "Discovered superfluidity of liquid helium"),
            event(1978, "Awarded the Nobel Prize in Physics for low-temperature physics research"),
        ],
        "famous_works": [
            work("Discovery of Superfluidity", 1938, "Discovered that liquid helium-4 flows without friction below 2.17 K, a phenomenon called superfluidity."),
            work("High-Magnetic-Field Research", 1924, "Pioneered methods for producing very strong magnetic fields for experimental physics."),
        ],
        "quotes": [
            quote("Theory is a good thing but a good experiment lasts forever.", "Attributed"),
            quote("The most important thing in science is not so much to obtain new facts as to discover new ways of thinking about them.", "Attributed"),
        ],
        "relations": [
            rel("ernest-rutherford", "influenced_by"),
            rel("lev-landau", "colleague"),
            rel("niels-bohr", "colleague"),
        ],
    },
    {
        "id": "andrei-sakharov",
        "name": name_i18n("Andrei Sakharov", "アンドレイ・サハロフ"),
        "birth_year": 1921,
        "death_year": 1989,
        "countries": ["ru"],
        "fields": ["physics"],
        "overview": i18n("Andrei Sakharov was a Soviet nuclear physicist who played a key role in developing the Soviet hydrogen bomb and later became a prominent human rights activist. He was awarded the Nobel Peace Prize in 1975 for his courageous advocacy for disarmament and civil liberties."),
        "early_life": i18n("Sakharov was born in Moscow to a family of intellectuals and studied physics at Moscow State University. During World War II he worked as an engineer, and afterwards joined the Soviet nuclear weapons program under Igor Tamm."),
        "impact": i18n("Sakharov's contributions to the Soviet thermonuclear weapons program were crucial to the Cold War balance of power. His later transformation into a dissident and human rights advocate made him a symbol of intellectual courage and moral integrity worldwide."),
        "timeline": [
            event(1948, "Joined the Soviet thermonuclear weapons program"),
            event(1953, "Contributed to the successful test of the first Soviet hydrogen bomb"),
            event(1968, "Published 'Reflections on Progress, Peaceful Coexistence, and Intellectual Freedom'"),
            event(1975, "Awarded the Nobel Peace Prize for human rights advocacy"),
            event(1980, "Exiled to Gorky for protesting the Soviet invasion of Afghanistan"),
        ],
        "famous_works": [
            work("Sakharov's Third Idea (Tokamak concept)", 1951, "Co-proposed the tokamak design for controlled thermonuclear fusion using magnetic confinement."),
            work("Reflections on Progress, Peaceful Coexistence, and Intellectual Freedom", 1968, "A landmark essay calling for nuclear disarmament, human rights, and intellectual freedom."),
            work("Baryogenesis Conditions", 1967, "Proposed three conditions necessary to explain the matter-antimatter asymmetry of the universe."),
        ],
        "quotes": [
            quote("I am no volunteer; I was simply doing what I had to do.", "Memoirs, 1990"),
            quote("A country that does not respect the rights of its own citizens will not respect the rights of its neighbors.", "Attributed"),
        ],
        "relations": [
            rel("igor-tamm", "mentor"),
            rel("edward-teller", "rival"),
            rel("lev-landau", "colleague"),
            rel("j-robert-oppenheimer", "colleague"),
        ],
    },
    {
        "id": "maria-goeppert-mayer",
        "name": name_i18n("Maria Goeppert Mayer", "マリア・ゲッパート＝メイヤー"),
        "birth_year": 1906,
        "death_year": 1972,
        "countries": ["de", "us"],
        "fields": ["physics"],
        "overview": i18n("Maria Goeppert Mayer was a German-American theoretical physicist who won the 1963 Nobel Prize in Physics for proposing the nuclear shell model. She was only the second woman to win a Nobel Prize in Physics, after Marie Curie."),
        "early_life": i18n("Goeppert Mayer was born in Kattowitz, Germany (now Katowice, Poland), and studied at the University of Göttingen, where she earned her PhD under Max Born. She married the American chemist Joseph Mayer and moved to the United States in 1930."),
        "impact": i18n("Goeppert Mayer's nuclear shell model explained why certain numbers of nucleons (magic numbers) result in particularly stable atomic nuclei. Her work provided a fundamental framework for understanding nuclear structure and remains a cornerstone of nuclear physics."),
        "timeline": [
            event(1930, "Earned PhD from the University of Göttingen under Max Born"),
            event(1930, "Moved to the United States with her husband Joseph Mayer"),
            event(1948, "Proposed the nuclear shell model with spin-orbit coupling"),
            event(1950, "Published 'Elementary Theory of Nuclear Shell Structure' with Jensen"),
            event(1963, "Awarded the Nobel Prize in Physics jointly with Jensen and Wigner"),
        ],
        "famous_works": [
            work("Nuclear Shell Model", 1948, "Proposed a model explaining the stability of nuclei with magic numbers through spin-orbit coupling of nucleons."),
            work("Göppert-Mayer Theory of Two-Photon Absorption", 1931, "Predicted in her doctoral thesis that atoms can absorb two photons simultaneously, confirmed decades later by lasers."),
            work("Elementary Theory of Nuclear Shell Structure", 1955, "Co-authored the definitive book on the nuclear shell model with J. Hans D. Jensen."),
        ],
        "quotes": [
            quote("Mathematics began to seem too much like puzzle solving. Physics is puzzle solving, too, but of puzzles created by nature, not by the mind of man.", "Attributed"),
        ],
        "relations": [
            rel("max-born", "student"),
            rel("j-hans-d-jensen", "collaborator"),
            rel("enrico-fermi", "colleague"),
            rel("eugene-wigner", "colleague"),
        ],
    },
    {
        "id": "chien-shiung-wu",
        "name": name_i18n("Chien-Shiung Wu", "呉健雄"),
        "birth_year": 1912,
        "death_year": 1997,
        "countries": ["cn", "us"],
        "fields": ["physics"],
        "overview": i18n("Chien-Shiung Wu was a Chinese-American experimental physicist known for conducting the Wu experiment, which proved that parity is not conserved in weak interactions. Often called the 'First Lady of Physics,' she made fundamental contributions to nuclear and particle physics."),
        "early_life": i18n("Wu was born in Liuhe, Jiangsu province, China, and studied physics at National Central University in Nanjing. She moved to the United States in 1936 and earned her PhD from the University of California, Berkeley under Ernest Lawrence."),
        "impact": i18n("Wu's 1956 experiment demonstrating parity violation in beta decay overturned one of physics' fundamental assumptions and earned the Nobel Prize for the theorists Lee and Yang, though Wu herself was controversially excluded. She became a powerful advocate for gender equality in science."),
        "timeline": [
            event(1940, "Earned PhD from the University of California, Berkeley"),
            event(1944, "Joined the Manhattan Project, working on uranium enrichment"),
            event(1956, "Conducted the Wu experiment proving parity violation in weak interactions"),
            event(1957, "Lee and Yang awarded Nobel Prize for parity violation theory; Wu controversially excluded"),
            event(1975, "Became the first woman president of the American Physical Society"),
        ],
        "famous_works": [
            work("Wu Experiment", 1956, "Experimentally demonstrated that parity is not conserved in weak interactions using cobalt-60 beta decay."),
            work("Beta Decay Research", 1950, "Confirmed Enrico Fermi's theory of beta decay through precise experimental measurements."),
            work("Beta Decay", 1965, "Authored the definitive textbook on beta decay physics."),
        ],
        "quotes": [
            quote("There is only one thing worse than coming home from the lab to a sink full of dirty dishes, and that is not going to the lab at all.", "Attributed"),
            quote("It is shameful that there are so few women in science... In China there are many women in physics. There is a misconception in America that women scientists are all dowdy spinsters. This is the fault of men.", "Newsweek interview, 1963"),
        ],
        "relations": [
            rel("tsung-dao-lee", "collaborator"),
            rel("chen-ning-yang", "colleague"),
            rel("enrico-fermi", "influenced_by"),
            rel("ernest-lawrence", "student"),
        ],
    },
    {
        "id": "tsung-dao-lee",
        "name": name_i18n("Tsung-Dao Lee", "李政道"),
        "birth_year": 1926,
        "death_year": 2024,
        "countries": ["cn", "us"],
        "fields": ["physics"],
        "overview": i18n("Tsung-Dao Lee was a Chinese-American physicist who shared the 1957 Nobel Prize in Physics with Chen-Ning Yang for their theoretical prediction that parity is not conserved in weak interactions. He was one of the youngest Nobel laureates in physics."),
        "early_life": i18n("Lee was born in Shanghai, China, and studied at the National Che Kiang University and Southwest Associated University during wartime. He moved to the United States in 1946 and earned his PhD from the University of Chicago under Enrico Fermi."),
        "impact": i18n("Lee and Yang's prediction of parity violation, confirmed by Wu's experiment, fundamentally changed our understanding of the laws of physics and the nature of symmetry. Lee also made important contributions to statistical mechanics, astrophysics, and field theory."),
        "timeline": [
            event(1950, "Earned PhD from the University of Chicago under Enrico Fermi"),
            event(1953, "Became the youngest full professor at Columbia University at age 29"),
            event(1956, "Co-proposed parity violation in weak interactions with Chen-Ning Yang"),
            event(1957, "Awarded the Nobel Prize in Physics at age 30"),
            event(1997, "Established the Chun-Tsung Endowment to support young Chinese scientists"),
        ],
        "famous_works": [
            work("Parity Violation Theory", 1956, "Co-proposed with Yang that the weak interaction does not conserve parity, a fundamental symmetry of nature."),
            work("Lee Model", 1954, "Developed a solvable quantum field theory model that illuminated renormalization and the structure of field theories."),
        ],
        "quotes": [
            quote("Since the beginning of physics, symmetry considerations have provided us with an extremely powerful and useful tool in our effort to understand nature.", "Nobel Lecture, 1957"),
        ],
        "relations": [
            rel("chen-ning-yang", "collaborator"),
            rel("chien-shiung-wu", "collaborator"),
            rel("enrico-fermi", "student"),
            rel("j-robert-oppenheimer", "colleague"),
        ],
    },
    {
        "id": "chen-ning-yang",
        "name": name_i18n("Chen-Ning Yang", "楊振寧"),
        "birth_year": 1922,
        "death_year": None,
        "countries": ["cn", "us"],
        "fields": ["physics"],
        "overview": i18n("Chen-Ning Yang is a Chinese-American theoretical physicist who shared the 1957 Nobel Prize in Physics for the prediction of parity violation. He is also renowned for the Yang-Mills theory, which became the foundation of the Standard Model of particle physics."),
        "early_life": i18n("Yang was born in Hefei, Anhui, China, and studied at the National Southwest Associated University and Tsinghua University. He moved to the United States in 1945 and earned his PhD from the University of Chicago under Edward Teller."),
        "impact": i18n("Yang's contributions to physics are among the most profound of the 20th century. The Yang-Mills gauge theory provides the mathematical framework for the Standard Model, describing the strong, weak, and electromagnetic interactions that govern all known fundamental particles."),
        "timeline": [
            event(1948, "Earned PhD from the University of Chicago"),
            event(1954, "Published Yang-Mills gauge theory with Robert Mills"),
            event(1956, "Co-proposed parity violation in weak interactions with T.D. Lee"),
            event(1957, "Awarded the Nobel Prize in Physics at age 34"),
            event(1966, "Joined Stony Brook University as Albert Einstein Professor of Physics"),
        ],
        "famous_works": [
            work("Yang-Mills Theory", 1954, "Co-developed with Robert Mills a non-abelian gauge theory that became the mathematical foundation of the Standard Model."),
            work("Parity Violation Theory", 1956, "Co-proposed with Lee that parity symmetry is violated in weak interactions."),
            work("Yang-Baxter Equation", 1967, "Derived an equation in statistical mechanics that became fundamental in mathematical physics and knot theory."),
        ],
        "quotes": [
            quote("In 1954 we felt that a beautiful principle must have some realization in nature. We did not know what it would be.", "Selected Papers 1945-1980 with Commentary, 1983"),
            quote("Symmetry dictates interaction.", "Attributed"),
        ],
        "relations": [
            rel("tsung-dao-lee", "collaborator"),
            rel("robert-mills", "collaborator"),
            rel("edward-teller", "student"),
            rel("enrico-fermi", "influenced_by"),
        ],
    },
    {
        "id": "murray-gell-mann",
        "name": name_i18n("Murray Gell-Mann", "マレー・ゲルマン"),
        "birth_year": 1929,
        "death_year": 2019,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Murray Gell-Mann was an American theoretical physicist who won the 1969 Nobel Prize in Physics for his classification of subatomic particles and the discovery of quarks. He introduced the concept of strangeness and developed the Eightfold Way classification scheme."),
        "early_life": i18n("Gell-Mann was born in New York City to a family of Jewish immigrants from Austria-Hungary. A child prodigy who entered Yale University at age 15, he earned his PhD from MIT at age 21 under Victor Weisskopf."),
        "impact": i18n("Gell-Mann's quark model revolutionized our understanding of the fundamental constituents of matter and led directly to quantum chromodynamics, the theory of the strong force. His work provided the foundation for the Standard Model of particle physics."),
        "timeline": [
            event(1953, "Introduced the concept of strangeness to explain particle decay patterns"),
            event(1955, "Joined Caltech, where he spent most of his career"),
            event(1961, "Proposed the Eightfold Way classification of hadrons"),
            event(1964, "Proposed the quark model of hadrons"),
            event(1969, "Awarded the Nobel Prize in Physics for particle classification"),
        ],
        "famous_works": [
            work("Quark Model", 1964, "Proposed that hadrons are composed of more fundamental particles called quarks, which come in different flavors."),
            work("Eightfold Way", 1961, "Developed a classification scheme for hadrons based on SU(3) symmetry that predicted the existence of new particles."),
            work("The Quark and the Jaguar", 1994, "A popular science book exploring the relationship between the simple and the complex in nature."),
        ],
        "quotes": [
            quote("Think how hard physics would be if particles could think.", "Attributed"),
            quote("If I have seen further than others, it is by tripping over the mistakes of great men.", "Attributed, a play on Newton's famous quote"),
        ],
        "relations": [
            rel("richard-feynman", "rival"),
            rel("george-zweig", "colleague"),
            rel("victor-weisskopf", "student"),
            rel("sheldon-glashow", "colleague"),
        ],
    },
    {
        "id": "abdus-salam",
        "name": name_i18n("Abdus Salam", "アブドゥス・サラム"),
        "birth_year": 1926,
        "death_year": 1996,
        "countries": ["pk"],
        "fields": ["physics"],
        "overview": i18n("Abdus Salam was a Pakistani theoretical physicist who shared the 1979 Nobel Prize in Physics for the electroweak unification theory. He was the first Pakistani and the first Muslim to receive a Nobel Prize in science."),
        "early_life": i18n("Salam was born in Jhang, Punjab, in British India (now Pakistan), to a modest family. He showed extraordinary academic talent from an early age and earned his PhD from the University of Cambridge in 1951."),
        "impact": i18n("Salam's electroweak theory, developed independently and in parallel with Sheldon Glashow and Steven Weinberg, unified the electromagnetic and weak nuclear forces into a single framework. He also founded the International Centre for Theoretical Physics in Trieste to support scientists from developing countries."),
        "timeline": [
            event(1951, "Earned PhD from the University of Cambridge"),
            event(1957, "Became the youngest Fellow of the Royal Society at age 29"),
            event(1964, "Founded the International Centre for Theoretical Physics in Trieste"),
            event(1968, "Proposed the electroweak unification theory"),
            event(1979, "Awarded the Nobel Prize in Physics jointly with Glashow and Weinberg"),
        ],
        "famous_works": [
            work("Electroweak Unification Theory", 1968, "Independently developed the theory unifying electromagnetic and weak nuclear forces into a single gauge theory."),
            work("Pati-Salam Model", 1974, "Co-proposed a grand unified theory that treats leptons as a fourth color of quarks."),
            work("International Centre for Theoretical Physics", 1964, "Founded the ICTP in Trieste to provide research opportunities for physicists from developing nations."),
        ],
        "quotes": [
            quote("Scientific thought is the common heritage of mankind.", "Nobel Banquet Speech, 1979"),
            quote("The creation of physics is the shared heritage of all mankind. East and West, North and South have equally participated in it.", "Ideals and Realities, 1984"),
        ],
        "relations": [
            rel("steven-weinberg", "collaborator"),
            rel("sheldon-glashow", "colleague"),
            rel("paul-dirac", "influenced_by"),
            rel("jogesh-pati", "collaborator"),
        ],
    },
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for person in PEOPLE:
        filepath = os.path.join(OUTPUT_DIR, f"{person['id']}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(person, f, ensure_ascii=False, indent=2)
        print(f"Created: {filepath}")
    print(f"\nTotal files generated: {len(PEOPLE)}")


if __name__ == "__main__":
    main()
