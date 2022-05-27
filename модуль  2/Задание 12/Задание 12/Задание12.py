# создать новый файл, в который поместить только четные числа
# из файла (каждое число остается в строке с тем же номером;
# если в строке не было четных чисел, то в новом файле эта
# строка пустая)

f = open('file1.txt','r')
spisok = f.readlines()
f.close()


fnew = open('file2.txt','w+')

for el in spisok:
    st = ''
    sp = el.split(' ')
    chet = 0
    numbers = [int(P) for P in sp]
    for num in numbers:
        if num%2==0:
            st = st + str(num) + ' '
            chet = 1
        else:
            k = 0
            for c in str(num):
                st = st + ' '
            st = st + ' '
    if chet == 0:
        st = ''
        
    fnew.write(st + '\n')

#fnew.seek(0)

fnew.close()
    
    


