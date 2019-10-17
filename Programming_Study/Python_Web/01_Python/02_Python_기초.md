Python_기초

#### Print 함수의 이해

Print

* 가장 기본적인 Output(출력) 함수
* 기본 출력
* Separator, End 옵션 사용
* Format 형식 출력
* Escape Code 사용법

```python
# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()  # 자동 줄바꿈

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep='')  # TEST
print('2019', '02', '19', sep='-')  # 2019-02-19
print('niceman', 'google.com', sep='@')  # 이메일형식

# end 옵션 사용
print('Welcome To', end='')
print(' the black parade', end='')
print(' piano notes')

print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
# Welcome To the black parade piano notes

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
# You and Me
print("{0} and {1} and {0}".format('You', 'Me'))
# 숫자를 내부에서 매핑
# You and Me and You
print('{a} and {b}'.format(a='You', b='Me'))
# You and Me

print("%s's favorite number is %d" % ('Seolyu', 4)) # %s : 문자, %d : 정수, %f : 실수
# Seolyu's favorite number is 4

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))
# Test1:   776, Price: 6534.12

'''
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폴 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
'''

print("'you'")
# 'you'
print('\'you\'')
# 'you'
print('"you"')
# "you"
print("""'you'""")
# 'you'
print('\\you\\\n')
print('test')
# \you\
#
# test
print('\t\t\ttest')
# 			test
```



파이썬 구성요소 기초 학습

* 인코딩(입력, 출력)
* 변수
* 조건문
* 함수, 클래스, 인스턴스(객체)
* 정보 출력

```python
# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습
import this
```

```python
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)  # utf-8
print(sys.stdout.encoding)  # utf-8

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Goodboy'
# 조건문
if myName == "Goodboy":
    print('OK')  # indent
# OK

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)

# 변수 선언(한글)
이름 = "좋은사람"
# 출력
print(이름)
# 좋은사람

# 함수 선언
def 인사():
    print("안녕하세요. 반갑습니다.")
    
인사()  # 안녕하세요. 반갑습니다.

# 함수 선언
def greeting():
    print('Hello!')
    
greeting()  # Hello!

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()  # 변수 선언하고 만들어놓은 클래스를 함수 실행하듯

print(id(cookie))
print(dir(cookie))
```



