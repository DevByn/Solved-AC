import sys
input = sys.stdin.readline

DP = [0 for _ in range(1000001)]
DP[1] = 1
DP[2] = 2
DP[3] = 4
for i in range(4,1000001):
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % 1000000009

T = int(input())

for _ in range(T):
    n = int(input())
    print(DP[n])