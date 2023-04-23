N=int(input())
maxx=-10001
maxy=-10001
minx=10001
miny=10001
for _ in range(N):
    x, y = map(int, input().split())
    if (maxx<=x):
        maxx=x
    if(maxy<=y):
        maxy=y
    if(minx>=x):
        minx=x
    if(miny>=y):
        miny=y
    else:
        continue
print((maxx-minx)*(maxy-miny))