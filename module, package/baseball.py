from  baseball_game_engine import make_quize, check

answer = make_quize()
print(answer)

# 무한 반복
while True:
    # 숫자 3자리 중복없이 묻기
    player = input("숫자 세자리는?")
    # strike, ball 확인하기
    strike, ball = check(answer, player)
    # 출력하기
    print(f'{player}\tstrike: {strike}\t ball: {ball}')
    # strike가 3일 때, 나가기
    if strike == 3:
        break

# 축하해주기
print("축하합니다! 정답입니다!")