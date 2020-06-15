# BFS

### 13913번 숨바꼭질 4

```python
from collections import deque
import sys
MAX = 200000
sys.setrecursionlimit(MAX)
check = [False] * MAX
dist = [-1] * MAX
via = [-1] * MAX
n,m = map(int,input().split())
check[n] = True
dist[n] = 0
q = deque()
q.append(n)
while q:
    now = q.popleft()
    if now-1 >= 0 and not check[now-1]:
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1
        via[now-1] = now
    if now+1 < MAX and not check[now+1]:
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
        via[now+1] = now
    if now*2 < MAX and not check[now*2]:
        q.append(now*2)
        check[now*2] = True
        dist[now*2] = dist[now] + 1
        via[now*2] = now
print(dist[m])
def go(n, m):
    if n != m:
        go(n, via[m])
    print(m, end=' ')
go(n, m)
```



### 9019번 DSLR

```python
from collections import deque
import sys
MAX = 10001
sys.setrecursionlimit(MAX)
def go(n, m):
    if n == m:
        return
    go(n, via[m])
    print(how[m], end='')
t = int(sys.stdin.readline())
for _ in range(t): 
    n,m = map(int,input().split())
    check = [False] * MAX
    dist = [-1] * MAX
    via = [-1] * MAX
    how = [''] * MAX
    check[n] = True
    dist[n] = 0
    via[n] = -1
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        next = (now*2) % 10000
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'D'
        next = now-1
        if next == -1:
            next = 9999
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'S'
        next = (now%1000)*10 + now//1000
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'L'
        next = (now//10) + (now%10)*1000
        if not check[next]:
            q.append(next)
            check[next] = True
            dist[next] = dist[now] + 1
            via[next] = now
            how[next] = 'R'

    go(n,m)
    print()
```



### 1525번 퍼즐

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = 3
a = [list(map(int,input().split())) for _ in range(n)]
start = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            a[i][j] = 9
        start = start * 10 + a[i][j]
q = deque()
dist = dict()
dist[start] = 0
q.append(start)
while q:
    now_num = q.popleft()
    now = str(now_num)
    z = now.find('9')
    x = z//3
    y = z%3
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            temp = list(now)
            temp[x*3+y],temp[nx*3+ny] = temp[nx*3+ny],temp[x*3+y]
            num = int(''.join(temp))
            if num not in dist:
                dist[num] = dist[now_num] + 1
                q.append(num)
if 123456789 in dist:
    print(dist[123456789])
else:
    print(-1)
```



### 2251번 물통

```python
from collections import deque
moves = list(zip([0,0,1,1,2,2], [1,2,0,2,0,1]))
ans = [False]*201
check = [[False]*201 for _ in range(201)]
cap = list(map(int,input().split()))
sum = cap[2]
q = deque()
q.append((0,0))
check[0][0] = True
ans[cap[2]] = True
while q:
    now = q.popleft()
    cur = [now[0], now[1], sum-now[0]-now[1]]
    for f, t in moves:
        next = cur[:]
        next[t] += next[f]
        next[f] = 0
        if next[t] >= cap[t]:
            next[f] = next[t] - cap[t]
            next[t] = cap[t]
        if not check[next[0]][next[1]]:
            check[next[0]][next[1]] = True
            q.append((next[0],next[1]))
            if next[0] == 0:
                ans[next[2]] = True
for i in range(0, cap[2]+1):
    if ans[i]:
        print(i, end=' ')
print()
```



### 12851번 숨바꼭질 2

```python
from collections import deque
MAX = 200000
check = [False]*MAX
dist = [0]*MAX
cnt = [0]*MAX
n,m = map(int,input().split())
check[n] = True
dist[n] = 0
cnt[n] = 1
q = deque()
q.append(n)
while q:
    now = q.popleft()
    for next in [now-1, now+1, now*2]:
        if 0 <= next < MAX:
            if not check[next]:
                q.append(next)
                check[next] = True
                dist[next] = dist[now]+1
                cnt[next] = cnt[now]
            elif dist[next] == dist[now]+1:
                cnt[next] += cnt[now]
