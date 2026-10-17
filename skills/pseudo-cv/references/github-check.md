# GitHub check

Goal: find which of the user's repos prove the JD's requirements, and collect any real numbers they state.

## How to look
Use web fetch or search tools.
1. **List the repos:** `https://github.com/<user>?tab=repositories` gives each public repo's name, description, language and last update.
2. **Read the repos:** for each project on the resume, plus up to 10 other recent repos, open the README.
3. **Get structured data, if reachable:**
   - `https://api.github.com/repos/<user>/<repo>`
   - `.../languages`
   - `.../contributors` (shows whether the user did most of the work)
4. **What not to do:** don't clone, don't run code, don't open private or login-only links.
5. **If a page fails:** record "couldn't open". Never guess a repo's contents.
6. **If there's no web access:** ask the user to paste the READMEs for their top 3 projects.

## Record for each repo
| Field | Meaning |
|---|---|
| Repo | link |
| Proves | which JD requirements it shows (stack, features, deployment, tests) |
| Numbers | metrics actually stated in the README (accuracy, latency, users, stars); "none" if there aren't any |
| JD relevance | High / Medium / Low, with one reason |
| Last updated | date |

## Only the user's own account
For reference repos by other authors, see `project-selection.md`. Those are never recorded as the user's work.
