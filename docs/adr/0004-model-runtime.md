# ADR-0004: Run models locally with a pinned llama.cpp build

- **Status:** Accepted
- **Date:** 2026-11-26

## Context

- taintline needs a local model runtime on my laptop: RTX 3050 6 GB, 16 GB RAM, Windows 11 Home.
- Eval results must be reproducible: the same inputs give the same outputs, and every result is tied to exact software and model versions.
- Nothing should leave the machine; the model reads attacker-controlled log content.
- The closest prior studies used llama.cpp (Tantaroudas et al.) and Ollama (llm-soc-triage).

## Options considered

1. **Ollama.**
   - Pros: one installer, models pulled by name.
   - Cons: updates very often and hides the llama.cpp version and chat template underneath, so results could shift without me changing anything.
2. **llama.cpp prebuilt, native Windows.**
   - Pros: pin an exact build and model file hash; schema-constrained JSON output and tool calling built in.
   - Cons: manual setup; I manage model files and updates myself.
3. **llama.cpp inside WSL2.**
   - Pros: Linux environment.
   - Cons: an extra layer and more setup, with no benefit for this project.

## Decision

- Option 2: llama.cpp build `b12774` (= release `v1.1.0`, commit `1715275`), Windows CUDA 12.4 build.
- Primary model: Llama 3.1 8B Instruct `Q4_K_M`. Second model: Phi-4-mini (same model as Tantaroudas et al.).
- Server settings: localhost only (`--host 127.0.0.1`); an API key from a file outside git; one request at a time (`--parallel 1`); 4K context; all layers on the GPU; temperature 0, top-k 1, fixed seed.
- Downloads verified before use: the sha256 of both zips matched the release page, and `gh attestation verify` confirmed the main zip was built by ggml-org/llama.cpp's own release workflow. The model's sha256 matched Hugging Face.

## Consequences

- **Easier:** reproducible results; the environment is recorded with every result; a clear provenance story (ASD: choose a trusted model and assess its provenance).
- **Harder:** manual updates; model files live outside the repo; a 4K context ceiling (only ~0.85 GB of VRAM spare when loaded).
- **Measured in the smoke test:** ~144 tokens/s reading the prompt, ~23 tokens/s generating.
- **Revisit if:** a bug forces an upgrade (record the new build), a longer context is needed, or the hardware changes.
