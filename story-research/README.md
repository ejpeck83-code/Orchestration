# Story research: infrastructural counterfactual mysteries

Research for a collection of science-fiction mysteries about ordinary technologies that history invented differently. Each story sits on a real engineering fork between 1880 and 1960. The mystery is set in 1962-82, and the missing object is never explained.

## What's here

| File | What it is |
|---|---|
| [`01-science-corpus.md`](01-science-corpus.md) | 158 sources with checked citations, organized as a spine for the whole series plus a section per story. Each story section has the historical fork, mechanisms the science supports, and traps to avoid |
| [`04-facts-to-check.md`](04-facts-to-check.md) | The 36 facts the stories lean on, with how sure I am about each, the cheapest way to check it, and what changes if it's wrong. Check these before you build on anything else |
| [`02-originality.md`](02-originality.md) | The comparable works, how close each one sits, a risk rating per story, and pitch comparisons |
| [`03-city.md`](03-city.md) | The setting pick (Lockport, New York), the chain from the fork to the city's growth, and 3 runners-up |
| [`corpus.csv`](corpus.csv) | The master list of sources. Open it in a spreadsheet and filter by story |
| [`corpus.bib`](corpus.bib) | The same list as BibTeX for Zotero or any reference manager |
| [`tools/build_corpus.py`](tools/build_corpus.py) | Rebuilds the BibTeX and the reading lists after you edit the CSV |
| [`print/premise-packet.pdf`](print/premise-packet.pdf) | This week's 15-page print packet: guides for Star and David, the 36 facts to check, and library requests. Rebuild it with `print/build.sh` |
| [`facts.csv`](facts.csv) and [`tools/build_facts.py`](tools/build_facts.py) | The facts list as a spreadsheet, and the script that turns it into `04-facts-to-check.md` and the packet's fact pages |

## The short version

**Science.** Your series engine already has a name in the research: infrastructure stays invisible until it breaks (Star 1999). Most of the 10 mysteries can resolve on real science that existed inside your window, like heat pipes, tritium dating of water, sound spectrographs and record linkage. Before you build on any of it, check the 36 facts in `04-facts-to-check.md`, starting with the 6 I'm least sure of.

**Originality.** The collection as a whole is original. Three seeds sit close to famous works and need changing or a deliberate nod: the elevator story (*The Intuitionist*), the clerk with two impossible databases (*The City & the City*), and the station that exists only in maintenance records ("A Subway Named Möbius").

**City.** Lockport, New York, population 20,876. Birdsill Holly invented district heating and reservoir-free hydrant systems there. The 1891 Niagara power commission considered pneumatic transmission 20 miles away. If that fork goes the other way, power can't travel far, industry clusters on the escarpment, and Lockport becomes the capital of district infrastructure.

## Updating the corpus

1. Add or edit a row in `corpus.csv`. The `section` column places it (A1-A5, B01-B10, C, D), and the `also` column cross-lists it under other stories.
2. Run `python3 story-research/tools/build_corpus.py`.
3. The script rewrites `corpus.bib` and the lists between the `<!-- papers:... -->` markers in `01-science-corpus.md`. Everything else in that file is left alone.

The facts list works the same way: edit `facts.csv`, run `python3 story-research/tools/build_facts.py`, then `story-research/print/build.sh` to reprint.

## How the sources were checked

Papers were verified against Crossref records for DOI, venue, volume and pages. Reports, web sources and primary documents were checked against the publisher or agency page. Books use standard catalog citations. The `verified_via` column says which check each entry got.

Those checks confirm that each source exists and is cited correctly. The notes are a separate matter. Only 1 source (Bottomley 2014) was read in full, and the notes on the rest come from Claude's knowledge of the work plus its abstract or record. Read the paper itself before a story depends on it.
