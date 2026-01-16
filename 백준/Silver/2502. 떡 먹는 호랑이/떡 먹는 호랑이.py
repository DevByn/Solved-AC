
D ,K = map(int,input().split())

dp = [(0,0)] * (D+1)

dp[1] = (1,0)
dp[2] = (0,1)

for i in range(3,D+1):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

A = 0

for i in range(1,100001):
    if((K - (dp[D][0] * i)) % dp[D][1] == 0):
        A = i
        break
    
B = (K - (A * dp[D][0])) // dp[D][1]

print(A)
print(B)