# 그래프와 BFS

## 그래프 Graph

* 자료구조의 일종
* 정점 (Node, Vertex)
* 간선 (Edge) : 정점간의 관계를 나타냄
* G = (V, E)

## 

## 경로 Path

* 정점 A에서 B로 가는 경로
* A -> C -> D -> E -> B
* A -> B : 최단경로(가중치 있을 땐 가중치 합이 가장 작은거)
* A -> C -> B
* A -> C -> E -> B



## 사이클

* 시작점과 도착점이 같은 경로



## 단순 경로와 단순 사이클 Simple Path and Simple Cycle

* 경로/사이클에서 같은 정점을 두 번 이상 방문하지 않는 경로/사이클
* 특별한 말이 없으면, 일반적으로 사용하는 경로와 사이클은 단순 경로/사이클을 말한다.



## 방향 있는 그래프 Directed Graph

* A -> C 와 같이 간선에 방향이 있다.



## 방향 없는 그래프 Undirected Graph

* A-C는 A->C와 C->A를 나타낸다
* 양방향 그래프(Bidirection Graph)



## 간선 여러개 Multiple Edge

* 두 정점 사이에 간선이 여러 개일 수도 있다.
* A-B는 연결하는 간선이 2개
* 두 간선은 서로 다른 간선



## 루프 Loop

* 간선의 양 끝 점이 같은 경우
* A -> A



## 가중치 Weight

* 간선에 가중치가 있는 경우
* A에서 B로 이동하는 거리, 이동하는데 필요한 시간, 이동하는데 필요한 비용 등등
* 가중치가 없는 경우에는 1이라고 생각하면 됨



## 차수 Degree

* 정점과 연결되어 있는 간선의 개수
* 방향 그래프의 경우 In-degree(들어오는 간선), Out-degree(나가는 간선)로 나누어서 차수를 계산



# 그래프의 표현 Representation of Graph

간선에 방향이 없는 방향이 없는 그래프. 정점이 6개, 간선이 8개

정점: {1, 2, 3, 4, 5, 6}

간선: {(1, 2), (1, 5), (2, 5), (2, 3), (3, 4), (2, 4), (4, 5), (4, 6)}



### 인접 행렬 Adjacency-matrix

* 정점의 개수를 V이라고 했을 때
* V X V 크기의 이차원 배열을 이용
* $A[i]A[j] = 1$ (i -> j 간선이 있을 때), 0 (없을 때)



### 인접 리스트 Adjacency-list

* 리스트를 이용해서 구현
* A[i] = i와 연결된 정점을 리스트로 포함하고 있음
* 리스트의 크기는 동적으로 변경할 수 있어야 한다
* 즉, 링크드 리스트나 길이를 동적으로 변경할 수 있는 배열을 사용. 파이썬은 List

```
A[1] (2,2) (5,7)
A[2] (1,2) (3,2) (4,3) (5,1)
A[3] (2,2) (4,1)
A[4] (3,1) (5,7) (2,3) (6,7)
A[5] (1,7) (2,1) (4,7)
A[6] (4,7)
```



## 공간 복잡도 Space Complexity

* 인접 행렬: O(V^2)

  * 장점 2가지

    1. 인접 행렬은 임의의 두 정점 u,v가 주어졌을 때 u->v 존재하는지 O(1) $A[u][v]$ 가 1인지 보면 됨

       인접 리스트는 A[u] 간선 모두 살펴봐야해서 u의 차수만큼 걸림

    2. 임의의 두 정점 u,v가 주어졌을 때 반대방향 정점 찾는 것도 O(1)

       인접 리스트는 v의 차수만큼 걸림

* 인접 리스트: O(E)

예외 : 완전 그래프. 그래프의 모든 정점 사이에 간선이 존재. $E=V(V-1)/2$ 인접 행렬이 더 좋음



## 간선 리스트 Edge-list

* 배열을 이용해서 구현
* 간선을 모두 저장
* E라는 배열에 간선을 모두 저장
* 동적 할당 없이 인접 리스트와 비슷한 효과



# 그래프의 탐색 (DFS, BFS)



### 그래프의 탐색 

목적 : 시작점 X 시작해서 모든 정점을 1번씩

* DFS: 깊이 우선 탐색
* BFS: 너비 우선 탐색



### 깊이 우선 탐색 Depth First Search

* 스택을 이용해서 갈 수 있는 만큼 최대한 많이 가고
* 갈 수 없으면 이전 정점으로 돌아간다.

정점을 한번씩 방문했는지 확인하기 위해 check 배열 필요

스택에서 pop하면서 비어있게되면 탐색 종료



재귀 호출 구현

```c++
// 인접 행렬을 이용한 구현 O(V제곱)
void dfs(int x) {  // dfs(x) x에 방문했다를 의미
    check[x] = true;
    printf("%d ",x);
    for (int i=1; i<=n; i++) {
        if (a[x][i] == 1 && check[i] == false) {
            dfs(i);
        }
    }
}

// 인접 리스트를 이용한 구현 O(V+E)
void dfs(int x) {
    check[x] = true;
    printf("%d ",x);
    for (int i=0; i<a[x].size(); i++) {
        int y = a[x][i];
        if (check[y] == false) {
            dfs(y);
        }
    }
}
```



### 너비 우선 탐색 Breadth First Search(BFS)

* 큐를 이용해서 지금 위치에서 갈 수 있는 것을 모두 큐에 넣는 방식
* 큐에 넣을 때 방문했다고 체크해야 한다

