n=int(input())
c=0
l=n//2
for i in range(0,l+1):
    p=i*i
    for j in range(0,l+1):
        k=j*j
        m=p+k
        if n==m:
            c+=1
if c>0 :
    print(True)
else:
    print(False)
