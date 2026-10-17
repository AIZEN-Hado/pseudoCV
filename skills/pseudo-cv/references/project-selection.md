# Project selection

## How many
| User's experience | Projects |
|---|---|
| 2 or more solid roles or internships | 2 |
| 1 role | 3 if it fits on one page, otherwise 2 |
| None | 3, plus a fuller summary and an Achievements section |

## Ready-now resume
Use only the user's real projects (resume projects and their own repos), ordered by JD relevance. If they
have fewer real projects than the slots, use what they have; don't add reference repos or ideas here.

## Target resume: which ones (in priority order)
1. **The user's own High-relevance repos or resume projects.** Keep them. They're real, linkable and defensible.
2. **Strong existing reference repos related to the JD.** Use these when the user's own projects don't cover the
   JD's must-haves. They are well-known or high-quality open-source projects the user can rebuild themselves.
   Find them with web search, e.g. `site:github.com <JD skill> <domain> stars:>500`, awesome-lists, or the
   company's own open-source repos.
3. **A strong original idea.** Use one only when no fitting reference repo exists.

## Quality bar (every chosen project must pass)
Recruiters skim hundreds of resumes and see the same tutorial projects again and again. A project only helps if it
stands out.
- **Not tutorial-level.** No to-do, weather or calculator apps, no basic chatbot or PDF-RAG, no e-commerce, Netflix
  or Spotify clones, no Titanic, Iris or MNIST, no stock predictors, no plain CRUD dashboards. The exception is a
  version with a clearly non-trivial angle.
- **Maps to the JD.** It proves at least 2 must-have skills, using the JD's stack where possible.
- **Real engineering depth.** It shows at least 2 of: system design, deployment, scale or concurrency, evaluation
  against a baseline, testing and CI, observability, security, or performance optimisation.
- **Fits the user's level.** One step beyond what they've already built, not five.

## Writing chosen projects on the resume
- **Name and tagline:** the user's own name for their project; for a reference repo, a clear descriptive name. Don't
  copy branded repo names verbatim.
- **Bullets:** describe what the user's version would do, with the JD's keywords.
- **Numbers:** include them only if the user's facts or the reference repo's README state them. Otherwise leave the
  bullet without a number.
- **Links:** the user's own repo gets `\href{URL}{GitHub}`. A reference repo or an idea gets no link; use
  `\hfill \textit{Tech, Stack}` instead.

## For the chat ("What to build and learn")
For each project in the target resume that the user hasn't built yet (or, with no target resume, the top 2–3
suggested projects):
- **Reference:** the repo link, or "original idea"
- **What to build:** 2–3 lines, focused on how their version should differ from the reference
- **Skills it proves:** which JD requirements
- **Build steps:** 4–6 short steps
- **Suggested order:** which project to build first
