s=input()
s=s.replace(' ','')
d={}
for i in s.lower():
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
k=list(d.keys())
k.sort(key=lambda x:ord(x))
string=''
for i in k:
    string+=i
print(string)