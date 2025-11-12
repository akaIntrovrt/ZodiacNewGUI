from View.View import View
from Model.Model import Model
import tkinter as tk

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root, self)
        self.model = Model(self.root, self.view.dayEntry, self.view.monthEntry, self.view.label_res)

    def getZodiac(self):
        day = int(self.view.dayEntry.get())
        month = int(self.view.monthEntry.get())
        self.model.Zodiac()

    def openApp(self):
        self.root.mainloop()

user = Controller()
user.openApp()