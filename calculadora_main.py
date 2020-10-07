from tkinter import *
import calculadora_operations as calc

number1 = 0
number2 = 0
number3 = 0
result = 0
actual_operation = 0
first = 1

def testdot(number):  # testa se tem ponto em qualquer parte
    for i in number:
        if i == '.':
            return 1
    return 0

def insertnumber(number):
    global first
    visor_number = e.get()
    has_dot = testdot(visor_number)
    if (first):
        if number != 0:
            if number != '.':
                e.delete(0, END)
                e.insert(END, number)
                first = 0
            else:
                e.insert(END, number)
                first = 0

    elif(not has_dot):
        e.insert(END, number)
    elif(has_dot and number !='.'):
        e.insert(END, number)

def clearnumber():
    global first
    e.delete(0, END)
    e.insert(END, 0)
    first = 1

def pressoperation(operation):
    global number1
    global actual_operation
    number1 = float(e.get())
    print("number1 = " + str(number1))
    actual_operation = operation
    clearnumber()

def pressequal():
    global number1
    global number2
    global actual_operation
    global result
    number2 = float(e.get())
    if int(actual_operation) == 1:
        result = calc.soma(number1, number2)
    elif int(actual_operation) == 2:
        result = calc.subtracao(number1, number2)
    elif int(actual_operation) == 3:
        result = calc.multiplicacao(number1, number2)
    elif int(actual_operation) == 4:
        result = calc.divisao(number1, number2)
    e.delete(0, END)
    e.insert(END, result)

def hidecalc():
    frame1.grid_forget()
    frame2.grid(row=1, column=0, padx=5, pady=5)

def hideconvertor():
    frame2.grid_forget()
    frame1.grid(row=0, column=0, padx=5, pady=5)

def destroy_labels_conversor():
    for i in vetor_labels:
        i.destroy()

def showw(event):
    destroy_labels_conversor()
    grid_text_conv()

def grid_text_conv():

    number3 = float(e2.get())

    text_mile = calc.km_to_mile(number3)
    text_km = str(number3) + ' Km = ' + '{:.2f}'.format(text_mile) + ' Mile'
    label_km = Label(frame2, text=text_km)
    label_km.grid(row=1, column=0, padx=25, pady=3)

    text_km2 = calc.mile_to_km(number3)
    text_mile2 = str(number3) + ' Mile = ' + '{:.2f}'.format(text_km2) + ' Km'
    label_mile = Label(frame2, text=text_mile2)
    label_mile.grid(row=2, column=0, padx=25, pady=2)

    text_kmh = calc.kmh_to_ms(number3)
    text_kmh2 = str(number3) + ' Km/h = ' + '{:.2f}'.format(text_kmh) + ' m/s'
    label_kmh = Label(frame2, text=text_kmh2)
    label_kmh.grid(row=3, column=0, padx=25, pady=2)

    text_ms = calc.ms_to_kmh(number3)
    text_ms2 = str(number3) + ' m/s = ' + '{:.2f}'.format(text_ms) + ' Km/h'
    label_ms = Label(frame2, text=text_ms2)
    label_ms.grid(row=4, column=0, padx=25, pady=2)

    text_inch = calc.inch_to_cm(number3)
    text_inch2 = str(number3) + ' inch = ' + '{:.2f}'.format(text_inch) + ' cm'
    label_inch = Label(frame2, text=text_inch2)
    label_inch.grid(row=5, column=0, padx=25, pady=2)

    text_cm = calc.cm_to_inch(number3)
    text_cm2 = str(number3) + ' cm = ' + '{:.2f}'.format(text_cm) + ' inch'
    label_cm = Label(frame2, text=text_cm2)
    # label_blank = Label(frame2, text='')
    # label_blank.grid(row=6, column=0)
    label_cm.grid(row=6, column=0, padx=25, pady=2)

    text_foot = calc.foot_to_meter(number3)
    text_foot2 = str(number3) + ' foot = ' + '{:.2f}'.format(text_foot) + ' meter'
    label_foot = Label(frame2, text=text_foot2)
    label_foot.grid(row=7, column=0, padx=25, pady=2)

    text_meter = calc.meter_to_foot(number3)
    text_meter2 = str(number3) + ' meter = ' + '{:.2f}'.format(text_meter) + ' foot'
    label_meter = Label(frame2, text=text_meter2)
    # label_blank = Label(frame2, text='')
    # label_blank.grid(row=6, column=0)
    label_meter.grid(row=8, column=0, padx=25, pady=3)

    global vetor_labels
    vetor_labels = [label_ms,label_mile,label_kmh,label_km,label_inch,label_cm,label_foot,label_meter]


