# #숫자 자료형
# from pip._vendor.urllib3.util import url
#
# print(5)
# print(-10)
# print(3.4)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
#
# #문자열 자료형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)
#
# #boolean 자료형
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))
#
# #변수(애완동물 소개)
# animal="강아지"
# name ="연탄이"
# age=4
# hobby="산책"
# is_adult= age>=3
#
# print("우리집" +animal+"의 이름은 "+name+"에요")
# hobby="공놀이"
# #print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name+"는 어른일까요? "+str(is_adult))
#
# #주석
# '''여러 문장
# 주석 처리 방법'''
#
# #Quiz 1
# # 변수를 이용하여 다음 문장을 출력하시오
# # 변수명: station
# # 변수값: "사당", "신도림", "인천공한" 순서대로 입력
# # 출력문장: xx행 열차가 들어오고 있습니다.
# station="사당"
# station="신도림"
# station="인천공항"
# # print(station+ "행 열차가 들어오고 있습니다.")
# print(station, "행 열차가 들어오고 있습니다.")
#
# #연산자
# print(1+1)#2
# print(3-2)#1
# print(5*2)#10
# print(6/3)#2
#
# print(2**3) #2^3=8
# print(5%3)#나머지 구하기 2
# print(10%3)#1
# print(5//3)#1
# print(10//3)#3
#
# print(10>3)#True
# print(4>=7)#False
# print(10<3)#False
# print(5<=5)#True
#
# print(3==3)#True
# print(4==2)#False
# print(3+4==7)#True
#
# print(1 != 3)#True(같지 않다)
# print(not(1 != 3))#False
#
# print((3>0)and(3<5))#True
# print((3>0)&(3<5))#True
#
# print((3>0) or (3>5))#True
# print((3>0) | (3>5))#True
#
# print(5>4>3)#True
# print(5>4>7)#False
#
# #간단한 수식
# print(2+3*4)#14
# print((2+3)*4)#20
# number=2+3*4 #14
# print(number)
# number= number+2 #16
# print(number)
# number +=2 #18
# print(number)
# number *= 2 #36
# print(number)
# number /= 2 #18
# print(number)
# number -= 2 # 16
# print(number)
#
# number %= 5 #1
# print(number)
#
# #숫자처리함수
# print(abs(-5))#5
# print(pow(4, 2))#4^2 = 4*4=16
# print(max(5, 12)) #12
# print(min(5, 12)) #5
# print(round(3.14))#3
# print(round(4.99)) #5
#
# from math import *
# print(floor(4.99)) # 내림. 4
# print(ceil(3.14)) #올림.4
# print(sqrt(16))  #제곱근. 4
#
# #랜덤 함수
# from random import *
#
# # print(random()) #0.0~1.0 미만의 임의의 값 생성
# # print(random() * 10) #0.0~10.0 미만의 임이의 값 생성
# # print(int(random() *10)) #0~10 미만의 임의의 값 생성
# # print(int(random() *10)) #0~10 미만의 임의의 값 생성
# # print(int(random() *10)) #0~10 미만의 임의의 값 생성
# # print(int(random() *10)+1)#1~10 이하의 임의의 값 생성
# # print(int(random() *10)+1)#1~10 이하의 임의의 값 생성
# # print(int(random() *10)+1)#1~10 이하의 임의의 값 생성
# # print(int(random() *10)+1)#1~10 이하의 임의의 값 생성
# # print(int(random() *10)+1)#1~10 이하의 임의의 값 생성
# # print(int(random() *10)+1)#1~10 이하의 임의의 값 생성
#
# # print(int(random() *45)+1)#1~45 이하의 임의의 값 생성
# # print(int(random() *45)+1)#1~45 이하의 임의의 값 생성
# # print(int(random() *45)+1)#1~45 이하의 임의의 값 생성
# # print(int(random() *45)+1)#1~45 이하의 임의의 값 생성
# # print(int(random() *45)+1)#1~45 이하의 임의의 값 생성
# # print(int(random() *45)+1)#1~45 이하의 임의의 값 생성
#
# # print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
# # print(randrange(1, 46)) #1~46 미만의 임의의 값 생성
#
# print(randint(1, 45)) #1~45 이하의 임의의 값 생성
# print(randint(1, 45)) #1~45 이하의 임의의 값 생성
# print(randint(1, 45)) #1~45 이하의 임의의 값 생성
# print(randint(1, 45)) #1~45 이하의 임의의 값 생성
# print(randint(1, 45)) #1~45 이하의 임의의 값 생성
# print(randint(1, 45)) #1~45 이하의 임의의 값 생성
#
# #Quiz 2
# # 당신은 취근에 코딩 스터디 모임을 새로 만들었습니다.
# # 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# # 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# # 조건1: 랜덤으로 날짜를 뽑아야 함
# # 조건2: 월별 날짜는 다름을 감안하여 최소 일수읜 28 이내로 정함
# # 조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외
# # (출력문 예제)
# # 오프라인 스터디 모임 날짜는 매월 x  일로 선정되었습니다.
# from random import *
# print("오프라인 스터디 모임 날짜는 매월", randint(4, 28), "일로 선정되었습니다.")
#
# date = randint(4, 28) #변수로 지정
# print("오프라인 스터디 모임 날짜는 매월", str(date), "일로 선정되었습니다.")
#
# #문자열
# sentence ='나는 소년입니다.'
# print(sentence)
# sentence2="파이썬은 쉬워요"
# print(sentence2)
# sentence3= """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)
#
# #슬라이싱
# jumin = "990120-1234567"
#
# print("성별: "+jumin[7])
# print("연: "+jumin[0:2])#0부터 2직전까지
# print("월: "+jumin[2:4])
# print("일: "+jumin[4:6])
#
# print("생년월일: "+jumin[:6])#처음부터 6직전까지
# print("뒤 7자리: "+jumin[7:])#7부터 끝까지
# print("뒤 7자리(뒤에서부터): "+jumin[-7:])
#
# #문자열 처리 함수
# python="Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
#
# index = python.index("n")
# print(index)
# index = python.index("n", index+1)
# print(index)
#
# #print(python.find("Java"))
# #print(python.index("Java"))
# print("hi")
#
# print(python.count("n"))
#
# #문자열 포맷
# #방법1
# print("a"+"b")
# print("a", "b")
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아해요." %"파이썬")
# print("Apple 은 %c로 시작해요" %"A")
#
# print("나는 %s살입니다. " %20)
# print("나는 %s색과 %s색을 좋아해요" %("파란", "빨강"))
# #방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨강"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))
# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨강"))
# #방법4
# age=20
# color="빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
#
# #탈출문자
# print("백문이 불여일견 \n 백견이 불여일타")#줄바꿈
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# #\" \' :문장 내에서 따옴표
# #\\ : 문장 내에서 \
# print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")
# #\r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
# #\b :백스페으스(한글자 삭제)
# print("Redd\bApple")
# #\t: 탭
# print("Red\tApple")
#
# #Quiz 3
# # 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# # 예) http://naver.com
# # 규칙1: http:// 부분은 제외 => naver.com
# # 규칙2: ㅊㅓ음 만나는 점(.) 이후 부분은 제외 => naver
# # 규칙3: 남은 글자 중 처음 세자리 +글자 갯수+ 글자내 'e' 객수 + "!" 로 구성
# #                     (nav)               (5)            (1)          (!)
# # 예) 생성된 비밀번호 nav51!
# nrl="http://naver.com"
# #my_str=url.replace("http://", "")
# #my_str=my_str[:my_str.index(".")] #my_str[0:5]
# print("my_str")
# def my_str(args):
#     pass
# #password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
# #print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
#
# #리스트
# #지하철 칸별로 10명, 20명, 30명
# #subway1=10
# #subway2=20
# #subway3=30
#
# # subway=[10, 20, 30]
# # print(subway)
# #
# # subway=["유재석", "조세호", "박명수"]
# # print(subway)
# #
# # print(subway.index("조세호"))
# # subway.append("하하")
# # print(subway)
# #
# # subway.insert(1, "정형돈")
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
#
# # print(subway.pop())
# # print(subway)
# #
# # print(subway.pop())
# # print(subway)
#
# # subway.append("유재석")
# # print(subway)
# # print(subway.count("유재석"))
# #
# # num_list = [5,2,4,3,1]
# # num_list.sort()
# # print(num_list)
# #
# # num_list.reverse()
# # print(num_list)
# #
# # num_list.clear()
# # print(num_list)
#
# num_list = [5,2,4,3,1]
# mix_list=["조세호", 20, True]
# # print(mix_list)
#
# num_list.extend(mix_list)
# print(num_list)
#
# #사전
# #cabinet={3:"유재석", 100:"김태호"}
# #print(cabinet[3])
# #print(cabinet[100])
#
# #print(cabinet.get(3))
# #print(cabinet[5])
# # print(cabinet.get(5))
# # print(cabinet.get(5, "사용 가능"))
# # print("ih")
#
# #print(3 in cabinet)#True
# #print(5 cabinet) # False
#
# cabinet ={"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["b-100"])
#
# print(cabinet)
# cabinet["A-3"]="김종국"
# cabinet["C-20"]="조세호"
# print(cabinet)
#
# del cabinet["A-3"]
# print(cabinet)
#
# print(cabinet.keys())
#
# print(cabinet.values())
#
# print(cabinet.items())
#
# cabinet.clear()
# print(cabinet)
#
# #튜플
# menu=("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스")

