from baseball_game_engine import make_quize, check
from custom_error import InvalidCountError

answer = make_quize()
# print(answer)

# 무한 반복
while True:
    # 숫자 3자리 중복없이 묻기
    player = input("숫자 세자리는?")  # player : "123" "fun"
    try:        # 숫자가 아닐 때 에러 처리
        player_int = int(player)    # valueError
    except ValueError:
        continue                    # 밑에 실행 X, 반복문 다시

    # 길이가 3이 아닐 때 에러 처리
    if len(player) != len(answer):
        # raise InvalidCountError("3자리가 아닙니다.")
        print(f'입력한 숫자의 개수가 정답과 다릅니다. 정답 : {len(answer)}글자')
        continue

    # strike, ball 확인하기
    strike, ball = check(answer, player)
    # 출력하기
    print(f'{player}\tstrike: {strike}\t ball: {ball}')
    # strike가 3일 때, 나가기
    if strike == 3:
        break

# 축하해주기
print("축하합니다! 정답입니다!")