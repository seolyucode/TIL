# BFS

### 15653번 구슬 탈출 4

```python
from collections import deque
import copy
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def simulate(a, k, x, y):
    if a[x][y] == '.':
        return (False, False, x, y)
    n = len(a)
    m = len(a[0])
    moved = False
    while True:
        nx,ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return (moved, False, x, y)
        if a[nx][ny] == '#':
            return (moved, False, x, y)
        elif a[nx][ny] in 'RB':
            return (moved, False, x, y)
        elif a[nx][ny] == '.':
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            x,y = nx,ny
            moved = True
        elif a[nx][ny] == 'O':
            a[x][y] = '.'
            moved = True
            return (moved, True, x, y)

def go(b, rx, ry, bx, by, direction):
    a = copy.deepcopy(b)
    a[rx][ry] = 'R'
    a[bx][by] = 'B'
    hole1 = False
    hole2 = False
    while True:
        rmoved, rhole, rx, ry = simulate(a, direction, rx, ry)
        bmoved, bhole, bx, by = simulate(a, direction, bx, by)
        if not rmoved and not bmoved:
            break
        if rhole:
            hole1 = True
        if bhole:
            hole2 = True
    return (hole1, hole2, rx, ry, bx, by)

n,m = map(int,input().split())
a = [list(input()) for _ in range(n)]
d = [[[[-1]*m for k in range(n)] for j in range(m)] for i in range(n)]
ans = -1
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 'O':
            hx,hy = i,j
        elif a[i][j] == 'R':
            rx,ry = i,j
            a[i][j] = '.'
        elif a[i][j] == 'B':
            bx,by = i,j
            a[i][j] = '.'
q.append((rx,ry,bx,by))
d[rx][ry][bx][by] = 0
found = False
while q:
    rx,ry,bx,by = q.popleft()
    for k in range(4):
        hole1,hole2,nrx,nry,nbx,nby = go(a,rx,ry,bx,by,k)
        if hole2:
            continue
        if hole1:
            found = True
            ans = d[rx][ry][bx][by] + 1
            break
        if d[nrx][nry][nbx][nby] != -1:
            continue
        q.append((nrx,nry,nbx,nby))
        d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1
    if found:
        break
print(ans)
```



### 5213번 과외맨

```python
from collections import deque
dx0 = [-1,-1,0,0,1,1]
dy0 = [-1,0,-1,1,-1,0]
dx1 = [-1,-1,0,0,1,1]
dy1 = [0,1,-1,1,0,1]
dx = [dx0,dx1]
dy = [dy0,dy1]

def ok(x, y):
    if x < 0 or x >= n:
        return False
    if x%2 == 0:
        return 0 <= y < n
    else:
        return 0 <= y < n-1

def go(x1, y1, x2, y2):
    if x1 == x2:
        if y1 < y2:
            return a[x1][y1][1] == a[x2][y2][0]
        else:
            return a[x1][y1][0] == a[x2][y2][1]
    else:
        if x1%2 == 0:
            if y1 == y2:
                return a[x1][y1][1] == a[x2][y2][0]
            else:
                return a[x1][y1][0] == a[x2][y2][1]
        else:
            if y1 == y2:
                return a[x1][y1][0] == a[x2][y2][1]
            else:
                return a[x1][y1][1] == a[x2][y2][0]

def num(x, y):
    ans = x//2*(n*2-1)
    if x%2 == 1:
        ans += n
    ans += y+1
    return ans

n = int(input())
a = [[] for _ in range(n)]
for i in range(n):
    lim = n if i%2 == 0 else n-1
    for j in range(lim):
        a[i].append(tuple(map(int,input().split())))

q = deque()
check = [[False]*n for _ in range(n)]
dist = [[False]*n for _ in range(n)]
via = [[-1]*n for _ in range(n)]
check[0][0] = True
dist[0][0] = 1
q.append((0,0))

while q:
    x,y = q.popleft()
    for k in range(6):
        nx,ny = x+dx[x%2][k], y+dy[x%2][k]
        if not ok(nx,ny):
            continue
        if not go(x, y, nx, ny):
            continue
        if check[nx][ny]:
            continue
        check[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1
        via[nx][ny] = (x,y)
        q.append((nx,ny))

x = n-1
y = n-1

while not check[x][y]:
    y -= 1
    if y < 0:
        x -= 1
        y = n-1
        if x%2 == 1:
            y -= 1

print(dist[x][y])
s = []
while not (x == 0 and y == 0):
    s.append((x,y))
    x, y = via[x][y]
s.append((x,y))

while s:
    print(num(*s[-1]),end=' ')
    s.pop()
print()
```



