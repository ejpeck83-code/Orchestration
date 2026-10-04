# Science corpus

158 sources for hardening the collection: 103 journal papers, the rest reports, chapters, primary sources and a short shelf of books. Every entry says what it is and what it gives you as a writer.

I checked every paper against Crossref or the publisher's record before it went in. 111 entries carry a verified DOI. Several DOIs and page ranges I had from memory turned out wrong, and the corrected versions are what you see here.

That check covers the citation. The notes come from what I know about each work plus its abstract, and I read only 1 in full (Bottomley 2014). Confirm a note against the paper before a story leans on it.

## Start here

Three findings shape everything below.

**Your series engine already has a name in the research.** Susan Leigh Star's work (1999) shows infrastructure stays invisible until it breaks. Every story in this collection is a breakdown that makes a hidden system visible, which is also how the reader discovers the fork.

**Most of your mysteries can resolve on real, period-accurate science.** The heat pipe (1964), tritium dating of water (1957), the sound spectrograph (1946) and probabilistic record linkage (1959 and 1969) all existed inside your 1962-82 window. Part C lists what your investigators could and couldn't do.

**Two plot ideas need correcting before you build on them.** Local Niagara Escarpment dolostone doesn't swell in concrete, so a "the stone itself grew" solution needs imported aggregate. And temperature alone can't make food age *radically* differently. Ethylene or storage atmosphere can.

## How to use this

