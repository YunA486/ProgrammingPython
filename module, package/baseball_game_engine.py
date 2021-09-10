# 숫자야구게임
import random

# 퀴즈내기(숫자 중복 없이)
def make_quize():
    list_r = random.sample(range(1, 9 + 1), 3)
    string_number = "".join(map(str, list_r))

    # 숫자 3자리 중복없이 묻기
    return string_number

def check(answer, player):
    strike = 0
    ball = 0

    for i, p in enumerate(player):
        for j, a in enumerate(answer):
            if p == a:  # 번호가 있고, 자리가 같으면 strike += 1
                if i == j:
                    strike += 1
                else:    # 번호가 있고, 자리가 다르면 ball += 1
                    ball += 1

    return strike, ball

if __name__ == '__main__':
    answer = make_quize()
    print(answer)
    strike, ball = check("238", "241")
    print(strike, ball)     # 1 0
    strike, ball = check("381", "182")
    print(strike, ball)     # 1 1



