import sys
import time
import os
import stat

# 메인 함수
def main(path: str, message: str):
    """
    입력받은 내용을 임시파일을 생성하여 자장후 20초 후에 입력한 파일에 작성하는 함수
    Args:
        path(str): 작성할 파일의 위치
        message(str): 입력할 내용. 
    """
    try:
        with open("./race.tmp", "w", encoding = "UTF-8") as race_tmp:
            race_tmp.write(message + "\n")

        
        os.chmod("./race.tmp", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IROTH | stat.S_IWOTH)
        print("Write Tmp Ok")
    except OSError:
        print("Can't open", file=sys.stderr)
        sys.exit("Tmp File Open Error")

    

    # 20초 대기
    for i in range(20):
        time.sleep(1)
        print(i + 1)
    
    # 20초로 부족하면 주석 해제 후 실행.
    input()


    try:
        # 파일을 쓰기 모드로 열기
        with open("./race.tmp", "r", encoding = "UTF-8") as race_tmp_2:
            message_tmp = race_tmp_2.read()
        print("Read Ok")


        with open(path, 'w', encoding = "UTF-8") as fopen:
            fopen.write(message_tmp)
        print("Write Ok")

        os.remove("./race.tmp")

    except OSError:
        print("Can't open", file=sys.stderr)
        sys.exit("Read/Write File Open Error")

# 프로그램 시작점
if __name__ == "__main__":
    main("./race.txt", "Root로 실행한 파일입니다" )