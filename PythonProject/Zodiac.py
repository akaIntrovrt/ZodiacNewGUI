# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("800x800")
# root.title("Zodiac")
# root.configure(bg="#f2f2f2")

# newPos = tk.Frame(root, bg="#f2f2f2")
# newPos.pack(pady=20)
#
# day = tk.Label(newPos, text="Day", font=("Arial",20), bg="#f2f2f2")
# day.pack(side="left",pady=(20,5))
# dayEntry = tk.Entry(newPos, font=("Arial", 20), width=5, justify="center", bg="#f2f2f2")
# dayEntry.pack(side="left",pady = 5, padx = 10)
#
# month = tk.Label(newPos, text="Month: ", font=("Arial", 20), bg="#f2f2f2")
# month.pack(side="left",pady=(20,5))
# monthEntry = tk.Entry(newPos, font=("Arial", 20), width=5, justify="center", bg="#f2f2f2")
# monthEntry.pack(side="left",pady = 5)
#
#
# year = tk.Label(newPos, text="Year: ", font=("Arial", 20), bg="#f2f2f2")
# year.pack(side="left",pady=(20,5))
# yearEntry = tk.Entry(newPos, font=("Arial", 20), width=5, justify="center", bg="#f2f2f2")
# yearEntry.pack(side="left",pady = 5)
#
# label_res = tk.Label(root, text="", font=("Arial", 20, "bold"), fg="blue", bg="#f2f2f2")
# label_res.pack(pady=20, padx=10)


# def Zodiac():
#     day = int(dayEntry.get())
#     month = int(monthEntry.get())
#     img = tk.PhotoImage(file="")
#     label = tk.Label(root, image=img, bg="#f2f2f2")
#     label.pack(pady=10)
#     if (month == 3 and day >= 21) or (month == 4 and day <= 19):
#         label_res.configure(text="Овен")
#         img = tk.PhotoImage(file="./img/Aries.png")
#     elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
#         label_res.configure(text="Телец")
#         img = tk.PhotoImage(file="./img/Taurus.png")
#     elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
#         label_res.configure(text="Близнецы")
#         img = tk.PhotoImage(file="./img/Gemini.png")
#     elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
#         label_res.configure(text="Лев")
#         img = tk.PhotoImage(file="./img/Lion.png")
#     elif (month == 9 and day >= 23) or (month == 9 and day <= 22):
#         label_res.configure(text="Дева")
#         img = tk.PhotoImage(file="./img/Virgo.png")
#     elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
#         label_res.configure(text="Скорпион")
#         img = tk.PhotoImage(file="./img/Scorpio.png")
#     elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
#         label_res.configure(text="Стрелец")
#         img = tk.PhotoImage(file="./img/Saggitarius.png")
#     elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
#         label_res.configure(text="Козерог")
#         img = tk.PhotoImage(file="./img/Carpicorn.png")
#     elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
#         label_res.configure(text="Водолей")
#         img = tk.PhotoImage(file="./img/Aquarius.png")
#     elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
#         label_res.configure(text="Рыбы")
#         img = tk.PhotoImage(file="./img/Pisces.png")
#
#     label = tk.Label(root, image=img, bg="#f2f2f2")
#     label.image = img
#     label.pack(pady=10)

# button = tk.Button(newPos,  text="Show Zodiac sign", font=("Arial",20),command=Zodiac, width = 20)
# button.pack(side = "left", padx = 10)

import tkinter as tk
from Controller.Controller import Controller


class Main():
    def __init__(self):
        self.controller = Controller()

    def run(self):
        self.controller.openApp()

user = Main()

user.run()











































