from  tkinter  import  *   	# подключаем  tkinter

# Подключаем  модуль с диалоговыми  окнами  tkinter:
from  tkinter.messagebox  import  * 

root  =  Tk(  )    	# создаем главное окно

# размеры окна:
root.geometry("650x180+180+100")

root.title("Калькулятор")         # заголовок окна

#  Создадим 3 фрейма:   	fr_xy,        fr_op    и     fr_res 
#  для размещения компонент.

# фрейм fr_xy – компоненты для ввода чисел x, y:
fr_xy  =  Frame(root)  
fr_xy.pack(side  =  TOP, expand  =  YES, fill  =  X)

fr_xy['bg'] = 'light green'

# На нем размещаем две метки и два редактора для ввода чисел x, y: 
lx  =  Label(fr_xy,  text  =  "x = ")
lx.pack(side  =  LEFT, padx  =  10, pady  =  10)


entX  =  Entry(fr_xy)
entX.insert(0,  0)  # – в редактор записываем в позицию 0 число 0
entX.pack(side  =  LEFT, padx  =  10, pady  =  10)

# Редактор будет выбран при старте (иметь фокус ввода):
entX.focus(  ) 

ly  =  Label(fr_xy,  text  =  "y = ")
ly.pack(side  =  LEFT, padx  =  10, pady  =  10)

entY  =  Entry(fr_xy)
entY.insert(0,  0)
entY.pack(side   =  LEFT, padx  =  10, pady  =  10)


# Создание фрейма с заголовком fr_op  – выбор операции: 
fr_op   =  LabelFrame(root,  text  =  "Операция:", bg = 'spring green', fg = 'black')
fr_op.pack(side   =  TOP, expand  =  YES, fill  =  X)

# задаем вид курсора мыши над виджетом:
fr_op.config(cursor = "gobbler")

#  Операцию будем выбирать с помощью виджета Radiobutton:
oper   =  ['+',  '-',  '*',  '/', '//', '%', 'y^2', 'sqrt(x)']    #   –  список операций

#   Вводим строковую переменную tkinter, ее свяжем с выбором
#   Radiobutton
varOper  =  StringVar(  ) 
#  В цикле создаем 4 кнопки Radiobutton (связываем их 
# с созданной переменной varOper):
for op in oper:
       Radiobutton(fr_op,  text  =  op, variable  =  varOper, 
                              value  =  op).pack(side  =  LEFT,
                              padx  =  20,  pady  =  10)

# Устанавливаем текущее значение ‘+’:
varOper.set(oper[0]) 

#  Создаем 3-й фрейм fr_res – вычисление значения 
#  и вывод результата: 
fr_res  =  Frame(root)
fr_res.pack(side  =  TOP, expand  =  YES, fill  =  BOTH)
fr_res['bg'] = 'green'

# Обработчик кнопки:
def OnButtunResult(  ):
   #  Защищенный блок, будем пытаться перевести текст 
   #  из редактора Entry в число:
    try: 
        x  =  float(entX.get())    #  извлекаем число из 1-го редактора
    except  ValueError: 
   # если не получилось, выдаем сообщение и выходим:
        showerror("Ошибка заполнения", "Переменная x не является числом")
        return
  # Защищенный блок 2:
    try: 
        y = float(entY.get()) 
    except  ValueError:
        showerror("Ошибка заполнения", "Переменная y не является числом")
        return
  #  В переменную op записываем выбранную операцию:
    op  =  varOper.get(  )
  #  Вычисляем:
    if    op ==  '+':   res  =  x  +  y
    elif  op ==  '-':  res  =  x  -  y
    elif  op ==  '*':  res  =  x  *  y
    elif  op ==  '/':
         if  y  !=  0:  res  =  x  /  y
         else:  res  =  'NAN'
    elif op == '//':
        if  y  !=  0:  res  =  x  //  y
        else:  res  =  'NAN'
    elif op == '%':
        if  y  !=  0:  res  =  x  %  y
        else:  res  =  'NAN'
    elif op == 'y^2':
        res = y ** 2
    elif op == 'sqrt(x)':
        if x < 0: res = 'NAN'
        else: res = x ** 0.5
    else:
        res = 'операция выбрана неправильно'
 # Вывод результата на метку:   
    lres['text']  =  res
# Обработчик кнопки закончился.

# Создаем кнопку и метку, к кнопке присоединяем обработчик:
Button(fr_res,  text  =  "=", width  =  10, 
              command  =  OnButtunResult).pack(side  =  LEFT,
              padx  =  30, pady  =  20) 
lres  =  Label(fr_res, text  =  "")
lres.pack(side  =  LEFT, padx  =  30, pady  =  20)

# Запуск цикла обработки сообщений:
root.mainloop(  )