### 3184번 양

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(sx, sy):
    q = deque()
    q.append((sx,sy))
    check[sx][sy] = True
    cnt = [0, 0]
    while q:
        x,y = q.popleft()
        if a[x][y] == 'v':
            cnt[0] += 1
        elif a[x][y] == 'o':
            cnt[1] += 1
        
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[nx][ny] == '#':
                continue
            if check[nx][ny]:
                continue
            q.append((nx,ny))
            check[nx][ny] = True
    return cnt

n,m = map(int,input().split())
a = [input() for _ in range(n)]
check = [[False]*m for _ in range(n)]
d = []
for i in range(n):
    for j in range(m):
        if a[i][j] != '#' and not check[i][j]:
            d.append(bfs(i, j))
v,o = 0,0
for cnt in d:
    if cnt[0] >= cnt[1]:
        v += cnt[0]
    else:
        o += cnt[1]
print(f"{o} {v}")
```



### 5014번 스타트링크

```python
from collections import deque
f,s,g,u,d = map(int, input().split())
check = [False] * (f+1)
dist = [0] * (f+1)
q = deque()
q.append(s)
check[s] = True
while q:
    now = q.popleft()
    if now+u <= f and not check[now+u]:
        dist[now+u] = dist[now] + 1
        check[now+u] = True
        q.append(now+u)
    if now-d >= 1 and not check[now-d]:
        dist[now-d] = dist[now] + 1
        check[now-d] = True
        q.append(now-d)
if check[g]:
    print(dist[g])
else:
    print('use the stairs')
```



### 12886번 돌 그룹

```python
import sys
sys.setrecursionlimit(1500*1500)
check = [[False]*1501 for _ in range(1501)]
x,y,z = map(int,input().split())
s = x+y+z
def go(x, y):
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, s-x-y]
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                b = [x, y, s-x-y]
                b[i] += a[i]
                b[j] -= a[i]
                go(b[0], b[1])
if s % 3 != 0:
    print(0)
else:
    go(x,y)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)
```



### 14442번 벽 부수고 이동하기 2

```python
from collections import deque
a = [[0]*1000 for _ in range(1000)]
d = [[[0]*11 for i in range(1000)] for j in range(1000)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m,l = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,list(input()))))
q = deque()
d[0][0][0] = 1
q.append((0,0,0))
while q:
    x,y,z = q.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] == 0 and d[nx][ny][z] == 0:
            d[nx][ny][z] = d[x][y][z] + 1
            q.append((nx,ny,z))
        if z+1 <= l and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
            d[nx][ny][z+1] = d[x][y][z] + 1
            q.append((nx,ny,z+1))
ans = -1
for i in range(l+1):
    if d[n-1][m-1][i] == 0:
        continue
    if ans == -1:
        ans = d[n-1][m-1][i]
    elif ans > d[n-1][m-1][i]:
        ans = d[n-1][m-1][i]
