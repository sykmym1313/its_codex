# Result: 02 Structured Context

## Condition

- Prompt specifies the requirement source, allowed file, prohibited files, and
  exact verification command.
- Repository guidance: none
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

The source-code fix and scope adherence succeeded on the first pass. This
single run does not establish that structured context is better than baseline.
