from PIL import Image, ImageTk
import tkinter as tk
import language
from tkinter import filedialog, SE, messagebox
def main():
    global FiltersSet
    FiltersSet = {}

    global ChangeLog

    ChangeLog = []

    languageChoose()
    createWindows()
    imageWindow.mainloop()
def createWindows():
    """
    creating window of size x,y
    """
    global imageWindow
    imageWindow = tk.Tk()
    imageWindow.title(u'StegoBox')
    menu()
    preview()
    filterWindowFunction()

def languageChoose():
    global lang
    lang = language.ru

def menu():
    m = tk.Menu(imageWindow)
    imageWindow.config(menu=m)
    """меню Файл"""
    fm = tk.Menu(m)
    m.add_cascade(label=lang[0],
                  menu=fm)
    fm.add_command(label=lang[1],
                   command=imageChoose)
    fm.add_command(label=lang[2])
    fm.add_command(label=lang[3])
    fm.add_command(label=lang[4])
    """меню фильтры"""
    filterMenu = tk.Menu(m)
    m.add_cascade(label=lang[14],
                  menu=filterMenu)
    filterMenu.add_command(label=lang[15])
    filterMenu.add_command(label=lang[16])


    """меню Помощь"""
    hm = tk.Menu(m)
    m.add_cascade(label=lang[5],
                  menu=hm)
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
        showOriginalImage()

def showOriginalImage():
    global ImageLabel,originalImage,changedImage
    if 'ImageLabel' in globals(): ImageLabel.destroy()
    originalImage = Image.open(openedPicture)
    photo = ImageTk.PhotoImage(originalImage)
    ImageLabel = tk.Label(image=photo)
    ImageLabel.image = photo
    ImageLabel.pack()
    changePreview(originalImage)
    imageWindow.mainloop()


def preview():
    global previeWindow
    previeWindow = tk.Toplevel()
    previeWindow.title(lang[17])
    previeWindow.geometry('270x180+1000+0')

def changePreview(changedImage):
    global image,showPreview
    if 'showPreview' in globals(): showPreview.destroy()
    width, height = changedImage.size
    x = 1
    success = 0
    while not success:
        if width//x<=270 and height//x<=180:
            success=1
            width = width//x
            height = height//x
        else:
            x+=1
    previewImage = changedImage.resize((width, height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(previewImage)
    showPreview = tk.Label(previeWindow,image=photo)
    showPreview.image = photo
    showPreview.pack()

def filterWindowFunction():
    """
    Window with filter options
    """

    global firstFilter

    ##################################################################
    def changeFirstFilter():
        """
        FIRST Filtet Oprions
        """
        try:
            z =(FiltersSet.get('FirstFilter')+1)%2
            FiltersSet.update({'FirstFilter':z})
        except:
            FiltersSet.update({'FirstFilter':1})

    ##################################################################



    filterWindow = tk.Toplevel(width=500)
    filterWindow.geometry('210x100+1000+0')
    filterWindow.title(lang[18])
    firstFilter = tk.Checkbutton(filterWindow,
                                     text = lang[16],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeFirstFilter
                                 )
    firstFilter.pack()

def AddPictureToChangelog(filter,image):
    global ChangeLog
    ChangeLog.append([filter,image])

def RemovePictureFromChangelog():



def ChangePicture(text_filter):
    global ChangeLog


main()