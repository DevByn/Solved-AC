import sys
input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))
DP = [1 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(i-1,0,-1):
        if(DP[j] + 1 > DP[i] and arr[j] < arr[i]):
            DP[i] = DP[j] + 1

print(max(DP))