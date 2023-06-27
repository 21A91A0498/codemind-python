r,c=map(int,input().split())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
s=0
ss=0
for i in range(r):
    for j in range(c):
        if (mat[i][j])%2:
            s+=mat[i][j]
        else:
            ss+=mat[i][j]
print(ss,s)