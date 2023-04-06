import sys
from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs(i,j,k):

    Q = deque()
    Q.append([i,j,k])
    visited[i][j][k] = 1
    while Q:
        i,j,k = Q.popleft()
        if i == N-1 and j  == M -1:
            return visited[i][j][k]
        for s in range(4):
            ni = i +di[s]
            nj = j +dj[s]
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj][k]:
                    if arr[ni][nj] == 0:
                        visited[ni][nj][k] = visited[i][j][k] + 1
                        Q.append([ni,nj,k])
                    if arr[ni][nj] == 1 and k == 1:
                        visited[ni][nj][k-1] = visited[i][j][k] + 1
                        Q.append([ni, nj,k-1])
    return -1





N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

print(bfs(0,0,1))
