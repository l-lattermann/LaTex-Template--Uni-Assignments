# LaTeX University Paper Template

This repository contains my personal **LaTeX template** for university papers and written
assignments at IU International University of Applied Sciences. It is designed for clean formatting,
academic readability, and easy reuse across modules.

The template is mainly for my own use, but it is public so others can benefit from it as well.
You are welcome to **clone, reuse, or adapt** it for your own studies or reports.

> ⚙️ The template is updated now and then.

## Features

- DIN A4, single-sided, 2 cm margins, centred page numbers in the footer
- Arial 11 pt (Helvetica substitute), justified text, 1.5 line spacing
- APA references via `biblatex` + `biber`, configured for locator-bearing citations
- Three heading levels with matching table-of-contents styling
- Ready-made title page, front matter (contents, list of tables/figures, abbreviations) and
  reference list

## Usage

```bash
git clone https://github.com/l-lattermann/LaTex-Template--Uni-Assignments.git
cd LaTex-Template--Uni-Assignments
cp template.tex my-assignment.tex
latexmk -pdf my-assignment.tex
```

Then fill in the `<PLACEHOLDERS>` on the title page, put your chapters in `sections/` and your
sources in `references.bib`.

`.latexmkrc` sends all intermediates to `build/`. Run `latexmk -C` to clean up.

**Requires** a TeX distribution with `biber` (TeX Live or MacTeX).

## What is not in this repository

`.gitignore` deliberately excludes everything belonging to a specific assignment: `sections/`,
`references.bib`, `literature/`, compiled PDFs and submission files. This repository holds the
template, not the papers written with it.
