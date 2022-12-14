n=int(input())
m=n+1
i=1
a=0
b=1
k=[]
while i<=m:
    c=a+b
    k.append(a)
    a=b
    b=c
    i+=1
c=0
for j in k:
    if j==n:
        c+=1
if c>0:
    print(True)
else:
    print(False)
    
    
    