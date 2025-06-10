class InsufficientFundsError(Exception):
    def __init__(self, balance: int) -> None:
        super().__init__(f"잔액이 부족합니다. 현재 잔액 : {balance}")

class NegativeAmountError(Exception):
    def __init__(self) -> None:
        super().__init__("금액은 음수를 입력할 수 없습니다.")

class UserNotFoundError(Exception):
    def __init__(self, username: str) -> None:
        super().__init__(f"검색 결과가 없습니다. 검색어 : {username}")