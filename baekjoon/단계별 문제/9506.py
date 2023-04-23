while True:
    n = int(input())
    a=[]
    sum=0
    if n == -1 :
        break
    for i in range(1, n):
        if(n%i==0):
            a.append(i)
            sum += i
      
    if( sum != n):
        print(n, "is NOT perfect.")        
    else:
        print(n, '=', end=' ')
        for i in a:
            print(i, end=' ')
            if(a.index(i)!=len(a)-1):
                print('+', end=' ')