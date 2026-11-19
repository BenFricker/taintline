# Contributing

## Setup

```powershell
uv sync                      # create .venv and install locked dependencies
uv run pre-commit install    # run checks on every commit
```

## Workflow

1. Branch from `main`: `git switch -c feat/short-description`
2. Make small, focused commits.
3. Run `uv run pre-commit run --all-files` and `uv run pytest`.
4. Push and open a pull request; CI must pass before merging.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):
`feat:`, `fix:`, `docs:`, `test:`, `chore:`, `refactor:`, followed by a short
present-tense summary, e.g. `feat: add provenance label to log schema`.

## Design decisions

Significant decisions are recorded as ADRs in `docs/adr/`. Copy `0000-template.md`.
