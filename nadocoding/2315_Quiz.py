#Quiz 1-1
# 주민등록번호 앞 6자리를 변수 id_number에 넣고,
# 출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
# 예시
# id_number = 020316 일 때
# 출력 예시
# 02
# 0316
# 632
# id_number = '020316'
# a=id_number[0:2]
# b=id_number[2:6]
# print(a)#[0:2], [:2], [-6: -4]
# print(b)#[2:6],[2:], [-4:]
# print(int(a)*int(b))

#Quiz 1-2
# 집전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기
# 예시
# phone_number = 02-1234-5678 또는 032-9876-4321
# 출력 예시
# 02			또는		032
# 5678		또는		4321
# phone_number = '02-1234-5678'
# x=phone_number.index('-')     #index() 없으면 ValueError , find() 없으면 -1
# print(phone_number[0:x]) #[:2]
# print(phone_number[8:12]) #[8:]
#
# phone_number2 = '032-9876-4321'
# x=phone_number2.index('-')
# print(phone_number2[0:x])#[:3]
# print(phone_number2[9:13]) #[9:]

# 전화번호 입력시, -가 있든, 없든, 잘 알아먹기
# phone_nubmer1='010-1234-5678'
# phone_nubmer2='01087654321'
# phone_nubmer3='010 1111 2222'
# phone_number= phone_number3
#result= phone_nubmer3.creplae('-', '').replace(' ', '')
# print(result)

# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

# student_number = '2400'
# number=student_number[1]
# if number=='1':
#     print("1반 뉴미디어소프트웨어과")
# elif number=='2':
#     print("2반 뉴미디어소프트웨어과")
# elif number=='3':
#     print("3반 뉴미디어웹솔루션과")
# elif number=='4':
#     print("4반 뉴미디어웹솔루션과")
# elif number == '5':
#     print("5반 뉴미디어디자인과")
# elif number == '6':
#     print("6반 뉴미디어디자인과")
# else :
#     print("잘못 입력했습니다.")

# number = '2600'
# number=int(number)
# number=student_number[1]
# if number=='1':
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif number=='2':
#     print(f"{number}반 뉴미디어소프트웨어과")
# elif number=='3':
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif number=='4':
#     print(f"{number}반 뉴미디어웹솔루션과")
# elif number == '5':
#     print(f"{number}반 뉴미디어디자인과")
# elif number == '6':
#     print(f"{number}반 뉴미디어디자인과")
# else :
#     print("잘못 입력했습니다.")

# majors=['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', "뉴미디어웹솔루션과", "뉴미디어웹솔루션과", "뉴미디어디자인과", "뉴미디어디자인과"]
# print(f'{number}반 {majors[number-1]}')

# majors=['뉴미디어소프트웨어과', "뉴미디어웹솔루션과", "뉴미디어디자인과"]
# if 1<= number <= 6:
#     print(f'{number}반 {majors[(number-1)//2]}')
# else:
#     print("잘못 입력했습니다.")


# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를
# 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2

# def get_major(number):
#     global major
#     grade=number[0]
#
#     number=number[1]
#     if number == '1' or number =='2':
#         major = "뉴미디어소프트웨어과"
#     elif number == '3' or number =='4':
#         major = "뉴미디어웹솔루션과"
#     elif number == '5' or number =='6':
#         major = "뉴미디어디자인과"
#     return  major, grade
#
# major, grade= get_major('1200')
# print(major, grade)


# Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고,
# 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

# def average(*number):
#     sum_value= 0
#     for i in number:
#         sum_value += i
#     return sum_value/len(number)
#
# print(average(4, 23))
#
# def acerage(*numbers):
#     return sum(numbers) / len(numbers)
#
# print(average(10, 20, 30))


# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를
# 리턴하는 함수 만들기(소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만
#
# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

# def get_bmi(height, weight):
#     #height /= 100
#     bim = round((weight/ (height**2))*10000, 1)
#     return bim
#
# bmi = get_bmi(176, 69)
# print(bmi)
#
# if bmi < 18.5:
#     print('저체중')
# elif bmi < 23:
#     print('정상')
# elif bmi < 25:
#     print('과체중')
# elif 25 <= bmi:
#     print('비만')


