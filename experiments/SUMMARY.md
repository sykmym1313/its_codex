# Week 2 Shipping Fee: Initial Experiment Summary

Date: 2026-10-15 (KST)

## Design

Every condition started from an independent copy of `starter_repo`. The agent
could edit only its own `workspace/`; results were checked afterward with the
same project virtual environment and public test suite.

| Condition | First-pass source fix | External public tests | Source files changed | Agent-side test |
| --- | --- | --- | --- | --- |
| 01 Baseline | Success | 7/7 passed | `shipping.py` only | Blocked by Python launcher |
| 02 Structured context | Success | 7/7 passed | `shipping.py` only | Blocked by Python launcher |
| 03 `AGENTS.md` | Success | 7/7 passed | `shipping.py` only | Blocked by Python launcher |

## Interpretation

All three conditions produced the same correct one-line boundary fix. This is
expected for a small, explicit task and is not enough evidence to rank the
conditions. The meaningful observed failure was environmental: Codex could
inspect and edit the task, but its workspace could not launch the configured
Windows `python.exe` alias.

## Repair-loop status

A repair loop was not run because every first-pass patch passed the acceptance
test externally. Retrying would address the runner's Python configuration,
not repair the task solution. A future run should provision a usable Python
interpreter inside each workspace before comparing repair-loop behavior.

## Next experiment

Repeat each condition at least three times after fixing the runner environment,
then add a harder multi-file task. Record elapsed time, token usage/cost when
available, retry count, and full command logs before drawing conclusions.
