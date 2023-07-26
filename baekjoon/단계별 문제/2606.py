computer=int(input())
pair=int(input())

graph=[[]*(computer+1) for _ in range(computer+1)]
visited=[False]*(computer+1)

for i in range(pair):
    a, b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    return visited

print(sum(dfs(1))-1)
    
    