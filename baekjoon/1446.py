#세준이는 0에서 시작 D까지 가야한다.
#노드로 보았을때 최소거리는 1로 초기화
#이후 지름길 정보가 들어오면 graph에 정보 추가
#지름길 정보에서 지름길 끝나는 지점이 목표지점 D보다 크면 정보추가X(뒤돌아갈수 없으므로)
import heapq
import sys
input=sys.stdin.readline
n, d=map(int,input().split()) #지름길 개수, 고속도로의 길이

graph=[[] for _ in range(d+1)]
INF= 1e8
visited=[False]*(d+1)
distance=[INF]*(d+1)

for i in range(d):
    graph[i].append((i+1,1))
    
for i in range(n):
    a,b,c=map(int, input().split()) # 지름길 시작 위치, 도착위치, 지름길의 길이
    if b > d:
        continue
    graph[a].append((b, c))
# print(graph)

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
                
dijkstra(0)
print(distance[d])

#다익스트라 알고리즘보다는 문제 이해가 어려웠다.