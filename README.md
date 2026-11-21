# taintline

Local-first AI SOC triage agent with a hardened harness, evaluated against log-borne prompt injection.

> **Status: work in progress.** Project setup is done; no results yet. First release (v0.1 "baseline") is planned for December 2026. This repo is built in public: every change lands through a pull request with passing CI, so the history is the progress log.

## What this is

Security teams are starting to use LLM agents to triage alerts. Those agents read log fields an attacker controls (User-Agent, Referer, request URLs), so a crafted log line can try to talk the agent into a wrong verdict or misuse its tools.

taintline has three parts:

- **Agent:** a small triage agent on a local, quantised model. It reads an alert and its logs, decides benign or malicious, explains why and maps it to MITRE ATT&CK.
- **Harness:** the controls around the model: provenance tagging, least-privilege tools, human approval, taint tracking, evidence checks and audit logging, following ASD's *Agentic AI harnesses* guidance (Sept 2026).
- **Evaluation:** reproduces published log-injection attacks against the agent and measures, per control, how much it reduces attack success and what it costs in usefulness (false escalations, approvals, tokens).

The harness and the measurements are the point; the agent is the test subject.

## Planned releases

- **v0.1 "baseline"** (Dec 2026): synthetic log generator, attack injector, eval harness, undefended baseline.
- **v0.2 "actions"** (Jan 2027): tool-using agent; permission and taint-tracking controls against action hijacking.
- **v0.3 "verdicts"** (Feb 2027): verdict-level controls, full security-versus-usefulness results, demo.

## Scope and safety

- Every attack payload targets only taintline's own synthetic log pipeline. Nothing here is aimed at systems the author doesn't own.
- No real customer, user or personal data is used.
- This reproduces published attacks to measure defences; it is not new attack research. Sources will be listed in `docs/references.md`.

## Design decisions

Recorded as ADRs in [`docs/adr/`](docs/adr/).

## Development

```bash
uv sync
uv run pre-commit install
uv run pytest
```

## Security

See [SECURITY.md](SECURITY.md).

## License

Apache 2.0. See [LICENSE](LICENSE).
