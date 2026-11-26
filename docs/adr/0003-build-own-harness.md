# ADR-0003: Build our own harness; MCPKernel as comparison baseline only

- **Status:** Accepted
- **Date:** 2026-11-26

## Context

- The decision was made on 17 November 2026; this ADR records why.
- taintline needs harness controls around the model, which split into two halves:
  1. **Action side:** permissions (C5), taint tracking into tool arguments (C6), audit log (C9).
  2. **Verdict side:** provenance tags and escaping (C1/C2), structured output (C3), evidence-citation checks (C4), locked-verdict baseline.
- The project's purpose is to measure each control on its own, so every control must be a separate switch that can be turned on or off between eval runs.
- MCPKernel is an open-source security gateway that sits between an agent and its tools and checks each tool call (policy rules, taint scanning, sandboxing, audit log). It overlaps with the action side, so the obvious question is why not use it.

## Options considered

1. **Use MCPKernel as the harness.**
   - Pros: already works; Apache 2.0; maps onto several ASD harness components.
   - Cons:
     - Only covers the action side; does nothing for verdicts.
     - Has no idea which log fields are attacker-controlled.
     - Most of the controls this project needs to measure are not in it.
     - Still early: version 0.3.0, 56 downloads in the last month (Nov 2026).
     - Heavy dependency tree (fastapi, httpx, mcp, OpenTelemetry, sigstore, uvicorn and more), which adds supply-chain surface.
2. **Build all controls ourselves, with no comparison.**
   - Pros: every control is a separate switch; small dependencies; I can explain every line.
   - Cons: more work; bugs are ours; nothing external to check the action-side controls against.
3. **Build our own controls, and use MCPKernel only as an optional comparison baseline for C5/C6/C9 if time allows.**
   - Pros: everything from option 2, plus a reference point on the action side.
   - Cons: the comparison only happens if there's spare time.

## Decision

Option 3. taintline builds every harness control itself, each as its own switch, so its effect on attack success and usefulness can be measured one control at a time. MCPKernel is not part of taintline. If time allows, the same action-hijack attacks will also be run through MCPKernel to compare it with taintline's own action-side controls (C5/C6/C9).

## Consequences

- **Easier:** measuring one control at a time; explaining the entire harness in interviews; keeping dependencies small.
- **Harder:** more code to write and test; no mature tool catching our mistakes.
- **Not doing:** sandboxing and signed traces, which MCPKernel has. They aren't needed for taintline's measurements.
- **Revisit if:** MCPKernel matures significantly, or taintline's tools move to MCP.
