n=int(input())
l=list(map(int,input().split()))
ol=[]
el=[]
for i in l:
    if i%2:
        ol.append(i)
    else:
        el.append(i)
nl=[]
if len(el)==len(ol):
    for i in range(len(el)):
        nl.append(el[i])
        nl.append(ol[i])
    print(*nl)
elif len(el)<len(ol):
    for i in range(len(el)):
        nl.append(el[i])
        nl.append(ol[i])
    nl=nl+ol[len(el)::]
    if len(nl)%2:
        nl.append(0)
        print(*nl)
    else:
        print(*nl)
else:
    for i in range(len(ol)):
        nl.append(el[i])
        nl.append(ol[i])
    nl=nl+el[len(ol)::]
    if len(nl)%2:
        nl.append(0)
        print(*nl)
    else:
        print(*nl)
        