from tkinter import *


class Todo:
    def __init__(self):
        self.create_list()
        self.show_list()

    def create_list(self):
        self.show = []
        self.state =int(input("Enter how many thing you need to enter"))
        for things in range(0,self.state):
            things = input("Enter the things you need to do")
            self.show.append(things)
    def show_list(self):

        canvas = Canvas(gui, width=1000, height=750, bg="black")

        canvas.create_text(300, 50, text = self.show, fill="white", font=('Helvetica 15 bold'))

        canvas.pack()


gui = Tk()
gui.geometry('800x450')
gui.title('To do list')

td = Todo()

gui.mainloop()




