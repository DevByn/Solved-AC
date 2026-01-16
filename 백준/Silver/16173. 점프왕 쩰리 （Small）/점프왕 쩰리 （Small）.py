import sys
input = sys.stdin.readline

def dfs(start,N,board):
    stack = [start]

    while stack:
        x,y = stack.pop()

        if(board[x][y] == -1):
            return 'HaruHaru'

        if board[x][y] == 0:  # 이동 불가
            continue

        if(x + board[x][y] < N):
             stack.append((x+board[x][y],y))

        if(y + board[x][y] < N):
            stack.append((x,y+board[x][y]))

    return 'Hing'


N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]
print(dfs((0,0),N,board))
