from recipe import Recipe
class Recipebook:
    def __init__(self):
        self.recipe_list = []
        self.food_court()

    def add_recipe(self):
        # 추가할 레시피 이름 입력
        recipe_name = input('>> 레시피 이름 입력: ')

        # 중복 체크
        for recipe in self.recipe_list:
        # 중복되는 레시피가 있으면
            if recipe_name == recipe.name:
            # 있다고 알려주기
                print('이미 존재하는 레시피')
                return
        # 중복되는 레시피가 없으면
        # 새 레시피 생성
        new_recipe = Recipe(recipe_name)
        new_recipe.set_recipe()
        # 레시피리스트에 추가
        self.recipe_list.append(new_recipe)

    def show_all_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index+1}번.')
            print(recipe)

    def search_recipe(self):
        # 음식 이름 입력 받기
        recipe_name = input('>> 원하는 레시피 검색: ')
        searched_recipe = []
        # (반복문시작) 레시피 리스트를 돌면서 레시피가 있는지 확인
        for recipe in self.recipe_list:
            # 찾는 레시피가 이름이 있으면
            if recipe_name in recipe.name: # if '부대' in '부대찌개" -> 찾을 수 있음
                # 레시피 보여주기
                print(recipe)
                searched_recipe.append(recipe)
        # (반복문종료)
        # 찾는 레시피 이름이 없다면
        if len(searched_recipe) == 0:  # 못찾음
            # 레시피 추가할지 물어보기
            choice = input('>> 원하는 레시피가 없을 시 추가하시겠습니까?(1: YES/ 0: NO): ')
            # 추가 선택시
            if choice == '1':
                #추가
                self.add_recipe()
            # 추가 안하면
            else:
                # 끝
                return

    def search_whatin(self):
        # 모든 재료 다 보여주기
        # set: 수학의 집합과 같은 개념/ 비순차적으로 저장하는 순열 자료구조/수정 가능/순서태로 데이터 리던x/중복 제거
        whatin_set = set()  # (재료세트)빈 세트 생성
        for recipe in self.recipe_list:
            for whatin in recipe.whatin:
                whatin_set.add(whatin)  # {'김치', '두부', '감자', '두부'} -> {"두부', '김치', 감자'}
        # 모든 재료 다 보여주기
        print('다음 재료를 사용하세요.')
        for index, whatin in enumerate(whatin_set):
            print(f'{index + 1}. {whatin}')

        # 보여준 재료 중 사용할 재료 선택
        num = int(input('>> 사용할 재료 번호 입력:'))
        use_whatin = list(whatin_set)[num - 1]
        # 고른 재료가 포함된 레시피 보여줌``
        for recipe in self.recipe_list:
            if use_whatin in recipe.whatin:     #딕셔너리는 키값으로 찾음
                print(recipe)

    def food_sourt(self):
        지원이 = Recipe('케이크')
        지원이.quantity = 1
        지원이.link = 'yourbe.com'
        지원이.whatin = {'밀가루': '500', '계란': '100', '생크림': '200', '딸기': '300'}
        지원이.into = '맛있게 만드세요'
        지원이.time = 60
        self.recipe_list.append(지원이)
        서연이. = Recipe('삼겹살김치볶음밥')
        서연이.quantity = 4
        서연이.link=' '
        서연이.whatin = {'삼겹살': '500', '김치': '100', '밥': '400'}
        self.recipe_list.append(서연이)

    def __str__(self):
        pass