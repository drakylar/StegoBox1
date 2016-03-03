from PIL import Image, ImageTk
import tkinter as tk
import time

root = tk.Tk()

leftButton = tk.Button(root, text="<--<", height=32, width=32, anchor=tk.SE)



root.mainloop()




"""
image = Image.open("/Users/iljashaposhnikov/Desktop/python/Steganogaphy/test/large.jpg")
photo = ImageTk.PhotoImage(image)
label = tk.Label(image=photo)
label.image = photo # keep a reference!
label.pack()"""