from PIL import Image, ImageTk
import tkinter as tk
import time
from tkinter import filedialog, SE, messagebox

root = tk.Tk()

def alert(text):
    messagebox.showinfo(text, text)
    root.mainloop()


firstFilter = tk.Checkbutton(root,
                                     text = '11111',
                                     onvalue = 1,
                                     offvalue = 0,
                                     height = 21,
                                     width = 168,
                                     command = alert('1234')
                                 )


root.mainloop()




"""
image = Image.open("/Users/iljashaposhnikov/Desktop/python/Steganogaphy/test/large.jpg")
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=photo)
label.image = photo # keep a reference!
label.pack()"""