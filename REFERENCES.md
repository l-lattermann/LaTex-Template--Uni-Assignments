# Reference list — DLBCSAPM01 Project Report, Task 2 (Recipe App)

APA 7. Fourteen sources, matching `references.bib` and the second-pass keep-set of
`task/Literature review.md` (Section 20). This file is the human-readable copy — the authoritative
version for the compiled PDF is `references.bib`, rendered by `biblatex` with `style=apa`.

> **Verified.** `references.bib` was test-compiled with `biber` + `biblatex-apa`: it parses with no
> warnings, all fifteen entries render, and all four non-standard locator forms come out correctly —
> `(Project Management Institute, 2021, PMBOK Guide, Section 4.4.4)`, `(Kelly, 2019, ch. 1,
> pp. 5–10)`, `(Beck et al., 2001b, para. 2)` and plain page numbers. The `2001a` / `2001b` suffixes
> on the two Manifesto works are generated automatically. The entries below are the actual rendered
> output, not an idealised version of it.

---

## The list

Beck, K., Beedle, M., van Bennekum, A., Cockburn, A., Cunningham, W., Fowler, M., Grenning, J., Highsmith, J., Hunt, A., Jeffries, R., Kern, J., Marick, B., Martin, R. C., Mellor, S., Schwaber, K., Sutherland, J., & Thomas, D. (2001a). *Manifesto for agile software development*. https://agilemanifesto.org/

Beck, K., Beedle, M., van Bennekum, A., Cockburn, A., Cunningham, W., Fowler, M., Grenning, J., Highsmith, J., Hunt, A., Jeffries, R., Kern, J., Marick, B., Martin, R. C., Mellor, S., Schwaber, K., Sutherland, J., & Thomas, D. (2001b). *Principles behind the Agile Manifesto*. https://agilemanifesto.org/principles.html

Cohn, M. (2004). *User stories applied: For agile software development*. Addison-Wesley.

Heikkilä, V. T., Paasivaara, M., Lassenius, C., Damian, D., & Engblom, C. (2017). Managing the requirements flow from strategy to release in large-scale agile development: A case study at Ericsson. *Empirical Software Engineering, 22*(6), 2892–2936. https://doi.org/10.1007/s10664-016-9491-z

Kelly, A. (2019). *The art of agile product ownership: A guide for product managers, business analysts, and entrepreneurs*. Apress. https://doi.org/10.1007/978-1-4842-5168-3

Kerzner, H. (2022). *Project management: A systems approach to planning, scheduling, and controlling* (13th ed.). John Wiley & Sons.

Lucassen, G., Dalpiaz, F., van der Werf, J. M. E. M., & Brinkkemper, S. (2016). Improving agile requirements: The Quality User Story framework and tool. *Requirements Engineering, 21*(3), 383–403. https://doi.org/10.1007/s00766-016-0250-x

Mishra, A., & Alzoubi, Y. I. (2023). Structured software development versus agile software development: A comparative analysis. *International Journal of System Assurance Engineering and Management, 14*(4), 1504–1522. https://doi.org/10.1007/s13198-023-01958-5

Project Management Institute. (2017). *Agile practice guide*. Project Management Institute.

Project Management Institute. (2021). *The standard for project management and a guide to the project management body of knowledge (PMBOK guide)* (7th ed.). Project Management Institute.

