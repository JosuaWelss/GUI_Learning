import tkinter as tk
from PIL import  ImageTk, Image

##Image bei Buttonclick, auf Label und als standard für button


def wechselFarbe1():
    lab2['bg'] = '#FFFF00'
    lab2['foreground'] ='#FF0000'
    lab2['font'] = 'Arial 16 italic'
    lab2['height'] = 2  ##Höhe = 2 Zeilen
    lab2['width'] = 20  ##Breite = 20 Zeichen
    lab2['anchor'] ="n" ##Schrift ist oben in der Zeile, north, east, south, west

    return

def wechselFarbe2():
    lab2['bg'] = '#000000'
    lab2['fg'] = '#FFFFFF'
    lab2['font'] = 'Courier 12 bold'
    lab2['height'] = 1
    lab2['width'] = 5
    lab1['image'] = img1
    return



root = tk.Tk()

img1 = ImageTk.PhotoImage(Image.open("bild1.png"))
img2 = ImageTk.PhotoImage(Image.open("bild2.png"))
img3 = ImageTk.PhotoImage(Image.open("bild3.png"))
img4 = ImageTk.PhotoImage(Image.open("bild4.png"))


lab1 = tk.Label(root, image=img3)
lab2 = tk.Label(root, text = "Welt!")



## merke bg = background


b = tk.Button(root, image=img2, command=wechselFarbe1)    ##command=wechselfarbe1 drückt den Knopf am anfang sofort, außerdem keine leerzeichen lassen!!!!
b2 = tk.Button(root, text = "Knopf", command=wechselFarbe2)


lab1.pack()
lab2.pack()
b.pack()
b2.pack()


root.mainloop()