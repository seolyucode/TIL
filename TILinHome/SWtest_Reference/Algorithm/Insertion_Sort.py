'''
삽입 정렬은 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여,
자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘이다.
주어진 데이터를 Insertion Sort를 사용하여 정렬 하시오. 데이터의 최대 크기는 100이다.
'''

arr = []
num = 0


def insertionSort():
    global arr
    for i in range(1, num):
        temp = arr[i]
        j = i - 1

        while temp < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp


def printResult():
    for i in range(0, num):
        print(arr[i], end=' ')


def main():
    global arr, num
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        arr = [int(x) for x in input().split()]

        insertionSort()
        print("#%d" % test_case, end=' ')
        printResult()


if __name__ == "__main__":
    main()

'''
1 // 전체 Test case 수
5 // 데이터 크기 
1 4 5 2 3
'''

'''
#1 1 2 3 4 5
'''