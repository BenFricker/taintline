# ADR-0002: Build in public

- **Status:** Accepted
- **Date:** 2026-11-20

## Context

AI security, and prompt injection defence in particular, is changing quickly. Several directly relevant papers and repositories were published in the weeks before this project started, and the literature review changed during a single evening. If this repository stays private until the MVP is finished in February, it will be hard to tell whether the work was done with genuine, consistent effort alongside the field, or reworked from whatever had been published by then. Commit dates alone can be faked; GitHub's server-side records of pull requests, CI runs and releases cannot. A public repository establishes a dated record of the work and shows how it was built, stage by stage, with the goal of building defences and publishing their measured results.

## Options considered

1. **Stay private, reveal when complete.**
  + Pros: mistakes and unfinished work stay hidden; one polished launch.
  + Cons: no proof of when the work was done; a single reveal in February could already look dated; the process is invisible.
2. **Build in public with staged releases.**
  + Pros: a timestamped record of every change; employers can see the process and decisions, not just the result; regular releases force steady progress.
  + Cons: mistakes are visible; a leaked secret would be public immediately; others can follow the approach as it develops.
3. **Several small one-month projects instead.**
  + Pros: always current; quick wins.
  + Cons: breadth without depth; reads like a set of tutorials rather than sustained engineering; no single result strong enough to anchor an interview.

## Decision

Make the repository public once Stage 0 is complete. Every change lands through a pull request with passing CI, and the project ships as three tagged releases with short write-ups: v0.1 "baseline" (December 2026), v0.2 "actions" (January 2027) and v0.3 "verdicts" (February 2027).

## Consequences

- **Easier:** proving when each piece of work was done; showing employers the process and the reasoning behind decisions; staying consistent, because progress is visible.
- **Harder:** mistakes are public; any leaked secret would be exposed immediately; others can follow and reuse the approach.
- **Mitigations:** gitleaks in pre-commit, a strict `.gitignore`, GitHub push protection and branch protection on `main`; a pre-public checklist before the switch; reference PDFs are never committed. If similar work appears later, the dated record shows which came first.
- **Revisit if:** anything in the repository starts to function as offensive tooling rather than defensive research, or a prospective defence employer or the clearance process raises concerns about publishing prompt-injection payloads.
