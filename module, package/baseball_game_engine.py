import random
# 숫자야구게임
# 퀴즈내기 - 숫자 3자리 중복없이

# 무한반복
# 숫자 3자리 중복 없이 묻자
#  strike, ball 확인하기
# 출력
# strik가 3일 떄 나가기
def make_quiz():
    list_r = random.sample(range(1, 10), 3)
    str_number = "".join(map(str, list_r))
    return str_number

def check(answer, player):
    strike = 0
    ball = 0
    #번호가 있고, 자리가 같으면 strike +=1
    for i, p in enumerate(player):
        for j, a in enumerate(answer):
            if p == a:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    #번호가 있고, 자리가 다르면 ball +=1
    # for i in range(0, 3):
    #     for j in range(0, 3):
    #         if (player[i] == answer[j] and i == j):
    #             strike += 1
    #         elif (player[i] == answer[j] and i != j):
    #             ball += 1
    return strike, ball

if __name__ == '__main__':
    answer = make_quiz()
    print(answer)
    strike, ball = check("238", "241")
    print(strike, ball )  #1 0
    strike, ball = check("381","182")
    print(strike, ball)  #1 1