- `corpus.csv` is the master list. Open it in any spreadsheet, filter by story, add rows.
- `corpus.bib` imports straight into Zotero or any reference manager.
- After editing the CSV, run `python3 story-research/tools/build_corpus.py` to rebuild the BibTeX and the reading lists in this file.
- For free, legal copies of paywalled papers, paste the DOI into [Unpaywall](https://unpaywall.org) or ask a library. Government reports (NTSB, NIST, USGS, FHWA, NASA, DTIC) are free at the links given.

---

## Part A. The spine: why a mundane fork can stick

Every story leans on the same claim: a small, contingent decision can lock in a whole technological system, and 70 years later it feels inevitable. These papers make that claim respectable. They also give you the vocabulary your in-world engineers would have used when they argued at each fork.

### Lock-in and path dependence

<!-- papers:A1 -->
- **David (1985).** Clio and the Economics of QWERTY. *American Economic Review* 75(2):332-337. [link](https://www.jstor.org/stable/1805621)  
  The founding case for lock-in: an early standard survives because everything around it adapts to it. Use it to argue that the divergent system can be permanent even where it is worse.
- **Liebowitz & Margolis (1990).** The Fable of the Keys. *Journal of Law and Economics* 33(1):1-25. [doi:10.1086/467198](https://doi.org/10.1086/467198)  
  The rebuttal to David. The QWERTY evidence is thinner than claimed, and markets do switch when an alternative is clearly better. Give this argument to your in-world skeptic, and use it to keep each fork from feeling arbitrary.
- **Arthur (1989).** Competing Technologies, Increasing Returns, and Lock-In by Historical Events. *The Economic Journal* 99(394):116-131. [doi:10.2307/2234208](https://doi.org/10.2307/2234208)  
  A formal model where small early events plus increasing returns pick the winning technology. Explains how the first few cities to adopt a district system could tip the whole country.
- **Liebowitz & Margolis (1995).** Path Dependence, Lock-In, and History. *Journal of Law, Economics, and Organization* 11(1):205-226. [doi:10.1093/oxfordjournals.jleo.a036867](https://doi.org/10.1093/oxfordjournals.jleo.a036867)  
  Sorts path dependence into three degrees by how costly the lock-in is. Use it to decide, story by story, whether their system is worse, equal or better than ours.
- **Cowan (1990).** Nuclear Power Reactors: A Study in Technological Lock-in. *Journal of Economic History* 50(3):541-567. [doi:10.1017/S0022050700037153](https://doi.org/10.1017/S0022050700037153)  
  Light-water reactors won because the Navy's submarine program got there first. A real case of military procurement choosing a civilian technology.
- **Cowan & Gunby (1996).** Sprayed to Death: Path Dependence, Lock-in and Pest Control Strategies. *The Economic Journal* 106(436):521-542. [doi:10.2307/2235561](https://doi.org/10.2307/2235561)  
  Chemical pest control locked in, and some local lock-ins later broke. Useful for a 1970s city where an old district system is starting to crack.
- **David & Bunn (1988).** The Economics of Gateway Technologies and Network Evolution: Lessons from Electricity Supply History. *Information Economics and Policy* 3(2):165-202. [doi:10.1016/0167-6245(88)90024-8](https://doi.org/10.1016/0167-6245(88)90024-8)  
  The AC/DC fight and the rotary converter, a gateway device that let rival networks connect. Supports 'compatibility with another technology' as a divergence cause, and the Niagara fork.
- **Puffert (2002).** Path Dependence in Spatial Networks: The Standardization of Railway Track Gauge. *Explorations in Economic History* 39(3):282-314. [doi:10.1006/exeh.2002.0786](https://doi.org/10.1006/exeh.2002.0786)  
  How railway gauge standards spread region by region across a network. Explains how a local standard, like a main pressure or a pipe size, radiates out from one city.
- **Unruh (2000).** Understanding Carbon Lock-In. *Energy Policy* 28(12):817-830. [doi:10.1016/S0301-4215(00)00070-7](https://doi.org/10.1016/S0301-4215(00)00070-7)  
  Lock-in happens to technologies and institutions together: utilities, codes, unions, lenders. Populate your 1962-82 city with people whose jobs depend on the divergent system.
- **Geels (2002).** Technological Transitions as Evolutionary Reconfiguration Processes: A Multi-Level Perspective and a Case-Study. *Research Policy* 31(8-9):1257-1274. [doi:10.1016/S0048-7333(02)00062-8](https://doi.org/10.1016/S0048-7333(02)00062-8)  
  The multi-level perspective: niche, regime and landscape. A simple frame for writing each fork as a niche technology that took over a regime.
- **Geels (2005).** The Dynamics of Transitions in Socio-Technical Systems: A Multi-Level Analysis of the Transition Pathway from Horse-Drawn Carriages to Automobiles (1860-1930). *Technology Analysis & Strategic Management* 17(4):445-476. [doi:10.1080/09537320500357319](https://doi.org/10.1080/09537320500357319)  
  The historical horse-to-car transition in US cities, 1860-1930. This is the historical window your Intersection and Meter forks bend.
- **Kline & Pinch (1996).** Users as Agents of Technological Change: The Social Construction of the Automobile in the Rural United States. *Technology and Culture* 37(4):763-795. [doi:10.2307/3107097](https://doi.org/10.2307/3107097)  
  Farmers turned the Model T into a portable power source. Precedent for residents using district systems in ways the engineers never planned.
- **Pierson (2000).** Increasing Returns, Path Dependence, and the Study of Politics. *American Political Science Review* 94(2):251-267. [doi:10.2307/2586011](https://doi.org/10.2307/2586011)  
  Why political institutions get cheaper to keep and costlier to change over time. Supports municipal politics as a divergence cause.
- **Shapiro & Varian (1999).** The Art of Standards Wars. *California Management Review* 41(2):8-32. [doi:10.2307/41165984](https://doi.org/10.2307/41165984)  
  The tactics firms use to win standards wars. Useful for the corporate fights at each fork.
<!-- /papers:A1 -->

### How technologies get chosen

<!-- papers:A2 -->
- **Pinch & Bijker (1984).** The Social Construction of Facts and Artefacts: or How the Sociology of Science and the Sociology of Technology Might Benefit Each Other. *Social Studies of Science* 14(3):399-441. [doi:10.1177/030631284014003004](https://doi.org/10.1177/030631284014003004)  
  Early bicycles had several 'correct' designs depending on who you asked, until the argument closed. Use it to show that in the 1890s their design and ours both looked right to someone.
- **Winner (1980).** Do Artifacts Have Politics?. *Daedalus* 109(1):121-136. [link](https://www.jstor.org/stable/20024652)  
  Robert Moses's low parkway bridges as design that carries a political decision. A model for an archival artifact that explains why a structure has its shape.
- **Joerges (1999).** Do Politics Have Artefacts?. *Social Studies of Science* 29(3):411-431. [doi:10.1177/030631299029003004](https://doi.org/10.1177/030631299029003004)  
  Shows the Moses bridge story is mostly legend. Pair it with Winner and you have investigators chasing a famous explanation that turns out to be folklore.
- **Hughes (1969).** Technological Momentum in History: Hydrogenation in Germany 1898-1933. *Past and Present* 44(1):106-132. [doi:10.1093/past/44.1.106](https://doi.org/10.1093/past/44.1.106)  
  Technological momentum: big systems gather people, capital and rules until they are hard to turn. This is why a 1973 resident can't picture the city without its district systems.
- **Hughes (1987).** The Evolution of Large Technological Systems. In Bijker, Hughes and Pinch (eds.), The Social Construction of Technological Systems. MIT Press, pp. 51-82.  
  System builders, reverse salients and momentum. Vocabulary for the engineers who argued at each fork.
- **Tarr (1979).** The Separate vs. Combined Sewer Problem: A Case Study in Urban Technology Design Choice. *Journal of Urban History* 5(3):308-339. [doi:10.1177/009614427900500303](https://doi.org/10.1177/009614427900500303)  
  A real municipal fork: separate or combined sewers, settled by engineers, cost and doctrine. A template for writing your fork scenes.
- **Cowan (1985).** How the Refrigerator Got Its Hum. In MacKenzie and Wajcman (eds.), The Social Shaping of Technology. Open University Press; reprinted in The Design History Reader, 2nd ed. (Bloomsbury), pp. 202-218. [doi:10.5040/9781350133532.ch-044](https://doi.org/10.5040/9781350133532.ch-044)  
  Why the compressor refrigerator beat the silent gas-absorption model. Corporate capital and electric utilities decided it. The core source for Cold Room.
<!-- /papers:A2 -->

### Why infrastructure goes invisible (your series engine)

<!-- papers:A3 -->
- **Star (1999).** The Ethnography of Infrastructure. *American Behavioral Scientist* 43(3):377-391. [doi:10.1177/00027649921955326](https://doi.org/10.1177/00027649921955326)  
  Infrastructure stays invisible until it breaks. This is your series engine: each mystery is a breakdown that makes a system visible.
- **Star & Ruhleder (1996).** Steps Toward an Ecology of Infrastructure: Design and Access for Large Information Spaces. *Information Systems Research* 7(1):111-134. [doi:10.1287/isre.7.1.111](https://doi.org/10.1287/isre.7.1.111)  
  Infrastructure depends on where you stand: a pipe is invisible to a tenant and central to the crew that maintains it. Use it to vary what each investigator can see.
- **Edwards (2003).** Infrastructure and Modernity: Force, Time, and Social Organization in the History of Sociotechnical Systems. In Misa, Brey and Feenberg (eds.), Modernity and Technology. MIT Press, pp. 185-226. [doi:10.7551/mitpress/4729.003.0011](https://doi.org/10.7551/mitpress/4729.003.0011)  
  Mature infrastructures become the natural background of modern life. Backs your rule that the characters never remark on the missing object.
- **Larkin (2013).** The Politics and Poetics of Infrastructure. *Annual Review of Anthropology* 42:327-343. [doi:10.1146/annurev-anthro-092412-155522](https://doi.org/10.1146/annurev-anthro-092412-155522)  
  Infrastructure carries promises and aesthetics along with function. Supports municipal beige as something the city chose on purpose.
- **Graham & Thrift (2007).** Out of Order: Understanding Repair and Maintenance. *Theory, Culture & Society* 24(3):1-25. [doi:10.1177/0263276407075954](https://doi.org/10.1177/0263276407075954)  
  Repair and maintenance as the hidden work that keeps cities running. Most of your protagonists are maintainers.
- **Russell & Vinsel (2018).** After Innovation, Turn to Maintenance. *Technology and Culture* 59(1):1-25. [doi:10.1353/tech.2018.0004](https://doi.org/10.1353/tech.2018.0004)  
  The case for writing technology history around upkeep. It fits the scratches-and-maintenance-stickers look.
- **Edgerton (1999).** From Innovation to Use: Ten Eclectic Theses on the Historiography of Technology. *History and Technology* 16(2):111-136. [doi:10.1080/07341519908581961](https://doi.org/10.1080/07341519908581961)  
  Argues historians should follow technologies in use, long after invention. Your 1962-82 world is exactly that.
<!-- /papers:A3 -->

### Building a counterfactual that holds

<!-- papers:A4 -->
- **Fogel (1962).** A Quantitative Approach to the Study of Railroads in American Economic Growth: A Report of Some Preliminary Findings. *Journal of Economic History* 22(2):163-197. [doi:10.1017/S0022050700062719](https://doi.org/10.1017/S0022050700062719)  
  The famous railroad counterfactual: without railroads, the 1890 US economy comes out only a few percent smaller. A useful constraint, since many forks change daily life far more than they change GDP.
- **Lebow (2000).** What's So Different about a Counterfactual?. *World Politics* 52(4):550-585. [doi:10.1017/S0043887100020104](https://doi.org/10.1017/S0043887100020104)  
  How to build counterfactuals that hold up: small rewrites, plausible second-order effects. A checklist for each fork.
- **Rosenfeld (2002).** Why Do We Ask 'What If?' Reflections on the Function of Alternate History. *History and Theory* 41(4):90-103. [doi:10.1111/1468-2303.00222](https://doi.org/10.1111/1468-2303.00222)  
  Alternate histories usually work as nightmares or fantasies. Your forks are neither, which helps set the collection apart.
<!-- /papers:A4 -->

### Books for the spine

<!-- papers:A5 -->
- **Hughes (1983).** Networks of Power: Electrification in Western Society, 1880-1930. *Johns Hopkins University Press* (book).  
  The standard history of how electric power systems were built, including the Niagara decision.
- **Bowker & Star (1999).** Sorting Things Out: Classification and Its Consequences. *MIT Press* (book).  
  How classification systems shape what institutions can see. Good for the clerk stories.
- **Edgerton (2006).** The Shock of the Old: Technology and Global History since 1900. *Oxford University Press* (book).  
  Old technologies persist and dominate long after the hype. The rationale for your aesthetic.
- **Yates & Murphy (2019).** Engineering Rules: Global Standard Setting since 1880. *Johns Hopkins University Press* (book).  
  How engineers built the standards bodies that settled forks like these, from 1880 on.
- **Scott (1998).** Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed. *Yale University Press* (book).  
  Legibility: why states number streets and survey land. Background for The Number.
- **Armstrong (ed.) (1976).** History of Public Works in the United States, 1776-1976. *American Public Works Association* (book).  
  Reference history of American public works. What your municipal agencies would look like.
- **Gallagher (2018).** Telling It Like It Wasn't: The Counterfactual Imagination in History and Fiction. *University of Chicago Press* (book).  
  Literary history of counterfactual fiction. Helps you place the collection.
- **Tetlock & Belkin (eds.) (1996).** Counterfactual Thought Experiments in World Politics. *Princeton University Press* (book).  
  Criteria for judging whether a counterfactual is plausible.
<!-- /papers:A5 -->

---

## Part B. Story by story

Each story gets four things: the historical fork, mechanisms the papers make defensible, the traps to avoid, and the reading list. The mechanisms are options for you to choose from. The plots are still yours.

### 1. The Intersection

**The fork in our history**

- London put up the world's first traffic signal in December 1868, a gas-lit semaphore outside Parliament. A gas leak blew it up in January 1869 and burned the constable running it. The signal was gone by 1870, and London didn't try again until the 1920s ([Smithsonian](https://www.smithsonianmag.com/smart-news/chaotic-traffic-from-horse-drawn-carriages-inspired-the-worlds-first-traffic-lights-180985558/); McShane 1999). That's a real "freak accident" fork you can borrow.
- Electric signals spread through US cities in the 1910s and 1920s (McShane 1999).
- In the 1920s, motor interests campaigned to make the street a car space and the pedestrian the problem, which is where "jaywalking" came from (Norton 2007).
- Reinforced concrete went from novelty to standard in American building between 1900 and 1930 (Slaton 2001). "Cheap concrete arrives earlier" is a small push on a real trend.

**Mechanisms the papers support**

- **Weaving and wrong-way conflicts.** Grade separation removes crossing conflicts and creates merging and weaving ones, which is where interchange crashes cluster (Pulugurtha & Bhatt 2010). Wrong-way entries through ramps put cars on paths they should never be on (NTSB 2012). Roads that never cross still share space in a weave.
- **Structures that move.** Frost heave, freeze-thaw damage and alkali-aggregate expansion change clearances and elevations over decades (Taber 1930; Powers 1945; Stanton 1940; Gillott 1964).
- **Records that disagree.** Drawings tied to different survey datums can disagree even when every survey was done right (Dewhurst 1990; Snay 2012). Your "mismatched elevations" can be a datum problem before anyone suspects a crime.
- **Shock waves.** Traffic disturbances travel backward and can put collisions at a fixed spot far from their cause (Lighthill & Whitham 1955; Richards 1956).

**Watch out for**

- Quarried Niagara Escarpment dolostone isn't alkali-reactive (Rogers et al. 2000). If concrete at your junction grows, the aggregate came from somewhere like Kingston, Ontario, where the alkali-carbonate reaction was first found in 1957.
- Modern roundabouts get their safety from yield-at-entry and low speeds (Retting et al. 2001 measured the effect in US conversions). The big, fast traffic circles of the 1920s-50s were a different machine, so decide which kind your city built.
- Your 1973 investigator reconstructs crashes from skid marks, crush and sight lines, using Baker's Northwestern manual (Baker 1975).

**Papers**

<!-- papers:B01 -->
- **McShane (1999).** The Origins and Globalization of Traffic Control Signals. *Journal of Urban History* 25(3):379-404. [doi:10.1177/009614429902500304](https://doi.org/10.1177/009614429902500304)  
  Scholarly history of traffic signals, from London's 1868 semaphore to US electric signals in the 1910s-20s and their spread worldwide.
- **Norton (2007).** Street Rivals: Jaywalking and the Invention of the Motor Age Street. *Technology and Culture* 48(2):331-359. [doi:10.1353/tech.2007.0085](https://doi.org/10.1353/tech.2007.0085)  
  How motor interests rewrote the rules of the street in the 1920s and turned 'jaywalking' into an offense. A world without signals would have different street law and etiquette.
- **Lighthill & Whitham (1955).** On Kinematic Waves II. A Theory of Traffic Flow on Long Crowded Roads. *Proceedings of the Royal Society of London A* 229(1178):317-345. [doi:10.1098/rspa.1955.0089](https://doi.org/10.1098/rspa.1955.0089)  
  Kinematic wave theory of traffic. Shows how a disturbance travels backward through traffic and causes crashes at a fixed point far from its cause.
- **Richards (1956).** Shock Waves on the Highway. *Operations Research* 4(1):42-51. [doi:10.1287/opre.4.1.42](https://doi.org/10.1287/opre.4.1.42)  
  An independent derivation of traffic shock waves. Pair with Lighthill and Whitham.
- **Retting et al. (2001).** Crash and Injury Reduction Following Installation of Roundabouts in the United States. *American Journal of Public Health* 91(4):628-631. [doi:10.2105/AJPH.91.4.628](https://doi.org/10.2105/AJPH.91.4.628)  
  US before-and-after data: converting intersections to modern roundabouts sharply cut injury crashes. Modern roundabouts depend on yield-at-entry and low speed. Older high-speed rotaries had worse records, so your world needs that rule early.
- **Persaud et al. (2001).** Safety Effect of Roundabout Conversions in the United States: Empirical Bayes Observational Before-After Study. *Transportation Research Record* 1751:1-8. [doi:10.3141/1751-01](https://doi.org/10.3141/1751-01)  
  The statistical method behind the roundabout safety numbers. Useful if a character has to prove a junction is dangerous with data.
- **Pulugurtha & Bhatt (2010).** Evaluating the Role of Weaving Section Characteristics and Traffic on Crashes in Weaving Areas. *Traffic Injury Prevention* 11(1):104-113. [doi:10.1080/15389580903370039](https://doi.org/10.1080/15389580903370039)  
  Crashes cluster in weaving sections, where entering and exiting traffic cross paths. Grade separation trades crossing conflicts for weaving conflicts, so roads that never cross can still produce collisions.
- **National Transportation Safety Board (2012).** Wrong-Way Driving (Highway Special Investigation Report NTSB/SIR-12/01). *NTSB*. [link](https://www.ntsb.gov/safety/safety-studies/Documents/SIR1201.pdf)  
  Wrong-way entries onto divided highways, usually through exit ramps. A plausible way for a car to end up on a path it should never be on.
- **Taber (1930).** The Mechanics of Frost Heaving. *Journal of Geology* 38(4):303-317. [doi:10.1086/623720](https://doi.org/10.1086/623720)  
  How freezing soil lifts structures. One way elevations and clearances drift over decades.
- **Powers (1945).** A Working Hypothesis for Further Studies of Frost Resistance of Concrete. *ACI Journal Proceedings* 41(1):245-272. [doi:10.14359/8684](https://doi.org/10.14359/8684)  
  Why concrete fails under freeze-thaw and how entrained air protects it. Relevant to 1920s-60s concrete in Niagara winters.
- **Stanton (1940).** Expansion of Concrete through Reaction between Cement and Aggregate. *Proceedings of the American Society of Civil Engineers* 66(10):1781-1811. [doi:10.14359/20122](https://doi.org/10.14359/20122)  
  The discovery of alkali-silica reaction: concrete that slowly swells and cracks from within. A mechanism for structures that move.
- **Gillott (1964).** Mechanism and Kinetics of Expansion in the Alkali-Carbonate Rock Reaction. *Canadian Journal of Earth Sciences* 1(2):121-145. [doi:10.1139/e64-007](https://doi.org/10.1139/e64-007)  
  The mechanism of alkali-carbonate expansion in dolomitic aggregate, first identified at Kingston, Ontario, in 1957.
- **Gillott & Swenson (1969).** Mechanism of the Alkali-Carbonate Rock Reaction. *Quarterly Journal of Engineering Geology* 2(1):7-23. [doi:10.1144/GSL.QJEG.1969.002.01.02](https://doi.org/10.1144/GSL.QJEG.1969.002.01.02)  
  Follow-up on the alkali-carbonate mechanism, co-written by Swenson, who first flagged the problem.
- **Rogers et al. (2000).** Alkali-Aggregate Reactions in Ontario. *Canadian Journal of Civil Engineering* 27(2):246-260. [doi:10.1139/l99-073](https://doi.org/10.1139/l99-073)  
  Survey of alkali-aggregate reaction across Ontario. Key point for you: quarried Niagara Escarpment dolostone is not reactive, so local stone can't be the culprit. Kingston-type aggregate shipped in can.
- **Galloway et al. (1999).** Land Subsidence in the United States (USGS Circular 1182). *U.S. Geological Survey*. [doi:10.3133/cir1182](https://doi.org/10.3133/cir1182)  
  USGS survey of how land sinks in the US: groundwater pumping, mines, soils. Background for benchmarks that move.
- **Slaton (2001).** Reinforced Concrete and the Modernization of American Building, 1900-1930. *Johns Hopkins University Press* (book). [doi:10.1353/book.20625](https://doi.org/10.1353/book.20625)  
  How reinforced concrete became standard in American building, 1900-1930. Background for a 'cheap concrete arrives early' fork.
- **Baker (1975).** Traffic Accident Investigation Manual. *Traffic Institute, Northwestern University* (book). [link](https://archive.org/details/trafficaccidenti0000bake)  
  The period-standard manual for reconstructing crashes from skid marks, damage and sight lines. What your 1973 investigator actually carries.

*Also useful here, listed in other sections:* Geels (2005), Dewhurst (1990), Snay (2012).
<!-- /papers:B01 -->

### 2. The Number

**The fork in our history**

- House numbers and city directories were tools for making cities readable to government and business, and American cities standardized them through the 1800s (Rose-Redwood 2008; Rose-Redwood & Tantner 2012).
- Western New York was laid out by survey. The Holland Land Company ran its transit meridians in 1798-99, and Transit Road through Lockport still follows the West Transit line (see `03-city.md`).
- In our 1963, the Post Office bolted a 5-digit ZIP code onto the street address. In a coordinate city, the address already does that job.

**Mechanisms the papers support**

- **The null sink.** Blank or failed coordinates collapse to (0, 0), and data systems start treating that point as a real place (Juhász & Mooney 2022). In a 1970s coordinate city, the grid origin collects mail that belongs nowhere.
- **Datum change.** Re-basing a coordinate system moves every old coordinate slightly (Dewhurst 1990; Snay 2012). A few land in the river, the gorge or the escarpment face.
- **Matching errors.** Street-based matching can put an address tens of meters off (Zandbergen 2008), and probabilistic record linkage can merge two people or invent one (Fellegi & Sunter 1969).

**Watch out for**

- A coordinate system needs an origin, a datum, units and an owner. Decide all 4 early, because every Number-style mystery will turn on one of them.
- Street naming is politics (Rose-Redwood, Alderman & Azaryahu 2010). A coordinate city takes naming away from someone, and in 1965 somebody fought about it.

**Papers**

<!-- papers:B02 -->
- **Rose-Redwood (2008).** Indexing the Great Ledger of the Community: Urban House Numbering, City Directories, and the Production of Spatial Legibility. *Journal of Historical Geography* 34(2):286-310. [doi:10.1016/j.jhg.2007.06.003](https://doi.org/10.1016/j.jhg.2007.06.003)  
  How house numbers and city directories made cities readable to government and business. The system a coordinate address replaces.
- **Rose-Redwood (2006).** Governmentality, Geography, and the Geo-Coded World. *Progress in Human Geography* 30(4):469-486. [doi:10.1191/0309132506ph619oa](https://doi.org/10.1191/0309132506ph619oa)  
  Geocoding as a tool of government. Frames a coordinate address as a state project with politics attached.
- **Rose-Redwood & Tantner (2012).** Introduction: Governmentality, House Numbering and the Spatial History of the Modern City. *Urban History* 39(4):607-613. [doi:10.1017/S0963926812000405](https://doi.org/10.1017/S0963926812000405)  
  Opens a special issue on the history of house numbering across Europe and the US.
- **Rose-Redwood et al. (2010).** Geographies of Toponymic Inscription: New Directions in Critical Place-Name Studies. *Progress in Human Geography* 34(4):453-470. [doi:10.1177/0309132509351042](https://doi.org/10.1177/0309132509351042)  
  Street naming as political inscription. In a coordinate city, who loses the power to name places?
- **Tantner (2015).** House Numbers: Pictures of a Forgotten History. *Reaktion Books* (book).  
  Illustrated history of house numbering since the 18th century.
- **Zandbergen (2008).** A Comparison of Address Point, Parcel and Street Geocoding Techniques. *Computers, Environment and Urban Systems* 32(3):214-232. [doi:10.1016/j.compenvurbsys.2007.11.006](https://doi.org/10.1016/j.compenvurbsys.2007.11.006)  
  Street-based address matching can put a point tens of meters off, sometimes much more. Real error sizes for a mislocated address.
- **Juhász & Mooney (2022).** 'I Think I Discovered a Military Base in the Middle of the Ocean': Null Island, the Most Real of Fictional Places. *IEEE Access* 10:84147-84165. [doi:10.1109/ACCESS.2022.3197222](https://doi.org/10.1109/ACCESS.2022.3197222)  
  How blank or broken coordinates collapse to (0, 0) and turn into a real-seeming place in data. A direct model for mail from a coordinate that cannot exist.
- **Dewhurst (1990).** NADCON: The Application of Minimum-Curvature-Derived Surfaces in the Transformation of Positional Data from the North American Datum of 1927 to the North American Datum of 1983 (NOAA Technical Memorandum NOS NGS-50). *NOAA National Geodetic Survey*. [link](https://www.ngs.noaa.gov/PUBS_LIB/NGS50.pdf)  
  The NGS method for converting NAD 27 coordinates to NAD 83. When a datum changes, every old coordinate lands somewhere slightly new.
- **Snay (2012).** Evolution of NAD 83 in the United States: Journey from 2D toward 4D. *Journal of Surveying Engineering* 138(4):161-171. [doi:10.1061/(ASCE)SU.1943-5428.0000083](https://doi.org/10.1061/(ASCE)SU.1943-5428.0000083)  
  How the NAD 83 datum itself was revised several times. Supports a city whose coordinates quietly move under it.

*Also useful here, listed in other sections:* Scott (1998), Fellegi & Sunter (1969), Newcombe et al. (1959).
<!-- /papers:B02 -->

### 3. The Lift

**The fork in our history**

- The paternoster started in 1868 at Oriel Chambers in Liverpool. J & E Hall of Dartford built its "Cyclic Elevator" in 1884 (Bottomley 2014).
- It moves more people at peak than conventional lifts: 60 people per 5 minutes against 40 in a 2008 survey at Sheffield's Arts Tower (Bottomley 2014).
- Safety is what stopped it. A 1970 fatality in Newcastle led UK paternosters to add car-stability tracking, and manufacturers now effectively won't build new ones (Bottomley 2014).

**Mechanisms the papers support**

- **The turnover.** Cars pass over the top and under the bottom of the loop, through machine space that isn't a floor on anyone's plan. A rider who stays aboard reaches places no log records.
- **Counting by flow.** A paternoster never stops, so any head count is a flow estimate at one landing (Fruin 1974). "Entered and never exited" can be a count taken at the wrong landing.
- **Car stability.** The 1970 accident is your template for a car that tilts or jams (Bottomley 2014).

**Watch out for**

- Colson Whitehead's *The Intuitionist* (1999) is elevator-inspector noir in an unexplained city. Read `02-originality.md` before you pick this story's protagonist.

**Papers**

<!-- papers:B03 -->
- **Bottomley (2014).** Modernising a Paternoster. *4th Symposium on Lift and Escalator Technologies*. [link](https://liftescalatorlibrary.org/paper_indexing/papers/00000067.pdf)  
  Engineering account of modernizing Sheffield's Arts Tower paternoster: 38 cars over 22 occupied floors. A 1970 fatality in Newcastle led UK paternosters to add car-stability tracking. A 2008 survey clocked 60 people per 5-minute peak against 40 for the building's conventional lifts. New paternosters are effectively no longer built.
- **Bernard (2014).** Lifted: A Cultural History of the Elevator. *NYU Press* (book). [doi:10.18574/nyu/9781479880423.001.0001](https://doi.org/10.18574/nyu/9781479880423.001.0001)  
  Cultural history of the elevator: how it reorganized buildings, status and privacy.
- **Fruin (1974).** Pedestrian System Planning for High Rise Buildings. *Transportation Engineering Journal of ASCE* 100(3):675-686. [doi:10.1061/TPEJAN.0000452](https://doi.org/10.1061/TPEJAN.0000452)  
  Pedestrian flow planning for high-rise buildings, from the Port Authority's research engineer. Numbers for how people queue and board.
- **Yamaguchi et al. (1996).** Brake Control Characteristics of a Linear Synchronous Motor for Ropeless Elevator. *Proceedings of the 4th IEEE International Workshop on Advanced Motion Control (AMC '96)*. [doi:10.1109/AMC.1996.509289](https://doi.org/10.1109/AMC.1996.509289)  
  Braking control for a ropeless, linear-motor elevator. Shows where multi-car and continuous-shaft ideas went after the paternoster.
- **Blacklock (2020).** The Paternoster: A Requiem. *Granta (online)*. [link](https://granta.com/paternoster-a-requiem/)  
  A literary essay on riding paternosters and how it feels like stepping into a building's circulatory system. A tone reference.
<!-- /papers:B03 -->

### 4. Cold Room

**The fork in our history**

- District cooling came early. Morris Pierce dates American district heating to Holly's Lockport system of 1877 and notes that brine and ammonia district cooling followed soon after (Pierce 1995; Østergaard et al. 2022).
- The home compressor fridge won because GE, GM, Westinghouse and the electric utilities had the capital and the motive. The quiet gas-absorption fridge lost (Cowan 1985).
- Controlled-atmosphere fruit storage was worked out in Britain in the 1920s and 30s (Kidd & West 1930).

**Mechanisms the papers support**

- **Ethylene.** Ripening fruit gives off ethylene, and tiny amounts trigger ripening in everything nearby (Gane 1934; Burg & Burg 1962). If a neighborhood's food sits in shared cold rooms, one ripening room or one leak ages all of it. A 1959 detector can measure the gas (Burg & Stolwijk 1959).
- **Atmosphere.** Less oxygen and more carbon dioxide slow aging (Kidd & West 1930). A carbon dioxide or nitrogen leak into cold rooms makes food last strangely long.
- **Temperature drift.** A few degrees changes spoilage measurably (Ratkowsky et al. 1982; Baranyi & Roberts 1994). A 10 degree C rise often speeds deterioration 2 to 3 times (Labuza 1984).
- **Radiation, the dark option.** Irradiation slows spoilage (Diehl 2002). A stray radiation source would slow it too, and hurt people, which takes the story somewhere much darker.

**Watch out for**

- Temperature alone gives you "faster." For "radically different," use ethylene or atmosphere.
- Brine and ammonia loops carry cold through pipes. Ethylene moves through air, so the mechanism needs shared rooms or shared ventilation.

**Papers**

<!-- papers:B04 -->
- **Østergaard et al. (2022).** The Four Generations of District Cooling: A Categorization of the Development in District Cooling from Origin to Future Prospect. *Energy* 251:124098. [doi:10.1016/j.energy.2022.124098](https://doi.org/10.1016/j.energy.2022.124098)  
  District cooling from the first brine and ammonia pipelines of the late 1800s to today, in four generations. The backbone history for a city that cools by the neighborhood.
- **Gang et al. (2016).** District Cooling Systems: Technology Integration, System Optimization, Challenges and Opportunities for Applications. *Renewable and Sustainable Energy Reviews* 53:253-264. [doi:10.1016/j.rser.2015.08.051](https://doi.org/10.1016/j.rser.2015.08.051)  
  Modern district cooling engineering: plants, networks, storage and failure points. Grounds the physics of a neighborhood cold loop.
- **Kidd & West (1930).** The Gas Storage of Fruit. II. Optimum Temperatures and Atmospheres. *Journal of Pomology and Horticultural Science* 8(1):67-77. [doi:10.1080/03683621.1930.11513351](https://doi.org/10.1080/03683621.1930.11513351)  
  Controlled-atmosphere storage: less oxygen and more carbon dioxide slow fruit aging. One lever for food that ages slower than it should.
- **Gane (1934).** Production of Ethylene by Some Ripening Fruits. *Nature* 134(3400):1008. [doi:10.1038/1341008a0](https://doi.org/10.1038/1341008a0)  
  The first proof that ripening fruit gives off ethylene.
- **Burg & Burg (1962).** Role of Ethylene in Fruit Ripening. *Plant Physiology* 37(2):179-189. [doi:10.1104/pp.37.2.179](https://doi.org/10.1104/pp.37.2.179)  
  Ethylene acts as the ripening hormone: tiny concentrations trigger ripening. The main lever for food that ages faster than it should.
- **Burg & Stolwijk (1959).** A Highly Sensitive Katharometer and Its Application to the Measurement of Ethylene and Other Gases of Biological Importance. *Journal of Biochemical and Microbiological Technology and Engineering* 1(3):245-259. [doi:10.1002/jbmte.390010302](https://doi.org/10.1002/jbmte.390010302)  
  A sensitive detector for ethylene built for plant research. Proof that a 1970s investigator could measure ethylene in a cold room.
- **Ratkowsky et al. (1982).** Relationship Between Temperature and Growth Rate of Bacterial Cultures. *Journal of Bacteriology* 149(1):1-5. [doi:10.1128/jb.149.1.1-5.1982](https://doi.org/10.1128/jb.149.1.1-5.1982)  
  The square-root model linking temperature to bacterial growth rate. Lets you calculate how much a few degrees changes spoilage.
- **Baranyi & Roberts (1994).** A Dynamic Approach to Predicting Bacterial Growth in Food. *International Journal of Food Microbiology* 23(3-4):277-294. [doi:10.1016/0168-1605(94)90157-0](https://doi.org/10.1016/0168-1605(94)90157-0)  
  How to model bacterial growth when temperature changes over time, as it would in a drifting district loop.
- **Labuza (1984).** Application of Chemical Kinetics to Deterioration of Foods. *Journal of Chemical Education* 61(4):348. [doi:10.1021/ed061p348](https://doi.org/10.1021/ed061p348)  
  Arrhenius and Q10 kinetics for food deterioration. Rule of thumb: a 10 degree C rise often speeds these reactions 2 to 3 times, so 'radically different rates' needs more than temperature alone.
- **Diehl (2002).** Food Irradiation: Past, Present and Future. *Radiation Physics and Chemistry* 63(3-6):211-215. [doi:10.1016/S0969-806X(01)00622-3](https://doi.org/10.1016/S0969-806X(01)00622-3)  
  History of food irradiation, including the 1950s-60s programs. A darker way food could age slowly in one area.
- **Anderson (1953).** Refrigeration in America: A History of a New Technology and Its Impact. *Princeton University Press* (book).  
  The classic history of American refrigeration, including ice plants and cold storage before the home fridge.
- **Rees (2013).** Refrigeration Nation: A History of Ice, Appliances, and Enterprise in America. *Johns Hopkins University Press* (book).  
  How ice harvesting, ice plants and appliances competed. Good detail on the businesses your fork would change.
- **Hayden (1981).** The Grand Domestic Revolution: A History of Feminist Designs for American Homes, Neighborhoods, and Cities. *MIT Press* (book).  
  Kitchenless houses and cooperative housekeeping: the communal path American homes did not take.
- **Cowan (1983).** More Work for Mother: The Ironies of Household Technology from the Open Hearth to the Microwave. *Basic Books* (book).  
  Includes the roads not taken in household technology, such as commercial laundries and communal kitchens.

*Also useful here, listed in other sections:* Cowan (1985), James & Martin (1952), Pierce (1995).
<!-- /papers:B04 -->

### 5. The Exchange

**The fork in our history**

- The Bell System kept human operators for decades because they were cheap, flexible and seen as part of the service (Lipartito 1994).
- From the 1890s into the 1910s, many towns ran 2 unconnected phone systems, Bell and an independent, and some subscribers kept both (Mueller 1993).
- Automation came in steps: crossbar switching in 1938-39 (Scudder & Reynolds 1939), then the first electronic switch in the mid-1960s (Keister et al. 1964).

**Mechanisms the papers support**

- **Dead pairs and bridged taps.** A "disconnected" line can stay physically attached to a live one through a leftover branch of cable (Reeve 2009).
- **The seam between networks.** A remnant of a second exchange never fully cut over (Mueller 1993).
- **In-band control.** Tones inside the voice channel steered the network, so anyone who could make the tones could steer calls (Weaver & Newell 1954; Breen & Dahlbom 1960). In an operator world, the equivalent is knowing an operator's codes and routines.
- **Staffing math.** Erlang's formulas predict how many operators a given load needs (Erlang 1917). A shift staffed above its recorded traffic points to calls the logs don't show.

**Watch out for**

- Pynchon's *The Crying of Lot 49* (1966) owns the "secret parallel communications network." See `02-originality.md`.

**Papers**

<!-- papers:B05 -->
- **Lipartito (1994).** When Women Were Switches: Technology, Work, and Gender in the Telephone Industry, 1890-1920. *American Historical Review* 99(4):1075-1111. [doi:10.2307/2168770](https://doi.org/10.2307/2168770)  
  Why the Bell System kept human operators for decades: operators were flexible, cheap and part of the service. The historical basis for operator routing persisting.
- **Mueller (1993).** Universal Service in Telephone History: A Reconstruction. *Telecommunications Policy* 17(5):352-369. [doi:10.1016/0308-5961(93)90050-D](https://doi.org/10.1016/0308-5961(93)90050-D)  
  The dual-service era, when many towns ran two unconnected phone networks. A ghost subscriber can live in the seam between systems.
- **Erlang (1917).** Solution of Some Problems in the Theory of Probabilities of Significance in Automatic Telephone Exchanges. *Elektroteknikeren (Danish); English translation in Post Office Electrical Engineers' Journal 10:189-197 (1918)* 13:5-13.  
  Erlang's formulas for how many operators and lines an exchange needs. Staffing records can reveal traffic the switchboard logs don't show.
- **Shannon (1938).** A Symbolic Analysis of Relay and Switching Circuits. *Transactions of the American Institute of Electrical Engineers* 57(12):713-723. [doi:10.1109/T-AIEE.1938.5057767](https://doi.org/10.1109/T-AIEE.1938.5057767)  
  Relay circuits as Boolean logic. The analysis tool for any electromechanical exchange in your world.
- **Scudder & Reynolds (1939).** Crossbar Dial Telephone Switching System. *Bell System Technical Journal* 18(1):76-118. [doi:10.1002/j.1538-7305.1939.tb00808.x](https://doi.org/10.1002/j.1538-7305.1939.tb00808.x)  
  Bell's crossbar system as introduced. The period machinery that would run alongside operators.
- **Keister et al. (1964).** No. 1 ESS: System Organization and Objectives. *Bell System Technical Journal* 43(5):1831-1844. [doi:10.1002/j.1538-7305.1964.tb04115.x](https://doi.org/10.1002/j.1538-7305.1964.tb04115.x)  
  The first electronic switching system. Marks what 1965-75 automation looked like in our history.
- **Weaver & Newell (1954).** In-Band Single-Frequency Signaling. *Bell System Technical Journal* 33(6):1309-1330. [doi:10.1002/j.1538-7305.1954.tb03755.x](https://doi.org/10.1002/j.1538-7305.1954.tb03755.x)  
  In-band single-frequency (2600 Hz) signaling, the weakness phone phreaks later exploited.
- **Breen & Dahlbom (1960).** Signaling Systems for Control of Telephone Switching. *Bell System Technical Journal* 39(6):1381-1444. [doi:10.1002/j.1538-7305.1960.tb01611.x](https://doi.org/10.1002/j.1538-7305.1960.tb01611.x)  
  Published specifications for multifrequency signaling. How outsiders learned to talk to the network.
- **Reeve (2009).** Appendix E: Reflection Loss Caused by a Bridged Tap. In Subscriber Loop Signaling and Transmission Handbook. IEEE Press / Wiley, pp. 265-274. [doi:10.1109/9780470546482.app5](https://doi.org/10.1109/9780470546482.app5)  
  Bridged taps: leftover cable branches still connected to a live line. A physical path for a 'disconnected' subscriber to stay on the wire.
- **Fischer (1992).** America Calling: A Social History of the Telephone to 1940. *University of California Press* (book).  
  How ordinary people actually used the telephone before 1940.
- **Green (2001).** Race on the Line: Gender, Labor, and Technology in the Bell System, 1880-1980. *Duke University Press* (book).  
  The operator workforce across a century, including how automation reshaped it. Essential for an operator-routed 1970s.
- **John (2010).** Network Nation: Inventing American Telecommunications. *Harvard University Press* (book).  
  How municipal politics shaped telegraph and telephone networks. Strong on the independents versus Bell.
- **Lapsley (2013).** Exploding the Phone: The Untold Story of the Teenagers and Outlaws Who Hacked Ma Bell. *Grove Press* (book).  
  History of phone phreaking, 1950s-70s. The people who treated the network as a puzzle.
<!-- /papers:B05 -->

### 6. The Meter

**The fork in our history**

- The parking meter arrived in Oklahoma City on July 16, 1935: 175 meters on 14 blocks, with timing parts from a Tulsa firm that made timers for nitroglycerin oil-well shots (Oklahoma Historical Society).
- Mechanical parking already existed. Kent Automatic Garages ran in several US cities from 1929 to the early 1960s, and the 25-story Manhattan one held about 1,000 cars (New York Times 2014).
- Los Angeles required off-street parking in 1935. By 1969, 96% of US cities over 25,000 did (Garber et al. 2024). That's the policy your world skips.

**Mechanisms the papers support**

- **Shuffling.** Automated storage systems move stored items around to speed retrieval (Roodbergen & Vis 2009; Li & Miao 2020). A car parked for 27 years can log a move every day because the machine keeps relocating it.
- **Record mismatch.** Ticket, plate and slot records drift apart, which is the record-linkage problem again (Fellegi & Sunter 1969).

**Watch out for**

- Decide the vault's record medium early: punch cards, paper tape or ledgers. The mystery depends on what the logs can and can't say.

**Papers**

<!-- papers:B06 -->
- **Oklahoma Historical Society (n.d.).** Parking Meter (Encyclopedia of Oklahoma History and Culture, entry PA015). *Oklahoma Historical Society*. [link](https://www.okhistory.org/publications/enc/entry?entry=PA015)  
  The first parking meter: Oklahoma City, July 16, 1935, with 175 meters on fourteen blocks. The mechanism came from a Tulsa firm that made timers for nitroglycerin oil-well shots.
- **New York Times (2014).** In 1929, an Automatic High-Rise Parking Garage. *New York Times, Nov. 9, 2014*. [link](https://www.nytimes.com/2014/11/09/realestate/in-1929-an-automatic-high-rise-parking-garage.html)  
  Kent Automatic Garages, 1929 to the early 1960s. The 25-story garage at 43 West 61st Street held about 1,000 cars moved by an electric 'parker' that hooked the rear axle. A working ancestor of your parking vaults.
- **Garber et al. (2024).** Parking and Public Health. *Current Environmental Health Reports*. [doi:10.1007/s40572-024-00465-4](https://doi.org/10.1007/s40572-024-00465-4)  
  Parking's health effects plus a compact history: Los Angeles required off-street parking in 1935, 12% of cities zoned for parking by 1946, and 96% of cities over 25,000 did by 1969.
- **Shoup (1999).** The Trouble with Minimum Parking Requirements. *Transportation Research Part A: Policy and Practice* 33(7-8):549-574. [doi:10.1016/S0965-8564(99)00007-5](https://doi.org/10.1016/S0965-8564(99)00007-5)  
  Minimum parking requirements reshaped American cities. If municipal vaults replace the parking lot, this paper tells you what land and street life you get back.
- **Roodbergen & Vis (2009).** A Survey of Literature on Automated Storage and Retrieval Systems. *European Journal of Operational Research* 194(2):343-362. [doi:10.1016/j.ejor.2008.01.038](https://doi.org/10.1016/j.ejor.2008.01.038)  
  Survey of automated storage and retrieval: dwell points, storage assignment, relocation. The operating logic of a mechanical parking vault.
- **Li & Miao (2020).** Automated Stereo-Garage with Multiple Cache Parking Spaces: Structure, System and Scheduling Performance. *Automation in Construction* 119:103377. [doi:10.1016/j.autcon.2020.103377](https://doi.org/10.1016/j.autcon.2020.103377)  
  Scheduling in an automated car garage with cache spaces, where cars get shuffled to speed retrieval. A mechanism for a stored car that 'moves' every day.
- **Jakle & Sculle (2004).** Lots of Parking: Land Use in a Car Culture. *University of Virginia Press* (book).  
  History of American parking lots and garages, including mechanical garages.
- **Shoup (2005).** The High Cost of Free Parking. *Planners Press* (book).  
  The long-form argument behind Shoup 1999, with the history of parking meters and requirements.

*Also useful here, listed in other sections:* Geels (2005), Fellegi & Sunter (1969).
<!-- /papers:B06 -->

### 7. The Lock

**The fork in our history**

- Pneumatic networks were real public works. Paris ran street mains that pulsed air to its clocks every minute (Popular Science Monthly 1882), and New York opened pneumatic mail in 1897 (Scientific American 1897).
- Fluidics, logic built from jets of air with no moving parts, came out of an Army lab in 1959-60 and boomed through the 1960s (Kirshner 1966, 1969).
- Master-key systems leak. One legitimate key plus a few blanks can reveal the master (Blaze 2003).

**Mechanisms the papers support**

- **Rights amplification.** A tenant's pneumatic code can reveal the building's master code the same way a single key reveals a master key (Blaze 2003).
- **Pressure spikes.** A sudden valve closure sends a shock through a network (Walters & Leishear 2018). A spike in an air main could flip a fluidic latch and log an entry that never happened.
- **The service side.** A building-wide pneumatic system has maintenance access that bypasses the front door entirely.

**Watch out for**

- The locked room is the oldest puzzle in the genre, from Poe on. The novelty here has to come from the lock's physics.

**Papers**

<!-- papers:B07 -->
- **Blaze (2003).** Rights Amplification in Master-Keyed Mechanical Locks. *IEEE Security & Privacy* 1(2):24-32. [doi:10.1109/MSECP.2003.1193208](https://doi.org/10.1109/MSECP.2003.1193208)  
  Anyone holding one legitimate key to a master-keyed system can work out the master key with a few blanks and some patience. The same logic applies to any hierarchical access system, pneumatic or otherwise.
- **Farman (2018).** Invisible and Instantaneous: Geographies of Media Infrastructure from Pneumatic Tubes to Fiber Optics. *Media Theory* 2(1):134-154. [doi:10.70064/mt.v2i1.718](https://doi.org/10.70064/mt.v2i1.718)  
  Pneumatic tubes as media infrastructure, and why people treat fast networks as instantaneous. Open access.
- **Scientific American (1897).** Opening of the Pneumatic Postal Tube Service in New York City. *Scientific American*. [doi:10.1038/scientificamerican10161897-243a](https://doi.org/10.1038/scientificamerican10161897-243a)  
  Contemporary report on New York's pneumatic mail opening in 1897. Period vocabulary and specs.
- **Popular Science Monthly (1882).** Time-Keeping in Paris. *Popular Science Monthly 20 (January 1882)*. [link](https://en.wikisource.org/wiki/Popular_Science_Monthly/Volume_20/January_1882/Time-Keeping_in_Paris)  
  Contemporary account of Paris's pneumatic clock network, which pushed a pulse of air through street mains every minute to move the clock hands.
- **Kruse (2011).** Pipeline as Network: Pneumatic Systems and the Social Order. In Park, Jankowski and Jones (eds.), The Long History of New Media. Peter Lang.  
  Pneumatic systems and the social order they built and enforced.
- **Kirshner (1966).** Fluid Amplifiers. *McGraw-Hill* (book).  
  The period textbook on fluidic amplifiers: logic built from jets of air or liquid with no moving parts.
- **Kirshner (1969).** Fluerics 28: State-of-the-Art 1969 (HDL-TR-1478). *Harry Diamond Laboratories, US Army*. [link](https://apps.dtic.mil/sti/trecms/pdf/AD0703117.pdf)  
  The Army lab that started fluidics in 1959-60 surveys what it could do by 1969. Period-accurate limits and uses for a pneumatic lock.
- **Prakash & Gershenfeld (2007).** Microfluidic Bubble Logic. *Science* 315(5813):832-835. [doi:10.1126/science.1136907](https://doi.org/10.1126/science.1136907)  
  Logic with no electronics: bubbles in tiny channels do the computing. Modern proof that fluid logic works.
- **Cole (2001).** Suspect Identities: A History of Fingerprinting and Criminal Identification. *Harvard University Press* (book).  
  How identification systems were built and trusted. Background for any system that decides who 'is' a resident.

*Also useful here, listed in other sections:* Walters & Leishear (2018), Millar (2014).
<!-- /papers:B07 -->

### 8. The Hydrant

**The fork in our history**

- Birdsill Holly's Lockport system pumped water through mains to hydrants with no reservoir or standpipe, and over 2,000 cities adopted it (National Inventors Hall of Fame).
- At Baltimore's 1904 fire, out-of-town engines couldn't couple to local hydrants. A century later, many cities still weren't on the national standard thread (Seck & Evans 2004).
- San Francisco built a separate high-pressure fire system after 1906, with its own mains, cisterns and seawater pumps (Scawthorn et al. 2006).

**Mechanisms the papers support**

- **Isotope fingerprints.** Evaporated surface water, like a canal, plots off the global meteoric water line, so a lab can tell canal water from groundwater (Craig 1961). Water with almost no tritium fell before the 1950s bomb tests, which points to a sealed cistern or a deep aquifer (Begemann & Libby 1957).
- **Network hydraulics.** A valve logged "closed" that sits open joins two pressure zones. The Hardy Cross method (Cross 1936) is how a 1970s engineer would find it.
- **Water balance.** Unaccounted-for water is a standard utility metric, and a standard clue (Puust et al. 2010).

**Watch out for**

- In a Holly-lineage city, "no reservoir" is normal. The strange thing has to be an intake or pump that isn't on the record.
- *Chinatown* (1974) owns water-politics noir. Keep the answer in hydrology.

**Papers**

<!-- papers:B08 -->
- **National Inventors Hall of Fame (n.d.).** Birdsill Holly, Jr. (inductee profile). *invent.org*. [link](https://www.invent.org/inductees/birdsill-holly-jr)  
  Holly founded the Holly Manufacturing Company in Lockport in 1859. After fires in Lockport, he built a system that pumped water through mains to hydrants with no reservoir or standpipe, and over 2,000 cities adopted it. He added district steam heating in 1877. In your world, 'no known reservoir' is normal by design, so the mystery has to be an unlisted pump or intake.
- **Seck & Evans (2004).** Major U.S. Cities Using National Standard Fire Hydrants, One Century After the Great Baltimore Fire (NISTIR 7158). *National Institute of Standards and Technology*. [doi:10.6028/NIST.IR.7158](https://doi.org/10.6028/NIST.IR.7158)  
  In 1904 Baltimore, out-of-town engines could not couple to local hydrants. The push for a national hose thread followed, and a century later many cities still hadn't adopted it. A real compatibility fork.
- **Freeman (1889).** Experiments Relating to Hydraulics of Fire Streams. *Transactions of the American Society of Civil Engineers* 21(2):303-461. [doi:10.1061/TACEAT.0000711](https://doi.org/10.1061/TACEAT.0000711)  
  The foundational fire-stream experiments: how much water, at what pressure, actually reaches a fire.
- **Scawthorn et al. (2006).** The 1906 San Francisco Earthquake and Fire: Enduring Lessons for Fire Protection and Water Supply. *Earthquake Spectra* 22(2S):135-158. [doi:10.1193/1.2186678](https://doi.org/10.1193/1.2186678)  
  San Francisco's 1906 fire and the Auxiliary Water Supply System built after it: high-pressure mains, cisterns and seawater pumping. The closest real version of your district fire mains.
- **Cross (1936).** Analysis of Flow in Networks of Conduits or Conductors (Engineering Experiment Station Bulletin 286). *University of Illinois*. [link](https://www.ideals.illinois.edu/items/4876)  
  The Hardy Cross method for solving flows in looped pipe networks. The standard hand method from 1936 into the computer era, so your investigators would use it.
- **Colebrook (1939).** Turbulent Flow in Pipes, with Particular Reference to the Transition Region Between the Smooth and Rough Pipe Laws. *Journal of the Institution of Civil Engineers* 11(4):133-156. [doi:10.1680/ijoti.1939.13150](https://doi.org/10.1680/ijoti.1939.13150)  
  The friction equation for pipe flow. With Moody's chart, the everyday tool for sizing and diagnosing mains.
- **Moody (1944).** Friction Factors for Pipe Flow. *Transactions of the ASME* 66(8):671-678.  
  The Moody chart. Any 1970s water engineer has it on the wall.
- **Walters & Leishear (2018).** When the Joukowsky Equation Does Not Predict Maximum Water Hammer Pressures. *ASME Pressure Vessels and Piping Conference (PVP2018-84050)*. [doi:10.1115/PVP2018-84050](https://doi.org/10.1115/PVP2018-84050)  
  Water hammer: a sudden valve closure sends a pressure spike through a network. Joukowsky's classic estimate, and the cases where real spikes run higher. Also covers the air-main version of the same shock for The Lock.
- **Puust et al. (2010).** A Review of Methods for Leakage Management in Pipe Networks. *Urban Water Journal* 7(1):25-45. [doi:10.1080/15730621003610878](https://doi.org/10.1080/15730621003610878)  
  How utilities find leaks and unaccounted-for water: water balances, pressure management, acoustic listening. The detective work of a water system.
- **Craig (1961).** Isotopic Variations in Meteoric Waters. *Science* 133(3465):1702-1703. [doi:10.1126/science.133.3465.1702](https://doi.org/10.1126/science.133.3465.1702)  
  The global meteoric water line. Evaporated surface water, like a canal or reservoir, plots off the line, so a 1970s lab can tell canal water from groundwater.
- **Begemann & Libby (1957).** Continental Water Balance, Ground Water Inventory and Storage Times, Surface Ocean Mixing Rates and World-Wide Water Circulation Patterns from Cosmic-Ray and Bomb Tritium. *Geochimica et Cosmochimica Acta* 12(4):277-296. [doi:10.1016/0016-7037(57)90040-6](https://doi.org/10.1016/0016-7037(57)90040-6)  
  Bomb-test tritium as a tracer. Water with almost no tritium fell as rain before the 1950s tests, which can date water from a sealed cistern or deep aquifer.
- **Knowles (2011).** The Disaster Experts: Mastering Risk in Modern America. *University of Pennsylvania Press* (book). [doi:10.9783/9780812207996](https://doi.org/10.9783/9780812207996)  
  Fire insurance engineers and the rise of safety standards. Insurance standards as a divergence cause.

*Also useful here, listed in other sections:* Pierce (1995).
<!-- /papers:B08 -->

### 9. The Crossing

**The fork in our history**

- American cities spent decades eliminating grade crossings. Chicago started raising its main-line track above street level in the 1890s under city ordinances ([Chicago track elevation history](https://www.chicagorailfan.com/elevate.html)), and the federal crossing handbook covers the national story (FHWA 2019).
- Your world finished the job everywhere, so rail runs above or below every road.

**Mechanisms the papers support**

- **Night inversions.** Temperature inversions bend sound back toward the ground, so a distant train sounds close (Piercy et al. 1977; Embleton 1996).
- **Ground-borne vibration.** Train energy travels through soil and rock and comes back up as rumble inside buildings (Colaço et al. 2025). A covered line can be heard where nothing shows on the surface.
- **A real template.** The Windsor Hum study traced a low-frequency noise across an international border to steel mills (Windsor Hum study 2014).
- **Reading the sound.** A spectrograph turns a recording into a timeline (Koenig et al. 1946). Wheel clicks at rail joints give you speed and joint spacing.

**Watch out for**

- Phantom trains are an old ghost-story staple. The acoustics has to carry this one.

**Papers**

<!-- papers:B09 -->
- **Piercy et al. (1977).** Review of Noise Propagation in the Atmosphere. *Journal of the Acoustical Society of America* 61(6):1403-1418. [doi:10.1121/1.381455](https://doi.org/10.1121/1.381455)  
  How the atmosphere bends and absorbs sound. Temperature inversions and wind gradients carry low-frequency noise far at night.
- **Embleton (1996).** Tutorial on Sound Propagation Outdoors. *Journal of the Acoustical Society of America* 100(1):31-48. [doi:10.1121/1.415879](https://doi.org/10.1121/1.415879)  
  Outdoor sound propagation, including ground effects and refraction. The physics of a train heard where it shouldn't be.
- **Colaço et al. (2025).** Ground-Borne Vibrations Induced by Railway Traffic: Impact, Prediction, Mitigation and Future Perspectives. *Vibration* 8(4):73. [doi:10.3390/vibration8040073](https://doi.org/10.3390/vibration8040073)  
  Review of railway ground vibration: how train energy moves through soil and rock and comes back up as rumble inside buildings. Open access.
- **University of Western Ontario & University of Windsor (for Foreign Affairs (2014).** Investigation of the Windsor Hum. *Government of Canada (summary of results)*. [link](https://www.international.gc.ca/department-ministere/windsor_hum_results-bourdonnement_windsor_resultats.aspx?lang=eng)  
  A real low-frequency noise traced across an international border to blast-furnace operations on Zug Island. A model investigation for a sound with no visible source.
- **Deming (2004).** The Hum: An Anomalous Sound Heard Around the World. *Journal of Scientific Exploration* 18(4):571-595.  
  Survey of 'Hum' reports since the 1970s. Shows how hard low-frequency sources are to locate and how communities react. Published in a fringe-leaning journal, so treat it as a record of reports.
- **Ogden & Cooper (2019).** Highway-Rail Crossing Handbook, Third Edition (FHWA-SA-18-040). *Federal Highway Administration*. [link](https://highways.dot.gov/safety/hsip/xings/highway-rail-crossing-handbook-third-edition)  
  The federal handbook on grade crossings, including the history of crossing elimination. What your world did everywhere, done here case by case.
- **Stilgoe (1983).** Metropolitan Corridor: Railroads and the American Scene. *Yale University Press* (book).  
  The railroad landscape of 1880-1930: embankments, cuts, stations, the corridor as a place.

*Also useful here, listed in other sections:* Koenig et al. (1946).
<!-- /papers:B09 -->

### 10. The Dial

**The fork in our history**

- American district heating starts with Holly's 1877 Lockport steam system (Pierce 1995).
- Engineers wanted whole-building "manufactured weather." Consumers bought window units (Cooper 1998). Home air conditioning spread fast from 1955 to 1980 (Biddle 2008).
- Your 68 degrees F has a date: Nixon's energy address of November 7, 1973 asked for a national daytime average of 68 (Nixon 1973).

**Mechanisms the papers support**

- **Variable-conductance heat pipe.** It holds a set temperature with no power and no thermostat (Grover et al. 1964; Marcus 1972). Tapped into a live district main, one could hold a sealed apartment steady.
- **Phase-change mass.** A mass that melts near room temperature pins the room there while heat keeps flowing (Zalba et al. 2003; Telkes 1980).
- **Feedback somewhere.** Any steady temperature implies a governor (Maxwell 1868). The investigator's job is to find the loop.

**Watch out for**

- "Exactly 68 while disconnected" needs both a heat source and a regulator. Without both, the room drifts.
- *Brazil*'s ductwork and SCP-style "anomalous objects" sit close in tone. Keep the answer in physics.

**Papers**

<!-- papers:B10 -->
- **Maxwell (1868).** On Governors. *Proceedings of the Royal Society of London* 16:270-283. [doi:10.1098/rspl.1867.0055](https://doi.org/10.1098/rspl.1867.0055)  
  The first mathematical analysis of feedback governors. A thermostat is a governor, so this is where its theory starts.
- **Carrier (1911).** Rational Psychrometric Formulae: Their Relation to the Problems of Meteorology and of Air Conditioning. *Transactions of the ASME* 33:1005-1039. [doi:10.1115/1.4060116](https://doi.org/10.1115/1.4060116)  
  Carrier's psychrometric formulas, the base of engineered air conditioning.
- **Grover et al. (1964).** Structures of Very High Thermal Conductance. *Journal of Applied Physics* 35(6):1990-1991. [doi:10.1063/1.1713792](https://doi.org/10.1063/1.1713792)  
  The heat pipe, invented at Los Alamos: fast, passive heat transport with no pump. Period-accurate hardware for a room held at temperature by something hidden.
- **Marcus (1972).** Theory and Design of Variable Conductance Heat Pipes (NASA CR-2018). *NASA*. [link](https://ui.adsabs.harvard.edu/abs/1972ntrs.rept16303M/abstract)  
  Variable-conductance heat pipes hold a set temperature on their own using a gas reservoir. Spacecraft hardware that keeps a set point with no power and no thermostat.
- **Zalba et al. (2003).** Review on Thermal Energy Storage with Phase Change: Materials, Heat Transfer Analysis and Applications. *Applied Thermal Engineering* 23(3):251-283. [doi:10.1016/S1359-4311(02)00192-8](https://doi.org/10.1016/S1359-4311(02)00192-8)  
  Phase-change materials soak up and release heat at a fixed melting point. A large mass that melts near 20 degrees C (68 degrees F) pins a room near that temperature.
- **Telkes (1980).** Thermal Storage in Salt-Hydrates. In Murr (ed.), Solar Materials Science. Academic Press, pp. 377-404. [doi:10.1016/B978-0-12-511160-7.50019-3](https://doi.org/10.1016/B978-0-12-511160-7.50019-3)  
  Salt-hydrate heat storage from Maria Telkes, who built the 1948 Dover Sun House around it.
- **Cooper (1998).** Air-Conditioning America: Engineers and the Controlled Environment, 1900-1960. *Johns Hopkins University Press* (book).  
  Engineers wanted whole-building 'manufactured weather'; consumers bought window units. The exact fork The Dial bends.
- **Biddle (2008).** Explaining the Spread of Residential Air Conditioning, 1955-1980. *Explorations in Economic History* 45(4):402-423. [doi:10.1016/j.eeh.2008.02.004](https://doi.org/10.1016/j.eeh.2008.02.004)  
  Why home air conditioning spread from 1955 to 1980: incomes, prices, climate. The spread your world routes through district systems.
- **Arsenault (1984).** The End of the Long Hot Summer: The Air Conditioner and Southern Culture. *Journal of Southern History* 50(4):597-628. [doi:10.2307/2208474](https://doi.org/10.2307/2208474)  
  How air conditioning remade the South. With district climate in place of window units, some of that shift weakens.
- **Glaeser & Tobio (2008).** The Rise of the Sunbelt. *Southern Economic Journal* 74(3):609-643. [doi:10.1002/j.2325-8012.2008.tb00856.x](https://doi.org/10.1002/j.2325-8012.2008.tb00856.x)  
  Argues Sunbelt growth owed more to housing supply and productivity than to air conditioning. Keeps the 'AC built the Sunbelt' claim honest.
- **Barreca et al. (2016).** Adapting to Climate Change: The Remarkable Decline in the US Temperature-Mortality Relationship over the Twentieth Century. *Journal of Political Economy* 124(1):105-159. [doi:10.1086/684582](https://doi.org/10.1086/684582)  
  Air conditioning drove the fall in US heat deaths after 1960. A district-climate world needs its own version of that health story.
- **Lund et al. (2014).** 4th Generation District Heating (4GDH): Integrating Smart Thermal Grids into Future Sustainable Energy Systems. *Energy* 68:1-11. [doi:10.1016/j.energy.2014.02.089](https://doi.org/10.1016/j.energy.2014.02.089)  
  The four generations of district heating, from steam to low-temperature networks. Tells you which generation your 1970s city runs.
- **Werner (2017).** International Review of District Heating and Cooling. *Energy* 137:617-631. [doi:10.1016/j.energy.2017.04.045](https://doi.org/10.1016/j.energy.2017.04.045)  
  Where district heating and cooling won worldwide, and why.
- **Nixon (1973).** Address to the Nation About Policies To Deal With the Energy Shortages (November 7, 1973). *The American Presidency Project*. [link](https://www.presidency.ucsb.edu/documents/address-the-nation-about-policies-deal-with-the-energy-shortages)  
  Nixon asked Americans to turn thermostats down at least 6 degrees for a national daytime average of 68 degrees F. Your 68 degrees has a date.

*Also useful here, listed in other sections:* Østergaard et al. (2022), Pierce (1995).
<!-- /papers:B10 -->

---

## Part C. The investigator's toolkit, 1962-1982

Period accuracy keeps your never-explain rule honest. If an investigator solves something with a method that didn't exist yet, readers notice.

| Method | Usable from | What it tells your investigator | Source |
|---|---|---|---|
| Pipe network analysis | 1936 | Flows and pressures in looped mains | Cross 1936 |
| Relay logic analysis | 1938 | How a switching circuit will behave | Shannon 1938 |
| Sound spectrograph | 1946 | Frequency over time of any recorded sound | Koenig et al. 1946 |
| Gas chromatography | 1952; routine by the 1960s | Which gases and volatiles are present | James & Martin 1952 |
| Tritium dating of water | late 1950s | Whether water fell before or after the bomb tests | Begemann & Libby 1957 |
| Ethylene detection | 1959 | Ripening gas at very low levels | Burg & Stolwijk 1959 |
| Record linkage | 1959; theory in 1969 | Whether two records are the same person or place | Newcombe et al. 1959; Fellegi & Sunter 1969 |
| Stable isotopes of water | 1961 | Evaporated surface water versus groundwater | Craig 1961 |
| Crash reconstruction | Baker's manual, 1975 edition | Speeds, paths and sequence from physical evidence | Baker 1975 |
| Teletraffic math | 1917 | Expected calls and operator staffing | Erlang 1917 |

**Not available yet:** DNA fingerprinting (1985, Jeffreys et al.), civilian satellite positioning, desktop computers in municipal offices, and mobile phones. Your investigators have punch cards, tape recorders, oscilloscopes, survey levels and a lot of carbon paper.

<!-- papers:C -->
- **Koenig et al. (1946).** The Sound Spectrograph. *Journal of the Acoustical Society of America* 18(1):19-49. [doi:10.1121/1.1916342](https://doi.org/10.1121/1.1916342)  
  Bell Labs' sound spectrograph: a picture of sound over time. Lets an investigator read a train's wheel rhythm or a machine's hum off paper.
- **James & Martin (1952).** Gas-Liquid Partition Chromatography: The Separation and Micro-Estimation of Volatile Fatty Acids from Formic Acid to Dodecanoic Acid. *Biochemical Journal* 50(5):679-690. [doi:10.1042/bj0500679](https://doi.org/10.1042/bj0500679)  
  The founding paper of gas chromatography. By the 1960s, GC identifies gases, solvents and fuels in routine labs.
- **Fellegi & Sunter (1969).** A Theory for Record Linkage. *Journal of the American Statistical Association* 64(328):1183-1210. [doi:10.1080/01621459.1969.10501049](https://doi.org/10.1080/01621459.1969.10501049)  
  The statistical theory for matching records across databases that share no clean key. Exactly the work of a clerk reconciling two city databases, and the way a false match creates a person who never existed.
- **Newcombe et al. (1959).** Automatic Linkage of Vital Records. *Science* 130(3381):954-959. [doi:10.1126/science.130.3381.954](https://doi.org/10.1126/science.130.3381.954)  
  Early computer linkage of birth and marriage records. Evidence that probabilistic matching was already in use by 1959.
- **Jeffreys et al. (1985).** Individual-Specific 'Fingerprints' of Human DNA. *Nature* 316(6023):76-79. [doi:10.1038/316076a0](https://doi.org/10.1038/316076a0)  
  Boundary marker: DNA fingerprinting arrives in 1985, after your window. A 1962-82 story can't use it.

*Also useful here, listed in other sections:* Baker (1975), Burg & Stolwijk (1959), Erlang (1917), Shannon (1938), Cross (1936), Craig (1961), Begemann & Libby (1957).
<!-- /papers:C -->

---

## Part D. Setting sources

The case for Lockport is in `03-city.md`. These are the papers behind it.

<!-- papers:D -->
- **Pierce (1995).** The Road to Lockport: Historical Background of District Heating and Cooling. *ASHRAE Transactions* 101(1). [link](https://www.osti.gov/biblio/87450)  
  Birdsill Holly installed the first successful commercial district heating system in Lockport in 1877; more than 50 existed by 1890, and district cooling with brine and ammonia followed. The historical anchor for putting the collection in Lockport.
- **Jia & Crabtree (2015).** The International Niagara Commission of 1891. In Driven by Demand: How Energy Gets Its Power. Cambridge University Press, pp. 93-108. [doi:10.1017/CBO9781316221778.005](https://doi.org/10.1017/CBO9781316221778.005)  
  The 1890-91 commission that judged how to send Niagara's power to Buffalo. The documented decision point your energy fork bends.
- **Lubar (1989).** Transmitting the Power of Niagara: Scientific, Technological, and Cultural Contexts of an Engineering Decision. *IEEE Technology and Society Magazine* 8(1):11-18. [doi:10.1109/44.17682](https://doi.org/10.1109/44.17682)  
  Argues the Niagara choice rested on cultural assumptions as much as engineering. Good material for engineers arguing at your fork.
- **Barnett (2020).** Energy in Niagara Falls: International Niagara Commission [History]. *IEEE Power and Energy Magazine* 18(4):76-86. [doi:10.1109/MPE.2020.2967906](https://doi.org/10.1109/MPE.2020.2967906)  
  IEEE history of the commission and its competition entries.
- **Millar (2014).** A Review of the Case for Modern-Day Adoption of Hydraulic Air Compressors. *Applied Thermal Engineering* 69(1-2):55-77. [doi:10.1016/j.applthermaleng.2014.04.008](https://doi.org/10.1016/j.applthermaleng.2014.04.008)  
  Review of hydraulic air compressors, trompe-style machines that make compressed air from falling water with almost no moving parts. The Ragged Chutes plant in Ontario ran on this principle from 1910 for about 70 years.
- **Newman (2016).** Love Canal: A Toxic History from Colonial Times to the Present. *Oxford University Press* (book). [link](https://academic.oup.com/book/40956)  
  Includes William T. Love's canal and Model City plan of the 1890s, and how the unfinished ditch became Love Canal.

*Also useful here, listed in other sections:* National Inventors Hall of Fame (n.d.), Biddle (2008), Arsenault (1984), Glaeser & Tobio (2008).
<!-- /papers:D -->
