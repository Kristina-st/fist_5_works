from tkinter import *
from math import *   #  подключаем математические функции
from tkinter.messagebox import * # подключаем диалоговые окна

root  =  Tk( )
#root.title("Методы eval  и exec")
#  создаем фрейм для размещения компонент задающих  x, y:
win1  =  Frame(root)
win1.pack(anchor  =  "n", expand  =  YES, fill  =  X)
lx  =  Label(win1,  text  =  "x = ", bg = '#b6efea')
lx.pack(side  =  LEFT,  padx  =  10, pady  =  10)
win1.config(bg = '#b6efea')  
win1.config(height = 3, width = 20, bd = 8, relief = RAISED)
entX  =  Entry(win1)
entX.insert(0, 0)
entX.pack(side   =  LEFT,  padx  = 10,  pady  =  10)
entX.focus(  )


# создаем второй фрейм для задания функции и вычисления:
win2  =  Frame(root)
win2.pack(anchor  =  "n", expand  =  YES, fill  =  X)
Label(win2,  text  =  "Функция: ").pack(side  =  LEFT, padx  =  10,  pady  =  10)
entF   =  Entry(win2)





# Создаем обработчик кнопки: 
def  res( ): 
     try: 
          x   =   int(entX.get()) 
     except ValueError:
          showerror("Ошибка заполнения", "Переменная x не является целым числом")
          return
     if abs(x)%2 != 0:
         showerror("Ошибка заполнения", "Выход за пределы области определения функции")
     else:
         labF['text'] = str(sin(pi*(x*x-x-2))/(cos(pi*x)+1))

     

# Создаем кнопку и метку:
Button(win2,  text  =  'Вычислить', command  =  res).pack(side  =  RIGHT,  padx  =  50,  pady  =  5)

labF  =  Label(win2,  text  =  " ")

labF.pack(side  =  LEFT,  padx  =  10,  pady  =  10)
root.mainloop()