# name="김종국"
# age=20
# hobby="코딩"
# print(name, age, hobby)
#
# name, age, hobby=("김종국", 20, "코딩")
# print(name, age, hobby)

#세트
# 집합(set)
# 중복 안됨, 순서 없음
# my_set={1,2,3,3,3}
# print(my_set)
#
# java={"유재석", "김태호", "양세형"}
# python=set(["유재석", "박명수"])

#교집합(java 와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

#합집합(java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

#차집합(java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

#phthon 할 줄 하는 사람이 늘어남
# python.add("김태호")
# print(python)

#java를 잊어버림
# java.remove("김태호")


#자료구조의 변경
# menu={"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu=list(menu)
# print(menu, type(menu))

#Quiz 4
# 당신은 학교에서 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
#  추첨 프로그램을 작성하시오.
#
# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2: 댁글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모튤의 shuffle 과 sample을 활용
#
# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --
#
# (활용 예제)
# from random import *
# lst = [1,2,3,4,5,]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# from random import *
# users = range(1, 21)#1부터 20까지 숫자생성
# #print(type(users))
# users=list(users)
# #print(type(users))
#
# print(users)
# shuffle(users)
# print(users)
#
# winners = sample(users, 4)#4명중에 1명은 치킨, 3명은 커피
#
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")

