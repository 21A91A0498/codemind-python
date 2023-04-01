n=int(input())
l=list(map(int,input().split()))
sum=0
s=0
for i in range(len(l)):
    if i%2:
        sum+=l[i]
    else:
        s+=l[i]
if (sum-s)==0:
    print('YES')
else:
    print('NO')