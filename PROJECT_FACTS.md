# Project substrate — the invented facts of the Cookbox project

**Purpose.** Everything in this file is fiction, and none of it may be cited. It exists because the
writing scaffold refers to concrete project facts in about twenty places across four chapters
("name the ONE feature that gets dropped", "name real story IDs", "state the actual sprint goal").
Fixing them here, once, is what keeps chapters 2 to 5 consistent with each other.

**Rule that governs this file:** *cite the concept, own the decision.* Nothing on this page gets a
citation. If a sentence in the report draws on something here, it is the report's own voice.

> **This is a draft substrate, not a verdict.** It is internally consistent and every dependency has
> been checked, so it can be written from as it stands. But 2.3 is where Creativity (15 %) is scored,
> and these are my inventions, not yours — read the ten stories first and change any that do not
> sound like something you would have written. Changing a *persona* or a *benefit clause* is free.
> Changing a *story* means re-checking the four dependency chains in §4 and the three refinement
> triggers in §7.

---

## 1. The product and the client

| | |
|---|---|
| **Product** | Cookbox, a mobile application for organising recipes |
| **Client** | An independent software studio of about 25 people, building Cookbox for its own account |
| **Platform** | iOS and Android only |
| **Target scale** | 50,000 registered users within twelve months of launch |
| **Commercial model** | Free at launch, no advertising. Monetisation is a deliberate later decision, so the first release earns nothing |
| **Product goal** | A cook can get a recipe into the app, find it again, and follow it while cooking |

The commercial model matters more than it looks: because the first release generates no revenue, the
budget is genuinely fixed. That is the concrete basis for the "cost is fixed" leg of the inverted
iron triangle in chapter 4 — it is a fact about this project, not a doctrine borrowed from Kelly.

## 2. Scope boundaries (for 2.1)

**In scope:** entering and storing a user's own recipes; retrieval; a cooking view; account-bound
storage; weekly planning; shopping lists; serving-size scaling; a small curated starter collection
shipped with the app.

**Explicitly out of scope** — state these as decisions, not omissions:

- no nutritional analysis and no dietary or medical advice
- no allergy-specific recipe curation
- no desktop or web version
- no grocery ordering or delivery integration
- no public recipe feed, following or messaging — Cookbox is a private collection, not a social network

> ⚠️ **Consistency check already run.** US-09 is about an internal *curated starter collection*, not
> about users publishing to each other. That is deliberate: an earlier draft had the moderator
> reviewing user-to-user shared recipes, which collides with the "no social network" exclusion. Do
> not reintroduce that framing.
>
> ⚠️ **Nutrition is out of scope**, which is why the progressive-elaboration example in §6 is *not*
> the tutor's own "categorising nutritional value" example. Using his would contradict 2.1.

## 3. Assumptions (for 1.4)

| | |
|---|---|
| **Scrum team** | 6 people: one Product Owner, one Scrum Master, four developers. Role labels only, no invented names |
| **Sprint length** | Two weeks |
| **Time frame** | First public release targeted six months after project start, i.e. twelve sprints |
| **Budget** | EUR 240,000 for the six-month period, fixed, with no revenue expected in that window |
| **Reporting** | The Product Owner is a senior business role in the studio, not a developer |

Team size sits under the Scrum Guide's "typically 10 or fewer people" (p. 5) — that is the one
citation the assumptions paragraph carries. **Do not also quote PMI's "three to nine".**

---

## 4. The ten user stories (for 2.3)

Nine distinct personas across ten stories. No story says "As a user".

