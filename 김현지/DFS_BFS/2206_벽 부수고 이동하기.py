from collections import deque

def bfs(x, y, wall):  # wall = 1 : 벽 부수기 가능, 0 : 불가능
    # enQ + visited 설정
    Q = deque()
    Q.append((x, y, wall))
    visited[x][y][wall] = 1

    # Q가 비어있지 않은 동안
    while Q:
        # v = deQ
        x, y, wall = Q.popleft()
        # 하고싶은 일 하기
        if x == N-1 and y == M-1:
            return visited[x][y][wall]

        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이면서 벽 부수기 가능할 때
                if arr[nx][ny] == 1 and wall == 1:
                    Q.append((nx, ny, 0))
                    visited[nx][ny][0] = visited[x][y][1] + 1
                # 벽이 아니면서 방문하지 않은 곳일 때
                elif arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    Q.append((nx, ny, wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1

    return -1





dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 1))
# print(visited)