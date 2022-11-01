n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in lst:
    if i%2:
        sum+=i
print(sum)
        