import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start, end, maze, N, M):
    queue = deque([start])
    visited = [[0]*(M+1) for _ in range(N+1)]  
    visited[start[0]][start[1]] = 1 

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return visited[x][y]
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= N and 1 <= ny <= M and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

INF = float("inf")

# 입력
N, M = map(int, input().split())
maze = [[0]*(M+1)]  
for _ in range(N):
    row = list(map(int, input().strip()))
    maze.append([0] + row)  # 1-based dummy column

print(bfs((1,1), (N,M), maze, N, M))