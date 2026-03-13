#!/usr/bin/env python3
"""Supplement batch 2: more people across all categories."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# === MORE WRITERS ===
p("marcel-proust", "Marcel Proust", "マルセル・プルースト", 1871, 1922, ["fr"], ["literature"],
  "Marcel Proust was a French novelist best known for his monumental In Search of Lost Time, one of the longest and most acclaimed novels in world literature.",
  "Proust was born in Auteuil, Paris. He suffered from asthma throughout his life and spent his later years in a cork-lined room writing his masterpiece.",
  "Proust's exploration of memory, time, and consciousness in In Search of Lost Time transformed the modern novel and influenced all subsequent literary fiction.",
  [(1896, "Published Pleasures and Days"), (1913, "Published Swann's Way"), (1919, "Won Prix Goncourt"), (1922, "Died before completing final volumes")],
  [("In Search of Lost Time", 1913, "Seven-volume novel exploring memory, art, and society")],
  [("The real voyage of discovery consists not in seeking new landscapes, but in having new eyes.", "In Search of Lost Time")])

p("fyodor-dostoevsky", "Fyodor Dostoevsky", "フョードル・ドストエフスキー", 1821, 1881, ["ru"], ["literature"],
  "Fyodor Dostoevsky was a Russian novelist and philosopher whose psychological insight into the dark sides of human nature influenced modern literature and existentialism.",
  "Dostoevsky was born in Moscow. He was sentenced to death for revolutionary activities but reprieved at the last moment and sent to a Siberian prison camp.",
  "Dostoevsky's novels explore the depths of human psychology, morality, and suffering. His influence extends to literature, philosophy, psychology, and theology.",
  [(1846, "Published Poor Folk"), (1849, "Arrested and sentenced to penal servitude"), (1866, "Published Crime and Punishment"), (1880, "Published The Brothers Karamazov")],
  [("Crime and Punishment", 1866, "Novel about guilt and redemption"), ("The Brothers Karamazov", 1880, "Philosophical novel about faith, doubt, and morality")],
  [("The soul is healed by being with children.", "The Idiot")])

p("herman-melville", "Herman Melville", "ハーマン・メルヴィル", 1819, 1891, ["us"], ["literature"],
  "Herman Melville was an American novelist and poet best known for Moby-Dick, one of the great masterpieces of American literature.",
  "Melville was born in New York City. He went to sea as a young man, experiences that inspired his novels of adventure and the sea.",
  "Moby-Dick was underappreciated in Melville's lifetime but is now recognized as one of the greatest novels ever written, exploring obsession, fate, and the nature of evil.",
  [(1846, "Published Typee"), (1851, "Published Moby-Dick"), (1856, "Published The Piazza Tales"), (1891, "Billy Budd published posthumously")],
  [("Moby-Dick", 1851, "Epic novel of Captain Ahab's obsessive pursuit of the white whale"), ("Bartleby, the Scrivener", 1853, "Short story about a clerk who refuses to work")],
  [("It is better to fail in originality than to succeed in imitation.", "Attributed")])

p("mark-twain", "Mark Twain", "マーク・トウェイン", 1835, 1910, ["us"], ["literature"],
  "Mark Twain was an American writer, humorist, and lecturer widely considered the greatest American humorist and the father of American literature.",
  "Born Samuel Clemens in Florida, Missouri, he grew up in Hannibal on the Mississippi River. He worked as a riverboat pilot, miner, and journalist before becoming a writer.",
  "Twain's The Adventures of Huckleberry Finn is considered the Great American Novel. His wit, social criticism, and ear for American speech transformed American literature.",
  [(1865, "Published The Celebrated Jumping Frog of Calaveras County"), (1876, "Published The Adventures of Tom Sawyer"), (1884, "Published Adventures of Huckleberry Finn")],
  [("Adventures of Huckleberry Finn", 1884, "Novel that Hemingway called the source of all American literature"), ("The Adventures of Tom Sawyer", 1876, "Classic novel of boyhood in small-town America")],
  [("The secret of getting ahead is getting started.", "Attributed")])

p("jane-austen", "Jane Austen", "ジェーン・オースティン", 1775, 1817, ["gb"], ["literature"],
  "Jane Austen was an English novelist known for her sharp social commentary and masterful portrayals of the British landed gentry in the Regency era.",
  "Austen was born in Steventon, Hampshire. She was educated by her father and began writing as a teenager, though her novels were published anonymously.",
  "Austen's novels combine wit, social observation, and psychological depth in ways that continue to resonate. Pride and Prejudice remains one of the most popular novels in English.",
  [(1811, "Published Sense and Sensibility"), (1813, "Published Pride and Prejudice"), (1815, "Published Emma"), (1817, "Died at age 41; Persuasion published posthumously")],
  [("Pride and Prejudice", 1813, "Novel about love and social class in Georgian England"), ("Emma", 1815, "Comic novel about a misguided matchmaker")],
  [("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.", "Pride and Prejudice")])

p("charles-dickens", "Charles Dickens", "チャールズ・ディケンズ", 1812, 1870, ["gb"], ["literature"],
  "Charles Dickens was an English writer and social critic who created some of the world's best-known fictional characters and is regarded as the greatest novelist of the Victorian era.",
  "Dickens was born in Portsmouth, England. After his father's imprisonment for debt, young Charles was sent to work in a blacking factory, an experience that shaped his social consciousness.",
  "Dickens's novels exposed social injustice and created enduring characters that have become part of Western culture. His works drove social reform in Victorian England.",
  [(1836, "Published The Pickwick Papers"), (1843, "Published A Christmas Carol"), (1850, "Published David Copperfield"), (1861, "Published Great Expectations")],
  [("A Christmas Carol", 1843, "Novella that transformed Christmas celebrations"), ("Great Expectations", 1861, "Novel about ambition, class, and moral growth")],
  [("It was the best of times, it was the worst of times.", "A Tale of Two Cities")])

p("emily-bronte", "Emily Brontë", "エミリー・ブロンテ", 1818, 1848, ["gb"], ["literature"],
  "Emily Brontë was an English novelist and poet who is best known for her only novel, Wuthering Heights, considered a classic of English literature.",
  "Brontë was born in Thornton, Yorkshire. She grew up on the Yorkshire moors with her siblings, creating an imaginary world that nourished her literary imagination.",
  "Wuthering Heights, with its passionate intensity and innovative structure, was ahead of its time and is now recognized as one of the greatest novels in the English language.",
  [(1846, "Published poems under the pseudonym Ellis Bell"), (1847, "Published Wuthering Heights"), (1848, "Died of tuberculosis at age 30")],
  [("Wuthering Heights", 1847, "Novel of passionate love and revenge on the Yorkshire moors")],
  [("Whatever our souls are made of, his and mine are the same.", "Wuthering Heights")])

p("oscar-wilde", "Oscar Wilde", "オスカー・ワイルド", 1854, 1900, ["ie", "gb"], ["literature"],
  "Oscar Wilde was an Irish poet and playwright who became one of the most popular writers of his era, known for his wit, flamboyant style, and tragic downfall.",
  "Wilde was born in Dublin, Ireland. He studied at Trinity College Dublin and Oxford, becoming famous for his wit and aesthetic philosophy.",
  "Wilde's plays, particularly The Importance of Being Earnest, are masterpieces of comic drama. His novel The Picture of Dorian Gray explores vanity and moral corruption.",
  [(1882, "Lecture tour in America"), (1890, "Published The Picture of Dorian Gray"), (1895, "Premiered The Importance of Being Earnest"), (1895, "Imprisoned for gross indecency")],
  [("The Importance of Being Earnest", 1895, "Comedy of manners satirizing Victorian society"), ("The Picture of Dorian Gray", 1890, "Novel about a portrait that ages while its subject remains young")],
  [("Be yourself; everyone else is already taken.", "Attributed")])

p("albert-camus", "Albert Camus", "アルベール・カミュ", 1913, 1960, ["fr", "dz"], ["literature", "philosophy"],
  "Albert Camus was a French-Algerian philosopher and author who won the Nobel Prize in Literature, known for his philosophy of the absurd.",
  "Camus was born in Mondovi, French Algeria. He grew up in poverty, studied philosophy in Algiers, and became a journalist and writer in Paris.",
  "Camus's philosophy of the absurd and his literary works exploring meaning, rebellion, and solidarity made him one of the most important thinkers of the 20th century.",
  [(1942, "Published The Stranger and The Myth of Sisyphus"), (1947, "Published The Plague"), (1951, "Published The Rebel"), (1957, "Awarded Nobel Prize in Literature")],
  [("The Stranger", 1942, "Novel about a man indifferent to his mother's death and his own murder trial"), ("The Myth of Sisyphus", 1942, "Philosophical essay on the absurd")],
  [("One must imagine Sisyphus happy.", "The Myth of Sisyphus")])

p("rabindranath-tagore", "Rabindranath Tagore", "ラビンドラナート・タゴール", 1861, 1941, ["in"], ["literature"],
  "Rabindranath Tagore was an Indian poet, musician, and artist who was the first non-European to win the Nobel Prize in Literature.",
  "Tagore was born in Calcutta into a prominent Bengali family. He began writing poetry as a child and became a towering figure in Bengali and Indian culture.",
  "Tagore's poems, songs, and novels shaped modern Bengali literature and Indian culture. He wrote the national anthems of both India and Bangladesh.",
  [(1877, "Published first poems"), (1901, "Founded Santiniketan school"), (1912, "Published English Gitanjali"), (1913, "Awarded Nobel Prize in Literature")],
  [("Gitanjali", 1912, "Collection of spiritual poems that won the Nobel Prize"), ("The Home and the World", 1916, "Novel about nationalism and personal relationships")],
  [("Where the mind is without fear and the head is held high.", "Gitanjali")])

p("lu-xun", "Lu Xun", "魯迅", 1881, 1936, ["cn"], ["literature"],
  "Lu Xun was a Chinese writer, essayist, and critic considered the founder of modern Chinese literature.",
  "Lu Xun was born in Shaoxing, Zhejiang. He studied medicine in Japan but turned to literature, believing that changing the spirit of the Chinese people was more important than treating their bodies.",
  "Lu Xun's stories and essays attacked traditional Chinese culture and inspired the May Fourth Movement. He is regarded as the father of modern Chinese literature.",
  [(1918, "Published A Madman's Diary, first modern Chinese short story"), (1921, "Published The True Story of Ah Q"), (1923, "Published Call to Arms")],
  [("A Madman's Diary", 1918, "First modern Chinese short story, critiquing traditional Confucian culture"), ("The True Story of Ah Q", 1921, "Satirical novella about a peasant's delusions")],
  [("Hope is like a path in the countryside. Originally, there is nothing — but as people walk this way again and again, a path appears.", "My Old Home")])

p("chinua-achebe", "Chinua Achebe", "チヌア・アチェベ", 1930, 2013, ["ng"], ["literature"],
  "Chinua Achebe was a Nigerian novelist, poet, and critic who is considered the father of modern African literature.",
  "Achebe was born in Ogidi, Nigeria. He studied at University College Ibadan and worked for the Nigerian Broadcasting Service before devoting himself to writing.",
  "Achebe's Things Fall Apart, translated into over 50 languages, gave voice to African experience and challenged Western narratives about Africa, transforming world literature.",
  [(1958, "Published Things Fall Apart"), (1960, "Published No Longer at Ease"), (1966, "Published A Man of the People"), (2007, "Awarded Man Booker International Prize")],
  [("Things Fall Apart", 1958, "Novel about the impact of colonialism on Igbo culture"), ("Arrow of God", 1964, "Novel about a priest caught between tradition and colonial rule")],
  [("Until the lions have their own historians, the history of the hunt will always glorify the hunter.", "Attributed")])

# === MORE ARTISTS ===
p("henri-de-toulouse-lautrec", "Henri de Toulouse-Lautrec", "アンリ・ド・トゥールーズ＝ロートレック", 1864, 1901, ["fr"], ["art"],
  "Henri de Toulouse-Lautrec was a French painter, printmaker, draughtsman, and illustrator whose art depicted the colorful and theatrical life of Paris.",
  "Toulouse-Lautrec was born into an aristocratic family but suffered from a genetic condition that stunted his legs. He immersed himself in the bohemian nightlife of Montmartre.",
  "Toulouse-Lautrec's posters and paintings of Parisian nightlife elevated the poster to an art form and captured the spirit of Belle Époque Paris.",
  [(1882, "Moved to Montmartre, Paris"), (1891, "Created famous Moulin Rouge poster"), (1893, "Exhibited at major Paris galleries")],
  [("Moulin Rouge: La Goulue", 1891, "Iconic poster that established the artistic poster"), ("At the Moulin Rouge", 1892, "Painting capturing the atmosphere of the famous nightclub")],
  [("I paint things as they are. I don't comment.", "Attributed")])

p("kazimir-malevich", "Kazimir Malevich", "カジミール・マレーヴィチ", 1879, 1935, ["ua", "ru"], ["art"],
  "Kazimir Malevich was a Russian avant-garde artist and art theorist who pioneered geometric abstract art and founded Suprematism.",
  "Malevich was born in Kiev, Ukraine. He studied at the Kiev School of Art and the Moscow School of Painting, evolving through Impressionism, Cubism, and Futurism.",
  "Malevich's Black Square and Suprematist compositions reduced art to pure geometric abstraction, influencing all subsequent abstract and minimalist art.",
  [(1913, "Designed Futurist opera Victory Over the Sun"), (1915, "Exhibited Black Square; founded Suprematism"), (1927, "Traveled to the Bauhaus"), (1935, "Died in Leningrad")],
  [("Black Square", 1915, "Iconic painting that inaugurated geometric abstraction"), ("Suprematist Composition: White on White", 1918, "Painting pushing abstraction to its extreme")],
  [("I have transformed myself in the zero of form and dragged myself out of the rubbish-filled pool of academic art.", "From Cubism and Futurism to Suprematism")])

p("faith-ringgold", "Faith Ringgold", "フェイス・リングゴールド", 1930, 2024, ["us"], ["art"],
  "Faith Ringgold was an American artist, author, and activist best known for her painted story quilts that addressed race, gender, and American identity.",
  "Ringgold was born in Harlem, New York. She studied at City College of New York and became a teacher and artist, developing her unique story quilt form.",
  "Ringgold's story quilts combined painting, quilting, and storytelling to address African American experience, feminism, and social justice, bridging fine art and craft traditions.",
  [(1963, "Began American People series"), (1970, "Cofounded Women Students and Artists for Black Art Liberation"), (1983, "Created first story quilt, Who's Afraid of Aunt Jemima?"), (1991, "Published Tar Beach children's book")],
  [("Tar Beach", 1988, "Story quilt that became a celebrated children's book"), ("Who's Afraid of Aunt Jemima?", 1983, "First story quilt addressing racial stereotypes")],
  [("Anyone can fly. All you need is somewhere to go that you can't get to any other way.", "Tar Beach")])

# === MORE BIOLOGISTS ===
p("charles-lyell", "Charles Lyell", "チャールズ・ライエル", 1797, 1875, ["gb"], ["biology"],
  "Charles Lyell was a British geologist whose Principles of Geology influenced Darwin's thinking and established uniformitarianism as the basis of geology.",
  "Lyell was born in Kinnordy, Scotland. He studied law but turned to geology, traveling extensively across Europe and North America to study rock formations.",
  "Lyell's principle that present geological processes explain the past — uniformitarianism — provided the deep time framework essential for Darwin's theory of evolution.",
  [(1830, "Published first volume of Principles of Geology"), (1838, "Published Elements of Geology"), (1863, "Published The Geological Evidences of the Antiquity of Man")],
  [("Principles of Geology", 1830, "Established uniformitarianism and deep geological time")],
  [("The present is the key to the past.", "Principles of Geology")])

p("alfred-kinsey", "Alfred Kinsey", "アルフレッド・キンゼイ", 1894, 1956, ["us"], ["biology"],
  "Alfred Kinsey was an American biologist and professor of entomology and zoology who founded the Institute for Sex Research at Indiana University.",
  "Kinsey was born in Hoboken, New Jersey. He studied biology at Bowdoin College and Harvard, first specializing in gall wasps before turning to human sexuality.",
  "Kinsey's research on human sexual behavior, published as the Kinsey Reports, was among the most influential scientific studies of the 20th century, changing social attitudes.",
  [(1938, "Began teaching course on marriage"), (1947, "Founded the Institute for Sex Research"), (1948, "Published Sexual Behavior in the Human Male"), (1953, "Published Sexual Behavior in the Human Female")],
  [("Sexual Behavior in the Human Male", 1948, "Groundbreaking study of male sexual behavior")],
  [("The only unnatural sex act is that which you cannot perform.", "Attributed")])

p("louis-leakey", "Louis Leakey", "ルイス・リーキー", 1903, 1972, ["ke", "gb"], ["biology"],
  "Louis Leakey was a British-Kenyan paleoanthropologist who, with his wife Mary, made landmark fossil discoveries in East Africa that demonstrated human evolution.",
  "Leakey was born in Kabete, Kenya, to British missionary parents. He studied at Cambridge and devoted his life to searching for human ancestors in East Africa.",
  "The Leakeys' fossil discoveries at Olduvai Gorge proved that humans evolved in Africa, not Asia as previously believed, transforming paleoanthropology.",
  [(1931, "Began excavations at Olduvai Gorge"), (1959, "Mary Leakey discovered Zinjanthropus"), (1960, "Discovered Homo habilis"), (1967, "Supported Goodall, Fossey, and Galdikas")],
  [("Olduvai Gorge Excavations", 1959, "Fossil discoveries proving human origins in Africa")],
  [("Nothing that I have done or shall do will be as important as the discoveries that Jane, Dian, and Biruté will make.", "Attributed")])

# === MORE MUSICIANS ===
p("hildegard-von-bingen", "Hildegard von Bingen", "ヒルデガルト・フォン・ビンゲン", 1098, 1179, ["de"], ["art", "philosophy"],
  "Hildegard von Bingen was a German Benedictine abbess, writer, composer, and polymath, one of the most remarkable women of the medieval period.",
  "Hildegard was born in Bermersheim, Germany. She entered a Benedictine monastery at age eight and experienced visions from childhood that she later recorded in writing.",
  "Hildegard's musical compositions, theological writings, and scientific observations made her one of the most extraordinary minds of the Middle Ages and an early feminist icon.",
  [(1136, "Became abbess of her community"), (1141, "Began writing Scivias"), (1150, "Founded the monastery at Rupertsberg"), (1170, "Completed Liber Divinorum Operum")],
  [("Scivias", 1151, "Visionary theological work with remarkable illustrations"), ("Ordo Virtutum", 1151, "One of the earliest known morality plays, set to music")],
  [("The soul is symphonic.", "Attributed")])

p("fela-kuti", "Fela Kuti", "フェラ・クティ", 1938, 1997, ["ng"], ["art"],
  "Fela Kuti was a Nigerian multi-instrumentalist, musician, composer, and political activist who pioneered Afrobeat, fusing traditional Yoruba music with jazz and funk.",
  "Kuti was born in Abeokuta, Nigeria. He studied at the Trinity College of Music in London before returning to Nigeria to create his unique musical style.",
  "Kuti's Afrobeat combined musical innovation with political protest against military dictatorship and corruption. His influence on African and world music is immeasurable.",
  [(1969, "Visited the United States; politicized by Black Power movement"), (1970, "Founded the Afrika Shrine nightclub"), (1977, "Released Zombie album"), (1979, "Founded Movement of the People party")],
  [("Zombie", 1977, "Album criticizing the Nigerian military that provoked a violent government response"), ("Expensive Shit", 1975, "Album recounting his conflict with the Nigerian military")],
  [("Music is the weapon of the future.", "Attributed")])

p("umm-kulthum", "Umm Kulthum", "ウンム・クルスーム", 1904, 1975, ["eg"], ["art"],
  "Umm Kulthum was an Egyptian singer, songwriter, and actress who is considered the most famous and distinguished singer in the history of Arabic music.",
  "Umm Kulthum was born in a small village in the Nile Delta. She began performing as a child, disguised as a boy, and moved to Cairo to pursue her career.",
  "Umm Kulthum's powerful voice and emotional performances made her the most beloved cultural figure in the Arab world. Her monthly radio concerts united millions of listeners.",
  [(1923, "Moved to Cairo"), (1926, "First commercial recordings"), (1934, "Began monthly radio concerts"), (1967, "Performed to raise funds after the Six-Day War")],
  [("Enta Omri", 1964, "Song considered one of the greatest in Arabic music"), ("Al-Atlal", 1966, "Epic poem set to music, a landmark of Arabic vocal art")],
  [("I chose songs that would live and remain after me.", "Attributed")])

p("ravi-shankar", "Ravi Shankar", "ラヴィ・シャンカル", 1920, 2012, ["in"], ["art"],
  "Ravi Shankar was an Indian sitar virtuoso and composer who brought Indian classical music to the Western world.",
  "Shankar was born in Varanasi, India. He studied under the great musician Allauddin Khan and became the world's most well-known Indian musician.",
  "Shankar's collaborations with George Harrison and his performances at major Western music festivals introduced Indian classical music to a global audience.",
  [(1956, "First concert tours to Europe and America"), (1966, "Befriended George Harrison"), (1967, "Performed at Monterey Pop Festival"), (1971, "Organized Concert for Bangladesh")],
  [("Concert for Bangladesh", 1971, "Landmark charity concert that set the model for benefit concerts"), ("Raga", 1971, "Documentary film about Indian music and his life")],
  [("If I've accomplished anything, it has been to make people aware of the beauty of our music.", "Attributed")])

# === MORE CHEMISTS ===
p("dmitri-mendeleev-student", "Alexander Fleming's contemporary Gertrude Elion", "ガートルード・エリオン", 1918, 1999, ["us"], ["chemistry", "biology"],
  "Gertrude Elion was an American pharmacologist and biochemist who shared the Nobel Prize for pioneering a rational approach to drug development.",
  "Elion was born in New York City. She was inspired to study chemistry after her grandfather died of cancer. She joined Burroughs Wellcome despite having no PhD.",
  "Elion's rational drug design approach produced medications for leukemia, herpes, malaria, gout, and HIV/AIDS, saving millions of lives and transforming pharmacology.",
  [(1950, "Developed first treatment for childhood leukemia"), (1957, "Developed azathioprine for organ transplants"), (1977, "Developed acyclovir for herpes"), (1988, "Awarded Nobel Prize in Physiology or Medicine")],
  [("Rational Drug Design", 1950, "Approach to developing drugs based on understanding biochemical mechanisms")],
  [("Don't be afraid of hard work. Nothing worthwhile comes easily.", "Attributed")])

p("fritz-haber-student", "Carl Djerassi", "カール・ジェラッシ", 1923, 2015, ["at", "us"], ["chemistry"],
  "Carl Djerassi was an Austrian-American chemist and author who is best known as the father of the birth control pill.",
  "Djerassi was born in Vienna. His family fled the Nazis and he studied at Kenyon College and the University of Wisconsin before working at Syntex in Mexico City.",
  "Djerassi's synthesis of norethindrone, the active ingredient in the first oral contraceptive pill, was one of the most socially transformative scientific achievements of the 20th century.",
  [(1951, "Synthesized norethindrone, the first oral contraceptive"), (1952, "Synthesized cortisone from plant sources"), (1959, "First oral contraceptive approved"), (1992, "Began writing novels and plays")],
  [("Norethindrone", 1951, "Synthesis of the active ingredient in the first birth control pill")],
  [("The Pill gave women the freedom to plan their lives.", "Attributed")])

# === MORE POLITICAL FIGURES ===
p("rosa-parks", "Rosa Parks", "ローザ・パークス", 1913, 2005, ["us"], ["politics"],
  "Rosa Parks was an American activist in the civil rights movement best known for her pivotal role in the Montgomery bus boycott.",
  "Parks was born in Tuskegee, Alabama. She worked as a seamstress and served as secretary of the Montgomery NAACP before her famous act of resistance.",
  "Parks's refusal to give up her bus seat to a white man sparked the Montgomery bus boycott, a landmark event in the American civil rights movement.",
  [(1943, "Became secretary of Montgomery NAACP"), (1955, "Refused to give up bus seat; arrested"), (1955, "Montgomery bus boycott began"), (1996, "Awarded Presidential Medal of Freedom")],
  [("Montgomery Bus Boycott", 1955, "381-day boycott that desegregated Montgomery's bus system")],
  [("I have learned over the years that when one's mind is made up, this diminishes fear.", "Quiet Strength")])

p("desmond-tutu", "Desmond Tutu", "デズモンド・ツツ", 1931, 2021, ["za"], ["politics"],
  "Desmond Tutu was a South African Anglican cleric and theologian who was a leading voice against apartheid and won the Nobel Peace Prize.",
  "Tutu was born in Klerksdorp, South Africa. He was ordained as an Anglican priest and became the first Black Archbishop of Cape Town.",
  "Tutu's moral leadership during the anti-apartheid struggle and his chairmanship of the Truth and Reconciliation Commission helped South Africa's peaceful transition.",
  [(1978, "Became first Black general secretary of the South African Council of Churches"), (1984, "Awarded Nobel Peace Prize"), (1986, "Became Archbishop of Cape Town"), (1996, "Chaired Truth and Reconciliation Commission")],
  [("Truth and Reconciliation Commission", 1996, "Body that investigated apartheid-era human rights abuses")],
  [("If you are neutral in situations of injustice, you have chosen the side of the oppressor.", "Attributed")])

p("dalai-lama-14", "14th Dalai Lama", "ダライ・ラマ14世", 1935, None, ["cn"], ["politics", "philosophy"],
  "The 14th Dalai Lama, Tenzin Gyatso, is the spiritual leader of Tibetan Buddhism who has advocated for Tibetan autonomy and promoted nonviolence, winning the Nobel Peace Prize.",
  "He was born Lhamo Thondup in Taktser, Tibet. He was recognized as the reincarnation of the Dalai Lama at age two and enthroned at age four.",
  "The Dalai Lama's advocacy for Tibetan rights through nonviolent means and his promotion of interfaith dialogue and compassion have made him a global moral authority.",
  [(1950, "Assumed political power after Chinese invasion"), (1959, "Fled Tibet to India"), (1989, "Awarded Nobel Peace Prize"), (2011, "Devolved political authority to elected leadership")],
  [("The Art of Happiness", 1998, "Book exploring the basis of happiness from Buddhist and secular perspectives")],
  [("Be kind whenever possible. It is always possible.", "Attributed")])

# === MORE ENGINEERS ===
p("alan-kay", "Alan Kay", "アラン・ケイ", 1940, None, ["us"], ["engineering"],
  "Alan Kay is an American computer scientist known for his pioneering work on object-oriented programming, personal computing, and graphical user interfaces.",
  "Kay was born in Springfield, Massachusetts. He studied at the University of Colorado and the University of Utah before joining Xerox PARC.",
  "Kay's vision of the Dynabook — a personal computer for children — and his development of Smalltalk helped shape the personal computer revolution.",
  [(1968, "Conceived the Dynabook concept"), (1971, "Joined Xerox PARC"), (1972, "Developed Smalltalk programming language"), (2003, "Awarded Turing Award")],
  [("Smalltalk", 1972, "Pioneering object-oriented programming language")],
  [("The best way to predict the future is to invent it.", "Attributed")])

p("vint-cerf", "Vint Cerf", "ヴィント・サーフ", 1943, None, ["us"], ["engineering"],
  "Vint Cerf is an American internet pioneer who is recognized as one of the fathers of the Internet for co-designing the TCP/IP protocols.",
  "Cerf was born in New Haven, Connecticut. He studied at Stanford and UCLA, where he worked on the ARPANET project that evolved into the Internet.",
  "Cerf's co-design of TCP/IP provided the fundamental architecture of the Internet, enabling global digital communication.",
  [(1974, "Co-designed TCP/IP with Bob Kahn"), (1982, "TCP/IP adopted as Internet standard"), (1992, "Co-founded the Internet Society"), (2004, "Awarded Turing Award with Kahn")],
  [("A Protocol for Packet Network Intercommunication", 1974, "Paper describing TCP/IP, the foundational Internet protocol")],
  [("The Internet is a reflection of our society, and that mirror is going to be that way.", "Attributed")])

p("linus-torvalds", "Linus Torvalds", "リーナス・トーバルズ", 1969, None, ["fi", "us"], ["engineering"],
  "Linus Torvalds is a Finnish-American software engineer who created the Linux kernel, the foundation of the Linux operating system.",
  "Torvalds was born in Helsinki, Finland. He studied computer science at the University of Helsinki, where he created Linux as a student project.",
  "The Linux kernel powers the majority of the world's servers, supercomputers, smartphones (via Android), and embedded systems, making it one of the most important software projects in history.",
  [(1991, "Released first version of the Linux kernel"), (1994, "Linux 1.0 released"), (2002, "Released BitKeeper for Linux development"), (2005, "Created Git version control system")],
  [("Linux Kernel", 1991, "Open-source operating system kernel powering most of the world's infrastructure")],
  [("Talk is cheap. Show me the code.", "Email to Linux kernel mailing list")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'dmitri-mendeleev-student':
            entry['id'] = 'gertrude-elion'
        elif entry['id'] == 'fritz-haber-student':
            entry['id'] = 'carl-djerassi'
    write_people(P)
