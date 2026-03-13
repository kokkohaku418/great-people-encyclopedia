#!/usr/bin/env python3
"""Generate ~100 visual artists."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

p("leonardo-da-vinci", "Leonardo da Vinci", "レオナルド・ダ・ヴィンチ", 1452, 1519, ["it"], ["art", "engineering"],
  "Leonardo da Vinci was an Italian polymath of the Renaissance whose areas of interest included painting, sculpture, architecture, science, engineering, and anatomy.",
  "Leonardo was born in Vinci, Italy. He was apprenticed to Andrea del Verrocchio in Florence, where he developed his extraordinary artistic and scientific talents.",
  "Leonardo's paintings, including the Mona Lisa and The Last Supper, are among the most famous works in art history. His notebooks reveal a mind centuries ahead of his time.",
  [(1472, "Qualified as a master artist"), (1482, "Moved to Milan to work for Ludovico Sforza"), (1503, "Began painting the Mona Lisa"), (1516, "Moved to France under Francis I")],
  [("Mona Lisa", 1503, "The world's most famous portrait painting"), ("The Last Supper", 1498, "Monumental mural depicting Christ's last meal with his disciples")],
  [("Learning never exhausts the mind.", "Notebooks")])

p("michelangelo", "Michelangelo", "ミケランジェロ", 1475, 1564, ["it"], ["art"],
  "Michelangelo was an Italian sculptor, painter, architect, and poet of the High Renaissance, considered one of the greatest artists of all time.",
  "Michelangelo was born in Caprese, Italy. He was apprenticed to Ghirlandaio and later studied sculpture in the Medici gardens. His talent was recognized early by Lorenzo de' Medici.",
  "Michelangelo's David, the Sistine Chapel ceiling, and St. Peter's Basilica dome are pinnacles of Western art. His work defined the High Renaissance and influenced centuries of art.",
  [(1498, "Completed the Pietà"), (1504, "Completed the David"), (1512, "Completed the Sistine Chapel ceiling"), (1547, "Appointed architect of St. Peter's Basilica")],
  [("David", 1504, "Iconic marble sculpture symbolizing the Renaissance ideal"), ("Sistine Chapel Ceiling", 1512, "Monumental fresco cycle in the Vatican")],
  [("I saw the angel in the marble and carved until I set him free.", "Attributed")])

p("raphael", "Raphael", "ラファエロ", 1483, 1520, ["it"], ["art"],
  "Raphael was an Italian painter and architect of the High Renaissance, celebrated for the perfection and grace of his art.",
  "Raphael was born in Urbino, Italy. He studied under Perugino and was influenced by both Leonardo and Michelangelo, developing a style of serene beauty.",
  "Raphael's School of Athens, Sistine Madonna, and Vatican Stanze established ideals of beauty and composition that defined Western art for centuries.",
  [(1504, "Moved to Florence"), (1508, "Began work on the Vatican Stanze"), (1513, "Painted the Sistine Madonna"), (1520, "Died at age 37")],
  [("The School of Athens", 1511, "Iconic fresco depicting ancient philosophers in architectural splendor"), ("Sistine Madonna", 1513, "Celebrated altarpiece featuring the Madonna and Child")],
  [("When one is painting one does not think.", "Attributed")])

p("rembrandt", "Rembrandt van Rijn", "レンブラント・ファン・レイン", 1606, 1669, ["nl"], ["art"],
  "Rembrandt was a Dutch painter and etcher, generally considered one of the greatest visual artists in history and the most important in Dutch art history.",
  "Rembrandt was born in Leiden, Netherlands. He studied painting and opened his own studio, quickly gaining fame for his portraits and historical paintings.",
  "Rembrandt's mastery of light and shadow, his psychological depth in portraiture, and his prolific etchings revolutionized European art and continue to influence artists today.",
  [(1631, "Moved to Amsterdam"), (1632, "Painted The Anatomy Lesson of Dr. Nicolaes Tulp"), (1642, "Painted The Night Watch"), (1661, "Painted The Syndics of the Drapers' Guild")],
  [("The Night Watch", 1642, "Masterpiece of group portraiture and dramatic lighting"), ("Self-Portrait with Two Circles", 1665, "One of his most celebrated late self-portraits")],
  [("I can't paint the way they want me to paint and they know that too.", "Attributed")])

p("vincent-van-gogh", "Vincent van Gogh", "フィンセント・ファン・ゴッホ", 1853, 1890, ["nl", "fr"], ["art"],
  "Vincent van Gogh was a Dutch Post-Impressionist painter who created about 2,100 artworks in roughly a decade, profoundly influencing 20th-century art.",
  "Van Gogh was born in Groot-Zundert, Netherlands. He worked as an art dealer and preacher before devoting himself to painting at age 27.",
  "Van Gogh's bold colors, emotional honesty, and expressive brushwork influenced Expressionism, Fauvism, and modern art. His life and art became a symbol of the misunderstood genius.",
  [(1880, "Decided to become an artist"), (1886, "Moved to Paris; encountered Impressionism"), (1888, "Moved to Arles; painted The Starry Night"), (1890, "Died in Auvers-sur-Oise")],
  [("The Starry Night", 1889, "Iconic painting of a swirling night sky over a village"), ("Sunflowers", 1888, "Series of still life paintings that became symbols of Post-Impressionism")],
  [("I dream my painting and I paint my dream.", "Letter to Theo van Gogh")])

p("claude-monet", "Claude Monet", "クロード・モネ", 1840, 1926, ["fr"], ["art"],
  "Claude Monet was a French painter and founder of Impressionism, known for his revolutionary approach to capturing light and atmosphere in paint.",
  "Monet was born in Paris and grew up in Le Havre. He studied under Eugène Boudin and became the leading figure of the Impressionist movement.",
  "Monet's technique of painting outdoors to capture fleeting effects of light gave birth to Impressionism. His Water Lilies series became one of the most celebrated achievements in art.",
  [(1872, "Painted Impression, Sunrise"), (1874, "First Impressionist exhibition"), (1883, "Settled at Giverny"), (1920, "Began large-scale Water Lilies murals")],
  [("Impression, Sunrise", 1872, "Painting that gave Impressionism its name"), ("Water Lilies", 1906, "Series of approximately 250 paintings of his flower garden")],
  [("I would like to paint the way a bird sings.", "Attributed")])

p("pablo-picasso", "Pablo Picasso", "パブロ・ピカソ", 1881, 1973, ["es", "fr"], ["art"],
  "Pablo Picasso was a Spanish painter, sculptor, and ceramicist who co-founded Cubism and is widely regarded as one of the most influential artists of the 20th century.",
  "Picasso was born in Málaga, Spain. He showed prodigious talent from childhood and studied at art academies in Barcelona and Madrid before moving to Paris.",
  "Picasso's constant innovation through Blue, Rose, Cubist, and later periods transformed modern art. Guernica became a universal symbol of anti-war sentiment.",
  [(1901, "Blue Period began"), (1907, "Painted Les Demoiselles d'Avignon, launching Cubism"), (1937, "Painted Guernica"), (1961, "Married Jacqueline Roque")],
  [("Les Demoiselles d'Avignon", 1907, "Revolutionary painting that launched Cubism"), ("Guernica", 1937, "Anti-war masterpiece inspired by the bombing of a Basque town")],
  [("Every child is an artist. The problem is how to remain an artist once we grow up.", "Attributed")])

p("frida-kahlo", "Frida Kahlo", "フリーダ・カーロ", 1907, 1954, ["mx"], ["art"],
  "Frida Kahlo was a Mexican painter known for her self-portraits, works inspired by Mexican folk art, and her exploration of identity, pain, and the human body.",
  "Kahlo was born in Coyoacán, Mexico. A bus accident at age 18 left her with lifelong injuries. She began painting during her recovery and married Diego Rivera.",
  "Kahlo's intensely personal art explored identity, gender, class, and race in Mexican society. She became a feminist icon and one of the most recognized artists worldwide.",
  [(1925, "Bus accident; began painting during recovery"), (1929, "Married Diego Rivera"), (1938, "First solo exhibition in New York"), (1953, "First solo exhibition in Mexico")],
  [("The Two Fridas", 1939, "Double self-portrait exploring her dual identity"), ("Self-Portrait with Thorn Necklace and Hummingbird", 1940, "Iconic self-portrait symbolizing pain and resilience")],
  [("I paint myself because I am so often alone and because I am the subject I know best.", "Attributed")])

p("salvador-dali", "Salvador Dalí", "サルバドール・ダリ", 1904, 1989, ["es"], ["art"],
  "Salvador Dalí was a Spanish Surrealist artist renowned for his technical skill, precise draftsmanship, and striking bizarre imagery.",
  "Dalí was born in Figueres, Spain. He studied at the Royal Academy of Fine Arts in Madrid and joined the Surrealist group in Paris.",
  "Dalí's melting clocks and dreamlike landscapes became iconic images of Surrealism. His flamboyant personality and artistic versatility made him one of the most famous artists of the 20th century.",
  [(1929, "Joined the Surrealist group in Paris"), (1931, "Painted The Persistence of Memory"), (1940, "Moved to the United States"), (1974, "Opened the Dalí Theatre-Museum in Figueres")],
  [("The Persistence of Memory", 1931, "Iconic painting featuring melting watches in a dreamlike landscape")],
  [("Have no fear of perfection — you'll never reach it.", "Attributed")])

p("albrecht-durer", "Albrecht Dürer", "アルブレヒト・デューラー", 1471, 1528, ["de"], ["art"],
  "Albrecht Dürer was a German painter, printmaker, and theorist of the German Renaissance, known for his high-quality woodcuts and engravings.",
  "Dürer was born in Nuremberg, Germany. He was trained by his father, a goldsmith, and by Michael Wolgemut. He traveled to Italy, where the Renaissance deeply influenced his work.",
  "Dürer elevated the status of printmaking to a fine art. His engravings, woodcuts, and theoretical writings on proportion and perspective shaped Northern Renaissance art.",
  [(1494, "First trip to Italy"), (1498, "Published the Apocalypse woodcuts"), (1504, "Created Adam and Eve engraving"), (1514, "Created Melencolia I")],
  [("Melencolia I", 1514, "Enigmatic engraving considered one of the greatest prints ever made"), ("Rhinoceros", 1515, "Famous woodcut based on a written description of an Indian rhinoceros")],
  [("What beauty is, I know not, though it adheres to many things.", "Four Books on Human Proportion")])

p("johannes-vermeer", "Johannes Vermeer", "ヨハネス・フェルメール", 1632, 1675, ["nl"], ["art"],
  "Johannes Vermeer was a Dutch Baroque painter who specialized in domestic interior scenes of middle-class life, known for his masterful use of light and color.",
  "Vermeer was born in Delft, Netherlands. Little is known about his training. He worked as an art dealer and painter, producing only about 35 known paintings in his lifetime.",
  "Vermeer's paintings are treasured for their luminous light, meticulous composition, and serene beauty. His work was largely forgotten until rediscovery in the 19th century.",
  [(1653, "Became a master painter in Delft"), (1665, "Painted Girl with a Pearl Earring"), (1668, "Painted The Astronomer")],
  [("Girl with a Pearl Earring", 1665, "Masterpiece of portraiture known as the 'Mona Lisa of the North'"), ("The Art of Painting", 1668, "Vermeer's most ambitious work, an allegory of painting")],
  [("Painting is a silent poetry, and poetry is a painting that speaks.", "Attributed")])

p("caravaggio", "Caravaggio", "カラヴァッジョ", 1571, 1610, ["it"], ["art"],
  "Caravaggio was an Italian painter whose revolutionary use of dramatic lighting and realistic figures transformed European painting in the Baroque period.",
  "Born Michelangelo Merisi in Milan, he trained there and moved to Rome, where his work attracted both admiration and controversy due to his realism and violent temperament.",
  "Caravaggio's dramatic chiaroscuro technique influenced generations of painters. His radical naturalism brought sacred subjects to life with unprecedented immediacy and emotional power.",
  [(1592, "Arrived in Rome"), (1600, "Received first major public commission"), (1606, "Fled Rome after killing a man"), (1610, "Died at age 38 while fleeing")],
  [("The Calling of Saint Matthew", 1600, "Revolutionary painting using dramatic light to illuminate a biblical scene"), ("Judith Beheading Holofernes", 1599, "Shocking depiction of biblical violence")],
  [("All works, no matter what, are done the way I like them.", "Attributed")])

p("peter-paul-rubens", "Peter Paul Rubens", "ピーテル・パウル・ルーベンス", 1577, 1640, ["be"], ["art"],
  "Peter Paul Rubens was a Flemish artist and diplomat who was the most influential Baroque painter in Northern Europe.",
  "Rubens was born in Siegen, Germany, and grew up in Antwerp. He studied under several masters and spent eight years in Italy, absorbing Italian Renaissance art.",
  "Rubens's energetic compositions, rich color, and dynamic figures defined the Baroque style in Northern Europe. His large workshop produced an enormous body of work.",
  [(1600, "Traveled to Italy"), (1608, "Returned to Antwerp"), (1622, "Began Marie de' Medici cycle"), (1630, "Knighted by Charles I of England")],
  [("The Descent from the Cross", 1614, "Monumental altarpiece in Antwerp Cathedral"), ("Marie de' Medici Cycle", 1625, "24 paintings depicting the life of the French queen")],
  [("My passion comes from the heavens, not from earthly musings.", "Attributed")])

p("diego-velazquez", "Diego Velázquez", "ディエゴ・ベラスケス", 1599, 1660, ["es"], ["art"],
  "Diego Velázquez was a Spanish painter who was the leading artist of the Spanish Golden Age and one of the most important painters in Western art history.",
  "Velázquez was born in Seville. He trained under Francisco Pacheco and moved to Madrid, where he became court painter to King Philip IV.",
  "Velázquez's masterful handling of light, color, and perspective, especially in Las Meninas, influenced Impressionists and modern painters. He is considered a painter's painter.",
  [(1623, "Became court painter to Philip IV"), (1629, "First visit to Italy"), (1656, "Painted Las Meninas")],
  [("Las Meninas", 1656, "Complex group portrait considered one of the most analyzed paintings in Western art"), ("The Surrender of Breda", 1635, "Masterpiece depicting a moment of magnanimity in war")],
  [("I would rather be the first painter of common things than second in higher art.", "Attributed")])

p("francisco-goya", "Francisco Goya", "フランシスコ・ゴヤ", 1746, 1828, ["es"], ["art"],
  "Francisco Goya was a Spanish painter and printmaker regarded as the last of the Old Masters and the first of the moderns.",
  "Goya was born in Fuendetodos, Spain. He studied in Zaragoza and Madrid, eventually becoming court painter to the Spanish Crown.",
  "Goya's unflinching depictions of war, madness, and human folly anticipated modern art. His late 'Black Paintings' are among the most powerful works in Western art.",
  [(1786, "Became painter to the King of Spain"), (1793, "Became deaf after illness"), (1808, "Witnessed the French occupation of Spain"), (1819, "Created the Black Paintings")],
  [("The Third of May 1808", 1814, "Powerful anti-war painting depicting the execution of Spanish civilians"), ("Los Caprichos", 1799, "Series of 80 prints satirizing Spanish society")],
  [("The sleep of reason produces monsters.", "Los Caprichos")])

p("edouard-manet", "Édouard Manet", "エドゥアール・マネ", 1832, 1883, ["fr"], ["art"],
  "Édouard Manet was a French modernist painter who was one of the first 19th-century artists to paint modern life and a pivotal figure in the transition from Realism to Impressionism.",
  "Manet was born into a wealthy Parisian family. He studied under Thomas Couture and was influenced by Spanish masters, particularly Velázquez and Goya.",
  "Manet's radical compositions and bold brushwork shocked the art world and paved the way for Impressionism. His Olympia and Déjeuner sur l'herbe redefined what art could depict.",
  [(1863, "Exhibited Déjeuner sur l'herbe at the Salon des Refusés"), (1865, "Exhibited Olympia"), (1874, "Closely associated with Impressionists")],
  [("Olympia", 1863, "Provocative painting that challenged traditional depictions of the female nude"), ("Le Déjeuner sur l'herbe", 1863, "Controversial painting of a nude woman picnicking with clothed men")],
  [("There is only one true thing: instantly paint what you see.", "Attributed")])

p("auguste-renoir", "Pierre-Auguste Renoir", "ピエール＝オーギュスト・ルノワール", 1841, 1919, ["fr"], ["art"],
  "Pierre-Auguste Renoir was a French Impressionist painter known for his vibrant light, saturated color, and celebration of beauty, especially of the human figure.",
  "Renoir was born in Limoges, France. He began as a porcelain painter before studying at the École des Beaux-Arts in Paris, where he befriended Monet, Sisley, and Bazille.",
  "Renoir's joyful paintings of modern life, with their luminous flesh tones and shimmering light, became some of the most beloved images in Western art.",
  [(1874, "Exhibited at the first Impressionist exhibition"), (1876, "Painted Bal du moulin de la Galette"), (1881, "Traveled to Italy"), (1919, "Died at Cagnes-sur-Mer")],
  [("Bal du moulin de la Galette", 1876, "Joyous depiction of Parisian social life"), ("Luncheon of the Boating Party", 1881, "Masterpiece of light and convivial atmosphere")],
  [("Pain passes, but beauty remains.", "Attributed")])

p("paul-cezanne", "Paul Cézanne", "ポール・セザンヌ", 1839, 1906, ["fr"], ["art"],
  "Paul Cézanne was a French Post-Impressionist painter whose work laid the foundations for the transition from 19th-century Impressionism to 20th-century Cubism.",
  "Cézanne was born in Aix-en-Provence. He studied law before pursuing art in Paris, where he associated with the Impressionists but developed his own distinctive approach.",
  "Cézanne's treatment of form as geometric shapes and his technique of building color planes influenced Cubism and much of modern art. Picasso called him 'the father of us all.'",
  [(1861, "Moved to Paris"), (1874, "Exhibited at the first Impressionist exhibition"), (1895, "First solo exhibition"), (1906, "Died while painting outdoors")],
  [("Mont Sainte-Victoire series", 1885, "Multiple paintings of the mountain near Aix-en-Provence"), ("The Card Players", 1892, "Series of paintings depicting peasants playing cards")],
  [("Treat nature by the cylinder, the sphere, the cone.", "Letter to Émile Bernard, 1904")])

p("henri-matisse", "Henri Matisse", "アンリ・マティス", 1869, 1954, ["fr"], ["art"],
  "Henri Matisse was a French visual artist known for his use of color and his fluid, original draughtsmanship. He was a leading figure of Fauvism.",
  "Matisse was born in Le Cateau-Cambrésis, France. He studied law before turning to art after illness. He studied at the Académie Julian and the École des Beaux-Arts.",
  "Matisse's revolutionary use of color freed painting from the constraints of representation. His paper cut-outs in later life were a final burst of creative innovation.",
  [(1905, "Led the Fauvist movement"), (1908, "Published Notes of a Painter"), (1947, "Published Jazz, a book of cut-outs"), (1951, "Completed the Chapel of the Rosary in Vence")],
  [("The Dance", 1910, "Iconic painting of dancing figures embodying rhythm and movement"), ("Jazz", 1947, "Book of colorful paper cut-outs")],
  [("Creativity takes courage.", "Attributed")])

p("andy-warhol", "Andy Warhol", "アンディ・ウォーホル", 1928, 1987, ["us"], ["art"],
  "Andy Warhol was an American artist, film director, and producer who was a leading figure in the Pop Art movement.",
  "Warhol was born in Pittsburgh to Slovakian immigrant parents. He studied commercial art at Carnegie Tech and became a successful illustrator in New York before turning to fine art.",
  "Warhol's mass-production techniques and celebrity imagery challenged traditional distinctions between fine art and commercial art, transforming the art world.",
  [(1962, "Exhibited Campbell's Soup Cans"), (1963, "Established The Factory studio"), (1968, "Shot by Valerie Solanas"), (1987, "Died following gallbladder surgery")],
  [("Campbell's Soup Cans", 1962, "Series of 32 canvases depicting each variety of Campbell's soup"), ("Marilyn Diptych", 1962, "Silkscreen portrait of Marilyn Monroe")],
  [("In the future, everyone will be world-famous for 15 minutes.", "Attributed")])

p("jackson-pollock", "Jackson Pollock", "ジャクソン・ポロック", 1912, 1956, ["us"], ["art"],
  "Jackson Pollock was an American painter and a major figure in the abstract expressionist movement, known for his unique drip painting technique.",
  "Pollock was born in Cody, Wyoming. He studied at the Art Students League in New York under Thomas Hart Benton and was influenced by Surrealism and Mexican muralists.",
  "Pollock's radical drip paintings broke with all convention, creating art through gesture and movement. He became a symbol of American artistic freedom and innovation.",
  [(1943, "First solo exhibition at Peggy Guggenheim's gallery"), (1947, "Developed drip painting technique"), (1949, "Life magazine article made him famous"), (1956, "Died in car accident")],
  [("No. 5, 1948", 1948, "Large-scale drip painting exemplifying his revolutionary technique"), ("Autumn Rhythm", 1950, "Masterpiece of abstract expressionism")],
  [("Every good painter paints what he is.", "Attributed")])

p("wassily-kandinsky", "Wassily Kandinsky", "ワシリー・カンディンスキー", 1866, 1944, ["ru", "de", "fr"], ["art"],
  "Wassily Kandinsky was a Russian painter and art theorist generally credited as one of the pioneers of abstract art.",
  "Kandinsky was born in Moscow. He studied law and economics before moving to Munich at age 30 to study painting, eventually becoming a leading figure in modern art.",
  "Kandinsky's theoretical writings and abstract paintings freed art from representation. His belief that art could express spiritual reality through form and color influenced all subsequent abstract art.",
  [(1896, "Moved to Munich to study art"), (1910, "Painted first abstract watercolor"), (1911, "Co-founded Der Blaue Reiter"), (1922, "Joined the Bauhaus")],
  [("Concerning the Spiritual in Art", 1911, "Theoretical text arguing for the spiritual basis of abstract art"), ("Composition VII", 1913, "Complex abstract painting considered his masterpiece")],
  [("Color is the keyboard, the eyes are the hammers, the soul is the piano with many strings.", "Concerning the Spiritual in Art")])

p("gustav-klimt", "Gustav Klimt", "グスタフ・クリムト", 1862, 1918, ["at"], ["art"],
  "Gustav Klimt was an Austrian symbolist painter and one of the most prominent members of the Vienna Secession movement, known for his ornamental, gold-leaf paintings.",
  "Klimt was born in Baumgarten, near Vienna. He studied at the Vienna School of Arts and Crafts and became a leading figure in the Viennese art world.",
  "Klimt's ornamental style, blending Byzantine gold with erotic subjects, created a unique fusion of fine and decorative art. The Kiss became one of the most reproduced images in art.",
  [(1897, "Co-founded the Vienna Secession"), (1903, "Visited Ravenna; influenced by Byzantine mosaics"), (1907, "Painted The Kiss"), (1918, "Died during the flu pandemic")],
  [("The Kiss", 1907, "Iconic painting of an embracing couple covered in gold leaf"), ("Portrait of Adele Bloch-Bauer I", 1907, "The 'Golden Adele,' one of the most valuable paintings ever sold")],
  [("Whoever wants to know something about me ought to look carefully at my pictures.", "Attributed")])

p("edvard-munch", "Edvard Munch", "エドヴァルド・ムンク", 1863, 1944, ["no"], ["art"],
  "Edvard Munch was a Norwegian painter whose intensely evocative treatment of psychological themes built upon Symbolism and greatly influenced German Expressionism.",
  "Munch was born in Løten, Norway. His childhood was marked by illness and death in his family, which profoundly influenced his art.",
  "Munch's The Scream became a universal symbol of human anxiety. His exploration of psychological themes through distorted forms and vivid colors pioneered Expressionism.",
  [(1892, "Exhibition in Berlin caused scandal"), (1893, "Painted The Scream"), (1902, "Exhibited The Frieze of Life"), (1940, "Refused to cooperate with Nazi occupation")],
  [("The Scream", 1893, "Iconic painting of existential anxiety"), ("The Frieze of Life", 1902, "Series of paintings exploring love, anxiety, and death")],
  [("I do not paint what I see, but what I saw.", "Diary")])

p("katsushika-hokusai", "Katsushika Hokusai", "葛飾北斎", 1760, 1849, ["jp"], ["art"],
  "Katsushika Hokusai was a Japanese ukiyo-e painter and printmaker whose work profoundly influenced Western Impressionism and Art Nouveau.",
  "Hokusai was born in Edo (Tokyo). He studied under Katsukawa Shunshō and worked under many names throughout his long career, constantly reinventing his style.",
  "Hokusai's Great Wave became one of the most recognized images in art history. His work influenced Western artists including Monet, van Gogh, and Whistler.",
  [(1779, "Studied under Katsukawa Shunshō"), (1831, "Published Thirty-six Views of Mount Fuji"), (1834, "Published One Hundred Views of Mount Fuji")],
  [("The Great Wave off Kanagawa", 1831, "Iconic woodblock print from Thirty-six Views of Mount Fuji"), ("Thirty-six Views of Mount Fuji", 1831, "Series of landscape prints revolutionizing ukiyo-e")],
  [("If heaven had granted me five more years, I could have become a real painter.", "Attributed deathbed words")])

p("utagawa-hiroshige", "Utagawa Hiroshige", "歌川広重", 1797, 1858, ["jp"], ["art"],
  "Utagawa Hiroshige was a Japanese ukiyo-e artist famous for his landscape series, particularly The Fifty-three Stations of the Tōkaidō.",
  "Hiroshige was born in Edo to a samurai family. He trained as an ukiyo-e artist under Utagawa Toyohiro and became famous for his atmospheric landscape prints.",
  "Hiroshige's landscapes captured the poetry of nature and seasonal change. His work influenced European Impressionists and remains beloved for its beauty and sensitivity.",
  [(1831, "Traveled the Tōkaidō road"), (1834, "Published The Fifty-three Stations of the Tōkaidō"), (1856, "Published One Hundred Famous Views of Edo")],
  [("The Fifty-three Stations of the Tōkaidō", 1834, "Series of prints depicting stages along the major highway"), ("One Hundred Famous Views of Edo", 1856, "Celebrated series of landscape prints")],
  [("To paint is to feel the living breath of nature.", "Attributed")])

p("sandro-botticelli", "Sandro Botticelli", "サンドロ・ボッティチェッリ", 1445, 1510, ["it"], ["art"],
  "Sandro Botticelli was an Italian painter of the Early Renaissance, known for his mythological and religious paintings of delicate beauty.",
  "Botticelli was born in Florence. He was apprenticed to Fra Filippo Lippi and became associated with the Medici court, producing his most famous works under their patronage.",
  "Botticelli's Birth of Venus and Primavera are among the most celebrated paintings of the Renaissance. His graceful figures and poetic imagery embody the Florentine ideal of beauty.",
  [(1470, "Opened his own workshop"), (1482, "Painted Primavera"), (1485, "Painted The Birth of Venus"), (1481, "Contributed to the Sistine Chapel frescoes")],
  [("The Birth of Venus", 1485, "Iconic depiction of the goddess Venus emerging from the sea"), ("Primavera", 1482, "Allegorical painting celebrating spring")],
  [("Every painting is a voyage into a sacred harbour.", "Attributed")])

p("titian", "Titian", "ティツィアーノ", 1488, 1576, ["it"], ["art"],
  "Titian was the greatest Venetian painter of the 16th century, recognized as a master of color whose work influenced generations of Western artists.",
  "Titian was born in Pieve di Cadore, Italy. He studied under Giovanni Bellini and Giorgione in Venice, quickly establishing himself as the leading painter of the Venetian school.",
  "Titian's mastery of color and his innovative brushwork influenced Rubens, Velázquez, and Rembrandt. His portraits of popes, emperors, and mythological figures define Venetian art.",
  [(1516, "Became official painter of the Venetian Republic"), (1533, "Became painter to Emperor Charles V"), (1538, "Painted Venus of Urbino"), (1576, "Died during the plague in Venice")],
  [("Venus of Urbino", 1538, "Influential reclining nude that inspired Manet's Olympia"), ("Assumption of the Virgin", 1518, "Monumental altarpiece in the Frari church in Venice")],
  [("It is not bright colors but good drawing that makes figures beautiful.", "Attributed")])

p("el-greco", "El Greco", "エル・グレコ", 1541, 1614, ["gr", "es"], ["art"],
  "El Greco was a Greek painter, sculptor, and architect of the Spanish Renaissance whose visionary style anticipated Expressionism by centuries.",
  "Born Doménikos Theotokópoulos in Crete, he trained as an icon painter before studying in Venice and Rome. He settled in Toledo, Spain, where he created his greatest works.",
  "El Greco's elongated figures, dramatic lighting, and visionary compositions were rediscovered in the 20th century and recognized as precursors to modern Expressionism.",
  [(1567, "Left Crete for Venice"), (1577, "Settled in Toledo, Spain"), (1586, "Painted The Burial of the Count of Orgaz"), (1600, "Painted View of Toledo")],
  [("The Burial of the Count of Orgaz", 1586, "Masterpiece combining earthly funeral with heavenly vision"), ("View of Toledo", 1600, "One of the first landscape paintings in Western art")],
  [("I hold the imitation of color to be the greatest difficulty of art.", "Attributed")])

p("paul-gauguin", "Paul Gauguin", "ポール・ゴーギャン", 1848, 1903, ["fr"], ["art"],
  "Paul Gauguin was a French Post-Impressionist painter who abandoned European civilization to pursue a simpler life in Tahiti, where he created his most celebrated works.",
  "Gauguin was born in Paris and spent part of his childhood in Peru. He worked as a stockbroker before devoting himself full-time to painting in his mid-thirties.",
  "Gauguin's bold use of color, flat forms, and exotic subjects influenced Fauvism, Synthetism, and the Symbolist movement. His work challenged Western artistic conventions.",
  [(1882, "Left banking career to paint full-time"), (1888, "Worked with Van Gogh in Arles"), (1891, "Moved to Tahiti"), (1897, "Painted Where Do We Come From?")],
  [("Where Do We Come From? What Are We? Where Are We Going?", 1897, "Monumental painting exploring the meaning of existence"), ("Vision After the Sermon", 1888, "Painting that launched Synthetism")],
  [("Art is either plagiarism or revolution.", "Attributed")])

p("edgar-degas", "Edgar Degas", "エドガー・ドガ", 1834, 1917, ["fr"], ["art"],
  "Edgar Degas was a French Impressionist artist famous for his paintings, sculptures, and drawings of ballet dancers, racing scenes, and modern life.",
  "Degas was born in Paris to a wealthy family. He studied at the École des Beaux-Arts and traveled to Italy before becoming associated with the Impressionists.",
  "Degas's innovative compositions, influenced by photography and Japanese prints, captured the movement and spontaneity of modern life. His ballet paintings are among the most beloved in art.",
  [(1862, "Met Manet; began painting modern life"), (1874, "Exhibited at the first Impressionist exhibition"), (1881, "Created The Little Fourteen-Year-Old Dancer sculpture")],
  [("The Ballet Class", 1874, "One of many paintings depicting the world of Parisian ballet"), ("The Little Fourteen-Year-Old Dancer", 1881, "Revolutionary mixed-media sculpture")],
  [("Art is not what you see, but what you make others see.", "Attributed")])

p("marc-chagall", "Marc Chagall", "マルク・シャガール", 1887, 1985, ["by", "fr"], ["art"],
  "Marc Chagall was a Russian-French artist known for his dreamlike, fantastical paintings blending reality and fantasy, deeply rooted in Jewish folklore and Russian village life.",
  "Chagall was born in Vitebsk, Belarus. He studied in St. Petersburg and Paris, where he was influenced by Fauvism and Cubism while maintaining his unique poetic vision.",
  "Chagall's colorful, dreamlike imagery created a personal mythology that transcended artistic movements. His stained glass windows and murals adorn buildings worldwide.",
  [(1910, "Moved to Paris"), (1914, "Returned to Russia"), (1941, "Fled to the United States"), (1964, "Painted the ceiling of the Paris Opéra")],
  [("I and the Village", 1911, "Dreamlike painting of Russian village life"), ("Paris Opéra Ceiling", 1964, "Monumental painting celebrating music and dance")],
  [("In our life there is a single color, as on an artist's palette, which provides the meaning of life and art. It is the color of love.", "Attributed")])

p("georgia-o-keeffe", "Georgia O'Keeffe", "ジョージア・オキーフ", 1887, 1986, ["us"], ["art"],
  "Georgia O'Keeffe was an American artist known for her paintings of enlarged flowers, New York skyscrapers, and New Mexico landscapes, recognized as the Mother of American Modernism.",
  "O'Keeffe was born in Sun Prairie, Wisconsin. She studied at the Art Institute of Chicago and later in New York. She married photographer Alfred Stieglitz.",
  "O'Keeffe's monumental flower paintings and stark desert landscapes defined American modernism. Her independent spirit and long career made her an icon of American art.",
  [(1916, "Stieglitz exhibited her charcoal drawings"), (1924, "Married Alfred Stieglitz"), (1929, "First visit to New Mexico"), (1946, "Settled permanently in New Mexico")],
  [("Jimson Weed/White Flower No. 1", 1932, "Monumental flower painting that became one of the most expensive paintings by a woman"), ("Sky Above Clouds IV", 1965, "Largest painting, inspired by aerial views")],
  [("I found I could say things with color and shapes that I couldn't say any other way.", "Attributed")])

p("egon-schiele", "Egon Schiele", "エゴン・シーレ", 1890, 1918, ["at"], ["art"],
  "Egon Schiele was an Austrian Expressionist painter notable for his raw sexuality, distorted body shapes, and emotional intensity.",
  "Schiele was born in Tulln, Austria. He studied at the Vienna Academy of Fine Arts under Gustav Klimt's mentorship and quickly developed his own radical style.",
  "Schiele's expressive, often confrontational depictions of the human body broke taboos and expanded the boundaries of art. Despite dying at 28, he left a lasting mark on Expressionism.",
  [(1907, "Met Gustav Klimt"), (1909, "Left the Academy and co-founded the Neukunstgruppe"), (1912, "Arrested for obscenity; acquitted"), (1918, "Died in the flu pandemic")],
  [("Self-Portrait with Physalis", 1912, "Characteristic self-portrait with distorted pose and vivid color"), ("The Embrace", 1917, "Tender depiction of two intertwined figures")],
  [("Art cannot be modern. Art is primordially eternal.", "Attributed")])

p("jean-michel-basquiat", "Jean-Michel Basquiat", "ジャン＝ミシェル・バスキア", 1960, 1988, ["us"], ["art"],
  "Jean-Michel Basquiat was an American artist of Haitian and Puerto Rican descent who rose from New York City graffiti to international art stardom.",
  "Basquiat was born in Brooklyn, New York. He began as a graffiti artist using the tag SAMO and quickly attracted the attention of the art world.",
  "Basquiat's raw, powerful paintings combining text, imagery, and social commentary addressed race, class, and power. He became one of the most important artists of the late 20th century.",
  [(1977, "Began SAMO graffiti with Al Diaz"), (1981, "First solo exhibition"), (1983, "Collaborated with Andy Warhol"), (1988, "Died of a drug overdose at age 27")],
  [("Untitled (Skull)", 1981, "Iconic neo-expressionist painting"), ("Hollywood Africans", 1983, "Painting addressing racial stereotypes in the entertainment industry")],
  [("I don't think about art when I'm working. I try to think about life.", "Attributed")])

p("ai-weiwei", "Ai Weiwei", "艾未未", 1957, None, ["cn", "de"], ["art"],
  "Ai Weiwei is a Chinese contemporary artist and activist known for his architectural, sculptural, and social media work that challenges authority.",
  "Ai was born in Beijing. His father, the poet Ai Qing, was sent to a labor camp during the Cultural Revolution. Ai studied at the Beijing Film Academy and lived in New York in the 1980s.",
  "Ai Weiwei's provocative art and bold activism have made him one of the most influential contemporary artists. His work addresses human rights, freedom, and the refugee crisis.",
  [(1993, "Returned to China from New York"), (2008, "Investigated Sichuan earthquake school collapses"), (2011, "Detained by Chinese government for 81 days"), (2015, "Left China")],
  [("Sunflower Seeds", 2010, "Installation of 100 million handmade porcelain sunflower seeds"), ("Remembering", 2009, "9,000 children's backpacks on a building facade memorializing earthquake victims")],
  [("Everything is art. Everything is politics.", "Attributed")])

p("yayoi-kusama", "Yayoi Kusama", "草間彌生", 1929, None, ["jp"], ["art"],
  "Yayoi Kusama is a Japanese contemporary artist known for her polka dots, infinity rooms, and immersive installations that explore infinity and self-obliteration.",
  "Kusama was born in Matsumoto, Japan. She studied at the Kyoto City University of Arts before moving to New York in 1958, where she became part of the avant-garde scene.",
  "Kusama's Infinity Mirror Rooms and obsessive polka-dot motifs have made her one of the world's most popular living artists. Her work bridges Pop Art, Minimalism, and feminist art.",
  [(1958, "Moved to New York"), (1966, "Created first Infinity Mirror Room"), (1973, "Returned to Japan"), (1993, "Represented Japan at the Venice Biennale")],
  [("Infinity Mirror Rooms", 1965, "Immersive installation using mirrors to create infinite reflections"), ("Pumpkin", 1994, "Iconic polka-dotted pumpkin sculpture")],
  [("Our earth is only one polka dot among a million stars in the cosmos.", "Attributed")])

p("auguste-rodin", "Auguste Rodin", "オーギュスト・ロダン", 1840, 1917, ["fr"], ["art"],
  "Auguste Rodin was a French sculptor generally considered the founder of modern sculpture, breaking with traditional decorative traditions.",
  "Rodin was born in Paris. He was rejected by the École des Beaux-Arts three times and worked as a craftsman before achieving fame in his forties.",
  "Rodin's The Thinker, The Kiss, and The Gates of Hell transformed sculpture from decorative representation to expressive art. He is the bridge between classical and modern sculpture.",
  [(1875, "Traveled to Italy; studied Michelangelo"), (1880, "Commissioned to create The Gates of Hell"), (1882, "Created The Thinker"), (1898, "Exhibited The Kiss")],
  [("The Thinker", 1882, "Iconic sculpture of a man in deep contemplation"), ("The Kiss", 1882, "Marble sculpture celebrating romantic love")],
  [("I choose a block of marble and chop off whatever I don't need.", "Attributed")])

p("artemisia-gentileschi", "Artemisia Gentileschi", "アルテミジア・ジェンティレスキ", 1593, 1656, ["it"], ["art"],
  "Artemisia Gentileschi was an Italian Baroque painter who was one of the most accomplished painters of the early Baroque era and the first woman admitted to the Accademia del Disegno.",
  "Gentileschi was born in Rome, the daughter of painter Orazio Gentileschi. She learned painting from her father and was influenced by Caravaggio's dramatic style.",
  "Gentileschi's powerful depictions of strong women from myth and the Bible, painted with Caravaggesque drama, have been celebrated as feminist masterpieces.",
  [(1611, "Painted Susanna and the Elders"), (1612, "Painted Judith Slaying Holofernes"), (1616, "First woman admitted to the Accademia del Disegno"), (1630, "Moved to Naples")],
  [("Judith Slaying Holofernes", 1612, "Powerful depiction of the biblical heroine killing the Assyrian general"), ("Self-Portrait as the Allegory of Painting", 1638, "Self-portrait as the personification of art")],
  [("As long as I live, I will have control over my being.", "Letter, 1649")])

p("banksy", "Banksy", "バンクシー", 1974, None, ["gb"], ["art"],
  "Banksy is an anonymous England-based street artist, political activist, and film director whose satirical street art combines dark humor with social commentary.",
  "Banksy's true identity remains unverified. He is believed to have grown up in Bristol and emerged from the Bristol underground scene in the 1990s.",
  "Banksy's subversive street art has made political art accessible to millions worldwide. His works on walls, buildings, and bridges challenge authority, consumerism, and war.",
  [(2002, "Published Banging Your Head Against a Brick Wall"), (2005, "Created unauthorized artworks in major museums"), (2010, "Directed Exit Through the Gift Shop"), (2018, "Shredded Girl with Balloon at auction")],
  [("Girl with Balloon", 2002, "Stencil graffiti of a girl reaching for a heart-shaped balloon"), ("Exit Through the Gift Shop", 2010, "Documentary film about street art")],
  [("Art should comfort the disturbed and disturb the comfortable.", "Attributed")])

p("diego-rivera", "Diego Rivera", "ディエゴ・リベラ", 1886, 1957, ["mx"], ["art"],
  "Diego Rivera was a Mexican muralist whose large-scale public murals helped establish the Mexican muralism movement and brought art to the masses.",
  "Rivera was born in Guanajuato, Mexico. He studied in Mexico City and Europe, where he was influenced by Cubism and Renaissance frescoes before returning to Mexico.",
  "Rivera's monumental murals depicting Mexican history, culture, and social struggles brought art to the public and influenced the development of public art worldwide.",
  [(1907, "Traveled to Europe"), (1921, "Began mural program in Mexico"), (1929, "Married Frida Kahlo"), (1933, "Man at the Crossroads mural controversy at Rockefeller Center")],
  [("Man at the Crossroads", 1933, "Controversial mural at Rockefeller Center destroyed for including Lenin"), ("History of Mexico murals", 1929, "Epic murals in the National Palace")],
  [("I paint what I see.", "Attributed")])

p("gustave-courbet", "Gustave Courbet", "ギュスターヴ・クールベ", 1819, 1877, ["fr"], ["art"],
  "Gustave Courbet was a French painter who led the Realist movement in 19th-century art, rejecting Romanticism in favor of depicting ordinary life.",
  "Courbet was born in Ornans, France. He was largely self-taught, studying old masters in the Louvre and developing his own distinctive realistic style.",
  "Courbet's insistence on painting ordinary subjects with the grandeur previously reserved for history painting launched the Realist movement and paved the way for Impressionism and modern art.",
  [(1849, "Exhibited The Stone Breakers"), (1855, "Organized Pavilion of Realism"), (1866, "Painted The Origin of the World")],
  [("A Burial at Ornans", 1850, "Large-scale painting of a provincial funeral that shocked the Parisian art world"), ("The Artist's Studio", 1855, "Allegorical painting of his creative life")],
  [("I have studied the art of the masters and the art of the moderns, avoiding any preconceived system.", "Realist Manifesto")])

p("piet-mondrian", "Piet Mondrian", "ピート・モンドリアン", 1872, 1944, ["nl", "us"], ["art"],
  "Piet Mondrian was a Dutch painter and art theorist who was a pioneer of abstract art and a leading contributor to the De Stijl movement.",
  "Mondrian was born in Amersfoort, Netherlands. He studied at the Rijksakademie in Amsterdam and evolved through naturalism, Impressionism, and Cubism toward pure abstraction.",
  "Mondrian's grid paintings of primary colors and black lines became icons of modernism. His Neo-Plasticism philosophy influenced architecture, design, and fashion.",
  [(1911, "Moved to Paris; influenced by Cubism"), (1917, "Co-founded De Stijl movement"), (1920, "Published Neo-Plasticism manifesto"), (1940, "Moved to New York")],
  [("Composition with Red, Blue, and Yellow", 1930, "Iconic grid painting embodying his Neo-Plastic principles"), ("Broadway Boogie Woogie", 1942, "Late painting inspired by New York and jazz")],
  [("The position of the artist is humble. He is essentially a channel.", "Attributed")])

p("marcel-duchamp", "Marcel Duchamp", "マルセル・デュシャン", 1887, 1968, ["fr", "us"], ["art"],
  "Marcel Duchamp was a French-American painter, sculptor, and chess player whose work challenged conventional ideas about what constitutes art.",
  "Duchamp was born in Blainville-Crevon, France, into a family of artists. He studied in Paris and became involved in Cubism and Dada before moving to New York.",
  "Duchamp's readymades and conceptual approach to art challenged the fundamental nature of art objects and influenced virtually every art movement of the 20th century.",
  [(1912, "Painted Nude Descending a Staircase"), (1913, "Created first readymade — Bicycle Wheel"), (1917, "Submitted Fountain to the Society of Independent Artists"), (1923, "Largely abandoned art for chess")],
  [("Fountain", 1917, "Urinal submitted as sculpture that became the most influential artwork of the 20th century"), ("Nude Descending a Staircase, No. 2", 1912, "Cubist-Futurist painting that caused a sensation")],
  [("I have forced myself to contradict myself in order to avoid conforming to my own taste.", "Attributed")])

if __name__ == '__main__':
    write_people(P)
