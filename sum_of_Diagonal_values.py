r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
s=0
for i in range(r):
    for j in range(c):
        if i==j or i+j==r-1:
            s+=mat[i][j]
print(s)