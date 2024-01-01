import sys
input=sys.stdin.readline

n=int(input())  #전체 사람 수
a,b=map(int,input().split()) # 촌수를 계산해야 하는 두 사람
m=int(input()) # 부모 자식들 간의 관계 개수

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    x,y=map(int,input().split()) #x: 부모, y: 자식
    graph[x].append(y)
    graph[y].append(x)

result=[]
cnt=0

def dfs(me, cnt):
    # global cnt
    cnt +=1 # 촌수 계산
    visited[me]=True
    
    if me==b:
        result.append(cnt) 
        
    for i in graph[me]:
        if not visited[i]:
            dfs(i,cnt)
            

dfs(a,cnt)

if len(result)==0:
    print(-1)
else:
    print(result[0]-1)

#틀린 코드
# import sys
# input=sys.stdin.readline

# n=int(input())  #전체 사람 수
# a,b=map(int,input().split()) # 촌수를 계산해야 하는 두 사람
# m=int(input()) # 부모 자식들 간의 관계 개수

# graph=[[] for _ in range(n+1)]
# visited=[False]*(n+1)

# for _ in range(m):
#     x,y=map(int,input().split()) #x: 부모, y: 자식
#     graph[x].append(y)
#     graph[y].append(x)

# result=[]
# cnt=0

# def dfs(graph, me, visited):
#     global cnt
#     cnt +=1 # 촌수 계산
#     visited[me]=True
    
#     if me==b:
#         result.append(cnt) 
        
#     for i in graph[me]:
#         if not visited[i]:
#             dfs(graph, i,visited)
            

# dfs(graph, a,visited)

# if len(result)==0:
#     print(-1)
# else:
#     print(result[0]-1)


# cnt를 파라미터로 주지 않고, global로 사용했을 때
# cnt값은 1,2,3,4,5,6
# cnt를 파라미터로 줄 경우
# cnt값은 1,2,3,4,3,3