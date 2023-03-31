n=int(input())
l=list(map(int,input().split()))
sum=0
s=0
for i in range(0,len(l)//2):
    sum=sum+l[i]
for j in range(len(l)//2,len(l)):
    s=s+l[j]
dif=abs(sum-s)
if dif%4:
    print('Y')
else:
    print('X')