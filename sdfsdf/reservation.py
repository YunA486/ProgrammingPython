class Hairshop:
    _HAIRSTYLE = ('컷트', '매직', '파마', '염색')
    _PRICE = (10000, 20000, 30000, 40000)
    _TIME = ('10:00', '12:00', '14:00', '16:00', '18:00', '20:00')

    def __init__(self):
        self.style = 0
        self.price = 0
        self.select_designer = ''
        self.my_style = ''

    def set_hairshop(self):
        select_hairshop = input('원하는 미용실을 입력하세요 : ')
        self.select_hairshop = '입력된 정보가 없습니다' if select_hairshop == '' else select_hairshop

    def set_style(self):
        for index, style in enumerate(Hairshop._HAIRSTYLE):  # 스타일 종류 보여주자
            price = Hairshop._PRICE[index]
            print(f'{index + 1}: {style}\t{price}원')
        style = input('원하는 헤어스타일을 선택하세요: ')

    def set_designer(self):
        select_designer = input('원하는 디자이너를 입력하세요: ')
        self.select_designer = '입력된 정보가 없습니다' if select_designer == '' else select_designer

    def set_mystyle(self):
        my_style = input('현재 자신의 헤어스타일을 입력하세요: ')
        self.my_style = '입력된 정보가 없습니다' if my_style == '' else my_style

    def set_time(self):
        for index, time in enumerate(Hairshop._TIME):
            print(f'{index + 1} : {time}')
        time = input('원하는 시간대를 선택하세요: ')

    def __str__(self):
        return '-' * 10 + '주문확인' + '-' * 10 + f'\n디자이너: {self.select_designer}\n자신의 헤어스타일: {self.my_style}\n원하는 헤어스타일: {Hairshop._HAIRSTYLE[self.style]}' \
                                              f'\n가격: {Hairshop._PRICE[self.price]}\n예약시간: {Hairshop._TIME[self.set_time()]}' + '-' * 26

    def set_hair_shop(self):
        self.set_hairshop()
        self.set_style()
        self.set_designer()
        self.set_mystyle()
        self.set_time()
        print(self)