# race_condition_example

레이스 컨디션 실습 예제입니다.

`race.py` 파일은 `race.tmp` 파일을 생성하여 "Root 권한으로 실행된 파일입니다."라는 내용을 저장한 후, 20초 뒤에 `race.tmp` 파일의 내용을 `race.txt` 파일로 저장합니다. `race_hack.py` 파일은 `race.tmp` 파일이 존재할 경우 이의 내용을 "Race Condition!!!"으로 변경합니다.

Race Condition으로 공유 자원인 `race.tmp` 파일을 변경함으로써, root 소유자의 644 권한 파일인 `race.txt` 파일을 변경한 것을 볼 수 있습니다.

## 사용법

1. `race.py`에 대해 setuid 비트를 설정하고 소유자를 root로 변경합니다:
   ```bash
   sudo chmod 4755 race.py
   sudo chown root:root race.py
   ```
   
2. `race_hack.py`에 대해 모든 사용자에게 읽기, 쓰기, 실행 권한을 부여하고 소유자를 변경합니다:
   ```bash
   sudo chmod 777 race_hack.py
   sudo chown [user]:[user] race_hack.py
   ```

3. 두 파일을 실행합니다:
   ```bash
   sudo python3 race.py &
   sudo python3 race_hack.py
   ```

4. `race.txt`를 확인합니다:
   ```bash
   cat race.txt
   ```




