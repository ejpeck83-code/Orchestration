# The Lead-and-Specialists Pattern for Codex Projects

## Introduction

Codex tasks inside one project can be organized much like a small development team:

- one task acts as the **lead architect and integrator**;
- other tasks act as **specialists**, each responsible for a coherent developmental area;
- Git branches, worktrees, documentation, tests, and pull requests provide the coordination system.

This comparison is useful, but it has one important limit: separate Codex tasks do not automatically share their full conversation history or decisions. They are not coworkers with a common memory. Their reliable shared context is the repository.

The repository therefore needs to carry the information that a human team would normally retain through meetings and ongoing conversation:

- product requirements;
- architecture decisions;
- shared types and interfaces;
- coding and safety rules;
- task ownership;
- tests and acceptance criteria;
- coordination notes;
- commits and pull requests.

The shortest description of the pattern is:

> One lead task defines the system and integrates it. Specialist tasks implement bounded capabilities in isolated worktrees. Documentation and code are their shared context. Specialists request shared changes; the lead controls them. Every capability returns through a tested pull request.

## Why this pattern works

The lead-and-specialists pattern is effective when a project contains several capabilities that can be separated behind stable interfaces. Examples include:

- retailer integrations, backend processing, and frontend experience;
- authentication, billing, and application features;
- data collection, transformation, analysis, and reporting;
- API services, administrative tools, and customer-facing interfaces;
- platform-specific modules inside a larger application.

It provides several advantages:

1. **Smaller working contexts.** Each specialist can focus on one problem without carrying the entire project conversation.
2. **Reduced file collisions.** Worktrees and explicit file ownership keep tasks from editing the same files simultaneously.
3. **Clearer review.** A specialist branch represents one coherent capability that the lead can inspect and test.
4. **Stable architecture.** Shared contracts remain under one owner instead of being independently redesigned by every task.
5. **Recoverable progress.** Decisions and implementation live in Git and documentation instead of disappearing inside a long conversation.

## When not to use it

One Codex task is usually better when:

- the project is small;
- most work touches the same few files;
- the architecture is changing every hour;
- the work cannot be separated into coherent capabilities;
- coordinating branches would take longer than implementing the change;
- the project is still at the exploratory prototype stage.

Adding more tasks does not automatically make development faster. The pattern works only when the boundaries are real.

## The basic structure

```text
Lead establishes requirements and architecture
                     |
                     v
Lead builds the foundation and one vertical slice
                     |
                     v
Specialist A works in an isolated worktree
                     |
                     v
Lead reviews, tests, and integrates A
                     |
                     v
Specialist B starts from the updated main branch
                     |
                     v
Lead reviews, tests, and integrates B
                     |
                     v
Specialist C starts from the updated main branch
                     |
                     v
Lead performs final integration and release work
```

The specialists should initially be introduced sequentially. Parallel work becomes appropriate after the shared contracts are stable and two assignments genuinely do not depend on one another.

---

# Single-Paste Handoff for a New Codex Project

Copy everything between **BEGIN PROMPT** and **END PROMPT** into the first Codex task attached to a new or existing project repository.

## BEGIN PROMPT

You are the Lead Architect and Integrator for this project. Establish a repository-based development structure in which one persistent lead task coordinates a small number of bounded specialist tasks. Do not create a swarm of tasks and do not begin broad feature implementation until the project structure, shared contracts, and first vertical-slice plan are clear.

Your purpose in this assignment is to inspect the project, formalize its development structure, and prepare a reliable Codex handoff system. If the repository already contains code or documentation, preserve it and adapt the structure to what exists. Do not overwrite user work or assume an empty repository.

## Core operating model

Use this model:

1. One **Lead Architect/Integrator task** owns requirements, architecture, shared contracts, repository conventions, schema and migrations when applicable, cross-cutting security/configuration, integration reviews, full-system tests, and releases.
2. A small number of **specialist tasks** each own one coherent developmental capability.
3. Each specialist receives its own Git branch and worktree.
4. The repository—not task conversation history—is the shared source of truth.
5. Specialists may read the full repository but may write only their assigned paths.
6. Specialists must not redesign shared contracts without lead approval.
7. Every specialist returns work through a reviewed, tested pull request or equivalent branch review.
8. Introduce specialists sequentially unless two areas are demonstrably independent and the shared architecture is already stable.

