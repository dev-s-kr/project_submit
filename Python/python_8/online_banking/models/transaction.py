class Transaction:
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def __str__(self) -> str:
        return f"{self.transaction_type} : {self.amount}, 잔액 : {self.balance}"
    
    def to_tuple(self) -> tuple:
        tuple(str(self))