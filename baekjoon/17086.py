#아기 상어2
from collections import deque
N,M=map(int,input().split())
graph=[]*(N)
for i in range(N):
    graph.append(list(map(int,input().split())))
#0은 빈칸 1은 아기상어 뚜루
count=0
# 방향 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]

