#데스나이트
from collections import deque

N=int(input())
r1, c1, r2, c2=map(int,input().split()) # y, x
graph=[[-1]*(N) for _ in range(N)]
#처음에는 0으로 초기화 했다가
#이동할수없는 경우에는 -1을 출력해줘야하기 때문에
#-1로 초기화해줌
move=[(-2,-1),(-2,1), (0,-2),(0,2),(2,-1),(2,1)] #얘가 중요

def bfs(y,x):
    queue=deque()
    queue.append((y,x))
    graph[y][x]=0
    while queue:
        y,x=queue.popleft()
        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N and graph[ny][nx]==-1:
                queue.append((ny,nx))
                graph[ny][nx]=graph[y][x]+1
            else:
                continue
bfs(r1,c1)

print(graph[r2][c2]) #이동횟수 출력