# Week 2 과제: 배송비 계산 버그 수정

## 폴더 구성

```text
week2_shipping_fee/
├── task.yaml                 # 과제 메타데이터와 검증 명령
├── REQUIREMENTS.md           # 원본 요구사항
├── starter_repo/             # 수정 전, 실행 가능한 시작 코드
│   ├── shipping.py
│   ├── requirements-dev.txt
│   ├── pytest.ini
│   └── tests/test_shipping.py
├── solution/shipping.py      # 해결된 코드
└── ...
```

`starter_repo`는 Codex에 제공할 고정된 시작 상태이며 자체 테스트와 실행 설정을
포함한다. `solution`은 사람이 검토할 수 있는 정답 구현이다. 평가 시에는
`starter_repo`를 별도 작업공간에 복사하고 공개/숨김 테스트로 결과를 판정한다.

## 과제 목표

`shipping.py`의 `calculate_shipping_fee`가 주문 금액에 따라 올바른 배송비를
반환하도록 수정한다.

## 요구사항

| 주문 금액 | 기대 배송비 |
| ---: | ---: |
| 30,000원 미만 | 3,000원 |
| 30,000원 이상 | 0원 |

함수 이름과 매개변수는 유지하고, 테스트나 요구사항 파일은 변경하지 않는다.

## 문제 재현

`starter_repo`의 수정 전 구현은 무료 배송 조건을 `order_amount > 30_000`으로 검사했다.
따라서 정확히 30,000원인 주문은 무료 배송이 아니라 3,000원으로 계산되어
경계값 테스트가 실패했다.

```python
calculate_shipping_fee(30_000)  # 수정 전: 3000, 기대값: 0
```

## 해결 방법

무료 배송 조건이 30,000원을 포함해야 하므로 비교 연산자를 `>`에서 `>=`로
변경했다.

```python
if order_amount >= 30_000:
    return 0
```

수정 범위는 `shipping.py`의 조건문 한 줄이다. 해결 결과는
`solution/shipping.py`에 보관한다.

## 검증

과제 폴더에서 `starter_repo`를 별도 작업공간으로 복사해 실행한다. 이렇게 하면
고정된 시작 스냅샷을 훼손하지 않고 해결 전후 결과를 모두 확인할 수 있다.

```powershell
Copy-Item starter_repo workspace -Recurse
Set-Location workspace
python -m pytest -q
```

시작 상태에서는 `1 failed, 6 passed`가 정상이다. 이어서 해결 코드를 작업공간에
반영하고 같은 테스트를 실행한다.

```powershell
Copy-Item ..\solution\shipping.py .\shipping.py -Force
python -m pytest -q
```

결과: `7 passed`

## 배운 점

조건이 바뀌는 값의 바로 아래·정확한 값·바로 위를 함께 검증하는 경계값
테스트가 중요하다. 이번 버그는 기준값 자체를 포함하지 않은 비교 연산자에서
발생했다.
