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
    lab1['image'] = img3
    return

def wechselFarbe2():
    lab2['bg'] = '#000000'
    lab2['fg'] = '#FFFFFF'
    lab2['font'] = 'Courier 12 bold'
    lab2['height'] = 1
    lab2['width'] = 5
    lab1['image'] = img2
    return



root = tk.Tk()

img1 = ImageTk.PhotoImage(Image.open("bild1.png"))
img2 = ImageTk.PhotoImage(Image.open("bild2.png"))
img3 = ImageTk.PhotoImage(Image.open("bild3.png"))
img4 = ImageTk.PhotoImage(Image.open("bild4.png"))

frame1 = tk.Frame(root)
lab1 = tk.Label(root, image=img3)
lab2 = tk.Label(root, text = "Welt!")



## merke bg = background


b = tk.Button(frame1, text='knopfx', command=wechselFarbe1)    ##command=wechselfarbe1 drückt den Knopf am anfang sofort, außerdem keine leerzeichen lassen!!
b2 = tk.Button(frame1, text = "Knopf", command=wechselFarbe2)
b3 = tk.Button(frame1, text = "Knopf1")
b4 = tk.Button(frame1, text = "Knopf2")
b5 = tk.Button(frame1, text = "Knopf3")


lab1.pack()
lab2.pack()
frame1.pack()
b.pack(side='left')
b2.pack(side='left')
b3.pack(side='left')
b4.pack(side='left')
b5.pack(side='left')

root.mainloop()