import webbrowser
import pickle

# 자료 조사..

def OpenUrl(self):  # 영화 예매 홈페이지로 넘어가기..
    url = 'https://www.aladin.co.kr/home/welcome.aspx'  # 주소 바꾸기
    webbrowser.open_new(url)

# 참고 : https://wikidocs.net/book/2165   https://reddb.tistory.com/137
# 네이버 영화 리뷰 크롤링하기 - https://velog.io/@changhtun1/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-3
# 로고 보여주고 몇 초 뒤에 다른 화면 보여주기 - https://trading-for-chicken.tistory.com/30
# 회원가입, 로그인..
# 메인 화면 - 제목, 내가 작성한 리뷰 보러가기 - 현재 상영중인 영화들 나열
# 내가 작성한 리뷰 - (날짜, 영화 제목, 스포 여부, 리뷰) 나열
# 영화 클릭하면 영화 포스터 중앙에 있고 밑에 쿠키영상 여부(쿠키영상 개수), 카테고리, 추천 좌석, 스포 리뷰 포함 여부 체크 - https://wikidocs.net/21937
# 체크 여부에 따라 크롤링 된 리뷰 나눠서 보여주기
# 리뷰 - 날짜, 영화 제목, 리뷰

from tkinter import * # tkinter 임포트
from tkinter import messagebox

window = Tk()   # 윈도우 변수에 TK() 셋

# 이 부분에서 화면을 구성하고 처리


# 기본 구성
window.title("GUI 연습")  # 윈도우 창 이름
window.geometry("400x100")  # 크기 가로 x 세로 ( x 소문자!!)
# window.resizable(width=False, height=False) # 리사이즈 가로 세로 여부

# 텍스트 넣기
# label1 = Label(window, text="labelTest1")   # 라벨1 변수에 Label() 생성, window 변수에 텍스트 표현
# label2 = Label(window, text="labelTest2", font=("궁서체", 30), fg="blue")  # 폰트 궁서체 30크기, 글자색 블루
# label3 = Label(window, text="labelTest3", bg="magenta", width=20, height=5, anchor=SE)   # 백그라운드 마젠타, anchor 사우스이스트(남동)
#
# label1.pack()
# label2.pack()
# label3.pack()


# 메세지 박스 출력
# def clickButton():  # 함수 호출 시 메세지 박스 보여주기(박스제목, 박스 내용)
#     messagebox.showinfo('메세지박스 제목', '메세지박스 내용입니다.') # 함수 호출 시 메세지 박스 보여주기(박스제목, 박스 내용)

# 버튼 출력
# button1 = Button(window, text="CLICK!", fg="red", bg="yellow", command=clickButton) # 버튼 1 변수에 버튼 생성, 커맨드(클릭시)=clickButton 함수 호출
# button1.pack(expand = 1)    # button1.채워넣기(확장두께=1)

# 버튼 정렬
# button2 = Button(window, text="Button2")    # button2 변수에 버튼 설정(윈도우 변수에, 텍스트 넣어서)
# button3 = Button(window, text="Button3")
# button4 = Button(window, text="Button4")
#
# button2.pack(side=LEFT) # 버튼 채워넣기(왼쪽에)
# button3.pack(side=LEFT)
# button4.pack(side=RIGHT) # 오른쪽 정렬, 채워넣을 때 정렬 pack(side=위치)


# 버튼 리스트로 만들어서 출력, 321로 나옴
# btnList = [None] * 3    # btnList 빈리스트 3개 공간 생성
#
# for i in range(0, 3):   # btnList 빈리스트 3개 공간 생성
#     btnList[i] = Button(window, text="Button" + str(i+1))   # i는 0,1,2로 돌지만 버튼 텍스트는 +1 해서 1,2,3으로 쓰여짐
#
# for btn in btnList: # 변수 btn에 btnList[0,1,2]설정
#     btn.pack(side=RIGHT)

# 이미지
# image = tkinter.PhotoImage(file="img_2.png")
# image1 = tkinter.Label(image=image)
# image1.place(x=530)

# 사진 버튼
# photo = PhotoImage(file="img_2.png")
# btn = Button(self.root, image=photo)
# btn.pack(expand=1, anchor=CENTER)

# 적는 박스, 선택 가능 박스
upFrame = Frame(window)     # 프레임 upFrame 변수에 셋
upFrame.pack()  # 채워넣기

downFrame = Frame(window)   # 프레임 downFrame 변수에 셋
downFrame.pack()    #  채워넣기

editBox = Entry(upFrame, width = 10, height=100, bg = 'pink')   # editBox변수에 한줄텍스트박스 Entry설정(upFrame을, 가로 10, 배경색핑크로)
editBox.pack(padx = 10, pady = 10)  # 채워넣기(여백)

listbox = Listbox(downFrame, bg = 'orange') # listbox변수에 Listbox설정(downFrame에, 배경색 오렌지로)
listbox.pack()  # 채워넣기

listbox.insert(END, "InsertText1")  # listbox에 값 입력
listbox.insert(END, "InsertText2")  # listbox에 값 입력

window.mainloop()

# 라디오 버튼
        # fruit_var = tkinter.IntVar()
        # button_fruit1 = tkinter.Radiobutton(self.root, text="apple", value=1, variable=fruit_var)
        # button_fruit2 = tkinter.Radiobutton(self.root, text="banana", value=2, variable=fruit_var)
        # button_fruit3 = tkinter.Radiobutton(self.root, text="strawberry", value=3, variable=fruit_var)
        # button_fruit4 = tkinter.Radiobutton(self.root, text="orange", value=4, variable=fruit_var)
        #
        # button_fruit1.pack()
        # button_fruit2.pack()
        # button_fruit3.pack()
        # button_fruit4.pack()

# 시간
#       label1 = Label(self.duneroot, text=datetime.today().strftime("%Y-%m-%d %H.%M"))
#       label1.pack()

# my_dict = {}  # empty dictionary
# while True:
#     key = int(input('키 입력 : '))
#     val = input('밸류 입력 : ')
#     my_dict[key] = val

# dic={"123":1,"345":2}
# file=open("fileName.txt","wb")
# pickle.dump(dic,file)
# file.close()
#
# file=open("fileName.txt","rb")
# content=pickle.load(file)
# print(content)