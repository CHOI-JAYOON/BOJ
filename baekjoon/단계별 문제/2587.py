a=[]
for _ in range(5):
    a.append(int(input()))
sum=0
for i in range(5):
    sum+=a[i]
a.sort()
print(int(sum/5))
print(a[2])