## First inspect the project

Before changing files:

- inspect Git status, branches, repository layout, existing documentation, package manifests, tests, CI, and deployment configuration;
- locate and read every existing `AGENTS.md` or equivalent instruction file;
- identify user changes and preserve them;
- determine the product purpose, current milestone, technical stack, and major architectural boundaries from repository evidence;
- distinguish established facts from assumptions;
- do not install dependencies or make unrelated implementation changes merely to create this structure.

## Decide whether this pattern fits

Evaluate whether the project is large and separable enough to benefit from multiple tasks. If it is not, document why one lead task is more appropriate and create only the lightweight documentation that remains useful.

If the pattern does fit, propose between two and four specialist areas. Divide by complete vertical capability, not by file type or programming layer.

Good specialist boundary:

> Own the payment-provider capability, including provider adapter, webhook handling, provider-specific tests, operational documentation, and stable outputs consumed by the application.

Bad specialist boundaries:

- one task writes buttons;
- another writes API routes used only by those buttons;
- another writes database inserts for those routes;
- another writes tests for code owned by the first three tasks.

Prefer the smallest number of specialists that creates meaningful independence.

## Create or update the project coordination files

Create the following only where they do not already have an authoritative equivalent. Merge with existing documentation instead of creating contradictory duplicates.

### Root `AGENTS.md`

It must define:

- project mission and scope boundaries;
- required documents to read before changing code;
- lead-owned shared contracts;
- coding, testing, security, privacy, and secret-handling rules;
- Git and worktree rules;
- external-content and external-service safety rules when applicable;
- file ownership policy;
- completion-report requirements;
- prohibition against claiming completion with failing tests.

### `docs/PRODUCT_BRIEF.md`

Capture:

- product statement;
- target users;
- core user jobs and workflows;
- included scope;
- explicit exclusions;
- success measures;
- later milestones that must not leak into the current build.

Do not invent product requirements unsupported by the repository. Mark unresolved items clearly.

### `docs/ARCHITECTURE.md`

Capture:

- system context and module boundaries;
- dependency direction;
- canonical domain concepts and stable contracts;
- persistence and migration ownership if relevant;
- integrations and adapter boundaries;
- security and trust boundaries;
- observability and failure behavior;
- architectural decisions that specialists must not change independently.

### `docs/BUILD_PLAN.md`

Define:

- the lead-owned foundation milestone;
- the first complete vertical slice;
- specialist introduction order;
- one branch and worktree name per specialist;
- exact owned and protected file paths;
- deliverables and acceptance gates;
- lead integration work after every specialist;
- final hardening and release milestone.

### `docs/ACCEPTANCE_AND_TESTS.md`

Define:

- project-wide acceptance criteria;
- unit, integration, contract, browser/UI, accessibility, security, and manual tests as applicable;
- deterministic fixture or fake-service rules;
- degraded and failure-mode testing;
- definition of done for the lead and specialists.

### `docs/coordination/README.md`

Define the coordination-note format. Every specialist note must include:

- branch and starting commit;
- capability owned;
- files changed;
- migrations or configuration changes;
- tests and exact results;
- known limitations;
- requests for lead-owned contract changes;
- final commit SHA and pull-request reference.

### Pull-request template

Create or update a pull-request template requiring:

- scope and user-visible behavior;
- ownership confirmation;
- test evidence;
- screenshots for user-visible work;
- migrations and environment changes;
- security and data-access considerations;
- known limitations;
- rollback instructions.

## Define lead ownership

Unless the existing architecture requires a different arrangement, the lead owns:

- product and architecture documents;
- canonical domain types and validation schemas;
- public interfaces between modules;
- database schema and migrations;
- authentication and authorization architecture;
- cross-cutting configuration;
- deployment and CI architecture;
- shared business rules;
- final integration and release decisions.

The lead should create stable extension points before delegating work.

## Define specialist ownership

For every proposed specialist, produce:

- task name and purpose;
- prerequisite milestone or tag;
- branch name;
- worktree path;
- exact owned paths;
- protected paths;
- required behavior;
- required tests and documentation;
- completion report;
- explicit instruction not to merge, rebase, or alter shared contracts without authorization.

