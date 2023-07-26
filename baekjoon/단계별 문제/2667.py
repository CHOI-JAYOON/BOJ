from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
graph=[]
answer=[]
visited=[[False]*(N+1) for _ in range(N+1)]

for i in range(N):
    graph.append(list(map(int,input().strip())))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1] #상하좌우
count=0

def bfs(x,y):
    global cnt
    queue=deque()
    queue.append((x,y))
    # visited[x][y]=True
    cnt=0
    while queue:
        x,y=queue.popleft()
        if graph[x][y]==1:
            graph[x][y]=0
            cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=N or nx<0 or ny>=N or ny<0:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1 :
                cnt+=1
                graph[nx][ny]=0
                # print(nx,ny)
                # visited[nx][ny]=True
                queue.append((nx,ny))
    return cnt
    
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            # print(i,j)
            answer.append(bfs(i,j))
            count+=1
print(count)            
answer.sort()
for ans in answer:
    print(ans)