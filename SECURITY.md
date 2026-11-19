# Security policy

taintline is a research and portfolio project that studies prompt injection against
AI security-triage agents and measures harness-level defences.

## Reporting a vulnerability

Please report suspected vulnerabilities privately through GitHub's
**"Report a vulnerability"** button on the Security tab (private vulnerability reporting).
Do not open a public issue for security problems.

## Scope

In scope:
- Bypasses of taintline's harness controls (provenance, permissions, taint tracking, audit log)
- Ways attacker-controlled log content can trigger tool calls or other side effects
- Secrets or sensitive data exposure in the code or CI pipeline

Out of scope:
- The underlying language models themselves
- Attacks requiring control of the machine taintline runs on

## Data handling

taintline uses **synthetic** log data only. Do not submit real logs, personal data or
classified material to this project.
