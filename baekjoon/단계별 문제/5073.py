
while True:
    a=list(map(int,input().split()))
    if (a[0]==a[1]==a[2]==0):
        break
    
    if (a[0]==a[1]==a[2]):
        print("Equilateral")
        a.clear
    else :
        maxx=max(a)
        a.remove(maxx)
        if (maxx<a[0]+a[1]):
            if(a[0]==a[1] or maxx==a[0] or maxx== a[1]):
                print("Isosceles")
                a.clear
            else:
                print("Scalene")
                a.clear
        else:
            print("Invalid")
            a.clear
            

    