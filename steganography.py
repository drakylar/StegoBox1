from PIL import Image, ImageTk
import tkinter as tk
import language
from tkinter import filedialog
def main():
    languageChoose()
    createWindows()
    root.mainloop()

def createWindows():
    """
    creating window of size x,y
    """
    global root
    root = tk.Tk()
    menu()

def languageChoose():
    global lang
    lang = language.ru

def menu():
    m = tk.Menu(root)
    root.config(menu=m)
    """меню Файл"""
    fm = tk.Menu(m)
    m.add_cascade(label=lang[0],menu=fm)
    fm.add_command(label=lang[1], command=imageChoose)
    fm.add_command(label=lang[2])
    fm.add_command(label=lang[3])
    fm.add_command(label=lang[4])
    """меню Помощь"""
    hm = tk.Menu(m)
    m.add_cascade(label=lang[5],menu=hm)
    hm.add_command(label=lang[6])
    hm.add_command(label=lang[7])


def imageChoose():
    global openedPicture
    print(lang[13])
    filename = filedialog.askopenfile(title = lang[8],filetypes = ((lang[9],"*.jpg"),
                                                                   (lang[10],"*.png"),
                                                                   (lang[11],"*.gif"),
                                                                   (lang[12],"*.bmp"),
                                                                   (lang[13],"*.*"))
                                      )
    print(filename,filename.name)
    images = ["bmp","png","jpg","gif"]
    if filename.name.lower()[-3:] in images:
        openedPicture = filename.name
        showImage()

def showImage():
    global ImageLabel
    if 'ImageLabel' in globals(): ImageLabel.destroy()
    image = Image.open(openedPicture)
    photo = ImageTk.PhotoImage(image)
    ImageLabel = tk.Label(image=photo)
    ImageLabel.image = photo
    ImageLabel.pack()
    root.mainloop()


main()