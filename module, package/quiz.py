import datetime
import random
import math
today = datetime.date.today()

# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다.
# 62400원 청구.59827원일 경우, 실제 청구 금액은?
bill = 59827
bill = math.floor(bill/100) * 100
# bill//100*100
# bill-bill%100
print("1.", bill)


# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다.
# 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
print('-'*20)
score = 56.5
score = math.floor(score/10) *10
# round(score/10)*10
# round(score, -1)
print("2.", score)


# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
print('-'*20)
num1 = random.sample(range(1, 46), 6) #중복 없음
print("3.", num1)


# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
print('-'*20)
num2 = random.sample(range(1, 10), 3)
# print("".join(str(n)for n in list_r))
# print("".join(map(str, list_r)))
print("4.", num2)

# 5. 내가 태어난 날로부터 며칠이 지났는지?
print('-'*20)
day1 = datetime.date(2004, 8, 29)
print("5.", today - day1)



# 6. 올해 크리스마스까지 며칠이 남았는지?
print('-'*20)
christmas = datetime.date(2021, 12, 25)
print("6.", christmas - today)



# 7. 내 생일이 며칠 남았는지?
print('-'*20)
day2 = datetime.date(2022, 8, 29)
print("7.", day2 - today)


# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
#마지막 번호가 몇 번인지 문자
#1~마지막 번호까지 리스트 만들기
# 나간 친구 번호 묻기 - 리스트에서 뺴기
#랜덤으로 섞고 출력
print('-'*20)
last_number = input("8. 마지막 번호는? ")
list_class = list(range(1, int(last_number) + 1))
while True:
    exclude_number = input("뺄 번호는?(enter치면 끝내자) ")
    if exclude_number == '':
        break
    list_class.remove(int(exclude_number))
print(list_class)