#!/usr/bin/env python3
"""Supplement batch 10: more people with dedup."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
PEOPLE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'people')
existing = {f.replace('.json', '') for f in os.listdir(PEOPLE_DIR) if f.endswith('.json')} if os.path.exists(PEOPLE_DIR) else set()
def add(id, *a, **k):
    if id not in existing:
        P.append(person(id, *a, **k))

# ── 19th-20th CENTURY WRITERS (~20) ──────────────────────────────────────────

add("cesar-vallejo", "César Vallejo", "セサル・バジェホ", 1892, 1938, ["pe"], ["literature"],
  "César Vallejo was a Peruvian poet regarded as one of the great poetic innovators of the 20th century.",
  "Born in Santiago de Chuco, Peru, the youngest of eleven children in a mestizo family.",
  "Vallejo's radical experimentation with language and form profoundly influenced Latin American and world poetry.",
  [(1919, "Published Los heraldos negros"), (1922, "Published Trilce, a groundbreaking avant-garde collection"), (1938, "Died in Paris")],
  [("Trilce", 1922, "Radically experimental poetry collection that broke with all existing conventions"), ("Los heraldos negros", 1919, "First poetry collection blending modernism with indigenous Andean themes")],
  [("I will die in Paris, on a rainy day, on some day I can already remember.", "Piedra negra sobre una piedra blanca")])

add("jose-marti", "José Martí", "ホセ・マルティ", 1853, 1895, ["cu"], ["literature", "politics"],
  "José Martí was a Cuban poet, essayist, and revolutionary leader who became a symbol of Cuba's struggle for independence from Spain.",
  "Born in Havana to Spanish immigrant parents. Imprisoned at age 16 for his political writings.",
  "Martí is considered the apostle of Cuban independence and a foundational figure in Latin American literature.",
  [(1869, "Imprisoned for supporting Cuban independence"), (1891, "Published Versos sencillos"), (1895, "Killed at the Battle of Dos Ríos")],
  [("Versos sencillos", 1891, "Collection of simple yet profound poems, source of the lyrics to Guantanamera"), ("Nuestra América", 1891, "Influential essay on Latin American identity")],
  [("Cultures are to be judged not by their fruits but by their roots.", "Attributed")])

add("ruben-dario", "Rubén Darío", "ルベン・ダリオ", 1867, 1916, ["ni"], ["literature"],
  "Rubén Darío was a Nicaraguan poet who founded the Spanish-language literary movement known as modernismo.",
  "Born Félix Rubén García Sarmiento in Metapa, Nicaragua. A child prodigy, he was known as the 'boy poet' by age 13.",
  "Darío revolutionized Spanish-language poetry, influencing virtually every major Spanish-language poet who followed.",
  [(1888, "Published Azul, launching the modernismo movement"), (1896, "Published Prosas profanas"), (1905, "Published Cantos de vida y esperanza")],
  [("Azul", 1888, "Collection that inaugurated the modernismo literary movement"), ("Cantos de vida y esperanza", 1905, "Mature masterwork blending personal and political themes")],
  [("If the homeland is small, one dreams it large.", "Attributed")])

add("mikhail-lermontov", "Mikhail Lermontov", "ミハイル・レールモントフ", 1814, 1841, ["ru"], ["literature"],
  "Mikhail Lermontov was a major Russian Romantic poet and novelist, often considered the successor to Pushkin.",
  "Born in Moscow to an aristocratic family. Raised by his wealthy grandmother after his mother's early death.",
  "Lermontov's A Hero of Our Time is considered the first Russian psychological novel and influenced Dostoevsky and Tolstoy.",
  [(1837, "Wrote Death of a Poet, a protest against Pushkin's death in a duel"), (1840, "Published A Hero of Our Time"), (1841, "Killed in a duel at age 26")],
  [("A Hero of Our Time", 1840, "Pioneering psychological novel featuring the disillusioned Pechorin"), ("Death of a Poet", 1837, "Poem mourning Pushkin that brought Lermontov fame and exile")],
  [("I was ready to love the whole world, but no one understood me, and I learned to hate.", "A Hero of Our Time")])

add("ivan-turgenev", "Ivan Turgenev", "イワン・ツルゲーネフ", 1818, 1883, ["ru"], ["literature"],
  "Ivan Turgenev was a Russian novelist and playwright whose works vividly portrayed Russian society and the conflicts between generations.",
  "Born in Oryol, Russia, to a wealthy landowning family. Studied in Moscow, St. Petersburg, and Berlin.",
  "Turgenev's Fathers and Sons defined the concept of nihilism for a generation and helped bring Russian literature to Western audiences.",
  [(1852, "Published A Sportsman's Sketches, contributing to the abolition of serfdom"), (1862, "Published Fathers and Sons"), (1883, "Died in Bougival, France")],
  [("Fathers and Sons", 1862, "Novel exploring the generational conflict between liberal idealists and young nihilists"), ("A Sportsman's Sketches", 1852, "Short story collection depicting the lives of serfs")],
  [("Nature is not a temple, but a workshop, and man is the workman in it.", "Fathers and Sons")])

add("nikolai-gogol", "Nikolai Gogol", "ニコライ・ゴーゴリ", 1809, 1852, ["ru", "ua"], ["literature"],
  "Nikolai Gogol was a Russian-Ukrainian writer whose satirical works founded the tradition of Russian realism.",
  "Born in Sorochyntsi, Poltava Governorate (modern Ukraine). Moved to St. Petersburg in 1828 to pursue a literary career.",
  "Gogol's grotesque satire and psychological depth profoundly influenced Dostoevsky, Bulgakov, and the entire Russian literary tradition.",
  [(1836, "Premiered The Government Inspector in St. Petersburg"), (1842, "Published Dead Souls"), (1852, "Burned the manuscript of Dead Souls Part 2 and died shortly after")],
  [("Dead Souls", 1842, "Satirical novel about a con man buying deceased serfs for tax fraud"), ("The Overcoat", 1842, "Short story considered a masterpiece of Russian literature"), ("The Government Inspector", 1836, "Satirical play mocking provincial corruption")],
  [("It is no use to blame the looking glass if your face is awry.", "The Government Inspector")])

add("maxim-gorky", "Maxim Gorky", "マクシム・ゴーリキー", 1868, 1936, ["ru"], ["literature"],
  "Maxim Gorky was a Russian author and political activist who became the founder of Soviet socialist realism.",
  "Born Alexei Maximovich Peshkov in Nizhny Novgorod. Orphaned early, he was largely self-educated through voracious reading.",
  "Gorky's depictions of the lower classes and his political activism made him a towering figure in both Russian literature and revolutionary politics.",
  [(1898, "Published his first short story collection, gaining wide acclaim"), (1906, "Published The Mother, a key text of socialist realism"), (1934, "Presided over the First Congress of Soviet Writers")],
  [("The Mother", 1906, "Novel about a working-class woman drawn into revolutionary politics"), ("The Lower Depths", 1902, "Play depicting life among the destitute in a flophouse")],
  [("You must write for children the same way you write for adults, only better.", "Attributed")])

add("boris-pasternak", "Boris Pasternak", "ボリス・パステルナーク", 1890, 1960, ["ru"], ["literature"],
  "Boris Pasternak was a Russian poet and novelist best known for Doctor Zhivago, for which he was awarded the Nobel Prize in Literature.",
  "Born in Moscow to a prominent artistic family; his father was a painter and his mother a concert pianist.",
  "Doctor Zhivago became a symbol of artistic freedom during the Cold War, and Pasternak's poetry is considered among the finest in the Russian language.",
  [(1957, "Doctor Zhivago published in Italy after being rejected in the USSR"), (1958, "Awarded Nobel Prize in Literature; forced by Soviet authorities to decline it")],
  [("Doctor Zhivago", 1957, "Epic novel of love and revolution during the Russian Civil War"), ("My Sister, Life", 1922, "Poetry collection considered a masterpiece of Russian verse")],
  [("What is laid down, ordered, factual is never enough to embrace the whole truth.", "Doctor Zhivago")])

add("anna-akhmatova", "Anna Akhmatova", "アンナ・アフマートヴァ", 1889, 1966, ["ru"], ["literature"],
  "Anna Akhmatova was one of the most significant Russian poets of the 20th century, whose work bore witness to the Stalinist terror.",
  "Born Anna Gorenko near Odessa. Began writing poetry at age 11 and adopted her Tatar grandmother's surname as a pen name.",
  "Akhmatova's Requiem stands as one of the great literary testimonies against political oppression.",
  [(1912, "Published her first collection, Evening"), (1935, "Began writing Requiem after her son's arrest"), (1965, "Awarded honorary doctorate from Oxford")],
  [("Requiem", 1963, "Poem cycle mourning the victims of Stalinist repression"), ("Poem Without a Hero", 1965, "Complex long poem reflecting on pre-revolutionary St. Petersburg")],
  [("I am your voice, the warmth of your breath, I am the reflection of your face.", "Requiem")])

add("marina-tsvetaeva", "Marina Tsvetaeva", "マリーナ・ツヴェターエワ", 1892, 1941, ["ru"], ["literature"],
  "Marina Tsvetaeva was a Russian poet of immense originality and emotional intensity, now regarded as one of the greatest poets of the 20th century.",
  "Born in Moscow to a professor father and a pianist mother. Began writing poetry in childhood and published her first collection at 18.",
  "Tsvetaeva's innovative rhythms, syntax, and emotional rawness expanded the possibilities of Russian poetry.",
  [(1910, "Published her first poetry collection, Evening Album"), (1922, "Emigrated from Soviet Russia"), (1941, "Returned to the USSR and died by suicide in Yelabuga")],
  [("Evening Album", 1910, "Debut poetry collection praised by leading poets"), ("The Ratcatcher", 1925, "Satirical narrative poem based on the Pied Piper legend")],
  [("I bow to all who have survived. I bow to all who are surviving.", "Attributed")])

add("mikhail-bulgakov", "Mikhail Bulgakov", "ミハイル・ブルガーコフ", 1891, 1940, ["ru"], ["literature"],
  "Mikhail Bulgakov was a Russian novelist and playwright best known for The Master and Margarita, a masterpiece of magical realism and satire.",
  "Born in Kyiv into a well-educated family. Trained as a physician before turning to writing full-time.",
  "The Master and Margarita became one of the most celebrated novels of the 20th century, blending supernatural fantasy with biting satire of Soviet society.",
  [(1925, "Published The White Guard"), (1928, "Began writing The Master and Margarita"), (1940, "Died of kidney disease; The Master and Margarita published posthumously in 1966")],
  [("The Master and Margarita", 1967, "Satirical novel about the Devil visiting Soviet Moscow"), ("The White Guard", 1925, "Novel about a family during the Russian Civil War"), ("Heart of a Dog", 1925, "Satirical novella about a dog surgically transformed into a human")],
  [("Manuscripts don't burn.", "The Master and Margarita")])

add("isaac-babel", "Isaac Babel", "イサーク・バーベリ", 1894, 1940, ["ru"], ["literature"],
  "Isaac Babel was a Russian short story writer and journalist known for his vivid, compressed prose about war and Jewish life.",
  "Born in Odessa to a Jewish merchant family. Witnessed pogroms as a child and later rode with Cossack cavalry in the Polish-Soviet War.",
  "Babel's Red Cavalry stories are considered among the finest short fiction of the 20th century, combining brutal violence with lyrical beauty.",
  [(1924, "Published Red Cavalry stories"), (1926, "Published Odessa Tales"), (1940, "Executed during the Great Purge")],
  [("Red Cavalry", 1926, "Short story cycle based on his experiences in the Polish-Soviet War"), ("Odessa Tales", 1931, "Stories about the Jewish gangster Benya Krik")],
  [("No iron can stab the heart with such force as a period put just at the right place.", "Attributed")])

add("osip-mandelstam", "Osip Mandelstam", "オシップ・マンデリシュターム", 1891, 1938, ["ru"], ["literature"],
  "Osip Mandelstam was a Russian poet and essayist, a leading figure of the Acmeist movement, who perished in a Soviet transit camp.",
  "Born in Warsaw to a Jewish family. Grew up in St. Petersburg and studied at the Sorbonne and Heidelberg.",
  "Mandelstam's precise, image-laden poetry and his martyrdom under Stalinism made him a symbol of artistic courage against tyranny.",
  [(1913, "Published his first collection, Stone"), (1934, "Arrested for his epigram mocking Stalin"), (1938, "Died in a transit camp near Vladivostok")],
  [("Stone", 1913, "Debut poetry collection of the Acmeist movement"), ("Tristia", 1922, "Second major poetry collection")],
  [("Poetry is the ploughman's hand that turns up time so that its deep layers, its black earth, appear on top.", "Conversation about Dante")])

add("mikhail-sholokhov", "Mikhail Sholokhov", "ミハイル・ショーロホフ", 1905, 1984, ["ru"], ["literature"],
  "Mikhail Sholokhov was a Russian novelist who won the Nobel Prize in Literature for his epic novels about Don Cossack life.",
  "Born in the Don Cossack region. Participated in the Russian Civil War as a teenager.",
  "And Quiet Flows the Don is one of the longest novels in the Russian language and a sweeping chronicle of Cossack life through revolution and war.",
  [(1928, "Began publishing And Quiet Flows the Don"), (1965, "Awarded Nobel Prize in Literature")],
  [("And Quiet Flows the Don", 1940, "Epic four-volume novel of Cossack life during World War I and the Civil War"), ("Virgin Soil Upturned", 1932, "Novel about collectivization in a Cossack village")],
  [("And here I am, at the crossroads, between two roads.", "And Quiet Flows the Don")])

add("aleksandr-blok", "Alexander Blok", "アレクサンドル・ブローク", 1880, 1921, ["ru"], ["literature"],
  "Alexander Blok was a leading Russian Symbolist poet whose work captured the mysticism and upheaval of early 20th-century Russia.",
  "Born in St. Petersburg into an intellectual family. Studied at St. Petersburg University.",
  "Blok's poem The Twelve, depicting twelve Red Army soldiers marching through revolutionary Petrograd, became one of the most debated works of Russian literature.",
  [(1904, "Published Verses About the Beautiful Lady"), (1918, "Published The Twelve"), (1921, "Died in Petrograd at age 40")],
  [("The Twelve", 1918, "Controversial poem blending revolutionary fervor with Christian imagery"), ("Verses About the Beautiful Lady", 1904, "Debut collection of Symbolist love poetry")],
  [("Night, street, lamp, drugstore, a dull and meaningless light.", "Night, Street, Lamp, Drugstore")])

add("yevgeny-zamyatin", "Yevgeny Zamyatin", "エヴゲニー・ザミャーチン", 1884, 1937, ["ru"], ["literature"],
  "Yevgeny Zamyatin was a Russian author best known for We, a pioneering dystopian novel that influenced Orwell's 1984 and Huxley's Brave New World.",
  "Born in Lebedyan, Russia. Trained as a naval engineer and participated in the 1905 Revolution.",
  "Zamyatin's We is considered the grandfather of dystopian fiction, directly inspiring both Aldous Huxley and George Orwell.",
  [(1921, "Completed the novel We, banned in the Soviet Union"), (1931, "Emigrated to Paris with Stalin's personal permission")],
  [("We", 1924, "Dystopian novel about a totalitarian glass city, first published in English translation")],
  [("The only means of ridding man of crime is ridding him of freedom.", "We")])

add("andrei-platonov", "Andrei Platonov", "アンドレイ・プラトーノフ", 1899, 1951, ["ru"], ["literature"],
  "Andrei Platonov was a Russian writer whose deeply original prose explored the contradictions of Soviet utopianism.",
  "Born in Voronezh to a railway worker's family. Worked as an engineer and land reclamation specialist.",
  "Platonov's novels, suppressed during his lifetime, are now considered among the most important works of 20th-century Russian literature.",
  [(1930, "Completed The Foundation Pit, suppressed by Soviet censors"), (1929, "Published Chevengur"), (1951, "Died of tuberculosis in Moscow")],
  [("The Foundation Pit", 1930, "Satirical novella about workers digging the foundation for a utopian building"), ("Chevengur", 1929, "Novel about a group of revolutionaries attempting to build communism in a provincial town")],
  [("Without me the people are incomplete.", "Chevengur")])

add("ivan-bunin", "Ivan Bunin", "イワン・ブーニン", 1870, 1953, ["ru"], ["literature"],
  "Ivan Bunin was the first Russian writer to win the Nobel Prize in Literature, known for his precise prose about the decline of the Russian gentry.",
  "Born in Voronezh into an impoverished noble family. Largely self-educated after leaving school early.",
  "Bunin's lyrical prose style and unflinching portrayal of desire and death influenced generations of Russian writers.",
  [(1920, "Emigrated to France after the Russian Revolution"), (1933, "Awarded Nobel Prize in Literature")],
  [("The Gentleman from San Francisco", 1915, "Short story about mortality and the emptiness of wealth"), ("Dark Avenues", 1943, "Collection of love stories written in exile")],
  [("Man is only happy in the expectation of happiness.", "Attributed")])

add("velimir-khlebnikov", "Velimir Khlebnikov", "ヴェリミール・フレーブニコフ", 1885, 1922, ["ru"], ["literature"],
  "Velimir Khlebnikov was a Russian poet and a founder of the Futurist movement, known for his radical linguistic experimentation.",
  "Born in Astrakhan. Studied mathematics and biology at Kazan University before devoting himself to poetry.",
  "Khlebnikov's invention of zaum (transrational language) and his mathematical approach to history made him one of the most innovative poets of the avant-garde.",
  [(1912, "Co-authored the Futurist manifesto A Slap in the Face of Public Taste"), (1922, "Died of malnutrition and illness at age 36")],
  [("A Slap in the Face of Public Taste", 1912, "Futurist manifesto calling for the overthrow of literary tradition"), ("Zangezi", 1922, "Experimental 'supersaga' combining poetry and mathematics")],
  [("We are the new people of a new life.", "A Slap in the Face of Public Taste")])

# ── 20th-21st CENTURY SCIENTISTS (~20) ───────────────────────────────────────

add("frederick-sanger", "Frederick Sanger", "フレデリック・サンガー", 1918, 2013, ["gb"], ["chemistry", "biology"],
  "Frederick Sanger was a British biochemist who won two Nobel Prizes in Chemistry for his work on protein and DNA sequencing.",
  "Born in Rendcombe, Gloucestershire. Studied at Cambridge and became a Quaker conscientious objector during WWII.",
  "Sanger's DNA sequencing method revolutionized molecular biology and made the Human Genome Project possible.",
  [(1958, "Awarded first Nobel Prize in Chemistry for sequencing insulin"), (1980, "Awarded second Nobel Prize for developing DNA sequencing methods")],
  [("Sanger sequencing method", 1977, "Chain-termination method for sequencing DNA that became the gold standard")],
  [("Scientific research is one of the most exciting and rewarding of occupations.", "Nobel Lecture")])

add("kary-mullis", "Kary Mullis", "キャリー・マリス", 1944, 2019, ["us"], ["chemistry", "biology"],
  "Kary Mullis was an American biochemist who invented the polymerase chain reaction (PCR), transforming molecular biology and forensic science.",
  "Born in Lenoir, North Carolina. Earned his PhD in biochemistry from UC Berkeley.",
  "PCR became one of the most important techniques in molecular biology, enabling DNA fingerprinting, disease diagnosis, and the Human Genome Project.",
  [(1983, "Conceived the polymerase chain reaction technique"), (1993, "Awarded Nobel Prize in Chemistry for inventing PCR")],
  [("The Unusual Origin of the Polymerase Chain Reaction", 1990, "Essay describing the invention of PCR")],
  [("I was just driving and thinking about experiments.", "On conceiving PCR")])

add("craig-venter", "Craig Venter", "クレイグ・ヴェンター", 1946, None, ["us"], ["biology"],
  "Craig Venter is an American biotechnologist who led the private effort to sequence the human genome and later created the first synthetic cell.",
  "Born in Salt Lake City. Served in the Vietnam War as a Navy medic, which inspired his interest in science.",
  "Venter's shotgun sequencing approach and creation of synthetic life opened new frontiers in genomics and synthetic biology.",
  [(2000, "Completed sequencing the human genome in competition with the public Human Genome Project"), (2010, "Created the first cell controlled by a synthetic genome")],
  [("A Life Decoded", 2007, "Autobiography describing his scientific journey"), ("The first self-replicating synthetic cell", 2010, "Landmark paper on creating synthetic life")],
  [("We are going from reading our genetic code to the ability to write it.", "TED Talk")])

add("birute-galdikas", "Biruté Galdikas", "ビルーテ・ガルディカス", 1946, None, ["ca", "lt"], ["biology"],
  "Biruté Galdikas is a Lithuanian-Canadian primatologist who is the world's foremost authority on orangutans.",
  "Born in Wiesbaden, Germany, to Lithuanian refugee parents. Grew up in Canada and studied at UCLA under Louis Leakey.",
  "Galdikas's decades-long research in Borneo has been crucial to understanding orangutan behavior and advancing their conservation.",
  [(1971, "Began field research on orangutans in Borneo"), (1986, "Published Reflections of Eden")],
  [("Reflections of Eden", 1995, "Memoir of her decades-long study of orangutans in the Borneo rainforest")],
  [("I felt I was looking into the eyes of someone who understood.", "On first encountering orangutans")])

add("harold-urey", "Harold Urey", "ハロルド・ユーリー", 1893, 1981, ["us"], ["chemistry", "physics"],
  "Harold Urey was an American physical chemist who discovered deuterium and pioneered the study of the origin of life.",
  "Born in Walkerton, Indiana. Taught in rural schools before attending university.",
  "Urey's discovery of deuterium opened new fields in isotope chemistry, and the Miller-Urey experiment became a landmark in origin-of-life research.",
  [(1931, "Discovered deuterium (heavy hydrogen)"), (1934, "Awarded Nobel Prize in Chemistry"), (1953, "Supervised the Miller-Urey experiment on the origin of life")],
  [("The discovery of deuterium", 1932, "Paper announcing the isolation of heavy hydrogen")],
  [("If God did not do it this way, He missed a good bet.", "On the Miller-Urey experiment")])

add("emilio-segre", "Emilio Segrè", "エミリオ・セグレ", 1905, 1989, ["it", "us"], ["physics"],
  "Emilio Segrè was an Italian-American physicist who discovered the antiproton and technetium, the first artificially produced element.",
  "Born in Tivoli, Italy. Studied under Enrico Fermi in Rome before emigrating to the United States.",
  "Segrè's discovery of the antiproton confirmed a major prediction of Dirac's theory and advanced the understanding of antimatter.",
  [(1937, "Co-discovered technetium, the first artificially made element"), (1955, "Co-discovered the antiproton"), (1959, "Awarded Nobel Prize in Physics with Owen Chamberlain")],
  [("Discovery of the antiproton", 1955, "Experimental confirmation of the existence of antimatter")],
  [("Physics is, hopefully, simple. Physicists are not.", "Attributed")])

add("owen-chamberlain", "Owen Chamberlain", "オーウェン・チェンバレン", 1920, 2006, ["us"], ["physics"],
  "Owen Chamberlain was an American physicist who co-discovered the antiproton with Emilio Segrè.",
  "Born in San Francisco. Worked on the Manhattan Project during World War II.",
  "The confirmation of the antiproton's existence validated Dirac's prediction and deepened understanding of fundamental particle physics.",
  [(1955, "Co-discovered the antiproton at the Bevatron"), (1959, "Awarded Nobel Prize in Physics")],
  [("Observation of Antiprotons", 1955, "Paper announcing the discovery of the antiproton")],
  [("The important thing in science is not so much to obtain new facts as to discover new ways of thinking about them.", "Attributed")])

add("val-logsdon-fitch", "Val Logsdon Fitch", "ヴァル・ログスドン・フィッチ", 1923, 2015, ["us"], ["physics"],
  "Val Fitch was an American nuclear physicist who co-discovered CP violation in kaon decay.",
  "Born in Merriman, Nebraska. Served in the Manhattan Project at Los Alamos as a young Army technician.",
  "The discovery of CP violation was crucial to understanding why the universe contains more matter than antimatter.",
  [(1964, "Co-discovered CP violation in neutral kaon decays"), (1980, "Awarded Nobel Prize in Physics with James Cronin")],
  [("Evidence for the 2π Decay of the K₂⁰ Meson", 1964, "Paper demonstrating CP symmetry violation")],
  [("The result was so unexpected that we spent months trying to find an error.", "On discovering CP violation")])

add("james-cronin", "James Cronin", "ジェームズ・クローニン", 1931, 2016, ["us"], ["physics"],
  "James Cronin was an American particle physicist who co-discovered CP violation, showing that certain physical processes are not time-reversal invariant.",
  "Born in Chicago. Studied at the University of Chicago under Samuel Allison.",
  "CP violation helped explain the matter-antimatter asymmetry of the universe and earned Cronin the Nobel Prize.",
  [(1964, "Co-discovered CP violation with Val Fitch"), (1980, "Awarded Nobel Prize in Physics")],
  [("CP Violation in K-meson decays", 1964, "Experimental demonstration that CP symmetry can be broken")],
  [("Nature had a surprise in store for us.", "Nobel Lecture")])

add("burton-richter", "Burton Richter", "バートン・リヒター", 1931, 2018, ["us"], ["physics"],
  "Burton Richter was an American physicist who co-discovered the J/psi meson, providing evidence for the charm quark.",
  "Born in Brooklyn, New York. Studied at MIT and spent his career at Stanford's SLAC.",
  "The discovery of the J/psi particle confirmed the existence of the charm quark and triggered the 'November Revolution' in particle physics.",
  [(1974, "Co-discovered the J/psi meson"), (1976, "Awarded Nobel Prize in Physics with Samuel Ting")],
  [("Discovery of the J/psi particle", 1974, "Experimental discovery confirming the existence of the charm quark")],
  [("The discovery was a pivotal moment in the history of particle physics.", "Nobel Lecture")])

add("samuel-ting", "Samuel Ting", "サミュエル・ティン", 1936, None, ["us", "cn"], ["physics"],
  "Samuel Ting is a Chinese-American physicist who co-discovered the J/psi meson, independently of Burton Richter.",
  "Born in Ann Arbor, Michigan, to Chinese academic parents. Grew up in China and Taiwan before returning to the US for graduate studies.",
  "Ting's independent discovery of the J/psi particle confirmed the charm quark and he continues to lead the Alpha Magnetic Spectrometer experiment on the ISS.",
  [(1974, "Co-discovered the J/psi meson at Brookhaven National Laboratory"), (1976, "Awarded Nobel Prize in Physics")],
  [("Discovery of the J Particle", 1974, "Paper announcing the discovery of a new heavy particle")],
  [("In experimental physics, you don't know until you measure.", "Attributed")])

add("carlo-rubbia", "Carlo Rubbia", "カルロ・ルビア", 1934, None, ["it"], ["physics"],
  "Carlo Rubbia is an Italian particle physicist who led the experiments that discovered the W and Z bosons, confirming the electroweak theory.",
  "Born in Gorizia, Italy. Studied at the University of Pisa and the Scuola Normale Superiore.",
  "The discovery of the W and Z bosons was a triumphant confirmation of the unified electroweak theory and a milestone in the Standard Model.",
  [(1983, "Led the UA1 experiment at CERN that discovered the W and Z bosons"), (1984, "Awarded Nobel Prize in Physics with Simon van der Meer")],
  [("Experimental Observation of the Intermediate Vector Bosons W+, W− and Z⁰", 1983, "Papers announcing discovery of the W and Z bosons")],
  [("The joy of discovery is one of the greatest joys of life.", "Attributed")])

add("simon-van-der-meer", "Simon van der Meer", "シモン・ファンデルメール", 1925, 2011, ["nl"], ["physics", "engineering"],
  "Simon van der Meer was a Dutch accelerator physicist who developed stochastic cooling, enabling the discovery of the W and Z bosons.",
  "Born in The Hague, Netherlands. Studied at the Delft University of Technology.",
  "Van der Meer's stochastic cooling technique was essential to accumulating antiprotons for the collisions that revealed the W and Z bosons.",
  [(1968, "Conceived the idea of stochastic cooling"), (1984, "Awarded Nobel Prize in Physics with Carlo Rubbia")],
  [("Stochastic Cooling of Particle Beams", 1972, "Technical description of the beam cooling method")],
  [("The technique was considered impossible until it worked.", "Attributed")])

add("leon-lederman", "Leon Lederman", "レオン・レーダーマン", 1922, 2018, ["us"], ["physics"],
  "Leon Lederman was an American physicist who co-discovered the muon neutrino and coined the popular term 'the God particle' for the Higgs boson.",
  "Born in New York City to Russian-Jewish immigrant parents. Served in the US Army Signal Corps during WWII.",
  "Lederman's discovery of the muon neutrino proved that more than one type of neutrino exists, reshaping particle physics.",
  [(1962, "Co-discovered the muon neutrino"), (1988, "Awarded Nobel Prize in Physics")],
  [("The God Particle", 1993, "Popular science book about the Higgs boson and particle physics"), ("Observation of High-Energy Neutrino Reactions", 1962, "Paper reporting discovery of the muon neutrino")],
  [("Physics isn't a religion. If it were, we'd have a much easier time raising money.", "The God Particle")])

add("melvin-schwartz", "Melvin Schwartz", "メルヴィン・シュワルツ", 1932, 2006, ["us"], ["physics"],
  "Melvin Schwartz was an American physicist who proposed the neutrino beam method and co-discovered the muon neutrino.",
  "Born in New York City. Studied under Jack Steinberger and Isidor Rabi at Columbia.",
  "Schwartz's idea of using neutrino beams became a standard tool in particle physics experiments.",
  [(1960, "Proposed the method of using neutrino beams"), (1962, "Co-discovered the muon neutrino"), (1988, "Awarded Nobel Prize in Physics")],
  [("Feasibility of Using High-Energy Neutrinos", 1960, "Paper proposing neutrino beam experiments")],
  [("The method was so simple that I was sure someone must have thought of it before.", "Attributed")])

add("jack-steinberger", "Jack Steinberger", "ジャック・シュタインバーガー", 1921, 2020, ["us", "ch"], ["physics"],
  "Jack Steinberger was a German-born American physicist who co-discovered the muon neutrino and made key contributions to neutrino physics.",
  "Born in Bad Kissingen, Germany. Fled Nazi Germany in 1934 as part of a Kindertransport and settled in Chicago.",
  "Steinberger's experimental work on neutrinos helped establish the Standard Model of particle physics.",
  [(1962, "Co-discovered the muon neutrino at Brookhaven"), (1988, "Awarded Nobel Prize in Physics")],
  [("Observation of High-Energy Neutrino Reactions and the Existence of Two Kinds of Neutrinos", 1962, "Landmark paper proving the existence of the muon neutrino")],
  [("I owe my life and my career to the kindness of strangers.", "Autobiography")])

add("martin-perl", "Martin Perl", "マーティン・パール", 1927, 2014, ["us"], ["physics"],
  "Martin Perl was an American physicist who discovered the tau lepton, the third generation of charged leptons.",
  "Born in Brooklyn, New York. Worked as a chemical engineer before turning to physics.",
  "The discovery of the tau lepton revealed a third generation of fundamental particles, expanding the Standard Model.",
  [(1975, "Discovered the tau lepton at SLAC"), (1995, "Awarded Nobel Prize in Physics")],
  [("Evidence for Anomalous Lepton Production in e+e− Annihilation", 1975, "Paper announcing the discovery of the tau lepton")],
  [("The tau was hiding in plain sight for years.", "Attributed")])

add("frederick-reines", "Frederick Reines", "フレデリック・ライネス", 1918, 1998, ["us"], ["physics"],
  "Frederick Reines was an American physicist who first detected the neutrino, confirming a particle predicted 26 years earlier by Pauli.",
  "Born in Paterson, New Jersey. Worked on nuclear weapons tests at Los Alamos before turning to neutrino detection.",
  "The experimental detection of the neutrino was one of the great triumphs of 20th-century physics.",
  [(1956, "Co-detected the neutrino with Clyde Cowan"), (1995, "Awarded Nobel Prize in Physics for the detection of the neutrino")],
  [("Detection of the Free Neutrino", 1956, "Paper reporting the first experimental observation of the neutrino")],
  [("The neutrino is the most tiny quantity of reality ever imagined by a human being.", "Attributed")])

# ── POLITICAL/HISTORICAL FIGURES (~20) ────────────────────────────────────────

add("woodrow-wilson", "Woodrow Wilson", "ウッドロウ・ウィルソン", 1856, 1924, ["us"], ["politics"],
  "Woodrow Wilson was the 28th President of the United States who led the country through World War I and championed the League of Nations.",
  "Born in Staunton, Virginia. Became a political science professor and president of Princeton University before entering politics.",
  "Wilson's Fourteen Points and advocacy for the League of Nations shaped the international order of the 20th century.",
  [(1913, "Inaugurated as 28th President of the United States"), (1918, "Proposed the Fourteen Points for peace after WWI"), (1919, "Awarded Nobel Peace Prize for founding the League of Nations")],
  [("Fourteen Points", 1918, "Peace proposals for ending World War I and preventing future wars")],
  [("The world must be made safe for democracy.", "Address to Congress, 1917")])

add("dwight-eisenhower", "Dwight D. Eisenhower", "ドワイト・D・アイゼンハワー", 1890, 1969, ["us"], ["politics"],
  "Dwight Eisenhower was the Supreme Allied Commander in WWII and the 34th President of the United States.",
  "Born in Denison, Texas, raised in Abilene, Kansas. Graduated from West Point in 1915.",
  "Eisenhower's leadership of D-Day and his presidency shaped the Cold War era, establishing NATO and the interstate highway system.",
  [(1944, "Led the D-Day invasion of Normandy as Supreme Allied Commander"), (1953, "Inaugurated as 34th President"), (1961, "Delivered farewell address warning of the military-industrial complex")],
  [("Crusade in Europe", 1948, "Memoir of his wartime leadership")],
  [("In preparing for battle I have always found that plans are useless, but planning is indispensable.", "Attributed")])

add("john-f-kennedy", "John F. Kennedy", "ジョン・F・ケネディ", 1917, 1963, ["us"], ["politics"],
  "John F. Kennedy was the 35th President of the United States who navigated the Cuban Missile Crisis and inspired the space program.",
  "Born in Brookline, Massachusetts, to a wealthy Irish-American family. Served as a PT boat commander in World War II.",
  "Kennedy's presidency defined the optimism of the early 1960s, and his assassination became a defining moment in American history.",
  [(1961, "Inaugurated as the youngest elected president"), (1962, "Resolved the Cuban Missile Crisis through diplomacy"), (1963, "Assassinated in Dallas, Texas")],
  [("Profiles in Courage", 1957, "Pulitzer Prize-winning book about senators who risked their careers for principle")],
  [("Ask not what your country can do for you — ask what you can do for your country.", "Inaugural Address, 1961")])

add("lyndon-johnson", "Lyndon B. Johnson", "リンドン・B・ジョンソン", 1908, 1973, ["us"], ["politics"],
  "Lyndon Johnson was the 36th President of the United States who signed the Civil Rights Act and launched the Great Society programs.",
  "Born near Stonewall, Texas. Worked as a teacher before entering politics as a congressional aide.",
  "Johnson's Great Society legislation transformed American social policy through Medicare, Medicaid, and landmark civil rights laws.",
  [(1964, "Signed the Civil Rights Act of 1964"), (1965, "Signed the Voting Rights Act and launched Medicare"), (1968, "Declined to run for re-election amid Vietnam War opposition")],
  [("The Great Society speech", 1964, "Address outlining his ambitious domestic reform agenda")],
  [("We shall overcome.", "Address to Congress on the Voting Rights Act, 1965")])

add("harry-truman", "Harry S. Truman", "ハリー・S・トルーマン", 1884, 1972, ["us"], ["politics"],
  "Harry Truman was the 33rd President of the United States who made the decision to use atomic weapons and implemented the Marshall Plan.",
  "Born in Lamar, Missouri. Served as an artillery officer in WWI and ran a haberdashery before entering politics.",
  "Truman's decisions to use atomic weapons, implement the Marshall Plan, and establish the Truman Doctrine defined the early Cold War.",
  [(1945, "Became president upon FDR's death; authorized use of atomic bombs on Japan"), (1947, "Announced the Truman Doctrine and supported the Marshall Plan"), (1948, "Won a surprise election victory")],
  [("Memoirs", 1955, "Two-volume presidential memoir")],
  [("The buck stops here.", "Sign on his presidential desk")])

add("charles-de-gaulle", "Charles de Gaulle", "シャルル・ド・ゴール", 1890, 1970, ["fr"], ["politics"],
  "Charles de Gaulle was a French general who led the Free French during WWII and founded the Fifth Republic as its first president.",
  "Born in Lille to a Catholic family. Graduated from Saint-Cyr military academy and was wounded and captured in WWI.",
  "De Gaulle's leadership during WWII and his creation of the Fifth Republic defined modern France's political identity and foreign policy.",
  [(1940, "Broadcast the Appeal of 18 June from London, rallying Free French forces"), (1944, "Led the liberation of Paris"), (1958, "Founded the Fifth Republic and became its first president")],
  [("The Army of the Future", 1934, "Book advocating mechanized warfare"), ("War Memoirs", 1954, "Three-volume memoir of WWII")],
  [("France cannot be France without greatness.", "War Memoirs")])

add("konrad-adenauer", "Konrad Adenauer", "コンラート・アデナウアー", 1876, 1967, ["de"], ["politics"],
  "Konrad Adenauer was the first Chancellor of West Germany who oversaw the country's post-war reconstruction and integration into the Western alliance.",
  "Born in Cologne. Served as mayor of Cologne during the Weimar Republic before being removed by the Nazis.",
  "Adenauer's leadership transformed West Germany from an occupied nation into a prosperous democracy anchored in the Western alliance.",
  [(1949, "Became first Chancellor of the Federal Republic of Germany"), (1955, "Achieved full sovereignty for West Germany"), (1963, "Retired as Chancellor at age 87")],
  [("Memoirs", 1966, "Political memoir covering his years as Chancellor")],
  [("We all live under the same sky, but we don't all have the same horizon.", "Attributed")])

add("willy-brandt", "Willy Brandt", "ヴィリー・ブラント", 1913, 1992, ["de"], ["politics"],
  "Willy Brandt was a German Chancellor whose Ostpolitik policy of engagement with Eastern Europe helped ease Cold War tensions.",
  "Born Herbert Frahm in Lübeck. Fled Nazi Germany as a young socialist and lived in exile in Scandinavia.",
  "Brandt's Ostpolitik and his iconic kneeling at the Warsaw Ghetto memorial symbolized German reconciliation with its past.",
  [(1969, "Became Chancellor of West Germany"), (1970, "Knelt at the Warsaw Ghetto memorial in a gesture of atonement"), (1971, "Awarded Nobel Peace Prize for Ostpolitik")],
  [("My Road to Berlin", 1960, "Autobiography covering his exile years and political career")],
  [("Peace is not everything, but without peace, everything is nothing.", "Attributed")])

add("helmut-kohl", "Helmut Kohl", "ヘルムート・コール", 1930, 2017, ["de"], ["politics"],
  "Helmut Kohl was a German Chancellor who presided over the reunification of Germany and was a driving force behind European integration.",
  "Born in Ludwigshafen. Earned a doctorate in political science and rose through the CDU party ranks.",
  "Kohl's decisive leadership during 1989-1990 made German reunification possible and his partnership with Mitterrand advanced European unity.",
  [(1982, "Became Chancellor of West Germany"), (1990, "Oversaw German reunification"), (1992, "Co-signed the Maastricht Treaty establishing the European Union")],
  [("Ich wollte Deutschlands Einheit", 1996, "Memoir on German reunification")],
  [("He who does not know where he comes from cannot know where he is going.", "Attributed")])

add("francois-mitterrand", "François Mitterrand", "フランソワ・ミッテラン", 1916, 1996, ["fr"], ["politics"],
  "François Mitterrand was the longest-serving President of France, who modernized the country and deepened European integration.",
  "Born in Jarnac, Charente. Captured during WWII, he escaped and joined the Resistance.",
  "Mitterrand's presidency abolished the death penalty, decentralized government, and strengthened Franco-German relations as the engine of European unity.",
  [(1981, "Elected President of France as the first Socialist president of the Fifth Republic"), (1981, "Abolished the death penalty in France"), (1992, "Championed the Maastricht Treaty")],
  [("The Wheat and the Chaff", 1982, "Political diary and reflections")],
  [("France is our homeland, Europe is our future.", "Attributed")])

add("clement-attlee", "Clement Attlee", "クレメント・アトリー", 1883, 1967, ["gb"], ["politics"],
  "Clement Attlee was a British Prime Minister who built the welfare state, including the National Health Service.",
  "Born in Putney, London. Trained as a barrister and became a social worker in London's East End, which shaped his politics.",
  "Attlee's government created the NHS, nationalized key industries, and granted independence to India, fundamentally reshaping Britain.",
  [(1945, "Became Prime Minister after defeating Churchill in a landslide"), (1946, "Established the National Health Service"), (1947, "Oversaw Indian independence")],
  [("As It Happened", 1954, "Autobiography of his political career")],
  [("Democracy means government by discussion, but it is only effective if you can stop people talking.", "Attributed")])

add("david-lloyd-george", "David Lloyd George", "デイヴィッド・ロイド・ジョージ", 1863, 1945, ["gb"], ["politics"],
  "David Lloyd George was a British Prime Minister who led the country through the latter half of World War I and introduced pioneering social reforms.",
  "Born in Manchester but raised in Wales by his uncle, a cobbler. Became a solicitor before entering Parliament.",
  "Lloyd George's People's Budget and social insurance programs laid the foundations of the British welfare state.",
  [(1908, "As Chancellor, introduced the People's Budget with new social programs"), (1916, "Became Prime Minister and reorganized the war effort"), (1919, "Represented Britain at the Paris Peace Conference")],
  [("War Memoirs", 1933, "Six-volume account of World War I")],
  [("Don't be afraid to take a big step if one is indicated. You can't cross a chasm in two small jumps.", "Attributed")])

add("william-gladstone", "William Gladstone", "ウィリアム・グラッドストン", 1809, 1898, ["gb"], ["politics"],
  "William Gladstone was a British Prime Minister who served four terms and championed liberal reform, Irish Home Rule, and free trade.",
  "Born in Liverpool to a wealthy merchant family. Educated at Eton and Oxford, he entered Parliament at age 22.",
  "Gladstone's reforms expanded voting rights, established public education, and defined Victorian liberalism.",
  [(1868, "Became Prime Minister for the first time"), (1870, "Passed the Elementary Education Act"), (1886, "Introduced the first Irish Home Rule Bill")],
  [("The State in Its Relations with the Church", 1838, "Early work on church-state relations")],
  [("Justice delayed is justice denied.", "Attributed")])

add("benjamin-disraeli", "Benjamin Disraeli", "ベンジャミン・ディズレーリ", 1804, 1881, ["gb"], ["politics", "literature"],
  "Benjamin Disraeli was a British Prime Minister and novelist who expanded the British Empire and enacted social reforms.",
  "Born in London to an Italian-Jewish family. Baptized as an Anglican at age 12. Became a successful novelist before entering politics.",
  "Disraeli's 'One Nation' conservatism and imperial ambitions shaped modern British Toryism.",
  [(1868, "Became Prime Minister for the first time"), (1875, "Purchased shares in the Suez Canal for Britain"), (1876, "Made Queen Victoria Empress of India")],
  [("Sybil, or The Two Nations", 1845, "Novel depicting the divide between rich and poor in England"), ("Coningsby", 1844, "Political novel advocating Young England ideals")],
  [("The secret of success is constancy to purpose.", "Attributed")])

add("camillo-benso-cavour", "Camillo Benso, Count of Cavour", "カミッロ・カヴール", 1810, 1861, ["it"], ["politics"],
  "Cavour was the architect of Italian unification who served as the first Prime Minister of a united Italy.",
  "Born in Turin to an aristocratic Piedmontese family. Traveled widely in Europe and studied British parliamentary government.",
  "Cavour's diplomatic skill united most of the Italian peninsula into a single nation-state through a combination of diplomacy and war.",
  [(1852, "Became Prime Minister of the Kingdom of Sardinia"), (1859, "Allied with France to defeat Austria in the Second Italian War of Independence"), (1861, "Became first Prime Minister of the Kingdom of Italy")],
  [("Letters", 1883, "Published correspondence revealing his diplomatic strategy")],
  [("Italy is made. All is safe.", "Attributed deathbed words, possibly apocryphal")])

add("metternich", "Klemens von Metternich", "クレメンス・フォン・メッテルニヒ", 1773, 1859, ["at"], ["politics"],
  "Metternich was an Austrian statesman who dominated European diplomacy from the defeat of Napoleon to the revolutions of 1848.",
  "Born in Koblenz to a noble Rhineland family. Studied at Strasbourg and Mainz before entering the Austrian diplomatic service.",
  "The Metternich system of conservative balance-of-power politics maintained European stability for over three decades.",
  [(1809, "Became Austrian Foreign Minister"), (1814, "Presided over the Congress of Vienna"), (1848, "Forced to resign and flee during the revolutions of 1848")],
  [("Memoirs", 1880, "Posthumously published political memoirs")],
  [("When Paris sneezes, Europe catches a cold.", "Attributed")])

add("talleyrand", "Charles Maurice de Talleyrand", "シャルル・モーリス・ド・タレーラン", 1754, 1838, ["fr"], ["politics"],
  "Talleyrand was a French diplomat who served every regime from the Ancien Régime through the Bourbon Restoration, shaping European diplomacy.",
  "Born in Paris to an aristocratic family. A childhood injury led him to the clergy, becoming Bishop of Autun.",
  "Talleyrand's diplomatic genius at the Congress of Vienna restored France's position among the great powers after Napoleon's defeat.",
  [(1797, "Became Foreign Minister under the Directory"), (1807, "Broke with Napoleon over imperial overreach"), (1814, "Represented France at the Congress of Vienna")],
  [("Memoirs", 1891, "Posthumously published diplomatic memoirs")],
  [("Speech was given to man to disguise his thoughts.", "Attributed")])

add("robespierre", "Maximilien Robespierre", "マクシミリアン・ロベスピエール", 1758, 1794, ["fr"], ["politics"],
  "Maximilien Robespierre was a leader of the French Revolution who became the dominant figure of the Committee of Public Safety during the Reign of Terror.",
  "Born in Arras to a lawyer's family. Studied law in Paris on a scholarship and became an advocate for the poor.",
  "Robespierre's radical pursuit of revolutionary virtue and the Reign of Terror remain defining moments in the history of revolution and political extremism.",
  [(1789, "Elected to the Estates-General as a representative of the Third Estate"), (1793, "Became dominant member of the Committee of Public Safety"), (1794, "Arrested and executed by guillotine in the Thermidorian Reaction")],
  [("Report on the Principles of Political Morality", 1794, "Speech defining revolutionary virtue and justifying the Terror")],
  [("The secret of freedom lies in educating people, whereas the secret of tyranny is in keeping them ignorant.", "Attributed")])

add("richelieu", "Cardinal Richelieu", "リシュリュー枢機卿", 1585, 1642, ["fr"], ["politics"],
  "Cardinal Richelieu was a French clergyman and statesman who served as chief minister to Louis XIII and consolidated royal power in France.",
  "Born Armand Jean du Plessis in Paris to a noble family. Became Bishop of Luçon at age 21.",
  "Richelieu centralized French royal authority, weakened the Habsburg powers, and laid the foundations for French dominance in Europe.",
  [(1624, "Became Chief Minister of France"), (1628, "Defeated the Huguenot stronghold of La Rochelle"), (1635, "Founded the Académie française")],
  [("Political Testament", 1688, "Posthumously published treatise on statecraft")],
  [("If you give me six lines written by the hand of the most honest of men, I will find something in them which will hang him.", "Attributed")])

# ── MUSICIANS (~15) ───────────────────────────────────────────────────────────

add("enrico-caruso", "Enrico Caruso", "エンリコ・カルーソー", 1873, 1921, ["it"], ["art"],
  "Enrico Caruso was an Italian operatic tenor who became the first major recording star and one of the most famous singers in history.",
  "Born in Naples to a poor family. Sang in local churches and cafes before his operatic debut at age 21.",
  "Caruso's powerful voice and early adoption of recording technology made opera accessible to millions and defined the tenor voice for generations.",
  [(1902, "Made his first gramophone recordings in Milan"), (1903, "Debuted at the Metropolitan Opera in New York"), (1920, "Gave his last performance at the Met")],
  [("Vesti la giubba recording", 1907, "One of the first recordings to sell a million copies")],
  [("I sing naturally, as a bird sings.", "Attributed")])

add("luciano-pavarotti", "Luciano Pavarotti", "ルチアーノ・パヴァロッティ", 1935, 2007, ["it"], ["art"],
  "Luciano Pavarotti was an Italian operatic tenor who became one of the most commercially successful and beloved tenors of all time.",
  "Born in Modena, Italy. His father was an amateur tenor and baker. Worked as a schoolteacher before pursuing singing full-time.",
  "Pavarotti brought opera to a mass audience through televised concerts, the Three Tenors performances, and crossover recordings.",
  [(1961, "Won the Achille Peri competition and made his operatic debut"), (1972, "Achieved fame for nine consecutive high C's in La fille du régiment at the Met"), (1990, "Performed with the Three Tenors at the FIFA World Cup in Rome")],
  [("Nessun dorma", 1990, "Performance at the World Cup that became a global phenomenon")],
  [("If children are not introduced to music at an early age, I believe something fundamental is actually being taken from them.", "Attributed")])

add("jose-carreras", "José Carreras", "ホセ・カレーラス", 1946, None, ["es"], ["art"],
  "José Carreras is a Spanish operatic tenor known as one of the Three Tenors alongside Pavarotti and Domingo.",
  "Born in Barcelona. Made his stage debut at age 11 at the Gran Teatre del Liceu.",
  "Carreras's lyric tenor voice and his comeback after leukemia inspired millions, and his foundation has raised significant funds for leukemia research.",
  [(1970, "Made his debut at the Royal Opera House, London"), (1988, "Recovered from leukemia and founded the José Carreras Leukemia Foundation"), (1990, "Performed as one of the Three Tenors at the World Cup")],
  [("Singing from the Soul", 1991, "Autobiography detailing his career and battle with leukemia")],
  [("When I recovered, I felt I had to give something back.", "On founding his leukemia foundation")])

add("placido-domingo", "Plácido Domingo", "プラシド・ドミンゴ", 1941, None, ["es", "mx"], ["art"],
  "Plácido Domingo is a Spanish tenor and conductor who has performed more roles than any other tenor in history.",
  "Born in Madrid to a family of zarzuela performers. Grew up in Mexico City, where he studied at the National Conservatory.",
  "Domingo's extraordinary versatility across over 150 roles and his work as a conductor and administrator have made him one of opera's most complete artists.",
  [(1966, "Debuted at the Metropolitan Opera"), (1990, "Performed as one of the Three Tenors"), (1996, "Became General Director of the Washington National Opera")],
  [("My First Forty Years", 1983, "Autobiography of his career in opera")],
  [("To me, opera is the greatest of all art forms because it combines all art forms.", "Attributed")])

add("marian-anderson", "Marian Anderson", "マリアン・アンダーソン", 1897, 1993, ["us"], ["art"],
  "Marian Anderson was an American contralto who broke racial barriers and became the first African American to perform at the Metropolitan Opera.",
  "Born in Philadelphia. Raised in poverty, her church congregation raised funds for her voice lessons.",
  "Anderson's historic Lincoln Memorial concert and Met debut challenged racial segregation in American culture.",
  [(1939, "Performed at the Lincoln Memorial after being denied Constitution Hall due to her race"), (1955, "Became the first African American to perform at the Metropolitan Opera"), (1963, "Sang at the March on Washington")],
  [("My Lord, What a Morning", 1956, "Autobiography recounting her journey as a Black artist in America")],
  [("As long as you keep a person down, some part of you has to be down there to hold them, so it means you cannot soar as you otherwise might.", "Attributed")])

add("jessye-norman", "Jessye Norman", "ジェシー・ノーマン", 1945, 2019, ["us"], ["art"],
  "Jessye Norman was an American soprano renowned for her powerful, richly textured voice and commanding stage presence.",
  "Born in Augusta, Georgia. Studied at Howard University and the Peabody Conservatory.",
  "Norman's extraordinary vocal range and dramatic intensity made her one of the greatest sopranos of the 20th century.",
  [(1969, "Made her operatic debut at the Deutsche Oper Berlin"), (1983, "Debuted at the Metropolitan Opera"), (1989, "Sang La Marseillaise at the French Bicentennial celebrations")],
  [("Stand Up Straight and Sing!", 2014, "Memoir reflecting on her life and career")],
  [("You have to know exactly what you want out of your career. If you want to be a star, you don't bother with other things.", "Attributed")])

add("leontyne-price", "Leontyne Price", "レオンタイン・プライス", 1927, None, ["us"], ["art"],
  "Leontyne Price is an American soprano who was one of the first African Americans to become a leading artist at the Metropolitan Opera.",
  "Born in Laurel, Mississippi. Studied at the Juilliard School on a scholarship.",
  "Price's lyric soprano voice and trailblazing career opened doors for African American opera singers and she became one of the most celebrated Aïdas in history.",
  [(1961, "Debuted at the Metropolitan Opera to a 42-minute standing ovation"), (1966, "Opened the new Metropolitan Opera House at Lincoln Center"), (1985, "Gave her farewell operatic performance as Aïda")],
  [("Aïda recordings", 1962, "Definitive recordings of Verdi's Aïda")],
  [("All token blacks have the same experience. I have been pointed at as a solution to things that have not yet begun to be solved.", "Attributed")])

add("joan-sutherland", "Joan Sutherland", "ジョーン・サザーランド", 1926, 2010, ["au"], ["art"],
  "Joan Sutherland was an Australian dramatic coloratura soprano known as 'La Stupenda' for her extraordinary vocal agility.",
  "Born in Sydney. Studied at the Royal College of Music in London.",
  "Sutherland's revival of bel canto opera roles restored forgotten masterworks to the repertoire and set new standards for coloratura singing.",
  [(1959, "Breakthrough performance as Lucia di Lammermoor at Covent Garden"), (1961, "Debuted at the Metropolitan Opera"), (1990, "Gave her farewell performance in Sydney")],
  [("The Art of the Prima Donna", 1960, "Landmark recording showcasing bel canto arias")],
  [("I think the audience deserves the best you can give them.", "Attributed")])

add("yo-yo-ma", "Yo-Yo Ma", "ヨーヨー・マ", 1955, None, ["us", "fr"], ["art"],
  "Yo-Yo Ma is a French-born American cellist known for his virtuosity, his wide-ranging musical curiosity, and his cultural ambassadorship.",
  "Born in Paris to Chinese parents. A child prodigy, he performed for President Kennedy at age seven and studied at Juilliard and Harvard.",
  "Ma's genre-crossing collaborations and his Silk Road Ensemble have promoted cross-cultural understanding through music worldwide.",
  [(1978, "Won the Avery Fisher Prize"), (1998, "Founded the Silk Road Ensemble"), (2018, "Began a project to perform all six Bach Cello Suites in 36 locations around the world")],
  [("Inspired by Bach", 1997, "Six-film project exploring Bach's Cello Suites through various art forms")],
  [("Music, in performance, is a type of sculpture. The air in the performance is sculpted into something.", "Interview")])

add("itzhak-perlman", "Itzhak Perlman", "イツァーク・パールマン", 1945, None, ["il", "us"], ["art"],
  "Itzhak Perlman is an Israeli-American violinist and conductor widely regarded as one of the greatest violinists of the 20th and 21st centuries.",
  "Born in Tel Aviv. Contracted polio at age four and plays the violin while seated. Studied at the Juilliard School.",
  "Perlman's warm tone, technical mastery, and charismatic performances have made him one of the most beloved classical musicians in the world.",
  [(1958, "Appeared on The Ed Sullivan Show at age 13"), (1964, "Made his Carnegie Hall debut"), (2015, "Awarded Presidential Medal of Freedom")],
  [("Schindler's List soundtrack", 1993, "Iconic violin solos for Steven Spielberg's film")],
  [("For every child prodigy, there are ten equally talented ones who never get the opportunity.", "Attributed")])

add("jascha-heifetz", "Jascha Heifetz", "ヤッシャ・ハイフェッツ", 1901, 1987, ["us", "lt"], ["art"],
  "Jascha Heifetz was a Lithuanian-born American violinist widely considered the greatest violinist of the 20th century.",
  "Born in Vilnius, Lithuania. A child prodigy, he studied at the Saint Petersburg Conservatory and debuted at Carnegie Hall at age 16.",
  "Heifetz's flawless technique and intense musical personality set the standard for modern violin playing.",
  [(1917, "Made his legendary Carnegie Hall debut at age 16"), (1925, "Became an American citizen"), (1972, "Retired from public performance and devoted himself to teaching")],
  [("Heifetz recordings of the Tchaikovsky and Brahms concertos", 1955, "Definitive recordings of the major violin concertos")],
  [("If I don't practice one day, I know it; two days, the critics know it; three days, the public knows it.", "Attributed")])

add("vladimir-horowitz", "Vladimir Horowitz", "ウラディミール・ホロヴィッツ", 1903, 1989, ["us", "ua"], ["art"],
  "Vladimir Horowitz was a Ukrainian-born American pianist regarded as one of the greatest pianists of all time.",
  "Born in Berdychiv, Ukraine. Studied at the Kyiv Conservatory and left the Soviet Union in 1925.",
  "Horowitz's electrifying technique and dramatic interpretations set a new standard for virtuoso piano performance.",
  [(1928, "Made his American debut at Carnegie Hall"), (1965, "Returned to the concert stage after a 12-year retirement"), (1986, "Gave a historic recital in Moscow, returning to Russia after 61 years")],
  [("Horowitz at Carnegie Hall", 1965, "Legendary comeback recital recording")],
  [("My face is my passport.", "On leaving the Soviet Union")])

add("arthur-rubinstein", "Arthur Rubinstein", "アルトゥール・ルービンシュタイン", 1887, 1982, ["pl", "us"], ["art"],
  "Arthur Rubinstein was a Polish-American pianist celebrated as one of the greatest interpreters of Chopin and the Romantic repertoire.",
  "Born in Łódź, Poland. A child prodigy, he debuted with the Berlin Philharmonic at age 13.",
  "Rubinstein's warm, singing tone and his definitive Chopin interpretations influenced generations of pianists.",
  [(1906, "Made his American debut at Carnegie Hall"), (1937, "Revitalized his career with renewed dedication to practice"), (1976, "Gave his farewell concert in London at age 89")],
  [("My Young Years", 1973, "First volume of autobiography"), ("My Many Years", 1980, "Second volume of autobiography")],
  [("I have found that if you love life, life will love you back.", "Attributed")])

add("sviatoslav-richter", "Sviatoslav Richter", "スヴャトスラフ・リヒテル", 1915, 1997, ["ua", "ru"], ["art"],
  "Sviatoslav Richter was a Ukrainian-born Soviet pianist renowned for his immense repertoire, technical power, and profound interpretive depth.",
  "Born in Zhytomyr, Ukraine. Largely self-taught until entering the Moscow Conservatory at age 22 under Heinrich Neuhaus.",
  "Richter's vast repertoire spanning Baroque to modern music and his uncompromising artistry made him one of the most revered pianists of the 20th century.",
  [(1945, "Won the All-Union Competition of Performers in Moscow"), (1960, "Made his American debut to sensational acclaim"), (1964, "Began performing in intimate, darkened halls lit only by a desk lamp")],
  [("Richter: The Enigma", 1998, "Documentary film by Bruno Monsaingeon")],
  [("The interpreter is really an executant, carrying out the composer's intentions to the letter.", "Interview with Monsaingeon")])

# ── ARTISTS (~15) ─────────────────────────────────────────────────────────────

add("ansel-adams", "Ansel Adams", "アンセル・アダムス", 1902, 1984, ["us"], ["art"],
  "Ansel Adams was an American landscape photographer and environmentalist known for his black-and-white photographs of the American West.",
  "Born in San Francisco. Trained as a pianist before turning to photography after a trip to Yosemite at age 14.",
  "Adams's photographs defined the aesthetic of American wilderness and his advocacy helped expand the national park system.",
  [(1927, "Published his first portfolio, Parmelian Prints of the High Sierras"), (1932, "Co-founded Group f/64 promoting sharp-focus photography"), (1941, "Began photographing national parks for the Department of the Interior")],
  [("Moonrise, Hernandez, New Mexico", 1941, "One of the most famous photographs ever made"), ("The Camera", 1980, "First volume of his technical photography trilogy")],
  [("You don't take a photograph, you make it.", "Attributed")])

add("dorothea-lange", "Dorothea Lange", "ドロシア・ラング", 1895, 1965, ["us"], ["art"],
  "Dorothea Lange was an American documentary photographer best known for her Depression-era work for the Farm Security Administration.",
  "Born in Hoboken, New Jersey. Childhood polio left her with a lifelong limp. Studied photography in New York.",
  "Lange's Migrant Mother became the defining image of the Great Depression and demonstrated the power of documentary photography to drive social change.",
  [(1936, "Photographed Migrant Mother at a California pea-pickers camp"), (1941, "Documented Japanese American internment for the War Relocation Authority")],
  [("Migrant Mother", 1936, "Iconic photograph of Florence Owens Thompson that became a symbol of the Depression")],
  [("The camera is an instrument that teaches people how to see without a camera.", "Attributed")])

add("man-ray", "Man Ray", "マン・レイ", 1890, 1976, ["us", "fr"], ["art"],
  "Man Ray was an American-French visual artist who was a significant contributor to Dada and Surrealism.",
  "Born Emmanuel Radnitzky in Philadelphia. Moved to New York and befriended Marcel Duchamp before settling in Paris.",
  "Man Ray's innovations in photography, including rayographs and solarization, expanded the boundaries of the medium as a fine art.",
  [(1921, "Moved to Paris and became a central figure in the Dada and Surrealist movements"), (1922, "Invented the rayograph, a cameraless photographic technique"), (1924, "Created the film Le Retour à la Raison")],
  [("Le Violon d'Ingres", 1924, "Iconic photograph transforming Kiki de Montparnasse into a violin"), ("Rayographs", 1922, "Series of photograms made without a camera")],
  [("I photograph the things that I do not wish to paint, the things which already have an existence.", "Self Portrait")])

add("christo", "Christo", "クリスト", 1935, 2020, ["bg", "us"], ["art"],
  "Christo was a Bulgarian-born American artist known for massive environmental works of art created with his wife Jeanne-Claude.",
  "Born Christo Vladimirov Javacheff in Gabrovo, Bulgaria. Studied at the National Academy of Art in Sofia before fleeing to the West.",
  "Christo and Jeanne-Claude's monumental wrapped structures and environmental installations redefined the scale and possibility of public art.",
  [(1985, "Wrapped the Pont Neuf bridge in Paris"), (1995, "Wrapped the Reichstag in Berlin"), (2005, "Installed The Gates in Central Park, New York")],
  [("Wrapped Reichstag", 1995, "The German parliament building wrapped in silvery fabric"), ("The Gates", 2005, "7,503 saffron-colored gates installed along Central Park pathways")],
  [("The work of art is a scream of freedom.", "Attributed")])

add("nam-june-paik", "Nam June Paik", "ナム・ジュン・パイク（白南準）", 1932, 2006, ["kr", "us"], ["art"],
  "Nam June Paik was a Korean-American artist considered the founder of video art.",
  "Born in Seoul, Korea. Studied music and art history in Tokyo and Germany, where he became associated with the Fluxus movement.",
  "Paik's pioneering use of television and video technology as artistic media created an entirely new art form and anticipated the digital age.",
  [(1963, "Created his first video art exhibition, Exposition of Music – Electronic Television"), (1974, "Used the term 'electronic superhighway,' predicting the internet"), (1995, "Created Electronic Superhighway, a monumental video installation")],
  [("Electronic Superhighway: Continental U.S., Alaska, Hawaii", 1995, "Monumental video installation using 336 television sets"), ("TV Buddha", 1974, "Iconic installation of a Buddha statue watching itself on a closed-circuit TV")],
  [("Skin has become inadequate in interfacing with reality. Technology has become the body's new membrane of existence.", "Attributed")])

add("marina-abramovic", "Marina Abramović", "マリーナ・アブラモヴィッチ", 1946, None, ["rs", "us"], ["art"],
  "Marina Abramović is a Serbian performance artist known as the 'grandmother of performance art' for her boundary-pushing endurance works.",
  "Born in Belgrade, Yugoslavia. Studied at the Academy of Fine Arts in Belgrade and Zagreb.",
  "Abramović's radical performances testing the limits of the body and mind expanded the definition of art and influenced generations of performance artists.",
  [(1974, "Performed Rhythm 0, allowing the audience to use 72 objects on her body"), (1988, "Performed The Lovers with Ulay, walking the Great Wall of China"), (2010, "Performed The Artist Is Present at MoMA for 736 hours")],
  [("The Artist Is Present", 2010, "Durational performance at MoMA where she sat silently across from visitors")],
  [("An artist should not lie to themselves or others.", "Attributed")])

add("joseph-beuys", "Joseph Beuys", "ヨーゼフ・ボイス", 1921, 1986, ["de"], ["art"],
  "Joseph Beuys was a German artist, sculptor, and activist whose expanded concept of art encompassed social sculpture and political action.",
  "Born in Krefeld, Germany. Served as a Luftwaffe pilot in WWII and was deeply shaped by the experience of war.",
  "Beuys's concept of 'social sculpture' — the idea that everyone is an artist and all of life is art — profoundly influenced contemporary art.",
  [(1965, "Performed How to Explain Pictures to a Dead Hare"), (1974, "Performed I Like America and America Likes Me, living with a coyote in a gallery"), (1982, "Planted 7000 Oaks in Kassel as a living artwork")],
  [("7000 Oaks", 1982, "Monumental environmental artwork planting trees across Kassel"), ("How to Explain Pictures to a Dead Hare", 1965, "Iconic performance in which he whispered to a dead hare while covered in honey and gold leaf")],
  [("Every human being is an artist.", "Attributed")])

add("anish-kapoor", "Anish Kapoor", "アニッシュ・カプーア", 1954, None, ["in", "gb"], ["art"],
  "Anish Kapoor is an Indian-born British sculptor known for his monumental works that play with form, color, and the perception of space.",
  "Born in Mumbai, India. Moved to London in the 1970s to study art at the Hornsey College of Art and Chelsea School of Art.",
  "Kapoor's Cloud Gate in Chicago and his use of Vantablack have made him one of the most recognized sculptors in the world.",
  [(1990, "Represented Britain at the Venice Biennale"), (2004, "Unveiled Cloud Gate ('The Bean') in Chicago's Millennium Park"), (2016, "Acquired exclusive artistic rights to Vantablack, the world's darkest material")],
  [("Cloud Gate", 2004, "Monumental polished steel sculpture in Chicago reflecting the city skyline"), ("Descent into Limbo", 1992, "Installation featuring a seemingly bottomless void")],
  [("I feel the less I do, the more of an artist I am.", "Interview")])

add("yoko-ono", "Yoko Ono", "オノ・ヨーコ（小野洋子）", 1933, None, ["jp", "us"], ["art"],
  "Yoko Ono is a Japanese-American artist, musician, and peace activist who was a pioneer of conceptual and performance art.",
  "Born in Tokyo to a wealthy banking family. Studied philosophy at Gakushuin University before moving to New York.",
  "Ono's instruction-based conceptual art and peace activism with John Lennon made her one of the most influential avant-garde artists of the 20th century.",
  [(1964, "Published Grapefruit, a book of conceptual art instructions"), (1966, "Exhibited Cut Piece, a landmark performance work"), (1969, "Staged the Bed-In for Peace with John Lennon in Amsterdam and Montreal")],
  [("Grapefruit", 1964, "Book of instruction-based conceptual art pieces"), ("Cut Piece", 1964, "Performance in which the audience cut away her clothing")],
  [("A dream you dream alone is only a dream. A dream you dream together is reality.", "Attributed")])

add("kara-walker", "Kara Walker", "カラ・ウォーカー", 1969, None, ["us"], ["art"],
  "Kara Walker is an American artist known for her provocative silhouette installations exploring race, gender, sexuality, and violence in American history.",
  "Born in Stockton, California. Moved to Atlanta as a teenager, where she confronted the deep racial history of the American South.",
  "Walker's unflinching visual narratives about race and power have made her one of the most important American artists of her generation.",
  [(1994, "Created Gone: An Historical Romance, her breakthrough room-sized silhouette installation"), (1997, "Became one of the youngest recipients of a MacArthur Fellowship at age 28"), (2014, "Created A Subtlety, a massive sugar sphinx installation at the old Domino Sugar factory")],
  [("A Subtlety", 2014, "Monumental sugar-coated sphinx installation addressing the history of sugar and slavery"), ("Gone: An Historical Romance of a Civil War as It Occurred b'tween the Dusky Thighs of One Young Negress and Her Heart", 1994, "Room-sized silhouette installation")],
  [("I make art that is interested in the uncomfortable.", "Interview")])

add("cindy-sherman", "Cindy Sherman", "シンディ・シャーマン", 1954, None, ["us"], ["art"],
  "Cindy Sherman is an American photographer and film director known for her conceptual self-portraits exploring identity and representation.",
  "Born in Glen Ridge, New Jersey. Studied at the State University College at Buffalo.",
  "Sherman's Untitled Film Stills series redefined the relationship between photography, identity, and the construction of femininity.",
  [(1977, "Began the Untitled Film Stills series"), (1995, "Awarded MacArthur Fellowship"), (2012, "Major retrospective at the Museum of Modern Art")],
  [("Untitled Film Stills", 1977, "Series of 69 black-and-white photographs of herself in various fictional female roles")],
  [("I feel I'm anonymous in my work. When I look at the pictures, I never see myself.", "Interview")])

add("olafur-eliasson", "Olafur Eliasson", "オラファー・エリアソン", 1967, None, ["dk", "is"], ["art"],
  "Olafur Eliasson is a Danish-Icelandic artist known for large-scale installations using natural elements like light, water, and temperature.",
  "Born in Copenhagen to Icelandic parents. Studied at the Royal Danish Academy of Fine Arts.",
  "Eliasson's immersive installations at major cultural institutions worldwide have brought environmental awareness and sensory experience into contemporary art.",
  [(2003, "Installed The Weather Project in the Turbine Hall of Tate Modern, London"), (2008, "Created New York City Waterfalls, four artificial waterfalls in New York Harbor"), (2019, "Installed Ice Watch in London, placing Arctic ice blocks in the city")],
  [("The Weather Project", 2003, "Installation creating an artificial sun inside Tate Modern, visited by two million people"), ("Ice Watch", 2014, "Installation placing blocks of glacial ice in public spaces to raise climate awareness")],
  [("Art does not show people what to do, yet engaging with a good work of art can connect you to your senses.", "Attributed")])

add("jeff-koons", "Jeff Koons", "ジェフ・クーンズ", 1955, None, ["us"], ["art"],
  "Jeff Koons is an American artist known for his large-scale reproductions of banal objects and his works exploring kitsch and commodity culture.",
  "Born in York, Pennsylvania. Studied at the Maryland Institute College of Art and worked as a Wall Street commodities broker.",
  "Koons's Balloon Dog sculptures and his audacious embrace of kitsch have made him one of the most expensive and controversial living artists.",
  [(1986, "Exhibited the Luxury and Degradation series"), (1988, "Created the Banality series including Michael Jackson and Bubbles"), (2013, "Balloon Dog (Orange) sold for $58.4 million, then a record for a living artist")],
  [("Balloon Dog", 1994, "Series of monumental stainless steel sculptures resembling balloon animals"), ("Michael Jackson and Bubbles", 1988, "Gold-and-white porcelain sculpture of the pop star")],
  [("I try to create work that doesn't make people feel intimidated.", "Interview")])

add("damien-hirst", "Damien Hirst", "ダミアン・ハースト", 1965, None, ["gb"], ["art"],
  "Damien Hirst is a British artist and the most prominent member of the Young British Artists, known for works exploring death and mortality.",
  "Born in Bristol and raised in Leeds. Studied at Goldsmiths, University of London.",
  "Hirst's provocative works using preserved animals and pharmaceuticals challenged conventional boundaries of art and dominated the contemporary art market.",
  [(1991, "Created The Physical Impossibility of Death in the Mind of Someone Living, a shark in formaldehyde"), (1995, "Won the Turner Prize"), (2007, "Created For the Love of God, a platinum skull covered in diamonds")],
  [("The Physical Impossibility of Death in the Mind of Someone Living", 1991, "Tiger shark preserved in formaldehyde"), ("For the Love of God", 2007, "Platinum cast of a human skull encrusted with 8,601 diamonds")],
  [("I sometimes feel that I have nothing to say and I want to communicate this.", "Attributed")])

add("renee-fleming", "Renée Fleming", "ルネ・フレミング", 1959, None, ["us"], ["art"],
  "Renée Fleming is an American soprano known for her lush, creamy voice and her versatility across opera, concert, and popular music.",
  "Born in Indiana, Pennsylvania. Studied at the Eastman School of Music and the Juilliard School.",
  "Fleming's artistry and crossover appeal have made her one of the most celebrated sopranos of her generation and a cultural ambassador for opera.",
  [(1991, "Won the Metropolitan Opera Auditions"), (2006, "Awarded the National Medal of Arts"), (2014, "Sang the national anthem at Super Bowl XLVIII, a first for an opera singer")],
  [("The Inner Voice", 2004, "Memoir exploring the art of singing and her career")],
  [("Singing is a form of meditation for me.", "Interview")])

add("dian-fossey", "Dian Fossey", "ダイアン・フォッシー", 1932, 1985, ["us"], ["biology"],
  "Dian Fossey was an American primatologist who devoted her life to studying and protecting mountain gorillas in Rwanda.",
  "Born in San Francisco. Worked as an occupational therapist before traveling to Africa, where she was inspired by Louis Leakey to study gorillas.",
  "Fossey's research transformed understanding of gorilla behavior, and her anti-poaching activism drew worldwide attention to the plight of mountain gorillas.",
  [(1967, "Established the Karisoke Research Center in Rwanda's Virunga Mountains"), (1983, "Published Gorillas in the Mist"), (1985, "Murdered at her camp, likely by poachers")],
  [("Gorillas in the Mist", 1983, "Account of her 18 years living with and studying mountain gorillas")],
  [("When you realize the value of all life, you dwell less on what is past and concentrate more on the preservation of the future.", "Gorillas in the Mist")])

add("robert-may", "Robert May", "ロバート・メイ", 1936, 2020, ["au", "gb"], ["biology", "mathematics"],
  "Robert May was an Australian-British theoretical ecologist whose mathematical models transformed the understanding of population dynamics and biodiversity.",
  "Born in Sydney, Australia. Trained as a physicist at the University of Sydney before turning to ecology.",
  "May's work on chaos in ecological systems and his estimates of global biodiversity shaped modern conservation biology and complexity science.",
  [(1976, "Published landmark paper showing simple ecological models can produce chaotic behavior"), (2000, "Became President of the Royal Society"), (2005, "Made a life peer as Baron May of Oxford")],
  [("Stability and Complexity in Model Ecosystems", 1973, "Influential book challenging the assumption that complex ecosystems are inherently stable")],
  [("The more we learn about the natural world, the more extraordinary and complex it turns out to be.", "Attributed")])

add("eo-wilson", "E.O. Wilson", "エドワード・O・ウィルソン", 1929, 2021, ["us"], ["biology"],
  "Edward O. Wilson was an American biologist and naturalist known as the father of sociobiology and a champion of biodiversity conservation.",
  "Born in Birmingham, Alabama. A childhood fishing accident blinded him in one eye, directing his attention to the study of insects.",
  "Wilson's work on sociobiology, island biogeography, and biodiversity made him one of the most influential biologists of the 20th century.",
  [(1975, "Published Sociobiology, sparking intense scientific and public debate"), (1979, "Won his first Pulitzer Prize for On Human Nature"), (1992, "Published The Diversity of Life, a landmark work on biodiversity")],
  [("Sociobiology: The New Synthesis", 1975, "Groundbreaking work applying evolutionary theory to social behavior"), ("The Diversity of Life", 1992, "Major work on biodiversity and the extinction crisis")],
  [("If all mankind were to disappear, the world would regenerate back to the rich state of equilibrium that existed ten thousand years ago.", "The Diversity of Life")])

add("james-lovelock", "James Lovelock", "ジェームズ・ラヴロック", 1919, 2022, ["gb"], ["biology", "chemistry"],
  "James Lovelock was a British independent scientist who proposed the Gaia hypothesis, viewing Earth as a self-regulating system.",
  "Born in Letchworth Garden City. Studied chemistry and medicine at the University of Manchester and the London School of Hygiene.",
  "The Gaia hypothesis fundamentally changed how scientists and the public think about the Earth as an interconnected living system.",
  [(1965, "Invented the electron capture detector, crucial for detecting CFCs in the atmosphere"), (1979, "Published Gaia: A New Look at Life on Earth"), (2022, "Died on his 103rd birthday")],
  [("Gaia: A New Look at Life on Earth", 1979, "Book proposing that Earth functions as a self-regulating organism")],
  [("The Earth is not just a ball of rock; it's a living system.", "Attributed")])

add("dorothy-hodgkin", "Dorothy Crowfoot Hodgkin", "ドロシー・ホジキン", 1910, 1994, ["gb"], ["chemistry"],
  "Dorothy Hodgkin was a British chemist who advanced X-ray crystallography to determine the structures of important biochemical substances.",
  "Born in Cairo, Egypt, to British parents. Studied chemistry at Oxford and Cambridge.",
  "Hodgkin's determination of the structures of penicillin, vitamin B12, and insulin was crucial to modern biochemistry and pharmacology.",
  [(1945, "Determined the structure of penicillin"), (1956, "Determined the structure of vitamin B12"), (1964, "Awarded Nobel Prize in Chemistry")],
  [("The X-ray Analysis of Complicated Molecules", 1964, "Nobel Lecture describing her crystallographic work")],
  [("I was captured for life by chemistry and by crystals.", "Attributed")])

if __name__ == "__main__":
    write_people(P)
