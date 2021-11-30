import tkinter
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import Combobox
# tkinter 임포트
from tkinter import messagebox
from datetime import datetime, timedelta
import pickle
import webbrowser

# print(pygame.font.get_fonts())  # 글꼴 종류 출력
# 휴먼모음t 휴먼편지체 휴먼둥근헤드라인 펜흘림 중간안상수체

class MovieGUI:
    def __init__(self):
        self.first_GUI()
        self.root = tkinter.Tk()

    def first_GUI(self):
        self.root = tkinter.Tk()  # 창 생성
        self.root.title('MoCookie')  # 창 제목
        self.root.geometry('1200x600+35+20')
        self.root.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.root.configure(bg="white")

        # 타이틀
        label1 = Label(self.root, font=("휴먼편지체", 40), text="MoCookie", bg="white", fg="black")
        label1.place(x="500", y="5")

        button_search = tkinter.Button(self.root, height=1, width=8, text="나의 리뷰", bg="white", font=("휴먼편지체", 10), command=self.myReview)
        button_search.place(x=1075, y=30)

        # Dune 버튼
        photo1 = PhotoImage(file="MoviePoster/Dune.png")
        btn1 = Button(self.root, image=photo1, command=self.dune_GUI)
        btn1.place(x="60", y="100")

        label1 = Label(self.root, text="듄", bg="white")
        label1.place(x="115", y="285")

        # 유체이탈자 버튼
        photo2 = PhotoImage(file="MoviePoster/Spiritwalker.png")
        btn2 = Button(self.root, image=photo2)
        btn2.place(x="250", y="100")

        label2 = Label(self.root, text="유체이탈자", bg="white")
        label2.place(x="285", y="285")

        # 연애 빠진 로맨스 버튼
        photo3 = PhotoImage(file="MoviePoster/NothingSerious.png")
        btn3 = Button(self.root, image=photo3)
        btn3.place(x="440", y="100")

        label3 = Label(self.root, text="연애 빠진 로맨스", bg="white")
        label3.place(x="458", y="285")

        # 엔칸토-마법의 세계 버튼
        photo4 = PhotoImage(file="MoviePoster/Encanto.png")
        btn4 = Button(self.root, image=photo4)
        btn4.place(x="630", y="100")

        label4 = Label(self.root, text="엔칸토-마법의 세계", bg="white")
        label4.place(x="640", y="285")

        # 이터널스 버튼
        photo5 = PhotoImage(file="MoviePoster/Eternals.png")
        btn5 = Button(self.root, image=photo5)
        btn5.place(x="820", y="100")

        label5 = Label(self.root, text="이터널스", bg="white")
        label5.place(x="860", y="285")

        # 장르만 로맨스 버튼
        photo6 = PhotoImage(file="MoviePoster/RomanceGenre.png")
        btn6 = Button(self.root, image=photo6)
        btn6.place(x="1010", y="100")

        label6 = Label(self.root, text="장르만 로맨스", bg="white")
        label6.place(x="1035", y="285")

        # 프렌치 디스패치 버튼
        photo7 = PhotoImage(file="MoviePoster/TheFrenchDispatch.png")
        btn7 = Button(self.root, image=photo7)
        btn7.place(x="60", y="325")

        label7 = Label(self.root, text="프렌치 디스패치", bg="white")
        label7.place(x="80", y="510")

        # 너에게 가는 길 버튼
        photo8 = PhotoImage(file="MoviePoster/Comingtoyou.png")
        btn8 = Button(self.root, image=photo8)
        btn8.place(x="250", y="325")

        label8 = Label(self.root, text="너에게 가는 길", bg="white")
        label8.place(x="273", y="510")

        # 라임 크라임 버튼
        photo9 = PhotoImage(file="MoviePoster/LIMECRIME.png")
        btn9 = Button(self.root, image=photo9)
        btn9.place(x="440", y="325")

        label9 = Label(self.root, text="라임 크라임", bg="white")
        label9.place(x="473", y="510")

        # 애비규환 버튼
        photo10 = PhotoImage(file="MoviePoster/MoreThanFamily.png")
        btn10 = Button(self.root, image=photo10)
        btn10.place(x="630", y="325")

        label10 = Label(self.root, text="애비규환", bg="white")
        label10.place(x="670", y="510")

        # 로그북 버튼
        photo11 = PhotoImage(file="MoviePoster/LogBook.png")
        btn11 = Button(self.root, image=photo11)
        btn11.place(x="820", y="325")

        label11 = Label(self.root, text="로그북", bg="white")
        label11.place(x="865", y="510")

        # 디어 에반 핸슨 버튼
        photo12 = PhotoImage(file="MoviePoster/DearEvanHansen.png")
        btn12 = Button(self.root, image=photo12)
        btn12.place(x="1010", y="325")

        label12 = Label(self.root, text="디어 에반 핸슨", bg="white")
        label12.place(x="1033", y="510")

        # 오른쪽 화살표
        photo13 = PhotoImage(file="Img/Right.png")
        btn13 = Button(self.root, image=photo13, bg="white", command=self.NextGUI)
        btn13.place(x="603", y="550")

        # 왼쪽 화살표
        photo14 = PhotoImage(file="Img/Left.png")
        btn14 = Button(self.root, image=photo14, bg="white")
        btn14.place(x="570", y="550")

        # 실행
        self.root.mainloop()

    def init_GUI(self):
        # main 화면 이미지 이미지를 덮는거임
        self.root.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
        self.root.mainBackL = tkinter.Label(image=self.root.mainBack)
        self.root.mainBackL.place(x=37, y=-2)

        self.root.title('MoCookie')  # 창 제목
        self.root.geometry('1200x600+35+20')
        self.root.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.root.configure(bg="white")

        # 타이틀
        label1 = Label(self.root, font=("휴먼편지체", 40), text="MoCookie", bg="white", fg="black")
        label1.place(x="500", y="5")

        button_search = tkinter.Button(self.root, height=1, width=8, text="나의 리뷰", bg="white", command=self.searchReview)
        button_search.place(x=1075, y=30)

        # Dune 버튼
        photo1 = PhotoImage(file="MoviePoster/Dune.png")
        btn1 = Button(self.root, image=photo1, command=self.dune_GUI)
        btn1.place(x="60", y="100")

        label1 = Label(self.root, text="듄", bg="white")
        label1.place(x="115", y="285")

        # 유체이탈자 버튼
        photo2 = PhotoImage(file="MoviePoster/Spiritwalker.png")
        btn2 = Button(self.root, image=photo2)
        btn2.place(x="250", y="100")

        label2 = Label(self.root, text="유체이탈자", bg="white")
        label2.place(x="285", y="285")

        # 연애 빠진 로맨스 버튼
        photo3 = PhotoImage(file="MoviePoster/NothingSerious.png")
        btn3 = Button(self.root, image=photo3)
        btn3.place(x="440", y="100")

        label3 = Label(self.root, text="연애 빠진 로맨스", bg="white")
        label3.place(x="458", y="285")

        # 엔칸토-마법의 세계 버튼
        photo4 = PhotoImage(file="MoviePoster/Encanto.png")
        btn4 = Button(self.root, image=photo4)
        btn4.place(x="630", y="100")

        label4 = Label(self.root, text="엔칸토-마법의 세계", bg="white")
        label4.place(x="640", y="285")

        # 이터널스 버튼
        photo5 = PhotoImage(file="MoviePoster/Eternals.png")
        btn5 = Button(self.root, image=photo5)
        btn5.place(x="820", y="100")

        label5 = Label(self.root, text="이터널스", bg="white")
        label5.place(x="860", y="285")

        # 장르만 로맨스 버튼
        photo6 = PhotoImage(file="MoviePoster/RomanceGenre.png")
        btn6 = Button(self.root, image=photo6)
        btn6.place(x="1010", y="100")

        label6 = Label(self.root, text="장르만 로맨스", bg="white")
        label6.place(x="1035", y="285")

        # 프렌치 디스패치 버튼
        photo7 = PhotoImage(file="MoviePoster/TheFrenchDispatch.png")
        btn7 = Button(self.root, image=photo7)
        btn7.place(x="60", y="325")

        label7 = Label(self.root, text="프렌치 디스패치", bg="white")
        label7.place(x="80", y="510")

        # 너에게 가는 길 버튼
        photo8 = PhotoImage(file="MoviePoster/Comingtoyou.png")
        btn8 = Button(self.root, image=photo8)
        btn8.place(x="250", y="325")

        label8 = Label(self.root, text="너에게 가는 길", bg="white")
        label8.place(x="273", y="510")

        # 라임 크라임 버튼
        photo9 = PhotoImage(file="MoviePoster/LIMECRIME.png")
        btn9 = Button(self.root, image=photo9)
        btn9.place(x="440", y="325")

        label9 = Label(self.root, text="라임 크라임", bg="white")
        label9.place(x="473", y="510")

        # 애비규환 버튼
        photo10 = PhotoImage(file="MoviePoster/MoreThanFamily.png")
        btn10 = Button(self.root, image=photo10)
        btn10.place(x="630", y="325")

        label10 = Label(self.root, text="애비규환", bg="white")
        label10.place(x="670", y="510")

        # 로그북 버튼
        photo11 = PhotoImage(file="MoviePoster/LogBook.png")
        btn11 = Button(self.root, image=photo11)
        btn11.place(x="820", y="325")

        label11 = Label(self.root, text="로그북", bg="white")
        label11.place(x="865", y="510")

        # 디어 에반 핸슨 버튼
        photo12 = PhotoImage(file="MoviePoster/DearEvanHansen.png")
        btn12 = Button(self.root, image=photo12)
        btn12.place(x="1010", y="325")

        label12 = Label(self.root, text="디어 에반 핸슨", bg="white")
        label12.place(x="1033", y="510")

        # 오른쪽 화살표
        photo13 = PhotoImage(file="Img/Right.png")
        btn13 = Button(self.root, image=photo13, bg="white", command=self.NextGUI)
        btn13.place(x="603", y="550")

        # 왼쪽 화살표
        photo14 = PhotoImage(file="Img/Left.png")
        btn14 = Button(self.root, image=photo14, bg="white")
        btn14.place(x="570", y="550")

        # 실행
        self.root.mainloop()

    def NextGUI(self):
        # main 화면 이미지 이미지를 덮는거임
        self.root.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
        self.root.mainBackL = tkinter.Label(image=self.root.mainBack)
        self.root.mainBackL.place(x=37, y=-2)

        self.root.title('MoCookie')  # 창 제목
        self.root.geometry('1200x600+35+20')
        self.root.resizable(width=False, height=False)

        # 타이틀
        label1 = Label(self.root, font=("휴먼편지체", 40), text="MoCookie", bg="white", fg="black")
        label1.place(x="500", y="5")

        button_search = tkinter.Button(self.root, height=1, width=8, text="나의 리뷰", bg="white", command=self.searchReview)
        button_search.place(x=1075, y=30)

        # 호빗: 스마우그의 폐허 버튼
        photo1 = PhotoImage(file="MoviePoster/TheHobbit.png")
        btn1 = Button(self.root, image=photo1)
        btn1.place(x="60", y="100")

        label1 = Label(self.root, text="호빗: 스마우그의 폐허", bg="white")
        label1.place(x="63", y="285")

        # 행복의 속도 버튼
        photo2 = PhotoImage(file="MoviePoster/SpeedOfHappiness.png")
        btn2 = Button(self.root, image=photo2)
        btn2.place(x="250", y="100")

        label2 = Label(self.root, text="행복의 속도", bg="white")
        label2.place(x="280", y="285")

        # 왕십리 김종분 버튼
        photo3 = PhotoImage(file="MoviePoster/Wangsimni.png")
        btn3 = Button(self.root, image=photo3)
        btn3.place(x="440", y="100")

        label3 = Label(self.root, text="왕십리 김종분", bg="white")
        label3.place(x="465", y="285")

        # 귀멸의 칼날 버튼
        photo4 = PhotoImage(file="MoviePoster/DemonSlayer.png")
        btn4 = Button(self.root, image=photo4)
        btn4.place(x="630", y="100")

        label4 = Label(self.root, text="귀멸의 칼날: 나타구모산 편", bg="white")
        label4.place(x="618", y="285")

        # 귀멸의 칼날2 버튼
        photo5 = PhotoImage(file="MoviePoster/DemonSlayer2.png")
        btn5 = Button(self.root, image=photo5)
        btn5.place(x="820", y="100")

        label5 = Label(self.root, text="귀멸의 칼날-남매의 연", bg="white")
        label5.place(x="823", y="285")

        # 퍼스트 카우 버튼
        photo6 = PhotoImage(file="MoviePoster/FirstCow.png")
        btn6 = Button(self.root, image=photo6)
        btn6.place(x="1010", y="100")

        label6 = Label(self.root, text="퍼스트 카우", bg="white")
        label6.place(x="1040", y="285")

        # 메이드 인 이태리 버튼
        photo7 = PhotoImage(file="MoviePoster/MadeInItaly.png")
        btn7 = Button(self.root, image=photo7)
        btn7.place(x="60", y="325")

        label7 = Label(self.root, text="메이드 인 이태리", bg="white")
        label7.place(x="78", y="510")

        # 1984 최동원 버튼
        photo8 = PhotoImage(file="MoviePoster/ChoiDongWon.png")
        btn8 = Button(self.root, image=photo8)
        btn8.place(x="250", y="325")

        label8 = Label(self.root, text="1984 최동원", bg="white")
        label8.place(x="275", y="510")

        # 휴가 버튼
        photo9 = PhotoImage(file="MoviePoster/ALeave.png")
        btn9 = Button(self.root, image=photo9)
        btn9.place(x="440", y="325")

        label9 = Label(self.root, text="휴가", bg="white")
        label9.place(x="490", y="510")

        # 러브 어페어 버튼
        photo10 = PhotoImage(file="MoviePoster/LoveAffair.png")
        btn10 = Button(self.root, image=photo10)
        btn10.place(x="630", y="325")

        label10 = Label(self.root, text="러브 어페어-우리가 말하는 것,\n 우리가 하는 것", bg="white")
        label10.place(x="613", y="510")

        # 꽃다발 같은 사랑을 했다 버튼
        photo11 = PhotoImage(file="MoviePoster/Bouquet.png")
        btn11 = Button(self.root, image=photo11)
        btn11.place(x="820", y="325")

        label11 = Label(self.root, text="꽃다발 같은 사랑을 했다", bg="white")
        label11.place(x="818", y="510")

        # 너의 이름은 버튼
        photo12 = PhotoImage(file="MoviePoster/YourName.png")
        btn12 = Button(self.root, image=photo12)
        btn12.place(x="1010", y="325")

        label12 = Label(self.root, text="너의 이름은", bg="white")
        label12.place(x="1040", y="510")

        # 오른쪽 화살표
        photo13 = PhotoImage(file="Img/Right.png")
        btn13 = Button(self.root, image=photo13, bg="white")
        btn13.place(x="603", y="550")

        # 왼쪽 화살표
        photo14 = PhotoImage(file="Img/Left.png")
        btn14 = Button(self.root, image=photo14, bg="white", command=self.init_GUI)
        btn14.place(x="570", y="550")

        # 실행
        self.root.mainloop()

    def dune_GUI(self):
        self.duneroot = tkinter.Toplevel()  # 창 생성
        self.duneroot.title('MoCookie')  # 창 제목
        self.duneroot.geometry('600x600+340+20')
        self.duneroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.duneroot.configure(bg="cadetblue")

        self.duneroot.label2 = Label(self.duneroot, font=("휴먼편지체", 35), text="DUNE", bg="cadetblue")
        self.duneroot.label2.place(x="10", y="10")

        self.duneroot.image = tkinter.PhotoImage(file="Poster/img_1.png")
        self.duneroot.label = tkinter.Label(self.duneroot, image=self.duneroot.image, bg="cadetblue")
        self.duneroot.label.place(x="195", y="55")

        self.duneroot.label1 = Label(self.duneroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="cadetblue")
        self.duneroot.label1.place(x="233", y="360")

        self.duneroot.label2= Label(self.duneroot, font=("휴먼편지체", 12), text="개봉일 : 2021.10.20", bg="cadetblue")
        self.duneroot.label2.place(x="234", y="395")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="장르 : SF", bg="cadetblue")
        self.duneroot.label3.place(x="264", y="415")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가", bg="cadetblue")
        self.duneroot.label3.place(x="230", y="435")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="러닝타임 : 155분", bg="cadetblue")
        self.duneroot.label3.place(x="241", y="455")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="추천 좌석 : B~C, 5~10", bg="cadetblue")
        self.duneroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.duneroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="cadetblue")
        c1.place(x="270", y="500")

        button1 = Button(self.duneroot, text="예매하기", font=("휴먼편지체", 11), bg="powderblue", command=self.DuneUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.duneroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="powderblue", command=self.review)
        button1.place(x="310", y="530")

        # 실행
        self.duneroot.mainloop()

    def DuneUrl(self): # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125057'
        webbrowser.open_new(url)

    def review(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.duneroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.duneroot.mainBackL = tkinter.Label(self.duneroot, image=self.duneroot.mainBack)
            self.duneroot.mainBackL.place(x=-2, y=-2)

            self.duneroot.title('MoCookie')  # 창 제목
            self.duneroot.geometry('600x600+340+20')
            self.duneroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            frame = Frame(self.duneroot)
            frame.pack()

            f = open("MovieReview/DuneReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(frame, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()

            # 버튼 출력
            button1 = Button(self.duneroot, text="리뷰 작성", bg="white", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.duneroot.label2 = Label(self.duneroot, font=("휴먼편지체", 35), text="DUNE", bg="white")
            self.duneroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.duneroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.duneroot.mainBackL = tkinter.Label(self.duneroot, image=self.duneroot.mainBack)
            self.duneroot.mainBackL.place(x=-2, y=-2)

            self.duneroot.title('MoCookie')  # 창 제목
            self.duneroot.geometry('600x600+340+20')
            self.duneroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            frame = Frame(self.duneroot)
            frame.pack()

            f = open("MovieReview/DuneSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(frame, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()

            # 버튼 출력
            button1 = Button(self.duneroot, text="리뷰 작성", bg="white", command=self.writeReview)
            button1.place(x="520", y="25")

            self.duneroot.label2 = Label(self.duneroot, font=("휴먼편지체", 35), text="DUNE", bg="white")
            self.duneroot.label2.place(x="10", y="10")

        # 실행
        self.duneroot.mainloop()

    # def Sporeview(self):
    #     self.rootreview = tkinter.Toplevel()  # 창 생성
    #     self.rootreview.title('MoCookie')  # 창 제목
    #     self.rootreview.geometry('600x600+340+20')
    #     self.rootreview.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
    #     self.rootreview.configure(bg="white")
    #
    #
    #
    #     # 버튼 출력
    #     button1 = Button(self.rootreview, text="!!!!!", fg="red", bg="blue", command=self.writeReview)  # 버튼 1 변수에 버튼 생성, 커맨드(클릭시)=clickButton 함수 호출
    #     button1.pack(expand=1)  # button1.채워넣기(확장두께=1)
    #
    #     # 버튼 출력
    #     button1 = Button(self.rootreview, text="CLICK", fg="red", bg="blue", command=self.fbutton)  # 버튼 1 변수에 버튼 생성, 커맨드(클릭시)=clickButton 함수 호출
    #     button1.pack(expand=1)  # button1.채워넣기(확장두께=1)
    #
    #     # 실행
    #     self.rootreview.mainloop()

    def writeReview(self):
        # main 화면 이미지 이미지를 덮는거임
        self.duneroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
        self.duneroot.mainBackL = tkinter.Label(self.duneroot, image=self.duneroot.mainBack)
        self.duneroot.mainBackL.place(x=-2, y=-2)

        self.duneroot.title('MoCookie')  # 창 제목
        self.duneroot.geometry('600x600+340+20')
        self.duneroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

        label1 = Label(self.duneroot, text="리뷰 작성", bg="white",font=("휴먼편지체", 23))
        label1.place(x=240, y=15)
        str = StringVar()
        self.entry1 = Entry(self.duneroot, width=20, font=("휴먼편지체", 10), textvariable=str)  # 이름 입력
        self.entry1.place(x=230, y=80)
        a = ["듄", "유체이탈자", "연애 빠진 로맨스", "엔칸토-마법의 세계", "이터널스", "장르만 로맨스", "프렌치 디스패치", "너에게 가는 길", "라임 크라임", "애비규환", "로그북",
             "디어 에반 핸슨", "호빗: 스마우그의 폐허", "행복의 속도", "왕십리 김종분", "귀멸의 칼날: 나타구모산 편", "귀멸의 칼날-남매의 연", "퍼스트 카우", "메이드 인 이태리", "1984 최동원", "휴가", "러브 어페어", "꽃다발 같은 사랑을 했다", "너의 이름은"]  # 콤보 박스
        self.combo1 = ttk.Combobox(self.duneroot)
        self.combo1.config(height=5, width=30)  # 높이 설정
        self.combo1.config(values=a, font=("휴먼편지체", 10))  # 나타낼 항목 리스트(a) 설정
        self.combo1.config(state="readonly", font=("휴먼편지체", 10))  # 콤보 박스에 사용자가 직접 입력 불가
        self.combo1.set("※리뷰를 남길 영화를 선택해주세요※")  # 맨 처음 나타낼 값 설정
        self.combo1.place(x=190, y=115)
        self.text15 = Text(self.duneroot, height="20", font=("휴먼편지체", 10))  # 리뷰 작성
        self.text15.place(x=55, y=160)
        # 체크 박스
        self.CheckVar2 = IntVar()
        self.c2 = Checkbutton(self.duneroot, text="스포포함", variable=self.CheckVar2, font=("휴먼편지체", 13), bg="white")
        self.c2.place(x="260", y="470")
        button_sa = tkinter.Button(self.duneroot, height=1, width=8, text="리뷰 저장", font=("휴먼편지체", 10), command=self.add_review)
        button_sa.place(x=260, y=500)

        # 실행
        self.duneroot.mainloop()

    # def spoReviewSaved(self, text): #파일 저장하는 함수
    #     f = open('spoilerReview.txt','a')
    #     f.write(text+"\n")
    #     messagebox.showwarning('저장완료', '저장되었습니다') #메세지 박스 출력
    #     self.window.destroy() #화면 창 끄기
    #
    # def ReviewSaved(self, text): #파일 저장하는 함수
    #     f = open('Review.txt','a')
    #     f.write(text+"\n")
    #     messagebox.showwarning('저장완료', '저장되었습니다') #메세지 박스 출력
    #     self.window.destroy() #화면 창 끄기

    # def mychart(self): #명대사 저장하기 위해 입력하는 창
    #         self.window = tkinter.Toplevel()
    #         self.window.geometry("800x400")
    #
    #         label1 = Label(self.window, text = "인상 깊게 본 명대사를 써주세요!")
    #         str = StringVar()
    #         self.entry1 = Entry(self.window, width=20, textvariable=str)
    #         label1.pack()
    #         self.entry1.pack()
    #         self.text15 = Text(self.window, height="10")
    #         self.text15.pack()
    #         a = ["Python", "JAVA", "C"]  # 콤보 박스에 나타낼 항목 리스트
    #         self.combo1 = ttk.Combobox(self.window)  # root라는 창에 콤보박스 생성
    #         self.combo1.config(height=5)  # 높이 설정
    #         self.combo1.config(values=a)  # 나타낼 항목 리스트(a) 설정
    #         self.combo1.config(state="readonly")  # 콤보 박스에 사용자가 직접 입력 불가
    #         self.combo1.set("골라 골라")  # 맨 처음 나타낼 값 설정
    #         self.combo1.pack()
    #         button_sa = tkinter.Button(self.window, height=6, width=10, text="저장", command=self.add_review)
    #         button_sa.pack()
    #         button_search = tkinter.Button(self.window, height=6, width=10, text="저장", command=self.searchReview)
    #         button_search.pack()
    #         self.window.mainloop()

    # def fbutton(self):  # 작성한 파일 불러오는 함수
    #
    #     # 스크롤
    #     # frame = Frame(self.root)
    #     # frame.grid(column=0, row=0)
    #     #
    #     # scrollbar = Scrollbar(frame)
    #     # scrollbar.pack(side="right", fill="both")
    #     #
    #     # list = Listbox(frame, yscrollcommand = scrollbar.set)
    #     # for line in range(30):
    #     #     list.insert(END, "Line No" + str(line))
    #     #
    #     # list.pack(side="left", fill="both")
    #     # scrollbar.config(command=list.yview)
    #     #
    #     # mainloop()
    #
    #     self.window2 = tkinter.Toplevel()
    #     self.window2.geometry("600x600")
    #
    #     frame = Frame(self.window2)
    #     frame.pack()
    #
    #     f = open("MovieReview/DuneReview.txt", 'r', encoding="UTF-8")
    #     text = f.read()
    #     label = tkinter.Label(frame, width=600, height=600, font=("휴먼편지체", 10), text=text)
    #     label.pack(side='left', fill="y")
    #
    #     #
    #     # # listNodes = Listbox(frame, width=600, height=600, font=("휴먼편지체", 10))
    #     # # listNodes.pack(side='left', fill="y")
    #     #
    #     # scrollbar = Scrollbar(frame, orient="vertical")
    #     # scrollbar.config(command=label.yview)
    #     # scrollbar.pack(side="right", fill="y")
    #     #
    #     # label.config(yscrollcommand=scrollbar.set)
    #
    #     # for x in range(100):
    #     #     label.insert(END, str(x))

    def myReview(self):
        self.myreview = tkinter.Toplevel()  # 창 생성
        self.myreview.title('MoCookie')  # 창 제목
        self.myreview.geometry('600x600+340+20')
        self.myreview.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.myreview.configure(bg="cadetblue")

        with open('MyReview.txt', 'rb') as fr:
            review_loaded = pickle.load(fr)
            label = tkinter.Label(self.myreview, text=review_loaded)
            label.pack()

    def add_review(self):
        # 리뷰 딕셔너리로 MyReview.txt에 저장
        self.reviews = []
        print(self.CheckVar.get())
        self.new_review = {'이름': self.entry1.get(), '영화 제목': self.combo1.get(), '스포 여부(0은 X, 1은 O)' : self.CheckVar2.get(), '리뷰': self.text15.get("0.1", "end")}

        self.reviews.append(self.new_review)

        with open('MyReview.txt', 'wb') as fw:
            pickle.dump(self.reviews, fw)

        messagebox.showwarning('저장완료', '저장되었습니다.')  # 메세지 박스 출력
        self.duneroot.destroy()  # 화면 창 끄기

    # def searchReview(self):
    #     self.window5 = tkinter.Toplevel()
    #     self.window5.geometry("600x600")
    #     self.x_entry = Entry(self.window5, width=10, bg="light blue")
    #     self.x_entry.pack()
    #     button_search = tkinter.Button(self.window5, height=6, width=10, text="저장", command=self.searchBtn)
    #     button_search.pack()

    # 검색..
    # def searchBtn(self):
    #     self.results = []
    #     for review in self.reviews:
    #         if name in review['이름']:
    #             self.results.append(review)
    #
    #     print(self.results)

if __name__ == '__main__':
    MovieGUI = MovieGUI()

