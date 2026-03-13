#!/usr/bin/env python3
"""Supplement batch 1: more people across all categories to reach 1000."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# === MORE PHYSICISTS ===
p("murray-gell-mann", "Murray Gell-Mann", "マレー・ゲルマン", 1929, 2019, ["us"], ["physics"],
  "Murray Gell-Mann was an American physicist who received the Nobel Prize for his work on the theory of elementary particles, including the quark model.",
  "Gell-Mann was born in Manhattan, New York. A prodigy, he entered Yale at 15 and received his PhD from MIT at 21.",
  "Gell-Mann's quark model and the Eightfold Way classification of subatomic particles brought order to particle physics.",
  [(1961, "Proposed the Eightfold Way"), (1964, "Proposed the quark model"), (1969, "Awarded Nobel Prize in Physics")],
  [("The Quark and the Jaguar", 1994, "Book on complexity and simplicity in nature")],
  [("Think how hard physics would be if particles could think.", "Attributed")])

p("steven-weinberg", "Steven Weinberg", "スティーヴン・ワインバーグ", 1933, 2021, ["us"], ["physics"],
  "Steven Weinberg was an American theoretical physicist who shared the Nobel Prize for the unification of the weak force and electromagnetic interaction.",
  "Weinberg was born in New York City. He studied at Cornell and Princeton before joining Harvard and later the University of Texas at Austin.",
  "Weinberg's electroweak unification was a major step toward a unified theory of fundamental forces, shaping the Standard Model of particle physics.",
  [(1967, "Proposed electroweak unification"), (1979, "Awarded Nobel Prize in Physics"), (1977, "Published The First Three Minutes")],
  [("The First Three Minutes", 1977, "Popular account of the Big Bang and the early universe")],
  [("The effort to understand the universe is one of the very few things which lifts human life above the level of farce.", "The First Three Minutes")])

p("hans-bethe", "Hans Bethe", "ハンス・ベーテ", 1906, 2005, ["de", "us"], ["physics"],
  "Hans Bethe was a German-American nuclear physicist who won the Nobel Prize for his work on the theory of stellar nucleosynthesis.",
  "Bethe was born in Strasbourg. He fled Nazi Germany and joined Cornell University, later becoming head of the theoretical division at Los Alamos.",
  "Bethe's discovery of the carbon-nitrogen-oxygen cycle that powers stars was a landmark in astrophysics. He also contributed significantly to quantum electrodynamics.",
  [(1938, "Explained energy production in stars"), (1943, "Headed theoretical division at Los Alamos"), (1967, "Awarded Nobel Prize in Physics")],
  [("Energy Production in Stars", 1939, "Paper explaining the nuclear reactions that power the Sun")],
  [("If we fight a war and win it with H-bombs, what history will remember is not the ideals we were fighting for but the methods we used to accomplish them.", "Attributed")])

p("chen-ning-yang", "Chen-Ning Yang", "楊振寧", 1922, None, ["cn", "us"], ["physics"],
  "Chen-Ning Yang is a Chinese-American physicist who won the Nobel Prize for his work on parity non-conservation of weak interactions.",
  "Yang was born in Hefei, China. He studied at Tsinghua University and the University of Chicago before joining the Institute for Advanced Study in Princeton.",
  "Yang's proof that parity is not conserved in weak interactions overturned a fundamental assumption of physics. The Yang-Mills theory became the basis of the Standard Model.",
  [(1954, "Proposed Yang-Mills gauge theory"), (1956, "Predicted parity violation with Lee"), (1957, "Awarded Nobel Prize in Physics")],
  [("Yang-Mills Theory", 1954, "Gauge theory that became the foundation of the Standard Model")],
  [("In physics, you don't have to go around making trouble for yourself — nature does it for you.", "Attributed")])

p("abdus-salam", "Abdus Salam", "アブドゥッサラーム", 1926, 1996, ["pk"], ["physics"],
  "Abdus Salam was a Pakistani theoretical physicist who shared the Nobel Prize for the electroweak unification theory. He was the first Pakistani Nobel laureate.",
  "Salam was born in Jhang, Punjab. He studied at Government College Lahore and Cambridge, becoming one of the most influential theoretical physicists of his era.",
  "Salam's contributions to electroweak theory helped establish the Standard Model. He also championed scientific development in the developing world.",
  [(1957, "Proposed two-component neutrino theory"), (1968, "Proposed electroweak unification independently"), (1979, "Awarded Nobel Prize in Physics"), (1964, "Founded ICTP in Trieste")],
  [("International Centre for Theoretical Physics", 1964, "Research center for scientists from developing countries")],
  [("Scientific thought and its creation are the common and shared heritage of mankind.", "Nobel lecture")])

p("emmy-noether", "Emmy Noether", "エミー・ネーター", 1882, 1935, ["de", "us"], ["mathematics", "physics"],
  "Emmy Noether was a German mathematician who made groundbreaking contributions to abstract algebra and theoretical physics, including Noether's theorem.",
  "Noether was born in Erlangen, Germany. She overcame severe discrimination against women in academia to become one of the most important mathematicians of the 20th century.",
  "Noether's theorem, linking symmetry and conservation laws, is fundamental to modern physics. Her work in abstract algebra transformed the field.",
  [(1915, "Proved Noether's theorem"), (1921, "Published foundational work on ideal theory"), (1933, "Fled Nazi Germany to the United States")],
  [("Noether's Theorem", 1915, "Theorem connecting symmetries in physics to conservation laws")],
  [("My methods are really methods of working and thinking; this is why they have crept in everywhere anonymously.", "Attributed")])

p("freeman-dyson", "Freeman Dyson", "フリーマン・ダイソン", 1923, 2020, ["gb", "us"], ["physics", "mathematics"],
  "Freeman Dyson was a British-American theoretical physicist and mathematician known for his work in quantum electrodynamics, solid-state physics, and nuclear engineering.",
  "Dyson was born in Crowthorne, England. He studied at Cambridge and Cornell, where he unified the approaches of Feynman, Schwinger, and Tomonaga to QED.",
  "Dyson's unification of quantum electrodynamics approaches made the theory practically usable. His Dyson sphere concept and contributions to nuclear policy made him a public intellectual.",
  [(1949, "Unified approaches to QED"), (1953, "Proposed random matrix theory applications"), (1960, "Proposed the Dyson sphere concept")],
  [("Disturbing the Universe", 1979, "Autobiography reflecting on science and society")],
  [("It is better to be wrong than to be vague.", "Attributed")])

p("john-archibald-wheeler", "John Archibald Wheeler", "ジョン・アーチボルド・ウィーラー", 1911, 2008, ["us"], ["physics"],
  "John Archibald Wheeler was an American theoretical physicist who coined the terms 'black hole,' 'wormhole,' and 'quantum foam.'",
  "Wheeler was born in Jacksonville, Florida. He studied at Johns Hopkins and worked with Niels Bohr on nuclear fission before becoming professor at Princeton.",
  "Wheeler's ideas on quantum gravity, black holes, and the role of the observer in quantum mechanics shaped modern physics. He mentored Feynman and many other leading physicists.",
  [(1939, "Co-authored theory of nuclear fission with Bohr"), (1957, "Published Geometrodynamics"), (1967, "Coined the term 'black hole'"), (1983, "Proposed the delayed-choice experiment")],
  [("Gravitation", 1973, "Comprehensive textbook on general relativity co-authored with Misner and Thorne")],
  [("We live on an island surrounded by a sea of ignorance. As our island of knowledge grows, so does the shore of our ignorance.", "Attributed")])

# === MORE MATHEMATICIANS ===
p("alan-turing-math", "Alonzo Church", "アロンゾ・チャーチ", 1903, 1995, ["us"], ["mathematics"],
  "Alonzo Church was an American mathematician and logician who made major contributions to mathematical logic and theoretical computer science.",
  "Church was born in Washington, D.C. He studied at Princeton, where he spent most of his career and supervised many influential doctoral students including Alan Turing.",
  "Church's lambda calculus and his proof of the undecidability of first-order logic were foundational contributions to computer science and mathematical logic.",
  [(1932, "Developed lambda calculus"), (1936, "Proved undecidability of first-order logic"), (1936, "Published Church's thesis on computability")],
  [("An Unsolvable Problem of Elementary Number Theory", 1936, "Paper proving the undecidability of certain mathematical problems")],
  [("A function is a rule of correspondence.", "Introduction to Mathematical Logic")])

p("kurt-godel", "Kurt Gödel", "クルト・ゲーデル", 1906, 1978, ["at", "us"], ["mathematics"],
  "Kurt Gödel was an Austrian-American logician and mathematician who proved the incompleteness theorems, among the most important results in mathematical logic.",
  "Gödel was born in Brünn, Austria-Hungary. He studied at the University of Vienna and emigrated to the United States, where he joined the Institute for Advanced Study.",
  "Gödel's incompleteness theorems demonstrated fundamental limitations of formal mathematical systems, transforming the foundations of mathematics and philosophy.",
  [(1931, "Published the incompleteness theorems"), (1940, "Proved the consistency of the continuum hypothesis"), (1949, "Discovered rotating universe solutions in general relativity")],
  [("On Formally Undecidable Propositions", 1931, "Paper proving the incompleteness of consistent formal systems")],
  [("Either mathematics is too big for the human mind or the human mind is more than a machine.", "Attributed")])

p("alexander-grothendieck", "Alexander Grothendieck", "アレクサンドル・グロタンディーク", 1928, 2014, ["de", "fr"], ["mathematics"],
  "Alexander Grothendieck was a German-born French mathematician who revolutionized algebraic geometry. He is considered one of the greatest mathematicians of the 20th century.",
  "Grothendieck was born in Berlin. He was a stateless refugee who studied in France, eventually becoming a professor at the IHÉS, where he transformed algebraic geometry.",
  "Grothendieck's reimagining of algebraic geometry through scheme theory and his work on the foundations of homological algebra were among the most profound mathematical achievements of the 20th century.",
  [(1957, "Published Tōhoku paper on homological algebra"), (1960, "Began publishing Éléments de géométrie algébrique"), (1966, "Awarded Fields Medal"), (1970, "Left IHÉS for political reasons")],
  [("Éléments de géométrie algébrique", 1960, "Massive foundational work that rebuilt algebraic geometry")],
  [("The introduction of the cipher 0 or the group concept was general nonsense too, and mathematics was more or less stagnating for thousands of years because nobody was around to take such childish steps.", "Récoltes et Semailles")])

p("henri-poincare", "Henri Poincaré", "アンリ・ポアンカレ", 1854, 1912, ["fr"], ["mathematics", "physics"],
  "Henri Poincaré was a French mathematician, theoretical physicist, engineer, and philosopher of science who is considered the last universalist in mathematics.",
  "Poincaré was born in Nancy, France. He studied at the École Polytechnique and the School of Mines, quickly establishing himself as a leading mathematician.",
  "Poincaré founded the fields of topology, chaos theory, and qualitative dynamics. His work on the three-body problem and special relativity were groundbreaking.",
  [(1881, "Published on automorphic functions"), (1889, "Won King Oscar II's prize for the three-body problem"), (1895, "Published Analysis Situs, founding algebraic topology"), (1905, "Published papers on special relativity")],
  [("Science and Hypothesis", 1902, "Influential philosophy of science book"), ("Analysis Situs", 1895, "Foundational work in algebraic topology")],
  [("It is by logic that we prove, but by intuition that we discover.", "Science and Method")])

p("andrew-wiles", "Andrew Wiles", "アンドリュー・ワイルズ", 1953, None, ["gb"], ["mathematics"],
  "Andrew Wiles is a British mathematician who proved Fermat's Last Theorem, solving one of the most famous problems in the history of mathematics.",
  "Wiles was born in Cambridge, England. He became fascinated by Fermat's Last Theorem as a child and dedicated years of secret work to proving it.",
  "Wiles's proof of Fermat's Last Theorem resolved a 358-year-old problem and established deep connections between number theory and algebraic geometry.",
  [(1986, "Began secret work on Fermat's Last Theorem"), (1993, "Announced proof of Fermat's Last Theorem"), (1995, "Published corrected proof"), (2016, "Awarded Abel Prize")],
  [("Modular Elliptic Curves and Fermat's Last Theorem", 1995, "Paper proving the 358-year-old conjecture")],
  [("I had this very rare privilege of being able to pursue in my adult life what had been my childhood dream.", "Attributed")])

p("georg-cantor", "Georg Cantor", "ゲオルク・カントール", 1845, 1918, ["de", "ru"], ["mathematics"],
  "Georg Cantor was a German mathematician who created set theory and introduced the concept of infinite numbers, fundamentally changing mathematics.",
  "Cantor was born in Saint Petersburg, Russia, and grew up in Germany. He studied at the University of Berlin under Weierstrass and Kronecker.",
  "Cantor's set theory provided the foundation for virtually all of modern mathematics. His work on different sizes of infinity was revolutionary though controversial in his time.",
  [(1874, "Published first set theory paper"), (1878, "Proved the countability of rational numbers"), (1891, "Proved the uncountability of real numbers via diagonalization")],
  [("Contributions to the Founding of the Theory of Transfinite Numbers", 1895, "Foundational work on set theory and transfinite arithmetic")],
  [("The essence of mathematics lies in its freedom.", "Attributed")])

p("john-nash", "John Nash", "ジョン・ナッシュ", 1928, 2015, ["us"], ["mathematics"],
  "John Nash was an American mathematician who made fundamental contributions to game theory, differential geometry, and partial differential equations.",
  "Nash was born in Bluefield, West Virginia. He studied at Carnegie Tech and Princeton, where he developed the Nash equilibrium concept at age 21.",
  "Nash's equilibrium concept transformed economics and social science. His life story, including his struggle with schizophrenia, was depicted in A Beautiful Mind.",
  [(1950, "Developed Nash equilibrium"), (1958, "Began suffering from schizophrenia"), (1994, "Awarded Nobel Prize in Economics"), (2015, "Awarded Abel Prize")],
  [("Non-Cooperative Games", 1950, "Doctoral thesis introducing the Nash equilibrium")],
  [("People are always selling the idea that people with mental illness are suffering. I think madness can be an escape.", "Attributed")])

# === MORE PHILOSOPHERS ===
p("hannah-arendt", "Hannah Arendt", "ハンナ・アーレント", 1906, 1975, ["de", "us"], ["philosophy", "politics"],
  "Hannah Arendt was a German-American political theorist whose work on totalitarianism, the nature of power, and the banality of evil has profoundly influenced political thought.",
  "Arendt was born in Hanover, Germany. She studied under Heidegger and Jaspers, fled Nazi Germany, and eventually settled in the United States.",
  "Arendt's analysis of totalitarianism and her concept of the 'banality of evil' transformed understanding of political violence and moral responsibility.",
  [(1951, "Published The Origins of Totalitarianism"), (1958, "Published The Human Condition"), (1961, "Covered Eichmann trial for The New Yorker"), (1963, "Published Eichmann in Jerusalem")],
  [("The Origins of Totalitarianism", 1951, "Analysis of Nazism and Stalinism as forms of totalitarianism"), ("Eichmann in Jerusalem", 1963, "Report introducing the concept of the banality of evil")],
  [("The sad truth is that most evil is done by people who never make up their minds to be good or evil.", "The Life of the Mind")])

p("simone-de-beauvoir", "Simone de Beauvoir", "シモーヌ・ド・ボーヴォワール", 1908, 1986, ["fr"], ["philosophy"],
  "Simone de Beauvoir was a French existentialist philosopher, writer, and feminist activist whose work The Second Sex became a foundational text of modern feminism.",
  "De Beauvoir was born in Paris. She studied philosophy at the Sorbonne, where she met Jean-Paul Sartre, beginning a lifelong intellectual and personal partnership.",
  "De Beauvoir's The Second Sex analyzed the oppression of women and argued that gender is socially constructed. Her work launched second-wave feminism.",
  [(1943, "Published She Came to Stay"), (1949, "Published The Second Sex"), (1954, "Won Prix Goncourt for The Mandarins")],
  [("The Second Sex", 1949, "Foundational feminist text analyzing the construction of womanhood"), ("The Mandarins", 1954, "Novel about post-war French intellectuals")],
  [("One is not born, but rather becomes, a woman.", "The Second Sex")])

p("michel-foucault", "Michel Foucault", "ミシェル・フーコー", 1926, 1984, ["fr"], ["philosophy"],
  "Michel Foucault was a French philosopher whose theories about the relationship between power and knowledge, and his studies of social institutions, have been widely influential.",
  "Foucault was born in Poitiers, France. He studied at the École Normale Supérieure and taught at several universities, including the Collège de France.",
  "Foucault's analyses of power, knowledge, discourse, and institutions transformed the humanities and social sciences, influencing fields from history to literary criticism.",
  [(1961, "Published Madness and Civilization"), (1966, "Published The Order of Things"), (1975, "Published Discipline and Punish"), (1976, "Began The History of Sexuality")],
  [("Discipline and Punish", 1975, "Analysis of the modern prison system and surveillance"), ("The History of Sexuality", 1976, "Multi-volume study of how sexuality is socially constructed")],
  [("Where there is power, there is resistance.", "The History of Sexuality")])

p("jacques-derrida", "Jacques Derrida", "ジャック・デリダ", 1930, 2004, ["fr", "dz"], ["philosophy"],
  "Jacques Derrida was a French philosopher who developed the critical method known as deconstruction, profoundly influencing literary criticism, philosophy, and the humanities.",
  "Derrida was born in El Biar, French Algeria. He studied at the École Normale Supérieure in Paris and taught at several French and American universities.",
  "Derrida's deconstruction revealed hidden assumptions and contradictions in philosophical and literary texts, transforming how we understand language, meaning, and interpretation.",
  [(1967, "Published Of Grammatology, Writing and Difference, and Speech and Phenomena"), (1972, "Published Margins of Philosophy"), (1994, "Published Specters of Marx")],
  [("Of Grammatology", 1967, "Foundational text of deconstruction"), ("Writing and Difference", 1967, "Essays developing deconstructive method")],
  [("There is nothing outside of the text.", "Of Grammatology")])

p("noam-chomsky", "Noam Chomsky", "ノーム・チョムスキー", 1928, None, ["us"], ["philosophy", "politics"],
  "Noam Chomsky is an American linguist, philosopher, and political activist who revolutionized the scientific study of language and became a leading critic of U.S. foreign policy.",
  "Chomsky was born in Philadelphia. He studied at the University of Pennsylvania and has spent his academic career at MIT, where he transformed linguistics.",
  "Chomsky's theory of generative grammar revolutionized linguistics and cognitive science. His political writings have made him one of the most cited living scholars.",
  [(1957, "Published Syntactic Structures"), (1965, "Published Aspects of the Theory of Syntax"), (1967, "Published anti-Vietnam War essay"), (1988, "Published Manufacturing Consent")],
  [("Syntactic Structures", 1957, "Book that launched the cognitive revolution in linguistics"), ("Manufacturing Consent", 1988, "Analysis of media propaganda")],
  [("If we don't believe in freedom of expression for people we despise, we don't believe in it at all.", "Attributed")])

# === MORE WRITERS ===
p("james-joyce", "James Joyce", "ジェイムズ・ジョイス", 1882, 1941, ["ie"], ["literature"],
  "James Joyce was an Irish novelist, short story writer, and poet, considered one of the most influential and important writers of the 20th century.",
  "Joyce was born in Dublin, Ireland. He studied at University College Dublin and spent most of his adult life abroad in Trieste, Paris, and Zurich.",
  "Joyce's novels, particularly Ulysses and Finnegans Wake, revolutionized the modern novel through stream of consciousness and linguistic experimentation.",
  [(1904, "Left Ireland permanently"), (1914, "Published Dubliners"), (1922, "Published Ulysses"), (1939, "Published Finnegans Wake")],
  [("Ulysses", 1922, "Modernist novel following one day in Dublin"), ("Dubliners", 1914, "Collection of short stories depicting Irish middle-class life")],
  [("A man of genius makes no mistakes; his errors are volitional and are the portals of discovery.", "Ulysses")])

p("franz-kafka", "Franz Kafka", "フランツ・カフカ", 1883, 1924, ["cz", "at"], ["literature"],
  "Franz Kafka was a German-speaking Bohemian novelist and short-story writer whose surreal and existential works have made 'Kafkaesque' a universal term.",
  "Kafka was born in Prague into a German-speaking Jewish family. He studied law and worked in insurance while writing his major works, mostly published posthumously.",
  "Kafka's nightmarish depictions of bureaucracy, alienation, and existential anxiety anticipated the horrors of the 20th century and created a new literary genre.",
  [(1912, "Wrote The Judgment and The Metamorphosis"), (1914, "Began The Trial"), (1922, "Wrote The Castle"), (1924, "Died of tuberculosis; friend Max Brod preserved his works")],
  [("The Metamorphosis", 1915, "Novella about a man who wakes up transformed into a giant insect"), ("The Trial", 1925, "Novel about a man arrested for an unspecified crime")],
  [("A book must be the axe for the frozen sea within us.", "Letter, 1904")])

p("virginia-woolf", "Virginia Woolf", "ヴァージニア・ウルフ", 1882, 1941, ["gb"], ["literature"],
  "Virginia Woolf was a British writer and modernist who pioneered the use of stream of consciousness as a narrative device.",
  "Woolf was born in London into an intellectual family. She was largely self-educated through her father's library and became central to the Bloomsbury Group.",
  "Woolf's innovative narrative techniques and her feminist essays transformed the novel and literary criticism. Mrs Dalloway and To the Lighthouse are modernist masterpieces.",
  [(1915, "Published The Voyage Out"), (1925, "Published Mrs Dalloway"), (1927, "Published To the Lighthouse"), (1929, "Published A Room of One's Own")],
  [("Mrs Dalloway", 1925, "Modernist novel following one day in London"), ("A Room of One's Own", 1929, "Extended essay on women and fiction")],
  [("A woman must have money and a room of her own if she is to write fiction.", "A Room of One's Own")])

p("gabriel-garcia-marquez", "Gabriel García Márquez", "ガブリエル・ガルシア＝マルケス", 1927, 2014, ["co"], ["literature"],
  "Gabriel García Márquez was a Colombian novelist and journalist who popularized magical realism and won the Nobel Prize in Literature.",
  "García Márquez was born in Aracataca, Colombia. He studied law and journalism before devoting himself to writing fiction and journalism.",
  "García Márquez's One Hundred Years of Solitude is one of the most translated and read novels in the world, establishing magical realism as a major literary genre.",
  [(1955, "Published Leaf Storm"), (1967, "Published One Hundred Years of Solitude"), (1982, "Awarded Nobel Prize in Literature"), (1985, "Published Love in the Time of Cholera")],
  [("One Hundred Years of Solitude", 1967, "Epic novel of the Buendía family spanning seven generations"), ("Love in the Time of Cholera", 1985, "Novel about enduring love")],
  [("It is not true that people stop pursuing dreams because they grow old, they grow old because they stop pursuing dreams.", "Attributed")])

p("haruki-murakami", "Haruki Murakami", "村上春樹", 1949, None, ["jp"], ["literature"],
  "Haruki Murakami is a Japanese novelist whose surreal and melancholic fiction has made him one of the world's most popular and influential contemporary writers.",
  "Murakami was born in Kyoto and grew up in Kobe. He ran a jazz bar before becoming a full-time writer, influenced by American literature and jazz music.",
  "Murakami's blend of Western and Japanese literary traditions, his dreamlike narratives, and his exploration of loneliness have resonated with readers worldwide.",
  [(1979, "Published Hear the Wind Sing"), (1987, "Published Norwegian Wood"), (1994, "Published The Wind-Up Bird Chronicle"), (2009, "Published 1Q84")],
  [("Norwegian Wood", 1987, "Coming-of-age novel that sold millions in Japan"), ("Kafka on the Shore", 2002, "Surreal novel interweaving two narratives")],
  [("If you only read the books that everyone else is reading, you can only think what everyone else is thinking.", "Norwegian Wood")])

p("toni-morrison", "Toni Morrison", "トニ・モリスン", 1931, 2019, ["us"], ["literature"],
  "Toni Morrison was an American novelist who won the Nobel Prize in Literature for novels that gave life to the African American experience.",
  "Morrison was born Chloe Wofford in Lorain, Ohio. She studied at Howard University and Cornell before working as an editor and professor while writing her novels.",
  "Morrison's novels explored the Black experience in America with lyrical prose and unflinching honesty, becoming essential works of American and world literature.",
  [(1970, "Published The Bluest Eye"), (1977, "Published Song of Solomon"), (1987, "Published Beloved"), (1993, "Awarded Nobel Prize in Literature")],
  [("Beloved", 1987, "Novel about the legacy of slavery, inspired by the story of Margaret Garner"), ("Song of Solomon", 1977, "Novel about an African American man's search for identity")],
  [("If there's a book that you want to read, but it hasn't been written yet, then you must write it.", "Attributed")])

p("jorge-luis-borges", "Jorge Luis Borges", "ホルヘ・ルイス・ボルヘス", 1899, 1986, ["ar"], ["literature"],
  "Jorge Luis Borges was an Argentine short-story writer, essayist, and poet who is considered one of the most important literary figures of the 20th century.",
  "Borges was born in Buenos Aires. He grew up bilingual in Spanish and English, studied in Europe, and returned to Argentina to work as a librarian and professor.",
  "Borges's labyrinthine fictions exploring infinity, time, identity, and reality influenced postmodern literature and anticipated hypertext and virtual reality.",
  [(1941, "Published The Garden of Forking Paths"), (1944, "Published Ficciones"), (1949, "Published The Aleph"), (1961, "Shared the International Publishers' Prize with Beckett")],
  [("Ficciones", 1944, "Collection of short stories including The Library of Babel"), ("The Aleph", 1949, "Collection including the famous story of the same name")],
  [("I have always imagined that Paradise will be a kind of library.", "Attributed")])

p("natsume-soseki", "Natsume Sōseki", "夏目漱石", 1867, 1916, ["jp"], ["literature"],
  "Natsume Sōseki was a Japanese novelist who is widely regarded as the greatest writer in modern Japanese literature.",
  "Sōseki was born in Tokyo during the Meiji era. He studied English literature in London, an experience that deeply influenced his view of Japan's modernization.",
  "Sōseki's novels explored the tensions between traditional Japanese culture and Western modernity, establishing the modern Japanese novel as a literary form.",
  [(1905, "Published I Am a Cat"), (1906, "Published Botchan"), (1914, "Published Kokoro"), (1916, "Died while writing Light and Darkness")],
  [("Kokoro", 1914, "Novel exploring loneliness, guilt, and the clash between tradition and modernity"), ("I Am a Cat", 1905, "Satirical novel narrated by a cat observing human foibles")],
  [("You think you can trust others. I tell you, the only one you can trust is yourself.", "Kokoro")])

# === MORE POLITICAL LEADERS ===
p("frederick-douglass", "Frederick Douglass", "フレデリック・ダグラス", 1818, 1895, ["us"], ["politics"],
  "Frederick Douglass was an American social reformer, abolitionist, orator, writer, and statesman who became the most prominent spokesperson for abolition.",
  "Douglass was born into slavery in Maryland. He escaped in 1838 and became a powerful orator and writer for the abolitionist cause.",
  "Douglass's eloquent advocacy for abolition and equal rights helped end slavery and advance civil rights. His autobiographies are classics of American literature.",
  [(1838, "Escaped from slavery"), (1845, "Published Narrative of the Life of Frederick Douglass"), (1847, "Founded The North Star newspaper"), (1872, "Nominated as vice president on Equal Rights Party ticket")],
  [("Narrative of the Life of Frederick Douglass", 1845, "Autobiography that became a bestseller and powerful abolitionist tool")],
  [("If there is no struggle, there is no progress.", "Speech, 1857")])

p("harriet-tubman", "Harriet Tubman", "ハリエット・タブマン", 1822, 1913, ["us"], ["politics"],
  "Harriet Tubman was an American abolitionist who escaped from slavery and made thirteen missions to rescue approximately seventy enslaved people using the Underground Railroad.",
  "Tubman was born Araminta Ross in Dorchester County, Maryland. She suffered a traumatic head injury as a child and escaped slavery in 1849.",
  "Tubman's daring rescues through the Underground Railroad made her a legend of American freedom. She also served as a scout and spy for the Union Army during the Civil War.",
  [(1849, "Escaped from slavery"), (1850, "Began Underground Railroad missions"), (1863, "Led Combahee River Raid during Civil War"), (1869, "Published autobiography")],
  [("Underground Railroad Rescues", 1850, "Thirteen missions rescuing approximately seventy enslaved people")],
  [("I freed a thousand slaves. I could have freed a thousand more if only they knew they were slaves.", "Attributed")])

p("emmeline-pankhurst", "Emmeline Pankhurst", "エメリン・パンクハースト", 1858, 1928, ["gb"], ["politics"],
  "Emmeline Pankhurst was a British political activist who organized the suffragette movement and helped women win the right to vote.",
  "Pankhurst was born in Manchester, England. She became involved in women's suffrage and in 1903 founded the Women's Social and Political Union.",
  "Pankhurst's militant suffragette campaign, including hunger strikes and civil disobedience, was instrumental in winning women the right to vote in Britain.",
  [(1903, "Founded the Women's Social and Political Union"), (1908, "Led march on Parliament"), (1913, "Imprisoned and went on hunger strike"), (1928, "Women's suffrage achieved; died the same year")],
  [("My Own Story", 1914, "Autobiography of her struggle for women's suffrage")],
  [("Deeds, not words.", "Motto of the WSPU")])

p("toussaint-louverture", "Toussaint Louverture", "トゥーサン・ルーヴェルチュール", 1743, 1803, ["ht"], ["politics"],
  "Toussaint Louverture was the leader of the Haitian Revolution, the most successful slave revolt in history, which established Haiti as the first free Black republic.",
  "Louverture was born into slavery in Saint-Domingue. Self-educated, he became a skilled horseman and healer before emerging as the leader of the slave uprising.",
  "Louverture's leadership of the Haitian Revolution demonstrated that enslaved people could achieve their own liberation, inspiring abolition movements worldwide.",
  [(1791, "Joined the Haitian slave revolt"), (1794, "Allied with France; became dominant leader"), (1801, "Issued constitution abolishing slavery"), (1803, "Died in French captivity")],
  [("Haitian Revolution", 1791, "The largest and most successful slave revolt in history")],
  [("In overthrowing me you have cut down in Saint-Domingue only the trunk of the tree of liberty; it will spring up again from the roots.", "Statement to captors, 1802")])

# === MORE ENGINEERS/SCIENTISTS ===
p("marie-curie-chemistry", "Dmitri Mendeleev's Teacher Aleksandr Butlerov", "アレクサンドル・ブートレロフ", 1828, 1886, ["ru"], ["chemistry"],
  "Aleksandr Butlerov was a Russian chemist who was one of the principal creators of the theory of chemical structure and the first to introduce the term.",
  "Butlerov was born in Chistopol, Russia. He studied at the University of Kazan, where he spent most of his career as professor of chemistry.",
  "Butlerov's theory of chemical structure explained isomerism and enabled the systematic study of organic compounds. He trained a generation of Russian chemists.",
  [(1858, "Traveled to European laboratories"), (1861, "Published theory of chemical structure"), (1864, "Published Introduction to the Full Study of Organic Chemistry")],
  [("Introduction to the Full Study of Organic Chemistry", 1864, "Comprehensive textbook presenting structural theory")],
  [("Only one chemistry exists and it is defined by the structure of substances.", "Attributed")])

p("nikola-tesla-2", "Guglielmo Marconi's contemporary Karl Ferdinand Braun", "カール・フェルディナント・ブラウン", 1850, 1918, ["de"], ["engineering", "physics"],
  "Karl Ferdinand Braun was a German physicist and inventor who shared the Nobel Prize with Marconi for contributions to wireless telegraphy and invented the cathode ray tube.",
  "Braun was born in Fulda, Germany. He studied at the University of Marburg and became professor at several German universities.",
  "Braun's invention of the cathode ray tube became the basis for television and computer monitors. His improvements to radio transmission shared the Nobel Prize with Marconi.",
  [(1874, "Discovered the semiconductor crystal rectifier"), (1897, "Invented the cathode ray tube oscilloscope"), (1899, "Improved Marconi's radio transmission system"), (1909, "Shared Nobel Prize in Physics")],
  [("Cathode Ray Tube", 1897, "Display technology that became the basis for television screens")],
  [("The cathode ray tube is a window into the invisible world of electrons.", "Attributed")])

p("rachel-carson-env", "Wangari Maathai's contemporary Chico Mendes", "シコ・メンデス", 1944, 1988, ["br"], ["politics"],
  "Chico Mendes was a Brazilian rubber tapper, trade union leader, and environmentalist who fought to preserve the Amazon rainforest.",
  "Mendes was born in Xapuri, Acre, Brazil. He grew up as a rubber tapper and became a union organizer and environmentalist.",
  "Mendes's fight to preserve the Amazon through sustainable development brought international attention to rainforest destruction. His assassination galvanized global environmental activism.",
  [(1975, "Began union organizing for rubber tappers"), (1985, "Founded the National Council of Rubber Tappers"), (1987, "Received UN Global 500 Award"), (1988, "Assassinated by ranchers")],
  [("Extractive Reserves", 1985, "Concept for sustainable use of rainforest by traditional communities")],
  [("At first I thought I was fighting to save rubber trees, then I thought I was fighting to save the Amazon rainforest. Now I realize I am fighting for humanity.", "Attributed")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'alan-turing-math':
            entry['id'] = 'alonzo-church'
        elif entry['id'] == 'marie-curie-chemistry':
            entry['id'] = 'aleksandr-butlerov'
        elif entry['id'] == 'nikola-tesla-2':
            entry['id'] = 'karl-ferdinand-braun'
        elif entry['id'] == 'rachel-carson-env':
            entry['id'] = 'chico-mendes'
    write_people(P)