# if문
# weather = input("오늘 날씨는 어때요?")
# if weather=="비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없음")

# temp = int(input("기온은 어때요?"))
# if 30<= temp:
#     print("너무 더워요 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0<=temp and temp <10 :
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요 나가지 마세요")

#반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for waiting_no in range(1, 6):
#     print("대기번호: {0}".format(waiting_no))

# starbucks=["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#while
# customer ="토르"
# index=5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분되었습니다.")

# customer ="아이언맨"
# index =1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#
# customer ="토르"
# person = "Unknown"
#
# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

#continue와 break
# absent =[2, 5] #결석
# no_book=[7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#     print("{0}, 책을 읽어봐".format(student))

#한줄 for
# students =[1, 2, 3, 4, 5]
# print(students)
# students =[i+100 for i in students]
# print(students)

# students=["Iron man", "Thor", "I am groot"]
# students=[len(i) for i in students]
# print(students)

# students=["Iron man", "Thor", "I am groot"]
# students =[i.upper() for i in students]
# print(students)

#Quiz 5
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램
# 조건 1: 승객별 운행 소요 시간은 5분 ~ 10분 사이의 난수로 정해짐
# 조건 2: 당신은 소요 시간 5분 ~ 15분 사시의 승객만 매칭해야 함
#
# (출력문 예제)
# [0] 1번쨰 손님 (소요시간 : 15분)
# [ ] 2번쨰 손님 (소요시간 : 50분)
# [0] 3번쨰 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2분
#
# form random import *
# cnt =0 #총 탑승 승객 수
# for i in range(1, 51): #1~50이라는 수(승객)
#     time=randrange(5, 51)#5분 ~ 50분 소요 시간
#     if 5 <=time <=15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt +=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {0}분")

