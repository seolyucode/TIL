# 함수에서 작성했던 피보나치 함수 두가지(재귀, 반복문)를 작성합니다.
def fibo_for(n):
    if n < 2:
        return n
    
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
        
    return b

def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)