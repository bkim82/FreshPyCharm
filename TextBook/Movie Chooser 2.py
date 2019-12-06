from tkinter import*

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Choose your favorite type of movie"
              ).grid(row = 0, column = 0, sticky = W)
        Label(self,
              text = "Select one:"
              ).grid(row = 1, column = 0, sticky = W)

        self.favorite = StringVar()
        self.facorite.set(None)

        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "comedy.",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
        Radiobutton(self,
                    text = "Drama",
                    variable = self.favorite,
                    value = "drama.",
                    )