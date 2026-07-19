# The Librarian Pattern for Codex Projects

## Introduction

Every Codex task starts cold. Whether it's a fresh single task or a specialist inside a Lead-and-Specialists structure, it either reads the whole repository and its documentation from scratch, or it works from a partial and possibly stale picture of the project.

Neither option is cheap. A full re-read burns tokens and time on every single task, including the tenth task this week that asks a question the ninth task already answered. A partial picture creates a different problem: decisions that only make sense if you happened to read the right file, or happened to be in the conversation where something was settled.

This pattern gives one task a standing job: maintain a catalog of what is currently true in the project and where it lives, and answer other tasks' questions with short, sourced, dated reference slips instead of pointing them at everything.

The Lead-and-Specialists pattern solves who owns which code. The Librarian pattern solves how a task gets exactly the context it needs, no more and no less, without re-deriving it every time. The two patterns pair well together, but the Librarian pattern also works on its own, including inside a single-task project.

The shortest description of the pattern:

> One task maintains a catalog of the project's canonical facts and where they live. Other tasks query the catalog instead of re-reading everything. Every answer is short, sourced, and marked with when it was last verified. The catalog is a working reference that grows with the project, not an archive of everything that was ever written.

## Why this pattern works

1. **Smaller context per task.** A task that needs one fact gets one fact, not an invitation to read six files to find it.
2. **Staleness gets caught early.** The librarian is the one task whose job is noticing when the catalog no longer matches the repository, instead of every task silently trusting whatever it happened to read.
3. **One place to fix a wrong fact.** Correct the catalog entry once instead of correcting the same misunderstanding across five different task transcripts.
4. **Cheaper iteration.** Short, sourced answers cost less than full-file context every time, and they compound across a project with many tasks.
5. **Works alone or paired.** A single ongoing Codex task can be its own librarian and patron. A Lead-and-Specialists project can add a librarian so specialists query instead of scanning the full repository for context outside their owned paths.

## When not to use it

- the repository and its documentation are small enough to fit comfortably in one context window;
- the documentation changes every few minutes, so any catalog would be stale before it's used;
- this is a single short-lived task with no repeat visits expected;
- the project has no meaningful canonical facts yet because it's still purely exploratory.

Building a catalog for a project too small or too early to need one just adds a second thing to keep in sync for no benefit.

## The basic structure

```text
Repository changes (code, docs, decisions)
                     |
                     v
        Librarian updates the catalog
                     |
                     v
Patron task submits a question -----> Librarian checks the catalog
                                              |
                                              v
                                   Returns a reference slip:
                                   short answer, source, last verified
                                              |
                                              v
                              Patron continues its own work,
                              citing the slip instead of re-deriving it
```

The librarian does not do the patron's work. It answers questions and keeps the catalog honest. Patrons still read the specific files they're actively editing; the catalog just means they stop re-reading everything else to find their bearings.

---

# Single-Paste Handoff for a New Librarian Task

Copy everything between **BEGIN PROMPT** and **END PROMPT** into the Codex task you want to act as librarian for this project.

## BEGIN PROMPT

You are the Librarian for this project. Your job is to maintain a catalog of the project's current, canonical facts and where they live, and to answer other tasks' questions with short, sourced, dated reference slips instead of directing them to read everything yourself.

You are not the architect and you are not an integrator. Do not make design decisions, do not resolve architectural disagreements, and do not write application code beyond what maintaining the catalog requires. If a question you receive is actually a design decision that hasn't been made yet, say so and name who should decide it, rather than deciding it yourself.

## Core operating model

1. The **catalog** is the single index of canonical facts: what's true right now, and exactly where the source of truth lives.
2. The **archive** is everything canonical the catalog points to: architecture docs, decision records, schemas, contracts, and any other file the project treats as authoritative.
3. **Patrons** are other tasks, human or Codex, that query the catalog instead of re-reading the whole project.
4. A **reference slip** is your answer format: a short, direct answer, the source it came from, and the date you last verified that source still says this.
5. If the catalog doesn't have an answer, or the answer is unverified or contested, say so plainly. Do not guess, and do not synthesize a plausible-sounding answer from partial information.
6. Keep the catalog itself short. It is an index, not a copy of the underlying documents.

## First inspect the project

Before creating anything:

- inspect the repository layout, existing documentation, README files, architecture docs, and any decision records;
- identify what already functions as a canonical source of truth versus what is exploratory or outdated;
- check whether a catalog or index already exists under a different name, and if so, evaluate whether to adopt and extend it rather than create a duplicate;
- note where documentation contradicts itself or contradicts the code, and flag these rather than silently picking one.

