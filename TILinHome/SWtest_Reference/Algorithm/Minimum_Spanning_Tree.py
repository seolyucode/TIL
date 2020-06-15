'''
최소비용 신장트리(minimum spanning tree)는 네트워크(가중치가 간선에 할당된 그래프)에 있는 모든 정점들을 가장 적은 비용으로 연결하는 트리를 말한다.
주어진 weighted graph에 대해 Minimum Spanning Tree를 구하고, 연결된 모든 Edge의 weight 합을 출력하시오.
첫째 줄에는 테스트 케이스의 수 T 및 Vertex의 개수 V가 들어온다.
두 번째 줄부터는 V x V개의 숫자가 들어오며, 이는 edge[i][j]의 weight를 나타내는 숫자이다 (단, V는 100을 넘지 않는다고 가정한다)
'''

def minKey(key, mstSet):
    min = 2147483647
    for v in range(0, V):
        if (mstSet[v] == 0) and (key[v] < min):
            min = key[v]
            min_index = v
    return min_index


def printMST(parent):
    weightSum = 0
    for i in range(1, V):
        weightSum += graph[i][parent[i]]
    print(weightSum)


def primMST():
    parent = [0] * 100
    key = [2147483647] * 100
    mstSet = [0] * 100
    key[0] = 0
    parent[0] = -1
    for count in range(0, V - 1):
        u = minKey(key, mstSet)
        mstSet[u] = 1
        for v in range(0, V):
            if graph[u][v] and (mstSet[v] == 0) and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]
    printMST(parent)


def main():
    global graph, V
    T, V = map(int, input().split())
    for test_case in range(1, T + 1):
        graph = [[int(x) for x in input().split()] for y in range(V)]
        print("#%d" % test_case, end=' ')
        primMST()


if __name__ == "__main__":
    main()

'''
1 5 // T - test case, V - Vertex 개수 
0 2 0 6 0 
2 0 3 8 5 
0 3 0 0 7 
6 8 0 0 9 
0 5 7 9 0
'''

'''
#1 16
'''