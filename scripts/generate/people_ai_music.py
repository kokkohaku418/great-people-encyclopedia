#!/usr/bin/env python3
"""Generate ~100 musicians and composers."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

p("johann-sebastian-bach", "Johann Sebastian Bach", "ヨハン・ゼバスティアン・バッハ", 1685, 1750, ["de"], ["art"],
  "Johann Sebastian Bach was a German composer and musician of the Baroque period, widely regarded as one of the greatest composers in the history of Western music.",
  "Bach was born in Eisenach, Germany, into a musical family. He was orphaned at age 10 and raised by his older brother, who taught him keyboard instruments.",
  "Bach's works — including the Brandenburg Concertos, Well-Tempered Clavier, and Mass in B minor — represent the pinnacle of Baroque music and continue to influence all Western music.",
  [(1708, "Became court organist in Weimar"), (1717, "Became Kapellmeister at Köthen"), (1723, "Became Cantor at St. Thomas Church, Leipzig"), (1747, "Visited Frederick the Great")],
  [("The Well-Tempered Clavier", 1722, "Collection of preludes and fugues in all major and minor keys"), ("Mass in B minor", 1749, "Monumental setting of the Latin Mass")],
  [("The aim and final end of all music should be none other than the glory of God and the refreshment of the soul.", "Attributed")])

p("wolfgang-amadeus-mozart", "Wolfgang Amadeus Mozart", "ヴォルフガング・アマデウス・モーツァルト", 1756, 1791, ["at"], ["art"],
  "Wolfgang Amadeus Mozart was an Austrian composer who is widely regarded as among the greatest composers in the history of Western music.",
  "Mozart was born in Salzburg. A child prodigy, he composed music from age five and performed across Europe. His father Leopold was his first teacher and promoter.",
  "Mozart's operas, symphonies, concertos, and chamber music set standards of beauty and perfection that define classical music. His approximately 600 works span every genre of his era.",
  [(1762, "Began performing tours as a child prodigy"), (1781, "Moved to Vienna as a freelance musician"), (1786, "Premiered The Marriage of Figaro"), (1791, "Composed Requiem; died at age 35")],
  [("The Marriage of Figaro", 1786, "Comic opera that perfected the form"), ("Requiem in D minor", 1791, "Unfinished final work of haunting beauty")],
  [("Neither a lofty degree of intelligence nor imagination nor both together go to the making of genius. Love, love, love, that is the soul of genius.", "Attributed")])

p("ludwig-van-beethoven", "Ludwig van Beethoven", "ルートヴィヒ・ヴァン・ベートーヴェン", 1770, 1827, ["de", "at"], ["art"],
  "Ludwig van Beethoven was a German composer and pianist who was a crucial figure in the transition between the Classical and Romantic eras of Western music.",
  "Beethoven was born in Bonn, Germany. He moved to Vienna at 21, where he studied under Haydn and established himself as a virtuoso pianist and composer despite increasing deafness.",
  "Beethoven expanded the scope and ambition of the symphony, sonata, and concerto. His music expressed personal struggle and triumph, transforming music into a medium of profound human expression.",
  [(1792, "Moved to Vienna"), (1798, "First symptoms of deafness"), (1804, "Premiered the Eroica Symphony"), (1824, "Premiered the Ninth Symphony while nearly deaf")],
  [("Symphony No. 9", 1824, "Groundbreaking symphony incorporating voices and Schiller's Ode to Joy"), ("Moonlight Sonata", 1801, "One of the most famous piano compositions")],
  [("Music is the mediator between the spiritual and the sensual life.", "Attributed")])

p("frederic-chopin", "Frédéric Chopin", "フレデリック・ショパン", 1810, 1849, ["pl", "fr"], ["art"],
  "Frédéric Chopin was a Polish composer and virtuoso pianist of the Romantic era who wrote primarily for solo piano.",
  "Chopin was born in Żelazowa Wola, Poland. A child prodigy, he completed his musical education in Warsaw and moved to Paris at age 21, where he spent the rest of his life.",
  "Chopin revolutionized piano technique and expanded the expressive range of the instrument. His nocturnes, études, polonaises, and ballades remain central to the piano repertoire.",
  [(1829, "Debuted in Vienna"), (1831, "Settled in Paris"), (1838, "Spent winter in Majorca with George Sand"), (1849, "Died of tuberculosis in Paris")],
  [("Ballades", 1835, "Four piano ballades that are among the most challenging works in the repertoire"), ("Nocturnes", 1827, "Series of lyrical, expressive piano pieces")],
  [("Simplicity is the final achievement.", "Attributed")])

p("pyotr-ilyich-tchaikovsky", "Pyotr Ilyich Tchaikovsky", "ピョートル・チャイコフスキー", 1840, 1893, ["ru"], ["art"],
  "Pyotr Ilyich Tchaikovsky was a Russian composer of the Romantic period whose works include some of the most popular concert and ballet music in the classical repertoire.",
  "Tchaikovsky was born in Votkinsk, Russia. He studied at the Saint Petersburg Conservatory and became the first Russian composer to gain international recognition.",
  "Tchaikovsky's emotionally powerful music, including Swan Lake, The Nutcracker, and the 1812 Overture, brought Russian music to the world stage and remains beloved today.",
  [(1866, "Became professor at the Moscow Conservatory"), (1877, "Completed Swan Lake and Symphony No. 4"), (1888, "International conducting tour"), (1893, "Premiered Symphony No. 6 (Pathétique)")],
  [("Swan Lake", 1877, "The most famous ballet in the classical repertoire"), ("The Nutcracker", 1892, "Holiday ballet that became a worldwide tradition")],
  [("Inspiration is a guest that does not willingly visit the lazy.", "Attributed")])

p("franz-schubert", "Franz Schubert", "フランツ・シューベルト", 1797, 1828, ["at"], ["art"],
  "Franz Schubert was an Austrian composer of the late Classical and early Romantic eras, known especially for his prolific output of lieder and chamber music.",
  "Schubert was born in Vienna. He studied under Salieri and showed prodigious talent, composing hundreds of works before his early death at age 31.",
  "Schubert composed over 600 lieder, transforming the art song into a major musical form. His symphonies, chamber music, and piano works are cornerstones of the repertoire.",
  [(1814, "Composed Gretchen am Spinnrade"), (1815, "Composed Erlkönig and over 140 songs"), (1822, "Composed the Unfinished Symphony"), (1828, "Composed String Quintet; died at age 31")],
  [("Erlkönig", 1815, "Dramatic art song setting Goethe's poem"), ("Symphony No. 8 (Unfinished)", 1822, "Enigmatic two-movement symphony")],
  [("Some people come into our lives and quickly go. Some stay for a while and leave footprints on our hearts.", "Attributed")])

p("giuseppe-verdi", "Giuseppe Verdi", "ジュゼッペ・ヴェルディ", 1813, 1901, ["it"], ["art"],
  "Giuseppe Verdi was an Italian opera composer who dominated Italian opera for half a century, creating works of dramatic power and emotional depth.",
  "Verdi was born in Le Roncole, Italy. He studied in Milan and after early setbacks, achieved his first major success with Nabucco, becoming Italy's most celebrated composer.",
  "Verdi transformed Italian opera from a vehicle for vocal display into intense musical drama. His operas remain the most frequently performed in the world.",
  [(1842, "Nabucco premiered at La Scala"), (1851, "Premiered Rigoletto"), (1853, "Premiered La Traviata"), (1887, "Premiered Otello at age 73")],
  [("Aida", 1871, "Grand opera set in ancient Egypt"), ("Otello", 1887, "Operatic adaptation of Shakespeare considered Verdi's masterpiece")],
  [("You may have the universe if I may have Italy.", "Attributed")])

p("richard-wagner", "Richard Wagner", "リヒャルト・ワーグナー", 1813, 1883, ["de"], ["art"],
  "Richard Wagner was a German composer known for his operas and music dramas, particularly the monumental Ring cycle, which revolutionized opera.",
  "Wagner was born in Leipzig, Germany. He studied music and wrote his own libretti, developing a vision of opera as Gesamtkunstwerk — a total work of art.",
  "Wagner's revolutionary approach to harmony, orchestration, and the use of leitmotifs transformed not only opera but all of Western music. His influence extends to film music.",
  [(1849, "Exiled from Germany for revolutionary activities"), (1865, "Premiered Tristan und Isolde"), (1876, "Premiered the complete Ring cycle at Bayreuth"), (1882, "Premiered Parsifal")],
  [("Der Ring des Nibelungen", 1876, "Monumental four-opera cycle lasting about 15 hours"), ("Tristan und Isolde", 1865, "Opera that pushed harmony to the edge of tonality")],
  [("Imagination creates reality.", "Attributed")])

p("johannes-brahms", "Johannes Brahms", "ヨハネス・ブラームス", 1833, 1897, ["de", "at"], ["art"],
  "Johannes Brahms was a German composer and pianist of the Romantic period who combined classical forms with Romantic expression.",
  "Brahms was born in Hamburg. He was championed by Robert and Clara Schumann and settled in Vienna, where he became one of the leading composers of his generation.",
  "Brahms's symphonies, concertos, and chamber music are pillars of the Romantic repertoire. His synthesis of classical structure with Romantic passion influenced generations of composers.",
  [(1853, "Met Robert and Clara Schumann"), (1868, "Premiered A German Requiem"), (1876, "Completed Symphony No. 1"), (1885, "Completed Symphony No. 4")],
  [("A German Requiem", 1868, "Choral work using German texts rather than the Latin Mass"), ("Symphony No. 4", 1885, "Final symphony, culminating in a magnificent passacaglia")],
  [("Without craftsmanship, inspiration is a mere reed shaken in the wind.", "Attributed")])

p("franz-liszt", "Franz Liszt", "フランツ・リスト", 1811, 1886, ["hu", "at"], ["art"],
  "Franz Liszt was a Hungarian composer and virtuoso pianist who was one of the most celebrated musicians of the 19th century.",
  "Liszt was born in Raiding, Hungary. A child prodigy, he studied in Vienna and Paris, becoming the most famous pianist of his age and inventing the modern recital.",
  "Liszt invented the symphonic poem, transformed piano technique, and pioneered the solo recital. His harmonic innovations anticipated Wagner and Impressionism.",
  [(1838, "Began decade of virtuoso concert tours"), (1847, "Settled in Weimar as Kapellmeister"), (1853, "Composed Piano Sonata in B minor"), (1865, "Took minor orders in the Catholic Church")],
  [("Piano Sonata in B minor", 1853, "Revolutionary one-movement sonata"), ("Hungarian Rhapsodies", 1847, "Series of 19 piano pieces based on Hungarian themes")],
  [("Beware of missing chances; otherwise it may be altogether too late some day.", "Attributed")])

p("igor-stravinsky", "Igor Stravinsky", "イーゴリ・ストラヴィンスキー", 1882, 1971, ["ru", "fr", "us"], ["art"],
  "Igor Stravinsky was a Russian-born composer whose revolutionary works changed the course of 20th-century music.",
  "Stravinsky was born in Oranienbaum, Russia. He studied under Rimsky-Korsakov and rose to fame through his ballets for Sergei Diaghilev's Ballets Russes.",
  "Stravinsky's The Rite of Spring caused a riot at its premiere and revolutionized rhythm and orchestration. His stylistic evolution through neoclassicism and serialism influenced all modern music.",
  [(1910, "Premiered The Firebird"), (1913, "Premiered The Rite of Spring"), (1920, "Moved to France; neoclassical period began"), (1939, "Moved to the United States")],
  [("The Rite of Spring", 1913, "Ballet that revolutionized modern music with its revolutionary rhythms"), ("The Firebird", 1910, "Ballet that established his international reputation")],
  [("Lesser artists borrow, great artists steal.", "Attributed")])

p("claude-debussy", "Claude Debussy", "クロード・ドビュッシー", 1862, 1918, ["fr"], ["art"],
  "Claude Debussy was a French composer who developed a new approach to harmony and orchestration that became known as musical Impressionism.",
  "Debussy was born in Saint-Germain-en-Laye, France. He studied at the Paris Conservatoire and won the Prix de Rome, but his mature style broke radically with tradition.",
  "Debussy's innovative use of non-traditional scales, unresolved harmonies, and tone color freed music from Germanic Romantic conventions and opened the door to modern music.",
  [(1884, "Won the Prix de Rome"), (1894, "Premiered Prélude à l'après-midi d'un faune"), (1902, "Premiered Pelléas et Mélisande"), (1905, "Composed La Mer")],
  [("Prélude à l'après-midi d'un faune", 1894, "Orchestral work that inaugurated modern music"), ("La Mer", 1905, "Three orchestral sketches depicting the sea")],
  [("Music is the space between the notes.", "Attributed")])

p("antonio-vivaldi", "Antonio Vivaldi", "アントニオ・ヴィヴァルディ", 1678, 1741, ["it"], ["art"],
  "Antonio Vivaldi was an Italian Baroque composer, virtuoso violinist, and priest, famous for his concertos, especially The Four Seasons.",
  "Vivaldi was born in Venice. He was ordained as a priest but devoted most of his life to music, teaching at the Ospedale della Pietà and composing prolifically.",
  "Vivaldi standardized the three-movement concerto form and composed over 500 concertos. The Four Seasons, with its vivid programmatic imagery, remains one of the most popular classical works.",
  [(1703, "Ordained as a priest; began teaching at the Pietà"), (1711, "Published L'estro armonico"), (1725, "Published The Four Seasons"), (1741, "Died in poverty in Vienna")],
  [("The Four Seasons", 1725, "Four violin concertos depicting the seasons"), ("L'estro armonico", 1711, "Collection of 12 concertos that established his European fame")],
  [("There is no music in nature, neither melody nor harmony. Music is the creation of man.", "Attributed")])

p("george-frideric-handel", "George Frideric Handel", "ゲオルク・フリードリヒ・ヘンデル", 1685, 1759, ["de", "gb"], ["art"],
  "George Frideric Handel was a German-born British Baroque composer known for his operas, oratorios, anthems, and organ concertos.",
  "Handel was born in Halle, Germany. He traveled to Italy, where he mastered Italian opera, then settled in London, where he became a naturalized British subject.",
  "Handel's Messiah is one of the most frequently performed choral works in Western music. His operas and oratorios combined drama with musical magnificence.",
  [(1706, "Traveled to Italy"), (1712, "Settled in London"), (1741, "Composed Messiah in 24 days"), (1751, "Became blind but continued to perform")],
  [("Messiah", 1741, "Oratorio telling the story of Christ, featuring the famous 'Hallelujah' chorus"), ("Water Music", 1717, "Orchestral suite composed for King George I")],
  [("Whether I was in my body or out of my body as I wrote it, I know not.", "On composing the Hallelujah Chorus")])

p("joseph-haydn", "Joseph Haydn", "フランツ・ヨーゼフ・ハイドン", 1732, 1809, ["at"], ["art"],
  "Joseph Haydn was an Austrian composer who was one of the most prolific and prominent composers of the Classical period, known as the Father of the Symphony.",
  "Haydn was born in Rohrau, Austria. He was a choirboy in Vienna and struggled as a freelance musician before becoming Kapellmeister to the Esterházy family for nearly 30 years.",
  "Haydn established the symphony and string quartet as major musical forms. His wit, invention, and craftsmanship influenced Mozart, Beethoven, and all subsequent Western music.",
  [(1761, "Became vice-Kapellmeister to the Esterházy family"), (1781, "Published groundbreaking String Quartets Op. 33"), (1791, "First London visit; composed 12 London Symphonies"), (1798, "Composed The Creation")],
  [("The Creation", 1798, "Oratorio depicting the creation of the world"), ("Symphony No. 94 (Surprise)", 1791, "Famous symphony with its startling loud chord")],
  [("There was no one near to confuse me, so I was forced to become original.", "Attributed")])

p("robert-schumann", "Robert Schumann", "ローベルト・シューマン", 1810, 1856, ["de"], ["art"],
  "Robert Schumann was a German composer and music critic of the Romantic era, known for his piano music, lieder, symphonies, and chamber music.",
  "Schumann was born in Zwickau, Germany. He studied law but devoted himself to music. A hand injury ended his pianistic career, and he turned to composition and criticism.",
  "Schumann's deeply personal music expressed the Romantic ideal of art as emotional confession. His criticism championed Chopin, Brahms, and other young composers.",
  [(1834, "Founded the Neue Zeitschrift für Musik journal"), (1840, "Composed over 130 songs in his 'Year of Song'"), (1840, "Married Clara Wieck"), (1854, "Attempted suicide; committed to asylum")],
  [("Dichterliebe", 1840, "Song cycle to poems by Heine"), ("Piano Concerto in A minor", 1845, "One of the most beloved Romantic concertos")],
  [("To send light into the darkness of men's hearts — such is the duty of the artist.", "Attributed")])

p("felix-mendelssohn", "Felix Mendelssohn", "フェリックス・メンデルスゾーン", 1809, 1847, ["de"], ["art"],
  "Felix Mendelssohn was a German composer, pianist, and conductor of the early Romantic period, known for reviving interest in Bach's music.",
  "Mendelssohn was born in Hamburg into a prominent Jewish family. A child prodigy, he composed his Octet at 16 and the Overture to A Midsummer Night's Dream at 17.",
  "Mendelssohn revived public interest in Bach, established the modern conductor's role, and composed works of luminous beauty that define early Romanticism.",
  [(1826, "Composed the Overture to A Midsummer Night's Dream"), (1829, "Revived Bach's St. Matthew Passion"), (1842, "Founded the Leipzig Conservatory"), (1846, "Premiered Elijah")],
  [("Violin Concerto in E minor", 1844, "One of the most performed and beloved violin concertos"), ("A Midsummer Night's Dream", 1826, "Overture and incidental music for Shakespeare's play")],
  [("People often complain that music is too ambiguous. I find it is quite the opposite.", "Letter, 1842")])

p("gustav-mahler", "Gustav Mahler", "グスタフ・マーラー", 1860, 1911, ["at", "cz"], ["art"],
  "Gustav Mahler was an Austrian-Bohemian late-Romantic composer and conductor, known for his monumental symphonies and song cycles.",
  "Mahler was born in Kaliště, Bohemia, to a Jewish family. He studied at the Vienna Conservatory and became one of the leading opera conductors of his time.",
  "Mahler's symphonies expanded the form to unprecedented scale and emotional range. His music, initially controversial, became central to the 20th-century orchestral repertoire.",
  [(1888, "Completed Symphony No. 1"), (1897, "Became director of the Vienna Court Opera"), (1907, "Left Vienna; composed Das Lied von der Erde"), (1910, "Premiered Symphony No. 8 (Symphony of a Thousand)")],
  [("Symphony No. 2 (Resurrection)", 1894, "Symphony exploring themes of death and resurrection"), ("Das Lied von der Erde", 1909, "Song-symphony based on Chinese poetry")],
  [("My time will come.", "Letter to Alma Mahler")])

p("dmitri-shostakovich", "Dmitri Shostakovich", "ドミートリイ・ショスタコーヴィチ", 1906, 1975, ["ru"], ["art"],
  "Dmitri Shostakovich was a Russian composer who is regarded as one of the major composers of the 20th century, navigating art and survival under Soviet repression.",
  "Shostakovich was born in Saint Petersburg. A prodigy, he entered the Petrograd Conservatory at age 13 and gained fame with his Symphony No. 1 at age 19.",
  "Shostakovich's 15 symphonies and 15 string quartets chronicle the Soviet experience with music of extraordinary power. His ability to embed dissent within Soviet-approved forms was remarkable.",
  [(1926, "Premiered Symphony No. 1"), (1936, "Denounced by Pravda for Lady Macbeth"), (1937, "Premiered Symphony No. 5"), (1953, "Premiered Symphony No. 10 after Stalin's death")],
  [("Symphony No. 5", 1937, "Comeback symphony after political denunciation"), ("String Quartet No. 8", 1960, "Intensely personal quartet dedicated to victims of fascism and war")],
  [("A creative artist works on his next composition because he is not satisfied with his previous one.", "Testimony")])

p("sergei-rachmaninoff", "Sergei Rachmaninoff", "セルゲイ・ラフマニノフ", 1873, 1943, ["ru", "us"], ["art"],
  "Sergei Rachmaninoff was a Russian composer, virtuoso pianist, and conductor of the late Romantic era.",
  "Rachmaninoff was born in Semyonovo, Russia. He studied at the Moscow Conservatory and achieved fame as both a composer and one of the greatest pianists of all time.",
  "Rachmaninoff's richly melodic music represents the culmination of the Romantic piano tradition. His concertos and solo works remain among the most performed in the repertoire.",
  [(1892, "Composed Prelude in C-sharp minor"), (1901, "Premiered Piano Concerto No. 2 after recovery from depression"), (1917, "Left Russia permanently"), (1934, "Composed Rhapsody on a Theme of Paganini")],
  [("Piano Concerto No. 2", 1901, "One of the most popular piano concertos"), ("Rhapsody on a Theme of Paganini", 1934, "Variations for piano and orchestra")],
  [("Music is enough for a lifetime, but a lifetime is not enough for music.", "Attributed")])

p("bela-bartok", "Béla Bartók", "バルトーク・ベーラ", 1881, 1945, ["hu", "us"], ["art"],
  "Béla Bartók was a Hungarian composer and pianist, one of the founders of ethnomusicology and one of the most important composers of the 20th century.",
  "Bartók was born in Nagyszentmiklós, Hungary (now Romania). He studied at the Budapest Academy and with Kodály began collecting folk music from across Eastern Europe.",
  "Bartók's fusion of folk music with modernist techniques created a distinctive musical language. His Concerto for Orchestra and string quartets are pillars of the modern repertoire.",
  [(1905, "Began collecting folk music with Kodály"), (1917, "Premiered The Wooden Prince ballet"), (1936, "Completed Music for Strings, Percussion and Celesta"), (1943, "Composed Concerto for Orchestra")],
  [("Concerto for Orchestra", 1943, "Virtuosic orchestral work composed in America"), ("Music for Strings, Percussion and Celesta", 1936, "Masterpiece of rhythmic and timbral innovation")],
  [("Competitions are for horses, not artists.", "Attributed")])

p("giacomo-puccini", "Giacomo Puccini", "ジャコモ・プッチーニ", 1858, 1924, ["it"], ["art"],
  "Giacomo Puccini was an Italian opera composer who was the last great representative of the Italian operatic tradition.",
  "Puccini was born in Lucca into a family of church musicians. He studied at the Milan Conservatory and devoted his career exclusively to opera.",
  "Puccini's operas combine beautiful melody with dramatic intensity. La Bohème, Tosca, and Madama Butterfly remain among the most frequently performed operas worldwide.",
  [(1893, "Premiered Manon Lescaut"), (1896, "Premiered La Bohème"), (1900, "Premiered Tosca"), (1904, "Premiered Madama Butterfly")],
  [("La Bohème", 1896, "Opera about young bohemians in Paris"), ("Madama Butterfly", 1904, "Tragic opera set in Nagasaki, Japan")],
  [("Inspiration is an awakening, a quickening of all man's faculties.", "Attributed")])

p("antonin-dvorak", "Antonín Dvořák", "アントニン・ドヴォルザーク", 1841, 1904, ["cz"], ["art"],
  "Antonín Dvořák was a Czech composer known for integrating folk music elements into the classical tradition, creating music of distinctive national character.",
  "Dvořák was born in Nelahozeves, Bohemia. He studied at the Prague Organ School and worked as a violist before gaining international fame through Brahms's encouragement.",
  "Dvořák's music combined Bohemian folk elements with classical mastery. His New World Symphony, composed in America, became one of the most popular symphonies ever written.",
  [(1878, "Slavonic Dances brought international fame"), (1892, "Became director of the National Conservatory in New York"), (1893, "Premiered the New World Symphony"), (1901, "Premiered opera Rusalka")],
  [("Symphony No. 9 (From the New World)", 1893, "Symphony inspired by American and Bohemian folk music"), ("Cello Concerto in B minor", 1895, "Considered the greatest cello concerto")],
  [("I have composed too much.", "Attributed")])

p("hector-berlioz", "Hector Berlioz", "エクトル・ベルリオーズ", 1803, 1869, ["fr"], ["art"],
  "Hector Berlioz was a French Romantic composer who was a major innovator in orchestration and the inventor of the program symphony.",
  "Berlioz was born in La Côte-Saint-André, France. He studied medicine before switching to music at the Paris Conservatoire, where he won the Prix de Rome.",
  "Berlioz revolutionized orchestration and the concept of the symphony through programmatic elements. His Treatise on Instrumentation became the standard text on orchestration.",
  [(1830, "Composed Symphonie fantastique"), (1838, "Composed Harold in Italy"), (1844, "Published Treatise on Instrumentation"), (1862, "Composed the opera Les Troyens")],
  [("Symphonie fantastique", 1830, "Revolutionary program symphony depicting an artist's opium dream"), ("Treatise on Instrumentation", 1844, "Definitive guide to orchestration")],
  [("Time is a great teacher, but unfortunately it kills all its pupils.", "Attributed")])

p("clara-schumann", "Clara Schumann", "クララ・シューマン", 1819, 1896, ["de"], ["art"],
  "Clara Schumann was a German pianist and composer, one of the most distinguished pianists of the Romantic era and one of the first professional female concert pianists.",
  "Clara was born in Leipzig, the daughter of piano teacher Friedrich Wieck. She was a child prodigy who debuted at age nine and toured Europe as a teenager.",
  "Clara Schumann was among the foremost pianists of her era and championed the works of her husband Robert Schumann and Johannes Brahms. She helped establish the modern piano recital.",
  [(1828, "Debuted as a concert pianist at age nine"), (1840, "Married Robert Schumann"), (1856, "Continued performing after Robert's death"), (1878, "Became professor at the Frankfurt Conservatory")],
  [("Piano Concerto in A minor", 1835, "Composed at age 14, displaying remarkable maturity"), ("Three Romances for Violin and Piano", 1853, "Beautiful chamber work")],
  [("I once believed that I possessed creative talent, but I have given up this idea; a woman must not desire to compose.", "Diary, later contradicted by her own achievements")])

p("sergei-prokofiev", "Sergei Prokofiev", "セルゲイ・プロコフィエフ", 1891, 1953, ["ru"], ["art"],
  "Sergei Prokofiev was a Russian composer, pianist, and conductor who created some of the most celebrated works of the 20th century.",
  "Prokofiev was born in Sontsovka, Ukraine. A prodigy, he entered the Saint Petersburg Conservatory at age 13 and quickly gained a reputation as a brilliant if provocative talent.",
  "Prokofiev's distinctive style combined lyrical melody with driving rhythms and biting wit. His Romeo and Juliet ballet and Peter and the Wolf are loved worldwide.",
  [(1914, "Graduated from Conservatory"), (1918, "Left Russia for the West"), (1936, "Returned permanently to the Soviet Union"), (1945, "Premiered Symphony No. 5")],
  [("Romeo and Juliet", 1935, "Ballet score of enduring popularity"), ("Peter and the Wolf", 1936, "Symphonic fairy tale introducing children to the orchestra")],
  [("Music is the language of feelings.", "Attributed")])

p("maurice-ravel", "Maurice Ravel", "モーリス・ラヴェル", 1875, 1937, ["fr"], ["art"],
  "Maurice Ravel was a French composer known for his musical craftsmanship and brilliant orchestration, associated with but distinct from Impressionism.",
  "Ravel was born in Ciboure, France. He studied at the Paris Conservatoire and became known for his impeccable technique and refined musical style.",
  "Ravel's orchestral mastery and distinctive harmonic language produced works of extraordinary beauty and precision. Boléro became one of the most performed orchestral pieces in the world.",
  [(1899, "Composed Pavane for a Dead Princess"), (1908, "Composed Gaspard de la nuit"), (1920, "Composed La Valse"), (1928, "Composed Boléro")],
  [("Boléro", 1928, "Hypnotic orchestral piece built on a single repeated melody with crescendo"), ("Daphnis et Chloé", 1912, "Ballet score of extraordinary orchestral brilliance")],
  [("The only love affair I have ever had was with music.", "Attributed")])

p("george-gershwin", "George Gershwin", "ジョージ・ガーシュウィン", 1898, 1937, ["us"], ["art"],
  "George Gershwin was an American composer and pianist whose compositions spanned popular music, jazz, and classical forms.",
  "Gershwin was born in Brooklyn, New York, to Russian-Jewish immigrant parents. He left school at 15 to work as a song plugger on Tin Pan Alley.",
  "Gershwin bridged the gap between popular and classical music. Rhapsody in Blue, Porgy and Bess, and his songs became integral to the American cultural identity.",
  [(1919, "Wrote Swanee"), (1924, "Premiered Rhapsody in Blue"), (1935, "Premiered Porgy and Bess"), (1937, "Died of brain tumor at age 38")],
  [("Rhapsody in Blue", 1924, "Orchestral composition blending jazz and classical music"), ("Porgy and Bess", 1935, "Opera depicting African American life in Charleston")],
  [("Life is a lot like jazz — it's best when you improvise.", "Attributed")])

p("louis-armstrong", "Louis Armstrong", "ルイ・アームストロング", 1901, 1971, ["us"], ["art"],
  "Louis Armstrong was an American trumpeter, composer, vocalist, and actor who was one of the most influential figures in the history of jazz.",
  "Armstrong was born into poverty in New Orleans. He learned to play cornet in a juvenile home and was mentored by Joe 'King' Oliver.",
  "Armstrong's virtuosic trumpet playing, distinctive voice, and charismatic personality transformed jazz from ensemble music to a soloist's art and influenced all popular music.",
  [(1922, "Joined King Oliver's Creole Jazz Band in Chicago"), (1925, "Recorded the Hot Five and Hot Seven sessions"), (1964, "Recorded 'Hello, Dolly!' — topped the Beatles"), (1967, "Recorded 'What a Wonderful World'")],
  [("Hot Five and Hot Seven recordings", 1925, "Revolutionary recordings that defined jazz improvisation"), ("What a Wonderful World", 1967, "Song that became an enduring anthem of optimism")],
  [("If you have to ask what jazz is, you'll never know.", "Attributed")])

p("duke-ellington", "Duke Ellington", "デューク・エリントン", 1899, 1974, ["us"], ["art"],
  "Duke Ellington was an American composer, pianist, and bandleader who led his jazz orchestra for over 50 years, composing thousands of works.",
  "Ellington was born in Washington, D.C. He began playing piano as a child and formed his first band as a teenager, eventually leading one of the most famous orchestras in jazz history.",
  "Ellington was one of the 20th century's most prolific composers. His sophisticated jazz compositions elevated the genre to an art form and his influence spans jazz, popular music, and beyond.",
  [(1927, "Began residency at the Cotton Club"), (1941, "Composed 'Take the A Train' with Strayhorn"), (1943, "First Carnegie Hall concert"), (1966, "Performed at first jazz concert at a church")],
  [("Take the A Train", 1941, "Signature song composed by Billy Strayhorn"), ("Black, Brown and Beige", 1943, "Extended work celebrating African American history")],
  [("It don't mean a thing if it ain't got that swing.", "Song title")])

p("miles-davis", "Miles Davis", "マイルス・デイヴィス", 1926, 1991, ["us"], ["art"],
  "Miles Davis was an American trumpeter, bandleader, and composer who was at the forefront of several major developments in jazz, including bebop, cool jazz, and jazz fusion.",
  "Davis was born in Alton, Illinois, into an affluent African American family. He moved to New York to study at Juilliard but quickly became part of the bebop scene.",
  "Davis constantly reinvented jazz through cool jazz, modal jazz, and jazz fusion. Kind of Blue is the best-selling jazz album of all time.",
  [(1949, "Recorded Birth of the Cool sessions"), (1959, "Recorded Kind of Blue"), (1969, "Recorded Bitches Brew, pioneering jazz fusion"), (1981, "Comeback after six-year hiatus")],
  [("Kind of Blue", 1959, "The best-selling jazz album of all time, pioneering modal jazz"), ("Bitches Brew", 1969, "Album that launched jazz fusion")],
  [("Do not fear mistakes. There are none.", "Attributed")])

p("john-coltrane", "John Coltrane", "ジョン・コルトレーン", 1926, 1967, ["us"], ["art"],
  "John Coltrane was an American jazz saxophonist and composer who was one of the most influential and acclaimed figures in the history of jazz.",
  "Coltrane was born in Hamlet, North Carolina. He served in the Navy and played in various bands before joining Miles Davis's quintet and Thelonious Monk's group.",
  "Coltrane expanded the boundaries of jazz through his innovative harmonic and melodic approaches. A Love Supreme is considered one of the greatest jazz recordings.",
  [(1957, "Recorded Blue Train"), (1959, "Performed on Kind of Blue"), (1960, "Formed his classic quartet"), (1964, "Recorded A Love Supreme")],
  [("A Love Supreme", 1964, "Spiritual jazz masterpiece in four parts"), ("Giant Steps", 1959, "Album featuring revolutionary harmonic patterns")],
  [("I think the main thing a musician would like to do is to give a picture to the listener of the many wonderful things he knows of and senses in the universe.", "Liner notes, A Love Supreme")])

p("ella-fitzgerald", "Ella Fitzgerald", "エラ・フィッツジェラルド", 1917, 1996, ["us"], ["art"],
  "Ella Fitzgerald was an American jazz singer known as the 'First Lady of Song,' celebrated for her purity of tone, impeccable diction, and phrasing.",
  "Fitzgerald was born in Newport News, Virginia. She won an amateur contest at the Apollo Theater at age 17, launching her career with Chick Webb's orchestra.",
  "Fitzgerald's vocal mastery, scat singing, and interpretive brilliance set the standard for jazz vocalists. Her Songbook series preserved the Great American Songbook.",
  [(1935, "Won amateur contest at the Apollo Theater"), (1938, "Recorded 'A-Tisket, A-Tasket'"), (1956, "Began the Songbook series"), (1960, "Won Grammy Awards")],
  [("Ella Fitzgerald Sings the Cole Porter Songbook", 1956, "First of the landmark Songbook series"), ("Mack the Knife - Ella in Berlin", 1960, "Legendary live recording")],
  [("The only thing better than singing is more singing.", "Attributed")])

p("bob-dylan", "Bob Dylan", "ボブ・ディラン", 1941, None, ["us"], ["art"],
  "Bob Dylan is an American singer-songwriter who has been a major figure in popular culture for more than 60 years, winning the Nobel Prize in Literature.",
  "Dylan was born Robert Zimmerman in Duluth, Minnesota. He moved to New York in 1961, drawn by the folk music scene and the influence of Woody Guthrie.",
  "Dylan transformed popular music by bringing literary sensibility to song lyrics. His music became the soundtrack of the civil rights and anti-war movements.",
  [(1962, "Released first album"), (1965, "Went electric at Newport Folk Festival"), (1975, "Released Blood on the Tracks"), (2016, "Awarded Nobel Prize in Literature")],
  [("Highway 61 Revisited", 1965, "Album featuring 'Like a Rolling Stone'"), ("Blood on the Tracks", 1975, "Album widely regarded as his masterpiece")],
  [("A man is a success if he gets up in the morning and gets to bed at night and in between does what he wants to do.", "Attributed")])

p("maria-callas", "Maria Callas", "マリア・カラス", 1923, 1977, ["us", "gr"], ["art"],
  "Maria Callas was a Greek-American soprano who was one of the most renowned and influential opera singers of the 20th century.",
  "Callas was born in New York to Greek immigrant parents. She studied at the Athens Conservatoire and made her professional debut in Greece during World War II.",
  "Callas revived interest in bel canto opera and set new standards for operatic acting. Her dramatic interpretations and vocal artistry transformed opera performance.",
  [(1942, "Professional debut in Athens"), (1947, "Italian debut in Verona"), (1952, "La Scala debut"), (1958, "Famous conflict with the Metropolitan Opera")],
  [("Tosca at Covent Garden", 1964, "Legendary recording of Puccini's opera"), ("Norma", 1960, "Definitive recording of Bellini's opera")],
  [("First I lost my voice, then I lost my figure, then I lost Onassis.", "Attributed")])

p("jimi-hendrix", "Jimi Hendrix", "ジミ・ヘンドリックス", 1942, 1970, ["us"], ["art"],
  "Jimi Hendrix was an American rock guitarist, singer, and songwriter who is widely regarded as the greatest electric guitarist in the history of popular music.",
  "Hendrix was born in Seattle, Washington. He taught himself guitar and played in various bands before moving to England, where he achieved fame with the Jimi Hendrix Experience.",
  "Hendrix revolutionized electric guitar through innovative techniques including feedback, distortion, and wah-wah effects. His influence on rock music is immeasurable.",
  [(1966, "Formed the Jimi Hendrix Experience in London"), (1967, "Released Are You Experienced"), (1969, "Performed at Woodstock"), (1970, "Died in London at age 27")],
  [("Are You Experienced", 1967, "Debut album that revolutionized rock guitar"), ("Electric Ladyland", 1968, "Double album showcasing his musical range")],
  [("Music doesn't lie. If there is something to be changed in this world, then it can only happen through music.", "Attributed")])

p("aretha-franklin", "Aretha Franklin", "アレサ・フランクリン", 1942, 2018, ["us"], ["art"],
  "Aretha Franklin was an American singer, songwriter, and pianist known as the 'Queen of Soul,' celebrated for her powerful vocals and emotional intensity.",
  "Franklin was born in Memphis, Tennessee, and grew up in Detroit. She began singing in her father's church as a child and signed her first recording contract at age 18.",
  "Franklin's voice defined soul music and crossed all musical boundaries. Her recording of 'Respect' became an anthem for civil rights and women's empowerment.",
  [(1961, "Signed with Columbia Records"), (1967, "Released 'Respect'; became Queen of Soul"), (1972, "Recorded Amazing Grace live album"), (1987, "First woman inducted into the Rock and Roll Hall of Fame")],
  [("I Never Loved a Man the Way I Love You", 1967, "Breakthrough album featuring 'Respect'"), ("Amazing Grace", 1972, "Best-selling gospel album of all time")],
  [("Being a singer is a natural gift. It means I'm using to the highest degree possible the gift that God gave me.", "Attributed")])

p("david-bowie", "David Bowie", "デヴィッド・ボウイ", 1947, 2016, ["gb"], ["art"],
  "David Bowie was a British singer-songwriter and actor who was a leading figure in the music industry for over five decades, known for his reinventive approach.",
  "Bowie was born David Jones in Brixton, London. He explored various musical styles and personas, becoming one of the most influential musicians of the 20th century.",
  "Bowie's constant reinvention — from Ziggy Stardust to the Thin White Duke to electronic innovator — pushed the boundaries of rock music, fashion, and popular culture.",
  [(1969, "Released 'Space Oddity'"), (1972, "Created Ziggy Stardust persona"), (1977, "Released the Berlin Trilogy"), (2016, "Released Blackstar; died two days later")],
  [("The Rise and Fall of Ziggy Stardust", 1972, "Concept album about a rock star alien"), ("Heroes", 1977, "Album from his Berlin period, featuring the iconic title track")],
  [("I don't know where I'm going from here, but I promise it won't be boring.", "Attributed")])

if __name__ == '__main__':
    write_people(P)
