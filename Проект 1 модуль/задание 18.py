from tkinter import *

# подключаем диалоговые окна:
from tkinter.messagebox import * 

#  подключаем диалоговое окно выбор цвета:
#from tkinter.colorchooser import askcolor 

root = Tk( )
root.title("Задание 18")
root.geometry("300x300+250+250")

#  Создаем фрейм для размещения на нем других компонент:
win1 = Frame(root, bg  =  '#555555')



#  Помещаем фрейм на форму методом pack.
#  Вместо параметра side (прижать к стороне) задаем 
#  параметр anchor (якорь): компонент будет прижат к северной 
#  (north) стороне и растянут по ширине.
win1.pack(anchor = "n", expand = YES, fill = X)

#  Обработчик кнопки закрытия программы: 
def closeQuery( ):
    #  При нажатии на кнопку запускаем диалоговое окно.
    #  Спрашиваем у пользователя, закрывать ли программу:
    if  askyesno('Выход из программы...', 'Закрыть программу? '):
        root.destroy()

def button_1():
    topL1 = Toplevel(root)
    topL1.title("окно кнопки 1")
    topL1.transient(root)
    
    

#  Создаем кнопку закрытия программы:
Button(win1, text  =  'Выход', command  =  closeQuery).pack(
    		  side  =  RIGHT, padx  =  10, pady  =  5)
Button(win1, text = 'Кнопка 1', command = button_1).pack(
 side = RIGHT, padx = 10, pady = 5)

root.mainloop(  )

