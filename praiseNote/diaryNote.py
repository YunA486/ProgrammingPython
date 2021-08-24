from diary import Diary
from time import sleep

class DiaryNote:

    def __init__(self):
        self.diary_list = []
        self.my_diary()

    def write(self):
        # 추가할 일기 날짜 입력 받기
        print("\n╭────────────✎")
        print("| 날짜 중복검사")
        diary_date = input("╰─▗ ▘➤ ")
        # 중복 체크
        for diary in self.diary_list:
            # 중복되는 날짜가 있으면
            if diary_date == diary.date:
                # 이미 있다고 알려주기
                print("\n╭─────────── °• ੈ♡₊˚•.")
                print("| 이미 존재하는 날짜입니다.")
                print("╰")
                return

        # 중복되는 날짜가 없으면
        # 새 일기 생성하기
        new_diary = Diary(diary_date)
        new_diary.set_diary()
        # 다이어리 리스트에 추가
        self.diary_list.append(new_diary)

    def loading(self):
        # 찾을 일기 날짜 입력 받기
        print("\n╭─────────────✎")
        print("| 찾을 날짜 입력")
        diary_date = input("╰─▗ ▘➤ ")
        searched_diary = []
        # (반복문시작) 다이어리 리스트를 돌면서 해당 날짜가 있는지 확인
        for diary in self.diary_list:
            # 찾는 날짜가 있다면
            if diary_date in diary.date:  # if '06' in '06.11' -> 찾을 수 있음
               # 다이어리 출력
               print()
               print(diary)
               sleep(2)
               searched_diary.append(diary)

        # (반복문 종료)
        # 찾는 날짜가 없다면
        if len(searched_diary) == 0:   # 못 찾음
            # 추가 할지 물어보기
            print("\n╭───────────────────── °• ੈ♡₊˚•.")
            print("| 찾는 날짜가 없습니다.")
            print("| 작성하시겠습니까?")
            print("| 1 : 예 0 : 아니오")
            choice = input("╰──✎ ")
            # 작성 한다고 하면
            if choice == '1':
                # 일기 추가하기
                print("\n★。＼｜／。★")
                print(" 일기 작성")
                self.write()
            # 작성 안 한다고 하면
            else:
                # 끝
                print("\n⋆ 。゜☁︎ 。⋆ 。゜☾゜。⋆")
                print("    메뉴로 돌아갑니다.   ")
                print("⋆ 。゜☁︎ 。⋆ 。゜☾゜。⋆")
                sleep(1)



    def revise(self):

        print("\n╭─────────────────────────✎")
        print("| 수정할 일기의 날짜를 입력하세요.")
        print("| 잘못 된 날짜 입력 시 메뉴로 돌아갑니다.")
        search_revise = input("╰─▗ ▘➤ ")
        for index, diary in enumerate(self.diary_list):
        # 중복되는 날짜가 있으면
            while True:
                if search_revise == diary.date:
                    print()
                    print(diary)
                    sleep(1)
                    print("\n┌─────────────────────────────┐")
                    print("│     위 일기를 수정하시겠습니까?   │")
                    print("│       1 : 예 2 : 아니오        │")
                    print("└───────────── ∧ ∧────────────┘")
                    print("　           (´･ω･ ∩")
                    print("　           o.　　 ,ﾉ.")
                    print("　           Ｏ＿ .ﾉ")
                    print("　            (ノ")
                    print("　            :｜|")
                    print("　            ━━")
                    select = input(">> ")
                    select = int(select)

                    if (select == 1):  # 선택이 1일 경우 빈 문자를 저장한 후 리턴
                        diary.update_write(diary.write)
                        print("              수정이 완료되었습니다.")
                        break
                    elif (select == 2):
                        print("\n⋆ 。゜☁︎ 。⋆ 。゜☾゜。⋆")
                        print("    메뉴로 돌아갑니다.   ")
                        print("⋆ 。゜☁︎ 。⋆ 。゜☾゜。⋆")
                        sleep(1)
                        break
                    else:
                        print("┏/\_/\━━━━━━━━━━━━━┓")
                        print("(='_' )다시 입력하세요. ")
                        print("""(, (") (")━━━━━━━━━┛""")
                        sleep(1)
                else:
                    break

    def delete(self):
        print("\n╭───────────────────────────────✎")
        print("| 삭제할 일기의 날짜를 입력하세요.")
        print("| 잘못 된 날짜 입력 시 메뉴로 돌아갑니다.")
        search_delete = input("╰─▗ ▘➤ ")

        for index, diary in enumerate(self.diary_list):
        # 중복되는 날짜가 있으면
            while True:
                if search_delete == diary.date:
                    print("\n┌─────────────────────────────┐")
                    print("│   일기 삭제 : 1 돌아가기 : 2   │")
                    print("└────────────∩───∩───────────┘")
                    print("　           (`･ω･´)")
                    select = input(">> ")
                    select = int(select)

                    if(select == 1):  # 선택이 1일 경우 빈 문자를 저장한 후 리턴
                        del self.diary_list[index]
                        print("┌┄┄┄┄◦◡◦┄┄┄◦◡◦┄┄┄┄┐")
                        print("  일기가 삭제되었습니다.  ")
                        break
                    elif(select == 2):
                        print("\n⋆ 。゜☁︎ 。⋆ 。゜☾゜。⋆")
                        print("    메뉴로 돌아갑니다.   ")
                        print("⋆ 。゜☁︎ 。⋆ 。゜☾゜。⋆")
                        sleep(1)
                        break
                    else:
                        print("""    (> ” ” <) """)
                        print("    ( =’o'= ) ")
                        print("""----(,,)-(,,)----""")
                        print("│  다시 입력하세요. │")
                else:
                    break

    def show_all_diary(self):
        for index, diary_1 in enumerate(self.diary_list):
            print(f'\n        {index + 1}번째 일기')
            print(diary_1)
            sleep(1)

    # 모든 일기 보여주기

    def statistics(self):
        while True:
            print("\n╭───────────────────────────✎")
            print("| 통계를 낼 일기의 개수를 입력하세요.")
            print("| 최근의 일기로 계산됩니다.")
            statistics_count = input("╰─▗ ▘➤ ")

            if int(statistics_count) > len(self.diary_list):
                print("입력하신 수가 다이어리 개수보다 많습니다.!")
                print('일기의 개수: ' + str(len(self.diary_list)))
            elif int(statistics_count) <= len(self.diary_list):
                # 다이어리 안의 이모티콘 개수로 통계내기
                count_dict = {}
                for diary in self.diary_list:
                    emoji = diary.emoji
                    # moji 꺼내서 없으면 키로 등록 값은 1
                    if not emoji in count_dict:
                        count_dict[emoji] = 1
                    # 키가 있으면 값 +=1
                    else:
                        count_dict[emoji] += 1
                a = "━━"
                print("\n ♡ ♡ ᕬ ᕬ ♡ ♡")
                print("+ ♡ ( ⌯′-′⌯) ♡ +")
                print("┏━♡━U U━♡" + a*len(count_dict)*7 + "┓")
                print(str(count_dict))
                print("┗━♡━━━♡" + a*len(count_dict)*7 + "┛")
                sleep(2)
                break

    # 원하는 개수 입력 받아 일기 통계 내기

    def my_diary(self):
        윤아 = Diary('2021.06.01')
        윤아.date = '2021.06.01'
        윤아.emoji = '((o(´∀｀)o))'
        윤아.write = '안녕하세요'
        self.diary_list.append(윤아)

        지우 = Diary('2021.06.11')
        지우.date = '2021.06.11'
        지우.emoji = '(´°̥̥̥̥̥̥̥̥ω°̥̥̥̥̥̥̥̥｀)'
        지우.write = '안녕하세요'
        self.diary_list.append(지우)

    def __str__(self):
        pass