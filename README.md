# Codex 버그 수정 평가 스터디

Python과 pytest로 작은 버그 수정 과제를 풀며 Codex의 코드 이해, 요구사항 해석,
수정 및 검증 과정을 연습하는 저장소입니다. 첫 과제는 **주문 금액에 따른 배송비 계산**입니다.

**평가용 버그가 의도적으로 남아 있습니다. 처음 테스트를 실행하면 1개 실패, 6개 통과가 정상입니다.**
버그를 고친 뒤에는 7개 테스트가 모두 통과해야 합니다. 정답 코드는 포함하지 않습니다.

## 준비 및 실행

Python 3.10 이상이 필요합니다. 아래 명령은 이 README가 있는 저장소 루트에서 실행하세요.

### Windows PowerShell

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
```

`py`를 찾을 수 없지만 `python --version`이 동작한다면 첫 줄에서 `py -3` 대신 `python`을 사용하세요.
둘 다 없다면 Python 3.10 이상을 설치한 뒤 새 터미널을 열어 실행하세요.
가상환경을 활성화할 필요 없이 위 경로로 실행할 수 있습니다.

### macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pytest -q
```

가상환경은 이 저장소에서 사용할 Python 패키지를 별도로 관리하는 폴더입니다.
이후 문서의 `python -m pytest -q`에서 `python`은 위 가상환경의 Python 실행 경로를 뜻합니다.
`-m pytest`는 pytest를 실행하며, `-q`는 출력 내용을 간결하게 만듭니다.

## 진행 방법

1. [요구사항](REQUIREMENTS.md)을 읽고 함수가 반환해야 하는 값을 확인합니다.
2. 테스트를 실행하고 실패한 입력, 기대값, 실제값을 비교합니다.
3. `shipping.py`의 구현을 수정합니다.
4. 같은 테스트 명령을 다시 실행하고 `7 passed`를 확인합니다.
5. 변경 내용을 검토하고 버그 원인과 테스트 결과를 기록합니다.

`FAILED`는 해당 요구사항을 충족하지 못했다는 뜻입니다. 실행 마지막의 실패 개수와
오류 내용을 읽으세요. `ModuleNotFoundError`나 테스트 수집 오류는 의도한 버그가 아니라
환경 또는 실행 위치 문제입니다.

## 파일별 역할

| 파일 | 초보자를 위한 설명 |
| --- | --- |
| `README.md` | 저장소의 목적, 설치 방법과 과제 진행 순서를 안내합니다. |
| `REQUIREMENTS.md` | 코드가 지켜야 할 배송비 정책과 평가 기준을 정의합니다. |
| `shipping.py` | 실제 배송비를 계산하는 코드입니다. 평가 대상 버그가 있으며, 참가자가 수정할 파일입니다. |
| `tests/test_shipping.py` | 여러 주문 금액을 함수에 넣고 실제 배송비가 기대값과 같은지 확인합니다. `assert`는 두 값이 다르면 테스트를 실패시킵니다. `parametrize`는 같은 검사를 7가지 입력으로 반복합니다. |
| `requirements-dev.txt` | 테스트 실행에 필요한 pytest 버전을 고정하여 동일한 도구로 평가하도록 합니다. |
| `pytest.ini` | 테스트 폴더를 지정하고 저장소 루트의 `shipping.py`를 불러올 수 있게 설정합니다. |
| `.gitignore` | 가상환경과 자동 생성 캐시가 Git에 추가되지 않도록 합니다. |

테스트는 일반적인 금액뿐 아니라 기준 금액의 바로 아래, 정확한 기준, 바로 위를 확인합니다.
이처럼 조건이 바뀌는 지점 주변을 확인하는 검사를 **경계값 테스트**라고 합니다.

## Codex에 전달할 평가 요청 예시

```text
REQUIREMENTS.md를 읽고 shipping.py의 배송비 계산 버그를 수정해줘.
함수 이름과 매개변수를 유지하고 shipping.py만 변경해줘.
테스트와 설정은 변경하지 말고 pytest를 실행해 검증해줘.
마지막으로 버그 원인, 수정 내용, 테스트 결과를 설명해줘.
```

동일한 초기 상태에서 이 요청을 사용하고, 요구사항 준수 여부, 변경 범위,
테스트 결과와 설명을 비교하면 됩니다. 공개 테스트를 사용하는 입문용 과제이며,
종합적인 코딩 능력을 평가하는 벤치마크는 아닙니다.
