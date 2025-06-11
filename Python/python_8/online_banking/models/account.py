from online_banking.models.transaction import Transaction
from online_banking.utils.decorators import validate_transaction
from online_banking.utils.exceptions import InsufficientFundsError, NegativeAmountError


class Account:
    bank_name = ""

    def __init__(self) -> None:
        self.__balance = 1000
        self.transactions = []
    
    @validate_transaction
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        self.__balance += amount
        self.transactions.append(Transaction("입금", amount, self.__balance))
        print(f"{amount}원을 입금했습니다. 잔액 : {self.__balance}")
    
    validate_transaction
    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise NegativeAmountError()
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance)
        self.__balance -= amount
        self.transactions.append(Transaction("출금", amount, self.__balance))
        print(f"{amount}원을 출금금했습니다. 잔액 : {self.__balance}")

    def get_balance(self) -> int:
        return self.__balance

    def get_transactions(self) -> list:
        return self.transactions
    
    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name