'''
Queue는 컴퓨터의 기본적인 자료 구조의 한가지로, 먼저 집어 넣은 데이터가 먼저 나오는 FIFO (First In First Out)구조로 저장하는 형식을 말한다.
주어진 N(2<= N <=100)개의 수를 순서대로 Queue에 넣은 후 하나씩 꺼내 화면에 출력하시오.
'''

queue = []


def queueInit():
    global queue
    queue.clear()


def queueIsEmpty():
    global queue
    return len(queue) == 0


def queueEnqueue(value):
    queue.append(value)


def queueDequeue():
    return queue.pop(0)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        queueInit()
        l = list(input().split())

        for i in l:
            queueEnqueue(i)

        print("#%d" % test_case, end=' ')

        while not queueIsEmpty():
            value = queueDequeue()
            if value != None:
                print(value, end=' ')

        print()


if __name__ == "__main__":
    main()

'''
2 // 테스트 케이스 수 
5 // 데이터 크기 
1 2 3 4 5 
5 
5 4 2 3 1
'''

'''
#1 1 2 3 4 5 
#2 5 4 2 3 1
'''