print(ans)
```



### 1600번 말이 되고픈 원숭이

```python
from collections import deque
dx = [0,0,1,-1,-2,-1,1,2,2,1,-1,-2]
dy = [1,-1,0,0,1,2,2,1,-1,-2,-2,-1]
cost = [0,0,0,0,1,1,1,1,1,1,1,1]
a = [[0]*200 for _ in range(200)]
d = [[[-1]*31 for i in range(200)] for j in range(200)]
l = int(input())
m,n = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
q = deque()
q.append((0,0,0))
d[0][0][0] = 0
while q:
    x,y,c = q.popleft()
    for k in range(12):
        nx = x+dx[k]
        ny = y+dy[k]
        nc = c+cost[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1:
                continue
            if nc <= l:
                if d[nx][ny][nc] == -1:
                    d[nx][ny][nc] = d[x][y][c] + 1
                    q.append((nx,ny,nc))
ans = -1
for i in range(l+1):
    if d[n-1][m-1][i] == -1:
        continue
    if ans == -1 or ans > d[n-1][m-1][i]:
        ans = d[n-1][m-1][i]
print(ans)
```



### 10026번 적록색약

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def can(blind, u, v):
    if u == v:
        return True
    if blind:
        if u == 'R' and v == 'G':
            return True
        if u == 'G' and v == 'R':
            return True
    return False

def go(a, blind):
    n = len(a)
    check = [[False]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            ans += 1
            q = deque()
            q.append((i,j))
            check[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx,ny = x+dx[k], y+dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if check[nx][ny]:
                            continue
                        if can(blind, a[x][y], a[nx][ny]):
                            check[nx][ny] = True
                            q.append((nx,ny))
    return ans

n = int(input())
a = [input() for _ in range(n)]
print(str(go(a, False)) + ' ' + str(go(a, True)))
```



### 2234번 성곽

```python
from collections import deque
dx = [0,-1,0,1]
dy = [-1,0,1,0]
m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
def bfs(x, y, rooms):
    q = deque()
    q.append((x,y))
    d[x][y] = rooms
    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] != 0:
                continue
            if (a[x][y] & (1<<k)) > 0:
                continue
            q.append((nx,ny))
            d[nx][ny] = rooms
    return cnt
rooms = 0
room = [0]
for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            rooms += 1
            room.append((bfs(i,j,rooms)))
print(rooms)
ans = 0
for i in range(1,rooms+1):
    if ans < room[i]:
        ans = room[i]
print(ans)
ans = 0
for i in range(n):
    for j in range(m):
        x,y = i,j
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] == d[x][y]:
                continue
            if (a[x][y] & (1<<k)) > 0:
                if ans < room[d[x][y]]+room[d[nx][ny]]:
                    ans = room[d[x][y]]+room[d[nx][ny]]
print(ans)
```



### 3197번 백조의 호수

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
wcheck = [[False]*m for _ in range(n)]
scheck = [[False]*m for _ in range(n)]
sx,sy,ex,ey=-1,-1,-1,-1
swan = deque()
nswan = deque()
water = deque()
nwater = deque()
a = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            if sx == -1:
                sx,sy = i,j
            else:
                ex,ey = i,j
            a[i][j] = '.'

        if a[i][j] == '.':
            water.append((i,j))
            wcheck[i][j] = True

swan.append((sx,sy))
scheck[sx][sy] = True

i = 0
while True:
    while water:
        x,y = water.popleft()
        a[x][y] = '.'
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if wcheck[nx][ny]:
                continue
            if a[nx][ny] == '.':
                water.append((nx,ny))
                wcheck[nx][ny] = True
            else:
                nwater.append((nx,ny))
                wcheck[nx][ny] = True
    while swan:
        x,y = swan.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if scheck[nx][ny]:
                continue
            if a[nx][ny] == '.':
                swan.append((nx,ny))
                scheck[nx][ny] = True
            else:
                nswan.append((nx,ny))
                scheck[nx][ny] = True
    if scheck[ex][ey]:
        print(i)
        break
    i += 1
    water = nwater
    swan = nswan
    nwater = deque()
    nswan = deque()
```



### 12906번 새로운 하노이 탑

```python
from collections import deque
s = []
for i in range(3):
    temp = input().split()
    cnt = int(temp[0])
    if cnt > 0:
        s.append(temp[1])
    else:
        s.append('')
cnt = [0,0,0]
for i in range(3):
    for ch in s[i]:
        cnt[ord(ch)-ord('A')] += 1
d = dict()
q = deque()
q.append(tuple(s))
d[tuple(s)] = 0
while q:
    x = q.popleft()
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if len(x[i]) == 0:
                continue
            y = list(x[:])
            y[j] = y[j] + x[i][-1]
            y[i] = y[i][:-1]
            y = tuple(y)
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)

