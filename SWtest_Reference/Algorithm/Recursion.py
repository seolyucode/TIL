'''
Recursion
Insertion Sort
Quick Sort
Counting Sort
Binary Search
DFS Searching
BFS Searching
Parametric Search
Dynamic Programming
Permutation & Combination
DFS Algorithm
BFS Algorithm
Dijkstra
Floyd Warshall
Plane Sweeping
Minimum Spanning Tree
Topological Sort
Maximum Flow
Bipartite Match

재귀는 수학이나 컴퓨터 과학 등에서 자신을 정의할 때 자기 자신을 재참조하는 방법을 뜻한다.
주로 이 방법은 함수에 적용한 재귀 함수(Recursion Function)의 형태로 많이 사용된다.
주어진 수의 Factorial 값을 구해 아래와 같이 출력하시오. 주어지는 수는 1 이상 20 이하의 수이다.
'''

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        value = factorial(num)
        print("#%d %d! = %d" % (test_case, num, value))


if __name__ == "__main__":
    main()

'''
3 // 전체 Test case 수 
9 // Test case index 
12 
20
'''

'''
#1 9! = 362880
#2 12! = 479001600 
#3 20! = 2432902008176640000
'''