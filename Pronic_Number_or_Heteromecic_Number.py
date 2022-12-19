n=int(input())
a=n//2
c=0
for i in range(1,a+1):
    if (i-1)*(i)==n or (i)*(i+1)==n:
        c+=1
        break
if c>0:
    print("YES")
else:
    print("NO")