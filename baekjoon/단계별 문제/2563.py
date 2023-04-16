a = int(input())
paper = [[0]*100 for i in range(100)]
for _ in range(a):
    x, y = list(map(int,input().split()))
   
    for row in range(x, x+10):
        for col in range(y, y+10):
            paper[row][col]=1
    
result=0

for i in paper:
    result += i.count(1)
print(result)

