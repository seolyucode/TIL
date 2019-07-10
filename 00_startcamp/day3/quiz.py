'''
# #print('이름을 적으세요')
# name = input('What\'s your name?: ') #입력받는 함수. 
# print('hi, ' + name)


# 박스 안에 든 타입/클래스?
words = input('입력 고고: ') # words에 string이 저장됨.
# 사용자의 입력을 받으면 str. 문자열도 리스트. 인덱스 접근 가능
print(type(words)) # type = class
print(words[0], words[-1])

my_list = list(words) # 리스트화하는 함수. 사실 안해도
print(my_list)
print(my_list[0], my_list[-1]) 

word = input('안내멘트. word 타입무관')
print(type(word))
print(word)

# words의 첫 글자와 마지막 글자를 출력하라.

import random

length = random.choice(range(1, 100)) # 만약 50
numbers = list(range(length)) # [0, 1, 2, .. , 49]
print(numbers[length-1])
print(numbers[-1]) #뒤에서 첫번째. 마지막.


numbers = [1, 2, 3, 4, 5]

# numbers의 첫 요소와 마지막 요소를 출력하라.

print(numbers[0])
print(numbers[4])
'''

'''
# n을 입력받고, 1부터 n까지 출력하라
# 형변환 
n = input('자연수를 입력하세요') # '10' => 10 숫자로
print(type(n))
n = int(n) # str => list(str) / str => int(str)
print(type(n))

for num in range(n):
    print(num + 1, end = ' ') # end = ' ' 가로출력
'''

# string = input('숫자를 입력하세요: ')
# number = int(string)
# number = int(input('숫자를 입력하세요: ')) # O

'''
# lotto
import random
# numbers = list(range(1, 46))
# lucky = random.sample(numbers, 6)
# print(lucky)

print(random.sample(list(range(1, 46)), 6)) # X
'''

'''
number = int(input('숫자를 입력하세요: '))

# 짝수/홀수를 구분하자. 2 => 짝! 3 => 홀!

if number % 2 == 0: # %연산자는 나눈 나머지
    print("짝!")
else:
    print("홀!")


if number % 2 == 1:
    print('홀!')
else:
    print('짝!')
'''

# fizz buzz => 3배수 fizz / 5배수 buzz / 15배수 fizzbuzz
'''
number = int(input('숫자를 입력하세요: '))

if number % 15 == 0:
    print('fizzbuzz')
elif number % 5 == 0:
    print('buzz')
elif number % 3 == 0:
    print('fizz')
'''
# fizz buzz => 3배수 fizz / 5배수 buzz / 15배수 fizzbuzz
# 1 ~ number 까지 출력
# 그와중에 3 fizz => 5 buzz => 15 fizzbuzz
# 동전분류기


number = int(input('숫자를 입력하세요:'))
for i in range(1, number+1):
    # if i % 3 == 0 and i % 5 == 0: #if에 들어가면 나머지는 X
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)


