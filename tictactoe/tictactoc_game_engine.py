class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE)  #['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn = 'X'

    def show_board(self):
        for a in range(len(self.board)):
            print(self.board[a], end=' ')
            if a % self.SIZE == self.SIZE -1:       # 중요중요중요중요중요중요기말기말기말기말
                print()

    def set(self, row, col):
        self.board[self.SIZE*(row-1) + (col-1)] = self.turn

    def position_to_index(self, row, col):
        return self.SIZE * (row - 1) + (col - 1)

    def set_winner(self):
        # - 3줄
        for row in range(1, 3+1):   # row : 1~3 반복
            if self.board[self.position_to_index(row,1)] == self.board[self.position_to_index(row,2)] == self.board[self.position_to_index(row,3)] == self.turn:    # '.'일 때, 끝 안나게 하기
                return self.turn
        # | 3줄
        for col in range(1, 3+1):   # col : 1~3 반복
            if self.board[self.position_to_index(1,col)] == self.board[self.position_to_index(2,col)] == self.board[self.position_to_index(3,col)] == self.turn:    # '.'일 때, 끝 안나게 하기
                return self.turn
        # / 3줄
        if self.board[self.position_to_index(1,1)] == self.board[self.position_to_index(2,2)] == self.board[self.position_to_index(3,3)] == self.turn:    # '.'일 때, 끝 안나게 하기
            return self.turn
        # \ 3줄
        if self.board[self.position_to_index(1,3)] == self.board[self.position_to_index(2,2)] == self.board[self.position_to_index(3,1)] == self.turn:    # '.'일 때, 끝 안나게 하기
            return self.turn
        # 비기는 조건 : 다 채워졌을 때 위의 것에 해당 안됐을 때
        if not '.' in self.board:   # self.board 안에 '.'이 없다면
            return 'd'  # draw

    def change_turn(self):
        # self.turn 'X'면  'O', 'O'면 'X'로 바꾸기
        # if self.turn == 'X':
        #     self.turn = '0'
        # else:
        #     self.turn = 'X'

        self.turn = '0' if self.turn == 'X' else 'X'  # 한줄로 바꿈

if __name__ == '__main__':
    game_engine = TictactoeGameEngine()
    game_engine.show_board()    # ...\n...\n...
    game_engine.set(3, 2)
    game_engine.show_board()
    game_engine.set(3, 2)
    game_engine.set(3, 3)
    print(game_engine.set_winner()) # 'X'
    game_engine.change_turn()
    print(game_engine.turn)     # 'O'
    # 무승부 만들기, 확인하기
    # game_engine.board('X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O')
    # print(game_engine.set_winner()) # d
    game_engine.set(1, 3)
    game_engine.set(2, 2)
    game_engine.set(3, 1)
    print(game_engine.set_winner())     # '/'