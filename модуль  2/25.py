f = open('для задания 25.txt', 'r')
L = [] # список для чисел из файла
for line in f: # читаем построчно
     # переводим в int и добавляем в список:
     L += map(int, line.split()) 
     # или
     # temp_list = [int(i) for i in line.split()]
     # L.extend(temp_list)
f.close()

maxi = max(L)
index = L.index(maxi)
L[index] = L[len(L) - 1] 

f = open('для задания 25.txt', 'w')
for i in range(len(L)):
    f.write('%d ' % L[i])
    
f.truncate(len(L)*2 - 1)
   
f.close()
