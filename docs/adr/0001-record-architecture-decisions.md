# ADR-0001: Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-11-19

## Context

taintline is a solo project built over several months, with long breaks during
semester and an overseas work year. Design choices made now (harness design,
evaluation method, model runtime) need to be explainable months later, both to
future me and to reviewers and interviewers.

## Options considered

1. **No formal record:** fastest, but the reasoning is lost.
2. **One long design document:** keeps everything together, but decisions get buried and edited over.
3. **Architecture Decision Records (one short file per decision):** lightweight, append-only, easy to review.

## Decision

Use ADRs in `docs/adr/`, numbered sequentially, using `0000-template.md`. ADRs are not
edited after acceptance; a changed decision gets a new ADR that supersedes the old one.

## Consequences

Each significant decision costs ~10 minutes to write up. In return, the repository
carries its own design history, and every major trade-off has a written rationale.