#함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()

#전달값과 반환값
# def open_account():
#      print("새로운 계좌가 생성되었습니다.")
#
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance+money
#
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
#
# def withdraw_night(balance, money):
#     commission =100
#     return  commission, balance-money-commission
#
# balance =0
# balance = deposit(balance, 1000)
# commission, balance=withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

#기본값
# def profile(name, age, main_lang):
#     print("이름: {0}\t 나이: {1}\t주 사용언어: {2}"\
#         .format_map(name, age, main_lang))
#
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬"):
#      print("이름: {0}\t 나이: {1}\t주 사용언어: {2}"\
#          .format(name, age, main_lang))
#
# profile("유재석")
# profile("김태호")

#키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
#
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t아니: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름: {0}\t아니: {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "kotlin", "Swift")

#지역변수와 전역변수
# gun =10
#
# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun 사용
#     gun =gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#
# def checkpoint_ret(gun, soldiers):
#     gun=gun-soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#
# print("전체 총: {0}".format(gun))
# # checkpoint(2)
# gun=checkpoint_ret(gun, 2)
# print("남은 총: {0}".format(gun))

#Quiz 6
# 표준 체중을 구하는 프로그램
# *표준 체중: 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21
#
# 조건1: 표준 체중은 별도의 함수 내에서 계산
#     *함수명: std_weight
#     *전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67,38kg 입니다.

# def std_weight(height, gender):
#     if gender =="남자":
#         return height*height*22
#     else:
#         return height*height*21
#
# height=175
# gender="남자"
# weigth=round(std_weight(height/100, gender), 2)
# print(" 키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weigth))


#구구단 7단 출력
# for i in range(1, 10):
#     print(f'7 x i = {7 * i}')
#구구단 1~9단 출력
# for dan in range(2, 10):
#     for i in range(1, 9+1):
#         print(f'{dan} x {i} = { dan * i}')
#     print('-' * 10)

#구구단 2~7단 출력
# for dan in range(2, 10):
#     for i in range(1, 9+1):
#         print(f'{dan} x {i} = { dan * i}')
#     print('-' * 10)
#     if dan == 7:
#         break
#구구단 2~7단을 출력하되 1, 3, 5, 7, 9인것만 출력하기
# for dan in range(2, 10):
#     for i in range(1, 9+1):
#         if i % 2 == 0: #i == 2 or i == 4 or i == 6 or i == 8:
#             continue
#         print(f'{dan} x {i} = { dan * i}')
#     print('-' * 10)
#     if dan == 7:
#         break

#클래스
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 멤버변수
# 레이스 : 공중 유닛, 비행기. 클로킨(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 메소드
# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\.format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
#

