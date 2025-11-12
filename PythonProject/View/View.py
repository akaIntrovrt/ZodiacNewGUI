import tkinter as tk
from Model.Model import Model

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Zodiac Checker")
        self.root.geometry("800x800")
        self.root.configure(background="#f2f2f2")

        newPos = tk.Frame(root, bg="#f2f2f2")
        newPos.pack(pady=20)

        tk.Label(newPos, text="Day", font=("Arial", 20), bg="#f2f2f2")
        self.dayEntry = tk.Entry(newPos, font=("Arial", 20), width=5, justify="center", bg="#f2f2f2")
        self.dayEntry.pack(side="left", pady=5, padx=10)

        month = tk.Label(newPos, text="Month: ", font=("Arial", 20), bg="#f2f2f2")
        self.monthEntry = tk.Entry(newPos, font=("Arial", 20), width=5, justify="center", bg="#f2f2f2")
        self.monthEntry.pack(side="left", pady=5)

        year = tk.Label(newPos, text="Year: ", font=("Arial", 20), bg="#f2f2f2")
        self.yearEntry = tk.Entry(newPos, font=("Arial", 20), width=5, justify="center", bg="#f2f2f2")
        self.yearEntry.pack(side="left", pady=5)

        self.label_res = tk.Label(root, text="", font=("Arial", 20, "bold"), fg="blue", bg="#f2f2f2")
        self.label_res.pack(pady=20, padx=10)


        self.model = Model(self.root, self.dayEntry, self.monthEntry, self.label_res)

        button = tk.Button(newPos, text="Show Zodiac sign", font=("Arial", 20), command=self.model.Zodiac, width=20)
        button.pack(side="left", padx=10)
