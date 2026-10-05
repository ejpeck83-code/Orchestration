#!/usr/bin/env python3
"""Build the facts checklist from facts.csv.

Writes 04-facts-to-check.md and refreshes the facts pages of the print packet
between the <!-- facts:... --> and <!-- facts-priority:... --> markers.

Run from anywhere: python3 story-research/tools/build_facts.py
"""
import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "facts.csv"
MD_PATH = ROOT / "04-facts-to-check.md"
PACKET_PATH = ROOT / "print" / "premise-packet.html"


def load():
    with open(CSV_PATH, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["links"] = []
        for part in r["check_first"].split(";;"):
            label, _, url = part.partition("|")
            if url.strip():
                r["links"].append((label.strip(), url.strip()))
    return rows


def sections(rows):
    out = []
    for r in rows:
        if not out or out[-1][0] != r["section"]:
            out.append((r["section"], []))
        out[-1][1].append(r)
    return out


def short_url(url, limit=46):
    s = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
    return s if len(s) <= limit else s.split("/")[0] + "/…"


def priority(rows):
    return [r for r in rows if r["confidence"] != "High"]


def render_md(rows):
    pri = priority(rows)
    fixed = [r for r in rows if r["corrected"] == "yes"]
    n_city = sum(1 for r in rows if r["id"].startswith("C"))
    lines = [
        "# Facts to check",
        "",
        f"The corpus is a reference shelf. These are the {len(rows)} facts the stories lean on: "
        f"{n_city} for the city, 2 to 4 per story and 1 for the investigators' toolkit. "
        "Check these and leave the rest on the shelf.",
        "",
        "Each fact has how sure I am, the cheapest way to check it (free sources first), the corpus "
        "source behind it, and what changes in the story if it's wrong. Numbers like #37 point to the "
        "reading order.",
        "",
        "This file is generated from `facts.csv`. Edit the CSV, then run "
        "`python3 story-research/tools/build_facts.py`.",
        "",
        "## How sure I am",
        "",
        "- **High:** widely documented. Most of these were also confirmed by a web search on October 5, 2026.",
        "- **Medium:** I believe it, but a detail could be off, or I couldn't confirm the key part.",
        "- **Low:** plausible on paper, and I know of no documented case.",
        "",
        f"## Start with these {len(pri)}",
        "",
    ]
    lines += [f"- **{r['id']}** · {r['title']} ({r['confidence']})" for r in pri]
    lines += [
        "",
        "## What changed while I built this",
        "",
        f"Checking turned up {len(fixed)} corrections. They're fixed in `01-science-corpus.md` too:",
        "",
    ]
    lines += [f"- **{r['id']}** · {r['title']}" for r in fixed]
    for name, items in sections(rows):
        lines += ["", f"## {name}", ""]
        for r in items:
            links = " · ".join(f"[{label}]({url})" for label, url in r["links"])
            tag = " *(corrected)*" if r["corrected"] == "yes" else ""
            lines += [
                f"- [ ] **{r['id']} · {r['title']}.**{tag} {r['detail']}",
                f"  - **How sure:** {r['confidence']}. {r['why']}",
                f"  - **Check first:** {links}",
                f"  - **Then:** {r['then']}",
                f"  - **If it's wrong:** {r['if_wrong']}",
            ]
    return "\n".join(lines) + "\n"


def esc(s):
    return html.escape(s, quote=False)


def render_print(rows):
    out = [
        '<section class="page facts">',
        '  <p class="kicker">Wednesday to Friday</p>',
        "  <h2>Facts to check</h2>",
        f'  <p class="facts-intro">The {len(rows)} facts your stories lean on, grouped by story. '
        "Tick the box when you’ve checked one. The links are clickable in "
        "<b>story-research/04-facts-to-check.md</b>.</p>",
    ]
    for name, items in sections(rows):
        out.append(f'  <h3 class="fsec">{esc(name)}</h3>')
        for r in items:
            conf = r["confidence"].lower()
            links = " · ".join(
                f"{esc(label)} <span class=\"url\">{esc(short_url(url))}</span>" for label, url in r["links"]
            )
            tag = ' <span class="fix">corrected</span>' if r["corrected"] == "yes" else ""
            out += [
                f'  <div class="fact conf-{conf}">',
                '    <div class="tick"></div>',
                '    <div class="fbody">',
                f'      <p class="ft"><span class="fid">{esc(r["id"])}</span>{esc(r["title"])}'
                f' <span class="conf">{esc(r["confidence"])}</span>{tag}</p>',
                f'      <p class="fd">{esc(r["detail"])}</p>',
                f'      <p class="fm"><b>How sure:</b> {esc(r["why"])}</p>',
                f'      <p class="fm"><b>Check first:</b> {links}. <b>Then:</b> {esc(r["then"])}.</p>',
                f'      <p class="fm"><b>If it’s wrong:</b> {esc(r["if_wrong"])}</p>',
                "    </div>",
                "  </div>",
            ]
    out.append("</section>")
    return "\n".join(out)


def render_priority(rows):
    pri = priority(rows)
    fixed = [r for r in rows if r["corrected"] == "yes"]
    out = [f"  <h3>Start with these {len(pri)}</h3>", '  <ul class="plist">']
    out += [
        f'    <li><span class="fid">{esc(r["id"])}</span>{esc(r["title"])} '
        f'<span class="conf conf-{r["confidence"].lower()}">{esc(r["confidence"])}</span></li>'
        for r in pri
    ]
    out += ["  </ul>", f"  <h3>{len(fixed)} corrections I made while checking</h3>", '  <ul class="plist">']
    out += [f'    <li><span class="fid">{esc(r["id"])}</span>{esc(r["title"])}</li>' for r in fixed]
    out.append("  </ul>")
    return "\n".join(out)


def inject(text, name, body):
    pattern = re.compile(rf"(<!-- {name}:start -->)(.*?)(<!-- {name}:end -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker <!-- {name}:start --> not found in {PACKET_PATH}")
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    rows = load()
    MD_PATH.write_text(render_md(rows))
    packet = PACKET_PATH.read_text()
    packet = inject(packet, "facts", render_print(rows))
    packet = inject(packet, "facts-priority", render_priority(rows))
    PACKET_PATH.write_text(packet)
    print(f"wrote {MD_PATH.name} and the facts pages of {PACKET_PATH.name} ({len(rows)} facts)")


if __name__ == "__main__":
    main()
