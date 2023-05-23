n=int(input())
l=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(k):
    sum+=l[i]
print(sum)