from collections import deque
T=int(input())

def bfs(x,y):
    global cnt
    queue=deque()
    queue.append((x,y))
    cnt=0
    
    # visited[x][y]=True
    while queue:
        x,y=queue.popleft()
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=N or ny>=M or nx<0 or ny<0:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
    return cnt
    
for t in range(T):
    count=0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    M,N,K=map(int,input().split()) #가로, 세로, 배추 위치 개수
    graph=[[0]*(M+1) for _ in range(N+1)]
    
    for k in range(K):
        x,y=map(int,input().split())
        graph[y][x]=1 #x가로 y세로
     
    for i in range(N+1): #i 세로 j 가로
        for j in range(M+1):
            if graph[i][j]==1:
                # print(bfs(i,j))
                bfs(i,j)
                count+=1
         
    print(count)