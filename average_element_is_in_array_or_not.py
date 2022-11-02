n=int(input())
count=0
sum=0
lst=list(map(int,input().split()))[:n]
for i in lst:
    sum+=i
k=sum//len(lst)
for i in lst:
    if k==i:
        count+=1
if count>0:
    print(True)
else:
    print(False)