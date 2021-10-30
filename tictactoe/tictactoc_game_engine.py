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
        pass

    # tictactoe game set Winner

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