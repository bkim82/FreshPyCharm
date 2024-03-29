from tkinter import *
class Application(Frame):
s
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Enter information for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,
              text = "Person: "
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        Label(self,
              text = "Plural Noun:"
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)

        Label(self,
              text = "Verb:"
              ). grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)

        Label(self,
              text="Adjective(s):"
              ).grid(row=4, column=0, sticky=W)


        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "itchy",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)

        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="joyous",
                    variable=self.is_joyous
                    ).grid(row=4, column=2, sticky=W)

        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="electric",
                    variable=self.is_electric
                    ).grid(row=4, column=3, sticky=W)
        Label(self,
              text = "Body Part:"
              ).grid(row=5, column=0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)

        body_parts = ["bellybutton", "big toe", "Medulla oblogata"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        Button(self,
               text = "Click for story",
               comman = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy, "
        if self.is_joyous.get():
            adjectives += "joyous, "
        body_part = self.body_part.get()

        story = "The famous explorer "
        story += person
        story += " had nearly given up a life-long quest to find The Lost City of "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + "."
        story += " A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed the explorer. "
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + "."
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()





