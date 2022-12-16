n=int(input())
m=list(map(int,input().split()))
k=[]
for i in m:
    k.insert(0,i)
sum=0
for j in range(len(k)):
    sum=sum+(k[j]*(2**j))
print(sum)