n=int(input())
l=list(map(int,input().split()))
nl=[]
c=0
for i in l:
    if i%2==0 and i not in nl:
        c+=1
        nl.append(i)
print(c)