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

# 행복의 속도, 러브 어페어 파일 안됨

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

        button_search = tkinter.Button(self.root, height=1, width=8, text="리뷰 작성", bg="white", font=("휴먼편지체", 10), command=self.writeReview)
        button_search.place(x=995, y=30)

        # Dune 버튼
        photo1 = PhotoImage(file="MoviePoster/Dune.png")
        btn1 = Button(self.root, image=photo1, command=self.dune_GUI)
        btn1.place(x="60", y="100")

        label1 = Label(self.root, text="듄", font=("휴먼편지체", 10), bg="white")
        label1.place(x="115", y="285")

        # 유체이탈자 버튼
        photo2 = PhotoImage(file="MoviePoster/Spiritwalker.png")
        btn2 = Button(self.root, image=photo2, command=self.spirit_GUI)
        btn2.place(x="250", y="100")

        label2 = Label(self.root, text="유체이탈자", font=("휴먼편지체", 10), bg="white")
        label2.place(x="285", y="285")

        # 연애 빠진 로맨스 버튼
        photo3 = PhotoImage(file="MoviePoster/NothingSerious.png")
        btn3 = Button(self.root, image=photo3, command=self.NothingSerious_GUI)
        btn3.place(x="440", y="100")

        label3 = Label(self.root, text="연애 빠진 로맨스", font=("휴먼편지체", 10), bg="white")
        label3.place(x="458", y="285")

        # 엔칸토-마법의 세계 버튼
        photo4 = PhotoImage(file="MoviePoster/Encanto.png")
        btn4 = Button(self.root, image=photo4, command=self.Encanto_GUI)
        btn4.place(x="630", y="100")

        label4 = Label(self.root, text="엔칸토-마법의 세계", font=("휴먼편지체", 10), bg="white")
        label4.place(x="640", y="285")

        # 이터널스 버튼
        photo5 = PhotoImage(file="MoviePoster/Eternals.png")
        btn5 = Button(self.root, image=photo5, command=self.Eternals_GUI)
        btn5.place(x="820", y="100")

        label5 = Label(self.root, text="이터널스", font=("휴먼편지체", 10), bg="white")
        label5.place(x="860", y="285")

        # 장르만 로맨스 버튼
        photo6 = PhotoImage(file="MoviePoster/RomanceGenre.png")
        btn6 = Button(self.root, image=photo6, command=self.Janr_GUI)
        btn6.place(x="1010", y="100")

        label6 = Label(self.root, text="장르만 로맨스", font=("휴먼편지체", 10), bg="white")
        label6.place(x="1035", y="285")

        # 프렌치 디스패치 버튼
        photo7 = PhotoImage(file="MoviePoster/TheFrenchDispatch.png")
        btn7 = Button(self.root, image=photo7, command=self.French_GUI)
        btn7.place(x="60", y="325")

        label7 = Label(self.root, text="프렌치 디스패치", font=("휴먼편지체", 10), bg="white")
        label7.place(x="80", y="510")

        # 너에게 가는 길 버튼
        photo8 = PhotoImage(file="MoviePoster/Comingtoyou.png")
        btn8 = Button(self.root, image=photo8, command=self.Coming_GUI)
        btn8.place(x="250", y="325")

        label8 = Label(self.root, text="너에게 가는 길", font=("휴먼편지체", 10), bg="white")
        label8.place(x="273", y="510")

        # 라임 크라임 버튼
        photo9 = PhotoImage(file="MoviePoster/LIMECRIME.png")
        btn9 = Button(self.root, image=photo9, command=self.Lime_GUI)
        btn9.place(x="440", y="325")

        label9 = Label(self.root, text="라임 크라임", font=("휴먼편지체", 10), bg="white")
        label9.place(x="473", y="510")

        # 호빗: 스마우그의 폐허 버튼
        photo10 = PhotoImage(file="MoviePoster/TheHobbit.png")
        btn10 = Button(self.root, image=photo10, command=self.Hobit_GUI)
        btn10.place(x="630", y="325")

        label10 = Label(self.root, text="호빗: 스마우그의 폐허", font=("휴먼편지체", 10), bg="white")
        label10.place(x="640", y="510")

        # 로그북 버튼
        photo11 = PhotoImage(file="MoviePoster/LogBook.png")
        btn11 = Button(self.root, image=photo11, command=self.Log_GUI)
        btn11.place(x="820", y="325")

        label11 = Label(self.root, text="로그북", font=("휴먼편지체", 10), bg="white")
        label11.place(x="865", y="510")

        # 디어 에반 핸슨 버튼
        photo12 = PhotoImage(file="MoviePoster/DearEvanHansen.png")
        btn12 = Button(self.root, image=photo12, command=self.Dear_GUI)
        btn12.place(x="1010", y="325")

        label12 = Label(self.root, text="디어 에반 핸슨", font=("휴먼편지체", 10), bg="white")
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

        button_search = tkinter.Button(self.root, height=1, width=8, text="나의 리뷰", bg="white", font=("휴먼편지체", 10), command=self.myReview)
        button_search.place(x=1075, y=30)

        button_search = tkinter.Button(self.root, height=1, width=8, text="리뷰 작성", bg="white", font=("휴먼편지체", 10),
                                       command=self.writeReview)
        button_search.place(x=995, y=30)

        # Dune 버튼
        photo1 = PhotoImage(file="MoviePoster/Dune.png")
        btn1 = Button(self.root, image=photo1, command=self.dune_GUI)
        btn1.place(x="60", y="100")

        label1 = Label(self.root, text="듄", font=("휴먼편지체", 10), bg="white")
        label1.place(x="115", y="285")

        # 유체이탈자 버튼
        photo2 = PhotoImage(file="MoviePoster/Spiritwalker.png")
        btn2 = Button(self.root, image=photo2, command=self.spirit_GUI)
        btn2.place(x="250", y="100")

        label2 = Label(self.root, text="유체이탈자", font=("휴먼편지체", 10), bg="white")
        label2.place(x="285", y="285")

        # 연애 빠진 로맨스 버튼
        photo3 = PhotoImage(file="MoviePoster/NothingSerious.png")
        btn3 = Button(self.root, image=photo3, command=self.NothingSerious_GUI)
        btn3.place(x="440", y="100")

        label3 = Label(self.root, text="연애 빠진 로맨스", font=("휴먼편지체", 10), bg="white")
        label3.place(x="458", y="285")

        # 엔칸토-마법의 세계 버튼
        photo4 = PhotoImage(file="MoviePoster/Encanto.png")
        btn4 = Button(self.root, image=photo4, command=self.Encanto_GUI)
        btn4.place(x="630", y="100")

        label4 = Label(self.root, text="엔칸토-마법의 세계", font=("휴먼편지체", 10), bg="white")
        label4.place(x="640", y="285")

        # 이터널스 버튼
        photo5 = PhotoImage(file="MoviePoster/Eternals.png")
        btn5 = Button(self.root, image=photo5, command=self.Eternals_GUI)
        btn5.place(x="820", y="100")

        label5 = Label(self.root, text="이터널스", font=("휴먼편지체", 10), bg="white")
        label5.place(x="860", y="285")

        # 장르만 로맨스 버튼
        photo6 = PhotoImage(file="MoviePoster/RomanceGenre.png")
        btn6 = Button(self.root, image=photo6, command=self.Janr_GUI)
        btn6.place(x="1010", y="100")

        label6 = Label(self.root, text="장르만 로맨스", font=("휴먼편지체", 10), bg="white")
        label6.place(x="1035", y="285")

        # 프렌치 디스패치 버튼
        photo7 = PhotoImage(file="MoviePoster/TheFrenchDispatch.png")
        btn7 = Button(self.root, image=photo7, command=self.French_GUI)
        btn7.place(x="60", y="325")

        label7 = Label(self.root, text="프렌치 디스패치", font=("휴먼편지체", 10), bg="white")
        label7.place(x="80", y="510")

        # 너에게 가는 길 버튼
        photo8 = PhotoImage(file="MoviePoster/Comingtoyou.png")
        btn8 = Button(self.root, image=photo8, command=self.Coming_GUI)
        btn8.place(x="250", y="325")

        label8 = Label(self.root, text="너에게 가는 길", font=("휴먼편지체", 10), bg="white")
        label8.place(x="273", y="510")

        # 라임 크라임 버튼
        photo9 = PhotoImage(file="MoviePoster/LIMECRIME.png")
        btn9 = Button(self.root, image=photo9, command=self.Lime_GUI)
        btn9.place(x="440", y="325")

        label9 = Label(self.root, text="라임 크라임", font=("휴먼편지체", 10), bg="white")
        label9.place(x="473", y="510")

        # 호빗: 스마우그의 폐허 버튼
        photo10 = PhotoImage(file="MoviePoster/TheHobbit.png")
        btn10 = Button(self.root, image=photo10, command=self.Hobit_GUI)
        btn10.place(x="630", y="325")

        label10 = Label(self.root, text="호빗: 스마우그의 폐허", font=("휴먼편지체", 10), bg="white")
        label10.place(x="640", y="510")

        # 로그북 버튼
        photo11 = PhotoImage(file="MoviePoster/LogBook.png")
        btn11 = Button(self.root, image=photo11, command=self.Log_GUI)
        btn11.place(x="820", y="325")

        label11 = Label(self.root, text="로그북", font=("휴먼편지체", 10), bg="white")
        label11.place(x="865", y="510")

        # 디어 에반 핸슨 버튼
        photo12 = PhotoImage(file="MoviePoster/DearEvanHansen.png")
        btn12 = Button(self.root, image=photo12, command=self.Dear_GUI)
        btn12.place(x="1010", y="325")

        label12 = Label(self.root, text="디어 에반 핸슨", font=("휴먼편지체", 10), bg="white")
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

        button_search = tkinter.Button(self.root, height=1, width=8, text="나의 리뷰", bg="white",  font=("휴먼편지체", 10),command=self.myReview)
        button_search.place(x=1075, y=30)

        button_search = tkinter.Button(self.root, height=1, width=8, text="리뷰 작성", bg="white", font=("휴먼편지체", 10),
                                       command=self.writeReview)
        button_search.place(x=995, y=30)

        # 꽃다발 같은 사랑을 했다 버튼
        photo1 = PhotoImage(file="MoviePoster/Bouquet.png")
        btn1 = Button(self.root, image=photo1, command=self.Bouquet_GUI)
        btn1.place(x="60", y="100")

        label1 = Label(self.root, text="꽃다발 같은 사랑을 했다", font=("휴먼편지체", 10), bg="white")
        label1.place(x="61", y="285")

        # 너의 이름은 버튼
        photo2 = PhotoImage(file="MoviePoster/YourName.png")
        btn2 = Button(self.root, image=photo2, command=self.YourName_GUI)
        btn2.place(x="250", y="100")

        label2 = Label(self.root, text="너의 이름은", font=("휴먼편지체", 10), bg="white")
        label2.place(x="280", y="285")

        # 왕십리 김종분 버튼
        photo3 = PhotoImage(file="MoviePoster/Wangsimni.png")
        btn3 = Button(self.root, image=photo3, command=self.Kim_GUI)
        btn3.place(x="440", y="100")

        label3 = Label(self.root, text="왕십리 김종분", font=("휴먼편지체", 10), bg="white")
        label3.place(x="465", y="285")

        # 귀멸의 칼날 버튼
        photo4 = PhotoImage(file="MoviePoster/DemonSlayer.png")
        btn4 = Button(self.root, image=photo4, command=self.Natagumo_GUI)
        btn4.place(x="630", y="100")

        label4 = Label(self.root, text="귀멸의 칼날: 나타구모산 편", font=("휴먼편지체", 10), bg="white")
        label4.place(x="618", y="285")

        # 귀멸의 칼날2 버튼
        photo5 = PhotoImage(file="MoviePoster/DemonSlayer2.png")
        btn5 = Button(self.root, image=photo5, command=self.Nammae_GUI)
        btn5.place(x="820", y="100")

        label5 = Label(self.root, text="귀멸의 칼날-남매의 연", font=("휴먼편지체", 10), bg="white")
        label5.place(x="823", y="285")

        # 퍼스트 카우 버튼
        photo6 = PhotoImage(file="MoviePoster/FirstCow.png")
        btn6 = Button(self.root, image=photo6, command=self.FirstCow_GUI)
        btn6.place(x="1010", y="100")

        label6 = Label(self.root, text="퍼스트 카우", font=("휴먼편지체", 10), bg="white")
        label6.place(x="1040", y="285")

        # 메이드 인 이태리 버튼
        photo7 = PhotoImage(file="MoviePoster/MadeInItaly.png")
        btn7 = Button(self.root, image=photo7, command=self.Italy_GUI)
        btn7.place(x="60", y="325")

        label7 = Label(self.root, text="메이드 인 이태리", font=("휴먼편지체", 10), bg="white")
        label7.place(x="78", y="510")

        # 1984 최동원 버튼
        photo8 = PhotoImage(file="MoviePoster/ChoiDongWon.png")
        btn8 = Button(self.root, image=photo8, command=self.Choi_GUI)
        btn8.place(x="250", y="325")

        label8 = Label(self.root, text="1984 최동원", font=("휴먼편지체", 10), bg="white")
        label8.place(x="275", y="510")

        # 휴가 버튼
        photo9 = PhotoImage(file="MoviePoster/ALeave.png")
        btn9 = Button(self.root, image=photo9, command=self.Leave_GUI)
        btn9.place(x="440", y="325")

        label9 = Label(self.root, text="휴가", font=("휴먼편지체", 10), bg="white")
        label9.place(x="490", y="510")

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
        self.duneroot.configure(bg="white")

        self.duneroot.label2 = Label(self.duneroot, font=("휴먼편지체", 35), text="DUNE", bg="white", fg="powderblue")
        self.duneroot.label2.place(x="10", y="10")

        self.duneroot.image = tkinter.PhotoImage(file="Poster/DunePoster.png")
        self.duneroot.label = tkinter.Label(self.duneroot, image=self.duneroot.image, bg="white")
        self.duneroot.label.place(x="195", y="55")

        self.duneroot.label1 = Label(self.duneroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.duneroot.label1.place(x="233", y="360")

        self.duneroot.label2= Label(self.duneroot, font=("휴먼편지체", 12), text="개봉일 : 2021.10.20", bg="white")
        self.duneroot.label2.place(x="234", y="395")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="장르 : SF", bg="white")
        self.duneroot.label3.place(x="264", y="415")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가", bg="white")
        self.duneroot.label3.place(x="230", y="435")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="러닝타임 : 155분", bg="white")
        self.duneroot.label3.place(x="241", y="455")

        self.duneroot.label3 = Label(self.duneroot, font=("휴먼편지체", 12), text="추천 좌석 : B~C, 5~10", bg="white")
        self.duneroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.duneroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.duneroot, text="예매하기", font=("휴먼편지체", 11), bg="powderblue", command=self.DuneUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.duneroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="powderblue", command=self.Dunereview)
        button1.place(x="310", y="530")

        # 실행
        self.duneroot.mainloop()

    def DuneUrl(self): # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125057'
        webbrowser.open_new(url)

    def Dunereview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.duneroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.duneroot.mainBackL = tkinter.Label(self.duneroot, image=self.duneroot.mainBack)
            self.duneroot.mainBackL.place(x=-2, y=-2)

            self.duneroot.title('MoCookie')  # 창 제목
            self.duneroot.geometry('600x600+340+20')
            self.duneroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/DuneReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.duneroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '듄':
                    tmp += 20
                    label = Label(self.duneroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=510 + tmp)

            # 버튼 출력
            button1 = Button(self.duneroot, text="리뷰 작성", bg="powderblue", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.duneroot.label2 = Label(self.duneroot, font=("휴먼편지체", 35), text="DUNE", bg="white", fg="powderblue")
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

            f = open("MovieReview/DuneSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.duneroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '듄':
                    tmp += 20
                    label = Label(self.duneroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=460 + tmp)

            # 버튼 출력
            button1 = Button(self.duneroot, text="리뷰 작성", bg="white", command=self.writeReview)
            button1.place(x="520", y="25")
            self.duneroot.label2 = Label(self.duneroot, font=("휴먼편지체", 35), text="DUNE", bg="white", fg="powderblue")
            self.duneroot.label2.place(x="10", y="10")

        # 실행
        self.duneroot.mainloop()

    # ---------------------------------------------------------------------------------------------------

    def spirit_GUI(self):
        self.spiritroot = tkinter.Toplevel()  # 창 생성
        self.spiritroot.title('MoCookie')  # 창 제목
        self.spiritroot.geometry('600x600+340+20')
        self.spiritroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.spiritroot.configure(bg="white")

        self.spiritroot.label2 = Label(self.spiritroot, font=("휴먼편지체", 28), text="SpiritWalker", bg="white", fg="slategrey")
        self.spiritroot.label2.place(x="10", y="10")

        self.spiritroot.image = tkinter.PhotoImage(file="Poster/SpiritWalkerPoster.png")
        self.spiritroot.label = tkinter.Label(self.spiritroot, image=self.spiritroot.image, bg="white")
        self.spiritroot.label.place(x="195", y="55")

        self.spiritroot.label1 = Label(self.spiritroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.spiritroot.label1.place(x="233", y="360")

        self.spiritroot.label2= Label(self.spiritroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.24", bg="white")
        self.spiritroot.label2.place(x="234", y="395")

        self.spiritroot.label3 = Label(self.spiritroot, font=("휴먼편지체", 12), text="장르 : 액션", bg="white")
        self.spiritroot.label3.place(x="264", y="415")

        self.spiritroot.label3 = Label(self.spiritroot, font=("휴먼편지체", 12), text="등급 : 15세이상 관람가", bg="white")
        self.spiritroot.label3.place(x="230", y="435")

        self.spiritroot.label3 = Label(self.spiritroot, font=("휴먼편지체", 12), text="러닝타임 : 108분", bg="white")
        self.spiritroot.label3.place(x="241", y="455")

        self.spiritroot.label3 = Label(self.spiritroot, font=("휴먼편지체", 12), text="추천 좌석 : B~D, 4~11", bg="white")
        self.spiritroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.spiritroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.spiritroot, text="예매하기", font=("휴먼편지체", 11), bg="slategrey", command=self.spiritUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.spiritroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="slategrey", command=self.spiritreview)
        button1.place(x="310", y="530")

        # 실행
        self.spiritroot.mainloop()

    def spiritUrl(self): # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000072286'
        webbrowser.open_new(url)

    def spiritreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.spiritroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.spiritroot.mainBackL = tkinter.Label(self.spiritroot, image=self.spiritroot.mainBack)
            self.spiritroot.mainBackL.place(x=-2, y=-2)

            self.spiritroot.title('MoCookie')  # 창 제목
            self.spiritroot.geometry('600x600+340+20')
            self.spiritroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/SpiritWalkerReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.spiritroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '유체이탈자':
                    tmp += 20
                    label = Label(self.spiritroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=500 + tmp)

            # 버튼 출력
            button1 = Button(self.spiritroot, text="리뷰 작성", bg="slategrey", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.spiritroot.label2 = Label(self.spiritroot, font=("휴먼편지체", 28), text="SpiritWalker", bg="white", fg="slategrey")
            self.spiritroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.spiritroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.spiritroot.mainBackL = tkinter.Label(self.spiritroot, image=self.spiritroot.mainBack)
            self.spiritroot.mainBackL.place(x=-2, y=-2)

            self.spiritroot.title('MoCookie')  # 창 제목
            self.spiritroot.geometry('600x600+340+20')
            self.spiritroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/SpiritWalkerSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.spiritroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '유체이탈자':
                    tmp += 20
                    label = Label(self.spiritroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=500 + tmp)

            # 버튼 출력
            button1 = Button(self.spiritroot, text="리뷰 작성", bg="white", command=self.writeReview)
            button1.place(x="520", y="25")
            self.spiritroot.label2 = Label(self.spiritroot, font=("휴먼편지체", 28), text="SpiritWalker", bg="white", fg="slategrey")
            self.spiritroot.label2.place(x="10", y="10")

        # 실행
        self.spiritroot.mainloop()

    # ---------------------------------------------------------------------------------------------------
    def NothingSerious_GUI(self):
        self.NothingSeriousroot = tkinter.Toplevel()  # 창 생성
        self.NothingSeriousroot.title('MoCookie')  # 창 제목
        self.NothingSeriousroot.geometry('600x600+340+20')
        self.NothingSeriousroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.NothingSeriousroot.configure(bg="white")

        self.NothingSeriousroot.label2 = Label(self.NothingSeriousroot, font=("휴먼편지체", 28), text="NothingSerious", bg="white", fg="lightgreen")
        self.NothingSeriousroot.label2.place(x="10", y="10")

        self.NothingSeriousroot.image = tkinter.PhotoImage(file="Poster/NothingSeriousPoster.png")
        self.NothingSeriousroot.label = tkinter.Label(self.NothingSeriousroot, image=self.NothingSeriousroot.image, bg="white")
        self.NothingSeriousroot.label.place(x="195", y="55")

        self.NothingSeriousroot.label1 = Label(self.NothingSeriousroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.NothingSeriousroot.label1.place(x="233", y="360")

        self.NothingSeriousroot.label2= Label(self.NothingSeriousroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.24", bg="white")
        self.NothingSeriousroot.label2.place(x="234", y="395")

        self.NothingSeriousroot.label3 = Label(self.NothingSeriousroot, font=("휴먼편지체", 12), text="장르 : 멜로/로맨스, 코미디", bg="white")
        self.NothingSeriousroot.label3.place(x="223", y="415")

        self.NothingSeriousroot.label3 = Label(self.NothingSeriousroot, font=("휴먼편지체", 12), text="등급 : 15세이상 관람가", bg="white")
        self.NothingSeriousroot.label3.place(x="230", y="435")

        self.NothingSeriousroot.label3 = Label(self.NothingSeriousroot, font=("휴먼편지체", 12), text=" 러닝타임 : 95분", bg="white")
        self.NothingSeriousroot.label3.place(x="241", y="455")

        self.NothingSeriousroot.label3 = Label(self.NothingSeriousroot, font=("휴먼편지체", 12), text="추천 좌석 : G~H, 1~4 or 11~14", bg="white")
        self.NothingSeriousroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.NothingSeriousroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.NothingSeriousroot, text="예매하기", font=("휴먼편지체", 11), bg="lightgreen", command=self.NothingSeriousUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.NothingSeriousroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="lightgreen", command=self.NothingSeriousreview)
        button1.place(x="310", y="530")

        # 실행
        self.NothingSeriousroot.mainloop()

    def NothingSeriousUrl(self): # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000121306'
        webbrowser.open_new(url)

    def NothingSeriousreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.NothingSeriousroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.NothingSeriousroot.mainBackL = tkinter.Label(self.NothingSeriousroot, image=self.NothingSeriousroot.mainBack)
            self.NothingSeriousroot.mainBackL.place(x=-2, y=-2)

            self.NothingSeriousroot.title('MoCookie')  # 창 제목
            self.NothingSeriousroot.geometry('600x600+340+20')
            self.NothingSeriousroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/NothingSeriousReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.NothingSeriousroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == "연애 빠진 로맨스":
                    tmp += 20
                    label = Label(self.NothingSeriousroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=470 + tmp)

            # 버튼 출력
            button1 = Button(self.NothingSeriousroot, text="리뷰 작성", bg="lightgreen", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.NothingSeriousroot.label2 = Label(self.NothingSeriousroot, font=("휴먼편지체", 28), text="NothingSerious", bg="white", fg="lightgreen")
            self.NothingSeriousroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.NothingSeriousroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.NothingSeriousroot.mainBackL = tkinter.Label(self.NothingSeriousroot, image=self.NothingSeriousroot.mainBack)
            self.NothingSeriousroot.mainBackL.place(x=-2, y=-2)

            self.NothingSeriousroot.title('MoCookie')  # 창 제목
            self.NothingSeriousroot.geometry('600x600+340+20')
            self.NothingSeriousroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/NothingSeriousSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.NothingSeriousroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == "연애 빠진 로맨스":

                    tmp += 20
                    label = Label(self.NothingSeriousroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=530 + tmp)

            # 버튼 출력
            button1 = Button(self.NothingSeriousroot, text="리뷰 작성", bg="white", command=self.writeReview)
            button1.place(x="520", y="25")
            self.NothingSeriousroot.label2 = Label(self.NothingSeriousroot, font=("휴먼편지체", 28), text="NothingSerious", bg="white", fg="lightgreen")
            self.NothingSeriousroot.label2.place(x="10", y="10")

        # 실행
        self.NothingSeriousroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Encanto_GUI(self):
        self.Encantoroot = tkinter.Toplevel()  # 창 생성
        self.Encantoroot.title('MoCookie')  # 창 제목
        self.Encantoroot.geometry('600x600+340+20')
        self.Encantoroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Encantoroot.configure(bg="white")

        self.Encantoroot.label2 = Label(self.Encantoroot, font=("휴먼편지체", 28), text="Encanto", bg="white",
                                        fg="dodgerblue")
        self.Encantoroot.label2.place(x="10", y="10")

        self.Encantoroot.image = tkinter.PhotoImage(file="Poster/EncantoPoster.png")
        self.Encantoroot.label = tkinter.Label(self.Encantoroot, image=self.Encantoroot.image,
                                               bg="white")
        self.Encantoroot.label.place(x="195", y="55")

        self.Encantoroot.label1 = Label(self.Encantoroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Encantoroot.label1.place(x="233", y="360")

        self.Encantoroot.label2 = Label(self.Encantoroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.24",
                                        bg="white")
        self.Encantoroot.label2.place(x="234", y="395")

        self.Encantoroot.label3 = Label(self.Encantoroot, font=("휴먼편지체", 12), text="장르 : 애니메이션",
                                        bg="white")
        self.Encantoroot.label3.place(x="240", y="415")

        self.Encantoroot.label3 = Label(self.Encantoroot, font=("휴먼편지체", 12), text="등급 : 전체 관람가",
                                        bg="white")
        self.Encantoroot.label3.place(x="240", y="435")

        self.Encantoroot.label3 = Label(self.Encantoroot, font=("휴먼편지체", 12), text="러닝타임 : 109분", bg="white")
        self.Encantoroot.label3.place(x="241", y="455")

        self.Encantoroot.label3 = Label(self.Encantoroot, font=("휴먼편지체", 12),
                                        text="추천 좌석 : D~H, 3~6 or 9~12", bg="white")
        self.Encantoroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Encantoroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Encantoroot, text="예매하기", font=("휴먼편지체", 11), bg="dodgerblue",
                         command=self.EncantoUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Encantoroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="dodgerblue",
                         command=self.Encantoreview)
        button1.place(x="310", y="530")

        # 실행
        self.Encantoroot.mainloop()

    def EncantoUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125515'
        webbrowser.open_new(url)

    def Encantoreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Encantoroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Encantoroot.mainBackL = tkinter.Label(self.Encantoroot,
                                                       image=self.Encantoroot.mainBack)
            self.Encantoroot.mainBackL.place(x=-2, y=-2)

            self.Encantoroot.title('MoCookie')  # 창 제목
            self.Encantoroot.geometry('600x600+340+20')
            self.Encantoroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/EncantoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Encantoroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '엔칸토-마법의 세계':
                    tmp += 20
                    label = Label(self.Encantoroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=470 + tmp)

            # 버튼 출력
            button1 = Button(self.Encantoroot, text="리뷰 작성", bg="dodgerblue", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Encantoroot.label2 = Label(self.Encantoroot, font=("휴먼편지체", 28), text="Encanto",
                                            bg="white", fg="dodgerblue")
            self.Encantoroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Encantoroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Encantoroot.mainBackL = tkinter.Label(self.Encantoroot,
                                                       image=self.Encantoroot.mainBack)
            self.Encantoroot.mainBackL.place(x=-2, y=-2)

            self.Encantoroot.title('MoCookie')  # 창 제목
            self.Encantoroot.geometry('600x600+340+20')
            self.Encantoroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/EncantoSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Encantoroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '엔칸토-마법의 세계':
                    tmp += 20
                    label = Label(self.Encantoroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=480 + tmp)

            # 버튼 출력
            button1 = Button(self.Encantoroot, text="리뷰 작성", bg="dodgerblue", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Encantoroot.label2 = Label(self.Encantoroot, font=("휴먼편지체", 28), text="Encanto",
                                            bg="white", fg="dodgerblue")
            self.Encantoroot.label2.place(x="10", y="10")

        # 실행
        self.Encantoroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Eternals_GUI(self):
        self.Eternalsroot = tkinter.Toplevel()  # 창 생성
        self.Eternalsroot.title('MoCookie')  # 창 제목
        self.Eternalsroot.geometry('600x600+340+20')
        self.Eternalsroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Eternalsroot.configure(bg="white")

        self.Eternalsroot.label2 = Label(self.Eternalsroot, font=("휴먼편지체", 28), text="Eternals", bg="white",
                                         fg="sienna")
        self.Eternalsroot.label2.place(x="10", y="10")

        self.Eternalsroot.image = tkinter.PhotoImage(file="Poster/EternalsPoster.png")
        self.Eternalsroot.label = tkinter.Label(self.Eternalsroot, image=self.Eternalsroot.image,
                                                bg="white")
        self.Eternalsroot.label.place(x="195", y="55")

        self.Eternalsroot.label1 = Label(self.Eternalsroot, font=("휴먼편지체", 17), text="쿠키 영상 2개", bg="white")
        self.Eternalsroot.label1.place(x="233", y="360")

        self.Eternalsroot.label2 = Label(self.Eternalsroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.03",
                                         bg="white")
        self.Eternalsroot.label2.place(x="234", y="395")

        self.Eternalsroot.label3 = Label(self.Eternalsroot, font=("휴먼편지체", 12), text="장르 : 액션, 드라마, 판타지",
                                         bg="white")
        self.Eternalsroot.label3.place(x="215", y="415")

        self.Eternalsroot.label3 = Label(self.Eternalsroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                         bg="white")
        self.Eternalsroot.label3.place(x="230", y="435")

        self.Eternalsroot.label3 = Label(self.Eternalsroot, font=("휴먼편지체", 12), text="러닝타임 : 155분", bg="white")
        self.Eternalsroot.label3.place(x="241", y="455")

        self.Eternalsroot.label3 = Label(self.Eternalsroot, font=("휴먼편지체", 12),
                                         text="추천 좌석 : B~C, 5~10", bg="white")
        self.Eternalsroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Eternalsroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Eternalsroot, text="예매하기", font=("휴먼편지체", 11), bg="sienna",
                         command=self.EternalsUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Eternalsroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="sienna",
                         command=self.Eternalsreview)
        button1.place(x="310", y="530")

        # 실행
        self.Eternalsroot.mainloop()

    def EternalsUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125013'
        webbrowser.open_new(url)

    def Eternalsreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Eternalsroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Eternalsroot.mainBackL = tkinter.Label(self.Eternalsroot,
                                                        image=self.Eternalsroot.mainBack)
            self.Eternalsroot.mainBackL.place(x=-2, y=-2)

            self.Eternalsroot.title('MoCookie')  # 창 제목
            self.Eternalsroot.geometry('600x600+340+20')
            self.Eternalsroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/EternalsReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Eternalsroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '이터널스':
                    tmp += 20
                    label = Label(self.Eternalsroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=480 + tmp)

            # 버튼 출력
            button1 = Button(self.Eternalsroot, text="리뷰 작성", bg="sienna", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Eternalsroot.label2 = Label(self.Eternalsroot, font=("휴먼편지체", 28), text="Eternals",
                                             bg="white", fg="sienna")
            self.Eternalsroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Eternalsroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Eternalsroot.mainBackL = tkinter.Label(self.Eternalsroot,
                                                        image=self.Eternalsroot.mainBack)
            self.Eternalsroot.mainBackL.place(x=-2, y=-2)

            self.Eternalsroot.title('MoCookie')  # 창 제목
            self.Eternalsroot.geometry('600x600+340+20')
            self.Eternalsroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/EternalsSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Eternalsroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '이터널스':
                    tmp += 20
                    label = Label(self.Eternalsroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=490 + tmp)

            # 버튼 출력
            button1 = Button(self.Eternalsroot, text="리뷰 작성", bg="sienna", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Eternalsroot.label2 = Label(self.Eternalsroot, font=("휴먼편지체", 28), text="Eternals",
                                             bg="white", fg="sienna")
            self.Eternalsroot.label2.place(x="10", y="10")

        # 실행
        self.Eternalsroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Janr_GUI(self):
        self.Janrroot = tkinter.Toplevel()  # 창 생성
        self.Janrroot.title('MoCookie')  # 창 제목
        self.Janrroot.geometry('600x600+340+20')
        self.Janrroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Janrroot.configure(bg="white")

        self.Janrroot.label2 = Label(self.Janrroot, font=("휴먼편지체", 28), text="Genre Romance", bg="white",
                                     fg="palevioletred")
        self.Janrroot.label2.place(x="10", y="10")

        self.Janrroot.image = tkinter.PhotoImage(file="Poster/JanrPoster.png")
        self.Janrroot.label = tkinter.Label(self.Janrroot, image=self.Janrroot.image,
                                            bg="white")
        self.Janrroot.label.place(x="195", y="55")

        self.Janrroot.label1 = Label(self.Janrroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Janrroot.label1.place(x="233", y="360")

        self.Janrroot.label2 = Label(self.Janrroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.17",
                                     bg="white")
        self.Janrroot.label2.place(x="234", y="395")

        self.Janrroot.label3 = Label(self.Janrroot, font=("휴먼편지체", 12), text="장르 : 드라마, 코미디",
                                     bg="white")
        self.Janrroot.label3.place(x="240", y="415")

        self.Janrroot.label3 = Label(self.Janrroot, font=("휴먼편지체", 12), text="등급 : 15세이상 관람가",
                                     bg="white")
        self.Janrroot.label3.place(x="230", y="435")

        self.Janrroot.label3 = Label(self.Janrroot, font=("휴먼편지체", 12), text="러닝타임 : 113분", bg="white")
        self.Janrroot.label3.place(x="241", y="455")

        self.Janrroot.label3 = Label(self.Janrroot, font=("휴먼편지체", 12),
                                     text="추천 좌석 : F~G, 6~9", bg="white")
        self.Janrroot.label3.place(x="235", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Janrroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Janrroot, text="예매하기", font=("휴먼편지체", 11), bg="palevioletred",
                         command=self.JanrUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Janrroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="palevioletred",
                         command=self.Janrreview)
        button1.place(x="310", y="530")

        # 실행
        self.Janrroot.mainloop()

    def JanrUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000073552'
        webbrowser.open_new(url)

    def Janrreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Janrroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Janrroot.mainBackL = tkinter.Label(self.Janrroot,
                                                    image=self.Janrroot.mainBack)
            self.Janrroot.mainBackL.place(x=-2, y=-2)

            self.Janrroot.title('MoCookie')  # 창 제목
            self.Janrroot.geometry('600x600+340+20')
            self.Janrroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/JanrReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Janrroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '장르만 로맨스':
                    tmp += 20
                    label = Label(self.Janrroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=510 + tmp)

            # 버튼 출력
            button1 = Button(self.Janrroot, text="리뷰 작성", bg="palevioletred", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Janrroot.label2 = Label(self.Janrroot, font=("휴먼편지체", 28), text="Genre Romance",
                                         bg="white", fg="palevioletred")
            self.Janrroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Janrroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Janrroot.mainBackL = tkinter.Label(self.Janrroot,
                                                    image=self.Janrroot.mainBack)
            self.Janrroot.mainBackL.place(x=-2, y=-2)

            self.Janrroot.title('MoCookie')  # 창 제목
            self.Janrroot.geometry('600x600+340+20')
            self.Janrroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/JanrSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Janrroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '장르만 로맨스':
                    tmp += 20
                    label = Label(self.Janrroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=485 + tmp)

            # 버튼 출력
            button1 = Button(self.Janrroot, text="리뷰 작성", bg="palevioletred", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Janrroot.label2 = Label(self.Janrroot, font=("휴먼편지체", 28), text="Genre Romance",
                                         bg="white", fg="palevioletred")
            self.Janrroot.label2.place(x="10", y="10")

        # 실행
        self.Janrroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def French_GUI(self):
        self.Frenchroot = tkinter.Toplevel()  # 창 생성
        self.Frenchroot.title('MoCookie')  # 창 제목
        self.Frenchroot.geometry('600x600+340+20')
        self.Frenchroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Frenchroot.configure(bg="white")

        self.Frenchroot.label2 = Label(self.Frenchroot, font=("휴먼편지체", 28), text="FrenchDispatch", bg="white",
                                       fg="darkturquoise")
        self.Frenchroot.label2.place(x="10", y="10")

        self.Frenchroot.image = tkinter.PhotoImage(file="Poster/FrenchPoster.png")
        self.Frenchroot.label = tkinter.Label(self.Frenchroot, image=self.Frenchroot.image,
                                              bg="white")
        self.Frenchroot.label.place(x="195", y="55")

        self.Frenchroot.label1 = Label(self.Frenchroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Frenchroot.label1.place(x="233", y="360")

        self.Frenchroot.label2 = Label(self.Frenchroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.18",
                                       bg="white")
        self.Frenchroot.label2.place(x="234", y="395")

        self.Frenchroot.label3 = Label(self.Frenchroot, font=("휴먼편지체", 12), text="장르 : 코미디, 드라마, 멜로/로맨스",
                                       bg="white")
        self.Frenchroot.label3.place(x="200", y="415")

        self.Frenchroot.label3 = Label(self.Frenchroot, font=("휴먼편지체", 12), text="등급 : 15세이상 관람가",
                                       bg="white")
        self.Frenchroot.label3.place(x="230", y="435")

        self.Frenchroot.label3 = Label(self.Frenchroot, font=("휴먼편지체", 12), text="러닝타임 : 107분", bg="white")
        self.Frenchroot.label3.place(x="241", y="455")

        self.Frenchroot.label3 = Label(self.Frenchroot, font=("휴먼편지체", 12),
                                       text="추천 좌석 : G~H, 1~4 or 11~14", bg="white")
        self.Frenchroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Frenchroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Frenchroot, text="예매하기", font=("휴먼편지체", 11), bg="darkturquoise",
                         command=self.FrenchUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Frenchroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="darkturquoise",
                         command=self.Frenchreview)
        button1.place(x="310", y="530")

        # 실행
        self.Frenchroot.mainloop()

    def FrenchUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125585'
        webbrowser.open_new(url)

    def Frenchreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Frenchroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Frenchroot.mainBackL = tkinter.Label(self.Frenchroot,
                                                      image=self.Frenchroot.mainBack)
            self.Frenchroot.mainBackL.place(x=-2, y=-2)

            self.Frenchroot.title('MoCookie')  # 창 제목
            self.Frenchroot.geometry('600x600+340+20')
            self.Frenchroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/FrenchReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Frenchroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '프렌치 디스패치':
                    tmp += 20
                    label = Label(self.Frenchroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=505 + tmp)

            # 버튼 출력
            button1 = Button(self.Frenchroot, text="리뷰 작성", bg="darkturquoise", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Frenchroot.label2 = Label(self.Frenchroot, font=("휴먼편지체", 28), text="FrenchDispatch",
                                           bg="white", fg="darkturquoise")
            self.Frenchroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Frenchroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Frenchroot.mainBackL = tkinter.Label(self.Frenchroot,
                                                      image=self.Frenchroot.mainBack)
            self.Frenchroot.mainBackL.place(x=-2, y=-2)

            self.Frenchroot.title('MoCookie')  # 창 제목
            self.Frenchroot.geometry('600x600+340+20')
            self.Frenchroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/FrenchSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Frenchroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '프렌치 디스패치':
                    tmp += 20
                    label = Label(self.Frenchroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=370 + tmp)

            # 버튼 출력
            button1 = Button(self.Frenchroot, text="리뷰 작성", bg="darkturquoise", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Frenchroot.label2 = Label(self.Frenchroot, font=("휴먼편지체", 28), text="FrenchDispatch",
                                           bg="white", fg="darkturquoise")
            self.Frenchroot.label2.place(x="10", y="10")

        # 실행
        self.Frenchroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Coming_GUI(self):
        self.Comingroot = tkinter.Toplevel()  # 창 생성
        self.Comingroot.title('MoCookie')  # 창 제목
        self.Comingroot.geometry('600x600+340+20')
        self.Comingroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Comingroot.configure(bg="white")

        self.Comingroot.label2 = Label(self.Comingroot, font=("휴먼편지체", 28), text="Coming to you", bg="white",
                                       fg="hotpink")
        self.Comingroot.label2.place(x="10", y="10")

        self.Comingroot.image = tkinter.PhotoImage(file="Poster/ComingPoster.png")
        self.Comingroot.label = tkinter.Label(self.Comingroot, image=self.Comingroot.image,
                                              bg="white")
        self.Comingroot.label.place(x="195", y="55")

        self.Comingroot.label1 = Label(self.Comingroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Comingroot.label1.place(x="233", y="360")

        self.Comingroot.label2 = Label(self.Comingroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.17",
                                       bg="white")
        self.Comingroot.label2.place(x="234", y="395")

        self.Comingroot.label3 = Label(self.Comingroot, font=("휴먼편지체", 12), text="장르 : 다큐멘터리",
                                       bg="white")
        self.Comingroot.label3.place(x="243", y="415")

        self.Comingroot.label3 = Label(self.Comingroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                       bg="white")
        self.Comingroot.label3.place(x="230", y="435")

        self.Comingroot.label3 = Label(self.Comingroot, font=("휴먼편지체", 12), text=" 러닝타임 : 93분", bg="white")
        self.Comingroot.label3.place(x="241", y="455")

        self.Comingroot.label3 = Label(self.Comingroot, font=("휴먼편지체", 12),
                                       text="추천 좌석 : F~G, 6~9", bg="white")
        self.Comingroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Comingroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Comingroot, text="예매하기", font=("휴먼편지체", 11), bg="hotpink",
                         command=self.ComingUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Comingroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="hotpink",
                         command=self.Comingreview)
        button1.place(x="310", y="530")

        # 실행
        self.Comingroot.mainloop()

    def ComingUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125573'
        webbrowser.open_new(url)

    def Comingreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Comingroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Comingroot.mainBackL = tkinter.Label(self.Comingroot,
                                                      image=self.Comingroot.mainBack)
            self.Comingroot.mainBackL.place(x=-2, y=-2)

            self.Comingroot.title('MoCookie')  # 창 제목
            self.Comingroot.geometry('600x600+340+20')
            self.Comingroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/ComingReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Comingroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '너에게 가는 길':
                    tmp += 20
                    label = Label(self.Comingroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=485 + tmp)

            # 버튼 출력
            button1 = Button(self.Comingroot, text="리뷰 작성", bg="hotpink", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Comingroot.label2 = Label(self.Comingroot, font=("휴먼편지체", 28), text="Coming to you",
                                           bg="white", fg="hotpink")
            self.Comingroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Comingroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Comingroot.mainBackL = tkinter.Label(self.Comingroot,
                                                      image=self.Comingroot.mainBack)
            self.Comingroot.mainBackL.place(x=-2, y=-2)

            self.Comingroot.title('MoCookie')  # 창 제목
            self.Comingroot.geometry('600x600+340+20')
            self.Comingroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/ComingSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Comingroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '너에게 가는 길':
                    tmp += 20
                    label = Label(self.Comingroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=350 + tmp)

            # 버튼 출력
            button1 = Button(self.Comingroot, text="리뷰 작성", bg="hotpink", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Comingroot.label2 = Label(self.Comingroot, font=("휴먼편지체", 28), text="Coming to you",
                                           bg="white", fg="hotpink")
            self.Comingroot.label2.place(x="10", y="10")

        # 실행
        self.Comingroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Lime_GUI(self):
        self.Limeroot = tkinter.Toplevel()  # 창 생성
        self.Limeroot.title('MoCookie')  # 창 제목
        self.Limeroot.geometry('600x600+340+20')
        self.Limeroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Limeroot.configure(bg="white")

        self.Limeroot.label2 = Label(self.Limeroot, font=("휴먼편지체", 28), text="LimeCrime", bg="white",
                                     fg="lime")
        self.Limeroot.label2.place(x="10", y="10")

        self.Limeroot.image = tkinter.PhotoImage(file="Poster/LimePoster.png")
        self.Limeroot.label = tkinter.Label(self.Limeroot, image=self.Limeroot.image,
                                            bg="white")
        self.Limeroot.label.place(x="195", y="55")

        self.Limeroot.label1 = Label(self.Limeroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Limeroot.label1.place(x="233", y="360")

        self.Limeroot.label2 = Label(self.Limeroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.25",
                                     bg="white")
        self.Limeroot.label2.place(x="234", y="395")

        self.Limeroot.label3 = Label(self.Limeroot, font=("휴먼편지체", 12), text="장르 : 드라마",
                                     bg="white")
        self.Limeroot.label3.place(x="253", y="415")

        self.Limeroot.label3 = Label(self.Limeroot, font=("휴먼편지체", 12), text="등급 : 15세이상 관람가",
                                     bg="white")
        self.Limeroot.label3.place(x="230", y="435")

        self.Limeroot.label3 = Label(self.Limeroot, font=("휴먼편지체", 12), text=" 러닝타임 : 82분", bg="white")
        self.Limeroot.label3.place(x="241", y="455")

        self.Limeroot.label3 = Label(self.Limeroot, font=("휴먼편지체", 12),
                                     text="추천 좌석 : F~G, 6~9", bg="white")
        self.Limeroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Limeroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Limeroot, text="예매하기", font=("휴먼편지체", 11), bg="lime",
                         command=self.LimeUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Limeroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="lime",
                         command=self.Limereview)
        button1.place(x="310", y="530")

        # 실행
        self.Limeroot.mainloop()

    def LimeUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125620'
        webbrowser.open_new(url)

    def Limereview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Limeroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Limeroot.mainBackL = tkinter.Label(self.Limeroot,
                                                    image=self.Limeroot.mainBack)
            self.Limeroot.mainBackL.place(x=-2, y=-2)

            self.Limeroot.title('MoCookie')  # 창 제목
            self.Limeroot.geometry('600x600+340+20')
            self.Limeroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/LimeReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Limeroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '라임 크라임':
                    tmp += 20
                    label = Label(self.Limeroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=415 + tmp)

            # 버튼 출력
            button1 = Button(self.Limeroot, text="리뷰 작성", bg="lime", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Limeroot.label2 = Label(self.Limeroot, font=("휴먼편지체", 28), text="LimeCrime",
                                         bg="white", fg="lime")
            self.Limeroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Limeroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Limeroot.mainBackL = tkinter.Label(self.Limeroot,
                                                    image=self.Limeroot.mainBack)
            self.Limeroot.mainBackL.place(x=-2, y=-2)

            self.Limeroot.title('MoCookie')  # 창 제목
            self.Limeroot.geometry('600x600+340+20')
            self.Limeroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/LimeSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Limeroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '라임 크라임':
                    tmp += 20
                    label = Label(self.Limeroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=415 + tmp)

            # 버튼 출력
            button1 = Button(self.Limeroot, text="리뷰 작성", bg="lime", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Limeroot.label2 = Label(self.Limeroot, font=("휴먼편지체", 28), text="LimeCrime",
                                         bg="white", fg="lime")
            self.Limeroot.label2.place(x="10", y="10")

        # 실행
        self.Limeroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Log_GUI(self):
        self.Logroot = tkinter.Toplevel()  # 창 생성
        self.Logroot.title('MoCookie')  # 창 제목
        self.Logroot.geometry('600x600+340+20')
        self.Logroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Logroot.configure(bg="white")

        self.Logroot.label2 = Label(self.Logroot, font=("휴먼편지체", 28), text="Logbook", bg="white",
                                    fg="darkslateblue")
        self.Logroot.label2.place(x="10", y="10")

        self.Logroot.image = tkinter.PhotoImage(file="Poster/LogPoster.png")
        self.Logroot.label = tkinter.Label(self.Logroot, image=self.Logroot.image,
                                           bg="white")
        self.Logroot.label.place(x="195", y="55")

        self.Logroot.label1 = Label(self.Logroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Logroot.label1.place(x="233", y="360")

        self.Logroot.label2 = Label(self.Logroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.24",
                                    bg="white")
        self.Logroot.label2.place(x="234", y="395")

        self.Logroot.label3 = Label(self.Logroot, font=("휴먼편지체", 12), text="장르 : 다큐멘터리",
                                    bg="white")
        self.Logroot.label3.place(x="243", y="415")

        self.Logroot.label3 = Label(self.Logroot, font=("휴먼편지체", 12), text="등급 : 전체 관람가",
                                    bg="white")
        self.Logroot.label3.place(x="240", y="435")

        self.Logroot.label3 = Label(self.Logroot, font=("휴먼편지체", 12), text="러닝타임 : 100분", bg="white")
        self.Logroot.label3.place(x="241", y="455")

        self.Logroot.label3 = Label(self.Logroot, font=("휴먼편지체", 12),
                                    text="추천 좌석 : F~G, 6~9", bg="white")
        self.Logroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Logroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Logroot, text="예매하기", font=("휴먼편지체", 11), bg="darkslateblue",
                         command=self.LogUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Logroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="darkslateblue",
                         command=self.Logreview)
        button1.place(x="310", y="530")

        # 실행
        self.Logroot.mainloop()

    def LogUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000073094'
        webbrowser.open_new(url)

    def Logreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Logroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Logroot.mainBackL = tkinter.Label(self.Logroot,
                                                   image=self.Logroot.mainBack)
            self.Logroot.mainBackL.place(x=-2, y=-2)

            self.Logroot.title('MoCookie')  # 창 제목
            self.Logroot.geometry('600x600+340+20')
            self.Logroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/LogReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Logroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '로그북':
                    tmp += 20
                    label = Label(self.Logroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=415 + tmp)

            # 버튼 출력
            button1 = Button(self.Logroot, text="리뷰 작성", bg="darkslateblue", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Logroot.label2 = Label(self.Logroot, font=("휴먼편지체", 28), text="Logbook",
                                        bg="white", fg="darkslateblue")
            self.Logroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Logroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Logroot.mainBackL = tkinter.Label(self.Logroot,
                                                   image=self.Logroot.mainBack)
            self.Logroot.mainBackL.place(x=-2, y=-2)

            self.Logroot.title('MoCookie')  # 창 제목
            self.Logroot.geometry('600x600+340+20')
            self.Logroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/LogSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Logroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '로그북':
                    tmp += 20
                    label = Label(self.Logroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=415 + tmp)

            # 버튼 출력
            button1 = Button(self.Logroot, text="리뷰 작성", bg="darkslateblue", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Logroot.label2 = Label(self.Logroot, font=("휴먼편지체", 28), text="Logbook",
                                        bg="white", fg="darkslateblue")
            self.Logroot.label2.place(x="10", y="10")

        # 실행
        self.Logroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Dear_GUI(self):
        self.Dearroot = tkinter.Toplevel()  # 창 생성
        self.Dearroot.title('MoCookie')  # 창 제목
        self.Dearroot.geometry('600x600+340+20')
        self.Dearroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Dearroot.configure(bg="white")

        self.Dearroot.label2 = Label(self.Dearroot, font=("휴먼편지체", 28), text="Dear Evan Hansen", bg="white",
                                     fg="cornflowerblue")
        self.Dearroot.label2.place(x="10", y="10")

        self.Dearroot.image = tkinter.PhotoImage(file="Poster/DearPoster.png")
        self.Dearroot.label = tkinter.Label(self.Dearroot, image=self.Dearroot.image,
                                            bg="white")
        self.Dearroot.label.place(x="195", y="55")

        self.Dearroot.label1 = Label(self.Dearroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Dearroot.label1.place(x="233", y="360")

        self.Dearroot.label2 = Label(self.Dearroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.17",
                                     bg="white")
        self.Dearroot.label2.place(x="234", y="395")

        self.Dearroot.label3 = Label(self.Dearroot, font=("휴먼편지체", 12), text="장르 : 뮤지컬, 드라마",
                                     bg="white")
        self.Dearroot.label3.place(x="235", y="415")

        self.Dearroot.label3 = Label(self.Dearroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                     bg="white")
        self.Dearroot.label3.place(x="230", y="435")

        self.Dearroot.label3 = Label(self.Dearroot, font=("휴먼편지체", 12), text="러닝타임 : 137분", bg="white")
        self.Dearroot.label3.place(x="241", y="455")

        self.Dearroot.label3 = Label(self.Dearroot, font=("휴먼편지체", 12),
                                     text="추천 좌석 : G~I, 4~11", bg="white")
        self.Dearroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Dearroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Dearroot, text="예매하기", font=("휴먼편지체", 11), bg="cornflowerblue",
                         command=self.DearUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Dearroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="cornflowerblue",
                         command=self.Dearreview)
        button1.place(x="310", y="530")

        # 실행
        self.Dearroot.mainloop()

    def DearUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125514'
        webbrowser.open_new(url)

    def Dearreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Dearroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Dearroot.mainBackL = tkinter.Label(self.Dearroot,
                                                    image=self.Dearroot.mainBack)
            self.Dearroot.mainBackL.place(x=-2, y=-2)

            self.Dearroot.title('MoCookie')  # 창 제목
            self.Dearroot.geometry('600x600+340+20')
            self.Dearroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/DearReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Dearroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '디어 에반 핸슨':
                    tmp += 20
                    label = Label(self.Dearroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=500 + tmp)

            # 버튼 출력
            button1 = Button(self.Dearroot, text="리뷰 작성", bg="cornflowerblue", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Dearroot.label2 = Label(self.Dearroot, font=("휴먼편지체", 28), text="Dear Evan Hansen",
                                         bg="white", fg="cornflowerblue")
            self.Dearroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Dearroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Dearroot.mainBackL = tkinter.Label(self.Dearroot,
                                                    image=self.Dearroot.mainBack)
            self.Dearroot.mainBackL.place(x=-2, y=-2)

            self.Dearroot.title('MoCookie')  # 창 제목
            self.Dearroot.geometry('600x600+340+20')
            self.Dearroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/DearSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Dearroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '디어 에반 핸슨':
                    tmp += 20
                    label = Label(self.Dearroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=490 + tmp)

            # 버튼 출력
            button1 = Button(self.Dearroot, text="리뷰 작성", bg="cornflowerblue", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Dearroot.label2 = Label(self.Dearroot, font=("휴먼편지체", 28), text="Dear Evan Hansen",
                                         bg="white", fg="cornflowerblue")
            self.Dearroot.label2.place(x="10", y="10")

        # 실행
        self.Dearroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Hobit_GUI(self):
        self.Hobitroot = tkinter.Toplevel()  # 창 생성
        self.Hobitroot.title('MoCookie')  # 창 제목
        self.Hobitroot.geometry('600x600+340+20')
        self.Hobitroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Hobitroot.configure(bg="white")

        self.Hobitroot.label2 = Label(self.Hobitroot, font=("휴먼편지체", 28), text="Hobit", bg="white",
                                      fg="peru")
        self.Hobitroot.label2.place(x="10", y="10")

        self.Hobitroot.image = tkinter.PhotoImage(file="Poster/HobitPoster.png")
        self.Hobitroot.label = tkinter.Label(self.Hobitroot, image=self.Hobitroot.image,
                                             bg="white")
        self.Hobitroot.label.place(x="195", y="55")

        self.Hobitroot.label1 = Label(self.Hobitroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Hobitroot.label1.place(x="233", y="360")

        self.Hobitroot.label2 = Label(self.Hobitroot, font=("휴먼편지체", 12), text="개봉일 : 2013.12.12",
                                      bg="white")
        self.Hobitroot.label2.place(x="234", y="395")

        self.Hobitroot.label3 = Label(self.Hobitroot, font=("휴먼편지체", 12), text="장르 : 판타지, 모험, 드라마",
                                      bg="white")
        self.Hobitroot.label3.place(x="223", y="415")

        self.Hobitroot.label3 = Label(self.Hobitroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                      bg="white")
        self.Hobitroot.label3.place(x="230", y="435")

        self.Hobitroot.label3 = Label(self.Hobitroot, font=("휴먼편지체", 12), text="러닝타임 : 161분", bg="white")
        self.Hobitroot.label3.place(x="241", y="455")

        self.Hobitroot.label3 = Label(self.Hobitroot, font=("휴먼편지체", 12),
                                      text="추천 좌석 : D~G, 3~6 or 9~12", bg="white")
        self.Hobitroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Hobitroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Hobitroot, text="예매하기", font=("휴먼편지체", 11), bg="peru",
                         command=self.HobitUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Hobitroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="peru",
                         command=self.Hobitreview)
        button1.place(x="310", y="530")

        # 실행
        self.Hobitroot.mainloop()

    def HobitUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000043214'
        webbrowser.open_new(url)

    def Hobitreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Hobitroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Hobitroot.mainBackL = tkinter.Label(self.Hobitroot,
                                                     image=self.Hobitroot.mainBack)
            self.Hobitroot.mainBackL.place(x=-2, y=-2)

            self.Hobitroot.title('MoCookie')  # 창 제목
            self.Hobitroot.geometry('600x600+340+20')
            self.Hobitroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/HobitReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Hobitroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '호빗: 스마우그의 폐허':
                    tmp += 20
                    label = Label(self.Hobitroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=480 + tmp)

            # 버튼 출력
            button1 = Button(self.Hobitroot, text="리뷰 작성", bg="peru", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Hobitroot.label2 = Label(self.Hobitroot, font=("휴먼편지체", 28), text="Hobit",
                                          bg="white", fg="peru")
            self.Hobitroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Hobitroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Hobitroot.mainBackL = tkinter.Label(self.Hobitroot,
                                                     image=self.Hobitroot.mainBack)
            self.Hobitroot.mainBackL.place(x=-2, y=-2)

            self.Hobitroot.title('MoCookie')  # 창 제목
            self.Hobitroot.geometry('600x600+340+20')
            self.Hobitroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/HobitSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Hobitroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '호빗: 스마우그의 폐허':
                    tmp += 20
                    label = Label(self.Hobitroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=350 + tmp)

            # 버튼 출력
            button1 = Button(self.Hobitroot, text="리뷰 작성", bg="peru", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Hobitroot.label2 = Label(self.Hobitroot, font=("휴먼편지체", 28), text="Hobit",
                                          bg="white", fg="peru")
            self.Hobitroot.label2.place(x="10", y="10")

        # 실행
        self.Hobitroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Bouquet_GUI(self):
        self.Bouquetroot = tkinter.Toplevel()  # 창 생성
        self.Bouquetroot.title('MoCookie')  # 창 제목
        self.Bouquetroot.geometry('600x600+340+20')
        self.Bouquetroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Bouquetroot.configure(bg="white")

        self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 25), text="We Made a Beautiful Bouquet",
                                        bg="white",
                                        fg="lightpink")
        self.Bouquetroot.label2.place(x="10", y="10")

        self.Bouquetroot.image = tkinter.PhotoImage(file="../MoCookie/Poster/BouquetPoster.png")
        self.Bouquetroot.label = tkinter.Label(self.Bouquetroot, image=self.Bouquetroot.image,
                                               bg="white")
        self.Bouquetroot.label.place(x="195", y="55")

        self.Bouquetroot.label1 = Label(self.Bouquetroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Bouquetroot.label1.place(x="233", y="360")

        self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="개봉일 : 2013.07.14",
                                        bg="white")
        self.Bouquetroot.label2.place(x="234", y="395")

        self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="장르 : 멜로/로맨스",
                                        bg="white")
        self.Bouquetroot.label3.place(x="243", y="415")

        self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                        bg="white")
        self.Bouquetroot.label3.place(x="230", y="435")

        self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="러닝타임 : 123분", bg="white")
        self.Bouquetroot.label3.place(x="241", y="455")

        self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12),
                                        text="추천 좌석 : G~H, 1~4 or 11~14", bg="white")
        self.Bouquetroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Bouquetroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Bouquetroot, text="예매하기", font=("휴먼편지체", 11), bg="lightpink",
                         command=self.BouquetUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Bouquetroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="lightpink",
                         command=self.Bouquetreview)
        button1.place(x="310", y="530")

        # 실행
        self.Bouquetroot.mainloop()

    def BouquetUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000124288'
        webbrowser.open_new(url)

    def Bouquetreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Bouquetroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Bouquetroot.mainBackL = tkinter.Label(self.Bouquetroot,
                                                       image=self.Bouquetroot.mainBack)
            self.Bouquetroot.mainBackL.place(x=-2, y=-2)

            self.Bouquetroot.title('MoCookie')  # 창 제목
            self.Bouquetroot.geometry('600x600+340+20')
            self.Bouquetroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("../MoCookie/MovieReview/BouquetReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Bouquetroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '꽃다발 같은 사랑을 했다':
                    tmp += 20
                    label = Label(self.Bouquetroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=460 + tmp)

            # 버튼 출력
            button1 = Button(self.Bouquetroot, text="리뷰 작성", bg="lightpink", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 25), text="We Made a Beautiful Bouquet",
                                            bg="white", fg="lightpink")
            self.Bouquetroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Bouquetroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Bouquetroot.mainBackL = tkinter.Label(self.Bouquetroot,
                                                       image=self.Bouquetroot.mainBack)
            self.Bouquetroot.mainBackL.place(x=-2, y=-2)

            self.Bouquetroot.title('MoCookie')  # 창 제목
            self.Bouquetroot.geometry('600x600+340+20')
            self.Bouquetroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("../MoCookie/MovieReview/BouquetSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Bouquetroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '꽃다발 같은 사랑을 했다':
                    tmp += 20
                    label = Label(self.Bouquetroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=325 + tmp)

            # 버튼 출력
            button1 = Button(self.Bouquetroot, text="리뷰 작성", bg="lightpink", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 25), text="We Made a Beautiful Bouquet",
                                            bg="white", fg="lightpink")
            self.Bouquetroot.label2.place(x="10", y="10")

        # 실행
        self.Bouquetroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def YourName_GUI(self):
        self.YourNameroot = tkinter.Toplevel()  # 창 생성
        self.YourNameroot.title('MoCookie')  # 창 제목
        self.YourNameroot.geometry('600x600+340+20')
        self.YourNameroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.YourNameroot.configure(bg="white")

        self.YourNameroot.label2 = Label(self.YourNameroot, font=("휴먼편지체", 28), text="YourName",
                                         bg="white",
                                         fg="deepskyblue")
        self.YourNameroot.label2.place(x="10", y="10")

        self.YourNameroot.image = tkinter.PhotoImage(file="../MoCookie/Poster/YourNamePoster.png")
        self.YourNameroot.label = tkinter.Label(self.YourNameroot, image=self.YourNameroot.image,
                                                bg="white")
        self.YourNameroot.label.place(x="195", y="55")

        self.YourNameroot.label1 = Label(self.YourNameroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.YourNameroot.label1.place(x="233", y="360")

        self.YourNameroot.label2 = Label(self.YourNameroot, font=("휴먼편지체", 12), text="개봉일 : 2021.08.08",
                                         bg="white")
        self.YourNameroot.label2.place(x="234", y="395")

        self.YourNameroot.label3 = Label(self.YourNameroot, font=("휴먼편지체", 12), text="장르 : 애니메이션",
                                         bg="white")
        self.YourNameroot.label3.place(x="240", y="415")

        self.YourNameroot.label3 = Label(self.YourNameroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                         bg="white")
        self.YourNameroot.label3.place(x="230", y="435")

        self.YourNameroot.label3 = Label(self.YourNameroot, font=("휴먼편지체", 12), text="러닝타임 : 106분", bg="white")
        self.YourNameroot.label3.place(x="241", y="455")

        self.YourNameroot.label3 = Label(self.YourNameroot, font=("휴먼편지체", 12),
                                         text="추천 좌석 : D~G, 3~6 or 9~12", bg="white")
        self.YourNameroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.YourNameroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.YourNameroot, text="예매하기", font=("휴먼편지체", 11), bg="deepskyblue",
                         command=self.YourNameUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.YourNameroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="deepskyblue",
                         command=self.YourNamereview)
        button1.place(x="310", y="530")

        # 실행
        self.YourNameroot.mainloop()

    def YourNameUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000061933'
        webbrowser.open_new(url)

    def YourNamereview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.YourNameroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.YourNameroot.mainBackL = tkinter.Label(self.YourNameroot,
                                                        image=self.YourNameroot.mainBack)
            self.YourNameroot.mainBackL.place(x=-2, y=-2)

            self.YourNameroot.title('MoCookie')  # 창 제목
            self.YourNameroot.geometry('600x600+340+20')
            self.YourNameroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("../MoCookie/MovieReview/YourNameReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.YourNameroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '너의 이름은':
                    tmp += 20
                    label = Label(self.YourNameroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=505 + tmp)

            # 버튼 출력
            button1 = Button(self.YourNameroot, text="리뷰 작성", bg="deepskyblue", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.YourNameroot.label2 = Label(self.YourNameroot, font=("휴먼편지체", 28), text="YourName",
                                             bg="white", fg="deepskyblue")
            self.YourNameroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.YourNameroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.YourNameroot.mainBackL = tkinter.Label(self.YourNameroot,
                                                        image=self.YourNameroot.mainBack)
            self.YourNameroot.mainBackL.place(x=-2, y=-2)

            self.YourNameroot.title('MoCookie')  # 창 제목
            self.YourNameroot.geometry('600x600+340+20')
            self.YourNameroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("../MoCookie/MovieReview/YourNameSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.YourNameroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '너의 이름은':
                    tmp += 20
                    label = Label(self.YourNameroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=380 + tmp)

            # 버튼 출력
            button1 = Button(self.YourNameroot, text="리뷰 작성", bg="deepskyblue", command=self.writeReview)
            button1.place(x="520", y="25")
            self.YourNameroot.label2 = Label(self.YourNameroot, font=("휴먼편지체", 28), text="YourName",
                                             bg="white", fg="deepskyblue")
            self.YourNameroot.label2.place(x="10", y="10")

        # 실행
        self.YourNameroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Kim_GUI(self):
        self.Kimroot = tkinter.Toplevel()  # 창 생성
        self.Kimroot.title('MoCookie')  # 창 제목
        self.Kimroot.geometry('600x600+340+20')
        self.Kimroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Kimroot.configure(bg="white")

        self.Kimroot.label2 = Label(self.Kimroot, font=("휴먼편지체", 25), text="Kim Jong-boon of Wangshimni", bg="white",
                                    fg="forestgreen")
        self.Kimroot.label2.place(x="10", y="10")

        self.Kimroot.image = tkinter.PhotoImage(file="../MoCookie/Poster/KimPoster.png")
        self.Kimroot.label = tkinter.Label(self.Kimroot, image=self.Kimroot.image,
                                           bg="white")
        self.Kimroot.label.place(x="195", y="55")

        self.Kimroot.label1 = Label(self.Kimroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Kimroot.label1.place(x="233", y="360")

        self.Kimroot.label2 = Label(self.Kimroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.11",
                                    bg="white")
        self.Kimroot.label2.place(x="234", y="395")

        self.Kimroot.label3 = Label(self.Kimroot, font=("휴먼편지체", 12), text="장르 : 다큐멘터리",
                                    bg="white")
        self.Kimroot.label3.place(x="243", y="415")

        self.Kimroot.label3 = Label(self.Kimroot, font=("휴먼편지체", 12), text="등급 : 15세이상 관람가",
                                    bg="white")
        self.Kimroot.label3.place(x="230", y="435")

        self.Kimroot.label3 = Label(self.Kimroot, font=("휴먼편지체", 12), text="러닝타임 : 103분", bg="white")
        self.Kimroot.label3.place(x="241", y="455")

        self.Kimroot.label3 = Label(self.Kimroot, font=("휴먼편지체", 12),
                                    text="추천 좌석 : F~G, 6~9", bg="white")
        self.Kimroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Kimroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Kimroot, text="예매하기", font=("휴먼편지체", 11), bg="forestgreen",
                         command=self.KimUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Kimroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="forestgreen",
                         command=self.Kimreview)
        button1.place(x="310", y="530")

        # 실행
        self.Kimroot.mainloop()

    def KimUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125633'
        webbrowser.open_new(url)

    def Kimreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Kimroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Kimroot.mainBackL = tkinter.Label(self.Kimroot,
                                                   image=self.Kimroot.mainBack)
            self.Kimroot.mainBackL.place(x=-2, y=-2)

            self.Kimroot.title('MoCookie')  # 창 제목
            self.Kimroot.geometry('600x600+340+20')
            self.Kimroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("../MoCookie/MovieReview/KimReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Kimroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '왕십리 김종분':
                    tmp += 20
                    label = Label(self.Kimroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=330 + tmp)

            # 버튼 출력
            button1 = Button(self.Kimroot, text="리뷰 작성", bg="forestgreen", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Kimroot.label2 = Label(self.Kimroot, font=("휴먼편지체", 25), text="Kim Jong-boon of Wangshimni",
                                        bg="white", fg="forestgreen")
            self.Kimroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Kimroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Kimroot.mainBackL = tkinter.Label(self.Kimroot,
                                                   image=self.Kimroot.mainBack)
            self.Kimroot.mainBackL.place(x=-2, y=-2)

            self.Kimroot.title('MoCookie')  # 창 제목
            self.Kimroot.geometry('600x600+340+20')
            self.Kimroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("../MoCookie/MovieReview/KimSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Kimroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '왕십리 김종분':
                    tmp += 20
                    label = Label(self.Kimroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=330 + tmp)

            # 버튼 출력
            button1 = Button(self.Kimroot, text="리뷰 작성", bg="forestgreen", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Kimroot.label2 = Label(self.Kimroot, font=("휴먼편지체", 25), text="Kim Jong-boon of Wangshimni",
                                        bg="white", fg="forestgreen")
            self.Kimroot.label2.place(x="10", y="10")

        # 실행
        self.Kimroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Natagumo_GUI(self):
        self.Natagumoroot = tkinter.Toplevel()  # 창 생성
        self.Natagumoroot.title('MoCookie')  # 창 제목
        self.Natagumoroot.geometry('600x600+340+20')
        self.Natagumoroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Natagumoroot.configure(bg="white")

        self.Natagumoroot.label2 = Label(self.Natagumoroot, font=("휴먼편지체", 28), text="Demon Slayer", bg="white",
                                         fg="firebrick")
        self.Natagumoroot.label2.place(x="10", y="10")

        self.Natagumoroot.image = tkinter.PhotoImage(file="../MoCookie/Poster/NatagumoPoster.png")
        self.Natagumoroot.label = tkinter.Label(self.Natagumoroot, image=self.Natagumoroot.image,
                                                bg="white")
        self.Natagumoroot.label.place(x="195", y="55")

        self.Natagumoroot.label1 = Label(self.Natagumoroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Natagumoroot.label1.place(x="233", y="360")

        self.Natagumoroot.label2 = Label(self.Natagumoroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.17",
                                         bg="white")
        self.Natagumoroot.label2.place(x="234", y="395")

        self.Natagumoroot.label3 = Label(self.Natagumoroot, font=("휴먼편지체", 12), text="장르 : 애니메이션",
                                         bg="white")
        self.Natagumoroot.label3.place(x="240", y="415")

        self.Natagumoroot.label3 = Label(self.Natagumoroot, font=("휴먼편지체", 12), text="등급 : 15세이상 관람가",
                                         bg="white")
        self.Natagumoroot.label3.place(x="230", y="435")

        self.Natagumoroot.label3 = Label(self.Natagumoroot, font=("휴먼편지체", 12), text="러닝타임 : 137분", bg="white")
        self.Natagumoroot.label3.place(x="241", y="455")

        self.Natagumoroot.label3 = Label(self.Natagumoroot, font=("휴먼편지체", 12),
                                         text="추천 좌석 : D~G, 3~6 or 9~12", bg="white")
        self.Natagumoroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Natagumoroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Natagumoroot, text="예매하기", font=("휴먼편지체", 11), bg="firebrick",
                         command=self.NatagumoUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Natagumoroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="firebrick",
                         command=self.Natagumoreview)
        button1.place(x="310", y="530")

        # 실행
        self.Natagumoroot.mainloop()

    def NatagumoUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125600'
        webbrowser.open_new(url)

    def Natagumoreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Natagumoroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Natagumoroot.mainBackL = tkinter.Label(self.Natagumoroot,
                                                        image=self.Natagumoroot.mainBack)
            self.Natagumoroot.mainBackL.place(x=-2, y=-2)

            self.Natagumoroot.title('MoCookie')  # 창 제목
            self.Natagumoroot.geometry('600x600+340+20')
            self.Natagumoroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("../MoCookie/MovieReview/NatagumoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Natagumoroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '귀멸의 칼날: 나타구모산 편':
                    tmp += 20
                    label = Label(self.Natagumoroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=480 + tmp)

            # 버튼 출력
            button1 = Button(self.Natagumoroot, text="리뷰 작성", bg="firebrick", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Natagumoroot.label2 = Label(self.Natagumoroot, font=("휴먼편지체", 28), text="Demon Slayer",
                                             bg="white", fg="firebrick")
            self.Natagumoroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Natagumoroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Natagumoroot.mainBackL = tkinter.Label(self.Natagumoroot,
                                                        image=self.Natagumoroot.mainBack)
            self.Natagumoroot.mainBackL.place(x=-2, y=-2)

            self.Natagumoroot.title('MoCookie')  # 창 제목
            self.Natagumoroot.geometry('600x600+340+20')
            self.Natagumoroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("../MoCookie/MovieReview/NatagumoSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Natagumoroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '귀멸의 칼날: 나타구모산 편':
                    tmp += 20
                    label = Label(self.Natagumoroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=350 + tmp)

            # 버튼 출력
            button1 = Button(self.Natagumoroot, text="리뷰 작성", bg="firebrick", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Natagumoroot.label2 = Label(self.Natagumoroot, font=("휴먼편지체", 28), text="Demon Slayer",
                                             bg="white", fg="firebrick")
            self.Natagumoroot.label2.place(x="10", y="10")

        # 실행
        self.Natagumoroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Nammae_GUI(self):
        self.Nammaeroot = tkinter.Toplevel()  # 창 생성
        self.Nammaeroot.title('MoCookie')  # 창 제목
        self.Nammaeroot.geometry('600x600+340+20')
        self.Nammaeroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Nammaeroot.configure(bg="white")

        self.Nammaeroot.label2 = Label(self.Nammaeroot, font=("휴먼편지체", 28), text="Demon Slayer", bg="white",
                                       fg="gainsboro")
        self.Nammaeroot.label2.place(x="10", y="10")

        self.Nammaeroot.image = tkinter.PhotoImage(file="../MoCookie/Poster/NammaePoster.png")
        self.Nammaeroot.label = tkinter.Label(self.Nammaeroot, image=self.Nammaeroot.image,
                                              bg="white")
        self.Nammaeroot.label.place(x="195", y="55")

        self.Nammaeroot.label1 = Label(self.Nammaeroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Nammaeroot.label1.place(x="233", y="360")

        self.Nammaeroot.label2 = Label(self.Nammaeroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.10",
                                       bg="white")
        self.Nammaeroot.label2.place(x="234", y="395")

        self.Nammaeroot.label3 = Label(self.Nammaeroot, font=("휴먼편지체", 12), text="장르 : 애니메이션",
                                       bg="white")
        self.Nammaeroot.label3.place(x="240", y="415")

        self.Nammaeroot.label3 = Label(self.Nammaeroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                       bg="white")
        self.Nammaeroot.label3.place(x="230", y="435")

        self.Nammaeroot.label3 = Label(self.Nammaeroot, font=("휴먼편지체", 12), text="러닝타임 : 105분", bg="white")
        self.Nammaeroot.label3.place(x="241", y="455")

        self.Nammaeroot.label3 = Label(self.Nammaeroot, font=("휴먼편지체", 12),
                                       text="추천 좌석 : D~G, 3~6 or 9~12", bg="white")
        self.Nammaeroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Nammaeroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Nammaeroot, text="예매하기", font=("휴먼편지체", 11), bg="gainsboro",
                         command=self.NammaeUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Nammaeroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="gainsboro",
                         command=self.Nammaereview)
        button1.place(x="310", y="530")

        # 실행
        self.Nammaeroot.mainloop()

    def NammaeUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125196'
        webbrowser.open_new(url)

    def Nammaereview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Nammaeroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Nammaeroot.mainBackL = tkinter.Label(self.Nammaeroot,
                                                      image=self.Nammaeroot.mainBack)
            self.Nammaeroot.mainBackL.place(x=-2, y=-2)

            self.Nammaeroot.title('MoCookie')  # 창 제목
            self.Nammaeroot.geometry('600x600+340+20')
            self.Nammaeroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("../MoCookie/MovieReview/NammaeReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Nammaeroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '귀멸의 칼날-남매의 연':
                    tmp += 20
                    label = Label(self.Nammaeroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=450 + tmp)

            # 버튼 출력
            button1 = Button(self.Nammaeroot, text="리뷰 작성", bg="gainsboro", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Nammaeroot.label2 = Label(self.Nammaeroot, font=("휴먼편지체", 28), text="Demon Slayer",
                                           bg="white", fg="gainsboro")
            self.Nammaeroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Nammaeroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Nammaeroot.mainBackL = tkinter.Label(self.Nammaeroot,
                                                      image=self.Nammaeroot.mainBack)
            self.Nammaeroot.mainBackL.place(x=-2, y=-2)

            self.Nammaeroot.title('MoCookie')  # 창 제목
            self.Nammaeroot.geometry('600x600+340+20')
            self.Nammaeroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("../MoCookie/MovieReview/NammaeSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Nammaeroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '귀멸의 칼날-남매의 연':
                    tmp += 20
                    label = Label(self.Nammaeroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=330 + tmp)

            # 버튼 출력
            button1 = Button(self.Nammaeroot, text="리뷰 작성", bg="gainsboro", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Nammaeroot.label2 = Label(self.Nammaeroot, font=("휴먼편지체", 28), text="Demon Slayer",
                                           bg="white", fg="gainsboro")
            self.Nammaeroot.label2.place(x="10", y="10")

        # 실행
        self.Nammaeroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def FirstCow_GUI(self):
        self.FirstCowroot = tkinter.Toplevel()  # 창 생성
        self.FirstCowroot.title('MoCookie')  # 창 제목
        self.FirstCowroot.geometry('600x600+340+20')
        self.FirstCowroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.FirstCowroot.configure(bg="white")

        self.FirstCowroot.label2 = Label(self.FirstCowroot, font=("휴먼편지체", 28), text="FirstCowCrime", bg="white",
                                         fg="gold")
        self.FirstCowroot.label2.place(x="10", y="10")

        self.FirstCowroot.image = tkinter.PhotoImage(file="Poster/FirstCowPoster.png")
        self.FirstCowroot.label = tkinter.Label(self.FirstCowroot, image=self.FirstCowroot.image,
                                                bg="white")
        self.FirstCowroot.label.place(x="195", y="55")

        self.FirstCowroot.label1 = Label(self.FirstCowroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.FirstCowroot.label1.place(x="233", y="360")

        self.FirstCowroot.label2 = Label(self.FirstCowroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.04",
                                         bg="white")
        self.FirstCowroot.label2.place(x="234", y="395")

        self.FirstCowroot.label3 = Label(self.FirstCowroot, font=("휴먼편지체", 12), text="장르 : 드라마",
                                         bg="white")
        self.FirstCowroot.label3.place(x="253", y="415")

        self.FirstCowroot.label3 = Label(self.FirstCowroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                         bg="white")
        self.FirstCowroot.label3.place(x="230", y="435")

        self.FirstCowroot.label3 = Label(self.FirstCowroot, font=("휴먼편지체", 12), text="러닝타임 : 122분", bg="white")
        self.FirstCowroot.label3.place(x="241", y="455")

        self.FirstCowroot.label3 = Label(self.FirstCowroot, font=("휴먼편지체", 12),
                                         text="추천 좌석 : F~G, 6~9", bg="white")
        self.FirstCowroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.FirstCowroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.FirstCowroot, text="예매하기", font=("휴먼편지체", 11), bg="gold",
                         command=self.FirstCowUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.FirstCowroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="gold",
                         command=self.FirstCowreview)
        button1.place(x="310", y="530")

        # 실행
        self.FirstCowroot.mainloop()

    def FirstCowUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125298'
        webbrowser.open_new(url)

    def FirstCowreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.FirstCowroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.FirstCowroot.mainBackL = tkinter.Label(self.FirstCowroot,
                                                        image=self.FirstCowroot.mainBack)
            self.FirstCowroot.mainBackL.place(x=-2, y=-2)

            self.FirstCowroot.title('MoCookie')  # 창 제목
            self.FirstCowroot.geometry('600x600+340+20')
            self.FirstCowroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/FirstCowReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.FirstCowroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '퍼스트 카우':
                    tmp += 20
                    label = Label(self.FirstCowroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=475 + tmp)

            # 버튼 출력
            button1 = Button(self.FirstCowroot, text="리뷰 작성", bg="gold", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.FirstCowroot.label2 = Label(self.FirstCowroot, font=("휴먼편지체", 28), text="FirstCowCrime",
                                             bg="white", fg="gold")
            self.FirstCowroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.FirstCowroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.FirstCowroot.mainBackL = tkinter.Label(self.FirstCowroot,
                                                        image=self.FirstCowroot.mainBack)
            self.FirstCowroot.mainBackL.place(x=-2, y=-2)

            self.FirstCowroot.title('MoCookie')  # 창 제목
            self.FirstCowroot.geometry('600x600+340+20')
            self.FirstCowroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/FirstCowSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.FirstCowroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '퍼스트 카우':
                    tmp += 20
                    label = Label(self.FirstCowroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=340 + tmp)

            # 버튼 출력
            button1 = Button(self.FirstCowroot, text="리뷰 작성", bg="gold", command=self.writeReview)
            button1.place(x="520", y="25")
            self.FirstCowroot.label2 = Label(self.FirstCowroot, font=("휴먼편지체", 28), text="FirstCowCrime",
                                             bg="white", fg="gold")
            self.FirstCowroot.label2.place(x="10", y="10")

        # 실행
        self.FirstCowroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Italy_GUI(self):
        self.Italyroot = tkinter.Toplevel()  # 창 생성
        self.Italyroot.title('MoCookie')  # 창 제목
        self.Italyroot.geometry('600x600+340+20')
        self.Italyroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Italyroot.configure(bg="white")

        self.Italyroot.label2 = Label(self.Italyroot, font=("휴먼편지체", 25), text="Made In Italy", bg="white",
                                      fg="peachpuff")
        self.Italyroot.label2.place(x="10", y="10")

        self.Italyroot.image = tkinter.PhotoImage(file="Poster/ItalyPoster.png")
        self.Italyroot.label = tkinter.Label(self.Italyroot, image=self.Italyroot.image,
                                             bg="white")
        self.Italyroot.label.place(x="195", y="55")

        self.Italyroot.label1 = Label(self.Italyroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Italyroot.label1.place(x="233", y="360")

        self.Italyroot.label2 = Label(self.Italyroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.24",
                                      bg="white")
        self.Italyroot.label2.place(x="234", y="395")

        self.Italyroot.label3 = Label(self.Italyroot, font=("휴먼편지체", 12), text="장르 : 코미디, 드라마, 멜로/로맨스",
                                      bg="white")
        self.Italyroot.label3.place(x="200", y="415")

        self.Italyroot.label3 = Label(self.Italyroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                      bg="white")
        self.Italyroot.label3.place(x="230", y="435")

        self.Italyroot.label3 = Label(self.Italyroot, font=("휴먼편지체", 12), text=" 러닝타임 : 94분", bg="white")
        self.Italyroot.label3.place(x="241", y="455")

        self.Italyroot.label3 = Label(self.Italyroot, font=("휴먼편지체", 12),
                                      text="추천 좌석 : G~H, 1~4 or 11~14", bg="white")
        self.Italyroot.label3.place(x="203", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Italyroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Italyroot, text="예매하기", font=("휴먼편지체", 11), bg="peachpuff",
                         command=self.ItalyUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Italyroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="peachpuff",
                         command=self.Italyreview)
        button1.place(x="310", y="530")

        # 실행
        self.Italyroot.mainloop()

    def ItalyUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125551'
        webbrowser.open_new(url)

    def Italyreview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Italyroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Italyroot.mainBackL = tkinter.Label(self.Italyroot,
                                                     image=self.Italyroot.mainBack)
            self.Italyroot.mainBackL.place(x=-2, y=-2)

            self.Italyroot.title('MoCookie')  # 창 제목
            self.Italyroot.geometry('600x600+340+20')
            self.Italyroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/ItalyReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Italyroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '메이드 인 이태리':
                    tmp += 20
                    label = Label(self.Italyroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=480 + tmp)

            # 버튼 출력
            button1 = Button(self.Italyroot, text="리뷰 작성", bg="peachpuff", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Italyroot.label2 = Label(self.Italyroot, font=("휴먼편지체", 25), text="Made In Italy",
                                          bg="white", fg="peachpuff")
            self.Italyroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Italyroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Italyroot.mainBackL = tkinter.Label(self.Italyroot,
                                                     image=self.Italyroot.mainBack)
            self.Italyroot.mainBackL.place(x=-2, y=-2)

            self.Italyroot.title('MoCookie')  # 창 제목
            self.Italyroot.geometry('600x600+340+20')
            self.Italyroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/ItalySpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Italyroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '메이드 인 이태리':
                    tmp += 20
                    label = Label(self.Italyroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=330 + tmp)

            # 버튼 출력
            button1 = Button(self.Italyroot, text="리뷰 작성", bg="peachpuff", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Italyroot.label2 = Label(self.Italyroot, font=("휴먼편지체", 25), text="Made In Italy",
                                          bg="white", fg="peachpuff")
            self.Italyroot.label2.place(x="10", y="10")

        # 실행
        self.Italyroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Choi_GUI(self):
        self.Choiroot = tkinter.Toplevel()  # 창 생성
        self.Choiroot.title('MoCookie')  # 창 제목
        self.Choiroot.geometry('600x600+340+20')
        self.Choiroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Choiroot.configure(bg="white")

        self.Choiroot.label2 = Label(self.Choiroot, font=("휴먼편지체", 25), text="1984 CHOI Dong-won", bg="white",
                                     fg="darkslategrey")
        self.Choiroot.label2.place(x="10", y="10")

        self.Choiroot.image = tkinter.PhotoImage(file="../MoCookie/Poster/ChoiPoster.png")
        self.Choiroot.label = tkinter.Label(self.Choiroot, image=self.Choiroot.image,
                                            bg="white")
        self.Choiroot.label.place(x="195", y="55")

        self.Choiroot.label1 = Label(self.Choiroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Choiroot.label1.place(x="233", y="360")

        self.Choiroot.label2 = Label(self.Choiroot, font=("휴먼편지체", 12), text="개봉일 : 2021.11.11",
                                     bg="white")
        self.Choiroot.label2.place(x="234", y="395")

        self.Choiroot.label3 = Label(self.Choiroot, font=("휴먼편지체", 12), text="장르 : 다큐멘터리",
                                     bg="white")
        self.Choiroot.label3.place(x="243", y="415")

        self.Choiroot.label3 = Label(self.Choiroot, font=("휴먼편지체", 12), text="등급 : 전체 관람가",
                                     bg="white")
        self.Choiroot.label3.place(x="240", y="435")

        self.Choiroot.label3 = Label(self.Choiroot, font=("휴먼편지체", 12), text=" 러닝타임 : 99분", bg="white")
        self.Choiroot.label3.place(x="241", y="455")

        self.Choiroot.label3 = Label(self.Choiroot, font=("휴먼편지체", 12),
                                     text="추천 좌석 : F~G, 6~9", bg="white")
        self.Choiroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Choiroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Choiroot, text="예매하기", font=("휴먼편지체", 11), bg="darkslategrey",
                         command=self.ChoiUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Choiroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="darkslategrey",
                         command=self.Choireview)
        button1.place(x="310", y="530")

        # 실행
        self.Choiroot.mainloop()

    def ChoiUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125470'
        webbrowser.open_new(url)

    def Choireview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Choiroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Choiroot.mainBackL = tkinter.Label(self.Choiroot,
                                                    image=self.Choiroot.mainBack)
            self.Choiroot.mainBackL.place(x=-2, y=-2)

            self.Choiroot.title('MoCookie')  # 창 제목
            self.Choiroot.geometry('600x600+340+20')
            self.Choiroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("../MoCookie/MovieReview/ChoiReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Choiroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '1984 최동원':
                    tmp += 20
                    label = Label(self.Choiroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=470 + tmp)

            # 버튼 출력
            button1 = Button(self.Choiroot, text="리뷰 작성", bg="darkslategrey", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Choiroot.label2 = Label(self.Choiroot, font=("휴먼편지체", 25), text="1984 CHOI Dong-won",
                                         bg="white", fg="darkslategrey")
            self.Choiroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Choiroot.mainBack = tkinter.PhotoImage(file="../MoCookie/Img/img_7.png")
            self.Choiroot.mainBackL = tkinter.Label(self.Choiroot,
                                                    image=self.Choiroot.mainBack)
            self.Choiroot.mainBackL.place(x=-2, y=-2)

            self.Choiroot.title('MoCookie')  # 창 제목
            self.Choiroot.geometry('600x600+340+20')
            self.Choiroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("../MoCookie/MovieReview/ChoiSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Choiroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('../MoCookie/MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '1984 최동원':
                    tmp += 20
                    label = Label(self.Choiroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=340 + tmp)

            # 버튼 출력
            button1 = Button(self.Choiroot, text="리뷰 작성", bg="darkslategrey", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Choiroot.label2 = Label(self.Choiroot, font=("휴먼편지체", 25), text="1984 CHOI Dong-won",
                                         bg="white", fg="forestgreen")
            self.Choiroot.label2.place(x="10", y="10")

        # 실행
        self.Choiroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    def Leave_GUI(self):
        self.Leaveroot = tkinter.Toplevel()  # 창 생성
        self.Leaveroot.title('MoCookie')  # 창 제목
        self.Leaveroot.geometry('600x600+340+20')
        self.Leaveroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.Leaveroot.configure(bg="white")

        self.Leaveroot.label2 = Label(self.Leaveroot, font=("휴먼편지체", 28), text="A Leave", bg="white",
                                      fg="lightblue")
        self.Leaveroot.label2.place(x="10", y="10")

        self.Leaveroot.image = tkinter.PhotoImage(file="Poster/LeavePoster.png")
        self.Leaveroot.label = tkinter.Label(self.Leaveroot, image=self.Leaveroot.image,
                                             bg="white")
        self.Leaveroot.label.place(x="195", y="55")

        self.Leaveroot.label1 = Label(self.Leaveroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
        self.Leaveroot.label1.place(x="233", y="360")

        self.Leaveroot.label2 = Label(self.Leaveroot, font=("휴먼편지체", 12), text="개봉일 : 2021.10.21",
                                      bg="white")
        self.Leaveroot.label2.place(x="234", y="395")

        self.Leaveroot.label3 = Label(self.Leaveroot, font=("휴먼편지체", 12), text="장르 : 드라마",
                                      bg="white")
        self.Leaveroot.label3.place(x="253", y="415")

        self.Leaveroot.label3 = Label(self.Leaveroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                      bg="white")
        self.Leaveroot.label3.place(x="230", y="435")

        self.Leaveroot.label3 = Label(self.Leaveroot, font=("휴먼편지체", 12), text=" 러닝타임 : 18분", bg="white")
        self.Leaveroot.label3.place(x="241", y="455")

        self.Leaveroot.label3 = Label(self.Leaveroot, font=("휴먼편지체", 12),
                                      text="추천 좌석 : F~G, 6~9", bg="white")
        self.Leaveroot.label3.place(x="233", y="475")

        # 체크 박스
        self.CheckVar = IntVar()

        c1 = Checkbutton(self.Leaveroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
        c1.place(x="270", y="500")

        button1 = Button(self.Leaveroot, text="예매하기", font=("휴먼편지체", 11), bg="lightblue",
                         command=self.LeaveUrl)
        button1.place(x="230", y="530")

        button1 = Button(self.Leaveroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="lightblue",
                         command=self.Leavereview)
        button1.place(x="310", y="530")

        # 실행
        self.Leaveroot.mainloop()

    def LeaveUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
        url = 'https://movie.yes24.com/Movie/Ticket?gId=M000125312'
        webbrowser.open_new(url)

    def Leavereview(self):
        # 체크 안했을 때 -> 스포 없는 리뷰 보여주기
        if self.CheckVar.get() == 0:

            # main 화면 이미지 이미지를 덮는거임
            self.Leaveroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Leaveroot.mainBackL = tkinter.Label(self.Leaveroot,
                                                     image=self.Leaveroot.mainBack)
            self.Leaveroot.mainBackL.place(x=-2, y=-2)

            self.Leaveroot.title('MoCookie')  # 창 제목
            self.Leaveroot.geometry('600x600+340+20')
            self.Leaveroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            f = open("MovieReview/LeaveReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Leaveroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '휴가':
                    tmp += 20
                    label = Label(self.Leaveroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=355 + tmp)

            # 버튼 출력
            button1 = Button(self.Leaveroot, text="리뷰 작성", bg="lightblue", command=self.writeReview)
            button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

            self.Leaveroot.label2 = Label(self.Leaveroot, font=("휴먼편지체", 28), text="A Leave",
                                          bg="white", fg="lightblue")
            self.Leaveroot.label2.place(x="10", y="10")

        # 체크박스 체크 했을 떄 -> 스포 있는 리뷰
        else:
            # main 화면 이미지 이미지를 덮는거임
            self.Leaveroot.mainBack = tkinter.PhotoImage(file="Img/img_7.png")
            self.Leaveroot.mainBackL = tkinter.Label(self.Leaveroot,
                                                     image=self.Leaveroot.mainBack)
            self.Leaveroot.mainBackL.place(x=-2, y=-2)

            self.Leaveroot.title('MoCookie')  # 창 제목
            self.Leaveroot.geometry('600x600+340+20')
            self.Leaveroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부

            # frame = Frame(self.duneroot)
            # frame.pack()

            f = open("MovieReview/LeaveSpoReview.txt", 'r', encoding="UTF-8")
            text = f.read()
            label = tkinter.Label(self.Leaveroot, width=600, height=600, bg="white", font=("휴먼편지체", 10), text=text)
            label.pack()
            fr = open('MyReview.txt', 'r', encoding='utf-8')
            arr = []
            arr1 = []
            tmp = 0
            while True:
                review_loaded = fr.readline()
                if not review_loaded: break
                arr = review_loaded.split('\t')
                arr1.append(arr)
            for a in arr1:
                if a[1] == '휴가':
                    tmp += 20
                    label = Label(self.Leaveroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                    label.place(x=180, y=365 + tmp)

            # 버튼 출력
            button1 = Button(self.Leaveroot, text="리뷰 작성", bg="lightblue", command=self.writeReview)
            button1.place(x="520", y="25")
            self.Leaveroot.label2 = Label(self.Leaveroot, font=("휴먼편지체", 28), text="A Leave",
                                          bg="white", fg="lightblue")
            self.Leaveroot.label2.place(x="10", y="10")

        # 실행
        self.Leaveroot.mainloop()
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------

    def writeReview(self):
        self.writereview = tkinter.Toplevel()  # 창 생성
        self.writereview.title('MoCookie')  # 창 제목
        self.writereview.geometry('500x300+390+180')
        self.writereview.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.writereview.configure(bg="white")

        label1 = Label(self.writereview, text="한줄 리뷰 작성", bg="white",font=("휴먼편지체", 23))
        label1.place(x=155, y=20)
        str = StringVar()
        self.writereview.label3 = Label(self.writereview, font=("휴먼편지체", 12), text="이름", bg="white")
        self.writereview.label3.place(x=165, y=80)
        self.entry1 = Entry(self.writereview, width=20, font=("휴먼편지체", 10), textvariable=str)  # 이름 입력
        self.entry1.place(x=205, y=80)
        a = ["듄", "유체이탈자", "연애 빠진 로맨스", "엔칸토-마법의 세계", "이터널스", "장르만 로맨스", "프렌치 디스패치", "너에게 가는 길", "라임 크라임", "호빗: 스마우그의 폐허", "로그북",
             "디어 에반 핸슨", "꽃다발 같은 사랑을 했다", "너의 이름은", "왕십리 김종분", "귀멸의 칼날: 나타구모산 편", "귀멸의 칼날-남매의 연", "퍼스트 카우", "메이드 인 이태리", "1984 최동원", "휴가"]  # 콤보 박스
        self.combo1 = ttk.Combobox(self.writereview)
        self.combo1.config(height=5, width=30)  # 높이 설정
        self.combo1.config(values=a, font=("휴먼편지체", 10))  # 나타낼 항목 리스트(a) 설정
        self.combo1.config(state="readonly", font=("휴먼편지체", 10))  # 콤보 박스에 사용자가 직접 입력 불가
        self.combo1.set("※리뷰를 남길 영화를 선택해주세요※")  # 맨 처음 나타낼 값 설정
        self.combo1.place(x=150, y=120)
        self.entry2 = Entry(self.writereview, width=65, font=("휴먼편지체", 10))  # 리뷰 작성
        self.entry2.place(x=60, y=160)
        # 체크 박스
        self.CheckVar2 = IntVar()
        self.c2 = Checkbutton(self.writereview, text="스포 포함", variable=self.CheckVar2, font=("휴먼편지체", 13), bg="white")
        self.c2.place(x=210, y=200)
        button_sa = tkinter.Button(self.writereview, height=1, width=8, text="리뷰 저장", font=("휴먼편지체", 10), command=self.CheckEntry)
        button_sa.place(x=220, y=240)

    def CheckEntry(self):
        if self.entry1.get() == '':
            messagebox.showwarning('다시시도', '작성자 명을 입력해 주세요.')  # 메세지 박스 출력
            self.writereview.destroy()  # 화면 창 끄기
            self.writeReview()
        elif self.combo1.get() == "※리뷰를 남길 영화를 선택해주세요※":
            messagebox.showwarning('다시시도', '영화를 선택해주세요.')  # 메세지 박스 출력
            self.writereview.destroy()  # 화면 창 끄기
            self.writeReview()
        elif self.entry2.get() == '':
            messagebox.showwarning('다시시도', '리뷰를 입력해주세요.')  # 메세지 박스 출력
            self.writereview.destroy()  # 화면 창 끄기
            self.writeReview()
        else:
            self.add_review()
            messagebox.showwarning('저장완료', '저장되었습니다.')  # 메세지 박스 출력
            self.writereview.destroy()  # 화면 창 끄기

    def add_review(self):
        # 리뷰 딕셔너리로 MyReview.txt에 저장
        self.reviews = list()
        print(self.CheckVar.get())
        self.new_review = f'{self.entry1.get()}\t{self.combo1.get()}\t{self.CheckVar2.get()}\t{self.entry2.get()}\n'

        self.reviews.append(self.new_review)

        with open('MyReview.txt', 'a', encoding='utf-8') as fw:
            fw.write(self.new_review)

    def myReview(self):
        self.myreview = tkinter.Toplevel()  # 창 생성
        self.myreview.title('MoCookie')  # 창 제목
        self.myreview.geometry('600x600+340+20')
        self.myreview.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
        self.myreview.configure(bg="white")

        label1 = Label(self.myreview, text="나의 리뷰", bg="white", font=("휴먼편지체", 23))
        label1.place(x=240, y=15)

        label2 = Label(self.myreview, text=" 사용자명      영화         스포여부   리뷰", bg="white", font=("휴먼편지체", 12))
        label2.place(x=20, y=65)
        label2 = Label(self.myreview, text="(0 = 스포X, 1 = 스포O)", bg="white", font=("휴먼편지체", 8))
        label2.place(x=165, y=88)

        fr = open('MyReview.txt', 'r', encoding='utf-8')
        tmp = 0
        while True:
            review_loaded = fr.readline()
            if not review_loaded: break
            tmp += 20
            label = Label(self.myreview, text=review_loaded, bg='white')
            label.place(x=40, y=100+tmp)

if __name__ == '__main__':
    MovieGUI = MovieGUI()