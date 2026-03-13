#!/usr/bin/env python3
"""Generate 20 physicist JSON files (Ancient to Early Modern era) into data/people/."""

import json
import os

LANGS = ["en", "es", "pt", "fr", "de", "zh", "hi", "ar", "id", "ja"]

def i18n(en="", ja=""):
    """Create an i18n dict with en and ja filled, rest empty."""
    d = {lang: "" for lang in LANGS}
    d["en"] = en
    if ja:
        d["ja"] = ja
    return d

def make_timeline(events):
    return [{"year": y, "event": i18n(e)} for y, e in events]

def make_works(works):
    return [{"title": i18n(t), "year": y, "description": i18n(d)} for t, y, d in works]

def make_quotes(quotes):
    return [{"text": i18n(t), "source": s} for t, s in quotes]

def make_relations(rels):
    return [{"person": p, "type": t} for p, t in rels]

people = [
    {
        "id": "archimedes",
        "name": i18n("Archimedes", "アルキメデス"),
        "birth_year": -287,
        "death_year": -212,
        "countries": ["gr"],
        "fields": ["physics", "mathematics", "engineering"],
        "overview": i18n("Archimedes of Syracuse was an ancient Greek mathematician, physicist, engineer, and astronomer, widely regarded as one of the greatest scientists of antiquity. He made groundbreaking contributions to geometry, statics, hydrostatics, and the design of innovative machines."),
        "early_life": i18n("Archimedes was born around 287 BC in Syracuse, a Greek colony on the island of Sicily. He likely studied in Alexandria, Egypt, at the great library, before returning to Syracuse where he spent most of his life in the service of King Hiero II."),
        "impact": i18n("Archimedes laid the foundations of hydrostatics and statics, discovering the principle of buoyancy and the law of the lever. His mathematical methods anticipated integral calculus by nearly two millennia, and his war machines defended Syracuse against Roman siege."),
        "timeline": make_timeline([
            (-287, "Born in Syracuse, Sicily"),
            (-270, "Studied at the Library of Alexandria in Egypt"),
            (-250, "Discovered the principle of buoyancy (Archimedes' principle)"),
            (-240, "Developed the Archimedes screw for raising water"),
            (-214, "Designed war machines to defend Syracuse against Roman siege"),
            (-212, "Killed by a Roman soldier during the siege of Syracuse"),
        ]),
        "famous_works": make_works([
            ("On the Sphere and Cylinder", -250, "Derived the relationship between a sphere and its circumscribing cylinder, showing the surface area and volume ratios."),
            ("On Floating Bodies", -250, "Established the foundations of hydrostatics and stated the principle of buoyancy."),
            ("The Method of Mechanical Theorems", -250, "Described a method using mechanics to discover mathematical theorems, anticipating integral calculus."),
        ]),
        "quotes": make_quotes([
            ("Give me a place to stand and I will move the earth.", "Attributed by Pappus of Alexandria"),
            ("Eureka! Eureka!", "Attributed, upon discovering the principle of buoyancy"),
        ]),
        "relations": make_relations([
            ("euclid", "influenced_by"),
            ("eratosthenes", "friend"),
            ("hero-of-alexandria", "influenced"),
        ]),
    },
    {
        "id": "ibn-al-haytham",
        "name": i18n("Ibn al-Haytham", "イブン・アル=ハイサム"),
        "birth_year": 965,
        "death_year": 1040,
        "countries": ["iq", "eg"],
        "fields": ["physics", "mathematics", "astronomy"],
        "overview": i18n("Ibn al-Haytham, known in the West as Alhazen, was an Arab mathematician, astronomer, and physicist who is widely considered the father of modern optics. His Book of Optics fundamentally changed the understanding of light and vision."),
        "early_life": i18n("Ibn al-Haytham was born in Basra, in present-day Iraq, around 965 AD. He received a thorough education in science and theology before moving to Cairo, Egypt, where he spent most of his productive years under the patronage of the Fatimid Caliphate."),
        "impact": i18n("Ibn al-Haytham's experimental method and insistence on empirical evidence anticipated the modern scientific method by centuries. His work on optics influenced European scientists including Roger Bacon, Kepler, and Descartes, and his camera obscura experiments laid groundwork for the development of photography."),
        "timeline": make_timeline([
            (965, "Born in Basra, present-day Iraq"),
            (1011, "Placed under house arrest in Cairo after failed Nile dam project"),
            (1021, "Completed the Book of Optics (Kitab al-Manazir)"),
            (1025, "Wrote treatises on astronomy and mathematics"),
            (1040, "Died in Cairo, Egypt"),
        ]),
        "famous_works": make_works([
            ("Book of Optics (Kitab al-Manazir)", 1021, "A seven-volume treatise that fundamentally changed the understanding of light, vision, and optics through systematic experimentation."),
            ("Doubts Concerning Ptolemy", 1028, "A critical examination of Ptolemy's astronomical and optical works, questioning established scientific authority."),
            ("On the Configuration of the World", 1020, "A cosmological work describing the physical structure of the universe based on Ptolemy's astronomy."),
        ]),
        "quotes": make_quotes([
            ("The duty of the man who investigates the writings of scientists, if learning the truth is his goal, is to make himself an enemy of all that he reads.", "Book of Optics"),
            ("The seeker after truth is not one who studies the writings of the ancients and puts his trust in them, but rather the one who suspects his faith in them and questions what he gathers from them.", "Doubts Concerning Ptolemy"),
        ]),
        "relations": make_relations([
            ("ptolemy", "influenced_by"),
            ("euclid", "influenced_by"),
            ("roger-bacon", "influenced"),
            ("johannes-kepler", "influenced"),
        ]),
    },
    {
        "id": "nicolaus-copernicus",
        "name": i18n("Nicolaus Copernicus", "ニコラウス・コペルニクス"),
        "birth_year": 1473,
        "death_year": 1543,
        "countries": ["pl"],
        "fields": ["physics", "astronomy", "mathematics"],
        "overview": i18n("Nicolaus Copernicus was a Polish astronomer and mathematician who formulated the heliocentric model of the universe, placing the Sun rather than the Earth at the center. His work triggered the Copernican Revolution and fundamentally transformed astronomy and science."),
        "early_life": i18n("Copernicus was born in 1473 in the city of Torun in Royal Prussia, part of the Kingdom of Poland. After his father's death, he was raised by his uncle, a bishop, who supported his education at the University of Krakow and later in Italy at Bologna and Padua."),
        "impact": i18n("Copernicus's heliocentric theory displaced the Earth from the center of the universe and initiated the Scientific Revolution. His model inspired Kepler, Galileo, and Newton, ultimately reshaping humanity's understanding of its place in the cosmos."),
        "timeline": make_timeline([
            (1473, "Born in Torun, Royal Prussia, Kingdom of Poland"),
            (1491, "Enrolled at the University of Krakow"),
            (1497, "Began studying canon law and astronomy in Bologna, Italy"),
            (1514, "Circulated the Commentariolus outlining the heliocentric hypothesis"),
            (1543, "De Revolutionibus Orbium Coelestium published; died in Frauenburg"),
        ]),
        "famous_works": make_works([
            ("De Revolutionibus Orbium Coelestium", 1543, "The landmark work presenting the heliocentric model of the solar system, arguing that the Earth and planets revolve around the Sun."),
            ("Commentariolus", 1514, "A short manuscript outlining the heliocentric hypothesis that was circulated among a small group of scholars before the full publication."),
        ]),
        "quotes": make_quotes([
            ("At rest, however, in the middle of everything is the Sun.", "De Revolutionibus Orbium Coelestium"),
            ("To know that we know what we know, and to know that we do not know what we do not know, that is true knowledge.", "Attributed"),
        ]),
        "relations": make_relations([
            ("ptolemy", "influenced_by"),
            ("galileo-galilei", "influenced"),
            ("johannes-kepler", "influenced"),
            ("georg-joachim-rheticus", "colleague"),
        ]),
    },
    {
        "id": "galileo-galilei",
        "name": i18n("Galileo Galilei", "ガリレオ・ガリレイ"),
        "birth_year": 1564,
        "death_year": 1642,
        "countries": ["it"],
        "fields": ["physics", "astronomy", "mathematics"],
        "overview": i18n("Galileo Galilei was an Italian astronomer, physicist, and mathematician, often called the father of modern observational astronomy and modern physics. His improvements to the telescope and consequent astronomical observations supported the Copernican heliocentric model."),
        "early_life": i18n("Galileo was born in Pisa, Italy, in 1564, the eldest of six children. He studied medicine at the University of Pisa before switching to mathematics, and quickly gained a reputation for his keen intellect and challenging of Aristotelian doctrine."),
        "impact": i18n("Galileo's telescopic discoveries, including Jupiter's moons and the phases of Venus, provided crucial evidence for heliocentrism. His emphasis on systematic observation and mathematical description of nature established the methodology of modern physics."),
        "timeline": make_timeline([
            (1564, "Born in Pisa, Duchy of Florence"),
            (1589, "Appointed professor of mathematics at the University of Pisa"),
            (1609, "Built an improved telescope and began astronomical observations"),
            (1610, "Published Sidereus Nuncius, revealing Jupiter's moons"),
            (1632, "Published Dialogue Concerning the Two Chief World Systems"),
            (1633, "Tried by the Inquisition and placed under house arrest"),
        ]),
        "famous_works": make_works([
            ("Sidereus Nuncius", 1610, "Reported telescopic observations of the Moon's surface, Jupiter's moons, and many new stars, revolutionizing astronomy."),
            ("Dialogue Concerning the Two Chief World Systems", 1632, "A comparison of the Copernican and Ptolemaic systems that effectively argued for heliocentrism, leading to Galileo's trial."),
            ("Two New Sciences", 1638, "Laid the foundations of modern kinematics and materials science, summarizing Galileo's work on motion and strength of materials."),
        ]),
        "quotes": make_quotes([
            ("And yet it moves.", "Attributed, after his forced recantation of heliocentrism"),
            ("Mathematics is the language in which God has written the universe.", "The Assayer, 1623"),
            ("In questions of science, the authority of a thousand is not worth the humble reasoning of a single individual.", "Attributed"),
        ]),
        "relations": make_relations([
            ("nicolaus-copernicus", "influenced_by"),
            ("isaac-newton", "influenced"),
            ("johannes-kepler", "colleague"),
            ("christiaan-huygens", "influenced"),
        ]),
    },
    {
        "id": "johannes-kepler",
        "name": i18n("Johannes Kepler", "ヨハネス・ケプラー"),
        "birth_year": 1571,
        "death_year": 1630,
        "countries": ["de"],
        "fields": ["physics", "astronomy", "mathematics"],
        "overview": i18n("Johannes Kepler was a German astronomer and mathematician best known for his three laws of planetary motion. His work provided the foundation for Newton's theory of universal gravitation and marked a pivotal advance in the Scientific Revolution."),
        "early_life": i18n("Kepler was born in 1571 in Weil der Stadt, in the Duchy of Wurttemberg. Despite a troubled childhood marked by poverty and illness, he excelled academically and studied theology and mathematics at the University of Tubingen, where he first encountered Copernican astronomy."),
        "impact": i18n("Kepler's three laws of planetary motion replaced circular orbits with ellipses and established precise mathematical relationships governing planetary movement. His work bridged Copernican astronomy and Newtonian physics, fundamentally shaping modern celestial mechanics."),
        "timeline": make_timeline([
            (1571, "Born in Weil der Stadt, Duchy of Wurttemberg"),
            (1596, "Published Mysterium Cosmographicum, his first major astronomical work"),
            (1600, "Joined Tycho Brahe as assistant in Prague"),
            (1609, "Published Astronomia Nova, containing his first two laws of planetary motion"),
            (1619, "Published Harmonices Mundi, containing his third law"),
            (1630, "Died in Regensburg, Bavaria"),
        ]),
        "famous_works": make_works([
            ("Astronomia Nova", 1609, "Presented the first two laws of planetary motion: that planets move in ellipses and sweep equal areas in equal times."),
            ("Harmonices Mundi", 1619, "Contained the third law of planetary motion relating orbital period to distance, and explored mathematical harmonies in nature."),
            ("Mysterium Cosmographicum", 1596, "Kepler's first major work defending the Copernican system using geometric models of the solar system."),
        ]),
        "quotes": make_quotes([
            ("I measured the skies, now the shadows I measure. Sky-bound was the mind, earth-bound the body rests.", "Kepler's self-composed epitaph"),
            ("Nature uses as little as possible of anything.", "Attributed"),
        ]),
        "relations": make_relations([
            ("nicolaus-copernicus", "influenced_by"),
            ("tycho-brahe", "mentor"),
            ("galileo-galilei", "colleague"),
            ("isaac-newton", "influenced"),
        ]),
    },
    {
        "id": "blaise-pascal",
        "name": i18n("Blaise Pascal", "ブレーズ・パスカル"),
        "birth_year": 1623,
        "death_year": 1662,
        "countries": ["fr"],
        "fields": ["physics", "mathematics", "philosophy"],
        "overview": i18n("Blaise Pascal was a French mathematician, physicist, inventor, and philosopher. He made fundamental contributions to projective geometry, probability theory, and fluid mechanics, and invented one of the earliest mechanical calculators."),
        "early_life": i18n("Pascal was born in 1623 in Clermont-Ferrand, France. A child prodigy, he was educated by his father, a mathematician, and by the age of sixteen had written a significant treatise on conic sections that impressed leading mathematicians."),
        "impact": i18n("Pascal's work on fluid mechanics established Pascal's law and advanced understanding of atmospheric pressure. His correspondence with Fermat founded probability theory, and his philosophical writings, particularly the Pensees, continue to influence theology and philosophy."),
        "timeline": make_timeline([
            (1623, "Born in Clermont-Ferrand, France"),
            (1642, "Invented the Pascaline, a mechanical calculator"),
            (1648, "Demonstrated atmospheric pressure variations with the Puy de Dome experiment"),
            (1654, "Corresponded with Fermat on probability theory"),
            (1656, "Published the Provincial Letters defending Jansenism"),
            (1662, "Died in Paris at age 39"),
        ]),
        "famous_works": make_works([
            ("Pensees", 1670, "A posthumously published collection of philosophical and theological fragments, including Pascal's famous wager argument."),
            ("Traite du triangle arithmetique", 1654, "Described what is now known as Pascal's triangle and its applications to combinatorics and probability."),
            ("Provincial Letters", 1656, "A series of eighteen letters attacking Jesuit casuistry, considered a masterpiece of French prose."),
        ]),
        "quotes": make_quotes([
            ("The heart has its reasons which reason knows nothing of.", "Pensees"),
            ("All of humanity's problems stem from man's inability to sit quietly in a room alone.", "Pensees"),
        ]),
        "relations": make_relations([
            ("pierre-de-fermat", "collaborator"),
            ("rene-descartes", "rival"),
            ("daniel-bernoulli", "influenced"),
            ("evangelista-torricelli", "influenced_by"),
        ]),
    },
    {
        "id": "robert-boyle",
        "name": i18n("Robert Boyle", "ロバート・ボイル"),
        "birth_year": 1627,
        "death_year": 1691,
        "countries": ["ie", "gb"],
        "fields": ["physics", "chemistry"],
        "overview": i18n("Robert Boyle was an Anglo-Irish natural philosopher, chemist, and physicist who is regarded as one of the founders of modern chemistry. He is best known for Boyle's law, which describes the inverse relationship between the pressure and volume of a gas."),
        "early_life": i18n("Boyle was born in 1627 at Lismore Castle in County Waterford, Ireland, the fourteenth child of the Earl of Cork. He was educated at Eton and traveled extensively in Europe before settling in Oxford, where he conducted his most important scientific work."),
        "impact": i18n("Boyle's emphasis on experimentation and his mechanical philosophy helped establish chemistry as a rigorous science distinct from alchemy. His gas law became foundational to physics and chemistry, and his work The Sceptical Chymist challenged Aristotelian and alchemical traditions."),
        "timeline": make_timeline([
            (1627, "Born at Lismore Castle, County Waterford, Ireland"),
            (1654, "Moved to Oxford and began experimental work"),
            (1660, "Published New Experiments Physico-Mechanical, describing the air pump"),
            (1661, "Published The Sceptical Chymist"),
            (1662, "Formulated Boyle's law on gas pressure and volume"),
            (1691, "Died in London"),
        ]),
        "famous_works": make_works([
            ("The Sceptical Chymist", 1661, "Challenged the Aristotelian theory of four elements and alchemical traditions, arguing for a corpuscular view of matter."),
            ("New Experiments Physico-Mechanical", 1660, "Described experiments with the air pump conducted with Robert Hooke, leading to Boyle's law."),
        ]),
        "quotes": make_quotes([
            ("The generality of men are so accustomed to judge of things by their senses that, because the air is invisible, they ascribe but little to it.", "New Experiments Physico-Mechanical"),
        ]),
        "relations": make_relations([
            ("robert-hooke", "collaborator"),
            ("isaac-newton", "colleague"),
            ("antoine-lavoisier", "influenced"),
        ]),
    },
    {
        "id": "robert-hooke",
        "name": i18n("Robert Hooke", "ロバート・フック"),
        "birth_year": 1635,
        "death_year": 1703,
        "countries": ["gb"],
        "fields": ["physics", "biology", "engineering"],
        "overview": i18n("Robert Hooke was an English natural philosopher, architect, and polymath who made contributions to an extraordinary range of fields. He is best remembered for Hooke's law of elasticity, his pioneering microscopic observations, and coining the term 'cell' in biology."),
        "early_life": i18n("Hooke was born in 1635 in Freshwater on the Isle of Wight, England. After his father's death, he moved to London and eventually entered Christ Church, Oxford, where he became Robert Boyle's assistant and began his experimental career."),
        "impact": i18n("Hooke's Micrographia opened up the microscopic world to public wonder and scientific inquiry. His law of elasticity remains fundamental to engineering and materials science, and his architectural work helped rebuild London after the Great Fire of 1666."),
        "timeline": make_timeline([
            (1635, "Born in Freshwater, Isle of Wight, England"),
            (1655, "Became Robert Boyle's assistant at Oxford"),
            (1660, "Discovered the law of elasticity (Hooke's law)"),
            (1662, "Appointed Curator of Experiments at the Royal Society"),
            (1665, "Published Micrographia"),
            (1703, "Died in London"),
        ]),
        "famous_works": make_works([
            ("Micrographia", 1665, "A groundbreaking illustrated book of microscopic observations, introducing the term 'cell' and revealing the intricate structure of common objects."),
            ("De Potentia Restitutiva", 1678, "Formally published Hooke's law of elasticity, describing the proportional relationship between force and deformation in springs."),
        ]),
        "quotes": make_quotes([
            ("The truth is, the Science of Nature has been already too long made only a work of the Brain and the Fancy.", "Micrographia, preface"),
        ]),
        "relations": make_relations([
            ("robert-boyle", "collaborator"),
            ("isaac-newton", "rival"),
            ("christiaan-huygens", "colleague"),
            ("christopher-wren", "collaborator"),
        ]),
    },
    {
        "id": "christiaan-huygens",
        "name": i18n("Christiaan Huygens", "クリスティアーン・ホイヘンス"),
        "birth_year": 1629,
        "death_year": 1695,
        "countries": ["nl"],
        "fields": ["physics", "astronomy", "mathematics"],
        "overview": i18n("Christiaan Huygens was a Dutch mathematician, physicist, and astronomer who was one of the leading scientists of the 17th century. He proposed the wave theory of light, invented the pendulum clock, and discovered Saturn's largest moon, Titan."),
        "early_life": i18n("Huygens was born in 1629 in The Hague, Netherlands, into a prominent diplomatic family. His father's connections with leading intellectuals, including Rene Descartes, provided young Christiaan with an exceptional education in mathematics and natural philosophy."),
        "impact": i18n("Huygens's wave theory of light provided an alternative to Newton's corpuscular theory and was later vindicated by Young and Fresnel. His invention of the pendulum clock revolutionized timekeeping and his work on probability contributed to the foundations of the field."),
        "timeline": make_timeline([
            (1629, "Born in The Hague, Netherlands"),
            (1655, "Discovered Titan, Saturn's largest moon"),
            (1656, "Invented the pendulum clock"),
            (1673, "Published Horologium Oscillatorium on pendulum dynamics"),
            (1690, "Published Traite de la Lumiere proposing the wave theory of light"),
            (1695, "Died in The Hague"),
        ]),
        "famous_works": make_works([
            ("Traite de la Lumiere", 1690, "Presented the wave theory of light using what is now known as Huygens' principle, explaining reflection and refraction."),
            ("Horologium Oscillatorium", 1673, "A major work on pendulum dynamics and clock design, containing important results in mechanics and the theory of evolutes."),
        ]),
        "quotes": make_quotes([
            ("The world is my country, science my religion.", "Attributed"),
        ]),
        "relations": make_relations([
            ("isaac-newton", "rival"),
            ("galileo-galilei", "influenced_by"),
            ("rene-descartes", "influenced_by"),
            ("thomas-young", "influenced"),
            ("augustin-jean-fresnel", "influenced"),
        ]),
    },
    {
        "id": "isaac-newton",
        "name": i18n("Isaac Newton", "アイザック・ニュートン"),
        "birth_year": 1643,
        "death_year": 1727,
        "countries": ["gb"],
        "fields": ["physics", "mathematics", "astronomy"],
        "overview": i18n("Sir Isaac Newton was an English mathematician, physicist, and astronomer, widely recognized as one of the most influential scientists of all time. He formulated the laws of motion and universal gravitation, co-invented calculus, and made seminal contributions to optics."),
        "early_life": i18n("Newton was born in 1643 in Woolsthorpe, Lincolnshire, England, a premature infant not expected to survive. Raised largely by his grandmother after his mother remarried, he attended the King's School in Grantham before enrolling at Trinity College, Cambridge, in 1661."),
        "impact": i18n("Newton's Principia Mathematica unified terrestrial and celestial mechanics under the law of universal gravitation, transforming physics into a mathematical science. His work dominated scientific thought for over two centuries and remains foundational to classical mechanics."),
        "timeline": make_timeline([
            (1643, "Born in Woolsthorpe, Lincolnshire, England"),
            (1665, "Developed early ideas on calculus, optics, and gravitation during the 'annus mirabilis'"),
            (1668, "Built the first practical reflecting telescope"),
            (1687, "Published Philosophiae Naturalis Principia Mathematica"),
            (1704, "Published Opticks on the nature of light and color"),
            (1727, "Died in Kensington, London"),
        ]),
        "famous_works": make_works([
            ("Philosophiae Naturalis Principia Mathematica", 1687, "Laid out the three laws of motion and the law of universal gravitation, unifying terrestrial and celestial mechanics."),
            ("Opticks", 1704, "Explored the nature of light through prism experiments, demonstrating that white light is composed of a spectrum of colors."),
            ("Method of Fluxions", 1736, "Posthumously published work describing Newton's development of calculus, including differentiation and integration techniques."),
        ]),
        "quotes": make_quotes([
            ("If I have seen further it is by standing on the shoulders of Giants.", "Letter to Robert Hooke, 1675"),
            ("I can calculate the motion of heavenly bodies, but not the madness of people.", "Attributed, after the South Sea Bubble"),
        ]),
        "relations": make_relations([
            ("galileo-galilei", "influenced_by"),
            ("johannes-kepler", "influenced_by"),
            ("robert-hooke", "rival"),
            ("gottfried-wilhelm-leibniz", "rival"),
            ("michael-faraday", "influenced"),
        ]),
    },
    {
        "id": "daniel-bernoulli",
        "name": i18n("Daniel Bernoulli", "ダニエル・ベルヌーイ"),
        "birth_year": 1700,
        "death_year": 1782,
        "countries": ["ch", "nl"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Daniel Bernoulli was a Swiss mathematician and physicist best known for his work in fluid dynamics. His most important contribution, Bernoulli's principle, describes the relationship between fluid speed and pressure, forming a cornerstone of aerodynamics."),
        "early_life": i18n("Bernoulli was born in 1700 in Groningen, Netherlands, into the famed Bernoulli family of mathematicians. His father Johann initially discouraged him from pursuing mathematics, insisting he study medicine, but Daniel combined both interests throughout his career."),
        "impact": i18n("Bernoulli's principle became fundamental to understanding fluid flow and is essential to the design of aircraft wings, carburetors, and many other technologies. His kinetic theory of gases also anticipated developments in statistical mechanics by over a century."),
        "timeline": make_timeline([
            (1700, "Born in Groningen, Netherlands"),
            (1724, "Published Exercitationes Mathematicae and gained recognition"),
            (1725, "Moved to St. Petersburg to join the Academy of Sciences"),
            (1733, "Returned to Basel, Switzerland"),
            (1738, "Published Hydrodynamica, containing Bernoulli's principle"),
            (1782, "Died in Basel, Switzerland"),
        ]),
        "famous_works": make_works([
            ("Hydrodynamica", 1738, "Presented the fundamental principles of fluid dynamics, including the relationship between fluid velocity and pressure now known as Bernoulli's principle."),
            ("Exposition of a New Theory on the Measurement of Risk", 1738, "Introduced the concept of expected utility and the St. Petersburg paradox solution, foundational to economic theory."),
        ]),
        "quotes": make_quotes([
            ("It would be better for the true physics if there were no mathematicians on earth.", "Attributed, in jest about mathematical abstraction"),
        ]),
        "relations": make_relations([
            ("leonhard-euler", "friend"),
            ("johann-bernoulli", "student"),
            ("blaise-pascal", "influenced_by"),
            ("isaac-newton", "influenced_by"),
        ]),
    },
    {
        "id": "benjamin-franklin",
        "name": i18n("Benjamin Franklin", "ベンジャミン・フランクリン"),
        "birth_year": 1706,
        "death_year": 1790,
        "countries": ["us"],
        "fields": ["physics", "politics"],
        "overview": i18n("Benjamin Franklin was an American polymath, statesman, and one of the Founding Fathers of the United States. As a scientist, he is best known for his experiments with electricity, including the famous kite experiment, and for inventing the lightning rod."),
        "early_life": i18n("Franklin was born in 1706 in Boston, Massachusetts, the fifteenth of seventeen children. Largely self-educated after leaving school at age ten, he became a successful printer in Philadelphia and used his wealth to pursue scientific and civic interests."),
        "impact": i18n("Franklin's experiments proved that lightning is electrical in nature and led to the invention of the lightning rod, saving countless buildings from fire. His concepts of positive and negative electrical charge remain fundamental to the understanding of electricity."),
        "timeline": make_timeline([
            (1706, "Born in Boston, Massachusetts"),
            (1729, "Became owner of the Pennsylvania Gazette"),
            (1749, "Published proposals on electrical experiments"),
            (1752, "Conducted the famous kite experiment demonstrating the electrical nature of lightning"),
            (1776, "Helped draft and signed the Declaration of Independence"),
            (1790, "Died in Philadelphia, Pennsylvania"),
        ]),
        "famous_works": make_works([
            ("Experiments and Observations on Electricity", 1751, "A collection of letters and papers describing Franklin's electrical experiments, including his single-fluid theory of electricity."),
            ("Poor Richard's Almanack", 1732, "An annual publication containing weather forecasts, household tips, and witty aphorisms that became widely popular in colonial America."),
        ]),
        "quotes": make_quotes([
            ("An investment in knowledge pays the best interest.", "Attributed, from Poor Richard's Almanack"),
            ("In this world, nothing is certain except death and taxes.", "Letter to Jean-Baptiste Le Roy, 1789"),
        ]),
        "relations": make_relations([
            ("joseph-priestley", "friend"),
            ("alessandro-volta", "influenced"),
            ("charles-augustin-de-coulomb", "influenced"),
            ("thomas-jefferson", "collaborator"),
        ]),
    },
    {
        "id": "charles-augustin-de-coulomb",
        "name": i18n("Charles-Augustin de Coulomb", "シャルル=オーギュスタン・ド・クーロン"),
        "birth_year": 1736,
        "death_year": 1806,
        "countries": ["fr"],
        "fields": ["physics", "engineering"],
        "overview": i18n("Charles-Augustin de Coulomb was a French military engineer and physicist who is best known for formulating Coulomb's law, which describes the electrostatic force between charged particles. His torsion balance experiments established the quantitative foundations of electrostatics."),
        "early_life": i18n("Coulomb was born in 1736 in Angouleme, France, into a family of minor nobility. He studied at the Ecole Royale du Genie de Mezieres, one of France's leading military engineering schools, and served as a military engineer in the West Indies before returning to France."),
        "impact": i18n("Coulomb's law became one of the fundamental laws of electromagnetism and is essential to understanding electrical interactions. His work on friction and structural mechanics also made lasting contributions to engineering, and the SI unit of electric charge is named in his honor."),
        "timeline": make_timeline([
            (1736, "Born in Angouleme, France"),
            (1761, "Graduated from the Ecole Royale du Genie de Mezieres"),
            (1773, "Published memoirs on structural mechanics and friction"),
            (1785, "Published Coulomb's law describing electrostatic force"),
            (1789, "Retired from military service during the French Revolution"),
            (1806, "Died in Paris"),
        ]),
        "famous_works": make_works([
            ("First Memoir on Electricity and Magnetism", 1785, "Presented the inverse-square law for electrostatic force using the torsion balance, now known as Coulomb's law."),
            ("Theory of Simple Machines", 1781, "A treatise on friction in machines that won the Grand Prize of the French Academy of Sciences."),
        ]),
        "quotes": make_quotes([
            ("The force between two charges is proportional to the product of the charges and inversely proportional to the square of the distance between them.", "First Memoir on Electricity and Magnetism, paraphrased"),
        ]),
        "relations": make_relations([
            ("benjamin-franklin", "influenced_by"),
            ("andre-marie-ampere", "influenced"),
            ("michael-faraday", "influenced"),
            ("isaac-newton", "influenced_by"),
        ]),
    },
    {
        "id": "alessandro-volta",
        "name": i18n("Alessandro Volta", "アレッサンドロ・ボルタ"),
        "birth_year": 1745,
        "death_year": 1827,
        "countries": ["it"],
        "fields": ["physics", "chemistry"],
        "overview": i18n("Alessandro Volta was an Italian physicist and chemist who invented the voltaic pile, the first true electric battery, providing the first reliable source of continuous electric current. The volt, the SI unit of electric potential, is named in his honor."),
        "early_life": i18n("Volta was born in 1745 in Como, in the Duchy of Milan. Despite his family's wish that he enter the legal profession, he developed a strong interest in electricity from a young age and was appointed professor of physics at the Royal School of Como at age 29."),
        "impact": i18n("Volta's invention of the electric battery in 1800 was transformative for science, enabling subsequent discoveries in electrochemistry, electromagnetism, and electrical engineering. It directly enabled the work of Humphry Davy, Faraday, and many others."),
        "timeline": make_timeline([
            (1745, "Born in Como, Duchy of Milan"),
            (1775, "Invented the electrophorus, a device for generating static electricity"),
            (1778, "Discovered and isolated methane gas"),
            (1791, "Disputed Galvani's theory of animal electricity"),
            (1800, "Invented the voltaic pile, the first electric battery"),
            (1827, "Died in Como, Lombardy-Venetia"),
        ]),
        "famous_works": make_works([
            ("Letter to Sir Joseph Banks", 1800, "Described the voltaic pile to the President of the Royal Society, announcing the invention of the first electric battery."),
            ("On the Electricity Excited by the Mere Contact of Conducting Substances", 1800, "Detailed the theory and construction of the voltaic pile based on contact electricity between dissimilar metals."),
        ]),
        "quotes": make_quotes([
            ("The language of experiment is more authoritative than any reasoning: facts can destroy our ratiocination—not vice versa.", "Attributed"),
        ]),
        "relations": make_relations([
            ("luigi-galvani", "rival"),
            ("benjamin-franklin", "influenced_by"),
            ("michael-faraday", "influenced"),
            ("andre-marie-ampere", "influenced"),
        ]),
    },
    {
        "id": "thomas-young",
        "name": i18n("Thomas Young", "トマス・ヤング"),
        "birth_year": 1773,
        "death_year": 1829,
        "countries": ["gb"],
        "fields": ["physics", "biology"],
        "overview": i18n("Thomas Young was an English polymath who made important contributions to optics, physiology, and Egyptology. He is best known for his double-slit experiment, which demonstrated the wave nature of light and established the principle of interference."),
        "early_life": i18n("Young was born in 1773 in Milverton, Somerset, England, a child prodigy who could read fluently by age two. He studied medicine at London, Edinburgh, and Gottingen, and became a physician, but his scientific curiosity ranged across an astonishing number of disciplines."),
        "impact": i18n("Young's double-slit experiment became one of the most important experiments in physics, providing definitive evidence for the wave theory of light. His work on color vision and elasticity (Young's modulus) also had lasting influence on physics and engineering."),
        "timeline": make_timeline([
            (1773, "Born in Milverton, Somerset, England"),
            (1793, "Published a paper on the mechanism of the eye's accommodation"),
            (1801, "Demonstrated the double-slit experiment proving light interference"),
            (1807, "Introduced the concept of Young's modulus of elasticity"),
            (1814, "Began deciphering the Rosetta Stone's demotic script"),
            (1829, "Died in London"),
        ]),
        "famous_works": make_works([
            ("On the Theory of Light and Colours", 1801, "Presented the wave theory of light and described the principle of interference, supported by the double-slit experiment."),
            ("A Course of Lectures on Natural Philosophy", 1807, "A comprehensive work covering mechanics, optics, and acoustics, introducing Young's modulus."),
        ]),
        "quotes": make_quotes([
            ("The experiments I am about to relate may be repeated with great ease, whenever the sun shines.", "On the Theory of Light and Colours"),
        ]),
        "relations": make_relations([
            ("christiaan-huygens", "influenced_by"),
            ("isaac-newton", "influenced_by"),
            ("augustin-jean-fresnel", "colleague"),
            ("james-clerk-maxwell", "influenced"),
        ]),
    },
    {
        "id": "andre-marie-ampere",
        "name": i18n("Andre-Marie Ampere", "アンドレ=マリ・アンペール"),
        "birth_year": 1775,
        "death_year": 1836,
        "countries": ["fr"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Andre-Marie Ampere was a French physicist and mathematician who was one of the founders of the science of classical electromagnetism. He formulated Ampere's law and is considered the father of electrodynamics; the ampere unit of electric current is named after him."),
        "early_life": i18n("Ampere was born in 1775 in Lyon, France. A child prodigy, he was largely self-educated, reportedly mastering advanced mathematics by age twelve. His early life was marked by personal tragedy, including his father's execution during the French Revolution."),
        "impact": i18n("Ampere's mathematical formulation of the relationship between electric currents and magnetic fields laid the foundation for electrodynamics. His work directly influenced Maxwell's electromagnetic theory and remains central to electrical engineering and physics."),
        "timeline": make_timeline([
            (1775, "Born in Lyon, France"),
            (1793, "Father executed during the French Revolution"),
            (1820, "Heard of Oersted's discovery and rapidly developed the theory of electrodynamics"),
            (1826, "Published Memoir on the Mathematical Theory of Electrodynamic Phenomena"),
            (1836, "Died in Marseille during an inspection tour"),
        ]),
        "famous_works": make_works([
            ("Memoir on the Mathematical Theory of Electrodynamic Phenomena", 1826, "Presented the mathematical foundations of electrodynamics, including Ampere's force law between current-carrying conductors."),
            ("Collection of Observations on Electrodynamics", 1822, "Compiled experimental results and theoretical analysis of the relationship between electric currents and magnetism."),
        ]),
        "quotes": make_quotes([
            ("Enlightened by the study of the works of the Creator, the mind of man can best be purified and strengthened.", "Attributed"),
        ]),
        "relations": make_relations([
            ("hans-christian-oersted", "influenced_by"),
            ("charles-augustin-de-coulomb", "influenced_by"),
            ("michael-faraday", "colleague"),
            ("james-clerk-maxwell", "influenced"),
        ]),
    },
    {
        "id": "sadi-carnot",
        "name": i18n("Sadi Carnot", "サディ・カルノー"),
        "birth_year": 1796,
        "death_year": 1832,
        "countries": ["fr"],
        "fields": ["physics", "engineering"],
        "overview": i18n("Nicolas Leonard Sadi Carnot was a French military engineer and physicist, often described as the father of thermodynamics. His only published work introduced the concept of the Carnot cycle and established the theoretical limits of heat engine efficiency."),
        "early_life": i18n("Carnot was born in 1796 in Paris, the son of the prominent military leader and mathematician Lazare Carnot. He was educated at the Ecole Polytechnique and the Ecole du Genie, both elite French military schools, before pursuing his interest in the theory of heat engines."),
        "impact": i18n("Carnot's analysis of heat engines established the second law of thermodynamics in embryonic form and defined the maximum possible efficiency of any heat engine. His work, rediscovered by Clapeyron and later Clausius and Kelvin, became the foundation of thermodynamic theory."),
        "timeline": make_timeline([
            (1796, "Born in Paris, France"),
            (1812, "Entered the Ecole Polytechnique"),
            (1824, "Published Reflections on the Motive Power of Fire"),
            (1828, "Retired from the military to focus on scientific research"),
            (1832, "Died of cholera in Paris at age 36"),
        ]),
        "famous_works": make_works([
            ("Reflections on the Motive Power of Fire", 1824, "Established the theoretical foundations of thermodynamics by analyzing the efficiency of heat engines and introducing the Carnot cycle."),
        ]),
        "quotes": make_quotes([
            ("Wherever there exists a difference of temperature, motive power can be produced.", "Reflections on the Motive Power of Fire"),
        ]),
        "relations": make_relations([
            ("lazare-carnot", "student"),
            ("rudolf-clausius", "influenced"),
            ("lord-kelvin", "influenced"),
            ("emile-clapeyron", "influenced"),
        ]),
    },
    {
        "id": "michael-faraday",
        "name": i18n("Michael Faraday", "マイケル・ファラデー"),
        "birth_year": 1791,
        "death_year": 1867,
        "countries": ["gb"],
        "fields": ["physics", "chemistry"],
        "overview": i18n("Michael Faraday was an English scientist who made extraordinary contributions to the study of electromagnetism and electrochemistry. He discovered electromagnetic induction, diamagnetism, and the laws of electrolysis, and his concept of the field transformed physics."),
        "early_life": i18n("Faraday was born in 1791 in Newington Butts, Surrey, England, to a poor blacksmith's family. With little formal education, he educated himself while working as a bookbinder's apprentice and gained entry to science through attending lectures by Humphry Davy at the Royal Institution."),
        "impact": i18n("Faraday's discovery of electromagnetic induction made possible the electric generator and transformer, forming the basis of modern electrical technology. His concept of lines of force and the electromagnetic field inspired Maxwell's equations and the entire framework of field theory in physics."),
        "timeline": make_timeline([
            (1791, "Born in Newington Butts, Surrey, England"),
            (1813, "Became Humphry Davy's assistant at the Royal Institution"),
            (1821, "Demonstrated electromagnetic rotation (the principle of the electric motor)"),
            (1831, "Discovered electromagnetic induction"),
            (1834, "Formulated Faraday's laws of electrolysis"),
            (1867, "Died at Hampton Court, Middlesex, England"),
        ]),
        "famous_works": make_works([
            ("Experimental Researches in Electricity", 1839, "A three-volume collection of Faraday's papers on electricity, covering electromagnetic induction, electrolysis, and field theory."),
            ("The Chemical History of a Candle", 1861, "A series of six public lectures on the chemistry and physics of a candle flame, famous for their clarity and elegance."),
            ("On the Various Forces of Nature", 1860, "A popular series of lectures explaining the fundamental forces of nature to a general audience."),
        ]),
        "quotes": make_quotes([
            ("Nothing is too wonderful to be true, if it be consistent with the laws of nature.", "Faraday's diary, March 19, 1849"),
            ("The important thing is to know how to take all things quietly.", "Letter, 1858"),
        ]),
        "relations": make_relations([
            ("humphry-davy", "mentor"),
            ("james-clerk-maxwell", "influenced"),
            ("andre-marie-ampere", "colleague"),
            ("alessandro-volta", "influenced_by"),
            ("isaac-newton", "influenced_by"),
        ]),
    },
    {
        "id": "augustin-jean-fresnel",
        "name": i18n("Augustin-Jean Fresnel", "オーギュスタン・ジャン・フレネル"),
        "birth_year": 1788,
        "death_year": 1827,
        "countries": ["fr"],
        "fields": ["physics", "engineering"],
        "overview": i18n("Augustin-Jean Fresnel was a French civil engineer and physicist who made major contributions to the wave theory of light. He developed the mathematical framework for diffraction and polarization, and invented the Fresnel lens used in lighthouses worldwide."),
        "early_life": i18n("Fresnel was born in 1788 in Broglie, Normandy, France. A slow learner as a child who could barely read at age eight, he later excelled in mathematics and attended the Ecole Polytechnique and the Ecole des Ponts et Chaussees to become a civil engineer."),
        "impact": i18n("Fresnel's wave theory of light, complete with a rigorous mathematical treatment of diffraction, definitively defeated Newton's corpuscular theory. His Fresnel lens revolutionized lighthouse technology and his equations for reflection and refraction remain fundamental in optics."),
        "timeline": make_timeline([
            (1788, "Born in Broglie, Normandy, France"),
            (1806, "Entered the Ecole des Ponts et Chaussees"),
            (1815, "Began his optical research during a period of political exile"),
            (1818, "Won the French Academy prize for his memoir on diffraction"),
            (1822, "Developed the Fresnel lens for lighthouses"),
            (1827, "Died in Ville-d'Avray near Paris at age 39"),
        ]),
        "famous_works": make_works([
            ("Memoir on the Diffraction of Light", 1818, "Presented a comprehensive mathematical wave theory of diffraction that won the French Academy of Sciences prize."),
            ("Fresnel Lens Design", 1822, "Invented the stepped lens design that dramatically improved lighthouse illumination and is still used today."),
        ]),
        "quotes": make_quotes([
            ("Nature is not embarrassed by difficulties of analysis.", "Attributed, during debates on wave theory"),
        ]),
        "relations": make_relations([
            ("christiaan-huygens", "influenced_by"),
            ("thomas-young", "colleague"),
            ("francois-arago", "collaborator"),
            ("james-clerk-maxwell", "influenced"),
        ]),
    },
    {
        "id": "georg-ohm",
        "name": i18n("Georg Ohm", "ゲオルク・オーム"),
        "birth_year": 1789,
        "death_year": 1854,
        "countries": ["de"],
        "fields": ["physics", "mathematics"],
        "overview": i18n("Georg Simon Ohm was a German physicist and mathematician who discovered the fundamental law governing electrical resistance. Ohm's law, relating voltage, current, and resistance, is one of the most basic and important laws in electrical science."),
        "early_life": i18n("Ohm was born in 1789 in Erlangen, Bavaria, to a Protestant family. His father, a locksmith, was a self-taught man who gave Georg and his brother an excellent education in mathematics, physics, and philosophy, enabling Georg to attend the University of Erlangen."),
        "impact": i18n("Ohm's law provided the quantitative foundation for understanding and designing electrical circuits. Despite initial rejection in Germany, his work was recognized internationally and became essential to the development of electrical engineering. The ohm, the unit of electrical resistance, is named after him."),
        "timeline": make_timeline([
            (1789, "Born in Erlangen, Bavaria"),
            (1811, "Received his doctorate from the University of Erlangen"),
            (1825, "Published his first paper on electrical resistance"),
            (1827, "Published The Galvanic Circuit Investigated Mathematically, containing Ohm's law"),
            (1841, "Awarded the Copley Medal by the Royal Society of London"),
            (1854, "Died in Munich, Bavaria"),
        ]),
        "famous_works": make_works([
            ("The Galvanic Circuit Investigated Mathematically", 1827, "Presented Ohm's law in a systematic mathematical form, relating current, voltage, and resistance in electrical circuits."),
        ]),
        "quotes": make_quotes([
            ("The force of the current in a galvanic circuit is directly as the sum of all the tensions, and inversely as the entire reduced length of the circuit.", "The Galvanic Circuit Investigated Mathematically"),
        ]),
        "relations": make_relations([
            ("alessandro-volta", "influenced_by"),
            ("michael-faraday", "colleague"),
            ("gustav-kirchhoff", "influenced"),
        ]),
    },
]

def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "people")
    os.makedirs(base_dir, exist_ok=True)

    for person in people:
        filepath = os.path.join(base_dir, f"{person['id']}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(person, f, ensure_ascii=False, indent=2)
        print(f"Created {filepath}")

    print(f"\nTotal: {len(people)} files generated.")

if __name__ == "__main__":
    main()
