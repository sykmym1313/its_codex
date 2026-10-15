Fixed `shipping.py`: free shipping now applies at exactly 30,000 won by changing `>` to `>=`.

Cause: the threshold order (`30,000`) incorrectly received a 3,000 won fee.

Verification: `python -m pytest -q` could not run because the configured Windows `python.exe` alias is inaccessible. `py -m pytest -q` also reported no installed Python. The seven test cases were inspected and the change matches all expected outcomes.