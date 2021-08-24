class Hairstyle:
    _HAIRSTYLE = ('컷트', '매직', '파마', '염색')
    _PRICE = ['10000', '20000', '30000', '40000']

    def __init__(self):
        self.style = 0
        self.price = 0
        self.select_designer = ''
        self.my_style = ''

    def set_style(self):
        for index, style in enumerate(Hairstyle._HAIRSTYLE):  # 스타일 종류 보여주자
            print(index+1, style)
            price = Hairstyle._PRICE[index]
        style = input('원하는 헤어스타일을 선택하세요: ')
        self.style = int(style)

    def set_designer(self):
        select_designer = input('원하는 디자이너를 입력하세요: ')
        self.select_designer = '입력된 정보가 없습니다' if select_designer == '' else select_designer

    def set_mystyle(self):
        my_style = input('현재 자신의 헤어스타일을 입력하세요: ')
        self.my_style = '입력된 정보가 없습니다' if my_style == '' else my_style

    def __str__(self):
        return '-' * 10 + '주문확인' + '-' * 10 + f'\n디자이너: {self.select_designer}\n자신의 헤어스타일: {self.my_style}\n원하는 헤어스타일: {Hairstyle._HAIRSTYLE[self.style-1]}'\
                                                f'가격: {self.price}'



def set_hairstyle(self):
        self.set_style()
        self.set_designer()
        self.set_mystyle()
        print(self)