from tkinter import *

class Application (Frame):

    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = Button(self, text = "I do nothing!")
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Me too!")

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3.configure(text = "Same here!")



root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)
root.mainloop()
