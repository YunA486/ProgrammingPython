from recipe import Recipe

class Recipebook:

    def __init__(self):
        self.recipe_list = []
        self.food_court()

    def add_recipe(self):
        # 추가할 레시피 이름 입력 받기
        recipe_name = input(">> 레시피 이름을 입력하세요 : ")
        # 중복 체크
        for recipe in self.recipe_list:
            # 중복되는 레시피가 있으면
            if recipe_name == recipe.name:
                # 이미 있다고 알려주기
                print("이미 존재하는 레시피입니다.")
                return

        # 중복되는 레시피가 없으면
        # 새 레시피 생성하기
        new_recipe = Recipe(recipe_name)
        new_recipe.set_recipe()
        # 레시피리스트에 추가
        self.recipe_list.append(new_recipe)

    def show_all_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'\n{index + 1}번')
            print(recipe)

    def search_recipe(self):
        # 찾을 레시피 이름 입력 받기
        recipe_name = input(">> 원하는 레시피를 입력하세요 : ")
        searched_recipe = []
        # (반복문시작) 레시피 리스트를 돌면서 레시피 있는지 확인
        for recipe in self.recipe_list:
            # 찾는 레시피 이름이 있다면
            if recipe_name in recipe.name:  # if '부대' in '부대찌개' -> 찾을 수 있음
               # 레시피 출력
                print(recipe)
                searched_recipe.append(recipe)
        # (반복문 종료)
        # 찾는 레시피 이름이 없다면
        if len(searched_recipe) == 0:   # 못 찾음
            # 추가 할지 물어보기
            choice = input(">> 원하는 레시피가 없습니다. 추가하시겠습니까? (1 : 예, 0 : 아니오)")
            # 추가 한다고 하면
            if choice == '1':
                # 레시피 추가하기
                self.add_recipe()
            # 추가 안 한다고 하면
            else:
                # 끝
                return

    def search_whatin(self):

        # (재료세트) 빈 세트 생성
        whatin_set = set()
        for recipe in self.recipe_list:
            for whatin in recipe.whatin:
                whatin_set.add(whatin)     # {'김치', '두부', '감자'}.add('두부') -> {'두부', '김치', '감자'}

        # 모든 재료 다 보여주기
        print("다음 재료를 사욯해보세요! ")
        for index, whatin in enumerate(whatin_set):
            print(f'{index + 1}.{whatin}')

        # 재료 중에 사용할 재료 고르기
        num = int(input(">> 사용할 재료 번호를 입력하세요 : "))
        use_whatin = list(whatin_set)[num-1]

        # 고른 재료가 포함되는 레시피를 다 보여주자
        for recipe in self.recipe_list:
            if use_whatin in recipe.whatin:     # 딕셔너리는 키값으로 찾는다.
                print(recipe)

    def food_court(self):
        윤아 = Recipe('마라탕')
        윤아.quantity = 1
        윤아.link = 'youtube.com'
        윤아.whatin = {'숙주 나물':'200', "청경채":'100', "고기":"300"}
        윤아.info = '맛있게 만드세요!'
        윤아.time = 30
        self.recipe_list.append(윤아)

        서연 = Recipe('삼겹살김치볶음밥')
        서연.quantity = 4
        서연.link = ''
        서연.whatin = {'삼겹살':'500', '김치':'100', '밥':'400'}
        self.recipe_list.append(서연)

    def __str__(self):
        pass