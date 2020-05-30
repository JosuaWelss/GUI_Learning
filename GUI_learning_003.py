import tkinter as tk

root = tk.Tk()

lab1 = tk.Label(root, text = "Hallo,")
lab2 = tk.Label(root, text = "Welt!")

b = tk.Button(root, text = "Knopf")


lab1.pack(side="left")
lab2.pack(side="left")
b.pack(side='bottom')


root.mainloop()
