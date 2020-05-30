import tkinter as tk



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
    lab2 ['width'] = 5
    return


root = tk.Tk()

lab1 = tk.Label(root, text = "Hallo,")
lab2 = tk.Label(root, text = "Welt!")



## merke bg = background


b = tk.Button(root, text = "Knopf", command=wechselFarbe1)    ##command=wechselfarbe1 drückt den Knopf am anfang sofort, außerdem keine leerzeichen lassen!!!!
b2 = tk.Button(root, text = "Knopf", command=wechselFarbe2)


lab1.pack()
lab2.pack()
b.pack()
b2.pack()


root.mainloop()