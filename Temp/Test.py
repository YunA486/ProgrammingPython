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
                label.place(x=180, y=475 + tmp)

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
                label.place(x=180, y=340 + tmp)

        # 버튼 출력
        button1 = Button(self.Leaveroot, text="리뷰 작성", bg="lightblue", command=self.writeReview)
        button1.place(x="520", y="25")
        self.Leaveroot.label2 = Label(self.Leaveroot, font=("휴먼편지체", 28), text="A Leave",
                                         bg="white", fg="lightblue")
        self.Leaveroot.label2.place(x="10", y="10")

    # 실행
    self.Leaveroot.mainloop()