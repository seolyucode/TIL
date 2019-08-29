'''
Priority Queue는 높은 우선순위를 가진 원소는 낮은 우선순위를 가진 원소보다 먼저 처리되는 자료구조이다.
주어진 N(2<= N <=100)개의 수를 작은 숫자가 높은 우선순위를 갖는 Priority Queue에 저장하고,
우선 순위가 높은 숫자부터 차례대로 출력하시오. (입력에는 오류가 없다고 가정)
'''

MAX_SIZE = 100
heapSize = 0
heap = list()


def heapInit():
    global heapSize, heap
    heap.clear()
    for i in range(MAX_SIZE):
        heap.append(0)


def heapPush(value):
    global heapSize, heap
    if heapSize + 1 > MAX_SIZE:
        return
    heap[heapSize] = value

    current = heapSize
    while current > 0 and heap[current] < heap[(current - 1) // 2]:
        heap[(current - 1) // 2], heap[current] = heap[current], heap[(current - 1) // 2]
        current = (current - 1) // 2

    heapSize = heapSize + 1


def heapPop():
    global heapSize, heap

    if heapSize <= 0:
        return -1

    value = heap[0]
    heapSize = heapSize - 1

    heap[0] = heap[heapSize]

    current = 0
    while current < heapSize and current * 2 + 1 < heapSize:
        child = 0
        if current * 2 + 2 >= heapSize:
            child = current * 2 + 1
        else:
            if heap[current * 2 + 1] < heap[current * 2 + 2]:
                child = current * 2 + 1
            else:
                child = current * 2 + 2

        if heap[current] < heap[child]:
            break

        heap[current], heap[child] = heap[child], heap[current]
        current = child

    return value


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        heapInit()

        value = list(map(int, input().split()))

        for i in range(N):
            heapPush(value[i])

        print("#%d" % test_case, end=' ')
        for i in range(N):
            print(heapPop(), end=' ')
        print()


if __name__ == "__main__":
    main()

'''
2 //테스트 케이스 수 
10 //입력 수 
10 49 38 17 56 92 8 1 13 55 //입력 데이터 
13 
4 22 50 13 5 1 22 35 21 7 99 100 14
'''

'''
#1 1 8 10 13 17 38 49 55 56 92 
#2 1 4 5 7 13 14 21 22 22 35 50 99 100
'''