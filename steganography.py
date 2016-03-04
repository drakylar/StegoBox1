from copy import deepcopy

from PIL import Image, ImageTk
import tkinter as tk
import language,filters
from tkinter import filedialog, SE, messagebox
def main():
    global ChangeLog,FiltersSet
    FiltersSet = []
    ######rotate90######
    FiltersSet.append(0)
    ######rotate180######
    FiltersSet.append(0)
    ######sepia######
    FiltersSet.append(0)
    ######white_pix######
    FiltersSet.append(0)


    ChangeLog = []

    languageChoose()
    createWindows()

    """
    0 - rotate90
    """





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
    global ImageLabel,originalImage,changedImage,ChangeLog
    if 'ImageLabel' in globals(): ImageLabel.destroy()
    originalImage = Image.open(openedPicture)
    AddPictureToChangelog('original',originalImage)
    showImage(originalImage)
    imageWindow.mainloop()


def showImage(image):
    global ImageLabel
    photo = ImageTk.PhotoImage(image)
    if 'ImageLabel' in globals(): ImageLabel.destroy()
    ImageLabel = tk.Label(image=photo)
    ImageLabel.image = photo
    print('preview')
    ImageLabel.pack()

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

    global firstFilter,originalImage,FiltersSet,previeWindow

    ##################################################################
    def changeFirstFilter():
        global FiltersSet
        """
        FIRST Filtet Oprions
        """
        print(FiltersSet[0])
        if FiltersSet[0]==0:
                FiltersSet[0]=1
                image = filters.rotate90(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('rotate90',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[0]==1:
                FiltersSet[0]=0
                image = RemovePictureFromChangelog('rotate90')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()

    ##################################################################
    ##################################################################
    def changeSecondFilter():
        global FiltersSet
        """
        second Filtet Oprions
        """
        if FiltersSet[1]==0:
                FiltersSet[1]=1
                image = filters.rotate180(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('rotate180',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[1]==1:
                FiltersSet[1]=0
                image = RemovePictureFromChangelog('rotate180')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
    ##################################################################
    ##################################################################
    def changeThirdFilter():
        global FiltersSet
        """
        third Filter Oprions
        """
        if FiltersSet[2]==0:
                FiltersSet[2]=1
                image = filters.sepia(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('sepia',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[2]==1:
                FiltersSet[2]=0
                image = RemovePictureFromChangelog('sepia')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
    ##################################################################
    ##################################################################

    def changeFourthFilter():
        global FiltersSet
        """
        third Filter Options
        """
        if FiltersSet[3]==0:
                FiltersSet[3]=1
                image = filters.whitePixels(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('white_pix',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[3]==1:
                FiltersSet[3]=0
                image = RemovePictureFromChangelog('white_pix')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
    ##################################################################




    filterWindow = tk.Toplevel(width=500)
    filterWindow.geometry('210x100+1000+0')
    filterWindow.title(lang[18])

    ###################################################
    #                 first filter                    #
    ###################################################


    firstFilter = tk.Checkbutton(filterWindow,
                                     text = lang[15],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeFirstFilter
                                 )
    firstFilter.pack()

    ###################################################
    #                 second filter                   #
    ###################################################


    secondFilter = tk.Checkbutton(filterWindow,
                                     text = lang[16],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeSecondFilter
                                 )
    secondFilter.pack()

    ###################################################
    #                 third filter                    #
    ###################################################


    thirdFilter = tk.Checkbutton(filterWindow,
                                     text = lang[19],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeThirdFilter
                                 )
    thirdFilter.pack()

    ###################################################
    #                 fourth filter                   #
    ###################################################


    fourthFilter = tk.Checkbutton(filterWindow,
                                     text = lang[20],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeFourthFilter
                                 )
    fourthFilter.pack()



def AddPictureToChangelog(filter,image):
    global ChangeLog
    ChangeLog.append([filter,image])
    print('addchange',ChangeLog)

def RemovePictureFromChangelog(filter):
    global ChangeLog,originalImage
    cross = []
    print('removechange',filter,ChangeLog )
    for x in ChangeLog:
        if x[0]==filter: cross=x
    i = ChangeLog.index(cross)
    ChangeLog.remove(cross)
    print(i)
    print('removechange',filter,ChangeLog )
    if i == 0: startimage = originalImage
    elif i > 0: startimage = ChangeLog[i-1][1]
    print(i)
    while i<len(ChangeLog):
        if ChangeLog[i][0]=='rotate90': startimage = filters.rotate90(startimage)
        elif ChangeLog[i][0]=='rotate180': startimage = filters.rotate180(startimage)
        elif ChangeLog[i][0]=='sepia': startimage = filters.sepia(startimage)
        elif ChangeLog[i][0]=='white_pix': startimage = filters.whitePixels(startimage)
        i+=1
    return startimage





main()