#!/usr/bin/env python3
"""Build the corpus outputs from corpus.csv.

corpus.csv is the single source of truth. This script:
  1. writes corpus.bib (BibTeX, for Zotero or any reference manager)
  2. refills the reading lists inside 01-science-corpus.md, between
     <!-- papers:SECTION --> and <!-- /papers:SECTION --> markers

Edit the CSV (add a row, fix a note), then run:
    python3 story-research/tools/build_corpus.py
No network access and no third-party packages needed.
"""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "corpus.csv"
BIB_PATH = ROOT / "corpus.bib"
MD_PATH = ROOT / "01-science-corpus.md"

# Story sections pull in "see also" entries tagged in the `also` column.
SECTION_TAGS = {
    "B01": "intersection",
    "B02": "number",
    "B03": "lift",
    "B04": "coldroom",
    "B05": "exchange",
    "B06": "meter",
    "B07": "lock",
    "B08": "hydrant",
    "B09": "crossing",
    "B10": "dial",
    "C": "toolkit",
    "D": "setting",
}

BIB_TYPES = {
    "article": "article",
    "book": "book",
    "chapter": "incollection",
    "report": "techreport",
    "conference": "inproceedings",
    "primary": "misc",
    "web": "misc",
}


def load_rows():
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def author_parts(authors):
    parts = [p.strip() for p in authors.split(";") if p.strip()]
    et_al = any(p.lower().startswith("et al") for p in parts)
    parts = [p for p in parts if not p.lower().startswith("et al")]
    return parts, et_al


def short_authors(authors):
    """'Lighthill, M. J.; Whitham, G. B.' -> 'Lighthill & Whitham'."""
    editor = ""
    m = re.search(r"\((eds?\.)\)\s*$", authors)
    if m:
        editor = f" ({m.group(1)})"
        authors = authors[: m.start()].strip()
    parts, et_al = author_parts(authors)
    names = []
    for p in parts:
        if "," in p:
            names.append(p.split(",")[0].strip())
        else:
            names.append(p.split(" (")[0].strip())
    if not names:
        return authors
    if et_al or len(names) > 2:
        label = f"{names[0]} et al."
    elif len(names) == 2:
        label = f"{names[0]} & {names[1]}"
    else:
        label = names[0]
    return label + editor


def link_for(row):
    links = []
    if row["doi"]:
        links.append(f"[doi:{row['doi']}](https://doi.org/{row['doi']})")
    if row["url"]:
        links.append(f"[link]({row['url']})")
    return " ".join(links)


def render_entry(row):
    who = short_authors(row["authors"])
    title = row["title"].rstrip(".")
    kind = row["type"]
    venue = row["venue"]
    vp = row["volume_pages"]
    if kind == "article":
        where = f"*{venue}*" + (f" {vp}" if vp else "")
    elif kind == "book":
        where = f"*{venue}* (book)"
    elif kind == "chapter":
        where = venue + (f", {vp}" if vp else "")
    elif kind in ("report", "conference"):
        where = f"*{venue}*" + (f" {vp}" if vp else "")
    else:
        where = f"*{venue}*"
    line = f"- **{who} ({row['year']}).** {title}. {where}."
    link = link_for(row)
    if link:
        line += f" {link}"
    line += f"  \n  {row['what_it_gives_you']}"
    return line


def render_section(rows, section):
    primary = [r for r in rows if r["section"] == section]
    lines = [render_entry(r) for r in primary]
    tag = SECTION_TAGS.get(section)
    if tag:
        extra = [r for r in rows if tag in r["also"].split(";") and r["section"] != section]
        if extra:
            refs = ", ".join(f"{short_authors(r['authors'])} ({r['year']})" for r in extra)
            lines.append("")
            lines.append(f"*Also useful here, listed in other sections:* {refs}.")
    return "\n".join(lines)


def fill_markdown(rows):
    text = MD_PATH.read_text(encoding="utf-8")
    pattern = re.compile(r"(<!-- papers:(\w+) -->)(.*?)(<!-- /papers:\2 -->)", re.S)
    seen = set()

    def repl(m):
        section = m.group(2)
        seen.add(section)
        body = render_section(rows, section)
        return f"{m.group(1)}\n{body}\n{m.group(4)}"

    new_text = pattern.sub(repl, text)
    used = {r["section"] for r in rows}
    missing = used - seen
    if missing:
        sys.exit(f"No markers in {MD_PATH.name} for sections: {sorted(missing)}")
    MD_PATH.write_text(new_text, encoding="utf-8")


def bib_escape(value):
    return value.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#").replace("_", r"\_")


def bib_authors(authors):
    editor = bool(re.search(r"\(eds?\.\)\s*$", authors))
    authors = re.sub(r"\s*\(eds?\.\)\s*$", "", authors)
    parts, et_al = author_parts(authors)
    out = []
    for p in parts:
        out.append(p if "," in p else "{" + p + "}")
    if et_al:
        out.append("others")
    return " and ".join(out), editor


def parse_volpages(vp):
    m = re.match(r"^(\d+)(?:\(([^)]+)\))?:(.+)$", vp)
    if m:
        return m.group(1), m.group(2), m.group(3)
    m = re.match(r"^(\d+)\(([^)]+)\)$", vp)
    if m:
        return m.group(1), m.group(2), None
    m = re.match(r"^pp\. (.+)$", vp)
    if m:
        return None, None, m.group(1)
    return None, None, None


def to_bibtex(row):
    kind = BIB_TYPES.get(row["type"], "misc")
    names, is_editor = bib_authors(row["authors"])
    fields = [("editor" if is_editor else "author", names),
              ("title", "{" + bib_escape(row["title"]) + "}"),
              ("year", row["year"])]
    venue = bib_escape(re.sub(r"^In ", "", row["venue"]))
    if kind == "article":
        fields.append(("journal", venue))
    elif kind == "book":
        fields.append(("publisher", venue))
    elif kind in ("incollection", "inproceedings"):
        fields.append(("booktitle", venue))
    elif kind == "techreport":
        fields.append(("institution", venue))
    else:
        fields.append(("howpublished", venue))
    volume, number, pages = parse_volpages(row["volume_pages"])
    if volume:
        fields.append(("volume", volume))
    if number:
        fields.append(("number", number))
    if pages:
        fields.append(("pages", pages.replace("-", "--")))
    if row["doi"]:
        fields.append(("doi", row["doi"]))
    if row["url"]:
        fields.append(("url", row["url"]))
    fields.append(("note", bib_escape(row["what_it_gives_you"])))
    body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields)
    return f"@{kind}{{{row['id']},\n{body}\n}}\n"


def main():
    rows = load_rows()
    ids = [r["id"] for r in rows]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        sys.exit(f"Duplicate ids in corpus.csv: {dupes}")
    BIB_PATH.write_text("\n".join(to_bibtex(r) for r in rows), encoding="utf-8")
    fill_markdown(rows)
    print(f"{len(rows)} entries -> {BIB_PATH.name}, {MD_PATH.name}")


if __name__ == "__main__":
    main()