Racheva, Z., Daneva, M., & Buglione, L. (2008). Supporting the dynamic reprioritization of requirements in agile development of software products. In *2008 Second International Workshop on Software Product Management (IWSPM'08)* (pp. 49–58). IEEE. https://doi.org/10.1109/IWSPM.2008.7

Schön, E.-M., Winter, D., Escalona, M. J., & Thomaschewski, J. (2017). Key challenges in agile requirements engineering. In H. Baumeister, H. Lichter, & M. Riebisch (Eds.), *Agile processes in software engineering and extreme programming (XP 2017)* (pp. 37–51). Springer. https://doi.org/10.1007/978-3-319-57633-6_3

Schwaber, K. (2004). *Agile project management with Scrum*. Microsoft Press.

Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide: The definitive guide to Scrum: The rules of the game*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf

Suryaatmaja, K., Wibisono, D., Ghazali, A., & Fitriati, R. (2020). Uncovering the failure of Agile framework implementation using SSM-based action research. *Palgrave Communications, 6*, Article 8. https://doi.org/10.1057/s41599-019-0384-9

---

## Where each source is used

Every source in the list must be cited in the text — a reference list containing an uncited work is
as much a defect as an uncited quotation. This table is the check.

| Source | `.bib` key | Chapters | Approx. citations |
|---|---|---|---|
| Schwaber & Sutherland (2020) | `scrumguide2020` | 1, 3.1, 3.2, 3.3, 3.4, 4 | ~14 |
| Cohn (2004) | `cohn2004` | 2.2, 3.2, 3.3, 4 | ~11 |
| PMI (2017) *Agile Practice Guide* | `pmi2017` | 3.1, 3.2, 3.3, 3.4, 4 | ~12 |
| Kerzner (2022) | `kerzner2022` | 2.1, 4, 5 | ~10 |
| PMI (2021) *PMBOK 7* | `pmbok2021` | 3.1, 3.2, 4, 5 | 6–8 |
| Kelly (2019) | `kelly2019` | 1, 3.1, 3.3, 4 | 6 |
| Lucassen et al. (2016) | `lucassen2016` | 2.2, 3.2, 5 | 4–5 |
| Racheva et al. (2008) | `racheva2008` | 3.2, 3.3 | 4–5 |
| Schön et al. (2017) | `schoen2017` | 2.2, 3.3 | 3–4 |
| Schwaber (2004) | `schwaber2004` | 3.2, 3.4 | 3 |
| Beck et al. (2001a/b) | `beck2001manifesto`, `beck2001principles` | 4, 5 | 3 |
| Mishra & Alzoubi (2023) | `mishra2023` | 4, 5 | 3 |
| Heikkilä et al. (2017) | `heikkila2017` | 3.3 | 1–2 |
| Suryaatmaja et al. (2020) | `suryaatmaja2020` | 3.1, 5 | 1–2 |

Total ≈ 60 in-text citations across 8 pages of text — roughly one every three to four lines, which
is already dense. Treat the per-source figures as ceilings.

---

## Four sources that are NOT in this list

Dropped in the second pass of the literature review. Do not re-add them without re-reading
Section 19 of `task/Literature review.md`.

| Source | Why not |
|---|---|
| Abrahamsson, Oza & Siponen (2010) | Pagination unrecoverable (author manuscript, no folios on any of 34 pages); restates what the task sheet already says; and its own abstract argues agile methods "fail to provide adequate project management support" |
| Behutiye et al. (2017) | Cohn (pp. 177–178) and Schwaber (p. 68) cover the same ground at higher tier with verified pages; the published page range cannot be mapped to the two quotes that mattered |
| Aizaz et al. (2021) | Kerzner owns scope creep; the paper's context is offshore vendor relationships, not a co-located team; four irreconcilable descriptions of its own sample |
| Racheva et al. (2010) | Three near-verbatim sentence pairs shared with the 2008 paper, and it contradicts the 2008 paper on when re-prioritisation may happen |

---

## Citation mechanics — the things that cost marks

**Every citation carries a locator.** This is the only explicitly named point-loser in the module.

**Four sources do not use plain page numbers.** Each is defensible under APA 7, but each must be
used consistently:

| Source | Locator form | Example |
|---|---|---|
| Kelly (2019) | chapter + **printed** page range | `(Kelly, 2019, ch. 1, pp. 5–10)` |
| PMI (2021) PMBOK 7 | section number, **naming the part** | `(Project Management Institute, 2021, PMBOK Guide, Section 4.4.4)` |
| Beck et al. (2001a/b) | paragraph number + a footnote | `(Beck et al., 2001b, para. 10)` |
| Racheva et al. (2008) | ⚠️ **derived, approximate** — declared in a footnote | `(Racheva et al., 2008, p. 53)` |

**Racheva et al. (2008) — NOT resolved; re-checked 2026-08-15.** An earlier version of this note
claimed the file was the IEEE-stamped camera-ready carrying the proceedings footer. That was wrong:
the file is the **authors' Word camera-ready** (metadata `RE-2008_Racheva-Daneva-camera-ready_final.doc`,
Distiller 7.0.5, 2008-08-08), and there is no proceedings footer on any page — no "IWSPM", no
"$25.00", no "978-0-7695" anywhere in the nine pages. The only open-access copy (UTwente) is the
same file. The first printed page is **49** (dblp and Crossref agree), but **the arithmetic does not
close**: the published range 49–58 is ten pages and the file has nine. Either the proceedings pad
with a trailing blank, or IEEE's typesetting pass adds the footer bar and reflows to ten pages — in
which case two of the three citations shift one page later. No folio-bearing copy is obtainable.

> **Working assumption: printed page = PDF page + 48.** Locations under that assumption: topic
> sentence **p. 52** · "informal and subjective" **p. 53** · client-vs-developer dependency **p. 55** ·
> prerequisite stories **p. 55** · the four method-selection criteria **p. 56**. A footnote at the
> first Racheva citation in `03_backlog_and_refinement.tex` declares these as approximate — that
> declaration is what protects the page-number criterion here, not the numbers themselves.
> Not used, recorded so they are not reintroduced: the MoSCoW definition **p. 52** (traces to an
> Oracle white paper) and the Wiegers "attractiveness" line **p. 53** (its next sentence proposes the
> risk-adjusted value/cost ratio the report rejects).

**The one that still needs attention:**

1. **PMBOK 7** — the volume binds *two* separately numbered documents, and **both** have a §3.1,
   §3.2, §3.3, §3.4 and §3.7. A locator that does not name the part is ambiguous, and an examiner who
   looks up the wrong one concludes the quote is fabricated. Both citations in the report currently
   name the part correctly. Note also that the available copy is a reflowed ebook with no folios, so
   printed page numbers cannot be added to this source without another copy — cite by section only.

*(A former warning about two unverified Cohn pages around pp. 137–141 has been removed: no Cohn
citation in the report falls in that range. The locators actually used are 4, 21, 78, 81, 98, 100,
148, 167 and 173, and all nine were verified against the source on 2026-08-15.)*

**Two footnotes to write:**

- *Kerzner edition.* The task sheet lists Kerzner (2009, 10th ed.); the edition read and cited is the
  13th (2022). One line noting the substitution is honest, costless, and protects the page-number
  criterion.
- *Manifesto locators.* Wording is in `sections/05_reflection_and_conclusion.tex`. Explaining why this
  one source legitimately carries no page number turns a potential defect into visible source care.

**One APA detail that is easy to get wrong:** the two Manifesto works share seventeen authors and a
year, so they need the **2001a / 2001b** suffixes, and **all seventeen authors must be listed in both
entries** — APA's "…" form applies only from twenty-one authors upwards. `biblatex-apa` adds the
year suffix automatically; the author lists are already complete in `references.bib`.
