n=int(input())
l=list(map(int,input().split()))
nl=[]
for i in l:
    if i%2 and i not in nl:
        nl.append(i)
sum=0
for i in nl:
    sum+=i
print(sum)