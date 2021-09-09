# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
import math

bill = 59827
# value = round(bill, -2)
temp = int(bill/100)
value = temp*100
print(value)

print(bill//100*100)    # 624 * 100
print(bill-bill%100)    # 62421 - 21
print(math.floor(bill/100)*100) # 524.21 내림 624.00 -> 62400

# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?

print('-'*20)

score = 56
print(round(score, -1))

print(round(score / 10) * 10)

# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)

print('-'*20)

import random

lotto = random.sample(range(1,46),6)
print(lotto)

# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)

print('-'*20)

import random

number = set()
while len(number)<3:
    number.add(random.randint(1,9))

print(number)

list_r = random.sample(range(1, 9 + 1), 3)
print(", ".join(str(n) for n in list_r))
print("".join(map(str, list_r)))

string = ''
for n in list_r:
    string += str(n)
print(string)


# 5. 내가 태어난 날로부터 며칠이 지났는지?

print('-'*20)

import datetime

now = datetime.datetime.now()
birthday = datetime.datetime(2004, 4, 2, 6, 30)
print(now - birthday)

# 6. 올해 크리스마스까지 며칠이 남았는지?

print('-'*20)

import datetime

now = datetime.datetime.now()
christmas = datetime.datetime(2021, 12, 25)
print(christmas - now)

# 7. 내 생일이 며칠 남았는지?

print('-'*20)

import datetime

now = datetime.datetime.now()
ya_birthday = datetime.datetime(2022, 4, 2)
print(christmas - now)

# if ya_birthday < now:
#     yj_birthday = ya_birthday.replave(year=ya_birthday.year+1)
# print(yj_birthday)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
# 마지막 번호가 몇 번인지 묻기
last_number = input("마지막 번호는? ")
# 1~마지막 번호까지 리스트 만들기
list_class = list(range(1, int(last_number) + 1))

# 무한반복
while True:
# 나간 친구 번호 묻기
    exclude_number = input("뺄 번호는?(종료 : enter)")
# enter치면 반복 끝내기
    if exclude_number == '':
        break
# 리스트에서 뺴기
    list_class.remove(int(exclude_number))
    print(list_class)

# 랜덤으로 섞기
random.shuffle(list_class)
# 출력
# print(list_class)
print('자리\t학생번호')
for index, n in enumerate(list_class):
    print(f'{index + 1}\t{n}')