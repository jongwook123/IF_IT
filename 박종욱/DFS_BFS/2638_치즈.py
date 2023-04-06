from collections import deque

def bfs1():
    Q = deque()
    visited1 = [[False]*M for _ in range(N)]
    Q.append((0,0))
    visited1[0][0] = True
    arr[0][0] = -1
    while Q:
        i,j = Q.popleft()
        for s in range(4):
            ni = i + di[s]
            nj = j + dj[s]
            if 0 > ni or ni >= N or 0 > nj or nj >= M: continue
            if arr[ni][nj] == 1 or visited1[ni][nj]: continue
            Q.append((ni,nj))
            arr[ni][nj] = -1
            visited1[ni][nj] = True
    return

def cheese():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return False
    return True

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt_ = 0

while not cheese():
    bfs1()
    check = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                cnt = 0
                for s in range(4):
                    ni = i + di[s]
                    nj = j + dj[s]
                    if 0 > ni or ni > N or 0 > nj or nj >= M: continue
                    if arr[ni][nj] == -1:
                        cnt += 1
                if cnt >= 2:
                    check.append((i,j))
    for i,j in check:
        arr[i][j] = 0
    cnt_ += 1

print(cnt_)

