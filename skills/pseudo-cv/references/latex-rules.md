# LaTeX rules

## Filling the template
- **Start point:** `assets/resume-template.tex`. Replace every `<<PLACEHOLDER>>`.
- **Unused parts:** delete them, e.g. the LeetCode link if the user has none, or the Experience, Certifications or
  Achievements section if it would be empty. Remove the `%` guide comments too.
- **Never change:** the document class, packages, geometry, colours, fonts, `\titleformat`, `\titlespacing`,
  `\linespread` or `\setlist`. The layout is the product; only the content changes.
- **Section order:** Header → Summary → Technical Skills → Experience → Projects → Education → Certifications →
  Achievements. With no experience, remove the Experience section. Projects then follow Technical Skills directly.

## One-page budget
| Section | Budget |
|---|---|
| Summary | 2–3 lines with experience; 3–4 lines without; up to 5 lines if the page is underfilled |
| Technical Skills | 5–7 rows, each fitting on one line |
| Experience | ≤ 2 roles × 2–3 bullets |
| Projects | 2 or 3 projects × 3–5 bullets (see `project-selection.md`) |
| Education | Degree + 12th + 10th |
| Certifications | ≤ 4 items |
| Achievements | ≤ 4 items |
| Any bullet | ≤ 2 printed lines (~200 characters) |

The target is exactly one page, filled to the bottom (FILL 94–100%).
- **Over a page:** cut the least JD-relevant bullet first, then shorten long bullets.
- **Visible empty space at the bottom:** expand the summary first, then the project detail, then the skills or
  achievements (see SKILL.md, Step 7).
- **Either way:** never change fonts, margins or spacing. `scripts/check_one_page.py` measures both page count and
  fill.

## Bullets
**Formula:** action verb + what was built or done + tech stack + measurable result (only if the source states one).

- **With a stated number:** "Built a FastAPI inference service with Redis caching and Docker, cutting p95 latency
  from 800 ms to 120 ms."
- **No number available:** "Built a FastAPI inference service with Redis caching and Docker, deployed on AWS EC2
  with GitHub Actions CI."

**Good verbs:** Built, Designed, Engineered, Implemented, Deployed, Optimised, Automated, Integrated, Trained,
Led, Reduced, Scaled.

**Avoid:** "Worked on", "Helped with", "Responsible for", backstory, motivation and adjectives like "amazing" or
"robust".

## ATS
- Standard headings only: Summary, Technical Skills, Experience, Projects, Education, Certifications, Achievements.
- No tables, columns, icons or images.
- Use the JD's exact keyword spelling. Each true must-have keyword should appear at least once, naturally. Don't
  stuff keywords.

## Escaping user text
| Character | Write it as |
|---|---|
| `\` | `\textbackslash{}` |
| `&` | `\&` |
| `%` | `\%` |
| `$` | `\$` |
| `#` | `\#` |
| `_` | `\_` |
| `{` | `\{` |
| `}` | `\}` |
| `~` | `\textasciitilde{}` |
| `^` | `\textasciicircum{}` |

- Inside `\href{URL}` URLs, escape only `%` and `#`.
- Use `--` for date ranges, `\%` for percentages and `$\vert$` for separators.
- C++ and C# are written `C++` and `C\#`.

## Project heading styles
```latex
\textbf{Name -- Tagline} \hfill \href{URL}{GitHub}                          % own repo
\textbf{Name -- Tagline} \hfill \href{URL}{Live} $\vert$ \href{URL}{GitHub} % own repo + demo
\textbf{Name -- Tagline} \hfill \textit{Tech, Stack}                        % no link
```
