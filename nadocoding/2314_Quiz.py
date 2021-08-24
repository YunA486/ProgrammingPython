# 3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# 출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력
# 예시
# id_number = 020316 일 때
#
# 출력 예시
# 02
# 0316
# 732

id_number = "040402"

year = id_number[0:2]
month = id_number[2:]

print("출생 년도 끝 두자리 : " + year)
print("출생 월일 : " + month)
print(int(year) * int(month))

# print("둘의 곱은 : " + str(int(year) * (int(month))

print("--------------------------------------------")

# 3-2. 집 전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# 예시
# phone_number = 02-1234-5678 또는 032-9876-4321
#
# 출력 예시
# 02 또는 032
# 5678 또는 4321

phone_number = "02-1234-5678"

# print("지역번호 : " + phone_number[0:4])-
print("전화번호 앞 자리 : " + phone_number.split("-")[0])
print("전화번호 뒷 자리 : " + phone_number.split("-")[2])

#  x = phone_number.index('-')
# print(phone_number[0:x])        #[:2]
# print(phone_number[-4:])        #[8:]

# 전화번호 입력 시, -가 있든 없든 알아들음

# phone_number1 = '010-1234-5678'
# phone_number2 = '01098765432'
# phone_number3 = '010 1111 2222'

# phone_number = phone_number3
# result = phone_number.replace('-','').replace(' ','')
# print(result)


print("--------------------------------------------")

# Quiz2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.

student_number = input("학번을 입력하세요 : ")

ban = int(student_number[1])

if ban == 1 or ban == 2:
    print(ban, "반 뉴미디어 소프트웨어과입니다.")
elif ban == 3 or ban == 4:
    print(ban, "반 뉴미디어 웹 솔루션과입니다.")
elif ban == 5 or ban == 6:
    print(ban, "반 뉴미디어 디자인과입니다.")
else:
    print("1에서 6반까지 입력해주세요")

# student_number = "2314"
# number = student_number[1]
# number = int(number)

# majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
# if 1 <= number <= 6:
#   print(f'{number}반 {majors[(number-1)//2]}')
# else:
#   print("잘못입력했습니다.")

print("--------------------------------------------")

# Quiz2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2

def get_major(argumenet):
    if argumenet[1] == "1" or argumenet[1] == "2":
        major = "뉴미디어소프트웨어과"
        return argumenet[0], major
    elif argumenet[1] == "3" or argumenet[1] == "4":
        major = "뉴미디어웹솔루션과"
        return argumenet[0], major
    elif argumenet[1] == "5" or argumenet[1] == "6":
        major = "뉴미디어디자인과"
        return argumenet[0], major

grade, major = get_major("2314")
print(major, grade)

print("--------------------------------------------")

# Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5

def average(list):
    return (sum(list) / len(list))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("평균 값 : {}".format(average(list)))

"""
def average(*numbers):
  sum_Value = 0
  count = 0
  for number in numbers:
      sum_value += number
      count += 1
  return sum_Value / count

print(average(10, 20, 30))
print(average(4, 23))
"""

"""
def average2(*numbers):
  sum = 0
  return sum(numbers) / len(numbers)

print(average(10, 20,30))
print(average(4, 23))

--> 이렇게 하면 안됨.
"""

print("--------------------------------------------")

# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만
#
# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

def get_bmi(height, weight):
    height = height * 0.01
    get_bmi = weight / (height * height)
    print("BMI : ", round(get_bmi), 3)

    if get_bmi < 18.5:
        print("저체중")
    elif 18.5 <= get_bmi < 23.0:
        print("보통")
    elif 23.0 <= get_bmi < 25.0:
        print("비만")
    else:
        print("고도비만")


bmi = get_bmi(176, 69)
print(bmi)


"""
def get_bmi(height, weight):
    height /= 100
    return round((weight / (height ** 2)), 1)
    
bmi = get_bmi(176, 69)

if bmi < 18.5:
    print("저체중")
elif bmi < 23:
    print("정상")
elif bmi < 25:
    print("과체중")
elif bmi:
    print("비만")

"""

print("--------------------------------------------")

# 구구단 7단 출력하기
for i in range(1, 9 + 1):   # i : 1~9
    print(f'7 x {i} = {7 * i}')

print("--------------------------------------------")

# 구구단 2~9단 출력하기
for dan in range(2, 10):    # dan : 2~9
    for i in range(1, 9 + 1):   # i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)

print("--------------------------------------------")

