# Facts to check

The corpus is a reference shelf. These are the 36 facts the stories lean on: 5 for the city, 2 to 4 per story and 1 for the investigators' toolkit. Check these and leave the rest on the shelf.

Each fact has how sure I am, the cheapest way to check it (free sources first), the corpus source behind it, and what changes in the story if it's wrong. Numbers like #37 point to the reading order.

This file is generated from `facts.csv`. Edit the CSV, then run `python3 story-research/tools/build_facts.py`.

## How sure I am

- **High:** widely documented. Most of these were also confirmed by a web search on October 5, 2026.
- **Medium:** I believe it, but a detail could be off, or I couldn't confirm the key part.
- **Low:** plausible on paper, and I know of no documented case.

## Start with these 6

- **I3** · Local Niagara stone probably doesn’t swell in concrete (Medium)
- **I4** · Elevations ran on more than one datum (Medium)
- **R3** · Temperature can do more than I first said (Medium)
- **M3** · Automated storage moves cars on its own (Medium)
- **K3** · A pressure surge could flip a fluidic latch (Low)
- **D2** · A melting mass can pin a room’s temperature (Medium)

## What changed while I built this

Checking turned up 4 corrections. They're fixed in `01-science-corpus.md` too:

- **I4** · Elevations ran on more than one datum
- **N3** · NAD 83 arrived after your window
- **R3** · Temperature can do more than I first said
- **M2** · Robot parking ran in Manhattan from 1929

## The city: Lockport

