'''
너비 우선 탐색은 맹목적 탐색방법의 하나로 시작 정점을 방문한 후 시작 정점에 인접한 모든 정점들을 우선 방문하는 방법이다.
위와 같은 그래프에서 숫자가 있는 원은 정점(Vertex)라고 하고, 정점과 정점을 잇는 연결선을 간선(Edge)이라고 한다. 정점의 최대 개수는 30개이다.
정점과 정점의 연결관계가 인접행렬로 주어졌을 때, BFS를 이용하여 시작 정점으로부터 모든 정점을 탐색한 결과를 순서대로 화면에 출력하시오.
* graph.png 참고
'''

class Queue:
    class Point:
        def __init__(self, y, x, c):
            self.y = y
            self.x = x
            self.c = c

    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head = self.rear = 0

    def isEmpty(self):
        return self.head <= self.rear

    def enQueue(self, y, x, c):
        self.queue[self.head] = self.Point(y, x, c)
        self.head = self.head + 1

    def deQueue(self):
        if self.isEmpty():
            return None
        self.rear = self.rear + 1
        return self.queue[self.rear - 1]


def breadthFirstSearch():
    queue = Queue(row * column)
    queue.enQueue(0, 0, 0)
    MAP[0][0] = 0

    while queue.isEmpty() == False:
        p = queue.deQueue()

        if p.y == row - 1 and p.x == column - 1:
            return p.c

        if p.y + 1 < row and MAP[p.y + 1][p.x]:
            queue.enQueue(p.y + 1, p.x, p.c + 1)
            MAP[p.y + 1][p.x] = 0
        if p.x + 1 < column and MAP[p.y][p.x + 1]:
            queue.enQueue(p.y, p.x + 1, p.c + 1)
            MAP[p.y][p.x + 1] = 0
        if p.y - 1 >= 0 and MAP[p.y - 1][p.x] != 0:
            queue.enQueue(p.y - 1, p.x, p.c + 1)
            MAP[p.y - 1][p.x] = 0
        if p.x - 1 > 0 and MAP[p.y][p.x - 1] != 0:
            queue.enQueue(p.y, p.x - 1, p.c + 1)
            MAP[p.y][p.x - 1] = 0

    return -1


def main():
    global MAP, row, column
    T = int(input())

    for test_case in range(1, T + 1):
        row, column = map(int, input().split())
        MAP = [[int(num) for num in input().split()] for _ in range(row)]
        print("#%d %d" % (test_case, breadthFirstSearch()))


if __name__ == "__main__":
    main()

'''
1 //test case 개수 
8 1 // 정점의 개수, 시작 정점 
1 2 // 정점 간 연결 관계. 1과 2가 연결 
1 3 
2 4 
2 5 
4 8 
5 8 
3 6 
3 7 
6 8 
7 8 
-1 -1 // 입력 끝 
'''

'''
#1 1 2 3 4 5 6 7 8 // 방문한 정점 순서
'''