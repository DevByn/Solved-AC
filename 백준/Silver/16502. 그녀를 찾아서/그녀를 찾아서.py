import sys
input = sys.stdin.readline

idx = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3
}

T = int(input())
M = int(input())

graph = [[] for _ in range(4)]

for _ in range(M):
    s, e, p = input().split()
    s = idx[s]
    e = idx[e]
    p = float(p)

    graph[s].append((e, p))

DP = [[0 for _ in range(4)] for _ in range(T+1)]
DP[0] = [0.25, 0.25, 0.25, 0.25]

for t in range(T):
    for u in range(4):
        for v, p in graph[u]:
            DP[t+1][v] += DP[t][u] * p

for _ in DP[T]:
    print(_ * 100)