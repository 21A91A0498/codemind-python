def elesum(i):
    n=str(i)
    sum=0
    for i in n:
        k=int(i)
        sum+=k
    return sum
n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    if i in range(1,10):
        sum+=i
    else:
        k=elesum(i)
        sum+=k
print(sum)

