n=int(input())
mat1=[]
mat2=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat1.append(l)
for i in range(n):
    ll=list(map(int,input().split()))
    mat2.append(ll)

mat=[]
for i in range(n):
    k=[]
    for j in range(n):
        s=abs((mat2[i][j])-(mat1[i][j]))
        k.append(s)
    mat.append(k)
for i in mat:
    print(*i)


