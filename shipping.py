"""주문 금액에 따른 배송비를 계산한다."""


def calculate_shipping_fee(order_amount: int) -> int:
    """0 이상의 정수 주문 금액(원)을 받아 배송비(원)를 반환한다."""
    # week2_jay2: 30,000원 이상 주문은 무료 배송으로 수정
    if order_amount >= 30_000:
        return 0
    return 3_000
