x=int(input())
line=0
end=0
while x>end:
    line+=1
    end+=line
a=end-x
if line%2==0:
    top=line-a
    bot=a+1
else:
    top=a+1
    bot=line-a

print("{0}/{1}".format(top,bot))


