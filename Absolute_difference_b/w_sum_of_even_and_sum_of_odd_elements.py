n=int(input())
ml=list(map(int,input().split()))[0:n]
sum=0
s=0
for i in ml:
    if i%2==0:
        sum+=i
    if i%2:
        s+=i
k=abs(sum-s)
print(k)