파이썬 데이터 타입

#### 데이터 타입, 숫자형 및 연산자



파이썬 데이터 타입 종류

* Boolean  1  0
* Numbers
* String
* Bytes
* Lists  아래 네개는 집합자료형
* Tuples
* Sets
* Dictionaries

```python
# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}

v_list = [3, 5, 7]  # 리스트 / 배열
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_tuple))  # <class 'tuple'>
print(type(v_set))  # <class 'set'>
print(type(v_float))  # <class 'float'>
```



파이썬 숫자형 및 연산자

* +더하기
* -빼기
* *곱하기
* /나누기
* //나누기(몫)
* %나누기(나머지)
* **지수(제곱)
* 단항 연산자

```python
i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999999
bit_int2 = 7777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5  # 0.5
f4 = 10.  # 10.0

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)  # 자동 형변환

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)  # 9.0

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))  # 10.0
print(complex(3))  # (3+0j)
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))  # 0j

y = 100
y += 100
print(y)  # 200
y *= 100

# 수치 연산 함수
# http://docs.python.org/3/library/math.html

print(abs(-7))  # 7
n, m = divmod(100, 8)  # 몫은 n, 나머지는 m에 들어감
print(n, m)

import math  # 수학 관련 패키지를 사용할 수 있는 모듈 불러오기
print(math.ceil(5.1))  # 6
print(math.floor(3.874))  # 3
```



#### 문자형 및 연산자

문자형 관련 연산자

* 문자열 생성, 길이
* 이스케이프 문자
* 문자열 연산
* 문자열 형 변환
* 문자열 함수
* 문자열 슬라이싱

```python
# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ''
str4 = str()
str5 = str('ace')

print(len(str1), len(str2), len(str3), len(str4), len(str5))  # 9 7 0 0 3 /  공백도 셈


escape_str1 = "Do you have a \"big collection\""
print(escape_str1)  # Do you have a "big collection"
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)  # Tab	Tab    Tab


# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)  # C:\Programs\Test\Bin
raw_s2 = r"\\a\\a"
print(raw_s2)  # \\a\\a


# 멀티라인
multi = \  # 변수 선언 후 \ 기호 나오면 그 다음줄에 이어진다는 의미
"""
문자열 

멀티라인 

테스트 
"""
print(multi)
'''
문자열

멀티라인

테스트
'''

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)  # abcdef
print(str_o1 + 3)  # 에러. 형 달라서 결합 불가능
print('a' in str_o4)  # True  /  a라는 문자가 str_o4에 포함되어 있는가
print('z' not in str_o4)  # True


# 문자열 형 변환
print(str(77) + 'a')  # 77a
print(str(10.4))

# 문자열 함수
# 참고: https://www.w3schools.com/python/python_ref_string.asp

a = 'niceman'
b = 'orange'

print(a.islower())  # True
print(a.endswith('s'))  # False  /  끝글자가 s로 끝나는가
print(a.capitalize())  # Niceman
print(a.replace('nice', 'good'))  # goodman
print(list(reversed(b)))  # ['e', 'g', 'n', 'a', 'r', 'o']


c = 'niceman'
d = 'orange'

print(a[0:3])  # nic
print(a[0:4])  # nice
print(a[0:7])
print(a[0:len(a)])
print(a[:4])  # 처음부터 인덱스가 4 이전까지
print(a[0:len(a-1)])
print(a[:])  # 처음부터 끝까지
print(b[0:4:2])  # oa
print(b[1:-2])  # ran
print(b[::-1])  # 처음부터 끝까지 역순  /  egnaro
```



리스트, 튜플

파이썬 자료구조(List, Tuple)

* 리스트 특징
* 튜플 특징
* 인덱싱
* 슬라이싱
* 삽입, 삭제, 함수 사용

```python
name1 = 'Lee'
name2 = 'Park'
```

```python
# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(str(c[0])+'hi')  # 형변환

# 리스트 수정, 삭제
c[0] = 77
print(c)  # [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000]
print(c)  # [77, 100, 1000, 10000, 3, 4]
c[1] = ['a', 'b', 'c']
print(c)  # [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]

del c[1]
print(c)  # [77, 1000, 10000, 3, 4]
del c[-1]
print(c)  # [77, 1000, 10000, 3]

# 리스트 함수
```

