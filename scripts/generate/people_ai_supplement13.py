#!/usr/bin/env python3
"""Supplement batch 13: final push to 1000+ with dedup."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from people_ai_helper import person, write_people

P = []
PEOPLE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'people')
existing = {f.replace('.json', '') for f in os.listdir(PEOPLE_DIR) if f.endswith('.json')} if os.path.exists(PEOPLE_DIR) else set()
def add(id, *a, **k):
    if id not in existing:
        P.append(person(id, *a, **k))

# EXPLORERS
add("marco-polo", "Marco Polo", "マルコ・ポーロ", 1254, 1324, ["it"], ["literature"],
  "Marco Polo was a Venetian merchant and explorer whose travels to Asia were recorded in one of the most influential travel books in history.", "Born in Venice to a merchant family.", "His accounts introduced Europeans to Central Asia and China.",
  [(1271, "Departed for Asia"), (1295, "Returned to Venice"), (1298, "Dictated his travels in prison")],
  [("The Travels of Marco Polo", 1300, "Account of his journeys through Asia")],
  [("I have not told half of what I saw.", "Attributed")])

add("ibn-sina-medicine", "Avicenna (Medical)", "イブン・スィーナー（医学）", 980, 1037, ["ir"], ["biology"],
  "Avicenna wrote the Canon of Medicine, the most influential medical textbook for centuries.", "Born near Bukhara in present-day Uzbekistan.", "The Canon of Medicine was used as a standard text in European universities until the 17th century.",
  [(1012, "Began writing the Canon of Medicine"), (1025, "Completed the Canon of Medicine")],
  [("The Canon of Medicine", 1025, "Comprehensive medical encyclopedia")],
  [("Medicine is not one of the difficult sciences.", "The Canon of Medicine")])

add("james-cook", "James Cook", "ジェームズ・クック", 1728, 1779, ["gb"], ["engineering"],
  "James Cook was a British explorer and navigator who made three voyages to the Pacific Ocean.", "Born in Marton, Yorkshire to a farming family.", "His voyages added much to European knowledge of the Pacific.",
  [(1769, "First voyage to observe Transit of Venus"), (1770, "Charted coast of Australia"), (1779, "Killed in Hawaii")],
  [("Charts of the Pacific", 1770, "Detailed navigation charts of the Pacific Ocean")],
  [("Ambition leads me farther than any other man has been before me.", "Journal")])

add("ferdinand-magellan", "Ferdinand Magellan", "フェルディナンド・マゼラン", 1480, 1521, ["pt", "es"], ["engineering"],
  "Ferdinand Magellan organized the first circumnavigation of the Earth.", "Born in Sabrosa, Portugal to a noble family.", "His expedition proved the Earth could be circumnavigated by sea.",
  [(1519, "Departed Spain with five ships"), (1520, "Navigated the Strait of Magellan"), (1521, "Killed in the Philippines")],
  [("Strait of Magellan", 1520, "Discovery of the strait connecting Atlantic and Pacific")],
  [("The church says the earth is flat, but I know that it is round.", "Attributed")])

add("roald-amundsen", "Roald Amundsen", "ロアルド・アムンセン", 1872, 1928, ["no"], ["engineering"],
  "Roald Amundsen was the first to reach the South Pole and navigate the Northwest Passage.", "Born in Borge, Norway.", "His expeditions were landmarks in polar exploration.",
  [(1906, "First to navigate Northwest Passage"), (1911, "First to reach South Pole")],
  [("The South Pole", 1912, "Account of his Antarctic expedition")],
  [("Adventure is just bad planning.", "Attributed")])

# MATHEMATICIANS
add("john-conway", "John Horton Conway", "ジョン・ホートン・コンウェイ", 1937, 2020, ["gb", "us"], ["mathematics"],
  "John Conway was a prolific mathematician known for the Game of Life and contributions to group theory.", "Born in Liverpool, England.", "His Game of Life became a foundational example in cellular automata.",
  [(1970, "Invented the Game of Life"), (1985, "Discovered the Conway groups")],
  [("On Numbers and Games", 1976, "Foundational work on surreal numbers")],
  [("You get surreal numbers by playing games.", "Attributed")])

add("emile-picard", "Émile Picard", "エミール・ピカール", 1856, 1941, ["fr"], ["mathematics"],
  "Émile Picard made important contributions to analysis and algebraic geometry.", "Born in Paris. Studied at École Normale Supérieure.", "His theorems on entire functions are fundamental in complex analysis.",
  [(1879, "Proved Picard's little theorem"), (1880, "Proved Picard's great theorem")],
  [("Traité d'analyse", 1891, "Three-volume treatise on mathematical analysis")],
  [("Mathematics is the art of giving the same name to different things.", "Attributed, paraphrasing Poincaré")])

add("george-polya", "George Pólya", "ジョージ・ポリア", 1887, 1985, ["hu", "us"], ["mathematics"],
  "George Pólya was a Hungarian mathematician known for his work in combinatorics and mathematical pedagogy.", "Born in Budapest, Hungary.", "His book How to Solve It has been translated into many languages and remains a classic.",
  [(1937, "Published Pólya enumeration theorem"), (1945, "Published How to Solve It")],
  [("How to Solve It", 1945, "Classic guide to mathematical problem-solving")],
  [("If you can't solve a problem, then there is an easier problem you can solve: find it.", "How to Solve It")])

# LITERATURE
add("hans-christian-andersen", "Hans Christian Andersen", "ハンス・クリスチャン・アンデルセン", 1805, 1875, ["dk"], ["literature"],
  "Hans Christian Andersen was a Danish author known for his fairy tales.", "Born in Odense, Denmark in poverty.", "His fairy tales are among the most translated works in literary history.",
  [(1835, "Published first fairy tales"), (1843, "Published The Ugly Duckling")],
  [("Fairy Tales Told for Children", 1835, "First collection of fairy tales"), ("The Little Mermaid", 1837, "Classic fairy tale")],
  [("Life itself is the most wonderful fairy tale.", "Attributed")])

add("brothers-grimm", "Brothers Grimm", "グリム兄弟", 1785, 1863, ["de"], ["literature"],
  "Jacob and Wilhelm Grimm collected and published German fairy tales and pioneered German linguistics.", "Jacob born in 1785, Wilhelm in 1786, in Hanau, Germany.", "Their fairy tale collection became one of the most widely read books in German culture.",
  [(1812, "Published first volume of fairy tales"), (1838, "Began German Dictionary")],
  [("Children's and Household Tales", 1812, "Collection of German fairy tales"), ("German Dictionary", 1854, "Comprehensive German dictionary")],
  [("Once upon a time there was...", "Traditional fairy tale opening")])

add("charles-baudelaire", "Charles Baudelaire", "シャルル・ボードレール", 1821, 1867, ["fr"], ["literature"],
  "Charles Baudelaire was a French poet who pioneered symbolism and modern poetry.", "Born in Paris. Lost his father at age six.", "His work profoundly influenced the direction of modern poetry.",
  [(1857, "Published Les Fleurs du mal"), (1860, "Published Les Paradis artificiels")],
  [("Les Fleurs du mal", 1857, "Revolutionary collection of poetry")],
  [("Always be a poet, even in prose.", "Mon cœur mis à nu")])

add("arthur-rimbaud", "Arthur Rimbaud", "アルチュール・ランボー", 1854, 1891, ["fr"], ["literature"],
  "Arthur Rimbaud was a French poet who influenced modern literature and the Surrealist movement.", "Born in Charleville, France.", "His radical innovation in poetic form influenced generations of poets.",
  [(1871, "Wrote The Drunken Boat at age 16"), (1873, "Published A Season in Hell")],
  [("A Season in Hell", 1873, "Autobiographical prose poem"), ("Illuminations", 1886, "Collection of prose poems")],
  [("I is another.", "Letter to Paul Demeny, 1871")])

add("stephane-mallarme", "Stéphane Mallarmé", "ステファヌ・マラルメ", 1842, 1898, ["fr"], ["literature"],
  "Stéphane Mallarmé was a French poet and critic, a major figure in Symbolism.", "Born in Paris. Worked as an English teacher.", "His experimental poetry influenced modern literature and literary theory.",
  [(1876, "Published L'Après-midi d'un faune"), (1897, "Published Un coup de dés")],
  [("Un coup de dés jamais n'abolira le hasard", 1897, "Experimental typographic poem")],
  [("Everything in the world exists in order to end up as a book.", "Attributed")])

add("paul-valery", "Paul Valéry", "ポール・ヴァレリー", 1871, 1945, ["fr"], ["literature"],
  "Paul Valéry was a French poet, essayist, and philosopher of art and science.", "Born in Sète, France.", "His intellectual poetry and essays on consciousness influenced 20th-century thought.",
  [(1917, "Published La Jeune Parque"), (1920, "Published Le Cimetière marin")],
  [("Le Cimetière marin", 1920, "Philosophical poem on death and the sea")],
  [("The purpose of psychology is to give us a completely different idea of the things we know best.", "Tel Quel")])

# POLITICS
add("tokugawa-tsunayoshi", "Tokugawa Tsunayoshi", "徳川綱吉", 1646, 1709, ["jp"], ["politics"],
  "Tokugawa Tsunayoshi was the fifth shogun of the Tokugawa dynasty, known for the Laws of Compassion for Living Things.", "Born in Edo as the fourth son of Tokugawa Iemitsu.", "His reign saw both cultural flourishing and controversial animal protection laws.",
  [(1680, "Became fifth Tokugawa shogun"), (1687, "Issued Laws of Compassion for Living Things")],
  [("Laws of Compassion for Living Things", 1687, "Controversial animal protection edicts")],
  [("All living things deserve compassion.", "Attributed")])

add("toyotomi-hideyori", "Toyotomi Hideyori", "豊臣秀頼", 1593, 1615, ["jp"], ["politics"],
  "Toyotomi Hideyori was the son and heir of Toyotomi Hideyoshi who fought against the Tokugawa in the Siege of Osaka.", "Born at Osaka Castle as son of the great unifier.", "His defeat at Osaka marked the final consolidation of Tokugawa power.",
  [(1600, "Lost political power after Battle of Sekigahara"), (1615, "Died in the Siege of Osaka")],
  [("Osaka Castle", 1600, "The great castle that was his stronghold")],
  [("The cherry blossoms scatter.", "Attributed death poem tradition")])

if __name__ == "__main__":
    write_people(P)
