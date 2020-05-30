import tkinter as tk
from PIL import  ImageTk, Image


##Kleber für Elemente z.B. labels
##columnspan/rowspan um elemente über mehreren zellen zu haben

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

def gebeStr():
    lab5['text'] = eingabe.get()
    return


# ------------------ Hauptfenster initialisieren -----------------------
root = tk.Tk()

img1 = ImageTk.PhotoImage(Image.open("bild1.png"))
img2 = ImageTk.PhotoImage(Image.open("bild2.png"))
img3 = ImageTk.PhotoImage(Image.open("bild3.png"))
img4 = ImageTk.PhotoImage(Image.open("bild4.png"))

frame1 = tk.Frame(root)

eingabe = tk.Entry(root, width=20)
lab1 = tk.Label(root, text='testKnopf', width=20)
lab2 = tk.Label(root, text = "Hallo")
lab3 = tk.Label(root, text = "Welt!")
lab4 = tk.Label(root, text = "Was wir so können:", bg='#00FFFF')
lab5 = tk.Label(root, text = "Was wir so alles machen!", bg='#FF3300')
## merke bg = background


b = tk.Button(frame1, text='knopfx', command=wechselFarbe1)    ##command=wechselfarbe1 drückt den Knopf am anfang sofort, außerdem keine leerzeichen lassen!!
b2 = tk.Button(frame1, text = "Knopf", command=wechselFarbe2)
b3 = tk.Button(frame1, text = "Knopf1", command=gebeStr)
b4 = tk.Button(frame1, text = "Knopf2")
b5 = tk.Button(frame1, text = "Knopf3")




# ----------------- Widgets platzieren -----------------------
lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1, sticky='e')
lab3.grid(row=0, column=2, sticky='w')
lab4.grid(row=1, column=1)
lab5.grid(row=1, column=2, sticky='w')


eingabe.grid(row=1, column=0)

frame1.grid(row=2, column=1, columnspan=2, sticky='e')
b.pack(side='left')
b2.pack(side='left')
b3.pack(side='left')
b4.pack(side='left')
b5.pack(side='left')

root.mainloop()