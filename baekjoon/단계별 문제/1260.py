from collections import deque

N,M,V=map(int,input().split())

graph=[[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
    
visited1=[False]*(N+1)
visited2=[False]*(N+1)


def dfs(V):
    visited1[V]=True
    print(V, end=" ")
    for i in graph[V]:
        if  not  visited1[i]:
            dfs(i)

def bfs(V):
    q=deque([V])
    visited2[V]=True
    
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited2[i]:
                q.append(i)
                visited2[i]=True
                
dfs(V)
print()
bfs(V)
