def Bouquet_GUI(self):
    self.Bouquetroot = tkinter.Toplevel()  # 창 생성
    self.Bouquetroot.title('MoCookie')  # 창 제목
    self.Bouquetroot.geometry('600x600+340+20')
    self.Bouquetroot.resizable(width=False, height=False)  # 리사이즈 가로 세로 여부
    self.Bouquetroot.configure(bg="white")

    self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 28), text="We Made a Beautiful Bouquet", bg="white",
                                    fg="peru")
    self.Bouquetroot.label2.place(x="10", y="10")

    self.Bouquetroot.image = tkinter.PhotoImage(file="../MoCookie/Poster/BouquetPoster.png")
    self.Bouquetroot.label = tkinter.Label(self.Bouquetroot, image=self.Bouquetroot.image,
                                           bg="white")
    self.Bouquetroot.label.place(x="195", y="55")

    self.Bouquetroot.label1 = Label(self.Bouquetroot, font=("휴먼편지체", 17), text="쿠키 영상 없음", bg="white")
    self.Bouquetroot.label1.place(x="233", y="360")

    self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="개봉일 : 2013.12.12",
                                    bg="white")
    self.Bouquetroot.label2.place(x="234", y="395")

    self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="장르 : 판타지, 모험, 드라마",
                                    bg="white")
    self.Bouquetroot.label3.place(x="223", y="415")

    self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="등급 : 12세이상 관람가",
                                    bg="white")
    self.Bouquetroot.label3.place(x="230", y="435")

    self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12), text="러닝타임 : 161분", bg="white")
    self.Bouquetroot.label3.place(x="241", y="455")

    self.Bouquetroot.label3 = Label(self.Bouquetroot, font=("휴먼편지체", 12),
                                    text="추천 좌석 : D~G, 3~6 or 9~12", bg="white")
    self.Bouquetroot.label3.place(x="203", y="475")

    # 체크 박스
    self.CheckVar = IntVar()

    c1 = Checkbutton(self.Bouquetroot, text="스포리뷰", variable=self.CheckVar, font=("휴먼편지체", 10), bg="white")
    c1.place(x="270", y="500")

    button1 = Button(self.Bouquetroot, text="예매하기", font=("휴먼편지체", 11), bg="peru",
                     command=self.BouquetUrl)
    button1.place(x="230", y="530")

    button1 = Button(self.Bouquetroot, text="리뷰 보기", font=("휴먼편지체", 11), bg="peru",
                     command=self.Bouquetreview)
    button1.place(x="310", y="530")

    # 실행
    self.Bouquetroot.mainloop()


def BouquetUrl(self):  # 영화 티켓 구매 웹사이트로 이동하는 함수
    url = 'https://movie.yes24.com/Movie/Ticket?gId=M000043214'
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
            if a[1] == '꽃다발같은 사랑을 했다':
                tmp += 20
                label = Label(self.Bouquetroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                label.place(x=180, y=470 + tmp)

        # 버튼 출력
        button1 = Button(self.Bouquetroot, text="리뷰 작성", bg="peru", command=self.writeReview)
        button1.place(x="520", y="25")  # button1.채워넣기(확장두께=1)

        self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 28), text="We Made a Beautiful Bouquet",
                                        bg="white", fg="peru")
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
            if a[1] == '꽃다발같은 사랑을 했다':
                tmp += 20
                label = Label(self.Bouquetroot, text=f'- {a[3]}', bg='white', font=("휴먼편지체", 10))
                label.place(x=180, y=480 + tmp)

        # 버튼 출력
        button1 = Button(self.Bouquetroot, text="리뷰 작성", bg="peru", command=self.writeReview)
        button1.place(x="520", y="25")
        self.Bouquetroot.label2 = Label(self.Bouquetroot, font=("휴먼편지체", 28), text="We Made a Beautiful Bouquet",
                                        bg="white", fg="peru")
        self.Bouquetroot.label2.place(x="10", y="10")

    # 실행
    self.Bouquetroot.mainloop()