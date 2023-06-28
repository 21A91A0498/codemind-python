r,c=map(int,input().split())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
rsum=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
    rsum.append(s)
print(max(rsum))