# 구구단 2~7단까지 출력하기
for dan in range(2, 9 + 1):    # dan : 2~9
    for i in range(1, 9 + 1):   # i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
    if dan == 7:
        break

print("--------------------------------------------")

# 구구단 2~7단 출력하되, x1, x3, x5, x7, x9인 것만 출력하기
for dan in range(2, 9 + 1):    # dan : 2~9
    for i in range(1, 9 + 1):   # i : 1~9
        if i % 2 == 0:           # i == 2 or i == 4 or i == 6 or i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
    if dan == 7:
        break

print("--------------------------------------------")

'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''

# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1

def n_sum(argument):
    num = str(argument)
    sum = 0

    if len(num) >= 10:
        return -1

    # for i in range(len(num)):   #num: '408' len(num): 3 range(3): 0, 1, 2
    #     sum += int(num[i])

    for i in num:
        sum += int(i)

    return sum

result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1


print("--------------------------------------------")

'''
Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
* 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''

# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

def get_subway_fare(km):
    money = 720

    if km <= 10:
        return money

    elif 10 < km < 50:
        for km in range(10, km, 5):     #range(10, 25, 5): 10, 15, 20
            money += 100
        return money

    elif 50 < km:
        money = 1520
        for km in range(50, km, 8):
            money += 100
        return money

fare = get_subway_fare(10)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(25)
print(fare)        #1020
fare = get_subway_fare(61)
print(fare)        #1720

print("--------------------------------------------")

'''
Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
* 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''

# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝

def get_three_six_nine(num):
    jjak = ""

    number = str(num)

    count = number.count("3") + number.count("6") + number.count("9")

    if count == 0:
        jjak = number
    else:
        # for i in range(count):
        #     jjak += "짝"
        jjak = "짝" * count

    return jjak

result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝


print("--------------------------------------------")

'''
Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
1. 함수의 이름을 정해준다.
2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
3. 리턴하는 것을 말해준다.
4. 출력 예시를 보여준다.
5. 내가 낸 문제의 답안을 제출한다.
'''


"""
Quiz. 
1. octal()함수를 만든다. 
2. 함수에 숫자 1개를 넣는다.
3. 10진수를 2진수로 변환 후 그 숫자들을 더하여 리턴한다.
4. result = octal(5)
   print(result)    #2(1 + 0 + 1)
   result = octal(13)
   print(result)    #3(1 + 1 + 0 + 1)
   result = octal(100)
   print(result)    #3(1 + 1 + 0 + 0 + 1 + 0 + 0)
   
"""

def octal(argument):

    sum = 0

    x = argument
    y = ""
    while x > 0:
        y = str(x % 2) + y
        x //= 2

    for i in range(len(y)):
        sum += int(y[i])
    return sum

result = octal(5)
print(result)
result = octal(13)
print(result)
result = octal(100)
print(result)

print("--------------------------------------------")

'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''

def is_prime(num):
    if num != 1:
        for f in range(2, num):
            if num % f == 0:
                return "소수 아님"
    else:
        return "소수 아님"

    return "소수"

result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님

print("--------------------------------------------")

'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''

def get_compliment(text):
    if "고구마" in text:
        return "왓쇼이!"
    elif "맛있는" in text:
        return "우마이!"
    elif "놀랄 만한" in text:
        return "요모야..!"
    elif "황당한" in text:
        return
    elif "굉장한" in text:
        return
    else:
        return "으무!"

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!

'''
result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!
'''


print("--------------------------------------------")

'''
Quiz5-1. 모듈이란?

필요한 것들끼리 부품처럼 잘 만들어진 파일
파이썬에서는 함수 정의나 클래스등의 파이썬 문장들을 담고 있는 파일, 모듈은 확장자가 .py

Quiz5-2. 패키지란?

모듈들을 모아놓은 집합
하나의 디렉터리에 여러모듈 파일들을 모아놓은 것

Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요

from theater_module import price as p2314

Quiz5-4. __all__의 역할은?

디렉터리 모듈을 *을 이용하여 import할 때에 필요함
공개범위를 설정

Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?

if __name__ == "__main__"

Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
< 가 > 
trip_tp = travel.vietnam.ThailandPackage()
trip_to.detail()


from travel import vietnam
< 나 > 
trip_to = vietnam.ThailandPackage()
trip_to.detail()


from travel.vietnam import ThailandPackage
< 다 > 
trip_to = ThailandPackage()
tipr_to.detail()

'''

