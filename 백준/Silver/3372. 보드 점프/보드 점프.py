import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
board = []
idx = 1
for i in range(N):
    board.append(list(map(int, data[idx:idx+N])))
    idx += N


dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        jump = board[i][j]
       
        if dp[i][j] == 0 or (i == N-1 and j == N-1):
            continue
            
        if i + jump < N:
            dp[i + jump][j] += dp[i][j]

        if j + jump < N:
            dp[i][j + jump] += dp[i][j]

print(dp[N-1][N-1])