print(dist[m])
print(cnt[m])
```



### 9376번 탈옥

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, x, y):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x,y))
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and a[nx][ny] != '*':
                if a[nx][ny] == '#':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx,ny))
    return dist

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = ['.'+input()+'.' for _ in range(n)]
    n += 2
    m += 2
    a = ['.'*m] + a + ['.'*m]
    d0 = bfs(a, 0, 0)
    x1=y1=x2=y2=-1
    for i in range(n):
        for j in range(m):
            if a[i][j] == '$':
                if x1 == -1:
                    x1,y1 = i,j
                else:
                    x2,y2 = i,j
    d1 = bfs(a,x1,y1)
    d2 = bfs(a,x2,y2)
    ans = n*m

    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                continue
            cur = d0[i][j] + d1[i][j] + d2[i][j]
            if a[i][j] == '#':
                cur -= 2
            ans = min(ans,cur)
    print(ans)
```



### 9328번 열쇠

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = ['*.'+input()+'.*' for _ in range(n)]
    n += 4
    m += 4
    a = ['*'*m,'*'+'.'*(m-2)+'*'] + a + ['*'+'.'*(m-2)+'*','*'*m]
    key = set(input())
    ans = 0
    check = [[False]*m for _ in range(n)]
    q = deque()
    door = [deque() for _ in range(26)]
    q.append((1,1))
    check[1][1] = True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if check[nx][ny]:
                continue
            w = a[nx][ny]
            if w == '*':
                continue
            check[nx][ny] = True
            if w == '.':
                q.append((nx,ny))
            elif w == '$':
                q.append((nx,ny))
                ans += 1
            elif 'A' <= w <= 'Z':
                if w.lower() in key:
                    q.append((nx,ny))
                else:
                    door[ord(w)-ord('A')].append((nx,ny))
            elif 'a' <= w <= 'z':
                q.append((nx,ny))
                if not w in key:
                    key.add(w)
                    q.extend(door[ord(w)-ord('a')])
    print(ans)
```



### 4991번 로봇 청소기

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def bfs(a, sx, sy):
    n = len(a)
    m = len(a[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((sx,sy))
    dist[sx][sy] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and a[nx][ny] != 'x':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = [input() for _ in range(n)]
    b = [(0,0)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'o':
                b[0] = (i,j)
            elif a[i][j] == '*':
                b.append((i,j))
    l = len(b)
    d = [[0]*l for _ in range(l)]
    ok = True
    for i in range(l):
        dist = bfs(a,b[i][0], b[i][1])
        for j in range(l):
            d[i][j] = dist[b[j][0]][b[j][1]]
            if d[i][j] == -1:
                ok = False
    if not ok:
        print(-1)
        continue
    p = [i+1 for i in range(l-1)]
    ans = -1
    while True:
        now = d[0][p[0]]
        for i in range(l-2):
            now += d[p[i]][p[i+1]]
        if ans == -1 or ans > now:
            ans = now
        if not next_permutation(p):
            break
    print(ans)
```



### 6087번 레이저 통신

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
m,n = map(int,input().split())
a = [input() for _ in range(n)]
sx=sy=ex=ey=-1
for i in range(n):
    for j in range(m):
        if a[i][j] == 'C':
            if sx == -1:
                sx,sy = i,j
            else:
                ex,ey = i,j
dist = [[-1]*m for _ in range(n)]
q = deque()
dist[sx][sy] = 0
q.append((sx,sy))
while q:
    x,y = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        while 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == '*':
                break
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
            nx += dx[k]
            ny += dy[k]
print(dist[ex][ey]-1)
```



### 8111번 0과 1

```python
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    via = [-1]*n
    how = [-1]*n
    dist = [-1]*n
    q = deque()
    q.append(1%n)
    dist[1%n] = 0
    how[1%n] = 1
    while q:
        now = q.popleft()
        for i in [0,1]:
            next = (now*10+i)%n
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                via[next] = now
                how[next] = i
                q.append(next)
    if dist[0] == -1:
        print('BRAK')
    else:
        ans = ''
        i = 0
        while i != -1:
            ans += str(how[i])
            i = via[i]
        print(ans[::-1])
```



### 15558번 점프 게임

```python
from collections import deque
n,k = map(int,input().split())
a = [input() for _ in range(2)]
dirs = [(0,1),(0,-1),(1,k)]
dist = [[-1]*n for _ in range(2)]
q = deque()
q.append((0,0))
dist[0][0] = 0
ok = False
while q:
    x,y = q.popleft()
    for dx,dy in dirs:
        nx,ny = (x+dx)%2,y+dy
        if ny >= n:
            ok = True
            break
        if ny < 0:
            continue
        if dist[nx][ny] != -1:
            continue
        if a[nx][ny] == '0':
            continue
        if ny < dist[x][y] + 1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))
    if ok:
        break
print(1 if ok else 0)
```

