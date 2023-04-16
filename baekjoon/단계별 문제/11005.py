N, B = map(int,input().split())

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
while(1):
    result += number[N%B]
    # num=number.find(str(N%B))
    # result += str(num)
    # result += str(N%B)
    N=N//B
    if(N<=0):
        break
    
result=''.join(reversed(result))
print(result)