```c++
# BFS의 구현은 Queue를 이용해서 할 수 있다.(인접 행렬)
queue<int> q;
check[1] = true; qu.push(1);
while(!q.empty()) {
    int x = q.front(); q.pop();
    printf("%d ", x);
    for (int i=1; i<=n; i++) {
        if (a[x][i]==1 && check[i]==false) {
            check[i] = true;
            q.push(i);
        }
    }
}

# 인접 리스트
queue<int> q;
check[1] = true; q.push(1);
while(!q.empty()) {
    int x = q.front(); q.pop();
    printf("%d ", x);
    for (int i=0; i<=a[x].size(); i++) {
        int y = a[x][i];
        if (check[y] == false) {
            check[y] == true; q.push(y);
        }
    }
}
```

시간 복잡도

* 인접 행렬: O(V제곱)
* 인접 리스트: O(V+E)



### DFS와 BFS

https://www.acmicpc.net/problem/1260

* 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 문제

```python
# 인접 리스트
from collections import deque
n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(n):
    a[i].sort()

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for y in a[x]:
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()
```

```python
# 간선 리스트
from collections import deque
n,m,start = map(int,input().split())
edges = []
check = [False] * (n+1)
for _ in range(m):
    u,v = map(int,input().split())
    edges.append((u,v))
    edges.append((v,u))
m *= 2
edges.sort()
cnt = [0]*(n+1)

for u, v in edges:
    cnt[u] += 1

for i in range(1, n+1):
    cnt[i] += cnt[i-1]

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for i in range(cnt[x-1],cnt[x]):
        y = edges[i][1]
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(cnt[x-1],cnt[x]):
            y = edges[i][1]
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()
```

```python
# 비재귀 구현
from collections import deque
n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(n):
    a[i].sort()

def dfs(node):
    check = [False] * (n+1)
    stack = []
    stack.append((node,0))
    check[node] = True
    print(node, end=' ')
    while stack:
        x,start = stack.pop()
        for i in range(start, len(a[x])):
            y = a[x][i]
            if check[y] == False:
                print(y, end=' ')
                check[y] = True
                stack.append((x,i+1))
                stack.append((y,0))
                break

def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()
```



### 연결 요소 Connected Component

* 연결 그래프가 아닌 경우.. 그래프가 하나 연결요소 2개
* 연결 요소를 구하는 것은 DFS나 BFS(DFS 시작이 두번 => 연결요소 2개) 탐색을 이용해서 구할 수 있다.

```python
import sys
sys.setrecursionlimit(100000)
n,m = map(int,input().split())
a = [[] for _ in range(n)]
check = [False] * (n)
for _ in range(m):
    u,v = map(int,input().split())
    a[u-1].append(v-1)
    a[v-1].append(u-1)

def dfs(x):
    check[x] = True
    for y in a[x]:
        if check[y] == False:
            dfs(y)

ans = 0
for i in range(n):
    if not check[i]:
        dfs(i)
        ans += 1
print(ans)
```



### 이분 그래프 Bipartite Graph

* 그래프를 A와 B로 나눌 수 있음
* A에 포함되어 있는 정점끼리 연결된 간선이 없음
* B에 포함되어 있는 정점끼리 연결된 간선이 없음
* 모든 간선의 한 끝 점은 A에, 다른 끝 점은 B에
* 그래프를 DFS 또는 BFS 탐색으로 이분 그래프인지 아닌지 알아낼 수 있다

DFS로 검사 -> 0: 방문X // 1: 그룹A // 2:그룹B

```python
import sys
sys.setrecursionlimit(1000000)
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    a = [[] for _ in range(n)]
    color = [0] * n
    for _ in range(m):
        u,v = map(int,sys.stdin.readline().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)

    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:
                if not dfs(y, 3-c):
                    return False
            elif color[y] == color[x]:
                return False
        return True

    ans = True
    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                ans = False
    print('YES' if ans else 'NO')
```



# 플러드 필 Flood Fill

* 어떤 위치와 연결된 모든 위치를 찾는 알고리즘



### 단지 번호 붙이기

https://www.acmicpc.net/problem/2667

그래프 문제(인접 행렬/리스트 만들지 않아도 됨. 위/왼쪽/오른쪽/아래 4 방향 알아보면 됨)

* DFS나 BFS 알고리즘을 이용해서 어떻게 이어져있는지 확인 가능
* $d[i][j]$ = (i,j)를 방문안했으면 0, 했으면 단지 번호

```c++
int cnt = 0;
for (int i=0; i<n; i++) {
    for (int j=0; j<n; j++) {
        if (a[i][j]==1 && d[i][j]==0) {
            bfs(i, j, ++cnt);
        }
    }
}
```

```c++
void bfs(int x, int y, int cnt) {
    queue<pair<int, int>> q; q.push(make_pair(x,y)); d[x][y] = cnt;
    while (!q.empty()) {
        x = q.front().first; y = q.front().second; q.pop();
        for (int k=0; k<4; k++) {
            int nx = x+dx[k], ny = y+dy[k];
            if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                if (a[nx][ny] == 1 && d[nx][ny] == 0) {
                    q.push(make_pair(nx,ny)); d[nx][ny]=cnt;
                }
            }
        }
    }
}
```



### 4963번 섬의 개수

* 연결이 대각선까지 8방향. dx, dy 리스트만 확장해주면 됨

```python
from collections import deque
dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
def bfs(x, y, cnt):
    q = deque()
    q.append((x,y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx,ny))
                    group[nx][ny] = cnt
while True:
    m,n = map(int,input().split())
    if n == 0 and m == 0:
        break
    a = [list(map(int,input().split())) for _ in range(n)]
    group = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and group[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)

    print(cnt)
```



### 나이트

dx = [-2, -1, 1, 2, 2, 1, -1, -2]

dy = [1, 2, 2, 1, -1, -2, -2, -1]



