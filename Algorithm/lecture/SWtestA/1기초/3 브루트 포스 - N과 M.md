# 브루트 포스 - N과 M

### 15649번 N과 M (1)

* 1부터 N까지 자연수 중 중복 없이 M개를 고른 수열을 모두 구하는 문제
* 1 <= M <= N <= 8

```python
import sys
n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, n, m)
        c[i] = False

go(0,n,m)
```



### 15650번  N과 M(2)

```python
import sys
n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, i+1, n, m)
        c[i] = False

go(0,1,n,m)
```

```python
import sys
n,m = map(int,input().split())
a = [0]*m
def go(index, selected, n, m):
    if selected == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    if index > n:
        return
    a[selected] = index
    go(index+1, selected+1, n, m)
    a[selected] = 0
    go(index+1, selected, n, m)

go(1,0,n,m)
```



### 15651번  N과 M(3)

```python
import sys
n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(1, n+1):
        c[i] = True
        a[index] = i
        go(index+1, n, m)
        c[i] = False

go(0,n,m)

```



### 15652번 N과 M(4)

```python
import sys
n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start, n+1):
        c[i] = True
        a[index] = i
        go(index+1, i, n, m)
        c[i] = False

go(0,1,n,m)
```

```python
import sys
n,m = map(int,input().split())
cnt = [0]*(n+1)
def go(index, selected, n, m):
    if selected == m:
        for i in range(1, n+1):
            for j in range(cnt[i]):
                sys.stdout.write(str(i)+' ')
        sys.stdout.write('\n')
        return
    if index > n:
        return
    for i in range(m-selected, 0, -1):
        cnt[index] = i
        go(index+1, selected+i, n, m)
    cnt[index] = 0
    go(index+1, selected, n, m)

go(1,0,n,m)
```



### 15654번 N과 M(5)

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(n):
        if c[i]:
            continue
        c[i] = True
        a[index] = num[i]
        go(index+1, n, m)
        c[i] = False

go(0,n,m)
```



### 15655번 N과 M(6)

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start, n):
        if c[i]:
            continue
        c[i] = True
        a[index] = num[i]
        go(index+1, i+1, n, m)
        c[i] = False

go(0,0,n,m)
```

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
a = [0]*m
def go(index, selected, n, m):
    if selected == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    if index >= n:
        return
    a[selected] = num[index]
    go(index+1, selected+1, n, m)
    a[selected] = 0
    go(index+1, selected, n, m)

go(0,0,n,m)
```



### 15656번 N과 M(7)

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(n):
        c[i] = True
        a[index] = num[i]
        go(index+1, n, m)
        c[i] = False

go(0,n,m)
```



### 15657번 N과 M(8)

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m

def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start, n):
        c[i] = True
        a[index] = num[i]
        go(index+1, i, n, m)
        c[i] = False

go(0,0,n,m)
```

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
cnt = [0]*n
def go(index, selected, n, m):
    if selected == m:
        for i in range(n):
            for j in range(cnt[i]):
                sys.stdout.write(str(num[i])+' ')
        sys.stdout.write('\n')
        return
    if index >= n:
        return
    for i in range(m-selected, 0, -1):
        cnt[index] = i
        go(index+1, selected+i, n, m)
    cnt[index] = 0
    go(index+1, selected, n, m)

go(0,0,n,m)
```



### 15663번 N과 M(9)

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
d = []
def go(index, n, m):
    if index == m:
        d.append(tuple(a))
        return
    for i in range(n):
        if c[i]:
            continue
        c[i] = True
        a[index] = num[i]
        go(index+1, n, m)
        c[i] = False
go(0,n,m)
d = sorted(list(set(d)))
for v in d:
    sys.stdout.write(' '.join(map(str,v))+'\n')
```

```python
import sys
from collections import Counter
n,m = map(int,input().split())
temp = list(map(int,input().split()))
temp = list(Counter(temp).items())
temp.sort()
n = len(temp)
num,cnt = map(list,zip(*temp))
a = [0]*m
def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(n):
        if cnt[i] > 0:
            cnt[i] -= 1
            a[index] = num[i]
            go(index+1, n, m)
            cnt[i] += 1
go(0,n,m)
```



### 15664번 N과 M(10)

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
d = []
def go(index, start, n, m):
    if index == m:
        d.append(tuple(a))
        return
    for i in range(start, n):
        if c[i]:
            continue
        c[i] = True
        a[index] = num[i]
        go(index+1, i+1, n, m)
        c[i] = False
go(0,0,n,m)
d = sorted(list(set(d)))
for v in d:
    sys.stdout.write(' '.join(map(str,v))+'\n')
```

```python
import sys
from collections import Counter
n,m = map(int,input().split())
temp = list(map(int,input().split()))
temp = list(Counter(temp).items())
temp.sort()
n = len(temp)
num,cnt = map(list,zip(*temp))
a = [0]*m
def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start,n):
        if cnt[i] > 0:
            cnt[i] -= 1
            a[index] = num[i]
            go(index+1, i, n, m)
            cnt[i] += 1
go(0,0,n,m)
```



### 15665번 N과 M(11)

```python
import sys
n,m = map(int,input().split())
num = list(set(map(int,input().split())))
num.sort()
n = len(num)
c = [False]*n
a = [0]*m
def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(n):
        c[i] = True
        a[index] = num[i]
        go(index+1, n, m)
        c[i] = False

go(0,n,m)
```

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
d = []
def go(index, start, n, m):
    if index == m:
        d.append(tuple(a))
        return
    for i in range(start, n):
        c[i] = True
        a[index] = num[i]
        go(index+1, 0, n, m)
        c[i] = False
go(0,0,n,m)
d = sorted(list(set(d)))
for v in d:
    sys.stdout.write(' '.join(map(str,v))+'\n')
```



### 15666번 N과 M(12)

```python
import sys
n,m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
c = [False]*n
a = [0]*m
d = []
def go(index, start, n, m):
    if index == m:
        d.append(tuple(a))
        return
    for i in range(start, n):
        c[i] = True
        a[index] = num[i]
        go(index+1, i, n, m)
        c[i] = False
go(0,0,n,m)
d = sorted(list(set(d)))
for v in d:
    sys.stdout.write(' '.join(map(str,v))+'\n')
```

