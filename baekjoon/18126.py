#너구리 구구
from collections import deque

N=int(input())
graph=[[] for _ in range(N + 1)]
visited=[False]*(N+1)

for n in range(N-1):
    a,b,c=map(int,input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
def bfs(graph):
    queue = deque([(1, 0)])
    visited[1] = True
    max_distance = 0  

    while queue:
        now,c = queue.popleft()
        max_distance = max(max_distance, c)

        for next, dist in graph[now]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, c+dist))

    return max_distance

print(bfs(graph))