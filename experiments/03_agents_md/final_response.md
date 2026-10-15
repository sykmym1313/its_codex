Fixed `shipping.py`: free shipping now applies at exactly ₩30,000 (`>=` rather than `>`).

Bug cause: the threshold excluded ₩30,000 orders, incorrectly charging ₩3,000.

Files changed: `shipping.py` only.

Test result: `python -m pytest -q` could not run because the configured Python launcher is unavailable (`WindowsApps\python.exe` access error); `py` also reports no installed Python interpreter.