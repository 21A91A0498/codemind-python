s=input()
s=s.replace(' ','').lower()
d={}
for  i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
l=[]
st='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'
for i,j in d.items():
    if j==1:
        l.append(i)
l.sort(key=lambda x:ord(x))
for i in l:
    st+=i
print(st)