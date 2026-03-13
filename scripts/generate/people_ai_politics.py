#!/usr/bin/env python3
"""Generate ~100 political leaders and thinkers."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

p("alexander-the-great", "Alexander the Great", "アレクサンドロス大王", -356, -323, ["gr"], ["politics"],
  "Alexander the Great was a king of Macedonia who created one of the largest empires in ancient history, stretching from Greece to northwestern India.",
  "Alexander was born in Pella, Macedonia. He was tutored by Aristotle and ascended to the throne at age 20 after his father Philip II's assassination.",
  "Alexander's conquests spread Greek culture across a vast empire, initiating the Hellenistic period and transforming the cultural landscape of the ancient world.",
  [(-334, "Began invasion of the Persian Empire"), (-331, "Defeated Darius III at the Battle of Gaugamela"), (-326, "Reached India"), (-323, "Died in Babylon")],
  [("Conquests of the Persian Empire", -331, "Military campaigns that created the largest empire the ancient world had seen")],
  [("There is nothing impossible to him who will try.", "Attributed")])

p("julius-caesar", "Julius Caesar", "ガイウス・ユリウス・カエサル", -100, -44, ["it"], ["politics"],
  "Julius Caesar was a Roman military general, statesman, and dictator who played a critical role in the transformation of the Roman Republic into the Roman Empire.",
  "Caesar was born into a patrician family in Rome. He rose through the Roman political ranks through military success, oratory, and political alliances.",
  "Caesar's military conquests expanded Roman territory, and his political reforms transformed the Republic. His assassination triggered civil wars that led to the rise of the Roman Empire.",
  [(-58, "Began conquest of Gaul"), (-49, "Crossed the Rubicon, starting civil war"), (-46, "Became dictator of Rome"), (-44, "Assassinated on the Ides of March")],
  [("Commentarii de Bello Gallico", -50, "Account of the Gallic Wars written by Caesar himself")],
  [("Veni, vidi, vici. (I came, I saw, I conquered.)", "Letter to the Roman Senate")])

p("augustus-caesar", "Augustus", "アウグストゥス", -63, 14, ["it"], ["politics"],
  "Augustus was the first Roman emperor, founding the Roman Principate and transforming the Republic into an empire that would endure for centuries.",
  "Born Gaius Octavius in Rome, he was adopted by Julius Caesar and became his heir. After defeating rivals Mark Antony and Cleopatra, he became the undisputed ruler of Rome.",
  "Augustus established the Pax Romana, a period of relative peace and stability lasting over 200 years. He reformed administration, built infrastructure, and transformed Rome.",
  [(-44, "Adopted as Caesar's heir"), (-31, "Defeated Antony and Cleopatra at Actium"), (-27, "Became first Roman Emperor"), (14, "Died after 40 years of rule")],
  [("Res Gestae Divi Augusti", 14, "Autobiography of Augustus's achievements inscribed on bronze tablets")],
  [("I found Rome a city of bricks and left it a city of marble.", "Attributed by Suetonius")])

p("genghis-khan", "Genghis Khan", "チンギス・カン", 1162, 1227, ["mn"], ["politics"],
  "Genghis Khan was the founder and first ruler of the Mongol Empire, which became the largest contiguous land empire in history.",
  "Born as Temüjin in the Mongolian steppe, he grew up in harsh conditions. Through alliances and military genius, he united the Mongol tribes under his rule.",
  "Genghis Khan's empire connected East and West through trade and communication, establishing the Pax Mongolica. His legal code, the Yassa, influenced governance across Asia.",
  [(1206, "Proclaimed Genghis Khan, uniting the Mongols"), (1215, "Conquered Beijing"), (1219, "Invaded the Khwarezmian Empire"), (1227, "Died during campaign in China")],
  [("The Yassa", 1206, "Legal code governing the Mongol Empire")],
  [("The greatest happiness is to vanquish your enemies and chase them before you.", "The Secret History of the Mongols")])

p("qin-shi-huang", "Qin Shi Huang", "始皇帝", -259, -210, ["cn"], ["politics"],
  "Qin Shi Huang was the first emperor of a unified China, founding the Qin dynasty and establishing the imperial system that lasted over two millennia.",
  "Born as Ying Zheng, he became king of Qin at age 13. Through military campaigns and political strategy, he conquered all rival states to unify China.",
  "Qin Shi Huang unified China's writing, currency, and measurements, built the first Great Wall, and established a centralized bureaucratic system that shaped Chinese governance for centuries.",
  [(-246, "Became king of Qin"), (-221, "Unified China and became First Emperor"), (-214, "Began construction of the Great Wall"), (-210, "Died and was buried with the Terracotta Army")],
  [("Unification of China", -221, "Unification of seven warring states into a single empire")],
  [("I have collected all the writings of the Empire and burnt those which were of no use.", "Attributed by Sima Qian")])

p("cleopatra", "Cleopatra VII", "クレオパトラ7世", -69, -30, ["eg"], ["politics"],
  "Cleopatra VII was the last active ruler of the Ptolemaic Kingdom of Egypt, known for her intelligence, political acumen, and alliances with Julius Caesar and Mark Antony.",
  "Cleopatra was born into the Ptolemaic dynasty in Alexandria. She received an extensive education and was the first Ptolemaic ruler to learn the Egyptian language.",
  "Cleopatra was one of the most powerful rulers of her era, maintaining Egyptian independence through diplomacy and alliance. Her story has influenced art and literature for two millennia.",
  [(-51, "Became co-ruler of Egypt"), (-48, "Allied with Julius Caesar"), (-41, "Allied with Mark Antony"), (-30, "Died after defeat at Actium")],
  [("Rule of Egypt", -51, "Maintained Egyptian sovereignty through strategic alliances with Rome")],
  [("I will not be triumphed over.", "Attributed by Plutarch")])

p("napoleon-bonaparte", "Napoleon Bonaparte", "ナポレオン・ボナパルト", 1769, 1821, ["fr"], ["politics"],
  "Napoleon Bonaparte was a French military commander and emperor who conquered much of Europe and enacted wide-ranging legal and administrative reforms.",
  "Napoleon was born in Corsica. He received a military education in France, rose rapidly through the ranks during the French Revolution, and seized power in a coup in 1799.",
  "Napoleon's Napoleonic Code reformed legal systems across Europe and beyond. His military campaigns redrew the map of Europe and spread the ideals of the French Revolution.",
  [(1799, "Seized power in a coup d'état"), (1804, "Crowned himself Emperor"), (1805, "Victory at Austerlitz"), (1815, "Defeated at Waterloo and exiled")],
  [("Napoleonic Code", 1804, "Civil code that became the basis of legal systems in many countries")],
  [("Impossible is a word to be found only in the dictionary of fools.", "Attributed")])

p("mahatma-gandhi", "Mahatma Gandhi", "マハトマ・ガンディー", 1869, 1948, ["in"], ["politics", "philosophy"],
  "Mahatma Gandhi was an Indian lawyer, anti-colonial nationalist, and political ethicist who employed nonviolent resistance to lead India to independence from British rule.",
  "Gandhi was born in Porbandar, India. He studied law in London and practiced in South Africa, where he developed his philosophy of nonviolent resistance against racial discrimination.",
  "Gandhi's philosophy of nonviolent civil disobedience inspired movements for civil rights and freedom worldwide. His methods influenced Martin Luther King Jr., Nelson Mandela, and many others.",
  [(1893, "Began activism in South Africa"), (1915, "Returned to India"), (1930, "Led the Salt March"), (1947, "India gained independence")],
  [("The Story of My Experiments with Truth", 1927, "Gandhi's autobiography describing his spiritual and political development")],
  [("Be the change you wish to see in the world.", "Attributed")])

p("abraham-lincoln", "Abraham Lincoln", "エイブラハム・リンカーン", 1809, 1865, ["us"], ["politics"],
  "Abraham Lincoln was the 16th President of the United States who preserved the Union during the Civil War and abolished slavery through the Emancipation Proclamation.",
  "Lincoln was born in a log cabin in Kentucky. Largely self-educated, he became a lawyer, state legislator, and congressman before winning the presidency in 1860.",
  "Lincoln preserved the United States as one nation and ended slavery, fundamentally transforming American society. His leadership during the Civil War is widely regarded as exemplary.",
  [(1860, "Elected 16th President"), (1863, "Issued the Emancipation Proclamation"), (1863, "Delivered the Gettysburg Address"), (1865, "Assassinated at Ford's Theatre")],
  [("Gettysburg Address", 1863, "Speech redefining the Civil War as a struggle for equality and democracy"), ("Emancipation Proclamation", 1863, "Executive order freeing enslaved people in Confederate states")],
  [("Government of the people, by the people, for the people, shall not perish from the earth.", "Gettysburg Address")])

p("george-washington", "George Washington", "ジョージ・ワシントン", 1732, 1799, ["us"], ["politics"],
  "George Washington was the first President of the United States and commander-in-chief of the Continental Army during the American Revolution.",
  "Washington was born in Westmoreland County, Virginia, into a planter family. He worked as a surveyor and soldier before leading the Continental Army against the British.",
  "Washington's leadership during the Revolution and his voluntary relinquishment of power after two presidential terms established precedents that define American democracy.",
  [(1775, "Appointed commander of the Continental Army"), (1781, "Won the Battle of Yorktown"), (1789, "Inaugurated as first President"), (1797, "Voluntarily left office after two terms")],
  [("Farewell Address", 1796, "Warning against political factions and foreign entanglements")],
  [("Liberty, when it begins to take root, is a plant of rapid growth.", "Letter, 1788")])

p("thomas-jefferson", "Thomas Jefferson", "トーマス・ジェファーソン", 1743, 1826, ["us"], ["politics", "philosophy"],
  "Thomas Jefferson was an American Founding Father, principal author of the Declaration of Independence, and the third President of the United States.",
  "Jefferson was born in Shadwell, Virginia. He studied at the College of William & Mary and became a lawyer, planter, and leading political figure.",
  "Jefferson's articulation of the ideals of liberty and equality in the Declaration of Independence became foundational texts of democratic governance worldwide.",
  [(1776, "Authored the Declaration of Independence"), (1785, "Served as Minister to France"), (1801, "Became third President"), (1819, "Founded the University of Virginia")],
  [("Declaration of Independence", 1776, "Foundational document of American democracy"), ("Notes on the State of Virginia", 1785, "Comprehensive account of Virginia's geography, society, and politics")],
  [("We hold these truths to be self-evident, that all men are created equal.", "Declaration of Independence")])

p("martin-luther-king-jr", "Martin Luther King Jr.", "マーティン・ルーサー・キング・ジュニア", 1929, 1968, ["us"], ["politics"],
  "Martin Luther King Jr. was an American Baptist minister and activist who became the most visible spokesperson and leader in the American civil rights movement.",
  "King was born in Atlanta, Georgia, into a family of Baptist ministers. He studied at Morehouse College, Crozer Theological Seminary, and Boston University.",
  "King's leadership in the civil rights movement through nonviolent resistance led to landmark legislation including the Civil Rights Act and the Voting Rights Act.",
  [(1955, "Led the Montgomery Bus Boycott"), (1963, "Delivered 'I Have a Dream' speech"), (1964, "Awarded Nobel Peace Prize"), (1968, "Assassinated in Memphis")],
  [("I Have a Dream", 1963, "Historic speech during the March on Washington for civil rights"), ("Letter from Birmingham Jail", 1963, "Influential defense of nonviolent civil disobedience")],
  [("I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.", "I Have a Dream speech")])

p("nelson-mandela", "Nelson Mandela", "ネルソン・マンデラ", 1918, 2013, ["za"], ["politics"],
  "Nelson Mandela was a South African anti-apartheid revolutionary and political leader who served as President of South Africa from 1994 to 1999.",
  "Mandela was born in Mvezo, South Africa. He studied law and became involved in anti-colonial and anti-apartheid activism, co-founding the ANC Youth League.",
  "Mandela's lifelong struggle against apartheid and his reconciliation after 27 years of imprisonment made him a global symbol of justice, peace, and resistance to oppression.",
  [(1944, "Joined the African National Congress"), (1964, "Sentenced to life imprisonment"), (1990, "Released from prison"), (1994, "Elected President of South Africa")],
  [("Long Walk to Freedom", 1994, "Autobiography covering his life from childhood through his presidency")],
  [("It always seems impossible until it's done.", "Attributed")])

p("winston-churchill", "Winston Churchill", "ウィンストン・チャーチル", 1874, 1965, ["gb"], ["politics"],
  "Winston Churchill was a British statesman who served as Prime Minister during World War II, leading Britain through its darkest hours with resolute determination.",
  "Churchill was born at Blenheim Palace into an aristocratic family. He served as a soldier, journalist, and politician, holding many cabinet positions before becoming Prime Minister.",
  "Churchill's wartime leadership inspired British resistance to Nazi Germany. His speeches remain among the most powerful in the English language, and he won the Nobel Prize in Literature.",
  [(1940, "Became Prime Minister"), (1940, "Delivered 'We shall fight on the beaches' speech"), (1945, "Led Britain to victory in WWII"), (1953, "Awarded Nobel Prize in Literature")],
  [("The Second World War", 1948, "Six-volume memoir of the war"), ("A History of the English-Speaking Peoples", 1956, "Four-volume history")],
  [("We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields and in the streets, we shall never surrender.", "Speech to Parliament, 1940")])

p("franklin-d-roosevelt", "Franklin D. Roosevelt", "フランクリン・D・ルーズベルト", 1882, 1945, ["us"], ["politics"],
  "Franklin D. Roosevelt was the 32nd President of the United States who led the country through the Great Depression and most of World War II.",
  "Roosevelt was born into a wealthy New York family. He attended Harvard and Columbia Law School, entered politics, and was struck by polio in 1921 but continued his political career.",
  "FDR's New Deal programs transformed the role of the American federal government, establishing the modern welfare state. His wartime leadership was crucial to Allied victory.",
  [(1933, "Inaugurated as President; began New Deal"), (1935, "Signed Social Security Act"), (1941, "Led U.S. into World War II"), (1945, "Died in office during fourth term")],
  [("New Deal", 1933, "Series of programs and reforms addressing the Great Depression")],
  [("The only thing we have to fear is fear itself.", "First Inaugural Address, 1933")])

p("queen-victoria", "Queen Victoria", "ヴィクトリア女王", 1819, 1901, ["gb"], ["politics"],
  "Queen Victoria was the Queen of the United Kingdom of Great Britain and Ireland and Empress of India whose reign of 63 years was the longest in British history at the time.",
  "Victoria was born at Kensington Palace, London. She became queen at age 18 and married Prince Albert of Saxe-Coburg and Gotha, with whom she had nine children.",
  "The Victorian era saw the expansion of the British Empire, industrialization, and significant social reform. Victoria's reign defined an age of dramatic change.",
  [(1837, "Became Queen at age 18"), (1840, "Married Prince Albert"), (1876, "Became Empress of India"), (1887, "Celebrated Golden Jubilee")],
  [("Victorian Era", 1837, "The period of British history defined by her 63-year reign")],
  [("We are not interested in the possibilities of defeat; they do not exist.", "Attributed")])

p("otto-von-bismarck", "Otto von Bismarck", "オットー・フォン・ビスマルク", 1815, 1898, ["de"], ["politics"],
  "Otto von Bismarck was a Prussian statesman who unified the German states into the German Empire and served as its first Chancellor.",
  "Bismarck was born into a Junker family in Schönhausen, Prussia. He studied law and agriculture before entering politics as a conservative monarchist.",
  "Bismarck's diplomatic and military strategy unified Germany, reshaping the balance of power in Europe. His domestic policies established pioneering social welfare programs.",
  [(1862, "Became Minister President of Prussia"), (1866, "Won Austro-Prussian War"), (1871, "Unified Germany and became Chancellor"), (1883, "Introduced national health insurance")],
  [("German Unification", 1871, "Diplomatic and military achievement creating the German Empire")],
  [("Politics is the art of the possible, the attainable, the art of the next best.", "Interview, 1867")])

p("simon-bolivar", "Simón Bolívar", "シモン・ボリバル", 1783, 1830, ["ve", "co"], ["politics"],
  "Simón Bolívar was a Venezuelan military and political leader who played a key role in the independence of several South American countries from the Spanish Empire.",
  "Bolívar was born in Caracas to a wealthy Creole family. He studied in Europe, where he was influenced by Enlightenment ideas, and returned to lead independence movements.",
  "Bolívar liberated Venezuela, Colombia, Ecuador, Peru, and Bolivia from Spanish rule. Known as 'El Libertador,' he envisioned a united South America.",
  [(1810, "Began revolutionary activities"), (1813, "Named El Libertador"), (1819, "Founded Gran Colombia"), (1824, "Won Battle of Ayacucho, securing independence")],
  [("Letter from Jamaica", 1815, "Political essay outlining his vision for South American independence")],
  [("A people that love freedom will in the end be free.", "Attributed")])

p("elizabeth-i", "Elizabeth I", "エリザベス1世", 1533, 1603, ["gb"], ["politics"],
  "Elizabeth I was Queen of England and Ireland whose 45-year reign is considered a golden age of English history, with the flowering of arts and exploration.",
  "Elizabeth was born at Greenwich Palace, the daughter of Henry VIII and Anne Boleyn. She survived political intrigue and imprisonment before ascending the throne.",
  "The Elizabethan era saw the defeat of the Spanish Armada, the flourishing of Shakespeare and English literature, and the foundation of English colonial enterprise.",
  [(1558, "Became Queen of England"), (1559, "Established the Church of England settlement"), (1588, "Defeated the Spanish Armada"), (1600, "Chartered the East India Company")],
  [("Elizabethan Era", 1558, "A golden age of English culture, exploration, and power")],
  [("I know I have the body of a weak and feeble woman, but I have the heart and stomach of a king.", "Tilbury speech, 1588")])

p("charlemagne", "Charlemagne", "カール大帝", 747, 814, ["fr", "de"], ["politics"],
  "Charlemagne was King of the Franks and Lombards and Emperor of the Romans who united most of Western Europe for the first time since the Roman Empire.",
  "Charlemagne was born into the Carolingian dynasty. He inherited the Frankish kingdom and expanded it through decades of military campaigns across Europe.",
  "Charlemagne's empire united much of Western Europe and sparked the Carolingian Renaissance, reviving learning, culture, and education after centuries of decline.",
  [(768, "Became King of the Franks"), (774, "Conquered the Lombard Kingdom"), (800, "Crowned Emperor by Pope Leo III"), (789, "Established schools throughout the empire")],
  [("Carolingian Renaissance", 789, "Revival of art, culture, and learning sponsored by Charlemagne")],
  [("To have another language is to possess a second soul.", "Attributed")])

p("meiji-emperor", "Emperor Meiji", "明治天皇", 1852, 1912, ["jp"], ["politics"],
  "Emperor Meiji was the 122nd Emperor of Japan whose reign saw Japan transform from a feudal society to a modern industrial power.",
  "Born Prince Mutsuhito in Kyoto, he became emperor at age 14 during a period of national crisis as Japan faced pressure from Western powers.",
  "The Meiji Restoration transformed Japan from a feudal society into a modern nation-state with industry, a constitution, and international influence, all within a single generation.",
  [(1868, "Meiji Restoration began"), (1872, "Established modern education system"), (1889, "Promulgated the Meiji Constitution"), (1905, "Japan won Russo-Japanese War")],
  [("Meiji Constitution", 1889, "Japan's first modern constitution establishing a parliamentary system")],
  [("Knowledge shall be sought throughout the world so as to strengthen the foundations of imperial rule.", "Charter Oath, 1868")])

p("mao-zedong", "Mao Zedong", "毛沢東", 1893, 1976, ["cn"], ["politics"],
  "Mao Zedong was a Chinese communist revolutionary who founded the People's Republic of China and served as Chairman of the Communist Party.",
  "Mao was born in Shaoshan, Hunan, into a peasant family. He became involved in revolutionary politics and led the Communist Party through the Long March and civil war.",
  "Mao unified mainland China and established the PRC, transforming Chinese society. His policies had enormous impact, though the Great Leap Forward and Cultural Revolution caused immense suffering.",
  [(1921, "Co-founded the Chinese Communist Party"), (1934, "Led the Long March"), (1949, "Proclaimed the People's Republic of China"), (1966, "Launched the Cultural Revolution")],
  [("Quotations from Chairman Mao", 1964, "Collection of excerpts from Mao's speeches and writings")],
  [("A revolution is not a dinner party.", "Report on the Hunan Peasant Movement, 1927")])

p("sun-yat-sen", "Sun Yat-sen", "孫文", 1866, 1925, ["cn"], ["politics"],
  "Sun Yat-sen was a Chinese revolutionary and political leader who is considered the father of modern China for his role in overthrowing the Qing dynasty.",
  "Sun was born in Guangdong Province. He received medical training in Hong Kong and became involved in revolutionary activities aimed at overthrowing the Qing dynasty.",
  "Sun Yat-sen's Three Principles of the People — nationalism, democracy, and livelihood — provided the ideological foundation for modern Chinese governance.",
  [(1894, "Founded the Revive China Society"), (1905, "Founded the Tongmenghui"), (1912, "Became provisional President of the Republic of China"), (1924, "Reorganized the Kuomintang")],
  [("The Three Principles of the People", 1924, "Political philosophy for the governance of China")],
  [("The revolution is not yet successful. Comrades, keep striving!", "Final testament")])

p("tokugawa-ieyasu", "Tokugawa Ieyasu", "徳川家康", 1543, 1616, ["jp"], ["politics"],
  "Tokugawa Ieyasu was the founder and first shogun of the Tokugawa shogunate of Japan, which ruled for over 260 years of peace.",
  "Ieyasu was born in Mikawa Province. He spent years as a hostage in his youth but rose to become one of Japan's most powerful warlords through patience and strategy.",
  "Tokugawa Ieyasu unified Japan after centuries of civil war and established the Tokugawa shogunate, bringing over 250 years of peace, stability, and cultural development.",
  [(1600, "Won the Battle of Sekigahara"), (1603, "Became Shogun, establishing the Tokugawa shogunate"), (1615, "Destroyed Osaka Castle, ending opposition")],
  [("Tokugawa Shogunate", 1603, "Establishment of a stable government that ruled Japan for 265 years")],
  [("Life is like unto a long journey with a heavy burden.", "Attributed")])

p("catherine-the-great", "Catherine the Great", "エカチェリーナ2世", 1729, 1796, ["ru", "de"], ["politics"],
  "Catherine the Great was Empress of Russia whose reign is considered the Golden Age of Russia, marked by territorial expansion and cultural development.",
  "Born Princess Sophie of Anhalt-Zerbst in Prussia, she married the future Peter III of Russia and seized power from him in a coup in 1762.",
  "Catherine expanded Russian territory, reformed administration, and promoted Enlightenment ideas. Under her rule, Russia became one of Europe's great powers.",
  [(1762, "Became Empress of Russia"), (1767, "Issued the Nakaz (Instruction) for legal reform"), (1783, "Annexed Crimea"), (1785, "Issued the Charter to the Nobility")],
  [("Nakaz", 1767, "Legislative guideline based on Enlightenment principles for Russian law")],
  [("I shall be an autocrat: that's my trade. And the good Lord will forgive me: that's his.", "Attributed")])

p("ashoka", "Ashoka the Great", "アショーカ王", -304, -232, ["in"], ["politics"],
  "Ashoka was an Indian emperor of the Maurya Dynasty who is considered one of the greatest rulers in history for his embrace of Buddhism and nonviolence.",
  "Ashoka was born into the Maurya dynasty. After a brutal conquest of Kalinga, he renounced violence and embraced Buddhism, transforming his approach to governance.",
  "Ashoka's embrace of dharma and nonviolence after the Kalinga war was unprecedented for a ruler. His rock edicts promoting tolerance and welfare are early examples of human rights.",
  [(-268, "Became Emperor of the Maurya Empire"), (-261, "Conquered Kalinga and embraced Buddhism"), (-250, "Sent Buddhist missionaries across Asia")],
  [("Rock Edicts of Ashoka", -250, "Stone inscriptions promoting dharma, tolerance, and nonviolence")],
  [("All men are my children.", "Rock Edict VI")])

p("cyrus-the-great", "Cyrus the Great", "キュロス2世", -600, -530, ["ir"], ["politics"],
  "Cyrus the Great was the founder of the Achaemenid Empire, the first Persian Empire, and is known for his respect for the customs and religions of conquered peoples.",
  "Cyrus was born in Anshan, Persia. He united the Persian and Median tribes and embarked on a series of conquests that created the largest empire the world had seen.",
  "Cyrus established the first extensive multi-ethnic empire governed by tolerance and respect for local customs. The Cyrus Cylinder is considered an early charter of human rights.",
  [(-550, "Defeated the Median Empire"), (-547, "Conquered the Lydian Empire"), (-539, "Conquered Babylon"), (-538, "Issued the Cyrus Cylinder")],
  [("Cyrus Cylinder", -538, "Declaration of religious tolerance and freedom, often called the first human rights charter")],
  [("I am Cyrus, king of the world.", "Cyrus Cylinder")])

p("pericles", "Pericles", "ペリクレス", -495, -429, ["gr"], ["politics"],
  "Pericles was an Athenian statesman, orator, and general who led Athens during its Golden Age, promoting democracy, arts, and philosophy.",
  "Pericles was born into an aristocratic Athenian family. He received an excellent education and entered politics, eventually becoming the most influential leader of democratic Athens.",
  "Under Pericles' leadership, Athens experienced an unprecedented flowering of art, architecture, philosophy, and democracy. The Parthenon was built during his leadership.",
  [(-461, "Became dominant leader of Athens"), (-447, "Began construction of the Parthenon"), (-443, "Re-elected strategos repeatedly"), (-429, "Died during the plague of Athens")],
  [("Funeral Oration", -431, "Speech honoring Athenian war dead that defined democratic ideals")],
  [("Freedom is the sure possession of those alone who have the courage to defend it.", "Funeral Oration, via Thucydides")])

p("theodore-roosevelt", "Theodore Roosevelt", "セオドア・ルーズベルト", 1858, 1919, ["us"], ["politics"],
  "Theodore Roosevelt was the 26th President of the United States, known for his progressive policies, conservation efforts, and construction of the Panama Canal.",
  "Roosevelt was born in New York City into a wealthy family. He overcame childhood illness through strenuous physical activity and became a rancher, soldier, and politician.",
  "Roosevelt expanded the role of the president, broke up monopolies, established national parks, and projected American power internationally. He won the Nobel Peace Prize.",
  [(1898, "Led the Rough Riders in the Spanish-American War"), (1901, "Became President after McKinley's assassination"), (1906, "Won Nobel Peace Prize"), (1908, "Expanded national parks and forests")],
  [("The Strenuous Life", 1899, "Speech advocating active engagement in public affairs")],
  [("Do what you can, with what you have, where you are.", "Attributed")])

p("indira-gandhi", "Indira Gandhi", "インディラ・ガンディー", 1917, 1984, ["in"], ["politics"],
  "Indira Gandhi was the first and to date only female Prime Minister of India, serving for a total of fifteen years across two periods.",
  "Gandhi was born in Allahabad into the Nehru political dynasty. She studied at Visva-Bharati and Oxford before becoming involved in Indian politics.",
  "Gandhi centralized power, led India through the 1971 war with Pakistan, and modernized India's economy. Her declaration of Emergency in 1975 remains controversial.",
  [(1966, "Became Prime Minister of India"), (1971, "Led India in the Bangladesh Liberation War"), (1975, "Declared state of Emergency"), (1984, "Assassinated by bodyguards")],
  [("Green Revolution in India", 1968, "Agricultural modernization that made India self-sufficient in food")],
  [("You cannot shake hands with a clenched fist.", "Attributed")])

p("jawaharlal-nehru", "Jawaharlal Nehru", "ジャワハルラール・ネルー", 1889, 1964, ["in"], ["politics"],
  "Jawaharlal Nehru was the first Prime Minister of India, serving from independence in 1947 until his death in 1964, and a central figure in Indian politics.",
  "Nehru was born in Allahabad into a wealthy family. He studied at Harrow and Cambridge, became a lawyer, and joined the Indian independence movement under Gandhi's leadership.",
  "Nehru shaped modern India through democratic governance, secularism, industrialization, and the Non-Aligned Movement. His vision of a democratic, secular India endures.",
  [(1929, "Became president of the Indian National Congress"), (1947, "Became first Prime Minister of India"), (1955, "Co-founded the Non-Aligned Movement"), (1961, "Established Indian Institutes of Technology")],
  [("The Discovery of India", 1946, "History and philosophy of Indian civilization")],
  [("At the stroke of the midnight hour, when the world sleeps, India will awake to life and freedom.", "Tryst with Destiny speech, 1947")])

p("kwame-nkrumah", "Kwame Nkrumah", "クワメ・エンクルマ", 1909, 1972, ["gh"], ["politics"],
  "Kwame Nkrumah was the first Prime Minister and President of Ghana who led the country to independence and became a symbol of pan-Africanism.",
  "Nkrumah was born in Nkroful, Gold Coast. He studied in the United States and Britain before returning to lead Ghana's independence movement.",
  "Nkrumah led the first sub-Saharan African country to independence from colonial rule and championed pan-African unity, inspiring independence movements across the continent.",
  [(1947, "Returned to Gold Coast to lead independence movement"), (1957, "Led Ghana to independence"), (1963, "Helped found the Organisation of African Unity"), (1966, "Overthrown in a military coup")],
  [("Africa Must Unite", 1963, "Argument for pan-African political unity")],
  [("We face neither East nor West: we face forward.", "Attributed")])

p("benito-juarez", "Benito Juárez", "ベニート・フアレス", 1806, 1872, ["mx"], ["politics"],
  "Benito Juárez was a Mexican lawyer and politician who served as President of Mexico and is regarded as the country's greatest and most beloved leader.",
  "Juárez was born in San Pablo Guelatao, Oaxaca, of Zapotec origin. Orphaned as a child, he educated himself, studied law, and entered politics.",
  "Juárez defended Mexican sovereignty against French intervention, separated church and state, and promoted liberal reforms. He is revered as the defender of the Republic.",
  [(1847, "Became Governor of Oaxaca"), (1858, "Became President during the Reform War"), (1862, "Resisted French intervention"), (1867, "Restored the Republic after defeating Maximilian")],
  [("Reform Laws", 1859, "Legislation separating church and state in Mexico")],
  [("Among individuals, as among nations, respect for the rights of others is peace.", "Manifesto, 1867")])

p("margaret-thatcher", "Margaret Thatcher", "マーガレット・サッチャー", 1925, 2013, ["gb"], ["politics"],
  "Margaret Thatcher was the first female Prime Minister of the United Kingdom, serving from 1979 to 1990, known for her conservative policies that transformed Britain.",
  "Thatcher was born in Grantham, Lincolnshire. She studied chemistry at Oxford and law before entering politics, becoming leader of the Conservative Party in 1975.",
  "Thatcher's economic policies of privatization, deregulation, and reducing trade union power transformed the British economy and influenced conservative politics worldwide.",
  [(1975, "Became leader of the Conservative Party"), (1979, "Became Prime Minister"), (1982, "Led Britain in the Falklands War"), (1990, "Resigned as Prime Minister")],
  [("Thatcherism", 1979, "Economic and political philosophy emphasizing free markets and individual responsibility")],
  [("The lady is not for turning.", "Conservative Party Conference, 1980")])

p("mikhail-gorbachev", "Mikhail Gorbachev", "ミハイル・ゴルバチョフ", 1931, 2022, ["ru"], ["politics"],
  "Mikhail Gorbachev was the last leader of the Soviet Union whose policies of glasnost and perestroika led to the end of the Cold War and the dissolution of the USSR.",
  "Gorbachev was born in Privolnoye, Russia. He studied law at Moscow State University and rose through Communist Party ranks to become General Secretary in 1985.",
  "Gorbachev's reforms ended the Cold War and earned him the Nobel Peace Prize. His policies of openness and restructuring, while aimed at saving the USSR, ultimately led to its dissolution.",
  [(1985, "Became General Secretary of the Communist Party"), (1986, "Introduced glasnost and perestroika"), (1990, "Awarded Nobel Peace Prize"), (1991, "USSR dissolved")],
  [("Perestroika: New Thinking for Our Country and the World", 1987, "Book outlining his vision for Soviet reform")],
  [("If not me, who? And if not now, when?", "Attributed")])

p("che-guevara", "Che Guevara", "チェ・ゲバラ", 1928, 1967, ["ar", "cu"], ["politics"],
  "Ernesto 'Che' Guevara was an Argentine Marxist revolutionary who was a major figure of the Cuban Revolution and became a symbol of rebellion worldwide.",
  "Guevara was born in Rosario, Argentina. He studied medicine and traveled throughout South America, where poverty and injustice radicalized his political views.",
  "Guevara became an iconic figure of revolutionary movements worldwide. His image remains one of the most recognized symbols of counterculture and rebellion.",
  [(1955, "Met Fidel Castro in Mexico"), (1959, "Cuban Revolution succeeded"), (1965, "Left Cuba for revolutionary activities abroad"), (1967, "Captured and executed in Bolivia")],
  [("Guerrilla Warfare", 1961, "Manual on guerrilla tactics and revolutionary strategy")],
  [("The revolution is not an apple that falls when it is ripe. You have to make it fall.", "Attributed")])

p("aung-san-suu-kyi", "Aung San Suu Kyi", "アウンサンスーチー", 1945, None, ["mm"], ["politics"],
  "Aung San Suu Kyi is a Myanmar politician and Nobel laureate who spent years under house arrest for her pro-democracy activism before leading the government.",
  "Suu Kyi was born in Rangoon, the daughter of independence hero Aung San. She studied at Oxford and worked for the UN before returning to Myanmar.",
  "Suu Kyi's nonviolent struggle for democracy in Myanmar earned her the Nobel Peace Prize. Her later tenure in government during the Rohingya crisis drew international criticism.",
  [(1988, "Entered politics during the 8888 Uprising"), (1989, "Placed under house arrest"), (1991, "Awarded Nobel Peace Prize"), (2016, "Became State Counsellor of Myanmar")],
  [("Freedom from Fear", 1991, "Collection of writings on democracy and human rights")],
  [("The only real prison is fear, and the only real freedom is freedom from fear.", "Freedom from Fear")])

p("lech-walesa", "Lech Wałęsa", "レフ・ワウェンサ", 1943, None, ["pl"], ["politics"],
  "Lech Wałęsa is a Polish statesman and labor activist who co-founded Solidarity, the first independent trade union in the Soviet bloc, and later became President of Poland.",
  "Wałęsa was born in Popowo, Poland. He worked as an electrician at the Gdańsk Shipyard and became a leader of labor protests against the communist government.",
  "Wałęsa's Solidarity movement was the first crack in the Soviet bloc, inspiring democratic movements across Eastern Europe and contributing to the end of communism in Europe.",
  [(1980, "Led Gdańsk shipyard strike and co-founded Solidarity"), (1981, "Solidarity declared illegal; Wałęsa interned"), (1983, "Awarded Nobel Peace Prize"), (1990, "Elected President of Poland")],
  [("Solidarity Movement", 1980, "First independent trade union in the Soviet bloc")],
  [("We hold our heads high, despite the price we have paid, because freedom is priceless.", "Nobel lecture, 1983")])

p("vaclav-havel", "Václav Havel", "ヴァーツラフ・ハヴェル", 1936, 2011, ["cz"], ["politics"],
  "Václav Havel was a Czech statesman, playwright, and dissident who served as the last President of Czechoslovakia and the first President of the Czech Republic.",
  "Havel was born in Prague into a prominent family. He became a playwright and essayist who became one of the leading voices of dissent against the communist regime.",
  "Havel's moral authority as a dissident and his leadership during the Velvet Revolution demonstrated the power of truth and conscience against totalitarianism.",
  [(1968, "Became prominent during the Prague Spring"), (1977, "Co-authored Charter 77 human rights declaration"), (1989, "Led the Velvet Revolution"), (1993, "Became first President of the Czech Republic")],
  [("The Power of the Powerless", 1978, "Essay on living in truth under totalitarianism")],
  [("Truth and love must prevail over lies and hatred.", "Attributed")])

p("kemal-ataturk", "Mustafa Kemal Atatürk", "ムスタファ・ケマル・アタテュルク", 1881, 1938, ["tr"], ["politics"],
  "Mustafa Kemal Atatürk was the founder and first President of the Republic of Turkey, who led the Turkish War of Independence and implemented sweeping modernization reforms.",
  "Atatürk was born in Thessaloniki, then part of the Ottoman Empire. He received military education and distinguished himself at Gallipoli during World War I.",
  "Atatürk transformed Turkey from an Ottoman remnant into a modern secular republic through radical political, social, and cultural reforms.",
  [(1915, "Commanded forces at Gallipoli"), (1919, "Led the Turkish War of Independence"), (1923, "Established the Republic of Turkey"), (1928, "Introduced the new Turkish alphabet")],
  [("Turkish Republic", 1923, "Establishment of a modern secular nation-state from the Ottoman Empire")],
  [("Peace at home, peace in the world.", "Attributed")])

p("hatshepsut", "Hatshepsut", "ハトシェプスト", -1507, -1458, ["eg"], ["politics"],
  "Hatshepsut was one of the most successful pharaohs of ancient Egypt, ruling as regent and then pharaoh during one of Egypt's most prosperous periods.",
  "Hatshepsut was born into the 18th dynasty royal family. She initially served as regent for her young stepson Thutmose III before declaring herself pharaoh.",
  "Hatshepsut's reign was marked by successful trade expeditions, extensive building programs including her mortuary temple at Deir el-Bahri, and economic prosperity.",
  [(-1479, "Became regent for Thutmose III"), (-1473, "Declared herself Pharaoh"), (-1470, "Launched trade expedition to Punt"), (-1458, "Died after over 20 years of rule")],
  [("Mortuary Temple at Deir el-Bahri", -1470, "Magnificent temple considered one of the architectural wonders of ancient Egypt")],
  [("Now my heart turns this way and that, as I think what the people will say.", "Temple inscription")])

p("saladin", "Saladin", "サラディン", 1137, 1193, ["eg", "iq", "sy"], ["politics"],
  "Saladin was the first sultan of Egypt and Syria who founded the Ayyubid dynasty and led the Muslim military campaign against the Crusaders.",
  "Saladin was born in Tikrit, in present-day Iraq, into a Kurdish family. He rose through military and political ranks in Egypt before becoming its ruler.",
  "Saladin's recapture of Jerusalem and his chivalrous conduct earned him respect from both Muslim and Christian worlds. He is remembered as a model of honor and leadership.",
  [(1171, "Became ruler of Egypt"), (1174, "Became Sultan of Egypt and Syria"), (1187, "Recaptured Jerusalem"), (1192, "Negotiated peace with Richard the Lionheart")],
  [("Recapture of Jerusalem", 1187, "Retook the holy city from the Crusaders with relative mercy")],
  [("I warn you against shedding blood, indulging in it and making a habit of it.", "Attributed")])

p("wangari-maathai", "Wangari Maathai", "ワンガリ・マータイ", 1940, 2011, ["ke"], ["politics"],
  "Wangari Maathai was a Kenyan environmental and political activist who founded the Green Belt Movement and became the first African woman to win the Nobel Peace Prize.",
  "Maathai was born in Nyeri, Kenya. She studied in the United States and became the first woman in East and Central Africa to earn a doctoral degree.",
  "Maathai's Green Belt Movement empowered communities through tree planting, combining environmental conservation with women's rights and democratic governance.",
  [(1977, "Founded the Green Belt Movement"), (2002, "Elected to Kenya's parliament"), (2004, "Awarded Nobel Peace Prize")],
  [("The Green Belt Movement", 1977, "Community-based program that planted over 51 million trees")],
  [("It's the little things citizens do. That's what will make the difference. My little thing is planting trees.", "Attributed")])

p("corazon-aquino", "Corazon Aquino", "コラソン・アキノ", 1933, 2009, ["ph"], ["politics"],
  "Corazon Aquino was the first female President of the Philippines who led the People Power Revolution that peacefully overthrew the Marcos dictatorship.",
  "Aquino was born into a wealthy political family in Tarlac. She married Benigno Aquino Jr., whose assassination galvanized her into politics.",
  "Aquino's People Power Revolution demonstrated that nonviolent action could topple dictatorships. She restored democracy to the Philippines and inspired democratic movements globally.",
  [(1983, "Husband Benigno Aquino assassinated"), (1986, "Led People Power Revolution; became President"), (1987, "Promulgated new Philippine constitution")],
  [("People Power Revolution", 1986, "Nonviolent revolution that restored democracy to the Philippines")],
  [("I would rather die a meaningful death than to live a meaningless life.", "Attributed")])

if __name__ == '__main__':
    write_people(P)
