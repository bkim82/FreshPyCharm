from tkinter import *
from Lab6_2.Encryptor import Encryptor

class Application(Frame):
    def __init__ (self,master):
        super(Application, self).__init__(master)
        self.encryptor = Encryptor("cipher1.txt")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Enter the message:").grid(row=0, column=0, columnspan=4, sticky=W)
        Label(self, text="Out:").grid(row=3, column=0, sticky=W)

        self.input = Text(self, width = 40, height=6, wrap=WORD)
        self.input.grid(row=1, column=0, columnspan=4, sticky=W)
        self.output = Text(self, width=40, height=6, wrap = WORD)
        self.output.grid(row=4, column=0, columnspan=4, sticky=W)

        Button(self, text="Encrypt", command=self.encrypt).grid(row=2, column=1, sticky=W)
        Button(self, text ="Decrypt", command=self.decrypt).grid(row=2, column=2, sticky=W)

    def encrypt(self):
        out = self.encryptor.encrypt_message(self.input.get(1.0, END))
        self.output.delete(0.0,END)
        self.output.insert(0.0,out)

    def decrypt(self):
        out = self.encryptor.decrypt_message(self.input.get(1.0, END))
        self.output.delete(0.0,END)
        self.output.insert(0.0,out)


root = Tk()
root.title("Encrypt/Decrypt Tool")
root.geometry("300x300")
app = Application(root)
root.mainloop()