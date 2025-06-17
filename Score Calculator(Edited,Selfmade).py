# n개 과목 점수 입력받기
subject_count = int(input("과목 수를 입력하세요:"))

scores = []

for i in range(subject_count):
    score = int(input(f"{i+1}번째 점수를 입력하세요:"))
    scores.append(score)

# 평균 계산하기

total = sum(scores)

avg_score = total / subject_count

print(avg_score)

# 평균 점수 기준으로 등급 계산 , 함수 출력(평균/등급 출력) 

if(avg_score > 90):
    print("평균 : " + f"{avg_score}")
    print("등급 : A")
elif(avg_score > 80):
    print("평균 : " + f"{avg_score}")
    print("등급 : B")
elif(avg_score > 70):
    print("평균 : " + f"{avg_score}")
    print("등급 : C")
elif(avg_score > 60):
    print("평균 : " + f"{avg_score}")
    print("등급 : D")
else:
    print("평균 : " + f"{avg_score}")
    print("등급 : F")