If a specialist needs a shared-contract change, it must document the smallest requested change in its coordination note. It should continue with safe capability-local work where possible. The lead reviews and implements accepted shared changes.

## Build one vertical slice before specialization

Define the smallest end-to-end path that proves the project architecture. It should cross the important layers of the application and produce visible or testable behavior.

Examples:

- request -> validation -> business logic -> persistence -> API response -> user interface;
- source ingestion -> normalization -> storage -> query -> report;
- user action -> authorization -> state change -> confirmation -> audit record.

The lead should implement or supervise this vertical slice before specialist tasks begin. The slice establishes patterns for error handling, testing, persistence, configuration, and UI behavior that specialists can follow.

## Produce reusable single-paste prompts

Create a `docs/handoff-prompts/` directory containing:

1. `01-LEAD-FOUNDATION.md`
2. one single-paste prompt for each proposed specialist;
3. one lead review/integration prompt after each specialist;
4. `90-LEAD-RELEASE.md` for final hardening and release.

Every specialist prompt must state the starting point, branch/worktree, owned paths, protected paths, deliverables, required tests, safety limits, and handoff format.

Every integration prompt must require the lead to:

- inspect the complete diff rather than trusting the specialist summary;
- enforce file ownership;
- decide each coordination request explicitly;
- review security and failure behavior;
- run specialist and full-system tests;
- fix integration defects or return focused work;
- merge only after acceptance criteria pass;
- record the merge commit and updated milestone/tag.

## Produce the exact user walkthrough

Create `docs/CODEX_WORKFLOW.md` with a precise sequence explaining:

1. which Codex task to open first;
2. which prompt to paste;
3. when the foundation and vertical slice are considered complete;
4. when and how to create each worktree;
5. which specialist task to open against each worktree;
6. what the user should inspect before returning to the lead;
7. which integration prompt to paste into the lead task;
8. when to merge and tag;
9. when it is safe to remove a worktree;
10. how to proceed to the next specialist from updated `main`;
11. how to perform final hardening and release.

Include concrete Git commands adapted to the actual repository. Never use destructive Git commands. Do not remove a worktree until its branch is pushed, reviewed, merged, and clean.

## Git workflow

Prefer this shape unless the project already has an established alternative:

```text
main
├── feature/lead-foundation
├── feature/<specialist-capability-a>
├── feature/<specialist-capability-b>
└── feature/<specialist-capability-c>
```

Use protected `main`, pull requests, green CI, and no force-push. Recommend sequential worktree creation from current `main` after the preceding milestone is integrated.

## Scope for this assignment

This assignment establishes the development system. Do not start all specialist implementations. Do not spawn tasks automatically. Do not broaden the product. Do not rewrite working architecture without evidence.

You may implement only minimal repository scaffolding necessary to make the coordination system coherent. If the user explicitly asked you to build the foundation and vertical slice as part of the same assignment, plan and execute that separately after the coordination documents are approved or internally consistent.

## Verification

Before finishing:

- ensure all paths and commands match the actual repository;
- ensure no prompt contradicts `AGENTS.md`;
- ensure every specialist has mutually understandable ownership boundaries;
- ensure every specialist has an integration gate;
- ensure the first vertical slice precedes specialist work;
- ensure documentation names unresolved assumptions;
- ensure no secrets or private data were added;
- inspect the final diff.

Finish with:

1. whether the multi-task pattern fits this project and why;
2. the proposed lead and specialist structure;
3. files created or changed;
4. the vertical slice definition;
5. the exact first prompt/task the user should run next;
6. unresolved decisions or constraints;
7. Git status and commit information if changes were committed.

## END PROMPT

---

# Advanced Implementation Guidance

The material below is optional. It is useful when the person operating the project is comfortable with Git, software architecture, testing, and integration workflows.

## 1. Think of tasks as contexts, not people

The team-member analogy is helpful for dividing responsibility, but a Codex task is more accurately an isolated reasoning context attached to a filesystem and Git state.

This leads to several design rules:

- Important decisions must be written down.
- A specialist prompt must be self-contained.
- A branch must be reviewable without reading its task transcript.
- Tests must express behavior that future tasks can verify.
- Integration should depend on diffs and evidence, not conversational trust.

