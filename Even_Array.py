n=int(input())
m=list(map(int,input().split()))
k=0
c=0
for i in m:
    k+=1
    if i%2==0:
        c+=1
if k==c:
    print(True)
else:
    print(False)