r,c=map(int,input().split())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
s=0
ss=0
for i in range(r):
    if i%2:
        s+=sum(mat[i])
    else:
        ss+=sum(mat[i])
print(ss,s)