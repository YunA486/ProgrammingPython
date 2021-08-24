class Recipe:
    def __init__(self, name):
        # 이름
        self.name = name
        # 재료
        self.whatin = {}
        # 시간
        self.time = ''
        # 영상 주소
        self.link = ''
        # 설명
        self.info = ''
        # 몇 인분인지
        self.quantity = 1
        pass

    def set_time(self):
        time = input(">> 레시피가 소요시간을 입력하세요 : ")
        self.time = 0 if time == '' else time

    def set_link(self):
        link = input('>> 레시피영상 주소를 입력하세요 : ')
        self.link = "입력된 주소가 없습니다." if link == '' else link

    def set_info(self):
        info = input(">> 레시피 정보를 입력하세요 : ")
        self.info = "입력된 종류가 없습니다." if info == '' else info

    def set_quantity(self):
        quantity = input(">> 레시피가 몇 인분 기준인지 입력하세요 : ")
        self.quantity = 1 if quantity == '' else quantity

    def set_whatin(self):
        while True:
            whatin = input(">> 재료를 입력하세요(예시 : 감자 100) : (입력이 끝나면 엔터를 치세요.)")
            if whatin == '':
                break
            name, gram = whatin.split()
            self.whatin[name] = gram + 'g'

    def set_recipe(self):
        self.set_link()
        self.set_whatin()
        self.set_time()
        self.set_info()
        self.set_quantity()

    def __str__(self):
        return f'레시피 : {self.name}\n양 : {self.quantity}인분\n정보 : {self.info}\n링크 : {self.link}\n재료 : {self.whatin}\n시간 : {self.time}'
    
# 김치찌개 = Recipe('김치찌개')
# 김치찌개.set_whatin()
# 김치찌개.set_info()
# 김치찌개.set_time()
# 김치찌개.set_link()
# 김치찌개.set_quantity()
# print(김치찌개)

