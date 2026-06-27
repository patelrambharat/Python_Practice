# AGENTS.md — AI Agent Instructions: Editor: Inline Suggest

Purpose
- Provide concise guidance to AI coding agents (inline suggestions) working in this small Python project.

When to use inline suggestions
- Use for small, local changes (bug fixes, small refactors, formatting, docstrings).
- Avoid proposing large cross-cutting refactors or new architecture in an inline suggestion.

Conventions
- Prefer minimal diffs: change as little as necessary and explain why.
- Run existing tests (if any) before proposing changes.
- Keep naming and style consistent with surrounding code.

How to propose a change
- Provide a one-paragraph rationale plus a single unified patch (diff or file edit).
- For `Conditionals.py`, suggest inline fixes like edge-case handling or clearer conditionals.

Commands to try (agent-run)
- Run tests if the project has pytest: `python -m pytest`
- Run a file directly for quick checks: `python "Conditionals.py"`

Notes
- No repository-wide docs were found in this folder; link to external docs if necessary.
- If you need broader context, ask the user before making sweeping changes.

---
Last-updated: 2026-06-27