root = Tk()
root.title("My Calculator")

mylabel = Label(root, text="Hi")

frame1 = LabelFrame(root, text = 'calculator', padx=5,pady=5)
frame1.grid(row=0,column=0,padx=5,pady=5)

e = Entry(frame1, width=15, font=('Verdana', 25), borderwidth=4, justify=RIGHT)
e.grid(row=0, column=0, columnspan=3)
e.insert(0, number1)
e.focus()

# 0 to 9
button0 = Button(frame1, text="0", font=('Verdana', 15), command=lambda: insertnumber(0))
button0.grid(row=4, column=0, sticky="nsew", padx=1,pady=1)
button1 = Button(frame1, text="1", font=('Verdana', 15), command=lambda: insertnumber(1))
button1.grid(row=3, column=0, sticky="nsew", padx=1,pady=1)
button2 = Button(frame1, text="2", font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber(2))
button2.grid(row=3, column=1, sticky="nsew", padx=1,pady=1)
button3 = Button(frame1, text="3", font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber(3))
button3.grid(row=3, column=2, sticky="nsew", padx=1,pady=1)
button4 = Button(frame1, text="4", font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber(4))
button4.grid(row=2, column=0, sticky="nsew", padx=1,pady=1)
button5 = Button(frame1, text="5", font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber(5))
button5.grid(row=2, column=1, sticky="nsew", padx=1,pady=1)
button6 = Button(frame1, text="6", font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber(6))
button6.grid(row=2, column=2, sticky="nsew", padx=1,pady=1)
button7 = Button(frame1, text="7", font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber(7))
button7.grid(row=1, column=0, sticky="nsew", padx=1,pady=1)
button8 = Button(frame1, text="8",  font=('Verdana', 15),padx=25, pady=15, command=lambda: insertnumber(8))
button8.grid(row=1, column=1, sticky="nsew", padx=1,pady=1)
button9 = Button(frame1, text="9", font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber(9))
button9.grid(row=1, column=2, sticky="nsew", padx=1,pady=1)

buttoncle = Button(frame1, text='clear', font=('Verdana', 15), padx=15, pady=5, command=lambda: clearnumber())
buttoncle.grid(row=0, column=3, sticky="nsew", padx=1,pady=1)
buttonsum = Button(frame1, text='+',  font=('Verdana', 15),padx=25, pady=15, command=lambda: pressoperation(1))
buttonsum.grid(row=1, column=3, sticky="nsew", padx=1,pady=1)
buttonsub = Button(frame1, text='-',  font=('Verdana', 15),padx=25, pady=15, command=lambda: pressoperation(2))
buttonsub.grid(row=2, column=3, sticky="nsew", padx=1,pady=1)
buttonmul = Button(frame1, text='*',  font=('Verdana', 15), width=5, height=2, command=lambda: pressoperation(3))
buttonmul.grid(row=3, column=3, sticky="nsew", padx=1,pady=1)
buttondiv = Button(frame1, text='/',  font=('Verdana', 15),padx=25, pady=15, command=lambda: pressoperation(4))
buttondiv.grid(row=4, column=3, sticky="nsew", padx=1,pady=1)
buttondot = Button(frame1, text='.', font=('Verdana', 15), padx=25, pady=15, command=lambda: insertnumber('.'))
buttondot.grid(row=4, column=1, sticky="nsew", padx=1,pady=1)
buttonequ = Button(frame1, text='=',  font=('Verdana', 15),padx=25, pady=15, command=lambda: pressequal())
buttonequ.grid(row=4, column=2, sticky="nsew", padx=1,pady=1)

#to implement
buttonpot = Button(root, text='^')
buttonsqr = Button(root, text='√')
buttonround = Button(root, text='round')


#frame convertor
frame2 = LabelFrame(root, text = 'converter', padx=5,pady=5)
# frame2.grid(row=1,column=0,padx=5,pady=5)

e2 = Entry(frame2, width=15, font=('Verdana', 20), borderwidth=4, justify=RIGHT)
e2.grid(row=0, column=0, columnspan=3)
e2.bind("<Return>", showw)
e2.insert(0, number3)
e2.focus()

grid_text_conv()

#switch to convertor
buttoncalc = Button(root, text='calculadora', command=hideconvertor)
buttoncalc.grid(row=5,column=0, padx=10, pady=2)

buttonconverter = Button(root, text='conversor', command=hidecalc)
buttonconverter.grid(row=5,column=1, padx=10, pady=5)

#text convertor



root.mainloop()


