# References

The published work taintline builds on, with a short note on how each source is used. Copies of these sources are not included in this repo; use the links. Any number quoted in a taintline write-up is checked against the original source first.

Keys in square brackets (e.g. [Watchtower]) are used to cite these sources elsewhere in the docs.

## Core sources

**[Watchtower]** Pandey, R. and Bhujang, A. (2026). *Poisoning the Watchtower: Prompt Injection Attacks Against LLM-Augmented Security Operations Through Adversarial Log Content.* arXiv:2605.24421, 23 May 2026. <https://arxiv.org/abs/2605.24421>

Defines log-substrate prompt injection, where an attacker places instructions in log fields they control so an LLM analyst reads them alongside the evidence. Introduces the S1–S4 attack classes (direct override, persona hijack, context manipulation, obfuscated payload) and tests them on gpt-4o-mini across classification, summarisation and remediation. taintline reuses its attack classes, task types, metrics and experimental design as the baseline, then extends the setup to a local model and a tool-using agent.

**[Poisoning the SOC]** Seymour, J. (2026). *Poisoning the SOC: Prompt Injection via Ingested Telemetry.* Poster, AI Village, DEF CON 34, August 2026. <https://aivillage.org/posters/poisoning-the-soc-prompt-injection-via-ingested-telemetry/>

A practitioner's view of the same attack in a real SOC pipeline: which log fields an attacker can control, and what a tool-using agent does once it reads them (verdict steering, action hijack, suppression rules, token-cost denial of service, evidence laundering). Source of the attacker-controlled field tiers in taintline's threat model and of the action-level attacks its tool controls are tested against.

**[ASD Harnesses]** Australian Signals Directorate (2026). *Agentic AI harnesses: the layer above the model.* First published 11 September 2026. <https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/agentic-ai-harnesses>

Defines the harness as every part of an agentic AI system except the model, lists eleven harness components and a set of good practices, and states that prompt-injection mitigations belong in the harness rather than the model. taintline's architecture is organised around the eleven components, and each control maps to one of the good practices. Licensed under CC BY 4.0; any material reproduced from it in this repo is attributed.

## Related work: prompt injection through logs

**[LogJack]** Shah, H. (2026). *LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents.* arXiv:2604.15368, 15 April 2026. <https://arxiv.org/abs/2604.15368> · Code: <https://github.com/HarshShah1997/logjack>

Injects instructions through cloud logs into tool-using debugging agents, run on eight models through cloud APIs, with outcomes up to remote code execution. It recommends least-privilege tools and human approval for writes but does not measure them. taintline measures those controls in a SOC triage setting.

**[LogInject]** Karanjai, R., Lu, Y., Hegadehalli Madhavarao, H., Xu, L. and Shi, W. (2026). *Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation.* arXiv:2607.14493, 16 July 2026. <https://arxiv.org/abs/2607.14493>

Introduces the LogInject framework and benchmark, including Context Stitching (a payload split across several log entries), and measures layered prompt- and input-level defences on GPT-4o, with their cost to benign accuracy. The closest prior result on layered defences for log analysis; it tests large models only.

**[Landauer]** Landauer, M., Skopik, F., Wurzenberger, M., Górski, F. and Krzysztoń, M. (2026). *Just Testing, Move Along: Evasion of LLM-based System Log Interpretation by Prompt Injection.* arXiv:2607.24174, 27 July 2026. <https://arxiv.org/abs/2607.24174> · Code: <https://github.com/ait-aecid/log-interpretation-prompt-injection>

Injected text presents malicious log activity as authorised testing, lowering an LLM's severity assessment while the logged behaviour stays malicious. An authority-style attack, in the same family as taintline's S2 persona hijack, tested on large models through cloud APIs.

**[Weight of Evidence]** Wilson, S. (2026). *The Weight of Evidence: How an Agentic SOC Analyst Earns Your Trust.* Poster, AI Village, DEF CON 34, August 2026. <https://aivillage.org/posters/the-weight-of-evidence-how-an-agentic-soc-analyst-earns-your-trust/>

Alters one machine-read artefact per trial to test whether a single attacker-controlled field can change an agentic SOC triage verdict, and argues that silent closures are the failure to watch for first. Summarised from the published abstract only.

## Related work: small local models

