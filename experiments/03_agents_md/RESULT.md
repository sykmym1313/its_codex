# Result: 03 AGENTS.md Guidance

## Condition

- Prompt: `Fix the shipping-fee bug in this repository and verify the result with tests.`
- Repository guidance: local `workspace/AGENTS.md` restricts edits to
  `shipping.py` and requires test execution.
- Codex runtime: `gpt-5.6-terra`, medium reasoning, `workspace-write`

## Observed change

- Changed file: `workspace/shipping.py` only
- Change: `order_amount > 30_000` to `order_amount >= 30_000`
- Unnecessary source-file changes: none

## Verification

- Codex's own `python -m pytest -q` attempt could not start because `python`
  resolved to an inaccessible Windows Store alias.
- External verification using the project virtual environment: **7 passed**.

## Outcome

The source-code fix and scope adherence succeeded on the first pass. More
runs and harder tasks are required to evaluate the effect of `AGENTS.md`.
