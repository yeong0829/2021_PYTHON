# 파일 저장
with open('my_fayorite_music.txt', 'w', encoding='utf-8') as f:
    f.write('이선우: 너를 생각해(경서)\n')
    f.write('주서영: 낙하(신봉선)\n')

# 파일 불러오기
with open('my_fayorite_music.text', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        #이름: 이선우[Tab]좋아하는 음악: 너를 생각해(경서)
        line_list = line.split(':')
        name = line_list[0]
        music = line_list[1].rstrip()
        print(f'이름: {name}\t좋아하는 음악: {music}')
        # print(line.rstrip())