from hairstyle import Hairstyle

def print_menu():
    print('1. 미용실 예약') # 미용실 선택, 디자이너 선택, 현재 머리스타일 선택, 예약 시간, 가격
    print('2. 스타일 선택') # 현재 머리스타일, 원하는 머리스타일 선택, 예약 시간, 가격
    print('3. 종료하기')
    num = input('메뉴를 선택하세요: ')
    return num

def main():
    Hairshop_204 = Hairstyle()
    while True:
        num = print_menu()
        if num == '1':
            # 미용실 예약
            Hairshop_204.order()
        elif num == '2':
            # 스타일 선택
            Hairshop_204.set_hairstyle()
        elif num == '3':
            break
        else:
            print('다시 입력하세요.')

main()