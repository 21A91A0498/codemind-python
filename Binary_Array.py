n=int(input())
m=list(map(int,input().split()))
c=0
k=0
for i in m:
    c+=1
    if i==0 or i==1:
        k+=1
if c==k:
    print(True)
else:
    print(False)
    