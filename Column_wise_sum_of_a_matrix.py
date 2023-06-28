r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
csum=[]
for j in range(c):
    s=0
    for i in range(r):
        s+=mat[i][j]
    csum.append(s)
print(*csum)