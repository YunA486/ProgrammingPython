from tkinter import *
from tkinter import messagebox
import os


class FindDict:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("단어장")
        self.__window.geometry("300x100")

        self.buildGUI()

        self.lines = []
        self.word = {}

        # 파일처리 시작
        pathname = "word.txt"

        if os.path.exists(pathname):
            self.WordFile()
        else:  # 파일없으면 에러 메세지
            messagebox.showinfo('ERROR', 'File road Failed')

    # 파일 읽어오기
    def WordFile(self):
        with open('word.txt', 'r', encoding='cp949') as file:
            for line in file:
                self.lines.append(line.strip())
        for i in range(len(self.lines)):
            key, value = self.lines[i].split(':')
            self.word[key] = value

    # enter 함수
    def confirm(self, event):
        self.searchDict()

    # GUI 환경 꾸미기
    def buildGUI(self):
        # 프레임 생성
        f1 = Frame(self.__window)
        f2 = Frame(self.__window)

        # 라벨 생성
        x_label = Label(self.__window, text="단어: ")
        y_label = Label(self.__window, text="뜻: ")

        # 입력칸 생성
        global x_entry, y_entry
        self.x_entry = Entry(f1, width=10, bg="light blue")
        self.y_entry = Entry(f2, width=29, bg="light green")

        # 버튼 생성
        search_b = Button(f1, text="검색", command=self.searchDict)
        add_b = Button(f1, text="추가", command=self.addDict)
        reset_b = Button(self.__window, text="초기화", command=self.reset)
        exit_b = Button(self.__window, text="종료", command=self.exit)

        # 배치
        x_label.grid(row=0, column=0, sticky=E)
        y_label.grid(row=1, column=0, sticky=E)
        self.x_entry.pack(side=LEFT)
        self.y_entry.pack(side=LEFT)
        f2.grid(row=1, column=1, sticky=W)
        search_b.pack(side=LEFT, ipadx=10, ipady=5, padx=5)
        add_b.pack(side=LEFT, ipadx=10, ipady=5, padx=5)
        f1.grid(row=0, column=1, sticky=S)
        reset_b.grid(row=2, column=0, sticky=W, ipadx=10, ipady=5, padx=5)
        exit_b.grid(row=2, column=1, sticky=W, ipadx=10, ipady=5, padx=5)

        # enter
        self.x_entry.bind("<Return>", self.confirm)

    def searchDict(self):
        eng = self.x_entry.get()
        if (eng in self.word) == False:
            messagebox.showinfo('검색 오류', "%s란 단어는 없습니다!" % eng)

        else:
            kor = self.word.get(eng)
            self.y_entry.delete(0, END)
            self.y_entry.insert(0, kor)

    def addDict(self):
        eng = self.x_entry.get()
        kor = self.y_entry.get()
        if (eng in self.word) == True:
            messagebox.showinfo('검색 오류', "이미 등록된 단어입니다.")
        else:
            self.word[eng] = kor
            messagebox.showinfo("추가 확인", "단어 %s를 추가했습니다." % eng)

    def exit(self):
        self.addTXT()
        quit()

    def addTXT(self):  # 단어 추가 txt파일 처리
        with open('word.txt', 'w') as file:
            for k in self.word.keys():
                file.write(k + ':' + self.word[k] + '\n')
        file.close()

    def reset(self):
        self.x_entry.delete(0, END)
        self.y_entry.delete(0, END)

    def start(self):
        self.__window.mainloop()


# main
dictionary = FindDict()
dictionary.start()