The repository becomes the project’s institutional memory.

## 2. Divide work by vertical capability

A good specialist assignment has meaningful internal cohesion and a small external interface.

Good examples:

- an external-service adapter plus normalization, fixtures, contract tests, and source documentation;
- a reporting feature from query service through rendered report and browser test;
- an authentication capability including provider integration, session handling, authorization tests, and operations documentation;
- an administrative workflow including API behavior, UI, auditing, and tests.

Weak examples:

- “write all database code” when every feature needs to change it;
- “write all tests” for code being changed simultaneously elsewhere;
- “build the frontend” when its required query contracts do not exist;
- “create components” without owning a user-visible workflow.

A useful test is:

> Can this specialist finish, test, document, and demonstrate a meaningful capability while changing very few shared files?

If the answer is no, the boundary should be reconsidered.

## 3. Establish contracts before concurrency

Parallelism is safest after the lead has stabilized:

- domain terminology;
- shared types and validation;
- database ownership;
- module boundaries;
- adapter interfaces;
- error/result types;
- authentication expectations;
- testing conventions;
- configuration patterns.

Without those contracts, parallel specialists often create incompatible assumptions that the lead must later reconcile.

That is why the first vertical slice matters. It is executable architecture documentation.

## 4. Use worktrees to isolate filesystems

A branch isolates history, but a worktree also gives each task its own checked-out filesystem.

Generic setup:

```bash
git switch main
git pull --ff-only
git worktree add ../project-capability-a -b feature/capability-a main
git worktree add ../project-capability-b -b feature/capability-b main
```

Verify:

```bash
git worktree list
git -C ../project-capability-a branch --show-current
git -C ../project-capability-a status
```

After a branch is pushed, reviewed, merged, and clean:

```bash
git worktree remove ../project-capability-a
git branch -d feature/capability-a
```

Do not delete a worktree merely because a specialist says it is finished. Verify its status and remote branch first.

## 5. Make file ownership explicit

An ownership table is one of the strongest collision-prevention tools.

Example:

| Role | May modify | Must not modify |
|---|---|---|
| Lead | Shared types, schema, CI, architecture, integration | Unrelated user work |
| Integration specialist | `src/adapters/provider-a/**`, related fixtures/tests | Schema, shared interfaces, UI |
| Workflow specialist | `src/features/workflow/**`, related API/UI/tests | Provider adapters, auth architecture |
| Experience specialist | Owned pages/components/UI tests | Schema, ingestion, shared business rules |

Ownership does not prevent reading. Specialists should inspect the shared code they consume. It prevents unilateral writes across high-conflict boundaries.

## 6. Use coordination notes instead of cross-task assumptions

A specialist coordination note can use this template:

```markdown
# Coordination Note — feature/capability-a

## Starting point
- Base commit:
- Branch:
- Worktree:

## Completed capability
-

## Files changed
-

## Tests
- Command:
- Result:

## Configuration or migrations
-

## Lead-owned change requests
1. Requested contract change:
   Reason:
   Smallest proposed shape:
   Compatibility impact:

## Limitations
-

## Handoff
- Final commit:
- Pull request:
```

This makes the specialist’s needs reviewable without requiring one task to reproduce another task’s entire conversation.

## 7. Use an integration gate after every specialist

The lead should not treat a green specialist test suite as sufficient. Integration review should cover:

- complete diff and ownership compliance;
- shared-contract changes;
- migrations and configuration;
- security and trust boundaries;
- error and degraded behavior;
- documentation accuracy;
- specialist tests;
- full project tests;
- end-to-end behavior;
- rollback and operational impact.

Generic integration prompt:

```text
Review and integrate the specialist branch.

1. Inspect the complete diff; do not rely only on its summary.
2. Verify that it changed only owned files.
3. Read its coordination note.
4. Decide every requested shared-contract change explicitly.
5. Review security, configuration, migrations, and failure behavior.
6. Run specialist tests and the full project suite.
7. Exercise the combined application end to end.
8. Fix integration defects or return a focused follow-up assignment.
9. Merge only after all acceptance criteria pass.
10. Record test evidence, limitations, merge commit, and next milestone.
```