## Decide whether this pattern fits

Evaluate whether the project has enough canonical, reusable facts to justify a catalog. If the project is too small, too early, or changing too fast for any index to stay current, say so and skip creating one. Recommend revisiting once the project has a stable architecture document or a first vertical slice, if this project also uses the Lead-and-Specialists pattern.

## Create the catalog

Create `docs/CATALOG.md` (or extend an existing equivalent) as a table or structured list. Each entry must include:

- **Topic**: the fact or concept, named plainly;
- **Answer**: one to three sentences, no more;
- **Source**: exact file path and section, or commit/decision record;
- **Last verified**: the date you confirmed the source still supports the answer;
- **Confidence**: settled, provisional, or contested.

Do not catalog anything you have not personally verified against its source. Do not catalog secrets, credentials, or anything that shouldn't be duplicated outside its original access-controlled location.

## Define the reference-slip format

Create `docs/coordination/REFERENCE_SLIPS.md` defining the format patrons should expect:

```markdown
## Question
[the question as asked]

## Answer
[one to three sentences]

## Source
[file path / section / decision record]

## Last verified
[date]

## Confidence
[settled / provisional / contested]

## If unanswered
[state plainly that the catalog does not cover this, and name who should resolve it]
```

Never pad a reference slip with unrequested context. The point of the pattern is that patrons get exactly what they asked for.

## Maintain the catalog

- Update the catalog whenever the archive changes, don't wait to be asked.
- When a patron's question reveals a gap or a contradiction, add or correct the catalog entry as part of answering.
- Periodically re-verify entries marked provisional or contested, and update their status.
- Prefer marking an entry stale or contested over deleting it silently. Deletions should be visible in the catalog's own history.

## Pairing with Lead-and-Specialists

If this project also uses the Lead-and-Specialists pattern:

- the lead remains the owner of architecture and contract decisions; the librarian catalogs those decisions but does not make them;
- specialists should query the librarian for context outside their owned paths instead of reading the full repository;
- coordination notes and PR descriptions are good source material for new catalog entries;
- the librarian should flag, but not resolve, any contradiction it finds between a specialist's coordination note and the existing catalog.

## Scope for this assignment

This assignment establishes and begins maintaining the catalog. Do not make architecture decisions. Do not resolve contested facts on your own judgment; mark them contested and name who should resolve them. Do not catalog information you have not verified against a real source in this repository.

## Verification

Before finishing:

- ensure every catalog entry has a real, checkable source;
- ensure no entry states as settled something that is actually contested or unverified;
- ensure the reference-slip format is documented and consistent;
- ensure no secrets or access-controlled information were copied into the catalog;
- inspect the final diff.

Finish with:

1. whether this project currently has enough canonical, reusable facts to justify a catalog, and why;
2. the catalog file created and its current entry count;
3. any contradictions found in existing documentation and how they were flagged;
4. any gaps you could not verify and who should resolve them;
5. the exact next step for a patron task to query the catalog.

## END PROMPT

---

# Advanced Implementation Guidance

The material below is optional. It's useful once the catalog is in active use across more than one task.

## 1. The catalog is an index, not a copy

The catalog should never contain the full text of a policy, a schema, or a design decision. It contains a short answer and a pointer. If a patron needs the full document, the catalog tells them exactly where it is; it doesn't reproduce it.

This keeps the catalog cheap to read in full and cheap to keep current. A copy has to be kept in sync with its source forever. A pointer just has to still point at the right place.

## 2. Two tiers: manual catalog versus indexed catalog

**Manual catalog.** A single `docs/CATALOG.md` file, hand-maintained, organized as a table. Works for most projects. No tooling required beyond the librarian task itself.

**Indexed catalog.** For larger projects, back the catalog with an actual retrieval system: embeddings and a vector search over the archive, or a search tool the librarian and patrons both call. The catalog file still exists as the canonical index of settled facts, but the librarian can also answer novel questions by searching the underlying archive directly rather than only checking existing entries.

Start manual. Move to indexed only when the manual catalog is large enough that a human or a task can no longer skim it in full, or when patrons are asking questions the catalog doesn't yet cover often enough that hand-adding every entry becomes the bottleneck.

## 3. Catalog entry format in practice

A good entry answers one question and cites one source:

