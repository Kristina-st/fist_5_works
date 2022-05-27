# сохранить произвольный словарь(dict) в файл с
# помощью модуля Pickle. Прочитайте обратно его из
# этого файла и выведите на экран

import pickle
f = open('file.txt','wb+')
d = {'1': 4, '2': 321, 'g': 'feed', 'add': 'kukarella'}
pickle.dump(d,f)
f.seek(0)
L = []
while True:
    try:
        L.append(pickle.load(f))
    except EOFError:
        break

print(L)
f.close()
