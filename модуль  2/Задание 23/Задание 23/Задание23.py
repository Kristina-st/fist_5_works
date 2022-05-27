#из двух файлов целых чисел, упорядоченных по возрастанию
#создать новый файл чисел, упорядоченных по возрастанию

f1 = open('file1.txt','r')
f2 = open('file2.txt','r')
fnew = open('vozrastanie.txt','w+')

sp1 = f1.readlines()
sp2 = f2.readlines()

i = 0
for el1 in sp1:
    el1 = el1.rstrip()
    sp1[i] = el1.split(' ')
    sp1[i] = [int(P) for P in sp1[i]]
    i+=1
    
i = 0
for el2 in sp2:
    el2 = el2.rstrip()
    sp2[i] = el2.split(' ')
    sp2[i] = [int(P) for P in sp2[i]]
    i+=1


i1 = 0
j1 = 0
i2 = 0
j2 = 0
if len(sp1)>len(sp2):
    sp1, sp2 = sp2, sp1
    
#if len(sp1)>len(sp2):
while i1<len(sp1):
    while j1<len(sp1[i1]) and j2<len(sp2[i2]):
            
        if sp1[i1][j1]<sp2[i2][j2]:
            fnew.write(str(sp1[i1][j1]) + ' ')
            j1+=1
        else:
            fnew.write(str(sp2[i2][j2]) + ' ')
            j2+=1
            
    if j1>=len(sp1[i1]):
        j1 = 0
        i1+= 1
            
    if j2>=len(sp2[i2]):
        j2 = 0
        i2+=1
    fnew.write('\n')

if i2!=len(sp2)-1:
    for el in sp2[i2:]:
        for num in el[j2:]:
            fnew.write(str(num) + ' ')
        fnew.write('\n')
    
#fnew.seek(0)  

#print(fnew.readlines())
f1.close()
f2.close()
fnew.close()
