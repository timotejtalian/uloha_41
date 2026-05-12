import tkinter as tk
win = tk.Tk()  
win.title('Halasle')
canvas = tk.Canvas(win, width=500, height=600, bg='white')
canvas.pack()
kod_student = ''

canvas.create_text(250, 375, text='Vyber jedla', font=('Comic Sans MS', 40), anchor='center', fill = 'darkkhaki')
obj1 = canvas.create_rectangle(50, 450, 150, 550, fill='red', outline='black')
obj2 = canvas.create_rectangle(150, 450, 250, 550, fill = 'green', outline='black')
obj3 = canvas.create_rectangle(250, 450, 350, 550, fill='blue', outline='black')
obj4 = canvas.create_rectangle(350, 450, 450, 550, fill='orange', outline='black')

label = tk.Label(win, text='Zadaj kod studenta :', font=('Comic Sans MS', 10))
label.pack()

kod = tk.Entry(win, width=20)
kod.insert(0, "")
kod.pack()

def ziskat_kod():
    if kod.get() == '' or not kod.get().isalpha():
        return ''
    return kod.get()

def klik(event):
    global kod_student
    if ziskat_kod() == '':
        return
    closest = canvas.find_closest(event.x, event.y)[0]
    if obj1 == closest:
        kod_student = ziskat_kod() + ' c'
    elif obj2 == closest:
        kod_student = ziskat_kod() + ' z'
    elif obj3 == closest:
        kod_student = ziskat_kod() + ' m'
    elif obj4 == closest:
        kod_student = ziskat_kod() + ' o'
    objednavky.write(kod_student + '\n')

objednavky = open('vyber_jedla.txt', 'w')

canvas.bind('<Button-1>', klik)
canvas.mainloop()
objednavky.close()
win.mainloop()