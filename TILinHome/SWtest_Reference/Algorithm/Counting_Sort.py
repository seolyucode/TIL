'''
계수정렬(counting sort)는 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하면서 정렬하는 알고리즘이다.
주어진 정수들을 Counting Sort를 이용하여 정렬하고 오름차순으로 출력하라. (주어진 정수들은 중복가능)
'''

MAX_N = 100
MAX_DIGIT = 10

N = 0
arr = []
cnt = []
sortedArr = []


def calculateDigitNumber():
    global cnt
    for i in range(N):
        cnt[arr[i]] += 1

    for i in range(1, MAX_DIGIT + 1):
        cnt[i] = cnt[i - 1] + cnt[i]


def executeCountingSort():
    global cnt, sortedArr
    for i in range(N - 1, -1, -1):
        sortedArr[cnt[arr[i]] - 1] = arr[i]
        cnt[arr[i]] = cnt[arr[i]] - 1


def main():
    global N, arr, cnt, sortedArr
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        arr = [int(x) for x in input().split()]
        sortedArr = [int(0)] * N
        cnt = [int(0)] * 11

        calculateDigitNumber()
        executeCountingSort()

        print("#%d" % test_case, end=' ')
        for i in range(N):
            print("%d" % sortedArr[i], end=' ')

        print()


if __name__ == "__main__":
    main()

'''
2 // # of test case 
10 // # of data set 
0 2 9 4 5 1 0 7 3 9 
5 
4 9 5 1 3
'''

'''
#1 0 0 1 2 3 4 5 7 9 9 
#2 1 3 4 5 9
'''