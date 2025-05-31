from utils.functions import chat
from ui import start_App

if __name__ == '__main__':
    while True :
        input_msg = input("프로그램 실행 목적을 입력하세요 (0: 종료, 1: 감정등록, 2: 감정캘린더확인) : ")
        if input_msg == "1" :
            chat()
        elif input_msg == "2" :
            start_App()
        elif input_msg == "0" :
            print("프로그램을 종료합니다.")
            break
        else :
            print("0, 1, 2 중 하나의 값을 입력해주시기 바랍니다.")
            continue
