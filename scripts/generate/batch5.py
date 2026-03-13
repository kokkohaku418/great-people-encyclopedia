#!/usr/bin/env python3
"""Batch 5: Generate 20 physicist JSON files (Late 20th Century to present + historical fill)."""

import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "people")


def i18n(en="", ja=""):
    return {"en": en, "es": "", "pt": "", "fr": "", "de": "", "zh": "", "hi": "", "ar": "", "id": "", "ja": ja}


def name_i18n(en, ja):
    return {"en": en, "es": "", "pt": "", "fr": "", "de": "", "zh": "", "hi": "", "ar": "", "id": "", "ja": ja}


PEOPLE = [
    {
        "id": "sheldon-glashow",
        "name": name_i18n("Sheldon Glashow", "シェルドン・グラショー"),
        "birth_year": 1932,
        "death_year": None,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Sheldon Glashow is an American theoretical physicist who made foundational contributions to the electroweak unification of the electromagnetic and weak nuclear forces. He shared the 1979 Nobel Prize in Physics with Abdus Salam and Steven Weinberg for this work."),
        "early_life": i18n("Glashow was born in New York City to immigrant parents from Russia. He attended the Bronx High School of Science alongside Steven Weinberg and went on to earn his Ph.D. from Harvard University under Julian Schwinger."),
        "impact": i18n("Glashow's proposal of a unified electroweak theory laid the groundwork for the Standard Model of particle physics. His work on the charm quark mechanism, known as the GIM mechanism, resolved key theoretical inconsistencies and predicted the existence of the charm quark before its experimental discovery."),
        "timeline": [
            {"year": 1932, "event": i18n("Born in New York City, United States")},
            {"year": 1961, "event": i18n("Proposed the electroweak unification incorporating the SU(2) x U(1) gauge structure")},
            {"year": 1970, "event": i18n("Co-proposed the GIM mechanism predicting the charm quark")},
            {"year": 1974, "event": i18n("Charm quark experimentally confirmed at Brookhaven and SLAC")},
            {"year": 1979, "event": i18n("Awarded the Nobel Prize in Physics for electroweak theory")},
        ],
        "famous_works": [
            {"title": i18n("Partial-symmetries of weak interactions"), "year": 1961, "description": i18n("Landmark paper proposing a gauge theory unifying electromagnetic and weak interactions, introducing the SU(2) x U(1) symmetry group.")},
            {"title": i18n("Weak Interactions with Lepton-Hadron Symmetry (GIM mechanism)"), "year": 1970, "description": i18n("Co-authored paper introducing the GIM mechanism, which predicted the charm quark and resolved anomalies in weak interaction theory.")},
        ],
        "quotes": [
            {"text": i18n("Teaching and research are complementary, not competitive, parsing of time."), "source": "Interview, Harvard University"},
        ],
        "relations": [
            {"person": "steven-weinberg", "type": "collaborator"},
            {"person": "abdus-salam", "type": "collaborator"},
            {"person": "julian-schwinger", "type": "mentor"},
        ],
    },
    {
        "id": "steven-weinberg",
        "name": name_i18n("Steven Weinberg", "スティーヴン・ワインバーグ"),
        "birth_year": 1933,
        "death_year": 2021,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Steven Weinberg was an American theoretical physicist who unified the electromagnetic and weak nuclear forces into the electroweak interaction. He shared the 1979 Nobel Prize in Physics and was considered one of the most influential physicists of the late 20th century."),
        "early_life": i18n("Weinberg was born in New York City and attended the Bronx High School of Science alongside Sheldon Glashow. He earned his Ph.D. from Princeton University and held positions at Berkeley, MIT, Harvard, and the University of Texas at Austin."),
        "impact": i18n("Weinberg's electroweak unification became a cornerstone of the Standard Model of particle physics. His textbooks on quantum field theory and cosmology became standard references, and he was a prominent public voice for science, writing extensively for general audiences."),
        "timeline": [
            {"year": 1933, "event": i18n("Born in New York City, United States")},
            {"year": 1967, "event": i18n("Published 'A Model of Leptons' unifying electromagnetic and weak forces")},
            {"year": 1979, "event": i18n("Awarded the Nobel Prize in Physics")},
            {"year": 1995, "event": i18n("Published 'The Quantum Theory of Fields,' a definitive textbook series")},
            {"year": 2021, "event": i18n("Died in Austin, Texas at age 88")},
        ],
        "famous_works": [
            {"title": i18n("A Model of Leptons"), "year": 1967, "description": i18n("Seminal paper presenting the electroweak unification, incorporating the Higgs mechanism to give mass to the W and Z bosons.")},
            {"title": i18n("The First Three Minutes"), "year": 1977, "description": i18n("Popular science book explaining the Big Bang theory and the first moments of the universe to a general audience.")},
            {"title": i18n("The Quantum Theory of Fields"), "year": 1995, "description": i18n("Comprehensive three-volume textbook on quantum field theory that became a standard graduate reference.")},
        ],
        "quotes": [
            {"text": i18n("The effort to understand the universe is one of the very few things that lifts human life a little above the level of farce, and gives it some of the grace of tragedy."), "source": "The First Three Minutes (1977)"},
            {"text": i18n("The more the universe seems comprehensible, the more it also seems pointless."), "source": "The First Three Minutes (1977)"},
        ],
        "relations": [
            {"person": "sheldon-glashow", "type": "collaborator"},
            {"person": "abdus-salam", "type": "collaborator"},
            {"person": "peter-higgs", "type": "colleague"},
        ],
    },
    {
        "id": "peter-higgs",
        "name": name_i18n("Peter Higgs", "ピーター・ヒッグス"),
        "birth_year": 1929,
        "death_year": 2024,
        "countries": ["gb"],
        "fields": ["physics"],
        "overview": i18n("Peter Higgs was a British theoretical physicist who proposed the mechanism of spontaneous symmetry breaking in gauge theories, predicting the existence of a massive scalar boson. The discovery of the Higgs boson at CERN in 2012 confirmed his theory, and he was awarded the 2013 Nobel Prize in Physics."),
        "early_life": i18n("Higgs was born in Newcastle upon Tyne and grew up in Bristol. He studied at King's College London, earning his Ph.D. in 1954, and spent most of his academic career at the University of Edinburgh."),
        "impact": i18n("The Higgs mechanism explains how fundamental particles acquire mass and is a central pillar of the Standard Model of particle physics. The experimental confirmation of the Higgs boson at the Large Hadron Collider was one of the greatest triumphs in the history of physics."),
        "timeline": [
            {"year": 1929, "event": i18n("Born in Newcastle upon Tyne, England")},
            {"year": 1964, "event": i18n("Published papers proposing the Higgs mechanism and predicting the Higgs boson")},
            {"year": 2012, "event": i18n("CERN announced the discovery of the Higgs boson at the Large Hadron Collider")},
            {"year": 2013, "event": i18n("Awarded the Nobel Prize in Physics with Francois Englert")},
            {"year": 2024, "event": i18n("Died in Edinburgh, Scotland at age 94")},
        ],
        "famous_works": [
            {"title": i18n("Broken Symmetries and the Masses of Gauge Bosons"), "year": 1964, "description": i18n("Paper proposing that spontaneous symmetry breaking in gauge theories could give mass to gauge bosons, predicting a new massive scalar particle.")},
            {"title": i18n("Broken Symmetries, Massless Particles and Gauge Fields"), "year": 1964, "description": i18n("Companion paper further developing the mechanism of mass generation through symmetry breaking.")},
        ],
        "quotes": [
            {"text": i18n("I had no expectation that I would still be alive when it happened."), "source": "On the discovery of the Higgs boson, 2012"},
            {"text": i18n("It's very nice to be right sometimes."), "source": "Press conference after Nobel Prize announcement, 2013"},
        ],
        "relations": [
            {"person": "francois-englert", "type": "collaborator"},
            {"person": "steven-weinberg", "type": "colleague"},
            {"person": "sheldon-glashow", "type": "colleague"},
        ],
    },
    {
        "id": "stephen-hawking",
        "name": name_i18n("Stephen Hawking", "スティーヴン・ホーキング"),
        "birth_year": 1942,
        "death_year": 2018,
        "countries": ["gb"],
        "fields": ["physics"],
        "overview": i18n("Stephen Hawking was a British theoretical physicist and cosmologist known for his groundbreaking work on black holes and general relativity. His discovery that black holes emit radiation, now called Hawking radiation, transformed the understanding of quantum gravity and made him one of the most famous scientists in history."),
        "early_life": i18n("Hawking was born in Oxford, England and studied physics at University College, Oxford before completing his Ph.D. at Cambridge. At age 21 he was diagnosed with amyotrophic lateral sclerosis (ALS), yet continued his research for over five decades despite progressive physical disability."),
        "impact": i18n("Hawking's theoretical work on black hole thermodynamics and the information paradox stimulated decades of research in quantum gravity. His bestselling book 'A Brief History of Time' made cosmology accessible to millions and established him as an iconic figure bridging science and popular culture."),
        "timeline": [
            {"year": 1942, "event": i18n("Born in Oxford, England")},
            {"year": 1966, "event": i18n("Completed Ph.D. thesis on singularities in general relativity at Cambridge")},
            {"year": 1974, "event": i18n("Proposed that black holes emit thermal radiation (Hawking radiation)")},
            {"year": 1979, "event": i18n("Appointed Lucasian Professor of Mathematics at Cambridge")},
            {"year": 1988, "event": i18n("Published 'A Brief History of Time,' which became an international bestseller")},
            {"year": 2018, "event": i18n("Died in Cambridge, England at age 76")},
        ],
        "famous_works": [
            {"title": i18n("Particle Creation by Black Holes"), "year": 1975, "description": i18n("Landmark paper demonstrating that black holes emit thermal radiation due to quantum effects near the event horizon.")},
            {"title": i18n("A Brief History of Time"), "year": 1988, "description": i18n("Popular science book on cosmology, the Big Bang, and black holes that sold over 25 million copies worldwide.")},
            {"title": i18n("The Large Scale Structure of Space-Time"), "year": 1973, "description": i18n("Technical monograph co-authored with George Ellis on the mathematical structure of general relativity and singularity theorems.")},
        ],
        "quotes": [
            {"text": i18n("Intelligence is the ability to adapt to change."), "source": "Attributed"},
            {"text": i18n("However difficult life may seem, there is always something you can do and succeed at."), "source": "Cambridge Union address, 2017"},
            {"text": i18n("Not only does God play dice, but He sometimes throws them where they cannot be seen."), "source": "The Nature of Space and Time (1996)"},
        ],
        "relations": [
            {"person": "roger-penrose", "type": "collaborator"},
            {"person": "kip-thorne", "type": "friend"},
            {"person": "dennis-sciama", "type": "mentor"},
        ],
    },
    {
        "id": "roger-penrose",
        "name": name_i18n("Roger Penrose", "ロジャー・ペンローズ"),
        "birth_year": 1931,
        "death_year": None,
        "countries": ["gb"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Roger Penrose is a British mathematical physicist who made fundamental contributions to general relativity, including the singularity theorems proving that black hole formation is an inevitable consequence of gravitational collapse. He was awarded the 2020 Nobel Prize in Physics for this work."),
        "early_life": i18n("Penrose was born in Colchester, England into an intellectually distinguished family. He studied mathematics at University College London and earned his Ph.D. from Cambridge, later holding professorships at Birkbeck College and the University of Oxford."),
        "impact": i18n("Penrose's singularity theorems fundamentally changed the understanding of general relativity and black holes. His work on Penrose tilings, twistor theory, and the connections between mathematics, physics, and consciousness has inspired research across multiple disciplines."),
        "timeline": [
            {"year": 1931, "event": i18n("Born in Colchester, England")},
            {"year": 1965, "event": i18n("Published the singularity theorem proving gravitational collapse leads to singularities")},
            {"year": 1969, "event": i18n("Proposed the cosmic censorship conjecture and the Penrose process for extracting energy from rotating black holes")},
            {"year": 1974, "event": i18n("Discovered Penrose tilings, aperiodic tilings with fivefold symmetry")},
            {"year": 1989, "event": i18n("Published 'The Emperor's New Mind' on consciousness and computation")},
            {"year": 2020, "event": i18n("Awarded the Nobel Prize in Physics for proving black hole formation under general relativity")},
        ],
        "famous_works": [
            {"title": i18n("Gravitational Collapse and Space-Time Singularities"), "year": 1965, "description": i18n("Paper proving the first singularity theorem showing that gravitational collapse inevitably leads to singularities.")},
            {"title": i18n("The Emperor's New Mind"), "year": 1989, "description": i18n("Book exploring the relationship between physics, mathematics, consciousness, and artificial intelligence.")},
            {"title": i18n("The Road to Reality"), "year": 2004, "description": i18n("Comprehensive guide to the laws of the universe spanning from basic mathematics to cutting-edge physics.")},
        ],
        "quotes": [
            {"text": i18n("Mathematics is not just a tool; it is the very language of the universe."), "source": "The Road to Reality (2004)"},
            {"text": i18n("My own view is that consciousness is an essential ingredient of the universe."), "source": "Interview, BBC"},
        ],
        "relations": [
            {"person": "stephen-hawking", "type": "collaborator"},
            {"person": "dennis-sciama", "type": "mentor"},
            {"person": "albert-einstein", "type": "influenced_by"},
        ],
    },
    {
        "id": "kip-thorne",
        "name": name_i18n("Kip Thorne", "キップ・ソーン"),
        "birth_year": 1940,
        "death_year": None,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Kip Thorne is an American theoretical physicist who made pioneering contributions to gravitational physics and astrophysics. He shared the 2017 Nobel Prize in Physics for the first direct detection of gravitational waves by the LIGO experiment, which he co-founded."),
        "early_life": i18n("Thorne was born in Logan, Utah and showed early aptitude for science. He earned his Ph.D. at Princeton University under John Archibald Wheeler and became one of the youngest full professors in Caltech's history at age 30."),
        "impact": i18n("Thorne's co-founding of the LIGO project led to one of the most significant experimental achievements in physics: the detection of gravitational waves from merging black holes. His theoretical work on wormholes and time warps also contributed to the scientific accuracy of the film Interstellar."),
        "timeline": [
            {"year": 1940, "event": i18n("Born in Logan, Utah, United States")},
            {"year": 1965, "event": i18n("Earned Ph.D. from Princeton under John Archibald Wheeler")},
            {"year": 1984, "event": i18n("Co-founded the LIGO project for detecting gravitational waves")},
            {"year": 2014, "event": i18n("Served as scientific consultant and executive producer for the film Interstellar")},
            {"year": 2015, "event": i18n("LIGO made the first direct detection of gravitational waves")},
            {"year": 2017, "event": i18n("Awarded the Nobel Prize in Physics for gravitational wave detection")},
        ],
        "famous_works": [
            {"title": i18n("Black Holes and Time Warps: Einstein's Outrageous Legacy"), "year": 1994, "description": i18n("Popular science book exploring the physics of black holes, wormholes, and the nature of spacetime.")},
            {"title": i18n("Gravitation"), "year": 1973, "description": i18n("Landmark graduate textbook on general relativity co-authored with Charles Misner and John Wheeler, widely known as 'MTW'.")},
            {"title": i18n("The Science of Interstellar"), "year": 2014, "description": i18n("Book explaining the real science behind the film Interstellar, covering black holes, wormholes, and higher dimensions.")},
        ],
        "quotes": [
            {"text": i18n("The universe is made of stories, not of atoms."), "source": "Public lecture"},
            {"text": i18n("LIGO is the most precise measuring device ever built by humankind."), "source": "Nobel Prize lecture, 2017"},
        ],
        "relations": [
            {"person": "stephen-hawking", "type": "friend"},
            {"person": "john-archibald-wheeler", "type": "mentor"},
            {"person": "roger-penrose", "type": "colleague"},
            {"person": "albert-einstein", "type": "influenced_by"},
        ],
    },
    {
        "id": "edward-witten",
        "name": name_i18n("Edward Witten", "エドワード・ウィッテン"),
        "birth_year": 1951,
        "death_year": None,
        "countries": ["us"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Edward Witten is an American theoretical physicist and mathematician widely regarded as one of the most brilliant physicists of his generation. He is the leading figure in string theory and proposed M-theory, which unified the five consistent superstring theories."),
        "early_life": i18n("Witten was born in Baltimore, Maryland, the son of theoretical physicist Louis Witten. He studied history at Brandeis University before switching to physics, earning his Ph.D. from Princeton University under David Gross."),
        "impact": i18n("Witten's work has profoundly influenced both theoretical physics and mathematics. He is the only physicist to have won the Fields Medal, awarded in 1990 for his mathematical contributions, and his M-theory conjecture unified the landscape of string theories."),
        "timeline": [
            {"year": 1951, "event": i18n("Born in Baltimore, Maryland, United States")},
            {"year": 1981, "event": i18n("Proved the positive energy theorem in general relativity")},
            {"year": 1988, "event": i18n("Developed topological quantum field theory")},
            {"year": 1990, "event": i18n("Awarded the Fields Medal for contributions to mathematics inspired by physics")},
            {"year": 1995, "event": i18n("Proposed M-theory unifying the five superstring theories")},
        ],
        "famous_works": [
            {"title": i18n("String Theory Dynamics in Various Dimensions"), "year": 1995, "description": i18n("Landmark paper proposing M-theory as the unifying framework for all five consistent superstring theories.")},
            {"title": i18n("Topological Quantum Field Theory"), "year": 1988, "description": i18n("Foundational paper that established deep connections between quantum field theory and topology.")},
            {"title": i18n("A New Proof of the Positive Energy Theorem"), "year": 1981, "description": i18n("Elegant physics-based proof of the positive mass theorem in general relativity using spinor methods.")},
        ],
        "quotes": [
            {"text": i18n("String theory is 21st century physics that fell into the 20th century by accident."), "source": "Interview, PBS NOVA"},
            {"text": i18n("The theory of everything would be the ultimate triumph of human reason."), "source": "Public lecture"},
        ],
        "relations": [
            {"person": "david-gross", "type": "mentor"},
            {"person": "albert-einstein", "type": "influenced_by"},
            {"person": "roger-penrose", "type": "colleague"},
        ],
    },
    {
        "id": "david-bohm",
        "name": name_i18n("David Bohm", "デヴィッド・ボーム"),
        "birth_year": 1917,
        "death_year": 1992,
        "countries": ["us", "gb"],
        "fields": ["physics"],
        "overview": i18n("David Bohm was an American-British theoretical physicist who made important contributions to quantum mechanics, neuropsychology, and the philosophy of mind. He is best known for his alternative interpretation of quantum mechanics, the de Broglie-Bohm theory, which provides a deterministic framework for quantum phenomena."),
        "early_life": i18n("Bohm was born in Wilkes-Barre, Pennsylvania to a Hungarian Jewish immigrant father. He studied under Robert Oppenheimer at the University of California, Berkeley, but was forced to leave the United States during the McCarthy era due to his refusal to testify against colleagues."),
        "impact": i18n("Bohm's pilot wave interpretation revived interest in hidden variable theories of quantum mechanics and continues to inspire foundational research. His concept of implicate order and his dialogues on consciousness and wholeness influenced philosophy, cognitive science, and interdisciplinary thinking."),
        "timeline": [
            {"year": 1917, "event": i18n("Born in Wilkes-Barre, Pennsylvania, United States")},
            {"year": 1951, "event": i18n("Published 'Quantum Theory,' a textbook praised by Einstein")},
            {"year": 1952, "event": i18n("Proposed the de Broglie-Bohm pilot wave interpretation of quantum mechanics")},
            {"year": 1959, "event": i18n("Predicted the Aharonov-Bohm effect demonstrating electromagnetic potential's physical significance")},
            {"year": 1980, "event": i18n("Published 'Wholeness and the Implicate Order' on his philosophy of physics")},
            {"year": 1992, "event": i18n("Died in London, England at age 74")},
        ],
        "famous_works": [
            {"title": i18n("A Suggested Interpretation of the Quantum Theory in Terms of 'Hidden' Variables"), "year": 1952, "description": i18n("Two-part paper presenting a deterministic alternative to the Copenhagen interpretation using pilot waves and hidden variables.")},
            {"title": i18n("Wholeness and the Implicate Order"), "year": 1980, "description": i18n("Philosophical work proposing that the universe has an underlying implicate order from which the explicate order of observable reality unfolds.")},
        ],
        "quotes": [
            {"text": i18n("In some sense man is a microcosm of the universe; therefore what man is, is a clue to the universe."), "source": "Wholeness and the Implicate Order (1980)"},
            {"text": i18n("The ability to perceive or think differently is more important than the knowledge gained."), "source": "On Creativity (1998, posthumous)"},
        ],
        "relations": [
            {"person": "albert-einstein", "type": "friend"},
            {"person": "j-robert-oppenheimer", "type": "mentor"},
            {"person": "john-stewart-bell", "type": "influenced"},
        ],
    },
    {
        "id": "hugh-everett-iii",
        "name": name_i18n("Hugh Everett III", "ヒュー・エヴェレット3世"),
        "birth_year": 1930,
        "death_year": 1982,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Hugh Everett III was an American physicist who proposed the many-worlds interpretation of quantum mechanics, suggesting that all possible quantum outcomes are physically realized in branching parallel universes. Though initially dismissed, his interpretation has become one of the most discussed foundations of quantum theory."),
        "early_life": i18n("Everett was born in Washington, D.C. and showed exceptional mathematical ability from a young age. He studied chemical engineering at the Catholic University of America before switching to physics at Princeton, where he developed the many-worlds interpretation under John Archibald Wheeler."),
        "impact": i18n("Everett's many-worlds interpretation offered a radical solution to the measurement problem in quantum mechanics by eliminating wave function collapse. Initially ignored, it gained traction from the 1970s onward and is now considered a serious contender among interpretations of quantum mechanics, especially in quantum computing and cosmology."),
        "timeline": [
            {"year": 1930, "event": i18n("Born in Washington, D.C., United States")},
            {"year": 1957, "event": i18n("Published his Ph.D. thesis proposing the many-worlds interpretation of quantum mechanics")},
            {"year": 1957, "event": i18n("Left academia to work in defense research at the Pentagon")},
            {"year": 1973, "event": i18n("Bryce DeWitt popularized Everett's ideas, coining the term 'many-worlds'")},
            {"year": 1982, "event": i18n("Died in McLean, Virginia at age 51")},
        ],
        "famous_works": [
            {"title": i18n("'Relative State' Formulation of Quantum Mechanics"), "year": 1957, "description": i18n("Ph.D. thesis proposing that quantum measurements result in branching of the observer's state rather than wave function collapse.")},
            {"title": i18n("The Theory of the Universal Wave Function"), "year": 1957, "description": i18n("Extended version of his thesis providing the full mathematical framework for the relative state formulation.")},
        ],
        "quotes": [
            {"text": i18n("I can't resist asking: Do you believe in the existence of other worlds?"), "source": "Letter exchange with Bryce DeWitt"},
        ],
        "relations": [
            {"person": "john-archibald-wheeler", "type": "mentor"},
            {"person": "niels-bohr", "type": "rival"},
            {"person": "bryce-dewitt", "type": "collaborator"},
        ],
    },
    {
        "id": "vera-rubin",
        "name": name_i18n("Vera Rubin", "ヴェラ・ルービン"),
        "birth_year": 1928,
        "death_year": 2016,
        "countries": ["us"],
        "fields": ["physics", "astronomy"],
        "overview": i18n("Vera Rubin was an American astronomer who provided some of the first strong observational evidence for the existence of dark matter. Her measurements of galaxy rotation curves showed that galaxies contain far more mass than is visible, fundamentally changing our understanding of the universe."),
        "early_life": i18n("Rubin was born in Philadelphia, Pennsylvania and developed a passion for astronomy as a child. She earned her master's degree from Cornell under Philip Morrison and her Ph.D. from Georgetown University, overcoming significant gender discrimination in astronomy throughout her career."),
        "impact": i18n("Rubin's galaxy rotation curve measurements provided compelling evidence that most of the matter in the universe is invisible dark matter. Her work opened an entirely new field of research and she became a prominent advocate for women in science, mentoring many female astronomers."),
        "timeline": [
            {"year": 1928, "event": i18n("Born in Philadelphia, Pennsylvania, United States")},
            {"year": 1954, "event": i18n("Earned Ph.D. from Georgetown University with work on galaxy clustering")},
            {"year": 1970, "event": i18n("Began systematic measurements of galaxy rotation curves with Kent Ford")},
            {"year": 1980, "event": i18n("Published landmark paper establishing flat rotation curves as evidence for dark matter")},
            {"year": 1993, "event": i18n("Awarded the National Medal of Science")},
            {"year": 2016, "event": i18n("Died in Princeton, New Jersey at age 88")},
        ],
        "famous_works": [
            {"title": i18n("Rotation of the Andromeda Nebula from a Spectroscopic Survey of Emission Regions"), "year": 1970, "description": i18n("Groundbreaking study of the Andromeda galaxy's rotation curve revealing unexpectedly high orbital velocities in the outer regions.")},
            {"title": i18n("Rotational Properties of 21 SC Galaxies"), "year": 1980, "description": i18n("Systematic study of spiral galaxy rotation curves demonstrating flat rotation curves inconsistent with visible mass alone, supporting the dark matter hypothesis.")},
        ],
        "quotes": [
            {"text": i18n("In a spiral galaxy, the weights of stars are not important; what really matters is the invisible dark matter."), "source": "Scientific American interview"},
            {"text": i18n("Fame is fleeting. My numbers mean more to me than my name."), "source": "Discover Magazine interview"},
        ],
        "relations": [
            {"person": "kent-ford", "type": "collaborator"},
            {"person": "fritz-zwicky", "type": "influenced_by"},
            {"person": "margaret-burbidge", "type": "colleague"},
        ],
    },
    {
        "id": "jocelyn-bell-burnell",
        "name": name_i18n("Jocelyn Bell Burnell", "ジョスリン・ベル・バーネル"),
        "birth_year": 1943,
        "death_year": None,
        "countries": ["gb", "ie"],
        "fields": ["physics", "astronomy"],
        "overview": i18n("Jocelyn Bell Burnell is a British-Irish astrophysicist who, as a graduate student, discovered the first radio pulsars in 1967. Despite her crucial role in the discovery, the Nobel Prize was controversially awarded only to her supervisor Antony Hewish."),
        "early_life": i18n("Bell Burnell was born in Lurgan, Northern Ireland and grew up near the Armagh Observatory, which sparked her interest in astronomy. She studied physics at the University of Glasgow and began her Ph.D. at Cambridge, where she built and operated the radio telescope that detected pulsars."),
        "impact": i18n("The discovery of pulsars opened a new window on extreme physics, confirming the existence of neutron stars and later enabling indirect detection of gravitational waves. Bell Burnell became a role model for women in science and has used her platform to advocate for diversity and inclusion in physics."),
        "timeline": [
            {"year": 1943, "event": i18n("Born in Lurgan, Northern Ireland")},
            {"year": 1967, "event": i18n("Discovered the first pulsar signals as a graduate student at Cambridge")},
            {"year": 1974, "event": i18n("Nobel Prize in Physics awarded to Hewish and Ryle for pulsar discovery; Bell Burnell was excluded")},
            {"year": 2018, "event": i18n("Awarded the Special Breakthrough Prize in Fundamental Physics worth 3 million dollars")},
            {"year": 2021, "event": i18n("Received the Copley Medal from the Royal Society")},
        ],
        "famous_works": [
            {"title": i18n("Observation of a Rapidly Pulsating Radio Source"), "year": 1968, "description": i18n("Paper announcing the discovery of the first pulsar, CP 1919, initially detected as a mysterious regularly pulsing radio signal.")},
            {"title": i18n("A New Class of Radio Sources"), "year": 1968, "description": i18n("Follow-up paper identifying additional pulsars and establishing them as a new class of astrophysical objects.")},
        ],
        "quotes": [
            {"text": i18n("I believe it would demean Nobel Prizes if they were awarded to research students."), "source": "Speech on the Nobel Prize controversy"},
            {"text": i18n("Breakthroughs tend to come from people who are a bit unusual."), "source": "Breakthrough Prize acceptance speech, 2018"},
        ],
        "relations": [
            {"person": "antony-hewish", "type": "mentor"},
            {"person": "martin-ryle", "type": "colleague"},
            {"person": "fred-hoyle", "type": "colleague"},
        ],
    },
    {
        "id": "donna-strickland",
        "name": name_i18n("Donna Strickland", "ドナ・ストリックランド"),
        "birth_year": 1959,
        "death_year": None,
        "countries": ["ca"],
        "fields": ["physics"],
        "overview": i18n("Donna Strickland is a Canadian optical physicist who co-invented chirped pulse amplification (CPA), a technique for creating ultra-short, high-intensity laser pulses. She shared the 2018 Nobel Prize in Physics, becoming the third woman to receive the prize."),
        "early_life": i18n("Strickland was born in Guelph, Ontario, Canada. She studied engineering physics at McMaster University and earned her Ph.D. from the University of Rochester, where she developed CPA under the supervision of Gerard Mourou."),
        "impact": i18n("Chirped pulse amplification revolutionized laser physics and enabled applications ranging from corrective eye surgery to industrial machining and fundamental physics research. Strickland's achievement highlighted the significant contributions of women to physics and inspired broader conversations about gender equity in science."),
        "timeline": [
            {"year": 1959, "event": i18n("Born in Guelph, Ontario, Canada")},
            {"year": 1985, "event": i18n("Co-invented chirped pulse amplification as a Ph.D. student at the University of Rochester")},
            {"year": 1997, "event": i18n("Joined the University of Waterloo as a faculty member")},
            {"year": 2018, "event": i18n("Awarded the Nobel Prize in Physics with Gerard Mourou and Arthur Ashkin")},
        ],
        "famous_works": [
            {"title": i18n("Compression of Amplified Chirped Optical Pulses"), "year": 1985, "description": i18n("Seminal paper describing the chirped pulse amplification technique, enabling generation of ultra-short high-intensity laser pulses without damaging the amplifier.")},
        ],
        "quotes": [
            {"text": i18n("We need to celebrate women physicists because they're out there."), "source": "Nobel Prize press conference, 2018"},
        ],
        "relations": [
            {"person": "gerard-mourou", "type": "mentor"},
            {"person": "arthur-ashkin", "type": "colleague"},
        ],
    },
    {
        "id": "emilie-du-chatelet",
        "name": name_i18n("Emilie du Chatelet", "エミリー・デュ・シャトレ"),
        "birth_year": 1706,
        "death_year": 1749,
        "countries": ["fr"],
        "fields": ["physics", "mathematics", "philosophy"],
        "overview": i18n("Emilie du Chatelet was a French natural philosopher, mathematician, and physicist who made significant contributions to Newtonian mechanics. Her translation and commentary on Newton's Principia Mathematica remains the standard French translation, and she proposed the concept of kinetic energy as proportional to the square of velocity."),
        "early_life": i18n("Du Chatelet was born into a wealthy aristocratic family in Paris that encouraged her education, unusual for women of her era. She received tutoring in mathematics, literature, and science, and later studied under leading mathematicians including Pierre-Louis Maupertuis and Samuel Koenig."),
        "impact": i18n("Du Chatelet's French translation and commentary on Newton's Principia made his work accessible to the French-speaking scientific world and remains authoritative to this day. Her experimental demonstration that kinetic energy is proportional to the square of velocity corrected Newton and contributed to the development of the concept of energy conservation."),
        "timeline": [
            {"year": 1706, "event": i18n("Born in Paris, France")},
            {"year": 1737, "event": i18n("Published a paper on the nature of fire submitted to the French Academy of Sciences")},
            {"year": 1740, "event": i18n("Published 'Institutions de Physique,' synthesizing Leibnizian and Newtonian physics")},
            {"year": 1749, "event": i18n("Completed her translation of Newton's Principia Mathematica shortly before her death")},
            {"year": 1749, "event": i18n("Died in Luneville, France at age 42 from complications of childbirth")},
        ],
        "famous_works": [
            {"title": i18n("Institutions de Physique"), "year": 1740, "description": i18n("Comprehensive physics textbook synthesizing Newtonian mechanics with Leibnizian metaphysics, introducing the concept of vis viva (living force).")},
            {"title": i18n("Translation and Commentary on Newton's Principia Mathematica"), "year": 1749, "description": i18n("French translation of Newton's masterwork with extensive commentary that remains the standard French edition.")},
        ],
        "quotes": [
            {"text": i18n("Judge me for my own merits, or lack of them, but do not look upon me as a mere appendage to this great general or that renowned scholar."), "source": "Personal correspondence"},
            {"text": i18n("If I were king, I would redress an abuse which cuts back, as it were, one half of human kind."), "source": "Preface to her translation of Bernard Mandeville"},
        ],
        "relations": [
            {"person": "voltaire", "type": "collaborator"},
            {"person": "isaac-newton", "type": "influenced_by"},
            {"person": "gottfried-wilhelm-leibniz", "type": "influenced_by"},
        ],
    },
    {
        "id": "zhang-heng",
        "name": name_i18n("Zhang Heng", "張衡"),
        "birth_year": 78,
        "death_year": 139,
        "countries": ["cn"],
        "fields": ["physics", "astronomy", "engineering"],
        "overview": i18n("Zhang Heng was a Chinese polymath of the Eastern Han dynasty who made groundbreaking contributions to astronomy, mathematics, seismology, and engineering. He invented the world's first seismoscope to detect distant earthquakes and constructed a water-powered armillary sphere for astronomical observation."),
        "early_life": i18n("Zhang Heng was born in Nanyang, Henan province, during the Eastern Han dynasty. He received a classical education and served in various government positions, eventually becoming the chief astronomer and later a prefect."),
        "impact": i18n("Zhang Heng's seismoscope, invented nearly 1,700 years before similar Western devices, demonstrated remarkable engineering ingenuity. His astronomical work, including his estimate of 2,500 visible stars and his correct explanation of lunar eclipses, represented some of the most advanced scientific thinking of the ancient world."),
        "timeline": [
            {"year": 78, "event": i18n("Born in Nanyang, Henan, Eastern Han dynasty China")},
            {"year": 111, "event": i18n("Appointed chief astronomer at the imperial court")},
            {"year": 117, "event": i18n("Constructed a water-powered armillary sphere for celestial observation")},
            {"year": 132, "event": i18n("Invented the first seismoscope (Houfeng Didong Yi) to detect earthquakes")},
            {"year": 139, "event": i18n("Died in Luoyang at age 61")},
        ],
        "famous_works": [
            {"title": i18n("Houfeng Didong Yi (Earthquake Weathervane)"), "year": 132, "description": i18n("The world's first seismoscope, a bronze vessel that could detect the direction of distant earthquakes using a pendulum mechanism.")},
            {"title": i18n("Ling Xian (The Spiritual Constitution of the Universe)"), "year": 120, "description": i18n("Astronomical treatise describing the hun tian (celestial sphere) model and cataloging over 2,500 stars.")},
            {"title": i18n("Water-Powered Armillary Sphere"), "year": 117, "description": i18n("Mechanized celestial globe driven by water power that could track the movements of celestial bodies.")},
        ],
        "quotes": [
            {"text": i18n("The sun is like fire and the moon is like water. The fire gives out light and the water reflects it."), "source": "Ling Xian (The Spiritual Constitution of the Universe)"},
        ],
        "relations": [
            {"person": "cai-lun", "type": "colleague"},
            {"person": "sima-qian", "type": "influenced_by"},
        ],
    },
    {
        "id": "evangelista-torricelli",
        "name": name_i18n("Evangelista Torricelli", "エヴァンジェリスタ・トリチェリ"),
        "birth_year": 1608,
        "death_year": 1647,
        "countries": ["it"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Evangelista Torricelli was an Italian physicist and mathematician who invented the barometer and demonstrated the existence of atmospheric pressure and the vacuum. He also made important contributions to mathematics, including the discovery of Torricelli's trumpet, a shape with finite volume but infinite surface area."),
        "early_life": i18n("Torricelli was born in Faenza, Italy and was educated by Benedictine monks before studying mathematics under Benedetto Castelli, a student of Galileo. He served as Galileo's secretary in the last months of the elder scientist's life and succeeded him as court mathematician to the Grand Duke of Tuscany."),
        "impact": i18n("Torricelli's invention of the mercury barometer proved the existence of atmospheric pressure and the vacuum, settling a centuries-long debate. His work laid the foundation for the development of vacuum technology and atmospheric science, and his mathematical contributions influenced the development of calculus."),
        "timeline": [
            {"year": 1608, "event": i18n("Born in Faenza, Italy")},
            {"year": 1641, "event": i18n("Became secretary and assistant to Galileo Galilei in Arcetri")},
            {"year": 1642, "event": i18n("Succeeded Galileo as court mathematician to Grand Duke Ferdinand II of Tuscany")},
            {"year": 1644, "event": i18n("Invented the mercury barometer, demonstrating atmospheric pressure and the vacuum")},
            {"year": 1647, "event": i18n("Died in Florence at age 39, likely of typhoid fever")},
        ],
        "famous_works": [
            {"title": i18n("Opera Geometrica"), "year": 1644, "description": i18n("Major mathematical work containing studies on the cycloid, the motion of fluids, and the properties of the parabola.")},
            {"title": i18n("Mercury Barometer Experiment"), "year": 1644, "description": i18n("Experimental demonstration using a mercury-filled tube inverted in a dish, proving the existence of atmospheric pressure and creating the first sustained vacuum.")},
        ],
        "quotes": [
            {"text": i18n("We live submerged at the bottom of an ocean of air."), "source": "Letter to Michelangelo Ricci, 1644"},
        ],
        "relations": [
            {"person": "galileo-galilei", "type": "mentor"},
            {"person": "benedetto-castelli", "type": "mentor"},
            {"person": "blaise-pascal", "type": "influenced"},
        ],
    },
    {
        "id": "guglielmo-marconi",
        "name": name_i18n("Guglielmo Marconi", "グリエルモ・マルコーニ"),
        "birth_year": 1874,
        "death_year": 1937,
        "countries": ["it"],
        "fields": ["physics", "engineering"],
        "overview": i18n("Guglielmo Marconi was an Italian inventor and electrical engineer who pioneered long-distance radio transmission. He shared the 1909 Nobel Prize in Physics for his contributions to the development of wireless telegraphy, which revolutionized global communications."),
        "early_life": i18n("Marconi was born in Bologna, Italy to an Italian father and Irish mother. He was educated privately and became fascinated with the work of Heinrich Hertz on electromagnetic waves, conducting his first radio experiments at his family estate at age 20."),
        "impact": i18n("Marconi's development of practical radio communication transformed maritime safety, military communications, and eventually led to the radio broadcasting industry. His transatlantic radio transmission in 1901 proved that radio waves could follow the curvature of the Earth, opening the era of global wireless communication."),
        "timeline": [
            {"year": 1874, "event": i18n("Born in Bologna, Italy")},
            {"year": 1895, "event": i18n("Conducted first successful radio transmission experiments at his family estate")},
            {"year": 1897, "event": i18n("Founded the Wireless Telegraph and Signal Company in London")},
            {"year": 1901, "event": i18n("Transmitted the first transatlantic radio signal from Cornwall to Newfoundland")},
            {"year": 1909, "event": i18n("Awarded the Nobel Prize in Physics with Karl Ferdinand Braun")},
            {"year": 1937, "event": i18n("Died in Rome at age 63")},
        ],
        "famous_works": [
            {"title": i18n("Transatlantic Radio Transmission"), "year": 1901, "description": i18n("First successful transmission of a radio signal across the Atlantic Ocean, from Poldhu, Cornwall to St. John's, Newfoundland.")},
            {"title": i18n("Wireless Telegraphy System"), "year": 1897, "description": i18n("Practical system for wireless communication using radio waves, commercially deployed for maritime and land-based communication.")},
        ],
        "quotes": [
            {"text": i18n("Every day sees humanity more victorious in the struggle with space and time."), "source": "Nobel Prize banquet speech, 1909"},
            {"text": i18n("I have never been disillusioned about the possibilities of wireless."), "source": "Interview"},
        ],
        "relations": [
            {"person": "heinrich-hertz", "type": "influenced_by"},
            {"person": "nikola-tesla", "type": "rival"},
            {"person": "karl-ferdinand-braun", "type": "colleague"},
        ],
    },
    {
        "id": "homi-j-bhabha",
        "name": name_i18n("Homi J. Bhabha", "ホミ・J・バーバ"),
        "birth_year": 1909,
        "death_year": 1966,
        "countries": ["in"],
        "fields": ["physics"],
        "overview": i18n("Homi Jehangir Bhabha was an Indian nuclear physicist who played a central role in establishing India's nuclear program. He made significant contributions to the theory of cosmic radiation and electron-positron scattering, and founded both the Tata Institute of Fundamental Research and India's Atomic Energy Commission."),
        "early_life": i18n("Bhabha was born into a prominent Parsi family in Bombay (Mumbai). He studied mechanical engineering and later physics at Cambridge University, where he worked under Paul Dirac and made important contributions to cosmic ray theory."),
        "impact": i18n("Bhabha is considered the father of India's nuclear program, establishing the institutional framework that led to India's development of nuclear energy and weapons capability. His scientific contributions to the theory of cosmic ray showers and Bhabha scattering remain significant in particle physics."),
        "timeline": [
            {"year": 1909, "event": i18n("Born in Bombay (Mumbai), India")},
            {"year": 1935, "event": i18n("Published the theory of Bhabha scattering (electron-positron scattering)")},
            {"year": 1945, "event": i18n("Founded the Tata Institute of Fundamental Research in Bombay")},
            {"year": 1948, "event": i18n("Appointed first chairman of India's Atomic Energy Commission")},
            {"year": 1954, "event": i18n("Presided over the first United Nations Conference on the Peaceful Uses of Atomic Energy")},
            {"year": 1966, "event": i18n("Died in a plane crash on Mont Blanc at age 56")},
        ],
        "famous_works": [
            {"title": i18n("The Scattering of Positrons by Electrons with Exchange on Dirac's Theory"), "year": 1935, "description": i18n("Paper on electron-positron scattering using Dirac's relativistic quantum theory, now known as Bhabha scattering.")},
            {"title": i18n("On the Theory of Cosmic Ray Showers"), "year": 1937, "description": i18n("Theoretical explanation of the cascade process in cosmic ray showers, co-authored with Walter Heitler.")},
        ],
        "quotes": [
            {"text": i18n("When nuclear energy has been successfully applied for power production, India will not have to look abroad for its experts."), "source": "Address to the Indian Science Congress, 1944"},
        ],
        "relations": [
            {"person": "paul-dirac", "type": "mentor"},
            {"person": "niels-bohr", "type": "colleague"},
            {"person": "jawaharlal-nehru", "type": "collaborator"},
        ],
    },
    {
        "id": "carl-david-anderson",
        "name": name_i18n("Carl David Anderson", "カール・デイヴィッド・アンダーソン"),
        "birth_year": 1905,
        "death_year": 1991,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Carl David Anderson was an American experimental physicist who discovered the positron, the first known antimatter particle, in 1932. He also co-discovered the muon in 1936, and was awarded the 1936 Nobel Prize in Physics for the positron discovery."),
        "early_life": i18n("Anderson was born in New York City to Swedish immigrant parents. He studied physics and engineering at Caltech, earning his Ph.D. under Robert Millikan, and spent his entire career at the institute."),
        "impact": i18n("Anderson's discovery of the positron confirmed Paul Dirac's theoretical prediction of antimatter and opened the field of particle physics to the study of antiparticles. His subsequent co-discovery of the muon revealed the existence of unexpected new particles, beginning the era of particle proliferation that would transform physics."),
        "timeline": [
            {"year": 1905, "event": i18n("Born in New York City, United States")},
            {"year": 1932, "event": i18n("Discovered the positron in cosmic ray cloud chamber photographs")},
            {"year": 1936, "event": i18n("Co-discovered the muon with Seth Neddermeyer")},
            {"year": 1936, "event": i18n("Awarded the Nobel Prize in Physics for the discovery of the positron")},
            {"year": 1991, "event": i18n("Died in San Marino, California at age 85")},
        ],
        "famous_works": [
            {"title": i18n("The Positive Electron"), "year": 1933, "description": i18n("Paper presenting definitive evidence for the positron from cloud chamber observations of cosmic rays.")},
            {"title": i18n("The Apparent Existence of Easily Deflectable Positives"), "year": 1932, "description": i18n("Initial publication reporting the observation of positively charged particles with electron mass in cosmic ray photographs.")},
        ],
        "quotes": [
            {"text": i18n("The discovery of the positron was wholly accidental."), "source": "Nobel Prize lecture, 1936"},
        ],
        "relations": [
            {"person": "robert-millikan", "type": "mentor"},
            {"person": "paul-dirac", "type": "influenced_by"},
            {"person": "seth-neddermeyer", "type": "collaborator"},
        ],
    },
    {
        "id": "willis-lamb",
        "name": name_i18n("Willis Lamb", "ウィリス・ラム"),
        "birth_year": 1913,
        "death_year": 2008,
        "countries": ["us"],
        "fields": ["physics"],
        "overview": i18n("Willis Lamb was an American physicist who discovered the Lamb shift, a small difference in energy levels of the hydrogen atom that could not be explained by the Dirac equation. This discovery was pivotal in the development of quantum electrodynamics and earned him the 1955 Nobel Prize in Physics."),
        "early_life": i18n("Lamb was born in Los Angeles, California. He studied chemistry at the University of California, Berkeley, but switched to theoretical physics, earning his Ph.D. under J. Robert Oppenheimer in 1938."),
        "impact": i18n("The Lamb shift provided crucial experimental evidence that spurred the development of renormalization techniques in quantum electrodynamics by Richard Feynman, Julian Schwinger, and Sin-Itiro Tomonaga. This measurement is considered one of the most important experiments in the history of physics."),
        "timeline": [
            {"year": 1913, "event": i18n("Born in Los Angeles, California, United States")},
            {"year": 1947, "event": i18n("Measured the Lamb shift in the hydrogen spectrum with Robert Retherford")},
            {"year": 1955, "event": i18n("Awarded the Nobel Prize in Physics for the discovery of the Lamb shift")},
            {"year": 1974, "event": i18n("Joined the University of Arizona, where he continued teaching until his 90s")},
            {"year": 2008, "event": i18n("Died in Tucson, Arizona at age 94")},
        ],
        "famous_works": [
            {"title": i18n("Fine Structure of the Hydrogen Atom by a Microwave Method"), "year": 1947, "description": i18n("Landmark paper reporting the precise measurement of the energy level splitting in hydrogen that became known as the Lamb shift.")},
            {"title": i18n("Anti-photon"), "year": 1995, "description": i18n("Paper challenging common interpretations of the photon concept in quantum optics.")},
        ],
        "quotes": [
            {"text": i18n("A photon is what a photodetector detects."), "source": "Anti-photon paper, 1995"},
        ],
        "relations": [
            {"person": "j-robert-oppenheimer", "type": "mentor"},
            {"person": "richard-feynman", "type": "influenced"},
            {"person": "julian-schwinger", "type": "influenced"},
        ],
    },
    {
        "id": "marian-smoluchowski",
        "name": name_i18n("Marian Smoluchowski", "マリアン・スモルコフスキ"),
        "birth_year": 1872,
        "death_year": 1917,
        "countries": ["pl"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Marian Smoluchowski was a Polish physicist who made fundamental contributions to statistical physics, kinetic theory, and the theory of Brownian motion. His independent derivation of the theory of Brownian motion, concurrent with Einstein's work, established him as one of the founders of statistical mechanics."),
        "early_life": i18n("Smoluchowski was born in Vorderbruhl near Vienna in the Austro-Hungarian Empire to a Polish family. He studied physics at the University of Vienna under Josef Stefan and Ludwig Boltzmann, earning his doctorate in 1895."),
        "impact": i18n("Smoluchowski's theory of Brownian motion, developed independently of Einstein, provided a rigorous statistical mechanical framework for understanding fluctuation phenomena. His work on coagulation kinetics (Smoluchowski coagulation equation) remains widely used in colloid science, atmospheric physics, and astrophysics."),
        "timeline": [
            {"year": 1872, "event": i18n("Born in Vorderbruhl near Vienna, Austro-Hungarian Empire")},
            {"year": 1906, "event": i18n("Published his theory of Brownian motion independently of Einstein")},
            {"year": 1908, "event": i18n("Appointed professor of physics at the University of Lwow (Lviv)")},
            {"year": 1916, "event": i18n("Published the Smoluchowski coagulation equation for particle aggregation")},
            {"year": 1917, "event": i18n("Died in Krakow during a dysentery epidemic at age 45")},
        ],
        "famous_works": [
            {"title": i18n("On the Kinetic Theory of Brownian Molecular Motion"), "year": 1906, "description": i18n("Independent derivation of the theory of Brownian motion from kinetic theory, arriving at results consistent with Einstein's contemporaneous work.")},
            {"title": i18n("Coagulation of Colloids (Smoluchowski Coagulation Equation)"), "year": 1916, "description": i18n("Mathematical framework describing the kinetics of particle aggregation, foundational to colloid chemistry and aerosol physics.")},
        ],
        "quotes": [
            {"text": i18n("The irregular movements of particles suspended in a fluid are a visible manifestation of the thermal molecular motions."), "source": "On Brownian motion, 1906"},
        ],
        "relations": [
            {"person": "ludwig-boltzmann", "type": "mentor"},
            {"person": "albert-einstein", "type": "colleague"},
            {"person": "jean-baptiste-perrin", "type": "colleague"},
        ],
    },
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for person in PEOPLE:
        filepath = os.path.join(OUTPUT_DIR, f"{person['id']}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(person, f, ensure_ascii=False, indent=2)
        print(f"Created {filepath}")
    print(f"\nTotal: {len(PEOPLE)} files generated.")


if __name__ == "__main__":
    main()
