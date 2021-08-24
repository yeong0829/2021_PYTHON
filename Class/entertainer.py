class Entertainer:
    def __int__(self, name):
        self.name = name

    def set_height(self, height):  #키
        self.height = height

    def set_face(self, face):  #얼굴
        self.face = face

    def set_kind(self, kind):  #인성
        self.kind = kind

    def set_name(self, name):  #이름
        self.name = name

    # def info(self):
    #     print(f'이름: {self.name},\t키: {self.height},\t얼굴: {self.face}\t인성: {self.kind}')

    def __str__(self):
        return f'이름: {self.name},\t키: {self.height},\t얼굴: {self.face}\t인성: {self.kind}'

아이유 = Entertainer()
아이유.set_name('이지은')
아이유.set_height('159cm')
아이유.set_face('형섭샘이상형')
아이유.set_kind('That\'s very good.')
print(아이유)

class Singer(Entertainer):
    def __init__(self, name, song):
        # self.name = name
        super().__init__(name)
        self.song = song

    def __str__(self):
        return f'이름: {self.name},\t키: {self.height},\t얼굴: {self.face}\t인성: {self.kind}\t대표곡: {self.song}'

    def __str__(self):
        return super().__str__() + f'\t대표곡: {self.song}'

# 강다니엘 = Singer('강다니엘', '깨워')
# 강다니엘.set_height("181cm")
# 강다니엘.set_face("댕댕이")
# 강다니엘.set_kind("very good")
# print("강다니엘")

class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'

# 최우식 = Talent('최우식', '기생충')
# 최우식.set_height('모름')
# 최우식.set_face('귀엽')
# 최우식.set_kind('쏘쏘')
# print(최우식)


V = Singer('V', 'Love Maze')
V.set_height('179cm')
V.set_face('진이지 이상형')
V.set_kind('That\'s very good and cute.')
print(V)

RM = Singer('RM', 'Answer: love myself')
RM.set_height('179cm')
RM.set_face('쏘쏘')
RM.set_kind('자기철학이 있어보임')
print(RM)

방탄소년단 = []
방탄소년단.append(뷔)
방탄소년단.append(RM)
print(방탄소년단)

