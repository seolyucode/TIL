'''
퀵 정렬은 기준키(pivot)를 기준으로 작거나 같은 값을 지닌 데이터는 앞으로,
큰 값을 지닌 데이터는 뒤로 가도록 하여 작은 값을 갖는 데이터와 큰 값을 갖는 데이터로 분리해가며 정렬하는 방법이다.
주어진 데이터를 Quick Sort를 사용하여 정렬 하시오. 데이터의 최대 크기는 100이다.
'''

arr = []
num = 0


def quick_sort(first, last):
    if first < last:
        pivot = first
        i = first
        j = last

        while i < j:
            while arr[i] <= arr[pivot] and i < last:
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]

        quick_sort(first, j - 1)
        quick_sort(j + 1, last)


def main():
    global arr, num
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        arr = [int(x) for x in input().split()]

        quick_sort(0, num - 1)
        print("#%d" % test_case, end=' ')
        for j in range(0, num):
            print(arr[j], end=' ')
        print()


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