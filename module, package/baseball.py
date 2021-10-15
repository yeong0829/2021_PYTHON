from baseball_game_engine import make_quiz, check
from custom_error import IncalidCountError
answer = make_quiz()
count = 0
def save_history(player, count):
    with open('baseball_history.txt', 'a') as f:
       f.write(f'{player}\t{count}\n')

def load_history():
    count_list = []
    with open('baseball_histor.txt', 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            #print(line.rstrip())
            line_data = line.rstrip().split('\t')
            count_list.append(line_data[1])
    #중복제거
    count_list = set(count_list)
    count_list = list(count_list)
    count_list.sort()
    return count_list[:3]


print(answer)
while True:
    #숫자3자리 중복없이 묻기
    player = input("숫자 세자리는?(t: top3)")
    if player == 't':
        history = load_history()
        print(history)
        continue
    try:
        player_int = int(player)
    except: # except ValueError:
        continue
    #길이가 3이 아닐떄 에러 처리
    if len(player) != len(answer):
       #raise IncalidCountError("3자리가 아닙니다.")
        print(f'입력한 숫자의 개수가 정답과 다름니다.: {len(answer)}글자')
        continue
    #strike, ball 확인하기
    count += 1
    strike, ball = check(answer, player)
    #출력하기
    print(f'{player}\tstrike: {strike}\t ball: {ball}\t{count}try')
    #strike가 3일 때 나가기
    if strike == 3:
        #저장하기
        save_history(player, count)
        break