'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면리턴한다,
각 자리의 숫자의 합계를 . 10자리 이상이면 -1 리턴한다.
'''
# def n_sum(argument):
#     if (10 > argument):
#         return argument
#     elif (10 <= len(str(argument))):
#         return -1
#     argument = map(int, list(str(argument)))        #a: 408  str(a): '408'   list(str(a)): ['4' , '0' , '8']  map(list(str(a))): [4, 0, 8]
#     return sum(argument)
#
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1


# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원

# def get_subway_fare(km):
#     money = 720
#     if 10 > km:
#        return money
#     elif 50 > km:
#         km -= 10
#         q = km // 5
#         money += q * 100
#         r = km % 5
#         if r > 0:
#             money += 100
#         return money
#     else:
#         km -= 50
#         money = 720 + (50-10)//5*100
#         q = km // 8
#         money += q *100
#         r = km % 8
#         if r > 0:
#             money += 100
#         return money
#
#
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720



# Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음

# def get_three_six_nine(number):
#     number = str(number)
#     count_369 = 0
#     for i in number:
#         if(i == '3') or (i == '6') or (i == '9'):
#             count_369 += 1
#     if count_369 == 0:
#         return number
#     else:
#         return count_369 *'짝'

    # n1 = number / 10
    # n2 = number % 10
    # count_369 = 0
    # if n1 != '0' or n1 % 3 == '0':
    #     count_369 += 1
    # if n2 != '0' or n2 % 3 == '0':
    #     count_369 += 1
    #
    # if count_369 == '1':
    #     return "짝"
    # elif count_369 == '2':
    #     return "짝짝"
    # else:
    #     return number

# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝
#
#
# Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
# 1. 함수의 이름을 정해준다.
# 2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
# 3. 리턴하는 것을 말해준다.
# 4. 출력 예시를 보여준다.
# 5. 내가 낸 문제의 답안을 제출한다.

# 계산기 만들기
# 함수이름 a _calculator(숫자 2개 입력받기)
# def a_count(n1, n2):
#     result = n1 + n2
#     print(n1, "+", n2, "=",  result)
#     result = n1 - n2
#     print(n1, "-", n2, "=", result)
#     result = n1 * n2
#     print(n1, "*", n2, "=", result)
#     result = n1 / n2
#     print(n1, "/", n2, "=", result)
#
# result = a_count(6, 2)


# Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
#
# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return '소수 아님'
#     return '소수'
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님


# Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
# '고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
#
# def get_compliment(word):
#     if '고구마' in word:
#         return '왓쇼이!'
#     elif '맛있는' in word:
#         return '우마이!'
#     elif '놀랄 만한' in word:
#         return '요모야..!'
#     elif '황당한' in word:
#         return '요모야..!'
#     elif '굉장한' in word:
#         return '요모야..!'
#     else:
#         return '으무!'
#
#
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!




#Quiz5-1. 모듈이란?
#    모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일로 다른 파이썬 프로그램을 불러와 사용할 수 있게끔 만든 파일이다.
#       파이썬 프로그램을 할 때 많은 모듈을 사용하는데 다른 사람이 이미 만들어 놓은 모듈을 사용할 수도 있고 직접 만들어서 사용할 수도 있다.


#Quiz5-2. 패키지란?
#    여러 개의 디렉토리와 모듈을 계단 형식으로 구조화하여 모아 놓은 것으로 모듈들을 넣어 놓은 디렉토리명이 패키지명이다.


#Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
#import theater_module as p
#p.price(3)
#p.price_morning(4)
#p.price_soldier(5)



#Quiz5-4. __all__의 역할은?
#    특정 디렉토리의 모듈을 *를 이용하여 improt할 때에 __all__이라는 변수를 설정하고 import할 수 있는 모듈을 정의할 때 __all__로 정의하지 않으면 인식되지 않는다.


#Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
#   if __name__ == '__main__':


#Quiz5-6.  패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
#import travel.vietnam
#< 가 >
#trip_to = travel.vietnam.VietnamPackage()
#trip_to.detail()

#from travel import vietnam
#< 나 >
#trip_to = vietnam.VietnamPackage()
#trip_to.datail()


#from travel.vietnam import
#< 다 >
#trip_to = VietnamPackage()
#trip_to.detail()
