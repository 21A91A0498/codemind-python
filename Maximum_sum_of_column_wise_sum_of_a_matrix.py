r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
csum=[]
for i in range(c):
    s=0
    for j in range(r):
        s+=mat[j][i]
    csum.append(s)
print(max(csum))