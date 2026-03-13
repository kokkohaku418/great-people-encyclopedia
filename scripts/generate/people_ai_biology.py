#!/usr/bin/env python3
"""Generate ~100 biologists."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

p("charles-darwin", "Charles Darwin", "チャールズ・ダーウィン", 1809, 1882, ["gb"], ["biology"],
  "Charles Darwin was an English naturalist who proposed the theory of evolution by natural selection, fundamentally changing our understanding of life on Earth.",
  "Darwin was born in Shrewsbury, England. He studied medicine at Edinburgh and theology at Cambridge before embarking on the five-year voyage of HMS Beagle.",
  "Darwin's theory of evolution by natural selection is the unifying theory of the life sciences. It explains the diversity of life and has implications for medicine, agriculture, and conservation.",
  [(1831, "Embarked on HMS Beagle voyage"), (1838, "Formulated theory of natural selection"), (1859, "Published On the Origin of Species"), (1871, "Published The Descent of Man")],
  [("On the Origin of Species", 1859, "Presented the theory of evolution by natural selection"), ("The Descent of Man", 1871, "Applied evolutionary theory to human origins")],
  [("There is grandeur in this view of life.", "On the Origin of Species")])

p("gregor-mendel", "Gregor Mendel", "グレゴール・メンデル", 1822, 1884, ["at", "cz"], ["biology"],
  "Gregor Mendel was an Augustinian friar and scientist who discovered the fundamental laws of inheritance through his experiments with pea plants.",
  "Mendel was born in Hynčice, Moravia. He entered the Augustinian monastery in Brno and studied physics and natural science at the University of Vienna.",
  "Mendel's laws of inheritance form the foundation of modern genetics. His work, unrecognized during his lifetime, was rediscovered in 1900 and transformed biology.",
  [(1856, "Began pea plant experiments"), (1866, "Published Experiments on Plant Hybridization"), (1868, "Became abbot of the monastery")],
  [("Experiments on Plant Hybridization", 1866, "Described the fundamental laws of genetic inheritance")],
  [("My time will come.", "Attributed")])

p("carl-linnaeus", "Carl Linnaeus", "カール・リンネ", 1707, 1778, ["se"], ["biology"],
  "Carl Linnaeus was a Swedish botanist, zoologist, and physician who formalized binomial nomenclature, the modern system of naming organisms.",
  "Linnaeus was born in Råshult, Sweden. His father was an amateur botanist, and young Carl showed a passion for plants from an early age. He studied at Uppsala University.",
  "Linnaeus's system of binomial nomenclature brought order to the classification of living organisms and remains the universal standard in biology today.",
  [(1735, "Published Systema Naturae"), (1737, "Published Genera Plantarum"), (1753, "Published Species Plantarum"), (1758, "Published 10th edition of Systema Naturae")],
  [("Systema Naturae", 1735, "Established the system of taxonomic classification"), ("Species Plantarum", 1753, "Comprehensive catalog of all known plant species using binomial nomenclature")],
  [("If you do not know the names of things, the knowledge of them is lost too.", "Philosophia Botanica")])

p("alexander-von-humboldt", "Alexander von Humboldt", "アレクサンダー・フォン・フンボルト", 1769, 1859, ["de"], ["biology", "astronomy"],
  "Alexander von Humboldt was a Prussian naturalist and explorer whose quantitative work on botanical geography laid the foundation for biogeography and ecology.",
  "Humboldt was born in Berlin into an aristocratic family. He studied at several German universities and the Freiberg School of Mines before embarking on a transformative expedition to the Americas.",
  "Humboldt's holistic view of nature as an interconnected whole inspired Charles Darwin and founded the fields of biogeography and ecology. His concept of isothermal lines transformed climatology.",
  [(1799, "Began five-year expedition to the Americas"), (1807, "Published Essay on the Geography of Plants"), (1845, "Began publishing Cosmos")],
  [("Cosmos", 1845, "A comprehensive account of the physical world seeking to unify all natural sciences"), ("Essay on the Geography of Plants", 1807, "Foundational work in biogeography")],
  [("The most dangerous worldview is the worldview of those who have not viewed the world.", "Attributed")])

p("antonie-van-leeuwenhoek", "Antonie van Leeuwenhoek", "アントニ・ファン・レーウェンフック", 1632, 1723, ["nl"], ["biology"],
  "Antonie van Leeuwenhoek was a Dutch businessman and scientist, often called the father of microbiology. He was the first to observe bacteria and protozoa using microscopes he built himself.",
  "Van Leeuwenhoek was born in Delft, Netherlands. He was a draper and haberdasher who developed skill in grinding lenses and built simple but powerful single-lens microscopes.",
  "Van Leeuwenhoek's observations of microorganisms opened an entirely new world to science. His meticulous descriptions of bacteria, blood cells, and sperm cells founded microbiology.",
  [(1674, "Observed protozoa for the first time"), (1676, "Observed bacteria"), (1677, "Described spermatozoa"), (1683, "Drew bacteria from dental plaque")],
  [("Letter to the Royal Society", 1676, "First descriptions of bacteria and protozoa observed through his microscopes")],
  [("My work, which I've done for a long time, was not pursued in order to gain the praise I now enjoy.", "Letter to the Royal Society")])

p("robert-hooke", "Robert Hooke", "ロバート・フック", 1635, 1703, ["gb"], ["biology", "physics"],
  "Robert Hooke was an English natural philosopher who coined the term 'cell' in biology and made contributions to mechanics, optics, and architecture.",
  "Hooke was born on the Isle of Wight. He studied at Christ Church, Oxford, and became Robert Boyle's assistant before being appointed curator of experiments at the Royal Society.",
  "Hooke's Micrographia introduced the world to microscopic life. His coining of the word 'cell' and his law of elasticity (Hooke's law) remain fundamental in biology and physics.",
  [(1660, "Discovered Hooke's law of elasticity"), (1662, "Became curator of the Royal Society"), (1665, "Published Micrographia")],
  [("Micrographia", 1665, "Pioneering work on microscopy that introduced the term 'cell'")],
  [("The truth is, the Science of Nature has been already too long made only a work of the Brain and the Fancy.", "Micrographia")])

p("alfred-russel-wallace", "Alfred Russel Wallace", "アルフレッド・ラッセル・ウォレス", 1823, 1913, ["gb"], ["biology"],
  "Alfred Russel Wallace was a British naturalist who independently conceived the theory of evolution through natural selection, prompting Darwin to publish his own theory.",
  "Wallace was born in Usk, Wales. He was largely self-educated and worked as a surveyor and teacher before becoming a professional naturalist and collector in the Amazon and Malay Archipelago.",
  "Wallace's independent discovery of natural selection spurred Darwin to publish. His work on biogeography, including the Wallace Line, established him as the father of biogeography.",
  [(1848, "Began expedition to the Amazon"), (1854, "Began eight-year expedition to the Malay Archipelago"), (1858, "Sent paper on natural selection to Darwin"), (1869, "Published The Malay Archipelago")],
  [("The Malay Archipelago", 1869, "Account of his travels and the biogeography of Southeast Asia"), ("On the Tendency of Varieties to Depart Indefinitely from the Original Type", 1858, "Paper independently proposing natural selection")],
  [("Every species has come into existence coincident both in space and time with a closely allied species.", "1855 paper")])

p("ernst-haeckel", "Ernst Haeckel", "エルンスト・ヘッケル", 1834, 1919, ["de"], ["biology"],
  "Ernst Haeckel was a German biologist, naturalist, and artist who named thousands of new species, mapped a genealogical tree of life, and coined terms including 'ecology' and 'phylogeny.'",
  "Haeckel was born in Potsdam, Germany. He studied medicine and zoology and was deeply influenced by Darwin's Origin of Species, becoming one of evolution's most passionate advocates in Germany.",
  "Haeckel coined foundational biological terms, created stunning scientific illustrations, and popularized Darwin's ideas in Germany. His tree of life concept influenced how we visualize evolution.",
  [(1862, "Published first monograph on radiolarians"), (1866, "Published Generelle Morphologie and coined 'ecology'"), (1899, "Published Kunstformen der Natur (Art Forms in Nature)")],
  [("Kunstformen der Natur", 1899, "Beautiful scientific illustrations of various organisms"), ("Generelle Morphologie der Organismen", 1866, "Systematic presentation of evolutionary morphology")],
  [("Ecology is the body of knowledge concerning the economy of nature.", "Generelle Morphologie")])

p("thomas-henry-huxley", "Thomas Henry Huxley", "トマス・ヘンリー・ハクスリー", 1825, 1895, ["gb"], ["biology"],
  "Thomas Henry Huxley was an English biologist known as 'Darwin's Bulldog' for his advocacy of Charles Darwin's theory of evolution by natural selection.",
  "Huxley was born in Ealing, Middlesex. Largely self-taught, he studied medicine and served as assistant surgeon on HMS Rattlesnake, collecting marine specimens.",
  "Huxley championed Darwinian evolution in public debates and through his writing, establishing biology as a professional science and advocating for science education.",
  [(1854, "Became professor at the Royal School of Mines"), (1860, "Debated Bishop Wilberforce on evolution"), (1863, "Published Evidence as to Man's Place in Nature")],
  [("Evidence as to Man's Place in Nature", 1863, "First book to argue explicitly for human evolution")],
  [("The great tragedy of Science—the slaying of a beautiful hypothesis by an ugly fact.", "Biogenesis and Abiogenesis")])

p("james-watson", "James Watson", "ジェームズ・ワトソン", 1928, None, ["us"], ["biology"],
  "James Watson is an American molecular biologist who co-discovered the structure of DNA with Francis Crick, earning the Nobel Prize in Physiology or Medicine.",
  "Watson was born in Chicago, Illinois. A child prodigy, he entered the University of Chicago at age 15 and received his PhD at Indiana University before going to Cambridge.",
  "Watson and Crick's discovery of the DNA double helix structure in 1953 is one of the most important scientific discoveries of the 20th century, launching molecular biology.",
  [(1953, "Co-discovered the double helix structure of DNA"), (1962, "Awarded Nobel Prize in Physiology or Medicine"), (1968, "Published The Double Helix"), (1990, "Led the Human Genome Project")],
  [("The Double Helix", 1968, "Personal account of the discovery of the structure of DNA")],
  [("Today, we can see that the path to the double helix was marked by a series of fortunate events.", "The Double Helix")])

p("francis-crick", "Francis Crick", "フランシス・クリック", 1916, 2004, ["gb"], ["biology", "physics"],
  "Francis Crick was a British molecular biologist, biophysicist, and neuroscientist who co-discovered the structure of DNA and later proposed the central dogma of molecular biology.",
  "Crick was born in Northampton, England. He studied physics at University College London and worked on military research during WWII before turning to biology at Cambridge.",
  "Crick's co-discovery of DNA's structure and his articulation of the central dogma of molecular biology provided the framework for modern genetics and biotechnology.",
  [(1953, "Co-discovered DNA double helix structure"), (1958, "Proposed the central dogma of molecular biology"), (1962, "Awarded Nobel Prize in Physiology or Medicine"), (1966, "Published Of Molecules and Men")],
  [("Molecular Structure of Nucleic Acids", 1953, "One-page paper in Nature describing the DNA double helix")],
  [("We have discovered the secret of life.", "Remark at the Eagle pub, Cambridge, 1953")])

p("barbara-mcclintock", "Barbara McClintock", "バーバラ・マクリントック", 1902, 1992, ["us"], ["biology"],
  "Barbara McClintock was an American cytogeneticist who was awarded the Nobel Prize for her discovery of genetic transposition, or 'jumping genes.'",
  "McClintock was born in Hartford, Connecticut. She studied at Cornell University, where she began her groundbreaking research on corn (maize) genetics.",
  "McClintock's discovery of transposable genetic elements overturned the prevailing view of the genome as a static entity and revealed the dynamic nature of genetic organization.",
  [(1931, "Demonstrated chromosomal crossover in maize"), (1948, "Discovered transposable elements"), (1983, "Awarded Nobel Prize in Physiology or Medicine")],
  [("The Origin and Behavior of Mutable Loci in Maize", 1950, "Paper describing the discovery of transposable genetic elements")],
  [("If you know you are on the right track, if you have this inner knowledge, then nobody can turn you off.", "Attributed")])

p("edward-o-wilson", "Edward O. Wilson", "エドワード・O・ウィルソン", 1929, 2021, ["us"], ["biology"],
  "Edward O. Wilson was an American biologist and naturalist known as the father of sociobiology and a champion of biodiversity conservation.",
  "Wilson was born in Birmingham, Alabama. A childhood accident left him blind in one eye, directing his interest toward insects. He studied at the University of Alabama and Harvard.",
  "Wilson founded sociobiology, advanced island biogeography theory, and became the world's foremost advocate for biodiversity. His concept of biophilia influenced conservation worldwide.",
  [(1967, "Published The Theory of Island Biogeography"), (1975, "Published Sociobiology: The New Synthesis"), (1979, "Won Pulitzer Prize for On Human Nature"), (1990, "Won Pulitzer for The Ants")],
  [("Sociobiology: The New Synthesis", 1975, "Controversial synthesis applying evolutionary theory to animal and human social behavior"), ("The Diversity of Life", 1992, "Survey of Earth's biodiversity and its destruction")],
  [("The diversity of life on Earth is far greater than even the most learned among us had imagined.", "The Diversity of Life")])

p("rachel-carson", "Rachel Carson", "レイチェル・カーソン", 1907, 1964, ["us"], ["biology"],
  "Rachel Carson was an American marine biologist and conservationist whose book Silent Spring helped launch the global environmental movement.",
  "Carson was born in Springdale, Pennsylvania. She studied biology at Johns Hopkins and worked for the U.S. Fish and Wildlife Service while writing about the natural world.",
  "Carson's Silent Spring documented the environmental damage caused by pesticides and sparked the modern environmental movement, leading to the creation of the EPA and the ban on DDT.",
  [(1941, "Published Under the Sea-Wind"), (1951, "Published The Sea Around Us"), (1962, "Published Silent Spring"), (1963, "Testified before Congress on pesticide dangers")],
  [("Silent Spring", 1962, "Documented the devastating effects of pesticides on ecosystems"), ("The Sea Around Us", 1951, "Popular account of ocean science")],
  [("In every outward and visible grace of life, in every just and noble action, there is a fine and secret root which connects it with the natural world.", "Attributed")])

p("alexander-fleming", "Alexander Fleming", "アレクサンダー・フレミング", 1881, 1955, ["gb"], ["biology"],
  "Alexander Fleming was a Scottish physician and microbiologist who discovered penicillin, the world's first broadly effective antibiotic.",
  "Fleming was born in Lochfield, Scotland. He studied medicine at St Mary's Hospital Medical School in London and served in the Royal Army Medical Corps during World War I.",
  "Fleming's discovery of penicillin launched the antibiotic era, saving hundreds of millions of lives and transforming modern medicine.",
  [(1928, "Discovered penicillin"), (1929, "Published paper on penicillin"), (1945, "Awarded Nobel Prize in Physiology or Medicine")],
  [("On the Antibacterial Action of Cultures of a Penicillium", 1929, "Paper reporting the discovery of penicillin")],
  [("One sometimes finds what one is not looking for.", "Nobel lecture, 1945")])

p("jane-goodall", "Jane Goodall", "ジェーン・グドール", 1934, None, ["gb"], ["biology"],
  "Jane Goodall is a British primatologist and anthropologist who is considered the world's foremost expert on chimpanzees, transforming our understanding of primate behavior.",
  "Goodall was born in London. Without formal training, she traveled to Tanzania at age 26 to study chimpanzees, mentored by anthropologist Louis Leakey.",
  "Goodall's observations of tool use, social behavior, and individual personalities in chimpanzees revolutionized primatology and blurred the line between humans and other animals.",
  [(1960, "Began chimpanzee research at Gombe Stream"), (1964, "Observed chimps making tools"), (1977, "Founded the Jane Goodall Institute"), (1986, "Published The Chimpanzees of Gombe")],
  [("In the Shadow of Man", 1971, "Groundbreaking account of chimpanzee behavior at Gombe"), ("The Chimpanzees of Gombe", 1986, "Comprehensive scientific study of chimpanzee behavior")],
  [("What you do makes a difference, and you have to decide what kind of difference you want to make.", "Attributed")])

p("louis-agassiz", "Louis Agassiz", "ルイ・アガシー", 1807, 1873, ["ch", "us"], ["biology"],
  "Louis Agassiz was a Swiss-American biologist and geologist recognized as an innovative scholar of Earth's natural history, particularly glaciology and ichthyology.",
  "Agassiz was born in Môtier, Switzerland. He studied at several European universities and worked with Cuvier in Paris before emigrating to the United States and joining Harvard.",
  "Agassiz proposed the Ice Age theory, made major contributions to paleontology and ichthyology, and founded Harvard's Museum of Comparative Zoology.",
  [(1837, "Proposed Ice Age theory"), (1840, "Published Études sur les glaciers"), (1846, "Moved to the United States"), (1859, "Founded Museum of Comparative Zoology at Harvard")],
  [("Études sur les glaciers", 1840, "Landmark work proposing that glaciers once covered much of Europe")],
  [("Study nature, not books.", "Attributed")])

p("georges-cuvier", "Georges Cuvier", "ジョルジュ・キュヴィエ", 1769, 1832, ["fr"], ["biology"],
  "Georges Cuvier was a French naturalist and zoologist who established the fields of comparative anatomy and paleontology and proved that extinction was a real phenomenon.",
  "Cuvier was born in Montbéliard, then part of the Duchy of Württemberg. He studied at the Karlsschule in Stuttgart before moving to Paris during the Revolution.",
  "Cuvier established extinction as a fact, founded comparative anatomy as a discipline, and classified the animal kingdom into four distinct body plans, transforming zoology.",
  [(1796, "Demonstrated mammoth extinction"), (1800, "Published Lessons in Comparative Anatomy"), (1812, "Published Researches on the Fossil Bones"), (1817, "Published The Animal Kingdom")],
  [("The Animal Kingdom", 1817, "Classified all animals into four major body plans"), ("Researches on the Fossil Bones of Quadrupeds", 1812, "Established paleontology as a science")],
  [("I am gifted with a memory that has allowed me to reconstruct the general plan of natural bodies.", "Attributed")])

p("jean-baptiste-lamarck", "Jean-Baptiste Lamarck", "ジャン＝バティスト・ラマルク", 1744, 1829, ["fr"], ["biology"],
  "Jean-Baptiste Lamarck was a French naturalist who proposed an early theory of evolution based on the inheritance of acquired characteristics and coined the term 'biology.'",
  "Lamarck was born in Bazentin, France. He served in the military, then studied medicine and botany, becoming professor of invertebrate zoology at the Muséum National d'Histoire Naturelle.",
  "Though his mechanism of evolution was incorrect, Lamarck was one of the first to propose that species change over time. He coined 'biology' and 'invertebrate' and classified invertebrates systematically.",
  [(1778, "Published Flore française"), (1801, "Published Système des animaux sans vertèbres"), (1809, "Published Philosophie Zoologique")],
  [("Philosophie Zoologique", 1809, "Presented his theory of evolution through inheritance of acquired characteristics")],
  [("Nature, in producing successively every species of animal, has begun with the most imperfect and ended with the most perfect.", "Philosophie Zoologique")])

p("thomas-hunt-morgan", "Thomas Hunt Morgan", "トーマス・ハント・モーガン", 1866, 1945, ["us"], ["biology"],
  "Thomas Hunt Morgan was an American evolutionary biologist and geneticist who won the Nobel Prize for discoveries relating to the role of chromosomes in heredity.",
  "Morgan was born in Lexington, Kentucky. He studied at the University of Kentucky and Johns Hopkins, eventually establishing the famous 'Fly Room' at Columbia University.",
  "Morgan's work with Drosophila fruit flies demonstrated that genes are carried on chromosomes, establishing the chromosomal theory of inheritance and modern genetics.",
  [(1908, "Began Drosophila experiments at Columbia"), (1910, "Discovered sex-linked inheritance"), (1915, "Published The Mechanism of Mendelian Heredity"), (1933, "Awarded Nobel Prize in Physiology or Medicine")],
  [("The Mechanism of Mendelian Heredity", 1915, "Established the chromosomal theory of inheritance")],
  [("The fly room was a breeding ground for ideas.", "Attributed")])

p("andreas-vesalius", "Andreas Vesalius", "アンドレアス・ヴェサリウス", 1514, 1564, ["be"], ["biology"],
  "Andreas Vesalius was a Flemish anatomist and physician who is considered the founder of modern human anatomy.",
  "Vesalius was born in Brussels. He studied at the Universities of Leuven and Paris before becoming professor of anatomy at the University of Padua at age 23.",
  "Vesalius's De Humani Corporis Fabrica corrected centuries of errors in Galenic anatomy and established anatomy as a science based on direct observation and dissection.",
  [(1537, "Became professor at University of Padua"), (1543, "Published De Humani Corporis Fabrica"), (1544, "Became physician to Emperor Charles V")],
  [("De Humani Corporis Fabrica", 1543, "Comprehensive illustrated atlas of human anatomy based on actual dissection")],
  [("I am not accustomed to saying anything with certainty after only one or two observations.", "De Humani Corporis Fabrica")])

p("william-harvey", "William Harvey", "ウィリアム・ハーヴェイ", 1578, 1657, ["gb"], ["biology"],
  "William Harvey was an English physician who made the first detailed description of the circulatory system, demonstrating that blood circulates through the body.",
  "Harvey was born in Folkestone, Kent. He studied at Cambridge and the University of Padua, then served as physician to King James I and King Charles I.",
  "Harvey's demonstration that blood circulates through the body, pumped by the heart, overturned 1,500 years of Galenic teaching and founded modern physiology.",
  [(1616, "First announced his theory of blood circulation"), (1628, "Published De Motu Cordis"), (1651, "Published De Generatione Animalium")],
  [("De Motu Cordis", 1628, "Demonstrated the circulation of blood through the body")],
  [("I profess to learn and to teach anatomy not from books but from dissections.", "De Motu Cordis")])

p("robert-koch", "Robert Koch", "ロバート・コッホ", 1843, 1910, ["de"], ["biology"],
  "Robert Koch was a German physician and microbiologist who identified the causative agents of tuberculosis, cholera, and anthrax, earning the Nobel Prize.",
  "Koch was born in Clausthal, Germany. He studied medicine at the University of Göttingen and served as a district physician before pursuing bacteriological research.",
  "Koch's postulates for proving disease causation and his identification of tuberculosis and cholera bacteria established the foundations of medical microbiology and public health.",
  [(1876, "Identified anthrax bacillus"), (1882, "Identified tuberculosis bacterium"), (1883, "Identified cholera bacterium"), (1905, "Awarded Nobel Prize in Physiology or Medicine")],
  [("The Aetiology of Tuberculosis", 1882, "Paper identifying Mycobacterium tuberculosis as the cause of TB")],
  [("The day will come when man will have to fight noise as inexorably as cholera and the plague.", "Attributed")])

p("ernst-mayr", "Ernst Mayr", "エルンスト・マイア", 1904, 2005, ["de", "us"], ["biology"],
  "Ernst Mayr was a German-American biologist who was one of the 20th century's leading evolutionary biologists, known for the biological species concept.",
  "Mayr was born in Kempten, Germany. He studied at the University of Greifswald and led ornithological expeditions to New Guinea before emigrating to the United States.",
  "Mayr's biological species concept and his work on speciation through geographic isolation became central to the modern evolutionary synthesis.",
  [(1942, "Published Systematics and the Origin of Species"), (1954, "Developed the biological species concept"), (1963, "Published Animal Species and Evolution")],
  [("Systematics and the Origin of Species", 1942, "Key work in the modern evolutionary synthesis"), ("The Growth of Biological Thought", 1982, "Comprehensive history of biological ideas")],
  [("The species is the most important unit of classification.", "Attributed")])

p("jonas-salk", "Jonas Salk", "ジョナス・ソーク", 1914, 1995, ["us"], ["biology"],
  "Jonas Salk was an American virologist who developed one of the first successful polio vaccines, helping to eradicate the disease worldwide.",
  "Salk was born in New York City to Russian-Jewish immigrant parents. He studied at New York University School of Medicine and conducted research at the University of Pittsburgh.",
  "Salk's polio vaccine, released in 1955, virtually eliminated polio in the developed world and saved millions of children from paralysis. He famously refused to patent it.",
  [(1947, "Began polio vaccine research"), (1953, "Announced successful vaccine"), (1955, "Vaccine approved for public use"), (1963, "Founded the Salk Institute for Biological Studies")],
  [("Polio Vaccine", 1955, "The first successful inactivated poliovirus vaccine")],
  [("Could you patent the sun?", "When asked who owned the patent on the polio vaccine, 1955")])

p("e-o-wilson-not-duplicate", "Theodor Schwann", "テオドール・シュワン", 1810, 1882, ["de"], ["biology"],
  "Theodor Schwann was a German physiologist who co-founded cell theory, discovered Schwann cells and pepsin, and coined the term 'metabolism.'",
  "Schwann was born in Neuss, Germany. He studied medicine at the University of Bonn and worked under Johannes Müller in Berlin.",
  "Schwann's cell theory, stating that all living things are composed of cells, is one of the most fundamental principles of biology. His discovery of pepsin founded enzyme chemistry.",
  [(1836, "Discovered pepsin"), (1838, "Extended cell theory to animals"), (1839, "Published Microscopic Investigations on the Structure and Growth of Animals and Plants")],
  [("Microscopic Investigations", 1839, "Established that cells are the basic unit of all animal life")],
  [("All living things are composed of cells and cell products.", "Microscopic Investigations")])

p("matthias-schleiden", "Matthias Schleiden", "マティアス・シュライデン", 1804, 1881, ["de"], ["biology"],
  "Matthias Schleiden was a German botanist who co-founded cell theory with Theodor Schwann, establishing that all plants are composed of cells.",
  "Schleiden was born in Hamburg, Germany. He first studied law but turned to botany, studying at the University of Jena.",
  "Schleiden's recognition that cells are the fundamental units of plants, combined with Schwann's work on animals, established cell theory as a cornerstone of biology.",
  [(1838, "Published cell theory for plants"), (1842, "Published Principles of Scientific Botany")],
  [("Contributions to Phytogenesis", 1838, "Paper establishing that all plant tissues are composed of cells")],
  [("Every plant is an aggregate of individual, fully individualized, independent, separate beings—the cells.", "Contributions to Phytogenesis")])

p("rudolf-virchow", "Rudolf Virchow", "ルドルフ・フィルヒョウ", 1821, 1902, ["de"], ["biology"],
  "Rudolf Virchow was a German physician and pathologist known as the father of modern pathology. He proposed that all cells arise from pre-existing cells.",
  "Virchow was born in Schivelbein, Pomerania. He studied medicine in Berlin and became professor at the University of Würzburg and later the Charité in Berlin.",
  "Virchow's principle 'omnis cellula e cellula' (every cell from a cell) completed cell theory. His cellular pathology approach transformed medicine from speculation to science.",
  [(1847, "Founded the journal Archiv für pathologische Anatomie"), (1855, "Proposed 'omnis cellula e cellula'"), (1858, "Published Die Cellularpathologie")],
  [("Die Cellularpathologie", 1858, "Established cellular pathology as the basis of medical science")],
  [("Omnis cellula e cellula. (Every cell originates from another existing cell.)", "Die Cellularpathologie")])

p("francis-galton", "Francis Galton", "フランシス・ゴルトン", 1822, 1911, ["gb"], ["biology", "mathematics"],
  "Francis Galton was an English polymath who pioneered the use of statistical methods in biology, developed fingerprint identification, and founded the study of human heredity.",
  "Galton was born in Birmingham, England, a half-cousin of Charles Darwin. He studied medicine and mathematics at Cambridge before becoming an explorer and scientist.",
  "Galton introduced regression to the mean, correlation coefficients, and questionnaire-based studies. His statistical innovations became fundamental tools in biology and social science.",
  [(1869, "Published Hereditary Genius"), (1883, "Coined the term 'eugenics'"), (1886, "Demonstrated regression toward the mean"), (1892, "Published Finger Prints")],
  [("Hereditary Genius", 1869, "Statistical study of the inheritance of abilities"), ("Finger Prints", 1892, "Established the uniqueness of fingerprints for identification")],
  [("Whenever you can, count.", "Attributed")])

p("santiago-ramon-y-cajal", "Santiago Ramón y Cajal", "サンティアゴ・ラモン・イ・カハール", 1852, 1934, ["es"], ["biology"],
  "Santiago Ramón y Cajal was a Spanish neuroscientist who won the Nobel Prize for his work on the structure of the nervous system, establishing the neuron doctrine.",
  "Cajal was born in Petilla de Aragón, Spain. He studied medicine at the University of Zaragoza and became professor of anatomy at several Spanish universities.",
  "Cajal's meticulous drawings and observations proved that the nervous system is composed of individual neurons, not a continuous network. He is considered the father of modern neuroscience.",
  [(1887, "Began systematic study of nervous tissue"), (1889, "Proposed the neuron doctrine"), (1906, "Awarded Nobel Prize in Physiology or Medicine")],
  [("Histology of the Nervous System of Man and Vertebrates", 1899, "Comprehensive atlas of neural microanatomy")],
  [("Every man can, if he so desires, become the sculptor of his own brain.", "Advice for a Young Investigator")])

p("linnaeus-junior", "Georges-Louis Leclerc, Comte de Buffon", "ジョルジュ＝ルイ・ルクレール・ビュフォン伯爵", 1707, 1788, ["fr"], ["biology"],
  "The Comte de Buffon was a French naturalist whose encyclopedic work Histoire Naturelle was one of the first attempts to describe the natural world comprehensively.",
  "Buffon was born in Montbard, France, into a wealthy family. He studied law and mathematics before devoting himself to natural history at the Jardin du Roi in Paris.",
  "Buffon's Histoire Naturelle, spanning 36 volumes, was one of the most widely read works of the Enlightenment and proposed ideas about species change that prefigured evolutionary theory.",
  [(1739, "Became keeper of the Jardin du Roi"), (1749, "Began publishing Histoire Naturelle"), (1778, "Published Epochs of Nature")],
  [("Histoire Naturelle", 1749, "Encyclopedic work on natural history spanning 36 volumes"), ("Epochs of Nature", 1778, "Proposed that the Earth was much older than biblical accounts")],
  [("Genius is only a greater aptitude for patience.", "Attributed")])

p("konrad-lorenz", "Konrad Lorenz", "コンラート・ローレンツ", 1903, 1989, ["at"], ["biology"],
  "Konrad Lorenz was an Austrian zoologist and ethologist who shared the Nobel Prize for discoveries in individual and social behavior patterns in animals.",
  "Lorenz was born in Vienna. He studied medicine and zoology at the University of Vienna and became fascinated with animal behavior, particularly imprinting in geese.",
  "Lorenz founded modern ethology (the study of animal behavior) and demonstrated imprinting. His work connecting animal and human behavior influenced psychology and philosophy.",
  [(1935, "Published work on imprinting in birds"), (1949, "Published King Solomon's Ring"), (1963, "Published On Aggression"), (1973, "Awarded Nobel Prize in Physiology or Medicine")],
  [("King Solomon's Ring", 1949, "Popular book on animal behavior"), ("On Aggression", 1963, "Study of aggressive behavior in animals and humans")],
  [("It is a good morning exercise for a research scientist to discard a pet hypothesis every day before breakfast.", "On Aggression")])

p("e-o-wilson-dup2", "Niko Tinbergen", "ニコ・ティンバーゲン", 1907, 1988, ["nl", "gb"], ["biology"],
  "Nikolaas (Niko) Tinbergen was a Dutch biologist and ornithologist who shared the Nobel Prize for pioneering work in ethology, the study of animal behavior.",
  "Tinbergen was born in The Hague, Netherlands. He studied biology at Leiden University and spent time observing animals in the wild, developing rigorous experimental methods.",
  "Tinbergen's four questions about animal behavior (causation, development, evolution, function) remain the foundation of ethological analysis. His elegant field experiments set the standard for behavioral research.",
  [(1951, "Published The Study of Instinct"), (1953, "Published The Herring Gull's World"), (1963, "Formulated Tinbergen's four questions"), (1973, "Awarded Nobel Prize in Physiology or Medicine")],
  [("The Study of Instinct", 1951, "Foundational textbook of ethology"), ("The Herring Gull's World", 1953, "Classic field study of animal behavior")],
  [("Observing is more than looking.", "Attributed")])

p("karl-von-frisch", "Karl von Frisch", "カール・フォン・フリッシュ", 1886, 1982, ["at"], ["biology"],
  "Karl von Frisch was an Austrian ethologist who shared the Nobel Prize for his discoveries about the dance language and orientation of honeybees.",
  "Von Frisch was born in Vienna into an academic family. He studied at the University of Munich and spent decades meticulously studying bee behavior.",
  "Von Frisch's discovery of the waggle dance as a communication system in bees was a landmark in animal behavior research, revealing complex communication in insects.",
  [(1927, "Published The Dancing Bees"), (1946, "Decoded the waggle dance"), (1967, "Published The Dance Language and Orientation of Bees"), (1973, "Awarded Nobel Prize in Physiology or Medicine")],
  [("The Dance Language and Orientation of Bees", 1967, "Definitive work on bee communication through dance")],
  [("The bee's life is like a magic well: the more you draw from it, the more it fills with water.", "Attributed")])

p("lynn-margulis", "Lynn Margulis", "リン・マーギュリス", 1938, 2011, ["us"], ["biology"],
  "Lynn Margulis was an American evolutionary theorist who proposed the endosymbiotic theory explaining the origin of eukaryotic cells.",
  "Margulis was born in Chicago. She entered the University of Chicago at age 14, later earning degrees from the University of Wisconsin and UC Berkeley.",
  "Margulis's endosymbiotic theory, initially rejected by mainstream biology, is now accepted as the explanation for the origin of mitochondria and chloroplasts, fundamentally changing cell biology.",
  [(1967, "Published endosymbiotic theory paper"), (1970, "Published Origin of Eukaryotic Cells"), (1981, "Published Symbiosis in Cell Evolution")],
  [("Symbiosis in Cell Evolution", 1981, "Comprehensive argument for endosymbiosis as a driver of evolution")],
  [("Life did not take over the globe by combat, but by networking.", "Attributed")])

p("mary-anning", "Mary Anning", "メアリー・アニング", 1799, 1847, ["gb"], ["biology"],
  "Mary Anning was an English fossil collector and paleontologist who made landmark discoveries in Jurassic marine fossil beds along the Dorset coast.",
  "Anning was born in Lyme Regis, Dorset. Her family was poor, and she supplemented their income by collecting and selling fossils from the cliffs along the English Channel.",
  "Anning's discoveries of ichthyosaur, plesiosaur, and pterosaur fossils contributed to major changes in scientific thinking about prehistoric life and the history of Earth.",
  [(1811, "Discovered first complete ichthyosaur skeleton"), (1823, "Discovered first complete plesiosaur skeleton"), (1828, "Discovered first British pterosaur")],
  [("Ichthyosaur Skeleton", 1811, "First complete specimen of an ichthyosaurus found in England")],
  [("The world has used me so unkindly, I fear it has made me suspicious of everyone.", "Letter, 1839")])

p("carolus-linnaeus-2", "E.O. Wilson's Teacher William Morton Wheeler", "ウィリアム・モートン・ウィーラー", 1865, 1937, ["us"], ["biology"],
  "William Morton Wheeler was an American entomologist and myrmecologist who was one of the world's leading authorities on ants and social insects.",
  "Wheeler was born in Milwaukee, Wisconsin. He studied at the German-American Academy and the University of Chicago, becoming professor at Harvard.",
  "Wheeler's studies of ant societies and their complex behaviors established myrmecology as a discipline and influenced the development of ethology and sociobiology.",
  [(1900, "Published studies on ant development"), (1910, "Published Ants: Their Structure, Development, and Behavior"), (1923, "Published Social Life Among the Insects")],
  [("Ants: Their Structure, Development, and Behavior", 1910, "Comprehensive monograph on ant biology")],
  [("The ant is the embodiment of industry and social cooperation.", "Attributed")])

p("dian-fossey", "Dian Fossey", "ダイアン・フォッシー", 1932, 1985, ["us"], ["biology"],
  "Dian Fossey was an American primatologist and conservationist who dedicated her life to studying and protecting mountain gorillas in Rwanda.",
  "Fossey was born in San Francisco. She studied occupational therapy before traveling to Africa, where she met Louis Leakey, who supported her gorilla research.",
  "Fossey's long-term study of mountain gorillas in their natural habitat transformed our understanding of primate behavior and brought global attention to gorilla conservation.",
  [(1966, "Began gorilla research in the Virunga Mountains"), (1967, "Established Karisoke Research Centre"), (1983, "Published Gorillas in the Mist"), (1985, "Murdered at Karisoke")],
  [("Gorillas in the Mist", 1983, "Account of 13 years living with mountain gorillas")],
  [("When you realize the value of all life, you dwell less on what is past and concentrate more on the preservation of the future.", "Gorillas in the Mist")])

p("theodosius-dobzhansky", "Theodosius Dobzhansky", "テオドシウス・ドブジャンスキー", 1900, 1975, ["ua", "us"], ["biology"],
  "Theodosius Dobzhansky was a Ukrainian-American geneticist and evolutionary biologist who was a central figure in the modern evolutionary synthesis.",
  "Dobzhansky was born in Nemyriv, Ukraine. He studied at the University of Kiev and emigrated to the United States, working with Thomas Hunt Morgan at Columbia.",
  "Dobzhansky's Genetics and the Origin of Species bridged genetics and evolutionary biology, establishing population genetics as central to understanding evolution.",
  [(1937, "Published Genetics and the Origin of Species"), (1962, "Published Mankind Evolving"), (1973, "Published famous essay on evolution in biology")],
  [("Genetics and the Origin of Species", 1937, "Key work in the modern evolutionary synthesis bridging genetics and evolution")],
  [("Nothing in biology makes sense except in the light of evolution.", "American Biology Teacher, 1973")])

p("george-beadle", "George Beadle", "ジョージ・ビードル", 1903, 1989, ["us"], ["biology"],
  "George Beadle was an American geneticist who won the Nobel Prize for demonstrating that genes act through the production of enzymes — the one gene-one enzyme hypothesis.",
  "Beadle was born in Wahoo, Nebraska. He studied at the University of Nebraska and Cornell, then worked with Boris Ephrussi in Paris on Drosophila eye pigments.",
  "Beadle and Tatum's one gene-one enzyme hypothesis provided a molecular basis for genetics, establishing the link between genes and biochemical function.",
  [(1941, "Proposed one gene-one enzyme hypothesis with Tatum"), (1945, "Confirmed hypothesis with Neurospora experiments"), (1958, "Awarded Nobel Prize in Physiology or Medicine")],
  [("Genetic Control of Biochemical Reactions in Neurospora", 1941, "Paper establishing the one gene-one enzyme hypothesis")],
  [("Few things in life are as satisfying as finding the answer to a question that has long puzzled you.", "Attributed")])

p("oswald-avery", "Oswald Avery", "オズワルド・エイブリー", 1877, 1955, ["ca", "us"], ["biology"],
  "Oswald Avery was a Canadian-American physician and medical researcher who demonstrated that DNA is the substance that causes bacterial transformation, identifying it as the material of heredity.",
  "Avery was born in Halifax, Nova Scotia, and moved to New York as a child. He studied at Colgate University and Columbia, then spent his career at the Rockefeller Institute.",
  "Avery's 1944 experiment demonstrating that DNA carries genetic information was one of the key discoveries of the 20th century, paving the way for modern molecular biology.",
  [(1928, "Began transformation experiments"), (1944, "Published DNA as transforming principle"), (1945, "DNA's role increasingly accepted")],
  [("Studies on the Chemical Nature of the Substance Inducing Transformation", 1944, "Paper demonstrating DNA as the genetic material")],
  [("Perhaps the substance inducing transformation may be DNA.", "Letter to his brother, 1943")])

p("edward-jenner", "Edward Jenner", "エドワード・ジェンナー", 1749, 1823, ["gb"], ["biology"],
  "Edward Jenner was an English physician and scientist who pioneered the concept of vaccines, developing the first smallpox vaccine.",
  "Jenner was born in Berkeley, Gloucestershire. He studied medicine under John Hunter in London and returned to practice in his hometown.",
  "Jenner's smallpox vaccination was the first successful vaccine and eventually led to the global eradication of smallpox, saving millions of lives.",
  [(1796, "Vaccinated James Phipps with cowpox"), (1798, "Published An Inquiry into the Causes and Effects of the Variolae Vaccinae")],
  [("An Inquiry into the Causes and Effects of the Variolae Vaccinae", 1798, "Paper introducing vaccination against smallpox")],
  [("I hope that some day the practice of producing cowpox in human beings will spread over the world.", "Attributed")])

p("joseph-lister", "Joseph Lister", "ジョゼフ・リスター", 1827, 1912, ["gb"], ["biology"],
  "Joseph Lister was a British surgeon who pioneered antiseptic surgery, applying Louis Pasteur's germ theory to surgical practice.",
  "Lister was born in Upton, Essex. He studied medicine at University College London and became professor of surgery at the University of Glasgow.",
  "Lister's introduction of antiseptic principles to surgery dramatically reduced surgical mortality and transformed surgery from a dangerous last resort to a routine medical practice.",
  [(1865, "Introduced carbolic acid antisepsis"), (1867, "Published paper on antiseptic surgery"), (1877, "Became professor of surgery at King's College London")],
  [("On the Antiseptic Principle in the Practice of Surgery", 1867, "Paper introducing carbolic acid as an antiseptic in surgery")],
  [("Since the antiseptic treatment has been brought into full operation, my wards have completely changed their character.", "The Lancet, 1867")])

p("ivan-pavlov", "Ivan Pavlov", "イワン・パブロフ", 1849, 1936, ["ru"], ["biology"],
  "Ivan Pavlov was a Russian physiologist known primarily for his work in classical conditioning, discovering the conditioned reflex through experiments with dogs.",
  "Pavlov was born in Ryazan, Russia. He studied chemistry and physiology at Saint Petersburg University, then medicine at the Imperial Medical Academy.",
  "Pavlov's discovery of conditioned reflexes demonstrated that behavior can be learned through association, founding behaviorist psychology and influencing neuroscience.",
  [(1897, "Published The Work of the Digestive Glands"), (1901, "Demonstrated the conditioned reflex"), (1904, "Awarded Nobel Prize in Physiology or Medicine")],
  [("The Work of the Digestive Glands", 1897, "Comprehensive study of digestive physiology"), ("Conditioned Reflexes", 1927, "Definitive work on conditioning and learned behavior")],
  [("Don't become a mere recorder of facts, but try to penetrate the mystery of their origin.", "Attributed")])

p("tu-youyou", "Tu Youyou", "屠呦呦", 1930, None, ["cn"], ["biology", "chemistry"],
  "Tu Youyou is a Chinese pharmaceutical chemist who discovered artemisinin, a drug used to treat malaria, winning the Nobel Prize in Physiology or Medicine.",
  "Tu was born in Ningbo, China. She studied at Peking University School of Medicine and worked at the China Academy of Traditional Chinese Medicine.",
  "Tu's discovery of artemisinin from traditional Chinese medicine has saved millions of lives in malaria-endemic regions, bridging traditional and modern medicine.",
  [(1972, "Isolated artemisinin from sweet wormwood"), (1986, "Received approval for artemisinin as antimalarial"), (2015, "Awarded Nobel Prize in Physiology or Medicine")],
  [("Artemisinin", 1972, "Antimalarial drug isolated from the traditional Chinese medicinal plant Artemisia annua")],
  [("Every scientist dreams of doing something that can help the world.", "Nobel lecture, 2015")])

p("paul-ehrlich", "Paul Ehrlich", "パウル・エールリヒ", 1854, 1915, ["de"], ["biology", "chemistry"],
  "Paul Ehrlich was a German physician and scientist who won the Nobel Prize for his contributions to immunology and is known as the founder of chemotherapy.",
  "Ehrlich was born in Strehlen, Silesia. He studied medicine at several German universities and became interested in the selective staining of tissues and cells.",
  "Ehrlich's concept of the 'magic bullet' — a chemical that selectively targets pathogens — launched the field of chemotherapy. His work on immunology earned him the Nobel Prize.",
  [(1897, "Developed side-chain theory of immunity"), (1908, "Awarded Nobel Prize in Physiology or Medicine"), (1910, "Developed Salvarsan for treating syphilis")],
  [("Salvarsan", 1910, "First effective treatment for syphilis, the first modern chemotherapeutic agent")],
  [("We must learn to shoot microbes with magic bullets.", "Attributed")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'e-o-wilson-not-duplicate':
            entry['id'] = 'theodor-schwann'
        elif entry['id'] == 'e-o-wilson-dup2':
            entry['id'] = 'niko-tinbergen'
        elif entry['id'] == 'linnaeus-junior':
            entry['id'] = 'buffon'
        elif entry['id'] == 'carolus-linnaeus-2':
            entry['id'] = 'william-morton-wheeler'
    write_people(P)
