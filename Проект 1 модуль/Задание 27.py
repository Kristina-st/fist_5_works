from tkinter import *
from tkinter.messagebox import *
# подключаем диалоговое окно выбор цвета:
from tkinter.colorchooser import askcolor


brush_size = 3
color = "#000000"

root = Tk( )
root.title("Виджет Canvas, рисование ")
root.geometry("400x400+250+250")
# создаем фрейм для размещения на нем кнопки:
win = Frame(root, bd = 1, relief = RAISED)
win.pack(anchor = "n", expand = YES, fill = X)


# создаем область рисования Canvas:
can = Canvas(root)
can.pack(expand = YES, fill = BOTH)


def closeQuery( ):
    # При нажатии на кнопку запускаем диалоговое окно.
    # Спрашиваем у пользователя, закрывать ли программу:
    if askyesno('Выход из программы...', 'Закрыть программу? '):
        showwarning('Диалоговое окно', 'Внимание!!!')
        # Уничтожаем главное окно и поэтому закрываем программу:
        root.destroy( )
    else:
        showinfo('Диалоговое окно', 'Информация')

def color_choose():
    global color
    color = askcolor( )[1]
    print("Диалоговое окно Цвет возвращает результат:", color)

#####
def fun(event):
    global brush_size
    global color
    if len(color)>7:
        color = "black"
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    can.create_oval(x1,y1,x2,y2,fill = color, outline = color)
        
#####

def brush_size_change(new_size):
    global brush_size
  
    brush_size = new_size
    


    
Button(win, text = 'Выход', command = closeQuery).pack(side = RIGHT,padx = 13, pady = 5)
Button(win, text = 'Цвет', command = color_choose).pack(side = RIGHT, padx = 10, pady = 5)

can.bind("<B1-Motion>",fun)


can.columnconfigure(6, weight=1)
can.rowconfigure(2, weight=1)

rb_var = StringVar()
rb_var.set('3')
five_btn = Radiobutton(text="5",width=0, command=lambda: brush_size_change(5),variable=rb_var, value = '5')
four_btn = Radiobutton(text="4",width=10, command=lambda: brush_size_change(4),variable=rb_var, value = '4')
two_btn = Radiobutton(text="2",width=10, command=lambda: brush_size_change(2), variable=rb_var, value = '2')
one_btn = Radiobutton(text="1",width=10, command=lambda: brush_size_change(1), variable=rb_var, value = '1')
three_btn = Radiobutton(text="3",width=10, command=lambda: brush_size_change(3),variable=rb_var, value = '3')


 
#Scala = Scale(win, from_=0, to=25, resolution = 0.5, command = brush_size_change(brush_size),orient = HORIZONTAL)
#Scala.pack(padx=10, pady=5)

five_btn.pack(side = LEFT, padx = 4, pady = 10)
four_btn.pack(side = LEFT, padx = 3, pady = 10)
three_btn.pack(side = LEFT, padx = 2, pady = 10)
two_btn.pack(side = LEFT, padx = 1, pady = 10)
one_btn.pack(side = LEFT, padx = 0, pady = 10)

root.mainloop( )
