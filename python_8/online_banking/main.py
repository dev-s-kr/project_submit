import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from online_banking.services.banking_service import BankingService
from online_banking.utils.exceptions import InsufficientFundsError, NegativeAmountError, UserNotFoundError

def main() -> None:
    bankingservice = BankingService()

    while True:
        try:
            input_menu_num = input(
                "원하시는 메뉴의 번호를 입력하세요.\n"
                "[1] 사용자 추가\n"
                "[2] 사용자 찾기\n"
                "[3] 종료\n"
                "입력 : "
            )
            if input_menu_num == "1":
                input_user_name = input("[사용자 추가] 이름을 입력해주세요. : ")
                bankingservice.add_user(input_user_name)
            elif input_menu_num == "2":
                input_user_name = input("[사용자 찾기] 이름을 입력해주세요. : ")
                bankingservice.user_menu(input_user_name)
            elif input_menu_num == "3":
                break
            else:
                print("입력값이 올바르지 않습니다 다시 입력해주세요.")
        except ValueError as e:
            print(f"잘못된 입력입니다. : {e}")
        except InsufficientFundsError as e:
            print(f"오류가 발생했습니다. : {e}")
        except NegativeAmountError as e:
            print(f"오류가 발생했습니다. : {e}")
        except UserNotFoundError as e:
            print(f"오류가 발생했습니다. : {e}")
        except:
            print("오류가 발생했습니다.")

if __name__ == "__main__":
    main()