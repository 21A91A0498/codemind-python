n=int(input())
ml=list(map(int,input().split()))[:n]
s=0
su=0
for i in range(len(ml)):
    if i%2==0:
        s+=ml[i]
    elif i%2:
        su+=ml[i]
print(abs(s-su))  