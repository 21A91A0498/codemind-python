n=int(input())
l=list(map(int,input().split()))
nl=[]
for i in l:
    if i%2==0 and i not in nl:
        nl.append(i)
print(len(nl))