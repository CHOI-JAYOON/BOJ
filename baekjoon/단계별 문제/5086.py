while True:
    a, b = map(int, input().split())
    
    if (a==0&b==0):
        break
    elif (a % b == 0 ):
        print("multiple")
        continue
    elif (b % a == 0):
        print("factor")
        continue
    else:
        print("neither")
        continue
    
    