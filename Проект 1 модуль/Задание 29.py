from tkinter import *
from math import *   #  подключаем математические функции
from tkinter.messagebox import * # подключаем диалоговые окна
root  =  Tk( )
root.title("Методы eval  и exec")
#  создаем фрейм для размещения компонент задающих  x, y:
win1  =  Frame(root)
win1.pack(anchor  =  "n", expand  =  YES, fill  =  X)
lx  =  Label(win1,  text  =  "x = ")
lx.pack(side  =  LEFT,  padx  =  10, pady  =  10)

entX  =  Entry(win1)
entX.insert(0, 0)
entX.pack(side   =  LEFT,  padx  = 10,  pady  =  10)
entX.focus(  )

ly  =  Label(win1,  text  =  "y = ")
ly.pack(side  =  LEFT, padx  =  10, pady  =  10)

entY  =  Entry(win1)
entY.insert(0, 0)
entY.pack(side  =  LEFT, padx  =  10, pady  =  10)

# создаем второй фрейм для задания функции и вычисления:
win2  =  Frame(root)
win2.pack(anchor  =  "n", expand  =  YES, fill  =  X)
Label(win2,  text  =  "Функция: ").pack(side  =  LEFT, 
            padx  =  10,  pady  =  10)
entF   =  Entry(win2)
entF.pack(side   =  LEFT, padx  =  10, pady  =  10, expand  =  YES,
                   fill  =  X)
entF.insert(0, "x and y")


# Создаем обработчик кнопки: 
def  res( ): 
     try: 
          x   =   list(entX.get())
          for el in x:
              if (el != ' '):
                   print(el)
                   if ( int(el) != 0 and int(el) != 1):
                        int(el) / 0
              else:
                   x.remove(' ')
                  
     except ValueError: # если вводится первый символ - не цифра
          showerror("Ошибка заполнения", 
                  "вектор x должен состоять из целых чисел")
          return

     except ZeroDivisionError:
          showerror("Ошибка заполнения", 
                  "вектор x должен состоять из 1 и 0")
          return

     
     try: 
          y  =  list(entY.get())
          for el in y:
              if (el != ' '):
                   if ( int(el) != 0 and int(el) != 1):
                        int(el) / 0
              else:
                   y.remove(' ')
                  
     except ValueError: # если вводится первый символ - не цифра
          showerror("Ошибка заполнения", 
                  "вектор y должен состоять из целых чисел")
          return

     except ZeroDivisionError:
          showerror("Ошибка заполнения", 
                  "вектор y должен состоять из 1 и 0")
          return
          

     try:
          if (len(x) == len(y)):
               F   =  entF.get( )  # считываем текст из редактора
               labF['text']  =  eval(F) # выполняем его и результат
               # записываем на метку
          else:
               5 / 0

     except ZeroDivisionError:
          showerror("Ошибка заполнения", 
                  "векторы должны быть одной длины")
          return
     
     
     #print(F)



# Создаем кнопку и метку:
Button(win2,  text  =  'Вычислить', command  =  res).pack(
             side  =  LEFT,  padx  =  10,  pady  =  5)
labF  =  Label(win2,  text  =  " ")
labF.pack(side  =  LEFT,  padx  =  10,  pady  =  10)
root.mainloop()
