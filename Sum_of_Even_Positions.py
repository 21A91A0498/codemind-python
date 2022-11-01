n=int(input())
lst=list(map(int,input().split()))[:n]
sum=0
for i in range(len(lst)):
    if i%2==0:
        sum+=lst[i]
print(sum)