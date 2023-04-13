sum=0
sumnum=0
for _ in range(20):
    subject, num, score = map(str, input().split())
    if(score=="A+"):
        sum+=float(num)*4.5
        sumnum+=float(num)
    elif(score=="A0"):
        sum+=float(num)*4.0
        sumnum+=float(num)
    elif(score=="B+"):
        sum+=float(num)*3.5
        sumnum+=float(num)
    elif(score=="B0"):
        sum+=float(num)*3.0
        sumnum+=float(num)
    elif(score=="C+"):
        sum+=float(num)*2.5
        sumnum+=float(num)
    elif(score=="C0"):
        sum+=float(num)*2.0
        sumnum+=float(num)
    elif(score=="D+"):
        sum+=float(num)*1.5
        sumnum+=float(num)
    elif(score=="D0"):
        sum+=float(num)*1.0
        sumnum+=float(num)
    elif(score=="F"):
        sum+=float(num)*0
        sumnum+=float(num)
    else:
        continue

print(sum/sumnum)
 