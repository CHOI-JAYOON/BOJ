a, b, c, d, e, f = map(int,input().split())

x=((c*e)-(f*b))/((a*e)-(b*d))
y=((c*d)-(f*a))/((b*d)-(a*e))
x=int(x)
y=int(y)

print(x, y)