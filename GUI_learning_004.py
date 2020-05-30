import tkinter as tk



def wechselFarbe():
    lab2['bg'] = '#000000'
    return

root = tk.Tk()

lab1 = tk.Label(root, text = "Hallo,")
lab2 = tk.Label(root, text = "Welt!")


lab1["bg"]='#FF00FF'
lab2["background"]='#FFFF00'

## merke bg = background


b = tk.Button(root, text = "Knopf", command = wechselFarbe())


lab1.pack()
lab2.pack()
b.pack()


root.mainloop()