| ID | Story |
|---|---|
| **US-01** | As a hobby cook, I want to enter my own recipes with their ingredients and steps, so that my handwritten collection is in one place. |
| **US-02** | As a busy parent, I want to search my saved recipes by ingredient, so that I can cook with what is already in the fridge. |
| **US-03** | As an elderly user, I want to read the cooking steps one at a time in large type, so that I can follow a recipe without my reading glasses. |
| **US-04** | As a registered user, I want my collection stored in my account and restored on a new phone, so that I do not lose it when I change device. |
| **US-05** | As a shift worker, I want to plan which recipes I will cook on which days, so that my cooking fits around an irregular roster. |
| **US-06** | As a busy parent, I want a shopping list generated from the recipes I have planned, so that I do not write the list out by hand. |
| **US-07** | As a beginner cook, I want to scale a recipe to a different number of servings, so that I do not have to recalculate the quantities myself. |
| **US-08** | As a privacy-conscious user, I want to delete my account together with everything I have uploaded, so that I can leave the service without a trace. |
| **US-09** | As a content moderator, I want to correct and approve the recipes in the curated starter collection, so that new users find usable content on first launch. |
| **US-10** | As an experienced cook, I want to import a recipe from a website link, so that I do not have to retype recipes I found online. |

**Persona spread:** hobby cook · busy parent (×2) · elderly user · registered user ·
shift worker · beginner cook · privacy-conscious user · **content moderator** (the non-end-user role
the tutor explicitly rewards) · experienced cook.

### Dependency chains — checked

These are what 3.2's dependency argument and 3.3's joint-ordering argument are built on. They also
satisfy the CRUD-completeness check from 2.3: every story that reads, transforms or deletes a recipe
has a corresponding create story.

```
US-01 (create) ──┬──▶ US-04  (cannot back up what cannot be created)
                 ├──▶ US-06  (cannot shop for what cannot be created)
                 ├──▶ US-07  (cannot scale what cannot be created)
                 └──▶ US-08  (cannot delete what cannot be created)

US-05 (plan) ─────────▶ US-06  (no list without a plan)
```

**The point to make from this in 3.2:** US-01 is ordered first *because four other stories depend on
it*, not because it carries the most user value — US-02 arguably does. That is dependency overriding
business value, concretely, in your own backlog.

---

## 5. Initial MoSCoW distribution (for 3.2)

Four / three / two / one. The table in `03_backlog_and_refinement.tex` has been rewritten to match.

| Order | ID | Band | Why |
|---|---|---|---|
| 1 | US-01 | Must | Foundation: every other story reads, transforms or deletes a recipe this one creates |
| 2 | US-02 | Must | Retrieval, not storage, is the problem the product exists to solve |
| 3 | US-03 | Must | The point of use is cooking; without a usable cooking view the app is tried once and abandoned |
| 4 | US-04 | Must | A lost hand-entered collection is not re-entered; retention depends on it |
| 5 | US-05 | Should | Valuable, but users can plan on paper and still adopt the product |
| 6 | US-06 | Should | Highest-value item after the must-haves, but blocked by US-05 and US-01 |
| 7 | US-07 | Should | Frequently requested; deferred within the band after the developers sized unit conversion well above the initial assumption |
| 8 | US-08 | Could | Placed here initially; promoted to must-have during refinement (§7) |
| 9 | US-09 | Could | Moderation is affordable manually at launch volumes; the tooling only pays off at scale |
| 10 | US-10 | Won't | Repeatedly requested, but parsing arbitrary recipe sites is disproportionately expensive for a first release |

> **Keep the justification column to one line per row.** Section 3.2 has 0.80 pages and the table
> must share it with six paragraphs of prose. Tables count toward the page limit.

Note how three rows do double duty: US-07's justification plants the cost-feedback trigger, US-08's
plants the legal trigger, and US-09's plants the feature that gets dropped in chapter 4.

---

## 6. The progressive-elaboration example (for 3.3)

**The coarse request:** during a user conversation, a participant asked for help *"using up what is
about to go off in my fridge"*.

It is a wish, not a story. It cannot be estimated, and it plausibly contains eight to ten stories —
recording what is in the household, tracking dates, matching those items against saved recipes,
notifying the user in time, and handling the near-miss cases. It enters the backlog as **one
high-level block below the ten stories** and is broken down over successive refinement sessions until
individual items are small, clear and estimable enough to be pulled into a sprint.

⚠️ It is deliberately **not** one of the ten, and deliberately **not** the tutor's own
"categorising nutritional value" example — nutrition is excluded in 2.1, so his example would
contradict your own scope section.

---

## 7. Refinement triggers (for 3.3)

