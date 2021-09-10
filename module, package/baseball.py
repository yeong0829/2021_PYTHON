answer = make_quiz()
print(answer)

while True:
    player = input("숫자 세자리는? ")
    strike, ball = check(answer, player)
    print(f'{player}\tstrike: {strike}\tball: {ball}')
    if strike == 3:
        break

print('🤗축하합니다🤗')