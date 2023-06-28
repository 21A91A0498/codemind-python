s=input()
s=s.replace(' ','').lower()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
k=list(d.keys())
print(len(k))