**[Tantaroudas]** Tantaroudas, N. D., Karachalios, I. and McCracken, A. J. (2026). *Can a Log Line Talk a Security Assistant out of an Alert? Prompt Injection, Quarantine and Locked Verdicts on a Small Local Model.* Preprints.org, 16 October 2026. Preprint, not peer-reviewed. doi:10.20944/preprints202610.1582.v1. <https://www.preprints.org/manuscript/202610.1582>

Tests Phi-4-mini (4-bit, llama.cpp) labelling web-server logs under four conditions, including a locked verdict where a rule-based detector sets the label and the model only explains it. Finds that a locked verdict protects the label but not the explanation, and that the exact payload wording matters more than the attack class. This is why taintline scores explanation integrity separately from the label and uses several wordings per attack class.

**[llm-soc-triage]** prhoguns (2026). *llm-soc-triage.* GitHub repository, MIT licence. <https://github.com/prhoguns/llm-soc-triage>

Qwen2.5-Coder 3B and 7B, run through Ollama, triage Wazuh-style alerts with a hardened prompt and a pattern-based guard; no tools. It shows that a naive local-model baseline plus a pattern guard is already public work. taintline adds the tool-using agent, per-control measurements and their utility cost.

## Defence prior art

**[Spotlighting]** Hines, K., Lopez, G., Hall, M., Zarfati, F., Zunger, Y. and Kıcıman, E. (2024). *Defending Against Indirect Prompt Injection Attacks With Spotlighting.* arXiv:2403.14720. <https://arxiv.org/abs/2403.14720>

Prompt transformations (delimiting, datamarking, encoding) that make the source of untrusted input clear to the model. taintline's provenance tags are a delimiting-style spotlight; datamarking is a candidate variant to compare against.

**[Dual LLM]** Willison, S. (2023). *The Dual LLM pattern for building AI assistants that can resist prompt injection.* Blog post, 25 April 2023. <https://simonwillison.net/2023/Apr/25/dual-llm-pattern/>

A privileged model with tools that never sees untrusted text, paired with a quarantined model without tools that handles it. The basis for taintline's isolated decoding step.

**[CaMeL]** Debenedetti, E., Shumailov, I., Fan, T., Hayes, J., Carlini, N., Fabian, D., Kern, C., Shi, C., Terzis, A. and Tramèr, F. (2025). *Defeating Prompt Injections by Design.* arXiv:2503.18813. <https://arxiv.org/abs/2503.18813> · Code: <https://github.com/google-research/camel-prompt-injection>

Tracks where every value came from and stops untrusted data from changing the program's control flow or leaving through unauthorised tool calls. taintline's taint tracking applies the same idea to tool arguments. In triage the verdict itself has to be derived from attacker-controlled log content, so this kind of flow control can protect taintline's actions but not its verdicts; the verdict path needs separate controls.

**[Design Patterns]** Beurer-Kellner, L., Buesser, B., Creţu, A.-M., Debenedetti, E., Dobos, D., Fabian, D., Fischer, M., Froelicher, D., Grosse, K., Naeff, D., Ozoani, E., Paverd, A., Tramèr, F. and Volhejn, V. (2025). *Design Patterns for Securing LLM Agents against Prompt Injections.* arXiv:2506.08837. <https://arxiv.org/abs/2506.08837>

Six design patterns that limit what an agent can do in exchange for resistance to prompt injection, including action-selector, plan-then-execute and context-minimisation. Gives taintline's architecture its vocabulary: a verdict restricted to fixed labels is close to an action-selector, and giving each alert its own context is close to context-minimisation.

## Guidance and technical references

**[NCSC]** National Cyber Security Centre (UK) (2025). *Prompt injection is not SQL injection (it may be worse).* Blog post, 8 December 2025. <https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection>

Argues that LLMs have no built-in separation between data and instructions, so prompt injection may never be fully mitigated and systems should limit what a misled model can do. Cited by [ASD Harnesses]. It underpins taintline's split between hard guarantees on actions and bounded risk on verdicts.

**[nginx log module]** nginx. *Module ngx_http_log_module* (`log_format` and its `escape` parameter). <https://nginx.org/en/docs/http/ngx_http_log_module.html#log_format>

Documents how nginx escapes access-log fields by default. taintline's log generator applies the same escaping, so payloads look the way they would after real ingestion.

**[MCPKernel]** MCPKernel. Open-source security gateway for agent tool calls, Apache 2.0. <https://pypi.org/project/mcpkernel/>

Applies policy rules, taint scanning and audit logging to MCP tool calls. An optional comparison baseline for taintline's own permission, taint-tracking and audit controls; taintline does not depend on it.
