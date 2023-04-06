'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''

from collections import deque


def bfs(x, y):
    cheese = []
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        i, j = Q.popleft()
        for k in dir:
            ni, nj = i + k[0], j + k[1]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if arr[ni][nj] >= 1:
                    arr[ni][nj] += 1
                else:
                    Q.append((ni, nj))
                    visited[ni][nj] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 3:
                cheese.append((i, j))  # 녹일 치즈 리스트
            elif arr[i][j] > 0:
                arr[i][j] = 1
    return cheese


dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
cheese = []
cnt = 0

while True:
    ch = bfs(0, 0)
    if len(ch) == 0:
        break
    for i, j in ch:
        arr[i][j] = 0
    cnt += 1

print(cnt)