Four concrete instances. Each names a story and a consequence — a generic trigger list scores
nothing.

1. **A legal obligation promotes an item.** A data-protection review during the first sprint
   establishes that account deletion is a legal requirement, not a convenience. **US-08 moves from
   Could-have to Must-have**, above three items previously ranked higher. This is also the cleanest
   illustration available that priority is set by the Product Owner but is not a matter of taste.
2. **Cost feedback demotes an item within its band.** US-07 looked inexpensive until the developers
   sized it: unit conversion across grams, millilitres, cups and indivisible items such as eggs is
   substantially larger than the story's one-line description suggested. **The PO moves it to last
   place among the should-haves** rather than dropping it.
3. **User feedback rewrites a story and removes a dependency.** Follow-up conversations showed that
   most participants already plan on paper and wanted only the list. **US-06 is reworded** to build a
   shopping list directly from selected recipes, which **removes its dependency on US-05** and drops
   US-05 down the order. One story changed, one dependency dissolved.
4. **Splitting.** The coarse fridge request in §6 is broken into smaller items across two sessions.

**Refinement cadence:** two one-hour sessions per two-week sprint. Derived, not asserted — see the
argument built in `03_backlog_and_refinement.tex`, 3.3 P6.

---

## 8. Sprint 1 (for 3.4)

| | |
|---|---|
| **Sprint goal** | A cook can put a recipe into Cookbox and find it again. |
| **Selected items** | US-01 and US-02 |
| **Deliberately not selected** | US-03 and US-04, although both are must-haves |
| **Rationale** | Two of the four must-haves in a two-week sprint for a team that has never worked together and has no velocity to plan against. The goal is a working end-to-end path, not maximum output |

The sprint backlog is the goal, the two selected items, **and** the plan for delivering them — the
tasks the developers decomposed them into. Say that explicitly; "not just a list" is the point.

---

## 9. Chapter 4 — the named feature per axis

Every axis must be played out on a *named* story. These assignments are already consistent with §5
and §7.

| Axis | Story to use | The concrete point |
|---|---|---|
| 1 · frozen spec vs. changing backlog | **US-06** | Under a sequential approach it would have been signed off months earlier *with* its dependency on US-05. In the backlog it was reworded after user feedback and the dependency disappeared — a change that a signed specification would have processed as a defect |
| 2 · planning horizon | **US-08** | Nothing in a six-month up-front plan would have anticipated the data-protection review that promoted it. The plan was reliable for about two sprints |
| 3 · who estimates | **US-07** | A project manager pricing "scale a recipe" from the one-line description would have priced it low. The four developers who would build it priced the unit conversion, and the estimate changed the order |
| 5 · inverted iron triangle | **US-09** | ⭐ The feature that gets dropped. Time (six months) and cost (EUR 240,000) are fixed, so scope flexes: moderation tooling is cut, the support team moderates the starter collection by hand for the first months, and US-01 to US-04 ship on the date |
| 6 · feedback and risk | **US-03** | The cooking view is the story most likely to be built wrong from a written description. At the sprint review a stakeholder sees it on a phone; under a sequential plan the first time anyone outside the team sees it is at acceptance, five months in |

---

## 10. Chapter 5 — what to reflect on

Own voice throughout. The material is already distributed across the chapters; chapter 5 judges it.

- **Achieved:** a scoped product, ten stories, a prioritised backlog, a planned first sprint.
  **Not achieved, by design:** no increment, no velocity, no multi-sprint history.
- **Difficulty worth naming honestly:** the initial ordering was wrong twice within one sprint —
  US-08 was under-prioritised because the PO treated a legal obligation as a feature, and US-07 was
  over-prioritised because nobody had sized it. Both were caught by refinement. That is an argument
  *for* the process, and admitting it is worth more than claiming the first backlog was correct.
- **Resources:** six people and EUR 240,000 fixed against a six-month date. The scope was the only
  variable left, which is why US-09 was cut rather than the date moved.
- **Done differently:** involve the developers in ordering the must-haves earlier — two of the three
  re-orderings came from information the developers already had.
