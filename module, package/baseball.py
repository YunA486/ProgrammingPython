from baseball_game_engine import make_quize, check
from custom_error import InvalidCountError

answer = make_quize()
# print(answer)

count = 0

# 무한 반복
def save_history(player, count):
    with open('baseball_history.txt', 'a') as f:
        f.write(f'{player}\t{count}\n')

def load_history():
    count_list = []
    with open('baseball_history.txt', 'r') as f:
        while True:
            line = f.readline()
            if line == '' or not line:
                break
            # print(line.rstrip())
            line_data = line.rstrip().split('\t')
            count_list.append(line_data[1])
    # 중복제거 (commit - top3 중복 제거)
    count_list = set(count_list)
    count_list = list(count_list)
    count_list.sort()
    return count_list[:3]

while True:
    # 숫자 3자리 중복없이 묻기
    player = input("숫자 세자리는?(t : top3)")  # player : "123" "fun"
    if player == 't':
        # 에러처리 반드시
        try:    #(commit - FileNotFoundError 처리)
            history = load_history()
        except FileNotFoundError:
            print('history 파일이 존재하지 않습니다.')
            continue
        print(history)
        continue
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
    count += 1
    strike, ball = check(answer, player)
    # 출력하기
    print(f'{player}\tstrike: {strike}\t ball: {ball}\tball: {ball}\t{count}t')
    # strike가 3일 때, 나가기
    if strike == 3:
        save_history(player, count)
        break

# 축하해주기
print("축하합니다! 정답입니다!")