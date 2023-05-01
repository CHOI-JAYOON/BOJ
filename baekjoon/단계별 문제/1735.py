#유클리드 호제, 최대공약수
def gcd(x, y):
    mod=x%y
    while mod>0:
        x=y
        y=mod
        mod=x%y
    return y

A, B = map(int,input().split())
C, D = map(int,input().split())
N=gcd((A*D)+(B*C),(B*D) )
    
print(((A*D)+(B*C))//N,(B*D)//N )
