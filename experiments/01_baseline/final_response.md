Fixed the shipping threshold in [shipping.py](C:\Users\dldls\OneDrive\Code\it's_codex\experiments\01_baseline\workspace\shipping.py:5): orders of exactly 30,000 won now receive free shipping.

Test execution could not run because no usable Python interpreter is installed/configured in this environment (`python` points to the Windows Store alias; `py` reports no installed Pythons). The required command to run once Python is available is:

```powershell
python -m pytest -q tests/test_shipping.py
```