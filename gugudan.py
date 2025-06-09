#1 사용자로부터 입력 받기
#1 ~~

dan = int(input(" Select the number (2~9) : "))

#2 입력값이 유효한지 검사
#2 ~~

if 2 <= dan <= 9:

#3 구구단 출력
#3 ~~

    for i in range(1,10):
        print(f"{dan} x {i} = {dan * i}")
else:
    print("You should select 2 ~ 9.")
