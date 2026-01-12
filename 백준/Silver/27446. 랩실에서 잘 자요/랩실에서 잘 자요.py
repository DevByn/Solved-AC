import sys
input = sys.stdin.readline

n, m = map(int,input().split())

page = list(map(int, input().split()))

missing_numbers = []

for i in range(1, n + 1):
    if i not in page:
        missing_numbers.append(i)

if not missing_numbers:
    print(0)
else:
    missing_numbers.sort()    
    DP = [0 for _ in range(len(missing_numbers))]
    DP[0] = 7
    for i in range(1,len(missing_numbers)):
        DP[i] = min(DP[i-1] + 7, DP[i-1] + (missing_numbers[i] - missing_numbers[i-1]) * 2)
    print(DP[len(missing_numbers)-1])