```markdown
| Topic | Answer | Source | Last verified | Confidence |
|---|---|---|---|---|
| Auth token expiry | Access tokens expire after 15 minutes; refresh tokens after 30 days | docs/ARCHITECTURE.md#auth | 2026-07-12 | settled |
| Retry policy for provider webhooks | Exponential backoff, 3 attempts, then dead-letter queue | src/adapters/webhook-retry.ts | 2026-07-10 | settled |
| Whether soft-deleted records appear in reports | Unresolved, current code excludes them but no decision is documented | — | — | contested |
```

A bad entry tries to answer a question that's actually several questions, or cites "the codebase" instead of a specific file.

## 4. The reference-slip format in practice

A patron asks a specific question. The librarian answers with exactly that, not with everything adjacent to it:

```markdown
## Question
Does the payment retry logic apply to webhook failures or only outbound API calls?

## Answer
Webhook failures only. Outbound API calls to the payment provider have no automatic retry; a failed call surfaces immediately to the caller.

## Source
src/adapters/webhook-retry.ts, lines 12-40

## Last verified
2026-07-10

## Confidence
settled
```

If the librarian doesn't know:

```markdown
## Question
Does the payment retry logic apply to webhook failures or only outbound API calls?

## Answer
Not documented. The webhook retry code exists and is catalogued, but there's no equivalent for outbound calls, and no decision record explains whether that's intentional.

## Source
—

## Last verified
—

## Confidence
unresolved. Recommend the lead or the original author confirm intent.
```

Both are useful answers. Only one of them is a guess dressed up as a fact, and that's the one to avoid.

## 5. Staleness and verification rules

- Every entry carries a last-verified date. An entry with no date is not yet trustworthy.
- Re-verify an entry whenever a patron's question touches it, even if the answer doesn't change; update the date.
- Re-verify proactively after any merge that touched a file a catalog entry cites.
- An entry that hasn't been verified in a long time relative to how fast the project moves should be treated as provisional until re-checked, not assumed current.

## 6. What not to catalog

- secrets, credentials, tokens, or anything access-controlled;
- per-task scratch notes or work-in-progress reasoning that isn't a settled fact;
- anything that changes so often the entry would be stale within a day;
- opinions or preferences with no source, even if they sound reasonable.

If it isn't traceable to a real, checkable source in the project, it doesn't belong in the catalog.

## 7. Common failure modes

### Catalog drift

Symptoms: entries contradict the current code; patrons start double-checking the catalog against the source anyway, which defeats the purpose.

Correction: tie catalog updates to the same review gate as code changes, so the catalog can't silently fall behind.

### The librarian becomes a bottleneck

Symptoms: patrons wait on librarian responses for questions they could answer themselves in ten seconds by reading one clearly-named file.

Correction: the catalog should make itself skimmable directly. Patrons shouldn't need to ask the librarian for anything they could find by reading the catalog file themselves.

### Overcaching stale answers

Symptoms: the librarian gives the same answer it gave three weeks ago without checking whether the source changed.

Correction: make re-verification part of answering, not a separate task nobody gets to.

### Patrons bypass the catalog anyway

Symptoms: tasks keep re-reading the full repository out of habit or distrust, and the catalog goes unused.

Correction: usually a trust problem, not a process problem. Audit a sample of catalog entries against their sources. If they hold up, the fix is habit, not process. If they don't hold up, fix the accuracy first.

## 8. Sequential versus on-demand queries

The librarian doesn't run on a schedule. It responds to patron questions as they arrive and updates the catalog opportunistically when it notices drift. In a Lead-and-Specialists project, it's reasonable for the librarian to also do a pass after every integration, since that's exactly when the archive is most likely to have changed.

## 9. A reusable project checklist

Before relying on the catalog:

- [ ] `docs/CATALOG.md` exists and every entry has a real source.
- [ ] Every entry has a last-verified date.
- [ ] Contested or unresolved facts are marked as such, not guessed at.
- [ ] The reference-slip format is documented somewhere patrons can find it.
- [ ] No secrets or access-controlled information appear in the catalog.

Before trusting a specific catalog entry:

- [ ] The source still exists at the path cited.
- [ ] The source still says what the entry claims.
- [ ] The last-verified date is recent relative to how fast this part of the project changes.

## Final principle

The goal isn't to write everything down. It's to make sure the thing that's already true only has to be figured out once, and that anyone who needs it after that gets a short, sourced answer instead of a research project.

Keep the catalog smaller than the archive. Keep every answer traceable. Say "I don't know, and here's who should" as often as the project actually requires it.
