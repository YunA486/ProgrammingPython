class Icecream:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor
        # 이름: name, 맛: flavor, 설명:description

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f'이름 : {self.name}\t맛 : {self.flavor}'

# 바람과함께사라지다 = Icecream('바람과함께사라지다', '블루베리, 딸기, 치즈케잌')
# 바람과함께사라지다.set_description('블루베리와 딸기로 상큼함을 더한 치즈케이크 한 조각')
# print(바람과함께사라지다)
# print(바람과함께사라지다.description)
#
# 초코나무숲 = Icecream('초코나무숲', '초코, 녹차')
# print(초코나무숲)
#
# 뉴욕치즈케이크 = Icecream('뉴욕치즈케이크', '치즈, 치즈케이크')
# print(뉴욕치즈케이크)

class Cup:
    _CUP_CATEGORIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]

    # CUP._CUP_CATOGORIES[self.count_flavor-1]
    def __init__(self, name, count_flavor):
        self.name = name
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor - 1]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        바람과함께사라지다 = Icecream('바람과함께사라지다', '블루베리, 딸기, 치즈케잌')
        바람과함께사라지다.set_description('블루베리와 딸기로 상큼함을 더한 치즈케이크 한 조각')

        초코나무숲 = Icecream('초코나무숲', '초코, 녹차')

        뉴욕치즈케이크 = Icecream('뉴욕치즈케이크', '치즈, 치즈케이크')

        self.menu.append(바람과함께사라지다)
        self.menu.append(초코나무숲)
        self.menu.append(뉴욕치즈케이크)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index+1, icecream)

    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()                        # 메뉴 보여주기
            flavor = input('맛을 고르세요 : ')        # 사용자 선택
            flavor = int(flavor)                    # 인덱스를 위해 문자 -> 숫자
            icecream = self.menu[flavor - 1]        # 메뉴에서 인덱스로 가져오자
            self.order_menu.append(icecream)        # 주문한 메뉴에 추가하자

        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu:            # 주문내역 보여주자
            print(icecream)

    def __str__(self):
        return f'이름 : {self.name}\t가격 : {self.price}원\t종류 : {Cup._CUP_CATEGORIES[self.count_flavor - 1]}'


윤아꺼 = Cup('더블컵', 2)
print(윤아꺼)
윤아꺼.order()