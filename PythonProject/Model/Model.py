import tkinter as tk
class Model():
    def __init__(self, root, dayEntry, monthEntry, label_res):
        self.root = root
        self.dayEntry = dayEntry
        self.monthEntry = monthEntry
        self.label_res = label_res


    def Zodiac(self):
        day = int(self.dayEntry.get())
        month = int(self.monthEntry.get())
        img = tk.PhotoImage(file="")

        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            self.label_res.configure(text="Овен")
            img = tk.PhotoImage(file="../img/Aries.png")
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            self.label_res.configure(text="Телец")
            img = tk.PhotoImage(file="../img/Taurus.png")
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            self.label_res.configure(text="Близнецы")
            img = tk.PhotoImage(file="../img/Gemini.png")
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            self.label_res.configure(text="Лев")
            img = tk.PhotoImage(file="../img/Lion.png")
        elif (month == 9 and day >= 23) or (month == 9 and day <= 22):
            self.label_res.configure(text="Дева")
            img = tk.PhotoImage(file="../img/Virgo.png")
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            self.label_res.configure(text="Скорпион")
            img = tk.PhotoImage(file="../img/Scorpio.png")
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            self.label_res.configure(text="Стрелец")
            img = tk.PhotoImage(file="../img/Sagittarius.png")
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            self.label_res.configure(text="Козерог")
            img = tk.PhotoImage(file="../img/Carpicorn.png")
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            self.label_res.configure(text="Водолей")
            img = tk.PhotoImage(file="../img/Aquarius.png")
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            self.label_res.configure(text="Рыбы")
            img = tk.PhotoImage(file="../img/Pisces.png")

        label = tk.Label(self.root, image=img, bg="#f2f2f2")
        label.image = img
        label.pack(pady=10)