- [ ] **C1 · Holly’s district heating started in Lockport.** Birdsill Holly installed the first successful commercial district heating system in Lockport in 1877, and more than 50 were running by 1890.
  - **How sure:** High. Pierce’s abstract says so, and a search on Oct. 5 agreed. While you’re in the paper, check what it says about early district cooling, which Cold Room borrows.
  - **Check first:** [Pierce 1995 abstract (OSTI)](https://www.osti.gov/biblio/87450) · [Birdsill Holly (National Inventors Hall of Fame)](https://www.invent.org/inductees/birdsill-holly-jr)
  - **Then:** Pierce 1995 (#12)
  - **If it's wrong:** The setting loses its origin story.
- [ ] **C2 · The Niagara Commission rejected every plan, pneumatic ones included.** In 1890-91 the International Niagara Commission, headed by Lord Kelvin, reviewed schemes ranging from pneumatic pressure to ropes, springs and pulleys, plus direct current. It rejected them all, and Westinghouse won the alternating-current contract in late 1893.
  - **How sure:** High. PBS says this almost word for word, and a search on Oct. 5 agreed.
  - **Check first:** [Tesla and Niagara (PBS)](https://www.pbs.org/tesla/ll/ll_niagara.html)
  - **Then:** Jia & Crabtree 2015 (#14); Lubar 1989 (#15)
  - **If it's wrong:** Your power fork needs a different decision point.
- [ ] **C3 · City-scale water and air power worked.** London Hydraulic Power, founded in 1883, ran about 180 miles of 800 psi water mains until its last pump house closed in 1977, driving lifts, cranes and theater stages. Paris pushed compressed air through street mains, first to run its clocks.
  - **How sure:** High. A search on Oct. 5 agreed on London’s numbers. The Paris clocks are in an 1882 magazine article.
  - **Check first:** [London Hydraulic Power Company (Wikipedia)](https://en.wikipedia.org/wiki/London_Hydraulic_Power_Company) · [Time-Keeping in Paris, 1882 (Wikisource)](https://en.wikisource.org/wiki/Popular_Science_Monthly/Volume_20/January_1882/Time-Keeping_in_Paris)
  - **Then:** Popular Science Monthly 1882 (#22)
  - **If it's wrong:** The whole world gets harder to believe.
- [ ] **C4 · Falling water can make compressed air.** Charles Taylor’s hydraulic air compressor at Ragged Chutes, on the Montreal River near Cobalt, Ontario, opened in 1910 and fed compressed air to mines for about 70 years, with almost no moving parts.
  - **How sure:** High. A search on Oct. 5 agreed on 1910, the place and the inventor. The 70-year run comes from secondary sources, so treat it as approximate.
  - **Check first:** [Trompe (Wikipedia)](https://en.wikipedia.org/wiki/Trompe) · [The Hydraulic Air Compressor: An Old Idea Made New](https://www.airbestpractices.com/technology/air-compressors/hydraulic-air-compressor-old-idea-made-new)
  - **Then:** Millar 2014 (#16)
  - **If it's wrong:** Lockport’s compressor halls need a different machine.
- [ ] **C5 · Love’s Model City became Love Canal.** William T. Love proposed a power-canal city in 1893, broke ground in 1894, dug about a mile and lost his investors by 1897. The unfinished ditch became Love Canal.
  - **How sure:** High. Well documented locally. Love Canal has living victims, so handle the mirror with care.
  - **Check first:** [Model City (Discover Niagara)](https://www.discoverniagara.org/model-city-pre-wwii) · [The dream and demise of Model City (Lockport Union-Sun & Journal)](https://www.lockportjournal.com/news/lifestyles/niagara-discoveries-the-dream-and-demise-of-model-city/article_e29081d6-e38b-5e3d-b7c6-67facbe2dc8a.html)
  - **Then:** Newman 2016 (#17)
  - **If it's wrong:** The mirror you never explain stops working.

## The Intersection (traffic light)

- [ ] **I1 · London’s first traffic signal blew up.** London put the first traffic signal outside Parliament on December 9, 1868. A gas leak blew it up on January 2, 1869, burning the policeman who ran it, and London’s next signal was an electric one in 1926.
  - **How sure:** High. A search on Oct. 5 agreed on all 3 dates.
  - **Check first:** [First traffic lights (Smithsonian)](https://www.smithsonianmag.com/smart-news/chaotic-traffic-from-horse-drawn-carriages-inspired-the-worlds-first-traffic-lights-180985558/)
  - **Then:** McShane 1999 (#34)
  - **If it's wrong:** You lose a real freak-accident fork.
- [ ] **I2 · Separated roads still collide in the weave.** Grade separation removes crossing conflicts and adds merges and weaves near ramps, which is where interchange crashes concentrate.
  - **How sure:** High. A standard traffic-safety finding, with a free FHWA report behind it.
  - **Check first:** [Safety Performance for Freeway Weaving Segments (FHWA)](https://rosap.ntl.bts.gov/view/dot/28221)
  - **Then:** Pulugurtha & Bhatt 2010 (#35)
  - **If it's wrong:** Roads that never cross can’t hit each other, and the story needs a new mechanism.
- [ ] **I3 · Local Niagara stone probably doesn’t swell in concrete.** Quarried Niagara Escarpment dolostone isn’t alkali-reactive, so concrete that grows needs imported stone. The classic swelling rock comes from Kingston, Ontario, where the alkali-carbonate reaction was identified in 1957.
  - **How sure:** Medium. A search on Oct. 5 confirmed the Kingston history and that the escarpment’s Amabel dolostone is a major Ontario concrete aggregate. I couldn’t confirm the non-reactive claim itself.
  - **Check first:** [15 Years of Living at Kingston with a Reactive Carbonate Rock (TRB, 1974)](https://onlinepubs.trb.org/Onlinepubs/trr/1974/525/525-003.pdf)
  - **Then:** Rogers et al. 2000 (#37)
  - **If it's wrong:** If local stone can swell, you lose the imported-stone clue.
- [ ] **I4 · Elevations ran on more than one datum.** *(corrected)* Before NAVD 88, US elevations used NGVD 29, and some cities and the New York State Barge Canal kept their own vertical datums. Two correct drawings on different datums can disagree by a foot or more.
  - **How sure:** Medium. A search on Oct. 5 confirmed NGVD 29, local city datums like Chicago’s, and that USGS lists a separate Barge Canal datum. I don’t know the Barge Canal’s offset. The corpus’s datum papers cover map coordinates, which is the wrong kind of datum for elevations.
  - **Check first:** [USGS vertical datum codes, which list BARGECANAL](https://help.waterdata.usgs.gov/code/alt_datum_cd_query?fmt=rdb) · [NGVD 29 (Wikipedia)](https://en.wikipedia.org/wiki/National_Geodetic_Vertical_Datum_of_1929)
  - **Then:** The NY Canal Corporation or a local surveyor, for the Barge Canal offset
  - **If it's wrong:** The mismatched elevations need a different cause.

## The Number (street address)

- [ ] **N1 · Broken coordinates pile up at (0, 0).** Blank or failed coordinates collapse to (0, 0), and data systems start treating that point as a real place. GIS people call it Null Island.
  - **How sure:** High. Well documented in modern GIS, and the paper is open access. A 1970s version is your world’s design.
  - **Check first:** [Juhász & Mooney 2022 (IEEE Access, free)](https://doi.org/10.1109/ACCESS.2022.3197222)
  - **Then:** Same paper (#40)
  - **If it's wrong:** Your grid origin can’t collect stray mail.
- [ ] **N2 · Record matching could merge or invent people by 1959.** Probabilistic record linkage ran on computers by 1959 and got its formal theory in 1969. False matches can merge 2 people into 1 or create a person who never existed.
  - **How sure:** High. Both papers are classics, and a free overview covers the method.
  - **Check first:** [Record linkage (Wikipedia)](https://en.wikipedia.org/wiki/Record_linkage)
  - **Then:** Fellegi & Sunter 1969 (#42); Newcombe et al. 1959
  - **If it's wrong:** The clerk’s false-person mystery needs a different engine.
- [ ] **N3 · NAD 83 arrived after your window.** *(corrected)* The NAD 27 to NAD 83 readjustment came in 1986 and moved positions by roughly 10 to 100 meters across the US. Any datum change inside 1962-82 has to be your city’s own.
  - **How sure:** High. The National Geodetic Survey’s own documentation, and a search on Oct. 5 agreed.
  - **Check first:** [Dewhurst 1990, NADCON (NGS, free PDF)](https://www.ngs.noaa.gov/PUBS_LIB/NGS50.pdf) · [NADCON readme (NGS)](https://www.ngs.noaa.gov/PC_PROD/NADCON/Readme.htm)
  - **Then:** Dewhurst 1990 (#36)
  - **If it's wrong:** Using NAD 83 inside your window would be an anachronism.

## The Lift (elevator)

- [ ] **L1 · Paternosters moved more people, and safety stopped them.** In a 2008 survey at Sheffield’s Arts Tower, the paternoster moved 60 people per 5 minutes against 40 for the building’s conventional lifts. A 1970 death in Newcastle led UK paternosters to add car-stability tracking, and new ones are effectively no longer built.
  - **How sure:** High. This is the one source in the corpus I read in full, and it’s free.
  - **Check first:** [Bottomley 2014 (free PDF)](https://liftescalatorlibrary.org/paper_indexing/papers/00000067.pdf)
  - **Then:** Same paper (#43)
  - **If it's wrong:** The fork’s numbers change.
- [ ] **L2 · Riders can stay on through the turnover.** A paternoster car crosses over the top and under the bottom of its loop and stays upright, so a rider who stays aboard passes through machine space no floor plan shows.
  - **How sure:** High. Widely described by riders and lift engineers. I haven’t confirmed it in these 2 sources.
  - **Check first:** [The Paternoster: A Requiem (Granta)](https://granta.com/paternoster-a-requiem/) · [Bottomley 2014 (free PDF)](https://liftescalatorlibrary.org/paper_indexing/papers/00000067.pdf)
  - **Then:** Bottomley 2014 (#43)
  - **If it's wrong:** The “reaches places no log records” mechanism fails.

## Cold Room (refrigerator)

- [ ] **R1 · Ethylene ripens everything nearby.** Ripening fruit gives off ethylene, and tiny amounts, well under 1 part per million, set off ripening in nearby fruit. Labs could measure it at those levels by the early 1960s.
  - **How sure:** High. A classic finding, and the 1962 paper is free on PubMed Central.
  - **Check first:** [Burg & Burg 1962 (PubMed Central, free)](https://pmc.ncbi.nlm.nih.gov/articles/PMC549760)
  - **Then:** Same paper (#31); Burg & Stolwijk 1959 (#33)
  - **If it's wrong:** Your fast-aging mechanism needs replacing.
- [ ] **R2 · Low oxygen and high carbon dioxide slow ripening.** Kidd and West showed in the 1920s that raising carbon dioxide and lowering oxygen slows ripening. England’s first commercial “gas storage” for apples opened in 1929.
  - **How sure:** High. A search on Oct. 5 agreed on the dates.
  - **Check first:** [Controlled atmosphere (Wikipedia)](https://en.wikipedia.org/wiki/Controlled_atmosphere)
  - **Then:** Kidd & West 1930
  - **If it's wrong:** Your slow-aging mechanism needs replacing.
- [ ] **R3 · Temperature can do more than I first said.** *(corrected)* Chemical quality loss speeds up about 2 to 3 times per 10°C. Microbial spoilage near fridge temperatures is more sensitive, often 4 to 10 times per 10°C, so a cold room drifting from 1°C to 8°C could spoil food several times faster.
  - **How sure:** Medium. The corpus said temperature alone couldn’t change spoilage much. A search on Oct. 5 turned up Q10 values of 2 to 10 for refrigerated foods, which fits Ratkowsky’s growth model.
  - **Check first:** [Ratkowsky et al. 1982, Journal of Bacteriology](https://doi.org/10.1128/jb.149.1.1-5.1982)
  - **Then:** Labuza 1984 (#32)
  - **If it's wrong:** If temperature can’t do it, you’re back to ethylene or atmosphere.

## The Exchange (telephone number)

- [ ] **E1 · Human operators ran the network at huge scale.** AT&T employed more than 350,000 telephone operators at its peak in the late 1940s, nearly all of them women.
  - **How sure:** High. A search on Oct. 5 agreed, citing the IEEE’s history wiki.
  - **Check first:** [Telephone Operators (IEEE history wiki, free)](https://ethw.org/Telephone_Operators)
  - **Then:** Lipartito 1994 (#50); Green 2001
  - **If it's wrong:** An operator-routed 1970s needs a different labor story.
- [ ] **E2 · A disconnected line can stay on the wire.** Phone pairs were wired to appear at several terminals along a cable. When a customer disconnected, the pair stayed in place, still wired to every terminal, and unused branches called bridged taps hung off working lines.
  - **How sure:** High. Standard practice in telephone cable plant.
  - **Check first:** [Bridge tap (Wikipedia)](https://en.wikipedia.org/wiki/Bridge_tap)
  - **Then:** Reeve 2009 (#52)
  - **If it's wrong:** The ghost subscriber needs a different path onto the network.
- [ ] **E3 · Erlang’s math predicts how many operators a load needs.** Erlang’s 1917 formulas turn call traffic into operator and trunk counts, and they were standard tools by mid-century. A shift staffed well above its logged calls points to traffic the logs don’t show.
  - **How sure:** High. The formulas are textbook. The staffing tell is my inference, built on them.
  - **Check first:** [Erlang (unit) (Wikipedia)](https://en.wikipedia.org/wiki/Erlang_(unit))
  - **Then:** Erlang 1917 (#53)
  - **If it's wrong:** The solve needs a different tell.

## The Meter (parking meter)

- [ ] **M1 · The first parking meter.** Oklahoma City installed 175 parking meters on 14 blocks on July 16, 1935, with timing parts from a Tulsa firm that made timers for nitroglycerin oil-well shots.
  - **How sure:** High. From the Oklahoma Historical Society’s encyclopedia.
  - **Check first:** [Parking Meter (Encyclopedia of Oklahoma History, free)](https://www.okhistory.org/publications/enc/entry?entry=PA015)
  - **Then:** Shoup 2005
  - **If it's wrong:** Your fork’s date moves.
- [ ] **M2 · Robot parking ran in Manhattan from 1929.** *(corrected)* The Kent Automatic Garage at 43 West 61st Street, built in 1929-30, was a 25-story tower for about 1,000 cars, moved by an electric “parker” that hooked each car’s rear axle. It ran as a garage until 1943.
  - **How sure:** High. The corpus said the Kent garages ran into the early 1960s. This building stopped in 1943, and I haven’t confirmed the company’s other garages.
  - **Check first:** [Kent Automatic Garages (Wikipedia)](https://en.wikipedia.org/wiki/Kent_Automatic_Garages) · [New York Times, 2014 (free with an account)](https://www.nytimes.com/2014/11/09/realestate/in-1929-an-automatic-high-rise-parking-garage.html)
  - **Then:** Jakle & Sculle 2004
  - **If it's wrong:** Your vaults lose their real ancestor.
- [ ] **M3 · Automated storage moves cars on its own.** Automated storage systems shuffle stored items into better positions to speed later retrievals, so a car that never left can log a move every day.
  - **How sure:** Medium. Shuffling cars through cache spaces is the subject of Li & Miao, which I haven’t read. A 1960s-70s garage doing it is your world’s design.
  - **Check first:** [Roodbergen & Vis 2009 (Erasmus repository, may have a free copy)](https://repub.eur.nl/pub/13640)
  - **Then:** Li & Miao 2020 (#49)
  - **If it's wrong:** The 27-year car needs another explanation.

## The Lock (house key)

- [ ] **K1 · One key can reveal the master.** With one legitimate key to a master-keyed system, a few blank keys and a file, you can work out the master key without doing anything suspicious at the lock.
  - **How sure:** High. A well-known security paper, free on the author’s site.
  - **Check first:** [Blaze 2003 (free PDF)](https://www.mattblaze.org/papers/mk.pdf)
  - **Then:** Same paper (#24)
  - **If it's wrong:** The tenant-code mechanism fails.
- [ ] **K2 · Air-jet logic boomed in the 1960s.** Engineers at the Army’s Diamond Ordnance Fuze Laboratories, later Harry Diamond Laboratories, built working fluid amplifiers in 1959, and fluidic controls drew heavy industry interest through the 1960s.
  - **How sure:** High. A search on Oct. 5 agreed, and the Army’s 1969 survey is free.
  - **Check first:** [Kirshner 1969, Fluerics 28 (DTIC, free PDF)](https://apps.dtic.mil/sti/trecms/pdf/AD0703117.pdf) · [Fluidics (Wikipedia)](https://en.wikipedia.org/wiki/Fluidics)
  - **Then:** Kirshner 1966
  - **If it's wrong:** Your pneumatic locks need different logic.
- [ ] **K3 · A pressure surge could flip a fluidic latch.** Joukowsky’s surge rule applies to air as well as water, and air’s low density keeps surges small. My rough estimate for a city air main is a few psi, which is about where fluidic devices switch. It’s plausible on paper, and I know of no documented case.
  - **How sure:** Low. This one is my own inference. Ask a fluid-power engineer, or look in Kirshner 1969 for what upset fluidic circuits.
  - **Check first:** [Kirshner 1969 (DTIC, free PDF)](https://apps.dtic.mil/sti/trecms/pdf/AD0703117.pdf)
  - **Then:** Walters & Leishear 2018 (#25) covers water hammer only
  - **If it's wrong:** The phantom entry needs another cause, like the building’s service side.

## The Hydrant (fire hydrant)

- [ ] **H1 · San Francisco built a separate fire-water system.** After the 1906 earthquake and fire, San Francisco built its Auxiliary Water Supply System from 1909 to 1913: high-pressure mains, a reservoir, pump stations that can draw bay water, cisterns, fireboats and its own oversized hydrants.
  - **How sure:** High. A search on Oct. 5 agreed.
  - **Check first:** [SF Auxiliary Water Supply System (Wikipedia)](https://en.wikipedia.org/wiki/San_Francisco_Fire_Department_Auxiliary_Water_Supply_System) · [Museum of the City of San Francisco](https://sfmuseum.org/quake/awss2.html)
  - **Then:** Scawthorn et al. 2006 (#18)
  - **If it's wrong:** Your district fire mains lose their real model.
- [ ] **H2 · Isotopes tell canal water from groundwater.** Rain and snow plot along Craig’s 1961 meteoric water line. Evaporated water, like a canal or reservoir, plots below it, so a 1970s lab could tell surface water from groundwater.
  - **How sure:** High. Textbook isotope hydrology, and USGS explains it for free.
  - **Check first:** [USGS Isotope Tracers: hydrogen](https://wwwrcamnl.wr.usgs.gov/isoig/period/h_iig.html)
  - **Then:** Craig 1961 (#20)
  - **If it's wrong:** The hydrant’s water can’t be fingerprinted.
- [ ] **H3 · Tritium dates water to before or after 1953.** Bomb tests from the early 1950s spiked tritium in rain, peaking in 1963-64. Water with almost no tritium fell before 1953, which points to a sealed cistern or a deep aquifer.
  - **How sure:** High. USGS covers it, and labs were measuring tritium in water by the late 1950s.
  - **Check first:** [Tritium as an indicator of groundwater age (USGS, free)](https://pubs.usgs.gov/publication/sir20195090)
  - **Then:** Begemann & Libby 1957 (#21)
  - **If it's wrong:** The pre-1953 water clue fails.

## The Crossing (railroad crossing gate)

- [ ] **X1 · Night inversions carry train sound.** At night, cool air near the ground under warmer air bends sound back down, so a distant train can sound close.
  - **How sure:** High. Textbook outdoor acoustics.
  - **Check first:** [Why sounds travel farther at night (COMSOL)](https://www.comsol.com/blogs/why-sounds-travel-farther-at-night)
  - **Then:** Embleton 1996 (#55)
  - **If it's wrong:** The phantom train needs another way to carry.
- [ ] **X2 · Trains shake the ground.** Train vibration travels through soil and rock and comes up inside buildings as a low rumble, so a covered line can be heard where nothing shows on the surface.
  - **How sure:** High. The federal transit noise manual covers ground-borne vibration and noise.
  - **Check first:** [FTA Transit Noise and Vibration Impact Assessment Manual, 2018 (free PDF)](https://www.transit.dot.gov/sites/fta.dot.gov/files/docs/research-innovation/118131/transit-noise-and-vibration-impact-assessment-manual-fta-report-no-0123_0.pdf)
  - **Then:** Colaço et al. 2025 (#56, also free)
  - **If it's wrong:** The buried line can’t be heard.
- [ ] **X3 · A 1970s investigator could see sound.** Bell Labs published the sound spectrograph in 1946, and Kay Electric sold its Sona-Graph from 1951, so a 1970s investigator could turn a recording into a picture of frequency over time.
  - **How sure:** High. A search on Oct. 5 agreed on both dates.
  - **Check first:** [Sound spectrograph (museum record)](https://chsi.emuseum.com/objects/22484/sound-spectrograph)
  - **Then:** Koenig et al. 1946 (#58)
  - **If it's wrong:** The solve needs a different instrument.

## The Dial (thermostat)

- [ ] **D1 · Heat pipes hold temperature with no power.** George Grover built the modern heat pipe at Los Alamos in 1963 and published it in 1964. NASA developed gas-loaded variable-conductance versions that hold a set temperature on their own, and published their theory and design in a 1972 report.
  - **How sure:** High. A search on Oct. 5 agreed on Grover and NASA’s role, and the 1972 NASA report is free.
  - **Check first:** [Heat pipe (Wikipedia)](https://en.wikipedia.org/wiki/Heat_pipe) · [Marcus 1972, NASA CR-2018 (free)](https://ui.adsabs.harvard.edu/abs/1972ntrs.rept16303M/abstract)
  - **Then:** Grover et al. 1964 (#29)
  - **If it's wrong:** The sealed apartment needs another regulator.
- [ ] **D2 · A melting mass can pin a room’s temperature.** Phase-change materials soak up and release heat at a fixed melting point. Maria Telkes patented building systems using them in the 1960s, and a 1970s Dow Chemical study screened about 20,000 candidates. Her favorite, Glauber’s salt, melts near 32°C (90°F), so holding 68°F takes a different material.
  - **How sure:** Medium. A search on Oct. 5 agreed on Telkes and the Dow study. I haven’t confirmed which material melting near 20°C (68°F) the period would have used.
  - **Check first:** [Phase-change material (Wikipedia)](https://en.wikipedia.org/wiki/Phase-change_material)
  - **Then:** Zalba et al. 2003; Telkes 1980
  - **If it's wrong:** Use the heat pipe alone, or let the room sit warmer.
- [ ] **D3 · Your 68°F has a date.** On November 7, 1973, Nixon asked Americans to turn thermostats down at least 6 degrees for a national daytime average of 68°F.
  - **How sure:** High. The primary source is free.
  - **Check first:** [Nixon’s address (American Presidency Project)](https://www.presidency.ucsb.edu/documents/address-the-nation-about-policies-deal-with-the-energy-shortages)
  - **Then:** None needed
  - **If it's wrong:** The date anchor moves.

## The investigators' toolkit

- [ ] **T1 · What your investigators can’t use yet.** DNA fingerprinting arrived in 1985, US cellular service in October 1983 and civilian GPS in the 1990s. Desktop computers were rare in city offices before the IBM PC of 1981.
  - **How sure:** High. A search on Oct. 5 agreed on the DNA and cellular dates. The computer line is my judgment.
  - **Check first:** [Alec Jeffreys (Wikipedia)](https://en.wikipedia.org/wiki/Alec_Jeffreys) · [Ameritech Cellular (Wikipedia)](https://en.wikipedia.org/wiki/Ameritech_Cellular)
  - **Then:** Jeffreys et al. 1985
  - **If it's wrong:** A solve that uses any of these breaks the period.
