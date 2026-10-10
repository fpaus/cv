# CV

Source for Fabrizio Dante Pauselli's CV, rendered with [RenderCV](https://github.com/rendercv/rendercv).

## Layout

| Path | Purpose |
|---|---|
| `cv/master.yaml` | Single source of truth: content, variants, translations and design. Edit only this file. |
| `scripts/build_cvs.py` | Generates one RenderCV input per variant and language, then renders them. |
| `generated/` | Generated RenderCV inputs (git-ignored). |
| `build/` | Generic CV (EN + ES): PDF, HTML and Markdown. Published to GitHub Pages. |
| `dist/` | Role-specific PDFs (EN + ES). Local only, not published. |

## Variants

| Key | Target roles | Output |
|---|---|---|
| `generic` | Any role; public web CV | `build/Fabrizio_Dante_Pauselli[_ES].pdf` |
| `staff` | Staff / Senior Backend Engineer, Software Architect (.NET, Azure) | `dist/..._Staff_DotNet_Azure[_ES].pdf` |
| `ai` | AI Engineer, Agent Systems, AI Platform | `dist/..._AI_Engineer[_ES].pdf` |
| `em` | Engineering Manager, Head of Engineering | `dist/..._Engineering_Manager[_ES].pdf` |
| `sa` | Solutions Architect, AI Architect, Forward Deployed | `dist/..._Solutions_AI_Architect[_ES].pdf` |

## Master file rules

- A text value is a plain string or an `{en, es}` mapping.
- `in: [variant, ...]` limits an item to those variants. No `in` means every variant.
- `rank: {variant: n}` moves an item up for that variant. Lower numbers come first.
- Each variant sets its `headline`, `summary` and section order in `variants`.
- Every output must fit on 2 pages. Check after each change.

## Build

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_cvs.py --render
pdfinfo build/Fabrizio_Dante_Pauselli.pdf | grep Pages   # must be 2
pnpm deploy                                              # publish build/ to gh-pages
```

On Windows (PowerShell), use `.venv\Scripts\pip.exe` and `.venv\Scripts\python.exe` instead of the `.venv/bin/...` paths.

