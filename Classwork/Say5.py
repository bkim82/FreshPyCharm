import tkinter

class Application (tkinter.Frame):

    def __init__ (self,master):
        super().__init__(master)
        self.grid()
        self.create__widgets()

    def create__widgets (self):

        self.bttn_hi = tkinter.Button(self)
        self.bttn_hi["text"] = "Hi Button"
        self.bttn_hi["command"] = self.say_hi
        self.bttn_hi.grid()

        self.bttn_quit = tkinter.Button(self, text = "Quit", bg = "red", font = ("Comic Sans", 12))
        self.bttn_quit.grid()
        self.bttn_quit["command"] = self.quit

    def say_hi(self):
        print("Hello")


root = tkinter.Tk()
root.title("Say Hi!")
root. geometry("200x85")
app = Application(root)
root.mainloop()