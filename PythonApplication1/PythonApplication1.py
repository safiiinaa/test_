import numpy as np
f = open('input\input16.txt')
i=0
aa=[]
for line in f:
    i+=1
    if i==1:
        n,k=line.split()
        n=int(n)
        k=int(k)
    if i==2:
        a=line.split()
        for v in a:
            aa.append(int(v))
        print(aa)
a=aa
while 1:
    vsep = [(a[i],a[j]) for i in range(len(a)) for j in range(i + 1, len(a))]
    novsep = [p for p in vsep if (p[0] + p[1]) % k == 0]
    if not novsep:
        break
    snovsep = sum(novsep, ())   
    counts = {el: snovsep.count(el) for el in set(snovsep)}
    S = max(counts, key=counts.__getitem__)
    a.remove(S)
answer=str(len(a))
print ("Введите полное название файла для ввода: ")
name_file = input()
file = open(name_file, mode='w')
file.write(answer) 