ans = ['', '', '']
for i in range(3):
    for j in range(cnt[i]):
        ans[i] += chr(ord('A')+i)
print(d[tuple(ans)])
```



### 14395번 4 연산

```python
from collections import deque
limit = 1000000000
s,t = map(int,input().split())
check = set()
q = deque()
q.append((s,''))
check.add(s)
while q:
    x, s = q.popleft()
    if x == t:
        if len(s) == 0:
            s = '0'
        print(s)
        exit()
    if 0 <= x*x <= limit and x*x not in check:
        q.append((x*x,s+'*'))
        check.add(x*x)
    if 0 <= x+x <= limit and x+x not in check:
        q.append((x+x,s+'+'))
        check.add(x+x)
    if 0 <= x-x <= limit and x-x not in check:
        q.append((x-x,s+'-'))
        check.add(x-x)
    if x != 0 and 0 <= x//x <= limit and x//x not in check:
        q.append((x//x,s+'/'))
        check.add(x//x)
print(-1)
```



### 2151번 거울 설치

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
s = [input() for _ in range(n)]
b = [[0]*n for _ in range(n)]
v = []
start,end = -1,-1
for i in range(n):
    for j in range(n):
        if s[i][j] == '#':
            if start == -1:
                start = len(v)
            else:
                end = len(v)
            v.append((i,j))
            b[i][j] = len(v)-1
        elif s[i][j] == '!':
            v.append((i,j))
            b[i][j] = len(v)-1
m = len(v)
a = [[False]*m for _ in range(m)]
for i in range(len(v)):
    for k in range(4):
        x,y = v[i]
        x += dx[k]
        y += dy[k]
        while 0 <= x < n and 0 <= y < n:
            if s[x][y] == '*':
                break
            if s[x][y] == '!' or s[x][y] == '#':
                a[i][b[x][y]] = True
            x += dx[k]
            y += dy[k]
q = deque()
dist = [-1] * m
q.append(start)
dist[start] = 0
while q:
    now = q.popleft()
    for i in range(m):
        if a[now][i] != 0 and dist[i] == -1:
            dist[i] = dist[now] + 1
            q.append(i)
print(dist[end]-1)
```



### 16137번 견우와 직녀

```python
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = -1
def bfs():
    dist = [[[-1]*20 for j in range(n)] for i in range(n)]
    q = deque()
    q.append((0,0,0))
    dist[0][0][0] = 0
    while q:
        x,y,t = q.popleft()
        if a[x][y] >= 2 and t%a[x][y] != 0:
            nt = (t+1)%a[x][y]
            if dist[x][y][nt] == -1:
                dist[x][y][nt] = dist[x][y][t] + 1
                q.append((x,y,nt))
        else:
            for k in range(4):
                nx,ny = x+dx[k], y+dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[x][y] >= 2 and a[nx][ny] >= 2:
                        continue
                    if a[nx][ny] >= 1:
                        nt = (dist[x][y][t]+1)%a[nx][ny]
                        if dist[nx][ny][nt] == -1:
                            dist[nx][ny][nt] = dist[x][y][t] + 1
                            q.append((nx,ny,nt))
    ans = -1
    for i in range(20):
        if dist[n-1][n-1][i] == -1:
            continue
        if ans == -1 or ans > dist[n-1][n-1][i]:
            ans = dist[n-1][n-1][i]
    return ans
def can(i,j):
    garo = False
    if j-1 >= 0 and a[i][j-1] == 0:
        garo = True
    if j+1 < n and a[i][j+1] == 0:
        garo = True
    sero = False
    if i-1 >= 0 and a[i-1][j] == 0:
        sero = True
    if i+1 < n and a[i+1][j] == 0:
        sero = True
    return not (garo and sero)
for i in range(n):
    for j in range(n):
        if a[i][j] == 0 and can(i,j):
            a[i][j] = m
            now = bfs()
            if now != -1:
                if ans == -1 or ans > now:
                    ans = now
            a[i][j] = 0
print(ans)
```