## 8. Sequential versus parallel specialists

Use sequential specialists when:

- later work depends on earlier data contracts;
- the schema is still changing;
- the first implementation establishes patterns others must follow;
- several specialists would touch shared files;
- the lead wants a clean review point after each capability.

Parallel specialists are reasonable when:

- both start from the same stable tagged foundation;
- their owned paths do not overlap;
- they consume stable interfaces;
- neither depends on the other’s behavior;
- integration tests can be added without contract redesign.

Even when specialists run in parallel, integrate them one at a time and rerun the full suite after each merge.

## 9. Keep the lead task persistent

The same lead task should usually remain active throughout the project because it carries useful architectural context. Its authoritative decisions must still be written into the repository.

The lead should:

- maintain architecture and decision records;
- review every specialist diff;
- implement accepted shared-contract changes;
- run full-system tests;
- update milestone tags;
- keep documentation synchronized;
- prepare releases.

The lead should not simply rewrite specialist code. When possible, it should return focused defects to the owning specialist or fix only the integration boundary.

## 10. Prefer milestone tags and known starting points

Specialist prompts should not say merely “start from the latest code.” They should name a branch, commit, or milestone tag.

Example:

```text
Starting point: main at tag m1-foundation-slice or later
Branch: feature/provider-integrations
Worktree: ../project-provider-integrations
```

This makes stale worktrees and accidental dependency omissions easier to detect.

## 11. Common failure modes

### Too many specialists

Symptoms:

- every change requires several branches;
- specialists repeatedly request access to the same files;
- the lead spends more time resolving conflicts than reviewing capabilities.

Correction: combine adjacent responsibilities into fewer vertical areas.

### Specialists redesign shared architecture

Symptoms:

- incompatible data types;
- duplicate service abstractions;
- multiple migration strategies;
- overlapping configuration systems.

Correction: return shared contracts to lead ownership and require coordination notes.

### Conversation-only decisions

Symptoms:

- a branch makes sense only after reading a long transcript;
- another task repeats already-settled questions;
- documentation contradicts implementation.

Correction: update architecture, decisions, and tests before more delegation.

### Premature parallelism

Symptoms:

- all specialists start from an unstable scaffold;
- each invents different error handling and test patterns;
- merging the first branch invalidates the others.

Correction: complete and tag the first vertical slice before restarting specialists from current `main`.

### “Green” specialist, broken product

Symptoms:

- unit tests pass in isolation;
- the combined application does not build or the workflow fails end to end.

Correction: make lead integration gates and full-system tests mandatory.

## 12. A reusable project checklist

Before specialists begin:

- [ ] Product scope and exclusions are written.
- [ ] Architecture and shared contracts are written or implemented.
- [ ] Root `AGENTS.md` governs all tasks.
- [ ] The lead owns schema and cross-cutting contracts.
- [ ] One end-to-end vertical slice works.
- [ ] CI and test commands are established.
- [ ] Specialist boundaries are vertical and non-overlapping.
- [ ] Every specialist has owned and protected paths.
- [ ] Every specialist has a single-paste prompt.
- [ ] Every specialist has a lead integration prompt.
- [ ] Worktree branches start from named milestones.

Before merging a specialist:

- [ ] Full diff reviewed.
- [ ] Ownership respected.
- [ ] Coordination requests decided.
- [ ] Migrations/configuration understood.
- [ ] Specialist tests pass.
- [ ] Full project tests pass.
- [ ] Security and failure behavior reviewed.
- [ ] Documentation is accurate.
- [ ] User-visible behavior is demonstrated where applicable.
- [ ] Rollback or recovery is understood.

Before release:

- [ ] All integrated requirements map to code and tests.
- [ ] Explicit exclusions remain excluded.
- [ ] Fresh setup/migration works.
- [ ] Degraded dependencies are tested.
- [ ] Secrets and production data are absent from Git.
- [ ] Deployment and rollback are documented.
- [ ] Final branch and release tags are recorded.

## Final principle

The goal is not to imitate a large organization. The goal is to give each Codex task enough independence to make progress while preserving one coherent system.

Use the fewest tasks that create clean capability boundaries, put all durable knowledge in the repository, and make the lead responsible for proving that the parts work together.
