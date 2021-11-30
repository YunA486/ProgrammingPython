import tkinter
from tkinter import *
# tkinter 임포트
from tkinter import messagebox
import pygame


# print(pygame.font.get_fonts())  # 글꼴 종류 출력
# 휴먼모음t 휴먼편지체 휴먼둥근헤드라인 펜흘림 중간안상수체

class MovieGUI:
    def __init__(self):
        self.init_GUI()

    def init_GUI(self):
        self.root = tkinter.Tk()    # 창 생성
        self.root.title('MoCookie') # 창 제목
        self.root.geometry('1200x600+35+20')
        self.root.configure(bg="white")

        # wall = PhotoImage(file="Background_Movie.png")
        # wall_label = Label(image=wall)
        # wall_label.place(x=-2, y=-2)

        # 제목 왼쪽 사진
        # image = tkinter.PhotoImage(file="img_4.png")
        # label = tkinter.Label(self.root, image=image, bg="black")
        # label.place(x="440", y="10")

        # 타이틀
        label1 = Label(self.root, font=("휴먼편지체", 40), text="MoCookie", bg="grey", fg="black")
        label1.place(x="500", y="5")

        # 그냥 버튼
        button = Button(self.root, text="Start", font=("휴먼편지체", 25), bg="white", fg="black")
        button.place(x=420, y=400)

        button = Button(self.root, text="Sign Up", font=("휴먼편지체", 25), bg="white", fg="black")
        button.place(x=550, y=400)

        button = Button(self.root, text="Login", font=("휴먼편지체", 25), bg="white", fg="black")
        button.place(x=710, y=400)

        # 짧은 입력
        # ent = Entry(self.root)  # root라는 창에 입력창 생성
        # ent.pack()  # 입력창 배치
        # 긴 입력
        # ent1 = Text(self.root)  # root라는 창에 입력창 생성
        # ent1.pack()  # 입력창 배치

        # 실행
        self.root.mainloop()

if __name__ == '__main__':
    MovieGUI = MovieGUI()

