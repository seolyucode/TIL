# 190708 startcamp - day1

## 컴퓨터 프로그래밍 언어

### 컴퓨터

컴퓨터란, 계산기다.

### 프로그래밍

명령어의 집합. 쉽게 일 시키는 것

### 언어

말, 약속



## Python 기초 문법 3형식

1. 저장
2. 조건
3. 반복



## Python 함수

파이썬 함수에는 내장 함수와 외장 함수가 있다.

* 내장함수
  * `print()`  : 출력하는 함수
  * `list()` :리스트를 생성하는 함수
  * `range()` :범위(range)를 생성하는 함수

* 외장 함수
  * `random` : 랜덤 관련 함수들의 묶음
  * `random.choice()` : 리스트에서 1개 무작위 선택
  * `random.sample(p, k)` : 모집단에서 n개의 요소를 무작위 비복원 선택

### 로또 번호 추첨 하기

```python
#서랍에서 꺼낸다
import random

# 공 바구니 numbers 만든다 (1 ~ 45)
numbers = range(1, 46) # 1 <= ? < 46

# 랜덤하게 공 바구니에서 6개를 뽑아서 lucky_numbers에 저장한다.
lucky_numbers = random.sample(numbers, 6)

# lucky_numbers를 출력한다.
print(lucky_numbers)
```



