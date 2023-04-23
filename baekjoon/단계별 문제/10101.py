a=[]
for _ in range(3):
    a.append(int(input()))
 
sum=0   
for i in range(3):
    sum += a[i]

if (a[0]==a[1]==a[2]==60):
    print("Equilateral")
    
elif (sum==180):
    if( a[0]==a[1] or a[1]==a[2] or a[0]==a[2]):
        print("Isosceles")
    elif (a[0]!=a[1]!=a[2]):
        print("Scalene")
elif (sum!=180):
    print("Error")