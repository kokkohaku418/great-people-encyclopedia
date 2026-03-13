#!/usr/bin/env python3
"""Supplement batch 4: final push to reach 1000+."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
p = lambda *a, **k: P.append(person(*a, **k))

# === MIXED CATEGORIES ===
p("confucius", "Confucius", "孔子", -551, -479, ["cn"], ["philosophy"],
  "Confucius was a Chinese philosopher whose teachings profoundly influenced the culture and history of East Asia and the world.",
  "Confucius was born in Qufu, State of Lu. He came from a noble but impoverished family and worked as a teacher and minor government official.",
  "Confucianism shaped Chinese civilization for over two millennia. Confucius's teachings on ethics, governance, and human relationships remain foundational to East Asian culture.",
  [(-530, "Began teaching"), (-497, "Traveled through Chinese states seeking ideal governance"), (-479, "Died in Lu")],
  [("Analerta (Lunyu)", -400, "Collection of Confucius's sayings and ideas compiled by his disciples")],
  [("It does not matter how slowly you go as long as you do not stop.", "Attributed")])

p("laozi", "Laozi", "老子", -601, -531, ["cn"], ["philosophy"],
  "Laozi was a legendary Chinese philosopher and writer, traditionally regarded as the founder of Taoism and author of the Tao Te Ching.",
  "According to tradition, Laozi was an archivist at the Zhou court. Disillusioned, he departed westward and wrote the Tao Te Ching before disappearing.",
  "Laozi's Tao Te Ching is one of the most translated and influential texts in world literature, offering a philosophy of harmony, simplicity, and the natural way.",
  [(-531, "Traditionally wrote the Tao Te Ching")],
  [("Tao Te Ching", -531, "Classic text of Chinese philosophy on the Tao (the Way)")],
  [("A journey of a thousand miles begins with a single step.", "Tao Te Ching")])

p("sun-tzu", "Sun Tzu", "孫子", -544, -496, ["cn"], ["politics"],
  "Sun Tzu was a Chinese military strategist, philosopher, and author of The Art of War, one of the most influential treatises on military strategy.",
  "Little is known about Sun Tzu's life. He is traditionally identified as a military advisor to the King of Wu during the Spring and Autumn Period.",
  "The Art of War has influenced military strategy, business, and competitive thinking for over two millennia across cultures worldwide.",
  [(-512, "Served as military advisor to King Helü of Wu")],
  [("The Art of War", -500, "Treatise on military strategy and tactics")],
  [("The supreme art of war is to subdue the enemy without fighting.", "The Art of War")])

p("avicenna", "Avicenna", "イブン・スィーナー", 980, 1037, ["ir"], ["philosophy", "biology"],
  "Avicenna was a Persian polymath who is regarded as one of the most significant physicians, astronomers, thinkers, and writers of the Islamic Golden Age.",
  "Avicenna was born near Bukhara in present-day Uzbekistan. He was a child prodigy who mastered medicine by age 18 and served as a physician to various rulers.",
  "Avicenna's Canon of Medicine was the standard medical text in Europe and the Islamic world for centuries. His philosophical works influenced both Islamic and Western thought.",
  [(1012, "Began writing The Canon of Medicine"), (1020, "Completed The Book of Healing"), (1025, "Completed The Canon of Medicine")],
  [("The Canon of Medicine", 1025, "Comprehensive medical encyclopedia used for centuries"), ("The Book of Healing", 1020, "Encyclopedia of philosophy and science")],
  [("The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes.", "The Canon of Medicine")])

p("al-khwarizmi", "Al-Khwarizmi", "アル＝フワーリズミー", 780, 850, ["ir", "iq"], ["mathematics"],
  "Al-Khwarizmi was a Persian mathematician and astronomer whose works introduced Hindu-Arabic numerals and algebra to Europe.",
  "Al-Khwarizmi was born in Khwarezm, in present-day Uzbekistan. He worked at the House of Wisdom in Baghdad during the Islamic Golden Age.",
  "Al-Khwarizmi's works gave us the words 'algebra' and 'algorithm.' His introduction of Hindu-Arabic numerals transformed mathematics and commerce worldwide.",
  [(820, "Published The Compendious Book on Calculation by Completion and Balancing"), (825, "Published On the Calculation with Hindu Numerals")],
  [("The Compendious Book on Calculation by Completion and Balancing", 820, "Foundational text of algebra")],
  [("When I consider what people generally want in calculating, I found that it always is a number.", "The Compendious Book")])

p("omar-khayyam", "Omar Khayyam", "ウマル・ハイヤーム", 1048, 1131, ["ir"], ["mathematics", "literature"],
  "Omar Khayyam was a Persian mathematician, astronomer, and poet who made important contributions to algebra and is famous for the Rubaiyat.",
  "Khayyam was born in Nishapur, Persia. He studied under leading scholars and became renowned for his mathematical and astronomical work.",
  "Khayyam classified and solved cubic equations, reformed the Persian calendar with remarkable accuracy, and his Rubaiyat became one of the world's most beloved poetry collections.",
  [(1070, "Published Treatise on Demonstration of Problems of Algebra"), (1079, "Developed the Jalali calendar"), (1120, "Wrote the Rubaiyat poems")],
  [("Treatise on Algebra", 1070, "Classification and geometric solution of cubic equations"), ("Rubaiyat", 1120, "Collection of quatrains translated by Edward FitzGerald")],
  [("A loaf of bread, a jug of wine, and thou.", "Rubaiyat")])

p("ibn-khaldun", "Ibn Khaldun", "イブン・ハルドゥーン", 1332, 1406, ["tn", "eg"], ["philosophy", "politics"],
  "Ibn Khaldun was a North African Arab sociologist, philosopher, and historian who is considered a founding father of modern sociology and historiography.",
  "Ibn Khaldun was born in Tunis to a prominent family originally from Seville. He served various rulers in North Africa before settling in Cairo as a judge.",
  "Ibn Khaldun's Muqaddimah introduced a scientific approach to history and developed concepts of social cohesion, economic cycles, and the rise and fall of civilizations.",
  [(1375, "Began writing the Muqaddimah"), (1377, "Completed the Muqaddimah"), (1382, "Moved to Cairo as a teacher and judge"), (1401, "Met Tamerlane outside Damascus")],
  [("Muqaddimah", 1377, "Introduction to history that founded sociology as a discipline")],
  [("Geography is fate.", "Muqaddimah")])

p("rumi", "Rumi", "ルーミー", 1207, 1273, ["af", "tr"], ["literature", "philosophy"],
  "Rumi was a 13th-century Persian poet, Sufi mystic, and theologian whose spiritual poetry has made him one of the most popular and best-selling poets in the world.",
  "Rumi was born in Balkh, in present-day Afghanistan. His family fled the Mongol invasions, eventually settling in Konya, Turkey.",
  "Rumi's poetry on love, spirituality, and the human condition transcends cultural and religious boundaries. His Masnavi is considered one of the greatest works of mystical literature.",
  [(1244, "Met Shams-i-Tabrizi, transforming his life"), (1248, "Began composing the Diwan-e Shams"), (1258, "Began composing the Masnavi")],
  [("Masnavi", 1258, "Six-volume poem of spiritual teaching"), ("Diwan-e Shams-e Tabrizi", 1248, "Collection of lyric poems dedicated to his spiritual companion")],
  [("The wound is the place where the Light enters you.", "Attributed")])

p("murasaki-shikibu", "Murasaki Shikibu", "紫式部", 978, 1014, ["jp"], ["literature"],
  "Murasaki Shikibu was a Japanese novelist, poet, and lady-in-waiting at the Imperial court, author of The Tale of Genji, considered the world's first novel.",
  "Murasaki was born into a lesser branch of the powerful Fujiwara clan. She served at the court of Empress Akiko and drew on court life for her novel.",
  "The Tale of Genji, written around the year 1000, is considered the world's first novel and a masterpiece of Japanese literature, exploring love, loss, and court intrigue.",
  [(1000, "Began writing The Tale of Genji"), (1005, "Entered service at the imperial court"), (1008, "Wrote the Murasaki Shikibu Diary")],
  [("The Tale of Genji", 1000, "Considered the world's first novel, depicting court life in Heian Japan")],
  [("The truth is that one writes not for others, but for oneself.", "Murasaki Shikibu Diary")])

p("sei-shonagon", "Sei Shōnagon", "清少納言", 966, 1025, ["jp"], ["literature"],
  "Sei Shōnagon was a Japanese author and court lady who served Empress Teishi. She is best known for The Pillow Book, a collection of observations and reflections.",
  "Sei Shōnagon was born into a family of poets. She served at the court of Empress Teishi and wrote her famous work during her years at court.",
  "The Pillow Book is one of the most important works of Japanese literature, offering witty, frank observations on court life, nature, and human behavior.",
  [(993, "Entered service at the imperial court"), (1000, "Wrote The Pillow Book")],
  [("The Pillow Book", 1002, "Collection of observations, poetry, and personal reflections on Heian court life")],
  [("In spring it is the dawn that is most beautiful.", "The Pillow Book")])

p("matsuo-basho", "Matsuo Bashō", "松尾芭蕉", 1644, 1694, ["jp"], ["literature"],
  "Matsuo Bashō was a Japanese poet who is recognized as the greatest master of haiku, elevating the form from comic verse to serious literary art.",
  "Bashō was born Matsuo Kinsaku in Ueno, Iga Province. He served a local lord before becoming a wandering poet, traveling throughout Japan.",
  "Bashō transformed haiku into a profound art form. His travel journals and poems capture the essence of nature and human experience in just seventeen syllables.",
  [(1672, "Moved to Edo (Tokyo) to pursue poetry"), (1680, "Established the Bashō style of haiku"), (1689, "Completed The Narrow Road to the Deep North")],
  [("The Narrow Road to the Deep North", 1689, "Travel journal combining prose and haiku, a masterpiece of Japanese literature")],
  [("An old silent pond / A frog jumps into the pond — / Splash! Silence again.", "Famous haiku")])

p("ibn-battuta", "Ibn Battuta", "イブン・バットゥータ", 1304, 1369, ["ma"], ["literature"],
  "Ibn Battuta was a Moroccan scholar and explorer who traveled over 75,000 miles across the medieval Islamic world and beyond, more than any traveler before the Steam Age.",
  "Ibn Battuta was born in Tangier, Morocco. He set out on his first pilgrimage to Mecca at age 21 and continued traveling for nearly 30 years.",
  "Ibn Battuta's Rihla (Travels) provides an invaluable account of 14th-century civilization across Africa, the Middle East, Central Asia, Southeast Asia, and China.",
  [(1325, "Left Tangier on pilgrimage to Mecca"), (1332, "Traveled to India and served as judge in Delhi"), (1345, "Traveled to China"), (1355, "Dictated the Rihla")],
  [("Rihla (The Travels)", 1355, "Detailed account of travels across the medieval world")],
  [("Traveling — it leaves you speechless, then turns you into a storyteller.", "Attributed")])

p("leonhard-euler-dup-check", "Pierre de Fermat", "ピエール・ド・フェルマー", 1601, 1665, ["fr"], ["mathematics"],
  "Pierre de Fermat was a French mathematician who is given credit for early developments that led to infinitesimal calculus and is famous for Fermat's Last Theorem.",
  "Fermat was born in Beaumont-de-Lomagne, France. He was a lawyer and magistrate who practiced mathematics as an amateur, making foundational contributions to number theory.",
  "Fermat's contributions to number theory, probability, and analytic geometry were fundamental. His Last Theorem, scribbled in a margin, remained unproven for 358 years.",
  [(1636, "Developed methods of analytic geometry"), (1637, "Wrote Fermat's Last Theorem in a margin"), (1654, "Corresponded with Pascal on probability")],
  [("Fermat's Last Theorem", 1637, "Conjecture that no three positive integers satisfy a^n + b^n = c^n for n > 2")],
  [("I have discovered a truly marvelous proof of this, which this margin is too narrow to contain.", "Margin note, Arithmetica")])

p("blaise-pascal", "Blaise Pascal", "ブレーズ・パスカル", 1623, 1662, ["fr"], ["mathematics", "philosophy"],
  "Blaise Pascal was a French mathematician, physicist, inventor, and religious philosopher who made pioneering contributions to probability theory and computing.",
  "Pascal was born in Clermont-Ferrand, France. A child prodigy, he wrote a significant treatise on conic sections at age 16 and built a mechanical calculator at 19.",
  "Pascal's contributions to probability theory, his invention of the mechanical calculator, and his philosophical Pensées made him one of the most versatile minds of the 17th century.",
  [(1642, "Built the Pascaline mechanical calculator"), (1654, "Corresponded with Fermat on probability"), (1656, "Published Lettres Provinciales"), (1670, "Pensées published posthumously")],
  [("Pensées", 1670, "Collection of philosophical fragments on religion and human nature"), ("Pascaline", 1642, "One of the first mechanical calculators")],
  [("The heart has its reasons which reason knows nothing of.", "Pensées")])

p("gottfried-leibniz", "Gottfried Wilhelm Leibniz", "ゴットフリート・ヴィルヘルム・ライプニッツ", 1646, 1716, ["de"], ["mathematics", "philosophy"],
  "Gottfried Wilhelm Leibniz was a German polymath who independently invented calculus, developed binary number systems, and made contributions to logic and philosophy.",
  "Leibniz was born in Leipzig, Germany. He studied law, philosophy, and mathematics, and served as a diplomat and librarian while conducting his intellectual work.",
  "Leibniz's independent invention of calculus, his binary arithmetic system, and his philosophical optimism profoundly influenced mathematics, computer science, and philosophy.",
  [(1666, "Published De Arte Combinatoria"), (1675, "Developed calculus notation"), (1684, "Published first calculus paper"), (1714, "Published Monadology")],
  [("Monadology", 1714, "Philosophical work on the nature of reality"), ("Nova Methodus", 1684, "First published account of differential calculus")],
  [("This is the best of all possible worlds.", "Theodicy")])

p("rene-descartes", "René Descartes", "ルネ・デカルト", 1596, 1650, ["fr", "nl"], ["mathematics", "philosophy"],
  "René Descartes was a French philosopher, mathematician, and scientist who is considered the father of modern Western philosophy.",
  "Descartes was born in La Haye en Touraine, France. He studied at a Jesuit college and traveled widely before settling in the Netherlands to write.",
  "Descartes's 'I think, therefore I am' is perhaps the most famous statement in philosophy. His analytical geometry united algebra and geometry, enabling modern mathematics.",
  [(1637, "Published Discourse on the Method"), (1637, "Published La Géométrie, founding analytic geometry"), (1641, "Published Meditations on First Philosophy"), (1649, "Moved to Sweden at Queen Christina's invitation")],
  [("Meditations on First Philosophy", 1641, "Foundational work of modern philosophy"), ("Discourse on the Method", 1637, "Introduction to his philosophical method and analytic geometry")],
  [("I think, therefore I am.", "Discourse on the Method")])

p("baruch-spinoza", "Baruch Spinoza", "バルーフ・スピノザ", 1632, 1677, ["nl"], ["philosophy"],
  "Baruch Spinoza was a Dutch philosopher of Portuguese-Jewish origin who laid the groundwork for the Enlightenment and modern biblical criticism.",
  "Spinoza was born in Amsterdam to a family of Sephardic Jews. He was excommunicated from the Jewish community for his radical philosophical views and earned his living as a lens grinder.",
  "Spinoza's radical monism, identifying God with nature, and his advocacy for freedom of thought influenced the Enlightenment, German Idealism, and modern secular thought.",
  [(1656, "Excommunicated from the Jewish community"), (1670, "Published Theologico-Political Treatise anonymously"), (1677, "Ethics published posthumously")],
  [("Ethics", 1677, "Philosophical masterwork presented in geometric order"), ("Theologico-Political Treatise", 1670, "Defense of freedom of thought and biblical criticism")],
  [("The highest activity a human being can attain is learning for understanding, because to understand is to be free.", "Attributed")])

p("voltaire", "Voltaire", "ヴォルテール", 1694, 1778, ["fr"], ["philosophy", "literature"],
  "Voltaire was a French Enlightenment writer, historian, and philosopher famous for his wit, his attacks on the Catholic Church, and his advocacy of freedom of speech.",
  "Born François-Marie Arouet in Paris, he adopted the pen name Voltaire. He was imprisoned in the Bastille and spent years in exile in England and at Frederick the Great's court.",
  "Voltaire's advocacy of civil liberties, freedom of religion, and separation of church and state influenced the French and American revolutions and the development of liberal democracy.",
  [(1726, "Exiled to England; studied English thought"), (1734, "Published Letters on the English"), (1759, "Published Candide"), (1764, "Published Philosophical Dictionary")],
  [("Candide", 1759, "Satirical novella attacking philosophical optimism"), ("Philosophical Dictionary", 1764, "Encyclopedia of philosophical thought")],
  [("I disapprove of what you say, but I will defend to the death your right to say it.", "Attributed by Evelyn Beatrice Hall")])

p("jean-jacques-rousseau", "Jean-Jacques Rousseau", "ジャン＝ジャック・ルソー", 1712, 1778, ["ch", "fr"], ["philosophy"],
  "Jean-Jacques Rousseau was a Genevan philosopher whose ideas about education, nature, and the social contract influenced the French Revolution and modern political thought.",
  "Rousseau was born in Geneva. He was largely self-educated, working various jobs before achieving fame with his writings on inequality and education.",
  "Rousseau's social contract theory and ideas about the general will shaped modern democracy. His educational philosophy influenced progressive education movements.",
  [(1750, "Won prize for Discourse on the Arts and Sciences"), (1755, "Published Discourse on Inequality"), (1762, "Published The Social Contract and Émile")],
  [("The Social Contract", 1762, "Political philosophy arguing for popular sovereignty"), ("Émile", 1762, "Treatise on education following natural development")],
  [("Man is born free, and everywhere he is in chains.", "The Social Contract")])

p("montesquieu", "Montesquieu", "モンテスキュー", 1689, 1755, ["fr"], ["philosophy", "politics"],
  "Montesquieu was a French judge, man of letters, and political philosopher whose work on the separation of powers influenced modern constitutional government.",
  "Born Charles-Louis de Secondat in La Brède, France, he inherited a noble title and judicial position. He traveled widely in Europe, studying different systems of government.",
  "Montesquieu's theory of the separation of powers directly influenced the United States Constitution and constitutional governments worldwide.",
  [(1721, "Published Persian Letters"), (1734, "Published Considerations on the Causes of the Grandeur and Decadence of the Romans"), (1748, "Published The Spirit of the Laws")],
  [("The Spirit of the Laws", 1748, "Monumental work on political theory and the separation of powers")],
  [("There is no greater tyranny than that which is perpetrated under the shield of the law and in the name of justice.", "The Spirit of the Laws")])

p("john-locke", "John Locke", "ジョン・ロック", 1632, 1704, ["gb"], ["philosophy"],
  "John Locke was an English philosopher and physician, widely regarded as the father of liberalism, whose ideas on government influenced modern democratic theory.",
  "Locke was born in Wrington, Somerset. He studied at Christ Church, Oxford, and became physician and advisor to the Earl of Shaftesbury.",
  "Locke's theories of natural rights, government by consent, and the social contract directly influenced the American Declaration of Independence and the French Revolution.",
  [(1689, "Published Two Treatises of Government"), (1689, "Published An Essay Concerning Human Understanding"), (1693, "Published Some Thoughts Concerning Education")],
  [("Two Treatises of Government", 1689, "Defense of natural rights and government by consent"), ("An Essay Concerning Human Understanding", 1689, "Foundational work in empiricist epistemology")],
  [("No man's knowledge here can go beyond his experience.", "An Essay Concerning Human Understanding")])

p("adam-smith", "Adam Smith", "アダム・スミス", 1723, 1790, ["gb"], ["philosophy"],
  "Adam Smith was a Scottish economist and philosopher who is considered the father of modern economics and author of The Wealth of Nations.",
  "Smith was born in Kirkcaldy, Scotland. He studied at the University of Glasgow and Oxford, becoming professor of moral philosophy at Glasgow.",
  "Smith's The Wealth of Nations established economics as a discipline and advocated for free markets, the division of labor, and limited government intervention.",
  [(1759, "Published The Theory of Moral Sentiments"), (1776, "Published The Wealth of Nations")],
  [("The Wealth of Nations", 1776, "Foundational work of modern economics"), ("The Theory of Moral Sentiments", 1759, "Philosophical work on human sympathy and moral judgment")],
  [("It is not from the benevolence of the butcher, the brewer, or the baker that we expect our dinner, but from their regard to their own interest.", "The Wealth of Nations")])

p("thomas-hobbes", "Thomas Hobbes", "トマス・ホッブズ", 1588, 1679, ["gb"], ["philosophy"],
  "Thomas Hobbes was an English philosopher best known for his political philosophy, especially his masterwork Leviathan.",
  "Hobbes was born in Westport, Wiltshire. He studied at Oxford and served as tutor to the Cavendish family, traveling throughout Europe.",
  "Hobbes's social contract theory argued that people surrender freedom to a sovereign to escape the state of nature. Leviathan remains foundational to political philosophy.",
  [(1640, "Published The Elements of Law"), (1642, "Published De Cive"), (1651, "Published Leviathan")],
  [("Leviathan", 1651, "Classic work on political philosophy and the social contract")],
  [("The life of man: solitary, poor, nasty, brutish, and short.", "Leviathan")])

p("marcus-aurelius", "Marcus Aurelius", "マルクス・アウレリウス", 121, 180, ["it"], ["philosophy", "politics"],
  "Marcus Aurelius was a Roman emperor and Stoic philosopher whose Meditations is one of the most important works of Stoic philosophy.",
  "Marcus Aurelius was born in Rome. He was adopted by Emperor Antoninus Pius and succeeded him, ruling during a period of wars and plagues.",
  "Marcus Aurelius's Meditations, written as personal reflections during military campaigns, remains one of the most widely read works of philosophy and a guide to Stoic living.",
  [(161, "Became Roman Emperor"), (166, "Began the Marcomannic Wars"), (170, "Began writing the Meditations"), (180, "Died during military campaign")],
  [("Meditations", 170, "Personal reflections on Stoic philosophy written during military campaigns")],
  [("The happiness of your life depends upon the quality of your thoughts.", "Meditations")])

p("epictetus", "Epictetus", "エピクテトス", 55, 135, ["gr"], ["philosophy"],
  "Epictetus was a Greek Stoic philosopher who was born into slavery but became one of the most influential teachers of Stoicism.",
  "Epictetus was born in Hierapolis, Phrygia, as a slave. He was freed after Nero's death, studied under Musonius Rufus, and opened his own school in Nicopolis.",
  "Epictetus's teachings on controlling what is within our power and accepting what is not became a cornerstone of Stoic philosophy, influencing Marcus Aurelius and modern cognitive therapy.",
  [(89, "Banished from Rome by Domitian"), (95, "Established philosophical school in Nicopolis"), (108, "Discourses recorded by Arrian")],
  [("Discourses", 108, "Records of Epictetus's philosophical teachings"), ("Enchiridion", 108, "Handbook summarizing his Stoic philosophy")],
  [("It's not what happens to you, but how you react to it that matters.", "Discourses")])

if __name__ == '__main__':
    for entry in P:
        if entry['id'] == 'leonhard-euler-dup-check':
            entry['id'] = 'pierre-de-fermat'
    write_people(P)
