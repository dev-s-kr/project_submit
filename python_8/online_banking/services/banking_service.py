from online_banking.models.user import User
from online_banking.utils.exceptions import InsufficientFundsError, NegativeAmountError, UserNotFoundError

class BankingService:
    def __init__(self) -> None:
            self.user_list = []
    
    def add_user(self, username: str) -> None:
        self.user_list.append(User(username))

    def find_user(self, username: str) -> User:
        for user in self.user_list:
            if user.username == username:
                return user
        raise UserNotFoundError("검색 결과가 없습니다.")

    def user_menu(self, username: str) -> None:
        user = self.find_user(username)
        while True:
            try:
                selected_menu = input(
                    "원하시는 메뉴의 번호를 입력하세요.\n"
                    "[1] 입금\n"
                    "[2] 출금\n"
                    "[3] 잔고 확인\n"
                    "[4] 거래 내역 확인\n"
                    "[5] 종료\n"
                    "입력 : "
                )
                if selected_menu == "1":
                    input_amount = input(
                        "입금하실 금액을 입력해주세요.\n"
                        "입력 : "
                    )
                    user.account.deposit(int(input_amount))
                elif selected_menu == "2":
                    input_amount = input(
                        "출금하실 금액을 입력해주세요.\n"
                        "입력 : "
                    )
                    user.account.withdraw((int(input_amount)))
                elif selected_menu == "3":
                    print(f"현재 잔액 : {user.account.get_balance()}")
                elif selected_menu == "4":
                    for transcation in user.account.get_transactions():
                        print(transcation)
                elif selected_menu == "5":
                    break
                else:
                        print("잘못된 입력입니다. 다시 시도하세요.")
            except ValueError as e:
                print(f"잘못된 입력입니다: {e}")
            except InsufficientFundsError as e:
                print(f"오류: {e}")
            except NegativeAmountError as e:
                print(f"오류: {e}")
            except UserNotFoundError as e:
                print(f"오류: {e}")