# tKINTER MODULE

from tkinter import *

# main window
w = Tk()
w.title('This is tkinter module')

b = Button(w, text='stop', width=25, command=w.destroy)
b.pack()

# canvas
c = Canvas(w, width=40, height=60)
c.pack()
ch = 20
cw = 200
y = int(ch / 2)
c.create_line(0, y, cw, y)

w.mainloop()
