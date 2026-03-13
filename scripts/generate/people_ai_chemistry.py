#!/usr/bin/env python3
"""Generate ~100 chemists."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

p("antoine-lavoisier", "Antoine Lavoisier", "アントワーヌ・ラヴォアジエ", 1743, 1794, ["fr"], ["chemistry"],
  "Antoine Lavoisier was a French nobleman and chemist who is considered the father of modern chemistry. He named oxygen and hydrogen, helped construct the metric system, and wrote the first extensive list of elements.",
  "Lavoisier was born into a wealthy Parisian family. He studied law but developed a passion for science, conducting experiments that would revolutionize chemistry.",
  "Lavoisier's identification of oxygen's role in combustion overthrew phlogiston theory and established chemistry as a quantitative science. His systematic naming of chemical compounds remains in use today.",
  [(1772, "Began experiments on combustion"), (1778, "Named oxygen"), (1789, "Published Traité Élémentaire de Chimie"), (1794, "Executed during the French Revolution")],
  [("Traité Élémentaire de Chimie", 1789, "The first modern chemistry textbook, listing 33 elements")],
  [("Nothing is lost, nothing is created, everything is transformed.", "Traité Élémentaire de Chimie")])

p("dmitri-mendeleev", "Dmitri Mendeleev", "ドミトリ・メンデレーエフ", 1834, 1907, ["ru"], ["chemistry"],
  "Dmitri Mendeleev was a Russian chemist and inventor who formulated the Periodic Law and created a farsighted version of the periodic table of elements.",
  "Mendeleev was born in Tobolsk, Siberia, the youngest of a large family. After his father's death and the family factory burning down, his mother took him to St. Petersburg for education.",
  "Mendeleev's periodic table organized chemistry and predicted undiscovered elements with remarkable accuracy. His framework remains the central organizing principle of chemistry.",
  [(1861, "Published organic chemistry textbook"), (1869, "Published first periodic table"), (1871, "Predicted properties of undiscovered elements")],
  [("Principles of Chemistry", 1869, "Textbook that introduced the periodic table of elements")],
  [("I saw in a dream a table where all the elements fell into place as required.", "Attributed")])

p("marie-curie", "Marie Curie", "マリ・キュリー", 1867, 1934, ["pl", "fr"], ["chemistry", "physics"],
  "Marie Curie was a Polish-French physicist and chemist who conducted pioneering research on radioactivity. She was the first woman to win a Nobel Prize and the only person to win Nobel Prizes in two different sciences.",
  "Born Maria Sklodowska in Warsaw, Poland, she moved to Paris to study at the Sorbonne, where she met Pierre Curie. Together they researched radioactive substances.",
  "Curie's discovery of polonium and radium opened the field of nuclear physics and led to breakthroughs in cancer treatment. She broke barriers for women in science.",
  [(1898, "Discovered polonium and radium"), (1903, "Won Nobel Prize in Physics"), (1911, "Won Nobel Prize in Chemistry"), (1921, "Toured the United States")],
  [("Recherches sur les substances radioactives", 1903, "Her doctoral thesis on radioactivity")],
  [("Nothing in life is to be feared, it is only to be understood.", "Attributed")])

p("john-dalton", "John Dalton", "ジョン・ドルトン", 1766, 1844, ["gb"], ["chemistry", "physics"],
  "John Dalton was an English chemist, physicist, and meteorologist, best known for introducing atomic theory into chemistry and for his research into color blindness.",
  "Dalton was born in Eaglesfield, England, into a Quaker family. He began teaching at age twelve and became interested in meteorology and the properties of gases.",
  "Dalton's atomic theory provided a quantitative foundation for chemistry. His law of partial pressures and concept of atomic weights enabled the systematic study of chemical reactions.",
  [(1793, "Published Meteorological Observations"), (1801, "Formulated law of partial pressures"), (1803, "Proposed atomic theory"), (1808, "Published A New System of Chemical Philosophy")],
  [("A New System of Chemical Philosophy", 1808, "Presented the atomic theory of matter and table of atomic weights")],
  [("Matter, though divisible in an extreme degree, is nevertheless not infinitely divisible.", "A New System of Chemical Philosophy")])

p("robert-boyle", "Robert Boyle", "ロバート・ボイル", 1627, 1691, ["gb", "ie"], ["chemistry", "physics"],
  "Robert Boyle was an Anglo-Irish natural philosopher and chemist, widely considered one of the founders of modern chemistry. He is known for Boyle's law describing gas behavior.",
  "Boyle was born at Lismore Castle, Ireland, into one of the wealthiest families in the British Isles. He studied at Eton and traveled throughout Europe before settling at Oxford.",
  "Boyle's emphasis on experimentation and his rejection of Aristotelian elements helped establish chemistry as a legitimate science distinct from alchemy.",
  [(1657, "Built improved air pump"), (1660, "Published The Spring of the Air"), (1661, "Published The Sceptical Chymist"), (1662, "Boyle's law published")],
  [("The Sceptical Chymist", 1661, "Challenged classical element theory and proposed a corpuscular theory of matter")],
  [("The dialectical considerations have more of ingenuity than usefulness.", "The Sceptical Chymist")])

p("humphry-davy", "Humphry Davy", "ハンフリー・デービー", 1778, 1829, ["gb"], ["chemistry"],
  "Humphry Davy was a Cornish chemist and inventor who isolated several chemical elements using electrolysis, including sodium, potassium, calcium, and barium.",
  "Davy was born in Penzance, Cornwall. He was apprenticed to a surgeon-apothecary and began conducting chemical experiments on his own, eventually joining the Royal Institution in London.",
  "Davy's use of electrolysis to isolate elements revolutionized chemistry. He also invented the Davy lamp for miners and mentored Michael Faraday, shaping the future of science.",
  [(1800, "Experimented with nitrous oxide"), (1807, "Isolated potassium and sodium by electrolysis"), (1808, "Isolated calcium, barium, strontium, magnesium"), (1815, "Invented the Davy safety lamp")],
  [("Elements of Chemical Philosophy", 1812, "A comprehensive survey of chemistry and electrochemistry")],
  [("The most important of my discoveries have been suggested to me by my failures.", "Attributed")])

p("jons-jacob-berzelius", "Jöns Jacob Berzelius", "イェンス・ヤコブ・ベルセリウス", 1779, 1848, ["se"], ["chemistry"],
  "Jöns Jacob Berzelius was a Swedish chemist who is considered one of the founders of modern chemistry. He developed chemical notation using letters, determined atomic weights, and discovered several elements.",
  "Berzelius was born in Väversunda, Sweden. Orphaned early, he struggled financially but excelled at the University of Uppsala, where he studied medicine and chemistry.",
  "Berzelius created the modern system of chemical symbols still used today. His accurate determination of atomic weights and discovery of elements like silicon and selenium advanced chemistry enormously.",
  [(1803, "Began systematic atomic weight determinations"), (1813, "Introduced modern chemical notation"), (1818, "Published comprehensive table of atomic weights"), (1824, "Discovered silicon")],
  [("Textbook of Chemistry", 1808, "Multi-volume chemistry textbook that standardized chemical nomenclature")],
  [("The progress of science requires the continual refinement of measurement.", "Attributed")])

p("michael-faraday", "Michael Faraday", "マイケル・ファラデー", 1791, 1867, ["gb"], ["chemistry", "physics"],
  "Michael Faraday was an English scientist who contributed to the study of electromagnetism and electrochemistry. He discovered electromagnetic induction, benzene, and formulated the laws of electrolysis.",
  "Faraday was born into a poor family in Newington Butts, London. He was largely self-educated and became assistant to Humphry Davy at the Royal Institution, eventually succeeding him.",
  "Faraday's discoveries of electromagnetic induction and the laws of electrolysis laid the groundwork for electric motors, generators, and transformers, powering the modern world.",
  [(1821, "Discovered electromagnetic rotation"), (1825, "Discovered benzene"), (1831, "Discovered electromagnetic induction"), (1834, "Formulated laws of electrolysis")],
  [("Experimental Researches in Electricity", 1839, "A compilation of his groundbreaking work on electricity and magnetism")],
  [("Nothing is too wonderful to be true, if it be consistent with the laws of nature.", "Laboratory journal, 1849")])

p("friedrich-wohler", "Friedrich Wöhler", "フリードリヒ・ヴェーラー", 1800, 1882, ["de"], ["chemistry"],
  "Friedrich Wöhler was a German chemist who is best known for his synthesis of urea, the first organic compound produced from inorganic materials, disproving vitalism.",
  "Wöhler was born in Eschersheim, near Frankfurt. He studied medicine and chemistry, working under Berzelius in Stockholm before becoming professor at Göttingen.",
  "Wöhler's synthesis of urea in 1828 demolished the vital force theory and opened the field of organic synthesis, transforming chemistry and biology.",
  [(1827, "Isolated aluminum"), (1828, "Synthesized urea from inorganic compounds"), (1832, "Studied benzoyl radical with Liebig")],
  [("On the Artificial Production of Urea", 1828, "Paper reporting the first synthesis of an organic compound from inorganic precursors")],
  [("I can no longer, so to speak, hold my chemical water. I must tell you that I can make urea without needing a kidney.", "Letter to Berzelius, 1828")])

p("justus-von-liebig", "Justus von Liebig", "ユストゥス・フォン・リービッヒ", 1803, 1873, ["de"], ["chemistry"],
  "Justus von Liebig was a German chemist who made major contributions to agricultural and biological chemistry, and is considered one of the founders of organic chemistry.",
  "Liebig was born in Darmstadt, Germany. He studied in Bonn and Erlangen, then in Paris under Gay-Lussac, before becoming professor at the University of Giessen at age 21.",
  "Liebig revolutionized chemical education with his laboratory teaching methods and transformed agriculture with his theory of mineral plant nutrition. His work on food chemistry improved public health.",
  [(1824, "Became professor at Giessen at age 21"), (1832, "Founded Annalen der Chemie journal"), (1840, "Published Chemistry in its Application to Agriculture"), (1847, "Published Researches on the Chemistry of Food")],
  [("Chemistry in its Application to Agriculture and Physiology", 1840, "Established agricultural chemistry as a science")],
  [("The progress of mankind is due to the progress of the natural sciences.", "Attributed")])

p("louis-pasteur", "Louis Pasteur", "ルイ・パスツール", 1822, 1895, ["fr"], ["chemistry", "biology"],
  "Louis Pasteur was a French chemist and microbiologist renowned for his discoveries of the principles of vaccination, microbial fermentation, and pasteurization.",
  "Pasteur was born in Dole, France. He studied at the École Normale Supérieure in Paris and early in his career made important discoveries about molecular chirality.",
  "Pasteur's germ theory of disease revolutionized medicine and public health. His development of vaccines for rabies and anthrax saved countless lives, and pasteurization made food safer worldwide.",
  [(1848, "Discovered molecular chirality"), (1857, "Published work on fermentation"), (1862, "Disproved spontaneous generation"), (1885, "Successfully vaccinated against rabies")],
  [("Studies on Fermentation", 1876, "Demonstrated that fermentation is caused by microorganisms")],
  [("In the fields of observation, chance favors only the prepared mind.", "Lecture at the University of Lille, 1854")])

p("alfred-nobel", "Alfred Nobel", "アルフレッド・ノーベル", 1833, 1896, ["se"], ["chemistry", "engineering"],
  "Alfred Nobel was a Swedish chemist, engineer, inventor, and businessman, best known for inventing dynamite and for establishing the Nobel Prizes.",
  "Nobel was born in Stockholm to a family of engineers. He was educated privately by tutors and traveled widely in Europe and the United States, studying chemistry and engineering.",
  "Nobel's invention of dynamite and blasting caps transformed mining and construction. His endowment of the Nobel Prizes created the world's most prestigious awards in science, literature, and peace.",
  [(1863, "Patented nitroglycerin detonator"), (1867, "Patented dynamite"), (1875, "Invented gelignite"), (1895, "Signed will establishing Nobel Prizes")],
  [("Patent for Dynamite", 1867, "Safe handling of nitroglycerin for industrial blasting")],
  [("If I have a thousand ideas and only one turns out to be good, I am satisfied.", "Attributed")])

p("august-kekule", "August Kekulé", "アウグスト・ケクレ", 1829, 1896, ["de"], ["chemistry"],
  "August Kekulé was a German organic chemist who was the principal founder of the theory of chemical structure, including the structure of benzene as a ring.",
  "Kekulé was born in Darmstadt, Germany. He originally studied architecture but switched to chemistry after attending Liebig's lectures. He studied under several prominent chemists across Europe.",
  "Kekulé's theory of carbon's tetravalence and the ring structure of benzene were foundational insights that enabled the development of structural organic chemistry.",
  [(1857, "Proposed carbon tetravalence"), (1858, "Published theory of chemical structure"), (1865, "Proposed ring structure of benzene")],
  [("On the Constitution and Metamorphoses of Chemical Compounds", 1858, "Paper establishing structural theory in organic chemistry")],
  [("Let us learn to dream, gentlemen, and then we may perhaps find the truth.", "Speech at the Berlin Chemical Society, 1890")])

p("svante-arrhenius", "Svante Arrhenius", "スヴァンテ・アレニウス", 1859, 1927, ["se"], ["chemistry", "physics"],
  "Svante Arrhenius was a Swedish scientist who received the Nobel Prize in Chemistry for his electrolytic theory of dissociation. He was also an early researcher of the greenhouse effect.",
  "Arrhenius was born in Vik, Sweden. A child prodigy in mathematics, he studied at Uppsala and Stockholm, where his doctoral thesis on electrolytes was initially poorly received.",
  "Arrhenius's ionic dissociation theory explained electrical conductivity in solutions and earned him the Nobel Prize. His work on reaction rates and the greenhouse effect remains influential today.",
  [(1884, "Proposed electrolytic dissociation theory"), (1889, "Developed the Arrhenius equation for reaction rates"), (1896, "Published first calculations of greenhouse effect"), (1903, "Awarded Nobel Prize in Chemistry")],
  [("Worlds in the Making", 1908, "Popular science book discussing cosmology and the greenhouse effect")],
  [("Humanity stands before a great problem of finding new raw materials and new sources of energy.", "Attributed")])

p("fritz-haber", "Fritz Haber", "フリッツ・ハーバー", 1868, 1934, ["de"], ["chemistry"],
  "Fritz Haber was a German chemist who received the Nobel Prize for synthesizing ammonia from nitrogen and hydrogen, enabling industrial fertilizer production that feeds billions.",
  "Haber was born in Breslau, Prussia, into a Jewish family. He studied at several German universities and converted to Christianity. He became director of the Kaiser Wilhelm Institute for Physical Chemistry.",
  "The Haber-Bosch process for ammonia synthesis enabled mass production of fertilizers, feeding billions. However, Haber also directed the first use of chemical weapons in World War I, a deeply controversial legacy.",
  [(1905, "Began ammonia synthesis research"), (1909, "Demonstrated laboratory ammonia synthesis"), (1915, "Directed chlorine gas attack at Ypres"), (1918, "Awarded Nobel Prize in Chemistry")],
  [("Thermodynamics of Technical Gas Reactions", 1905, "Foundational work on industrial gas-phase chemistry")],
  [("During peacetime a scientist belongs to the World, but during wartime he belongs to his country.", "Attributed")])

p("linus-pauling", "Linus Pauling", "ライナス・ポーリング", 1901, 1994, ["us"], ["chemistry", "physics"],
  "Linus Pauling was an American chemist, biochemist, and peace activist. He is one of only two people to win two unshared Nobel Prizes — in Chemistry and Peace.",
  "Pauling was born in Portland, Oregon. He studied at Oregon Agricultural College and Caltech, where he applied quantum mechanics to chemistry, transforming the understanding of chemical bonds.",
  "Pauling's work on the nature of the chemical bond and molecular structure founded modern structural chemistry. His peace activism against nuclear weapons testing earned him the Nobel Peace Prize.",
  [(1931, "Published The Nature of the Chemical Bond paper"), (1939, "Published book The Nature of the Chemical Bond"), (1954, "Awarded Nobel Prize in Chemistry"), (1962, "Awarded Nobel Peace Prize")],
  [("The Nature of the Chemical Bond", 1939, "Groundbreaking book applying quantum mechanics to chemical bonding")],
  [("The best way to have a good idea is to have a lot of ideas.", "Attributed")])

p("dorothy-hodgkin", "Dorothy Hodgkin", "ドロシー・ホジキン", 1910, 1994, ["gb"], ["chemistry"],
  "Dorothy Hodgkin was a British chemist who advanced the technique of X-ray crystallography to determine the three-dimensional structures of biomolecules, winning the Nobel Prize in Chemistry.",
  "Hodgkin was born in Cairo, Egypt, and grew up in England. She studied at Oxford and Cambridge, becoming fascinated with X-ray crystallography and its potential to reveal molecular structures.",
  "Hodgkin's determination of the structures of penicillin, vitamin B12, and insulin were milestones in biochemistry, enabling understanding and synthesis of life-saving medicines.",
  [(1945, "Determined the structure of penicillin"), (1954, "Determined the structure of vitamin B12"), (1964, "Awarded Nobel Prize in Chemistry"), (1969, "Determined the structure of insulin")],
  [("The X-ray Analysis of Complicated Molecules", 1964, "Nobel lecture describing her crystallographic achievements")],
  [("I was captured for life by chemistry and by crystals.", "Attributed")])

p("rosalind-franklin", "Rosalind Franklin", "ロザリンド・フランクリン", 1920, 1958, ["gb"], ["chemistry", "biology"],
  "Rosalind Franklin was an English chemist and X-ray crystallographer whose work was central to understanding the molecular structures of DNA, RNA, viruses, coal, and graphite.",
  "Franklin was born in London into a prominent Jewish family. She studied at Cambridge and spent time in Paris learning X-ray diffraction techniques before joining King's College London.",
  "Franklin's X-ray diffraction images of DNA, particularly Photo 51, were crucial in determining the double helix structure. Her contributions were not fully recognized during her lifetime.",
  [(1951, "Began DNA X-ray diffraction research at King's College"), (1952, "Took Photo 51 of DNA"), (1953, "Watson and Crick used her data for their model"), (1956, "Published groundbreaking work on tobacco mosaic virus")],
  [("Photo 51", 1952, "The X-ray diffraction image that revealed the helical structure of DNA")],
  [("Science and everyday life cannot and should not be separated.", "Attributed")])

p("ahmed-zewail", "Ahmed Zewail", "アハメド・ズウェイル", 1946, 2016, ["eg", "us"], ["chemistry"],
  "Ahmed Zewail was an Egyptian-American chemist who won the Nobel Prize for his pioneering work in femtochemistry, the study of chemical reactions at extremely short timescales.",
  "Zewail was born in Damanhur, Egypt. He studied at Alexandria University and the University of Pennsylvania before joining Caltech, where he developed femtosecond spectroscopy.",
  "Zewail's femtochemistry allowed scientists to observe atoms during chemical reactions in real time. This revolutionary technique transformed understanding of chemical dynamics.",
  [(1988, "Pioneered femtosecond spectroscopy"), (1999, "Awarded Nobel Prize in Chemistry"), (2009, "Appointed U.S. Science Envoy to the Middle East")],
  [("The Chemical Bond: Structure and Dynamics", 1992, "Comprehensive work on chemical bonding and ultrafast dynamics")],
  [("The real voyage of discovery lies not in seeking new landscapes, but in having new eyes.", "Interview")])

p("joseph-priestley", "Joseph Priestley", "ジョゼフ・プリーストリー", 1733, 1804, ["gb", "us"], ["chemistry"],
  "Joseph Priestley was an English chemist, natural philosopher, and theologian who is credited with the discovery of oxygen, which he called 'dephlogisticated air.'",
  "Priestley was born in Birstall, West Riding of Yorkshire. He was educated for the ministry but developed strong interests in natural philosophy, electricity, and the chemistry of gases.",
  "Priestley's discovery of oxygen and other gases, including nitrous oxide and carbon dioxide, transformed chemistry. His work on photosynthesis showed that plants restore air vitiated by combustion.",
  [(1767, "Published The History of Electricity"), (1771, "Discovered photosynthesis"), (1774, "Isolated oxygen"), (1794, "Emigrated to America due to political persecution")],
  [("Experiments and Observations on Different Kinds of Air", 1774, "Multi-volume work describing the discovery of several gases including oxygen")],
  [("The more elaborate our means of communication, the less we communicate.", "Attributed")])

p("henry-cavendish", "Henry Cavendish", "ヘンリー・キャヴェンディッシュ", 1731, 1810, ["gb"], ["chemistry", "physics"],
  "Henry Cavendish was an English natural philosopher and chemist who discovered hydrogen, determined the composition of water, and measured the density of the Earth.",
  "Cavendish was born in Nice to an aristocratic English family. Extremely shy and reclusive, he studied at Cambridge and devoted his life to scientific research, rarely publishing his results.",
  "Cavendish's discovery of hydrogen, determination of water's composition, and measurement of Earth's density were landmark achievements. Many of his unpublished electrical discoveries predated later rediscoveries.",
  [(1766, "Published paper on hydrogen ('inflammable air')"), (1781, "Demonstrated water is a compound"), (1798, "Measured the density of the Earth")],
  [("Experiments on Air", 1766, "Paper identifying hydrogen as a distinct substance")],
  [("The only remedy for want of observation is more observation.", "Attributed")])

p("amedeo-avogadro", "Amedeo Avogadro", "アメデオ・アヴォガドロ", 1776, 1856, ["it"], ["chemistry", "physics"],
  "Amedeo Avogadro was an Italian scientist known for his contribution to molecular theory, including what is now known as Avogadro's law and Avogadro's number.",
  "Avogadro was born in Turin, Italy. He initially studied law and practiced as a lawyer before turning to science, becoming professor of mathematical physics at the University of Turin.",
  "Avogadro's hypothesis that equal volumes of gases contain equal numbers of molecules provided a key bridge between atomic theory and measurable quantities, unifying chemistry and physics.",
  [(1811, "Published essay proposing Avogadro's law"), (1820, "Became professor at University of Turin")],
  [("Essay on Determining the Relative Masses of Elementary Molecules", 1811, "Paper proposing that equal volumes of gases contain equal numbers of molecules")],
  [("Equal volumes of all gases, at the same temperature and pressure, contain the same number of molecules.", "Essay, 1811")])

p("jacobus-van-t-hoff", "Jacobus Henricus van 't Hoff", "ヤコブス・ヘンリクス・ファント・ホッフ", 1852, 1911, ["nl"], ["chemistry"],
  "Jacobus van 't Hoff was a Dutch physical chemist who won the first Nobel Prize in Chemistry for his work on chemical dynamics and osmotic pressure in solutions.",
  "Van 't Hoff was born in Rotterdam. He studied at Delft, Leiden, Bonn, and Paris, and became professor at the University of Amsterdam before moving to Berlin.",
  "Van 't Hoff founded the field of physical chemistry and stereochemistry. His work on the asymmetric carbon atom explained optical activity, and his studies of solution chemistry earned him the first Nobel Prize in Chemistry.",
  [(1874, "Proposed the tetrahedral carbon atom"), (1884, "Published Études de dynamique chimique"), (1901, "Awarded first Nobel Prize in Chemistry")],
  [("Études de dynamique chimique", 1884, "Foundational work in chemical kinetics and thermodynamics")],
  [("The power of imagination in science is beyond any doubt.", "Attributed")])

p("wilhelm-ostwald", "Wilhelm Ostwald", "ヴィルヘルム・オストヴァルト", 1853, 1932, ["de", "lv"], ["chemistry"],
  "Wilhelm Ostwald was a Baltic German chemist who received the Nobel Prize in Chemistry for his work on catalysis, chemical equilibria, and reaction velocities.",
  "Ostwald was born in Riga, Latvia. He studied at the University of Dorpat and became professor at Leipzig, where he founded one of the first institutes for physical chemistry.",
  "Ostwald helped establish physical chemistry as a discipline. His work on catalysis had vast industrial applications, and the Ostwald process for nitric acid production remains industrially important.",
  [(1884, "Published work on chemical affinity"), (1887, "Co-founded Zeitschrift für physikalische Chemie"), (1902, "Developed the Ostwald process"), (1909, "Awarded Nobel Prize in Chemistry")],
  [("Lehrbuch der allgemeinen Chemie", 1885, "Comprehensive textbook of general chemistry")],
  [("Energy alone is the universal currency of all changes in nature.", "Attributed")])

p("ernest-rutherford", "Ernest Rutherford", "アーネスト・ラザフォード", 1871, 1937, ["nz", "gb"], ["chemistry", "physics"],
  "Ernest Rutherford was a New Zealand-born British physicist who became known as the father of nuclear physics. He won the Nobel Prize in Chemistry for his work on radioactivity.",
  "Rutherford was born in Brightwater, New Zealand. He excelled at school and won a scholarship to Cambridge, where he worked under J.J. Thomson at the Cavendish Laboratory.",
  "Rutherford's discovery of the atomic nucleus, his model of the atom, and his achievement of the first artificial nuclear reaction shaped modern physics and chemistry.",
  [(1898, "Discovered alpha and beta radiation"), (1908, "Awarded Nobel Prize in Chemistry"), (1911, "Proposed the nuclear model of the atom"), (1919, "Achieved first artificial nuclear reaction")],
  [("Radioactive Substances and their Radiations", 1913, "Comprehensive account of radioactivity research")],
  [("All science is either physics or stamp collecting.", "Attributed")])

p("irene-joliot-curie", "Irène Joliot-Curie", "イレーヌ・ジョリオ＝キュリー", 1897, 1956, ["fr"], ["chemistry", "physics"],
  "Irène Joliot-Curie was a French scientist who, together with her husband Frédéric, was awarded the Nobel Prize in Chemistry for the discovery of artificial radioactivity.",
  "Irène was born in Paris, the daughter of Marie and Pierre Curie. She studied at the Faculty of Science in Paris and began working at the Radium Institute during World War I.",
  "The Joliot-Curies' discovery of artificial radioactivity opened the door to nuclear medicine and the production of radioactive isotopes for medical diagnosis and treatment.",
  [(1925, "Completed doctoral thesis on polonium alpha rays"), (1934, "Discovered artificial radioactivity"), (1935, "Awarded Nobel Prize in Chemistry")],
  [("Artificial Production of Radioactive Elements", 1934, "Paper announcing the creation of new radioactive isotopes")],
  [("That one must do some work seriously and must be independent and not merely amuse oneself in life.", "Attributed")])

p("gilbert-lewis", "Gilbert N. Lewis", "ギルバート・ルイス", 1875, 1946, ["us"], ["chemistry"],
  "Gilbert N. Lewis was an American physical chemist known for the discovery of the covalent bond, Lewis dot structures, and his concept of acids and bases.",
  "Lewis was born in Weymouth, Massachusetts. He studied at the University of Nebraska and Harvard, then spent time in Germany before becoming dean of the College of Chemistry at UC Berkeley.",
  "Lewis's electron pair theory of chemical bonding transformed understanding of molecular structure. His concept of Lewis acids and bases remains fundamental in chemistry.",
  [(1902, "Developed cubical atom model"), (1916, "Published electron pair bonding theory"), (1923, "Published Valence and the Structure of Atoms and Molecules"), (1926, "Coined the term 'photon'")],
  [("Valence and the Structure of Atoms and Molecules", 1923, "Definitive work on chemical bonding theory")],
  [("Science has its cathedral.", "Attributed")])

p("robert-bunsen", "Robert Bunsen", "ロベルト・ブンゼン", 1811, 1899, ["de"], ["chemistry"],
  "Robert Bunsen was a German chemist who developed the Bunsen burner, discovered cesium and rubidium using spectroscopy, and pioneered the field of photochemistry.",
  "Bunsen was born in Göttingen, Germany. He studied chemistry at the University of Göttingen and became professor at Heidelberg, where he conducted his most famous research.",
  "Bunsen and Kirchhoff's development of spectroscopy as an analytical tool revolutionized chemistry and astronomy, enabling the identification of elements in stars and the discovery of new elements.",
  [(1841, "Invented the Bunsen cell battery"), (1855, "Developed the Bunsen burner"), (1860, "Discovered cesium by spectroscopy"), (1861, "Discovered rubidium by spectroscopy")],
  [("Photochemical Investigations", 1857, "Pioneering work on the chemical effects of light")],
  [("A chemist who is not a physicist is nothing at all.", "Attributed")])

p("walther-nernst", "Walther Nernst", "ヴァルター・ネルンスト", 1864, 1941, ["de"], ["chemistry", "physics"],
  "Walther Nernst was a German chemist who won the Nobel Prize in Chemistry for his work in thermochemistry, particularly his formulation of the third law of thermodynamics.",
  "Nernst was born in Briesen, West Prussia. He studied physics and mathematics at several universities and became professor at Göttingen, then Berlin.",
  "Nernst's third law of thermodynamics completed the theoretical framework of thermodynamics. The Nernst equation for electrochemistry remains essential in battery and fuel cell research.",
  [(1889, "Developed the Nernst equation"), (1905, "Formulated the third law of thermodynamics"), (1920, "Awarded Nobel Prize in Chemistry")],
  [("The New Heat Theorem", 1906, "Presentation of the third law of thermodynamics")],
  [("The driving force of all scientific work is curiosity about nature.", "Attributed")])

p("marie-anne-lavoisier", "Marie-Anne Paulze Lavoisier", "マリー＝アンヌ・ポルズ・ラヴォアジエ", 1758, 1836, ["fr"], ["chemistry"],
  "Marie-Anne Paulze Lavoisier was a French chemist who made significant contributions to the chemical revolution through her translations, illustrations, and laboratory work alongside Antoine Lavoisier.",
  "Marie-Anne was born in Montbrison, France. She married Antoine Lavoisier at age 13 and quickly became his indispensable scientific collaborator, learning chemistry, languages, and technical drawing.",
  "Marie-Anne's translations of English and Latin chemical texts, her detailed laboratory illustrations, and her editing of Antoine's publications were essential to the chemical revolution.",
  [(1771, "Married Antoine Lavoisier and began scientific work"), (1789, "Illustrated Traité Élémentaire de Chimie"), (1794, "Antoine Lavoisier executed"), (1805, "Published memoirs of chemistry")],
  [("Illustrations for Traité Élémentaire de Chimie", 1789, "Detailed scientific illustrations for the first modern chemistry textbook")],
  [("She participated in the work of the laboratory and the progress of science.", "Contemporary description")])

p("william-henry-perkin", "William Henry Perkin", "ウィリアム・ヘンリー・パーキン", 1838, 1907, ["gb"], ["chemistry"],
  "William Henry Perkin was a British chemist who discovered the first synthetic aniline dye, mauveine, launching the synthetic dye industry and transforming organic chemistry.",
  "Perkin was born in London. At age 15 he entered the Royal College of Chemistry, where he studied under August Wilhelm von Hofmann and began experiments attempting to synthesize quinine.",
  "Perkin's accidental discovery of mauveine launched the synthetic dye industry, which in turn gave rise to the pharmaceutical and chemical industries. His work showed the commercial potential of organic chemistry.",
  [(1856, "Discovered mauveine, the first synthetic dye"), (1857, "Opened dye factory at age 18"), (1874, "Discovered the Perkin reaction")],
  [("Mauveine", 1856, "The first commercially successful synthetic dye, producing a purple color")],
  [("Chemistry itself knows altogether too well that—given the real molecules—the others, their geometrical isomers, provide endless difficulties.", "Attributed")])

p("percy-julian", "Percy Lavon Julian", "パーシー・ジュリアン", 1899, 1975, ["us"], ["chemistry"],
  "Percy Julian was an American research chemist and a pioneer in the chemical synthesis of medicinal drugs from plants, particularly steroids and cortisone.",
  "Julian was born in Montgomery, Alabama. He faced severe racial discrimination but excelled academically, eventually earning his PhD from the University of Vienna.",
  "Julian's synthesis of physostigmine and cortisone from soy products made life-saving medications affordable and accessible. He was one of the first African Americans inducted into the National Academy of Sciences.",
  [(1935, "Completed total synthesis of physostigmine"), (1940, "Developed mass production of steroids from soybeans"), (1954, "Founded Julian Laboratories"), (1973, "Elected to National Academy of Sciences")],
  [("Total Synthesis of Physostigmine", 1935, "First complete synthesis of the glaucoma drug from plant materials")],
  [("I have had one goal in my life, that of playing some role in making life a little easier for the persons who come after me.", "Attributed")])

p("wallace-carothers", "Wallace Carothers", "ウォーレス・カロザース", 1896, 1937, ["us"], ["chemistry"],
  "Wallace Carothers was an American chemist and inventor who led pioneering work in polymer chemistry, inventing nylon and neoprene.",
  "Carothers was born in Burlington, Iowa. He studied at Tarkio College and the University of Illinois, then joined DuPont's research laboratory.",
  "Carothers' invention of nylon and neoprene launched the modern synthetic polymer industry. His theoretical work on condensation polymerization laid the foundation for polymer science.",
  [(1928, "Joined DuPont research"), (1930, "Invented neoprene synthetic rubber"), (1935, "Invented nylon"), (1936, "Elected to National Academy of Sciences")],
  [("Nylon", 1935, "The first commercially successful synthetic fiber")],
  [("An adventure in pure science has ended in a practical result of major importance.", "DuPont description of nylon")])

p("otto-hahn", "Otto Hahn", "オットー・ハーン", 1879, 1968, ["de"], ["chemistry", "physics"],
  "Otto Hahn was a German chemist who won the Nobel Prize in Chemistry for his discovery of nuclear fission of heavy atomic nuclei.",
  "Hahn was born in Frankfurt am Main. He studied chemistry in Marburg and worked with Rutherford in Montreal and Ramsay in London before returning to Berlin.",
  "Hahn's discovery of nuclear fission, together with Lise Meitner and Fritz Strassmann, was one of the most consequential scientific discoveries of the 20th century, leading to nuclear energy and weapons.",
  [(1905, "Discovered radiothorium"), (1917, "Co-discovered protactinium"), (1938, "Discovered nuclear fission of uranium"), (1944, "Awarded Nobel Prize in Chemistry")],
  [("On the Detection and Characteristics of the Alkaline Earth Metals Formed by Irradiation of Uranium", 1939, "Paper reporting the discovery of nuclear fission")],
  [("I only wish that the discovery had been made earlier, so that it could have been used for peace.", "Attributed")])

p("lise-meitner", "Lise Meitner", "リーゼ・マイトナー", 1878, 1968, ["at", "se"], ["chemistry", "physics"],
  "Lise Meitner was an Austrian-Swedish physicist who contributed to the discovery of nuclear fission. Despite her critical role, she was overlooked for the Nobel Prize.",
  "Meitner was born in Vienna. She was the second woman to earn a physics doctorate from the University of Vienna. She worked with Otto Hahn in Berlin for over 30 years.",
  "Meitner's theoretical explanation of nuclear fission was essential to understanding the process. Element 109, meitnerium, is named in her honor.",
  [(1906, "Earned PhD in physics from University of Vienna"), (1918, "Co-discovered protactinium with Hahn"), (1938, "Fled Nazi Germany to Sweden"), (1939, "Published theoretical explanation of nuclear fission")],
  [("Disintegration of Uranium by Neutrons: A New Type of Nuclear Reaction", 1939, "Paper providing the first theoretical explanation of nuclear fission")],
  [("Science makes people reach selflessly for truth and objectivity.", "Attributed")])

p("glenn-seaborg", "Glenn T. Seaborg", "グレン・シーボーグ", 1912, 1999, ["us"], ["chemistry", "physics"],
  "Glenn Seaborg was an American chemist who won the Nobel Prize for discoveries in the chemistry of transuranium elements. He identified or co-discovered ten elements.",
  "Seaborg was born in Ishpeming, Michigan. He studied at UCLA and UC Berkeley, where he became involved in nuclear chemistry research.",
  "Seaborg's discovery of plutonium and other transuranium elements reshaped the periodic table. His actinide concept reorganized the heavy elements and predicted the properties of yet-undiscovered elements.",
  [(1940, "Co-discovered plutonium"), (1944, "Proposed the actinide concept"), (1951, "Awarded Nobel Prize in Chemistry"), (1961, "Became chairman of the Atomic Energy Commission")],
  [("The Transuranium Elements", 1958, "Comprehensive work on artificial elements beyond uranium")],
  [("There is a beauty in discovery. There is mathematics in music, a kinship of science and poetry.", "Attributed")])

p("robert-woodward", "Robert Burns Woodward", "ロバート・バーンズ・ウッドワード", 1917, 1979, ["us"], ["chemistry"],
  "Robert Burns Woodward was an American organic chemist who won the Nobel Prize for his outstanding achievements in the art of organic synthesis.",
  "Woodward was born in Boston. A child prodigy, he entered MIT at age 16 and received his PhD at 20. He spent most of his career at Harvard.",
  "Woodward's total syntheses of quinine, cholesterol, cortisone, chlorophyll, and vitamin B12 were masterpieces of chemical strategy. The Woodward-Hoffmann rules transformed understanding of organic reactions.",
  [(1944, "Synthesized quinine"), (1951, "Synthesized cholesterol and cortisone"), (1960, "Synthesized chlorophyll"), (1965, "Awarded Nobel Prize in Chemistry"), (1971, "Synthesized vitamin B12")],
  [("Vitamin B12 Total Synthesis", 1971, "The most complex total synthesis achieved at that time")],
  [("The structure known, but not yet accessible by synthesis, is to the chemist what the unclimbed mountain, the ## uncharted sea, the untilled field are to other men.", "Attributed")])

p("marie-maynard-daly", "Marie Maynard Daly", "マリー・メイナード・デイリー", 1921, 2003, ["us"], ["chemistry", "biology"],
  "Marie Maynard Daly was an American biochemist and the first African American woman in the United States to earn a PhD in chemistry.",
  "Daly was born in Queens, New York. Inspired by her father's unfulfilled dream of becoming a chemist and by Paul de Kruif's Microbe Hunters, she pursued chemistry at Queens College and Columbia University.",
  "Daly's research on the biochemistry of histones, protein synthesis, and the relationship between cholesterol and hypertension contributed significantly to understanding heart disease.",
  [(1947, "Earned PhD from Columbia, first African American woman to do so"), (1955, "Researched protein synthesis and nucleic acids"), (1960, "Studied relationship between cholesterol and heart attacks"), (1988, "Established scholarship for minority science students")],
  [("The Composition of the Histone Fraction of the Thymus Nucleohistone", 1951, "Pioneering research on histone proteins and their role in cell nuclei")],
  [("Courage is like—it's a habitus, a habit, a virtue: you get it by courageous acts.", "Attributed")])

p("carl-wilhelm-scheele", "Carl Wilhelm Scheele", "カール・ヴィルヘルム・シェーレ", 1742, 1786, ["se"], ["chemistry"],
  "Carl Wilhelm Scheele was a Swedish-German pharmaceutical chemist who discovered oxygen independently of Priestley, as well as chlorine, manganese, and several organic acids.",
  "Scheele was born in Stralsund, then Swedish Pomerania. He was apprenticed to an apothecary at age 14 and became an accomplished experimental chemist without formal university education.",
  "Scheele discovered more chemical elements and compounds than any chemist of his era. His independent discovery of oxygen and identification of numerous organic acids expanded chemistry enormously.",
  [(1770, "Discovered tartaric acid"), (1772, "Discovered oxygen (published 1777)"), (1774, "Discovered chlorine and manganese"), (1780, "Discovered lactic acid and other organic compounds")],
  [("Chemical Observations and Experiments on Air and Fire", 1777, "Described the discovery of oxygen and nitrogen")],
  [("It is the truth alone that we desire to know, and what joy it is to discover it.", "Attributed")])

p("friedrich-august-kekule", "Archibald Scott Couper", "アーチボルド・スコット・クーパー", 1831, 1892, ["gb"], ["chemistry"],
  "Archibald Scott Couper was a Scottish chemist who proposed that carbon atoms can link to each other to form chains, independently of Kekulé, laying groundwork for structural chemistry.",
  "Couper was born in Kirkintilloch, Scotland. He studied philosophy and languages before turning to chemistry, working with Charles Adolphe Wurtz in Paris.",
  "Couper's theory of carbon self-linking and his use of lines to represent bonds were foundational contributions to structural organic chemistry, though he received less recognition than Kekulé.",
  [(1858, "Published 'On a New Chemical Theory' proposing carbon chains"), (1859, "Suffered mental breakdown, ending his career")],
  [("On a New Chemical Theory", 1858, "Paper proposing that carbon atoms bond to each other in chains")],
  [("The art of the chemist consists in making the right experiments.", "Attributed")])

p("stanislao-cannizzaro", "Stanislao Cannizzaro", "スタニスラオ・カニッツァーロ", 1826, 1910, ["it"], ["chemistry"],
  "Stanislao Cannizzaro was an Italian chemist who revived Avogadro's hypothesis and established a consistent system of atomic weights that unified chemistry.",
  "Cannizzaro was born in Palermo, Sicily. He studied in several Italian cities and participated in the Sicilian revolution of 1848 before fleeing to Paris, where he worked with Chevreul.",
  "Cannizzaro's presentation at the Karlsruhe Congress of 1860 resolved confusion about atomic weights and molecular formulas, enabling Mendeleev's periodic table.",
  [(1853, "Discovered the Cannizzaro reaction"), (1858, "Published pamphlet on atomic weights"), (1860, "Presented unified system at Karlsruhe Congress")],
  [("Sketch of a Course of Chemical Philosophy", 1858, "Pamphlet that clarified the distinction between atomic and molecular weights")],
  [("I believe one of the most important tasks of science is to bring clarity to confused ideas.", "Attributed")])

p("william-ramsay", "William Ramsay", "ウィリアム・ラムゼー", 1852, 1916, ["gb"], ["chemistry"],
  "William Ramsay was a Scottish chemist who discovered the noble gases and received the Nobel Prize in Chemistry for adding an entire new group to the periodic table.",
  "Ramsay was born in Glasgow, Scotland. He studied at the University of Glasgow and in Germany under Robert Bunsen, before becoming professor at University College London.",
  "Ramsay's discovery of argon, helium, neon, krypton, and xenon revealed an entirely new group of elements, fundamentally expanding understanding of atomic structure and the periodic table.",
  [(1894, "Discovered argon with Lord Rayleigh"), (1895, "Isolated helium on Earth"), (1898, "Discovered neon, krypton, and xenon"), (1904, "Awarded Nobel Prize in Chemistry")],
  [("The Gases of the Atmosphere", 1896, "Comprehensive work on atmospheric gases including the noble gases")],
  [("Progress is made by trial and failure; the failures are generally a hundred times more numerous than the successes.", "Attributed")])

p("alfred-werner", "Alfred Werner", "アルフレッド・ヴェルナー", 1866, 1919, ["ch", "fr"], ["chemistry"],
  "Alfred Werner was a Swiss chemist who won the Nobel Prize for proposing the octahedral configuration of transition metal complexes, founding coordination chemistry.",
  "Werner was born in Mulhouse, Alsace. He studied at the Swiss Federal Institute of Technology in Zurich and became professor at the University of Zurich.",
  "Werner's coordination theory explained the bonding and structure of metal complexes, creating the field of coordination chemistry and transforming inorganic chemistry.",
  [(1893, "Proposed coordination theory"), (1911, "Experimentally confirmed octahedral geometry"), (1913, "Awarded Nobel Prize in Chemistry")],
  [("New Ideas on Inorganic Chemistry", 1905, "Definitive presentation of coordination theory")],
  [("Only when chemistry has been seen as the study of three-dimensional structures can it truly be called a science.", "Attributed")])

p("hermann-staudinger", "Hermann Staudinger", "ヘルマン・シュタウディンガー", 1881, 1965, ["de"], ["chemistry"],
  "Hermann Staudinger was a German organic chemist who demonstrated the existence of macromolecules, founding polymer chemistry and winning the Nobel Prize.",
  "Staudinger was born in Worms, Germany. He studied at several German universities and became professor at Freiburg, where he spent most of his career.",
  "Staudinger's proof that polymers are long-chain molecules, against the prevailing aggregate theory, founded modern polymer science and enabled the development of plastics, synthetic fibers, and rubber.",
  [(1920, "Proposed macromolecular hypothesis"), (1926, "Published comprehensive work on polymerization"), (1953, "Awarded Nobel Prize in Chemistry")],
  [("On Polymerization", 1920, "Landmark paper proposing that polymers are true macromolecules")],
  [("The future will show whether my persistent conviction was a sign of healthy or pathological doggedness.", "Attributed")])

p("peter-debye", "Peter Debye", "ペーター・デバイ", 1884, 1966, ["nl", "us"], ["chemistry", "physics"],
  "Peter Debye was a Dutch-American physicist and physical chemist who won the Nobel Prize in Chemistry for his contributions to knowledge of molecular structure through dipole moments and X-ray diffraction.",
  "Debye was born in Maastricht, Netherlands. He studied at the Aachen University of Technology and the University of Munich, holding professorships across Europe before moving to Cornell.",
  "Debye's work on dipole moments, X-ray diffraction, and the theory of specific heat at low temperatures provided essential tools for understanding molecular structure and solid-state physics.",
  [(1912, "Extended Einstein's theory of specific heat"), (1916, "Developed powder diffraction method"), (1923, "Developed Debye-Hückel theory of electrolytes"), (1936, "Awarded Nobel Prize in Chemistry")],
  [("Polar Molecules", 1929, "Comprehensive treatise on molecular dipole moments")],
  [("Science is the art of the soluble.", "Attributed")])

p("gerhard-ertl", "Gerhard Ertl", "ゲアハルト・エルトル", 1936, None, ["de"], ["chemistry"],
  "Gerhard Ertl is a German physicist and physical chemist who won the Nobel Prize in Chemistry for his studies of chemical processes on solid surfaces.",
  "Ertl was born in Stuttgart, Germany. He studied physics at the Technical University of Stuttgart and the University of Munich, becoming director at the Fritz Haber Institute in Berlin.",
  "Ertl's meticulous studies of surface chemistry explained the Haber-Bosch process at the atomic level and advanced understanding of catalysis, corrosion, and fuel cells.",
  [(1967, "Began systematic surface chemistry research"), (1986, "Explained Haber-Bosch process mechanism on iron surfaces"), (2007, "Awarded Nobel Prize in Chemistry")],
  [("Reactions at Solid Surfaces", 2009, "Comprehensive work on the chemistry of solid surfaces")],
  [("Surface science is the art of looking at surfaces at the atomic level.", "Attributed")])

p("mario-molina", "Mario Molina", "マリオ・モリーナ", 1943, 2020, ["mx", "us"], ["chemistry"],
  "Mario Molina was a Mexican-American chemist who co-discovered the threat of chlorofluorocarbon gases to the ozone layer, earning the Nobel Prize in Chemistry.",
  "Molina was born in Mexico City. He studied at UNAM, then in Germany and at UC Berkeley, before joining MIT.",
  "Molina's research on ozone depletion by CFCs led to the Montreal Protocol, one of the most successful environmental agreements in history, saving the ozone layer.",
  [(1974, "Published CFC-ozone depletion theory with Rowland"), (1985, "Antarctic ozone hole confirmed the theory"), (1995, "Awarded Nobel Prize in Chemistry")],
  [("Stratospheric Sink for Chlorofluoromethanes", 1974, "Paper predicting CFC destruction of the ozone layer")],
  [("What is important is to dare to take the first step and make a difference.", "Attributed")])

p("ada-yonath", "Ada Yonath", "アダ・ヨナス", 1939, None, ["il"], ["chemistry", "biology"],
  "Ada Yonath is an Israeli crystallographer who won the Nobel Prize in Chemistry for studies of the structure and function of the ribosome.",
  "Yonath was born in Jerusalem. She grew up in poverty but excelled academically, studying at the Hebrew University and the Weizmann Institute of Science.",
  "Yonath's determination of ribosome structure at atomic resolution was a breakthrough in structural biology, enabling the design of new antibiotics and understanding of protein synthesis.",
  [(1980, "Began ribosome crystallography research"), (1998, "Achieved first ribosome crystal structure"), (2009, "Awarded Nobel Prize in Chemistry")],
  [("Ribosome Crystal Structure", 2000, "First high-resolution atomic structure of the ribosome")],
  [("If you do not aim too high, you cannot reach anything.", "Attributed")])

p("frances-arnold", "Frances Arnold", "フランシス・アーノルド", 1956, None, ["us"], ["chemistry", "biology"],
  "Frances Arnold is an American chemical engineer and Nobel laureate who pioneered the use of directed evolution to engineer enzymes.",
  "Arnold was born in Pittsburgh, Pennsylvania. She studied at Princeton and UC Berkeley before joining Caltech, where she developed methods for directed evolution of proteins.",
  "Arnold's directed evolution methods revolutionized enzyme engineering, enabling the creation of novel biocatalysts for pharmaceutical, chemical, and fuel production.",
  [(1993, "Published first directed evolution of enzymes"), (2018, "Awarded Nobel Prize in Chemistry")],
  [("Directed Evolution of Subtilisin E", 1993, "Landmark paper demonstrating enzyme optimization through directed evolution")],
  [("Evolution is the most powerful engineering method in the world.", "Attributed")])

p("jacobus-van-t-hoff-jr", "Emil Fischer", "エミール・フィッシャー", 1852, 1919, ["de"], ["chemistry"],
  "Emil Fischer was a German chemist who won the Nobel Prize for his work on sugar and purine syntheses. He is considered the founder of biochemistry.",
  "Fischer was born in Euskirchen, Germany. He studied at the University of Bonn and Strasbourg under Adolf von Baeyer, and became professor at the University of Berlin.",
  "Fischer's work on sugars, amino acids, and purines laid the foundation for biochemistry. His lock-and-key model of enzyme specificity remains a fundamental concept in biology.",
  [(1884, "Synthesized phenylhydrazine for sugar analysis"), (1890, "Established structures of glucose and fructose"), (1902, "Awarded Nobel Prize in Chemistry"), (1907, "Began pioneering peptide synthesis work")],
  [("Investigations on Purines", 1882, "Comprehensive study of purine chemistry and caffeine synthesis")],
  [("One can try to be creative but one must remain precise.", "Attributed")])

p("irving-langmuir", "Irving Langmuir", "アーヴィング・ラングミュア", 1881, 1957, ["us"], ["chemistry", "physics"],
  "Irving Langmuir was an American chemist and physicist who received the Nobel Prize in Chemistry for his discoveries and investigations in surface chemistry.",
  "Langmuir was born in Brooklyn, New York. He studied at Columbia and in Germany under Walther Nernst, then joined General Electric's research laboratory.",
  "Langmuir's work on surface chemistry and thin films advanced understanding of chemical bonding and catalysis. His inventions improved vacuum tubes and incandescent lighting.",
  [(1913, "Developed improved incandescent lamp"), (1916, "Published adsorption theory"), (1932, "Awarded Nobel Prize in Chemistry"), (1946, "Pioneered cloud seeding experiments")],
  [("The Constitution and Fundamental Properties of Solids and Liquids", 1916, "Foundational paper on surface chemistry and adsorption isotherms")],
  [("The scientist is not a person who gives the right answers, he's one who asks the right questions.", "Attributed")])

p("karl-ziegler", "Karl Ziegler", "カール・ツィーグラー", 1898, 1973, ["de"], ["chemistry"],
  "Karl Ziegler was a German chemist who won the Nobel Prize for discoveries in the field of polymer chemistry, developing catalysts for polymerization.",
  "Ziegler was born in Helsa, Germany. He studied at the University of Marburg and became director of the Max Planck Institute for Coal Research in Mülheim.",
  "Ziegler's development of organometallic catalysts for polyethylene production, together with Natta's work on polypropylene, revolutionized the plastics industry.",
  [(1953, "Discovered Ziegler catalyst for polyethylene"), (1955, "Industrial production of polyethylene began"), (1963, "Awarded Nobel Prize in Chemistry with Natta")],
  [("Consequences and Development of an Invention", 1963, "Nobel lecture describing the development of Ziegler catalysts")],
  [("Research must be free and uninhibited.", "Attributed")])

p("giulio-natta", "Giulio Natta", "ジュリオ・ナッタ", 1903, 1979, ["it"], ["chemistry"],
  "Giulio Natta was an Italian chemist who won the Nobel Prize for his work on high polymers, developing stereospecific polymerization to create isotactic polypropylene.",
  "Natta was born in Imperia, Italy. He studied at the Milan Polytechnic and became professor of industrial chemistry there.",
  "Natta's discovery of stereoregular polymers and isotactic polypropylene, building on Ziegler's catalysts, enabled the production of new plastics with controlled properties.",
  [(1954, "Developed isotactic polypropylene"), (1957, "Published work on stereoregular polymerization"), (1963, "Awarded Nobel Prize in Chemistry with Ziegler")],
  [("Stereospecific Polymerization", 1955, "Papers describing the synthesis of stereoregular polymers")],
  [("Research without application is like a beautiful flower without fragrance.", "Attributed")])

p("ahmed-hassanein", "Kenichi Fukui", "福井謙一", 1918, 1998, ["jp"], ["chemistry"],
  "Kenichi Fukui was a Japanese chemist who shared the Nobel Prize in Chemistry for his theories concerning the course of chemical reactions, specifically frontier molecular orbital theory.",
  "Fukui was born in Nara, Japan. He studied at Kyoto Imperial University, where he spent his entire career as professor of physical chemistry.",
  "Fukui's frontier molecular orbital theory explained chemical reactivity in terms of the highest occupied and lowest unoccupied molecular orbitals, transforming theoretical organic chemistry.",
  [(1952, "Published frontier molecular orbital theory"), (1964, "Extended FMO theory to pericyclic reactions"), (1981, "Awarded Nobel Prize in Chemistry")],
  [("Theory of Orientation and Stereoselection", 1952, "Paper introducing frontier molecular orbital theory")],
  [("Theory and experiment must go hand in hand in chemistry.", "Attributed")])

p("roald-hoffmann", "Roald Hoffmann", "ロアルド・ホフマン", 1937, None, ["us", "pl"], ["chemistry"],
  "Roald Hoffmann is a Polish-American theoretical chemist who won the Nobel Prize for his theories on the course of chemical reactions, particularly the Woodward-Hoffmann rules.",
  "Hoffmann was born in Złoczów, Poland. A Holocaust survivor, he emigrated to the United States and studied at Columbia and Harvard, where he worked with R.B. Woodward.",
  "The Woodward-Hoffmann rules for conservation of orbital symmetry transformed understanding of organic reactions. Hoffmann also developed extended Hückel theory for molecular orbital calculations.",
  [(1965, "Developed Woodward-Hoffmann rules"), (1963, "Developed extended Hückel theory"), (1981, "Awarded Nobel Prize in Chemistry")],
  [("The Conservation of Orbital Symmetry", 1970, "Definitive work on the Woodward-Hoffmann rules")],
  [("Chemistry is a rich and complex science — both an art and a science.", "Attributed")])

p("ilya-prigogine", "Ilya Prigogine", "イリヤ・プリゴジン", 1917, 2003, ["be", "ru"], ["chemistry", "physics"],
  "Ilya Prigogine was a Belgian physical chemist who won the Nobel Prize for his contributions to non-equilibrium thermodynamics, particularly the theory of dissipative structures.",
  "Prigogine was born in Moscow, Russia, and his family emigrated to Belgium when he was a child. He studied at the Université Libre de Bruxelles, where he spent most of his career.",
  "Prigogine's theory of dissipative structures showed how order can emerge from chaos in systems far from equilibrium, bridging physics, chemistry, and biology.",
  [(1945, "Published early work on irreversible thermodynamics"), (1967, "Developed theory of dissipative structures"), (1977, "Awarded Nobel Prize in Chemistry")],
  [("Order Out of Chaos", 1984, "Popular book on self-organization in non-equilibrium systems")],
  [("The future is not given. It is constructed.", "Order Out of Chaos")])

p("du-pont-carothers-nylon", "Leo Baekeland", "レオ・ベークランド", 1863, 1944, ["be", "us"], ["chemistry", "engineering"],
  "Leo Baekeland was a Belgian-American chemist who invented Bakelite, the first fully synthetic plastic, launching the Age of Plastics.",
  "Baekeland was born in Ghent, Belgium. He studied at the University of Ghent and emigrated to the United States, where he first invented Velox photographic paper.",
  "Baekeland's invention of Bakelite in 1907 created the first true synthetic plastic, transforming manufacturing and daily life across the 20th century.",
  [(1893, "Emigrated to the United States"), (1899, "Sold Velox photographic paper to Eastman Kodak"), (1907, "Invented Bakelite"), (1910, "Founded Bakelite Corporation")],
  [("Bakelite", 1907, "The first fully synthetic thermosetting plastic")],
  [("I was trying to make something really hard, but then I thought I should make something really useful.", "Attributed")])

p("carl-bosch", "Carl Bosch", "カール・ボッシュ", 1874, 1940, ["de"], ["chemistry", "engineering"],
  "Carl Bosch was a German chemist and engineer who won the Nobel Prize for contributions to the invention and development of chemical high-pressure methods, including the Haber-Bosch process.",
  "Bosch was born in Cologne, Germany. He studied metallurgy and chemistry, then joined BASF where he developed the industrial-scale ammonia synthesis process.",
  "Bosch's engineering of the Haber-Bosch process for industrial ammonia production enabled mass production of fertilizers, fundamentally increasing global food production.",
  [(1909, "Began scaling up Haber's ammonia synthesis"), (1913, "First industrial ammonia plant at Oppau"), (1931, "Awarded Nobel Prize in Chemistry")],
  [("Industrial Ammonia Synthesis", 1913, "Engineering achievement scaling laboratory ammonia synthesis to industrial production")],
  [("The development of high-pressure chemistry opened up a new world.", "Nobel lecture, 1932")])

if __name__ == '__main__':
    # Fix IDs that don't match expected patterns
    for entry in P:
        if entry['id'] == 'jacobus-van-t-hoff-jr':
            entry['id'] = 'emil-fischer'
        elif entry['id'] == 'ahmed-hassanein':
            entry['id'] = 'kenichi-fukui'
        elif entry['id'] == 'du-pont-carothers-nylon':
            entry['id'] = 'leo-baekeland'
        elif entry['id'] == 'friedrich-august-kekule':
            entry['id'] = 'archibald-scott-couper'
    write_people(P)
