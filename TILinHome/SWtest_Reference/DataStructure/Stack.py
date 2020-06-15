'''
Stack
Queue
Priority Queue
Hash
Tree
Graph
Linked List
Deque
Map
Set
'''

'''
Stack은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조(LIFO - Last In First Out)로 데이터를 저장하는 형식을 말한다.
주어진 N(2<= N <=100)개의 수를 순서대로 Stack에 넣은 후 하나씩 꺼내 화면에 출력하시오.
'''

stack = []


def stackInit():
    global stack
    stack.clear()


def stackIsEmpty():
    global stack
    return len(stack) == 0


def stackPush(value):
    stack.append(value)


def stackPop():
    return stack.pop()


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        stackInit()

        l = list(input().split())

        for i in l:
            stackPush(i)

        print("#%d" % test_case, end=' ')

        while not stackIsEmpty():
            value = stackPop()
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
#1 5 4 3 2 1 
#2 1 3 2 4 5
'''