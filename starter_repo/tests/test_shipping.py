"""요구사항에 따른 배송비 계산 결과를 검증하는 평가용 테스트."""

import pytest

from shipping import calculate_shipping_fee


@pytest.mark.parametrize(
    ("order_amount", "expected_fee"),
    [
        pytest.param(0, 3_000, id="zero-order"),
        pytest.param(1, 3_000, id="smallest-positive-order"),
        pytest.param(15_000, 3_000, id="ordinary-paid-shipping"),
        pytest.param(29_999, 3_000, id="just-below-threshold"),
        pytest.param(30_000, 0, id="exact-threshold"),
        pytest.param(30_001, 0, id="just-above-threshold"),
        pytest.param(100_000, 0, id="large-free-shipping-order"),
    ],
)
def test_calculate_shipping_fee(order_amount: int, expected_fee: int) -> None:
    assert calculate_shipping_fee(order_amount) == expected_fee