# 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
#
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         printf("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\.format(self.name, location, self.speed))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# 공격유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\.format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)
#
#     # 스림패 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp >10:
#             self.hp -= 10
#             print("{0} : 스림팩을 사용합니다. (HP 10 감소)".format(self.name)
#         else:
#             print("{0} : 체력이 부족하여 스림팩을 사용하지 않습니다.".format(self.name)))

# 탱크
# class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 놓은 파워로 공격 가능. 이동 불가
    # seize_developed = Flase # 시즈모드 개발여부
    #
    # def __init__(self):
    #     AttackUnit.__init__(self, "탱크", 150, 1, 35)
    #     self.set_seize_mode==False
    #
    # def set_seize_mode(self):
    #     if Tank.seize_developed == False:
    #         return

        # 현재 시즈몯가 아닐 떄 -> 시즈모드
#         if self.set_seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(slef.name))
#             self.damage /= 2
#             self.set_seize_mode = False
#
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중상속
#드랍쉽 : 공중 유닛, 수송기.마린 / 파이어뱃/ 탱크 등을 수송. 공격 불가
# 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self, name, location):
#         print("{0{ : {1} 방향으로 날아갑니다. [속도 {2}]"\.format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
#
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__("리이스", 80, 20, 5)
#             self.clocked = False # 클로킹 모드( 해제 상태)
#
#     def clocking(self):
#         if self.clocking == True:
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else: #클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 모드 설정ㅎ바니다.".format(self.name))
#             self.clocked = True

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# pass
# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         Unit.__init__(self, name, hp, 0)
#         #super
#         super().__init__(name, hp, 0)
#         self.location = location

# 서플라이 디폿 : 건물, 1개 건물=8유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     pass

# game_start()
# game_over()
#
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")
#
# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")
#
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         #super().__init__()
#     Unit.__init__(self)
#     Flyable.__init__(self)

# 드랍쉽
# dropship = FlyableUnit()

# 스타크래프트 프로젝트
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_over():
#     print("Player : gg") # good game
#     print("[plyer] 님이 게임에서 퇴장하셨습니다.")

# 게입 시작
# game_start()

# 마린 3기 생성
#     m1 = Marine()
#     m2 = Marine()
#     m3 = Marine()

# 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# 레이스 1기 생성성
# w1 = Wraith()

# 유닛 일괄 관리(생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스림팩, 탱크 : 시스모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith)
#         unit.clocking()

# 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21))  #공격은 랜덤으로 발음 (5 ~ 20)
 # 게임 종료
# game_over()

# Quiz 8) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년
#  [코드]
# class House:
#     def __init__(self, location, house_type, deal_type, price. completion_year):
#         self.cloation = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
        # self.completion_tear = completion_year

    # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type\, slef.price, slef.completion_year)
#
# house = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", " 오피스텔", "전세", " 5억", " 2007년")
# house2 = House("송파", "빌라", "월세", "500/50", "2000년")
#
# house.append(house1)
# house.append(house2)
# house.append(house3)
#
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()


#모듈
import theater_module
theater_module.price(3) #3명 영화 가격
theater_module.price_morning(4) #4명 조조할인 영화 가격
theater_module.price_soldier(5) # 5명 군인 영화 가격

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7) #사용 불가
#
# from theater_modlue improt price_soldier as price
# price(5)

# #모듈 직접 실행
# if __name__ ==  "__main__":
#     print("Thailand 모듈을 직접 실행")
#     print("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
#     trip_to = ThailandPackage()
#     trip_to.detail()
# else:
#     print("Thailand 외부에서 모듈 호출")

# #패키지
import travel_.thailand
#import travel.thailand.ThailandPackeage - 사용 불가
trip_to = travel_.thailand.ThailandPackage()
trip_to.detail()

from travel_.thailand improt ThailandPackeage
trip_to = ThailandPackeage()
trip_to.detail()

from travel_ import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

#__all__
from travel_ improt *
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackeage()
trip_to.datail()

#패키지, 모듈 위치
improt inspect
improt random
print(inspect.getfile(random))
print(inspect.getfile(thailand))



