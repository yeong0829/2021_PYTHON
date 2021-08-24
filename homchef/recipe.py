class Recipe:
    def __init__(self, name):
        # 재료
        self.whatin = {}
        # 딕셔너리(Ditionary): key-value 형태의 값으로 가료를 저장할 수 있는 구조로 key값을 통해 value값을 찾음
        # 이름
        self.name = name
        # 시간
        self.time = ''
        # 영상 주소
        self.link = ''
        # 설명
        self.info = ''
        # 인분 설정
        self.quantity = 1

    def set_link(self):
        link = input('>> 레시피 영상 주소 입력: ')
        self.link = '입력된 주소가 없음' if link == '' else link

    def set_info(self):
        info = input('>> 레시피 정보 입력: ')
        self.info = '입력딘 주소가 없음' if info == '' else info

    def set_quantity(self):
        quantity = input('>> 레시피 몇 인분인가?: ')
        self.quantity = 1 if quantity == '' else quantity

    def set_time(self):
        time = input('>> 레시피 소요 시간 입력: ')
        self.time = 0 if time == '' else time

    def set_whatin(self):
        while True:
            whatin = input('>> 재료 입력(ex: 감자 100)(입력이 끝나면 엔터): ')
            if whatin == '':
                break
            name, gram = whatin.split(' ')
            self.whatin[name] = gram + 'g'

    def set_recipe(self):
        self.set_link()
        self.set_whatin()
        self.set_time()
        self.set_info()
        self.set_quantity()

    def __str__(self):
        return f'레시피: {self.name}\n양: {self.quantity}\t인분\n정보: {self.info}\n링크: {self.link}\n'  \
               f'재료: {self.whatin}\n시간: {self.time}'


