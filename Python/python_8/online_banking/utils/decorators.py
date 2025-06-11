from typing import Callable

def validate_transaction(func: Callable) -> Callable:
    def wrapper(self, amount):
        if amount <= 0:
            raise ValueError("0보다 큰 금액을 입력하세요.")
        return func(self, amount)
    return wrapper