r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
rsum=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
    rsum.append(s)
csum=[]
for i in range(c):
    s=0
    for j in range(r):
        s+=mat[j][i]
    csum.append(s)
s=rsum+csum
print(max(s))