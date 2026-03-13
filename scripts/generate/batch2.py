#!/usr/bin/env python3
"""Batch 2: Generate 20 physicist JSON files (19th century physicists, IDs 21-40)."""

import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "people")


def i18n(en="", ja=""):
    return {"en": en, "es": "", "pt": "", "fr": "", "de": "", "zh": "", "hi": "", "ar": "", "id": "", "ja": ja}


def name_i18n(en, ja):
    return {"en": en, "es": "", "pt": "", "fr": "", "de": "", "zh": "", "hi": "", "ar": "", "id": "", "ja": ja}


PHYSICISTS = [
    {
        "id": "james-prescott-joule",
        "name": name_i18n("James Prescott Joule", "ジェームズ・プレスコット・ジュール"),
        "birth_year": 1818,
        "death_year": 1889,
        "countries": ["gb"],
        "fields": ["physics"],
        "overview": i18n("James Prescott Joule was an English physicist who established the mechanical equivalent of heat, demonstrating that heat is a form of energy. His meticulous experiments laid the groundwork for the first law of thermodynamics and the conservation of energy principle."),
        "early_life": i18n("Born in Salford, Lancashire, Joule was the son of a wealthy brewer. He was educated at home and later studied under John Dalton, developing a lifelong passion for precise measurement and experimental physics."),
        "impact": i18n("Joule's determination of the mechanical equivalent of heat was pivotal in establishing the conservation of energy as a fundamental law of physics. The SI unit of energy, the joule, is named in his honor, reflecting his lasting contribution to science."),
        "timeline": [
            {"year": 1840, "event": i18n("Published Joule's first law on the relationship between electric current and heat.")},
            {"year": 1843, "event": i18n("Presented his paddle-wheel experiment determining the mechanical equivalent of heat.")},
            {"year": 1847, "event": i18n("Met William Thomson (Lord Kelvin) and began a fruitful collaboration.")},
            {"year": 1849, "event": i18n("Published refined measurements of the mechanical equivalent of heat.")},
            {"year": 1852, "event": i18n("Discovered the Joule-Thomson effect with Lord Kelvin.")},
        ],
        "famous_works": [
            {"title": i18n("On the Mechanical Equivalent of Heat"), "year": 1845, "description": i18n("Landmark paper establishing precise measurements of the conversion between mechanical work and heat energy.")},
            {"title": i18n("On the Calorific Effects of Magneto-Electricity and the Mechanical Value of Heat"), "year": 1843, "description": i18n("Early paper presenting experimental evidence for the equivalence of heat and mechanical work.")},
        ],
        "quotes": [
            {"text": i18n("The grand agents of nature are, by the Creator's fiat, indestructible; and that wherever mechanical force is expended, an exact equivalent of heat is always obtained."), "source": "On the Mechanical Equivalent of Heat, 1845"},
        ],
        "relations": [
            {"person": "lord-kelvin", "type": "collaborator"},
            {"person": "hermann-von-helmholtz", "type": "colleague"},
            {"person": "rudolf-clausius", "type": "colleague"},
        ],
    },
    {
        "id": "rudolf-clausius",
        "name": name_i18n("Rudolf Clausius", "ルドルフ・クラウジウス"),
        "birth_year": 1822,
        "death_year": 1888,
        "countries": ["de"],
        "fields": ["physics"],
        "overview": i18n("Rudolf Clausius was a German physicist and mathematician who formulated the second law of thermodynamics and introduced the concept of entropy. He was one of the founders of thermodynamics as a rigorous scientific discipline."),
        "early_life": i18n("Born in Köslin, Prussia, Clausius studied at the University of Berlin and the University of Halle. He showed early aptitude for mathematics and physics, eventually becoming a professor at several German and Swiss universities."),
        "impact": i18n("Clausius's introduction of the entropy concept transformed thermodynamics from an engineering tool into a fundamental branch of physics. His formulation of the second law of thermodynamics remains one of the most important principles in all of science."),
        "timeline": [
            {"year": 1850, "event": i18n("Published his first paper on thermodynamics, reformulating Carnot's theory.")},
            {"year": 1854, "event": i18n("Introduced the concept that would later be named entropy.")},
            {"year": 1857, "event": i18n("Published foundational work on the kinetic theory of gases.")},
            {"year": 1865, "event": i18n("Coined the term 'entropy' and formulated the second law of thermodynamics in its modern form.")},
        ],
        "famous_works": [
            {"title": i18n("On the Motive Power of Heat"), "year": 1850, "description": i18n("Foundational paper that reconciled Carnot's work with the first law of thermodynamics.")},
            {"title": i18n("On the Mechanical Theory of Heat"), "year": 1865, "description": i18n("Comprehensive treatise introducing the concept of entropy and its role in thermodynamics.")},
            {"title": i18n("The Mechanical Theory of Heat"), "year": 1867, "description": i18n("Book compiling his major thermodynamic works into a unified framework.")},
        ],
        "quotes": [
            {"text": i18n("The energy of the universe is constant. The entropy of the universe tends to a maximum."), "source": "The Mechanical Theory of Heat, 1865"},
        ],
        "relations": [
            {"person": "lord-kelvin", "type": "rival"},
            {"person": "james-prescott-joule", "type": "colleague"},
            {"person": "ludwig-boltzmann", "type": "influenced"},
            {"person": "hermann-von-helmholtz", "type": "colleague"},
        ],
    },
    {
        "id": "lord-kelvin",
        "name": name_i18n("Lord Kelvin (William Thomson)", "ケルヴィン卿（ウィリアム・トムソン）"),
        "birth_year": 1824,
        "death_year": 1907,
        "countries": ["gb"],
        "fields": ["physics", "engineering"],
        "overview": i18n("Lord Kelvin was a British mathematical physicist and engineer who formulated the absolute temperature scale and made major contributions to thermodynamics and electromagnetism. He played a key role in the transatlantic telegraph cable project."),
        "early_life": i18n("Born William Thomson in Belfast, Ireland, he entered the University of Glasgow at age ten and later studied at Cambridge. His extraordinary mathematical talent was evident from childhood, and he became a professor at Glasgow at age 22."),
        "impact": i18n("Lord Kelvin's absolute temperature scale provided a fundamental reference for thermodynamics. His contributions to the laying of the transatlantic telegraph cable demonstrated the practical power of theoretical physics, and he was one of the most influential scientists of the Victorian era."),
        "timeline": [
            {"year": 1848, "event": i18n("Proposed the absolute temperature scale, later named the Kelvin scale.")},
            {"year": 1851, "event": i18n("Published a comprehensive paper on the dynamical theory of heat.")},
            {"year": 1852, "event": i18n("Discovered the Joule-Thomson effect with James Prescott Joule.")},
            {"year": 1858, "event": i18n("Successfully supervised the laying of the first transatlantic telegraph cable.")},
            {"year": 1866, "event": i18n("Knighted for contributions to the transatlantic telegraph project.")},
            {"year": 1892, "event": i18n("Elevated to the peerage as Baron Kelvin of Largs.")},
        ],
        "famous_works": [
            {"title": i18n("On an Absolute Thermometric Scale"), "year": 1848, "description": i18n("Paper proposing an absolute temperature scale based on Carnot's theory of heat.")},
            {"title": i18n("On the Dynamical Theory of Heat"), "year": 1851, "description": i18n("Major work establishing the mathematical foundations of thermodynamics.")},
        ],
        "quotes": [
            {"text": i18n("When you can measure what you are speaking about, and express it in numbers, you know something about it."), "source": "Lecture on Electrical Units of Measurement, 1883"},
            {"text": i18n("There is nothing new to be discovered in physics now. All that remains is more and more precise measurement."), "source": "Address to the British Association for the Advancement of Science, 1900"},
        ],
        "relations": [
            {"person": "james-prescott-joule", "type": "collaborator"},
            {"person": "rudolf-clausius", "type": "rival"},
            {"person": "james-clerk-maxwell", "type": "colleague"},
            {"person": "hermann-von-helmholtz", "type": "friend"},
        ],
    },
    {
        "id": "gustav-kirchhoff",
        "name": name_i18n("Gustav Kirchhoff", "グスタフ・キルヒホッフ"),
        "birth_year": 1824,
        "death_year": 1887,
        "countries": ["de"],
        "fields": ["physics"],
        "overview": i18n("Gustav Kirchhoff was a German physicist who formulated fundamental laws governing electrical circuits and co-founded the science of spectroscopy. His circuit laws remain essential tools in electrical engineering and physics."),
        "early_life": i18n("Born in Königsberg, Prussia, Kirchhoff studied at the University of Königsberg under Franz Neumann. He showed exceptional talent in mathematical physics and began his academic career at the University of Berlin."),
        "impact": i18n("Kirchhoff's circuit laws became foundational principles for electrical engineering. His work on spectroscopy with Robert Bunsen led to the discovery of cesium and rubidium and enabled the chemical analysis of distant stars, revolutionizing astronomy."),
        "timeline": [
            {"year": 1845, "event": i18n("Formulated Kirchhoff's circuit laws while still a student.")},
            {"year": 1859, "event": i18n("Established the relationship between emission and absorption spectra (Kirchhoff's law of thermal radiation).")},
            {"year": 1860, "event": i18n("Discovered cesium with Robert Bunsen using spectroscopy.")},
            {"year": 1861, "event": i18n("Discovered rubidium with Robert Bunsen.")},
            {"year": 1862, "event": i18n("Introduced the concept of a blackbody radiator.")},
        ],
        "famous_works": [
            {"title": i18n("On the Relation between the Radiating and Absorbing Powers of Different Bodies"), "year": 1859, "description": i18n("Foundational paper establishing the law relating emission and absorption of thermal radiation.")},
            {"title": i18n("Chemical Analysis by Spectral Observations"), "year": 1860, "description": i18n("Landmark work with Bunsen establishing spectroscopy as a tool for chemical analysis.")},
            {"title": i18n("Kirchhoff's Circuit Laws"), "year": 1845, "description": i18n("Formulation of the current and voltage laws governing electrical circuits.")},
        ],
        "quotes": [
            {"text": i18n("The highest object at which the natural sciences are constrained to aim is the discovery of the ultimate and irreducible elements of which the universe is composed."), "source": "Lectures on Mathematical Physics"},
        ],
        "relations": [
            {"person": "hermann-von-helmholtz", "type": "colleague"},
            {"person": "max-planck", "type": "mentor"},
            {"person": "ludwig-boltzmann", "type": "colleague"},
        ],
    },
    {
        "id": "james-clerk-maxwell",
        "name": name_i18n("James Clerk Maxwell", "ジェームズ・クラーク・マクスウェル"),
        "birth_year": 1831,
        "death_year": 1879,
        "countries": ["gb"],
        "fields": ["physics"],
        "overview": i18n("James Clerk Maxwell was a Scottish physicist who unified electricity, magnetism, and optics into a single theoretical framework through his equations of electromagnetism. He is widely regarded as one of the most influential physicists in history, on par with Newton and Einstein."),
        "early_life": i18n("Born in Edinburgh, Scotland, Maxwell showed remarkable mathematical ability from a young age, publishing his first scientific paper at fourteen. He studied at the University of Edinburgh and then Cambridge, where he became one of the top students."),
        "impact": i18n("Maxwell's equations unified electricity, magnetism, and light into a single coherent theory, paving the way for radio, television, and modern telecommunications. His work on statistical mechanics and the kinetic theory of gases also laid essential foundations for modern physics."),
        "timeline": [
            {"year": 1855, "event": i18n("Published 'On Faraday's Lines of Force,' beginning his mathematical treatment of electromagnetism.")},
            {"year": 1861, "event": i18n("Produced the first color photograph, demonstrating the three-color process.")},
            {"year": 1864, "event": i18n("Presented 'A Dynamical Theory of the Electromagnetic Field,' unifying electricity, magnetism, and light.")},
            {"year": 1867, "event": i18n("Proposed the thought experiment known as Maxwell's demon in thermodynamics.")},
            {"year": 1871, "event": i18n("Became the first Cavendish Professor of Physics at Cambridge.")},
            {"year": 1873, "event": i18n("Published 'A Treatise on Electricity and Magnetism,' his masterwork.")},
        ],
        "famous_works": [
            {"title": i18n("A Dynamical Theory of the Electromagnetic Field"), "year": 1865, "description": i18n("The paper presenting Maxwell's equations unifying electricity, magnetism, and optics.")},
            {"title": i18n("A Treatise on Electricity and Magnetism"), "year": 1873, "description": i18n("Comprehensive two-volume treatise presenting the full mathematical framework of electromagnetism.")},
            {"title": i18n("On the Dynamical Theory of Gases"), "year": 1867, "description": i18n("Key paper developing the Maxwell-Boltzmann distribution in statistical mechanics.")},
        ],
        "quotes": [
            {"text": i18n("The special theory of electricity and magnetism, the undulatory theory of light, and the theory of heat are now unified."), "source": "A Dynamical Theory of the Electromagnetic Field, 1865"},
            {"text": i18n("In science, there are no authorities; only those who have investigated and those who have not."), "source": "Attributed"},
        ],
        "relations": [
            {"person": "ludwig-boltzmann", "type": "influenced"},
            {"person": "heinrich-hertz", "type": "influenced"},
            {"person": "lord-kelvin", "type": "colleague"},
            {"person": "hermann-von-helmholtz", "type": "colleague"},
        ],
    },
    {
        "id": "ludwig-boltzmann",
        "name": name_i18n("Ludwig Boltzmann", "ルートヴィヒ・ボルツマン"),
        "birth_year": 1844,
        "death_year": 1906,
        "countries": ["at"],
        "fields": ["physics"],
        "overview": i18n("Ludwig Boltzmann was an Austrian physicist who developed statistical mechanics, providing a microscopic explanation for the macroscopic laws of thermodynamics. His statistical interpretation of entropy bridged the gap between Newtonian mechanics and thermodynamics."),
        "early_life": i18n("Born in Vienna, Austria, Boltzmann studied physics at the University of Vienna, earning his doctorate in 1866. He was deeply influenced by the work of Maxwell and became a passionate advocate for the atomic theory of matter."),
        "impact": i18n("Boltzmann's statistical mechanics provided the theoretical foundation for understanding thermodynamic phenomena at the molecular level. His famous equation S = k log W, relating entropy to the number of microstates, is engraved on his tombstone and remains a cornerstone of physics."),
        "timeline": [
            {"year": 1866, "event": i18n("Earned his doctorate from the University of Vienna.")},
            {"year": 1872, "event": i18n("Published the Boltzmann equation and the H-theorem.")},
            {"year": 1877, "event": i18n("Formulated the statistical definition of entropy: S = k log W.")},
            {"year": 1884, "event": i18n("Derived the Stefan-Boltzmann law for blackbody radiation from thermodynamic principles.")},
            {"year": 1896, "event": i18n("Published 'Lectures on Gas Theory,' his comprehensive treatise on kinetic theory.")},
        ],
        "famous_works": [
            {"title": i18n("Further Studies on the Thermal Equilibrium of Gas Molecules"), "year": 1872, "description": i18n("Foundational paper introducing the Boltzmann equation and the H-theorem for irreversible processes.")},
            {"title": i18n("On the Relationship between the Second Law of Thermodynamics and Probability"), "year": 1877, "description": i18n("Paper establishing the statistical interpretation of entropy with the famous S = k log W formula.")},
            {"title": i18n("Lectures on Gas Theory"), "year": 1896, "description": i18n("Comprehensive treatise on the kinetic theory of gases and statistical mechanics.")},
        ],
        "quotes": [
            {"text": i18n("If you are out to describe the truth, leave elegance to the tailor."), "source": "Attributed"},
            {"text": i18n("Available energy is the main object at stake in the struggle for existence and the evolution of the world."), "source": "Lectures on Gas Theory, 1896"},
        ],
        "relations": [
            {"person": "james-clerk-maxwell", "type": "influenced_by"},
            {"person": "max-planck", "type": "influenced"},
            {"person": "josiah-willard-gibbs", "type": "colleague"},
            {"person": "rudolf-clausius", "type": "influenced_by"},
        ],
    },
    {
        "id": "lord-rayleigh",
        "name": name_i18n("Lord Rayleigh (John William Strutt)", "レイリー卿（ジョン・ウィリアム・ストラット）"),
        "birth_year": 1842,
        "death_year": 1919,
        "countries": ["gb"],
        "fields": ["physics"],
        "overview": i18n("Lord Rayleigh was an English physicist who made fundamental contributions to wave physics, acoustics, and the scattering of light. He won the Nobel Prize in Physics in 1904 for his discovery of argon and investigations of gas densities."),
        "early_life": i18n("Born John William Strutt in Langford Grove, Essex, he studied at Trinity College, Cambridge, where he excelled in mathematics. He succeeded Maxwell as the Cavendish Professor of Physics at Cambridge in 1879."),
        "impact": i18n("Rayleigh scattering explains why the sky is blue, and his work on wave phenomena influenced fields from acoustics to optics. His discovery of argon opened the door to the study of noble gases and earned him the Nobel Prize."),
        "timeline": [
            {"year": 1871, "event": i18n("Published his theory of light scattering, explaining why the sky is blue (Rayleigh scattering).")},
            {"year": 1877, "event": i18n("Published 'The Theory of Sound,' a comprehensive treatise on acoustics.")},
            {"year": 1879, "event": i18n("Became Cavendish Professor of Physics at Cambridge, succeeding Maxwell.")},
            {"year": 1894, "event": i18n("Discovered argon with William Ramsay.")},
            {"year": 1904, "event": i18n("Awarded the Nobel Prize in Physics for the discovery of argon.")},
        ],
        "famous_works": [
            {"title": i18n("The Theory of Sound"), "year": 1877, "description": i18n("Comprehensive two-volume treatise on acoustics and wave phenomena that became a standard reference.")},
            {"title": i18n("On the Light from the Sky, Its Polarisation and Colour"), "year": 1871, "description": i18n("Paper explaining the scattering of light by small particles, now known as Rayleigh scattering.")},
        ],
        "quotes": [
            {"text": i18n("The whole is simpler than the sum of its parts."), "source": "Attributed"},
        ],
        "relations": [
            {"person": "james-clerk-maxwell", "type": "influenced_by"},
            {"person": "jj-thomson", "type": "colleague"},
            {"person": "lord-kelvin", "type": "colleague"},
        ],
    },
    {
        "id": "josiah-willard-gibbs",
        "name": name_i18n("Josiah Willard Gibbs", "ジョサイア・ウィラード・ギブズ"),
        "birth_year": 1839,
        "death_year": 1903,
        "countries": ["us"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Josiah Willard Gibbs was an American scientist who made foundational contributions to thermodynamics, statistical mechanics, and vector calculus. He is considered one of the greatest American scientists of the 19th century."),
        "early_life": i18n("Born in New Haven, Connecticut, Gibbs was the son of a Yale professor. He studied at Yale and earned one of the first PhD degrees granted in the United States, then spent three years studying in Europe before returning to Yale."),
        "impact": i18n("Gibbs's work on chemical thermodynamics introduced the concept of free energy and the phase rule, which became essential tools in chemistry and materials science. His development of statistical mechanics independently of Boltzmann provided an elegant mathematical framework for the field."),
        "timeline": [
            {"year": 1863, "event": i18n("Received one of the first engineering PhDs in the United States from Yale.")},
            {"year": 1873, "event": i18n("Published his first papers on geometric methods in thermodynamics.")},
            {"year": 1876, "event": i18n("Published 'On the Equilibrium of Heterogeneous Substances,' his masterwork.")},
            {"year": 1881, "event": i18n("Developed vector analysis as a simplification of quaternion methods.")},
            {"year": 1902, "event": i18n("Published 'Elementary Principles in Statistical Mechanics.'")},
        ],
        "famous_works": [
            {"title": i18n("On the Equilibrium of Heterogeneous Substances"), "year": 1876, "description": i18n("Landmark paper establishing the foundations of chemical thermodynamics, introducing Gibbs free energy and the phase rule.")},
            {"title": i18n("Elementary Principles in Statistical Mechanics"), "year": 1902, "description": i18n("Comprehensive treatise developing statistical mechanics from first principles using ensemble theory.")},
            {"title": i18n("Vector Analysis"), "year": 1881, "description": i18n("Development of modern vector calculus notation, replacing the more cumbersome quaternion formalism.")},
        ],
        "quotes": [
            {"text": i18n("One of the principal objects of theoretical research in any department of knowledge is to find the point of view from which the subject appears in its greatest simplicity."), "source": "On the Equilibrium of Heterogeneous Substances, 1876"},
            {"text": i18n("Mathematics is a language."), "source": "Attributed"},
        ],
        "relations": [
            {"person": "ludwig-boltzmann", "type": "colleague"},
            {"person": "james-clerk-maxwell", "type": "influenced_by"},
            {"person": "max-planck", "type": "influenced"},
        ],
    },
    {
        "id": "hermann-von-helmholtz",
        "name": name_i18n("Hermann von Helmholtz", "ヘルマン・フォン・ヘルムホルツ"),
        "birth_year": 1821,
        "death_year": 1894,
        "countries": ["de"],
        "fields": ["physics", "biology"],
        "overview": i18n("Hermann von Helmholtz was a German physicist and physician who made fundamental contributions to the conservation of energy, optics, electrodynamics, and the physiology of perception. He was one of the most versatile scientists of the 19th century."),
        "early_life": i18n("Born in Potsdam, Prussia, Helmholtz initially trained as a military physician due to financial constraints. His broad interests led him to study physics alongside medicine, and he quickly established himself as a leading figure in both fields."),
        "impact": i18n("Helmholtz's mathematical formulation of the conservation of energy was one of the most important achievements of 19th-century physics. His work on the physiology of vision and hearing bridged physics and biology, and he mentored a generation of leading physicists including Hertz and Planck."),
        "timeline": [
            {"year": 1847, "event": i18n("Published 'On the Conservation of Force,' establishing the mathematical basis for conservation of energy.")},
            {"year": 1850, "event": i18n("Measured the speed of nerve impulses for the first time.")},
            {"year": 1851, "event": i18n("Invented the ophthalmoscope for examining the interior of the eye.")},
            {"year": 1856, "event": i18n("Published the first volume of 'Handbook of Physiological Optics.'")},
            {"year": 1863, "event": i18n("Published 'On the Sensations of Tone,' a major work on acoustics and music perception.")},
            {"year": 1871, "event": i18n("Became professor of physics at the University of Berlin.")},
        ],
        "famous_works": [
            {"title": i18n("On the Conservation of Force"), "year": 1847, "description": i18n("Seminal paper providing a mathematical formulation of the principle of conservation of energy.")},
            {"title": i18n("Handbook of Physiological Optics"), "year": 1856, "description": i18n("Comprehensive treatise on the physics and physiology of vision, a foundational text in the field.")},
            {"title": i18n("On the Sensations of Tone"), "year": 1863, "description": i18n("Major work bridging physics and physiology in the study of acoustics and musical perception.")},
        ],
        "quotes": [
            {"text": i18n("Whoever, in the pursuit of science, seeks after immediate practical utility may rest assured that he will seek in vain."), "source": "Academic Discourse, 1862"},
            {"text": i18n("All science is either physics or stamp collecting."), "source": "Attributed (also attributed to Rutherford)"},
        ],
        "relations": [
            {"person": "heinrich-hertz", "type": "mentor"},
            {"person": "max-planck", "type": "mentor"},
            {"person": "lord-kelvin", "type": "friend"},
            {"person": "james-clerk-maxwell", "type": "colleague"},
            {"person": "gustav-kirchhoff", "type": "colleague"},
        ],
    },
    {
        "id": "heinrich-hertz",
        "name": name_i18n("Heinrich Hertz", "ハインリヒ・ヘルツ"),
        "birth_year": 1857,
        "death_year": 1894,
        "countries": ["de"],
        "fields": ["physics"],
        "overview": i18n("Heinrich Hertz was a German physicist who first conclusively proved the existence of electromagnetic waves predicted by Maxwell's theory. His experiments demonstrated that electromagnetic waves travel at the speed of light and can be reflected, refracted, and polarized."),
        "early_life": i18n("Born in Hamburg, Germany, Hertz studied engineering and physics at the University of Berlin under Helmholtz. He showed exceptional experimental skill and quickly rose to academic positions at the Universities of Kiel and Bonn."),
        "impact": i18n("Hertz's experimental confirmation of electromagnetic waves opened the door to radio communication, television, and all wireless technology. The SI unit of frequency, the hertz, is named in his honor, reflecting the profound importance of his discoveries."),
        "timeline": [
            {"year": 1880, "event": i18n("Earned his PhD under Hermann von Helmholtz at the University of Berlin.")},
            {"year": 1886, "event": i18n("Began experiments to detect electromagnetic waves.")},
            {"year": 1887, "event": i18n("Successfully generated and detected electromagnetic waves, confirming Maxwell's theory.")},
            {"year": 1887, "event": i18n("Observed the photoelectric effect during his electromagnetic wave experiments.")},
            {"year": 1892, "event": i18n("Published 'Electric Waves,' compiling his experimental results on electromagnetism.")},
        ],
        "famous_works": [
            {"title": i18n("On Electromagnetic Effects Produced by Electrical Disturbances in Insulators"), "year": 1887, "description": i18n("Landmark paper reporting the first experimental detection of electromagnetic waves.")},
            {"title": i18n("Electric Waves"), "year": 1893, "description": i18n("Comprehensive collection of Hertz's experimental work on electromagnetic waves.")},
        ],
        "quotes": [
            {"text": i18n("I do not think that the wireless waves I have discovered will have any practical application."), "source": "Attributed, c. 1890"},
            {"text": i18n("It is of no use whatsoever. This is just an experiment that proves Maestro Maxwell was right."), "source": "When asked about the practical use of his discoveries"},
        ],
        "relations": [
            {"person": "hermann-von-helmholtz", "type": "student"},
            {"person": "james-clerk-maxwell", "type": "influenced_by"},
            {"person": "nikola-tesla", "type": "colleague"},
            {"person": "philipp-lenard", "type": "mentor"},
        ],
    },
    {
        "id": "nikola-tesla",
        "name": name_i18n("Nikola Tesla", "ニコラ・テスラ"),
        "birth_year": 1856,
        "death_year": 1943,
        "countries": ["rs", "us"],
        "fields": ["physics", "engineering"],
        "overview": i18n("Nikola Tesla was a Serbian-American inventor and electrical engineer who developed the alternating current (AC) electrical system and made pioneering contributions to electromagnetism and wireless communication. His inventions and theoretical work helped shape the modern electrical power industry."),
        "early_life": i18n("Born in Smiljan, in the Austrian Empire (modern-day Croatia), Tesla studied engineering in Graz and Prague. He emigrated to the United States in 1884 and briefly worked for Thomas Edison before striking out on his own."),
        "impact": i18n("Tesla's AC motor and polyphase electrical system became the worldwide standard for electrical power distribution. His work on radio technology, wireless energy transmission, and high-voltage experiments made him one of the most visionary inventors of the modern era."),
        "timeline": [
            {"year": 1884, "event": i18n("Emigrated to the United States and began working for Thomas Edison.")},
            {"year": 1887, "event": i18n("Filed patents for his AC induction motor and polyphase power system.")},
            {"year": 1891, "event": i18n("Invented the Tesla coil, a resonant transformer circuit.")},
            {"year": 1893, "event": i18n("Demonstrated AC power at the World's Columbian Exposition in Chicago.")},
            {"year": 1899, "event": i18n("Conducted high-voltage experiments at his laboratory in Colorado Springs.")},
            {"year": 1901, "event": i18n("Began construction of the Wardenclyffe Tower for wireless communication.")},
        ],
        "famous_works": [
            {"title": i18n("Alternating Current Induction Motor"), "year": 1887, "description": i18n("Patent for the AC induction motor that became the basis for modern electrical power systems.")},
            {"title": i18n("Tesla Coil"), "year": 1891, "description": i18n("Invention of the resonant transformer circuit used in radio technology and high-voltage experiments.")},
            {"title": i18n("Polyphase Alternating Current System"), "year": 1888, "description": i18n("System for generating, transmitting, and using alternating current power that became the global standard.")},
        ],
        "quotes": [
            {"text": i18n("The present is theirs; the future, for which I really worked, is mine."), "source": "Attributed, c. 1900"},
            {"text": i18n("If you want to find the secrets of the universe, think in terms of energy, frequency and vibration."), "source": "Attributed"},
        ],
        "relations": [
            {"person": "heinrich-hertz", "type": "colleague"},
            {"person": "lord-kelvin", "type": "friend"},
            {"person": "hendrik-lorentz", "type": "colleague"},
        ],
    },
    {
        "id": "wilhelm-rontgen",
        "name": name_i18n("Wilhelm Röntgen", "ヴィルヘルム・レントゲン"),
        "birth_year": 1845,
        "death_year": 1923,
        "countries": ["de"],
        "fields": ["physics"],
        "overview": i18n("Wilhelm Röntgen was a German physicist who discovered X-rays in 1895, a breakthrough that revolutionized medicine and earned him the first Nobel Prize in Physics in 1901. His discovery opened entirely new fields in medical imaging and materials science."),
        "early_life": i18n("Born in Lennep, Prussia, Röntgen studied mechanical engineering at the ETH Zurich and later earned his PhD in physics. He held professorships at several German universities, becoming known for his careful experimental work."),
        "impact": i18n("Röntgen's discovery of X-rays transformed medical diagnosis by enabling doctors to see inside the human body without surgery. His work also spurred the discovery of radioactivity and led to advances in crystallography, materials science, and nuclear physics."),
        "timeline": [
            {"year": 1869, "event": i18n("Earned his PhD from the University of Zurich.")},
            {"year": 1895, "event": i18n("Discovered X-rays while experimenting with cathode rays.")},
            {"year": 1896, "event": i18n("Published his findings on X-rays, including the famous image of his wife's hand.")},
            {"year": 1901, "event": i18n("Awarded the first Nobel Prize in Physics for his discovery of X-rays.")},
        ],
        "famous_works": [
            {"title": i18n("On a New Kind of Rays"), "year": 1895, "description": i18n("Original paper announcing the discovery of X-rays and describing their remarkable properties.")},
            {"title": i18n("Further Observations on the Properties of X-Rays"), "year": 1897, "description": i18n("Follow-up investigations characterizing the nature and behavior of X-rays.")},
        ],
        "quotes": [
            {"text": i18n("I did not think; I investigated."), "source": "When asked what he thought upon discovering X-rays"},
        ],
        "relations": [
            {"person": "henri-becquerel", "type": "influenced"},
            {"person": "philipp-lenard", "type": "colleague"},
            {"person": "max-planck", "type": "colleague"},
        ],
    },
    {
        "id": "henri-becquerel",
        "name": name_i18n("Henri Becquerel", "アンリ・ベクレル"),
        "birth_year": 1852,
        "death_year": 1908,
        "countries": ["fr"],
        "fields": ["physics"],
        "overview": i18n("Henri Becquerel was a French physicist who discovered radioactivity in 1896, a finding that fundamentally changed our understanding of matter and energy. He shared the 1903 Nobel Prize in Physics with Pierre and Marie Curie for this groundbreaking work."),
        "early_life": i18n("Born in Paris into a distinguished family of scientists, Becquerel was the son and grandson of physicists. He studied at the École Polytechnique and the École des Ponts et Chaussées, eventually succeeding his father as professor at the Muséum National d'Histoire Naturelle."),
        "impact": i18n("Becquerel's discovery of spontaneous radioactivity opened an entirely new branch of physics and chemistry. His work directly inspired the Curies' research and ultimately led to nuclear physics, nuclear energy, and modern medical treatments using radiation."),
        "timeline": [
            {"year": 1896, "event": i18n("Discovered radioactivity while studying the phosphorescence of uranium salts.")},
            {"year": 1896, "event": i18n("Demonstrated that the radiation from uranium was not related to phosphorescence.")},
            {"year": 1900, "event": i18n("Showed that the radiation from radium could be deflected by magnetic fields.")},
            {"year": 1903, "event": i18n("Awarded the Nobel Prize in Physics jointly with Pierre and Marie Curie.")},
        ],
        "famous_works": [
            {"title": i18n("On the Rays Emitted by Phosphorescence"), "year": 1896, "description": i18n("Initial report of the discovery of radioactivity from uranium salts.")},
            {"title": i18n("On the Invisible Rays Emitted by Phosphorescent Bodies"), "year": 1896, "description": i18n("Follow-up paper demonstrating that the radiation was a new phenomenon distinct from phosphorescence.")},
        ],
        "quotes": [
            {"text": i18n("The discovery was not the result of a search, but of a fortunate accident."), "source": "On the discovery of radioactivity, attributed"},
        ],
        "relations": [
            {"person": "pierre-curie", "type": "colleague"},
            {"person": "marie-curie", "type": "colleague"},
            {"person": "wilhelm-rontgen", "type": "influenced_by"},
        ],
    },
    {
        "id": "hendrik-lorentz",
        "name": name_i18n("Hendrik Lorentz", "ヘンドリック・ローレンツ"),
        "birth_year": 1853,
        "death_year": 1928,
        "countries": ["nl"],
        "fields": ["physics"],
        "overview": i18n("Hendrik Lorentz was a Dutch physicist who developed the Lorentz transformation equations and the electron theory of matter. He shared the 1902 Nobel Prize in Physics and his mathematical framework became essential to Einstein's special theory of relativity."),
        "early_life": i18n("Born in Arnhem, Netherlands, Lorentz studied at Leiden University, earning his PhD at age 22. He became professor of theoretical physics at Leiden at 24, one of the youngest professors in Europe at the time."),
        "impact": i18n("Lorentz's transformation equations provided the mathematical foundation for special relativity, and his electron theory helped bridge classical and modern physics. He was universally respected and served as a guiding figure for an entire generation of European physicists."),
        "timeline": [
            {"year": 1875, "event": i18n("Earned his PhD from Leiden University at age 22.")},
            {"year": 1878, "event": i18n("Became professor of theoretical physics at Leiden University.")},
            {"year": 1895, "event": i18n("Introduced the Lorentz transformation to explain the Michelson-Morley experiment.")},
            {"year": 1899, "event": i18n("Refined the Lorentz transformation, introducing the concept of local time.")},
            {"year": 1902, "event": i18n("Awarded the Nobel Prize in Physics jointly with Pieter Zeeman.")},
        ],
        "famous_works": [
            {"title": i18n("Attempt of a Theory of Electrical and Optical Phenomena in Moving Bodies"), "year": 1895, "description": i18n("Paper introducing the Lorentz transformation to reconcile electromagnetism with the principle of relativity.")},
            {"title": i18n("The Theory of Electrons"), "year": 1909, "description": i18n("Comprehensive work presenting Lorentz's electron theory and its applications to electromagnetic phenomena.")},
        ],
        "quotes": [
            {"text": i18n("I am unable to believe that the ether does not exist, but I am equally unable to believe that it has the properties which have been attributed to it."), "source": "Attributed, c. 1910"},
        ],
        "relations": [
            {"person": "max-planck", "type": "colleague"},
            {"person": "henri-becquerel", "type": "colleague"},
            {"person": "jj-thomson", "type": "colleague"},
            {"person": "james-clerk-maxwell", "type": "influenced_by"},
        ],
    },
    {
        "id": "jj-thomson",
        "name": name_i18n("J. J. Thomson", "J・J・トムソン"),
        "birth_year": 1856,
        "death_year": 1940,
        "countries": ["gb"],
        "fields": ["physics"],
        "overview": i18n("J. J. Thomson was an English physicist who discovered the electron in 1897, fundamentally changing our understanding of atomic structure. He won the Nobel Prize in Physics in 1906 and led the Cavendish Laboratory during one of its most productive periods."),
        "early_life": i18n("Born in Cheetham Hill, Manchester, Thomson entered Owens College at age 14 and later studied at Trinity College, Cambridge. He became Cavendish Professor of Physics at Cambridge at the remarkably young age of 28."),
        "impact": i18n("Thomson's discovery of the electron proved that atoms are not indivisible and opened the era of subatomic physics. His plum pudding model of the atom, while later superseded, was the first attempt to describe internal atomic structure and inspired Rutherford's nuclear model."),
        "timeline": [
            {"year": 1884, "event": i18n("Became Cavendish Professor of Physics at Cambridge at age 28.")},
            {"year": 1897, "event": i18n("Discovered the electron through cathode ray experiments.")},
            {"year": 1904, "event": i18n("Proposed the plum pudding model of the atom.")},
            {"year": 1906, "event": i18n("Awarded the Nobel Prize in Physics for his work on electrical conductivity in gases.")},
            {"year": 1913, "event": i18n("Discovered the existence of isotopes through positive ray analysis.")},
        ],
        "famous_works": [
            {"title": i18n("Cathode Rays"), "year": 1897, "description": i18n("Landmark paper announcing the discovery of the electron and measuring its charge-to-mass ratio.")},
            {"title": i18n("On the Structure of the Atom"), "year": 1904, "description": i18n("Paper proposing the plum pudding model of atomic structure.")},
            {"title": i18n("Rays of Positive Electricity and Their Application to Chemical Analyses"), "year": 1913, "description": i18n("Work describing the discovery of isotopes using positive ray analysis.")},
        ],
        "quotes": [
            {"text": i18n("Could anything at first sight seem more impractical than a body which is so small that its mass is an insignificant fraction of the mass of an atom of hydrogen?"), "source": "Nobel Lecture, 1906"},
        ],
        "relations": [
            {"person": "ernest-rutherford", "type": "mentor"},
            {"person": "lord-rayleigh", "type": "colleague"},
            {"person": "hendrik-lorentz", "type": "colleague"},
            {"person": "max-planck", "type": "colleague"},
        ],
    },
    {
        "id": "max-planck",
        "name": name_i18n("Max Planck", "マックス・プランク"),
        "birth_year": 1858,
        "death_year": 1947,
        "countries": ["de"],
        "fields": ["physics"],
        "overview": i18n("Max Planck was a German physicist who originated quantum theory by introducing the concept of energy quanta to explain blackbody radiation. His revolutionary insight that energy is emitted in discrete packets marked the birth of modern physics."),
        "early_life": i18n("Born in Kiel, Germany, Planck came from an academic family. He studied at the Universities of Munich and Berlin under Kirchhoff and Helmholtz, initially focusing on thermodynamics before turning his attention to the problem of blackbody radiation."),
        "impact": i18n("Planck's quantum hypothesis fundamentally changed physics by revealing that energy at the atomic scale comes in discrete units. His constant, h, is one of the most fundamental constants in nature, and his work opened the door to quantum mechanics, one of the pillars of modern physics."),
        "timeline": [
            {"year": 1879, "event": i18n("Earned his PhD from the University of Munich with a thesis on the second law of thermodynamics.")},
            {"year": 1889, "event": i18n("Became professor at the University of Berlin.")},
            {"year": 1900, "event": i18n("Introduced the quantum hypothesis to solve the blackbody radiation problem.")},
            {"year": 1918, "event": i18n("Awarded the Nobel Prize in Physics for his discovery of energy quanta.")},
            {"year": 1930, "event": i18n("Became president of the Kaiser Wilhelm Society (later Max Planck Society).")},
        ],
        "famous_works": [
            {"title": i18n("On the Law of Distribution of Energy in the Normal Spectrum"), "year": 1900, "description": i18n("The paper introducing the quantum hypothesis and Planck's constant to explain blackbody radiation.")},
            {"title": i18n("The Theory of Heat Radiation"), "year": 1906, "description": i18n("Comprehensive treatise on radiation theory incorporating quantum concepts.")},
            {"title": i18n("Introduction to Theoretical Physics"), "year": 1916, "description": i18n("Multi-volume textbook series covering the major branches of theoretical physics.")},
        ],
        "quotes": [
            {"text": i18n("A new scientific truth does not triumph by convincing its opponents and making them see the light, but rather because its opponents eventually die, and a new generation grows up that is familiar with it."), "source": "Scientific Autobiography, 1948"},
            {"text": i18n("Science cannot solve the ultimate mystery of nature because we ourselves are part of the mystery that we are trying to solve."), "source": "Where Is Science Going?, 1932"},
        ],
        "relations": [
            {"person": "gustav-kirchhoff", "type": "student"},
            {"person": "hermann-von-helmholtz", "type": "student"},
            {"person": "ludwig-boltzmann", "type": "influenced_by"},
            {"person": "hendrik-lorentz", "type": "colleague"},
        ],
    },
    {
        "id": "pierre-curie",
        "name": name_i18n("Pierre Curie", "ピエール・キュリー"),
        "birth_year": 1859,
        "death_year": 1906,
        "countries": ["fr"],
        "fields": ["physics"],
        "overview": i18n("Pierre Curie was a French physicist who made fundamental contributions to the understanding of crystallography, magnetism, and radioactivity. Together with his wife Marie Curie, he shared the 1903 Nobel Prize in Physics for their research on radiation."),
        "early_life": i18n("Born in Paris, Pierre Curie was educated at home by his father before studying at the Sorbonne. He and his brother Jacques discovered piezoelectricity in 1880, establishing Pierre's reputation as an innovative experimentalist."),
        "impact": i18n("Pierre Curie's work on piezoelectricity and magnetism (the Curie point) made lasting contributions to materials science. His collaboration with Marie on radioactivity led to the discovery of polonium and radium, transforming our understanding of atomic physics."),
        "timeline": [
            {"year": 1880, "event": i18n("Discovered piezoelectricity with his brother Jacques Curie.")},
            {"year": 1895, "event": i18n("Published his doctoral thesis on magnetism, introducing the Curie point and Curie's law.")},
            {"year": 1898, "event": i18n("Discovered polonium and radium with Marie Curie.")},
            {"year": 1903, "event": i18n("Awarded the Nobel Prize in Physics jointly with Marie Curie and Henri Becquerel.")},
            {"year": 1905, "event": i18n("Elected to the French Academy of Sciences.")},
        ],
        "famous_works": [
            {"title": i18n("Magnetic Properties of Bodies at Various Temperatures"), "year": 1895, "description": i18n("Doctoral thesis establishing the relationship between temperature and magnetism, introducing the Curie point.")},
            {"title": i18n("On a New Radioactive Substance Contained in Pitchblende"), "year": 1898, "description": i18n("Paper announcing the discovery of radium, co-authored with Marie Curie and Gustave Bémont.")},
        ],
        "quotes": [
            {"text": i18n("It would be a fine thing, in which I hardly dare believe, to pass our lives near each other, hypnotized by our dreams."), "source": "Letter to Marie Curie, 1894"},
        ],
        "relations": [
            {"person": "marie-curie", "type": "collaborator"},
            {"person": "henri-becquerel", "type": "colleague"},
            {"person": "lord-kelvin", "type": "colleague"},
        ],
    },
    {
        "id": "marie-curie",
        "name": name_i18n("Marie Curie", "マリ・キュリー"),
        "birth_year": 1867,
        "death_year": 1934,
        "countries": ["pl", "fr"],
        "fields": ["physics", "chemistry"],
        "overview": i18n("Marie Curie was a Polish-French physicist and chemist who pioneered research on radioactivity. She was the first woman to win a Nobel Prize, the first person to win Nobel Prizes in two different sciences, and remains one of the most celebrated scientists in history."),
        "early_life": i18n("Born Maria Sklodowska in Warsaw, Poland, she moved to Paris in 1891 to study at the Sorbonne. Despite financial hardship, she earned degrees in both physics and mathematics and met Pierre Curie, whom she married in 1895."),
        "impact": i18n("Marie Curie's discovery of polonium and radium and her research on radioactivity transformed physics and chemistry. Her work led to the development of X-ray machines used in World War I field hospitals and laid the foundations for nuclear physics and cancer treatment."),
        "timeline": [
            {"year": 1891, "event": i18n("Moved to Paris to study physics and mathematics at the Sorbonne.")},
            {"year": 1898, "event": i18n("Discovered polonium and radium with Pierre Curie.")},
            {"year": 1903, "event": i18n("Awarded the Nobel Prize in Physics jointly with Pierre Curie and Henri Becquerel.")},
            {"year": 1906, "event": i18n("Became the first female professor at the Sorbonne after Pierre's death.")},
            {"year": 1911, "event": i18n("Awarded the Nobel Prize in Chemistry for isolating pure radium.")},
        ],
        "famous_works": [
            {"title": i18n("Researches on Radioactive Substances"), "year": 1904, "description": i18n("Comprehensive thesis compiling her groundbreaking research on radioactivity, polonium, and radium.")},
            {"title": i18n("Treatise on Radioactivity"), "year": 1910, "description": i18n("Two-volume treatise establishing radioactivity as a distinct branch of science.")},
            {"title": i18n("On a New Radioactive Substance Contained in Pitchblende"), "year": 1898, "description": i18n("Paper announcing the discovery of radium, co-authored with Pierre Curie.")},
        ],
        "quotes": [
            {"text": i18n("Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less."), "source": "Attributed"},
            {"text": i18n("I was taught that the way of progress was neither swift nor easy."), "source": "Attributed"},
        ],
        "relations": [
            {"person": "pierre-curie", "type": "collaborator"},
            {"person": "henri-becquerel", "type": "colleague"},
            {"person": "ernest-rutherford", "type": "colleague"},
        ],
    },
    {
        "id": "ernest-rutherford",
        "name": name_i18n("Ernest Rutherford", "アーネスト・ラザフォード"),
        "birth_year": 1871,
        "death_year": 1937,
        "countries": ["nz", "gb"],
        "fields": ["physics", "chemistry"],
        "overview": i18n("Ernest Rutherford was a New Zealand-born British physicist who is considered the father of nuclear physics. He discovered the atomic nucleus, proposed the nuclear model of the atom, and performed the first artificial nuclear reaction."),
        "early_life": i18n("Born in Brightwater, New Zealand, Rutherford won a scholarship to study at Canterbury College and then at the Cavendish Laboratory under J. J. Thomson. His experimental brilliance was recognized early, and he quickly made a name for himself in the study of radioactivity."),
        "impact": i18n("Rutherford's discovery of the atomic nucleus and his nuclear model of the atom overturned the prevailing plum pudding model and reshaped atomic physics. His work on radioactive decay, alpha particles, and nuclear transmutation laid the foundations for nuclear energy and particle physics."),
        "timeline": [
            {"year": 1895, "event": i18n("Arrived at the Cavendish Laboratory in Cambridge to study under J. J. Thomson.")},
            {"year": 1899, "event": i18n("Identified alpha and beta radiation as distinct types of radioactive emission.")},
            {"year": 1908, "event": i18n("Awarded the Nobel Prize in Chemistry for his investigations into the disintegration of elements.")},
            {"year": 1911, "event": i18n("Discovered the atomic nucleus through the gold foil experiment.")},
            {"year": 1917, "event": i18n("Performed the first artificial nuclear reaction by transmuting nitrogen into oxygen.")},
            {"year": 1919, "event": i18n("Succeeded J. J. Thomson as director of the Cavendish Laboratory.")},
        ],
        "famous_works": [
            {"title": i18n("The Scattering of Alpha and Beta Particles by Matter and the Structure of the Atom"), "year": 1911, "description": i18n("Paper presenting the nuclear model of the atom based on the gold foil scattering experiments.")},
            {"title": i18n("Radioactive Substances and Their Radiations"), "year": 1913, "description": i18n("Comprehensive treatise on radioactivity and the properties of radioactive materials.")},
            {"title": i18n("Collision of Alpha Particles with Light Atoms"), "year": 1919, "description": i18n("Paper reporting the first artificial nuclear transmutation.")},
        ],
        "quotes": [
            {"text": i18n("All science is either physics or stamp collecting."), "source": "Attributed, c. 1910"},
            {"text": i18n("If your experiment needs statistics, you ought to have done a better experiment."), "source": "Attributed"},
        ],
        "relations": [
            {"person": "jj-thomson", "type": "student"},
            {"person": "marie-curie", "type": "colleague"},
            {"person": "max-planck", "type": "colleague"},
            {"person": "henri-becquerel", "type": "colleague"},
        ],
    },
    {
        "id": "philipp-lenard",
        "name": name_i18n("Philipp Lenard", "フィリップ・レーナルト"),
        "birth_year": 1862,
        "death_year": 1947,
        "countries": ["hu", "de"],
        "fields": ["physics"],
        "overview": i18n("Philipp Lenard was a Hungarian-German physicist who made significant contributions to the study of cathode rays and the photoelectric effect. He won the Nobel Prize in Physics in 1905 for his work on cathode rays."),
        "early_life": i18n("Born in Pressburg (now Bratislava), in the Kingdom of Hungary, Lenard studied physics in Budapest, Vienna, and Berlin. He worked as an assistant to Heinrich Hertz at the University of Bonn, which deeply shaped his early research career."),
        "impact": i18n("Lenard's experiments on cathode rays and the photoelectric effect provided crucial experimental evidence that helped shape early quantum theory. His observation that the energy of photoelectrons depends on light frequency, not intensity, was later explained by Einstein's photon theory."),
        "timeline": [
            {"year": 1892, "event": i18n("Developed the Lenard window for studying cathode rays outside vacuum tubes.")},
            {"year": 1894, "event": i18n("Succeeded Heinrich Hertz as professor at the University of Bonn.")},
            {"year": 1902, "event": i18n("Published detailed studies on the photoelectric effect.")},
            {"year": 1905, "event": i18n("Awarded the Nobel Prize in Physics for his work on cathode rays.")},
        ],
        "famous_works": [
            {"title": i18n("On Cathode Rays"), "year": 1894, "description": i18n("Systematic experimental study of cathode rays using the Lenard window technique.")},
            {"title": i18n("On the Photoelectric Effect"), "year": 1902, "description": i18n("Detailed investigation showing that photoelectron energy depends on light frequency, a key observation for quantum theory.")},
        ],
        "quotes": [
            {"text": i18n("The most important thing in science is not so much to obtain new facts as to discover new ways of thinking about them."), "source": "Attributed"},
        ],
        "relations": [
            {"person": "heinrich-hertz", "type": "student"},
            {"person": "wilhelm-rontgen", "type": "colleague"},
            {"person": "jj-thomson", "type": "colleague"},
        ],
    },
]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for person in PHYSICISTS:
        filepath = os.path.join(OUTPUT_DIR, f"{person['id']}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(person, f, ensure_ascii=False, indent=2)
        print(f"Created {filepath}")
    print(f"\nDone. Generated {len(PHYSICISTS)} files.")


if __name__ == "__main__":
    main()
