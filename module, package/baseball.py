from baseball_game_engine import make_quiz, check
from custom_error import IncalidCountError
answer = make_quiz()

while True:
    #숫자3자리 중복없이 묻기
    player = input("숫자 세자리는?")
    try:
        player_int = int(player)
    except: # except ValueError:
        continue
    #길이가 3이 아닐떄 에러 처리
    if len(player) != 3:
        raise IncalidCountError("3자리가 아닙니다.")
    #strike, ball 확인하기
    strike, ball = check(answer, player)
    #출력하기
    print(f'{player}\tstrike: {strike}\t ball: {ball}')
    #strike가 3일 때 나가기
    if strike == 3:
        break