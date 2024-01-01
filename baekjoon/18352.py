from collections import deque

import sys
input=sys.stdin.readline

N,M,K,X=map(int,input().split()) #도시개수, 도로 개수, 거리정보, 출발 도시번호

graph=[[] for _ in range(N+1)]
dist=[0]*(N+1)
visited=[False]*(N+1)

for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    
def bfs(X):
    answer=[]
    q=deque([X])
    visited[X]=True
    dist[X]=0
    
    while q:
        x=q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                dist[i]=dist[x]+1
                if dist[i]==K:
                    answer.append(i)
                    
    if len(answer)==0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')
            
bfs(X)