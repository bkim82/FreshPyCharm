from tkinter import *
class Application(Frame):

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Enter the following:"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,
              text = "Character1: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person1_ent = Entry(self)
        self.person1_ent.grid(row = 1, column = 1, sticky = W)

        Label(self,
              text = "Character2:"
              ).grid(row = 3, column = 0, sticky = W)
        self.person2_ent = Entry(self)
        self.person2_ent.grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = "Pet Name:"
              ). grid(row = 5, column = 0, sticky = W)
        self.pet_ent = Entry(self)
        self.pet_ent.grid(row = 5, column = 1, sticky = W)


#Object
        Label(self,
              text="Object:"
              ).grid(row=2, column=0, sticky=W)

        self.phone = BooleanVar()
        Checkbutton(self,
                    text="Phone",
                    variable=self.phone
                    ).grid(row=2, column=1, sticky=W)

        self.money = BooleanVar()
        Checkbutton(self,
                    text="Money",
                    variable=self.money
                    ).grid(row=2, column=2, sticky=W)

#Time Of Day

        Label(self,
              text = "Time of Day:"
              ).grid(row=4, column=0, sticky = W)
        self.time = StringVar()
        self.time.set(None)

        time = ["Night", "Day"]
        column = 1
        for part in time:
            Radiobutton(self,
                        text = part,
                        variable = self.time,
                        value = part
                        ).grid(row = 4, column = column, sticky = W)
            column += 1

#Location

        Label(self,
              text="Location:"
              ).grid(row=6, column=0, sticky=W)
        self.place = StringVar()
        self.place.set(None)

        place = ["New Jersey", "New York"]
        column = 1
        for part in place:
            Radiobutton(self,
                        text=part,
                        variable=self.place,
                        value=part
                        ).grid(row=6, column=column, sticky=W)
            column += 1

        Button(self,
               text = "Click for story",
               comman = self.tell_story
               ).grid(row = 7, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 8, column = 0, columnspan = 4)

    def tell_story(self):
        person1 = self.person1_ent.get()
        person2 = self.person2_ent.get()
        pet = self.pet_ent.get()
        objects = ""
        if self.phone.get():
            objects += "a phone, "
        if self.money.get():
            objects += "a coins, "
        time = self.time.get()
        location = self.place.get()

        story = person1
        story += " and "
        story += person2
        story += " was in a barn at "
        story += location
        story += " during the "
        story += time
        story += " time."
        story += "They were relaxing in the right corner of the barn, when suddenly they heard a sound in the left corner."
        story += "There were multiple objects on a table, and "
        story += person1
        story += " and "
        story += person2
        story += " were frightened that one of the objects fell. The objects were the following: "
        story += objects
        story += "and a tablet."
        story += "They went to go check on the sound, and they found out that it was just "
        story += pet
        story += " making the noise."
        story += " The moral of the story? Be optimistic."


        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()





