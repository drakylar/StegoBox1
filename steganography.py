from copy import deepcopy

from PIL import Image, ImageTk
import tkinter as tk
import language,filters,time
from tkinter import filedialog, SE, messagebox


def main():
    createVaribles()

    languageChoose()
    createWindows()

    """
    0 - rotate90
    """





    imageWindow.mainloop()

def createVaribles():
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

    ######invert######
    FiltersSet.append(0)

    ######red0######
    FiltersSet.append(0)
    ######red1######
    FiltersSet.append(0)
    ######red2######
    FiltersSet.append(0)
    ######red3######
    FiltersSet.append(0)
    ######red4######
    FiltersSet.append(0)
    ######red5######
    FiltersSet.append(0)
    ######red6######
    FiltersSet.append(0)
    ######red7######
    FiltersSet.append(0)

    ######green0######
    FiltersSet.append(0)
    ######green1######
    FiltersSet.append(0)
    ######green2######
    FiltersSet.append(0)
    ######green3######
    FiltersSet.append(0)
    ######green4######
    FiltersSet.append(0)
    ######green5######
    FiltersSet.append(0)
    ######green6######
    FiltersSet.append(0)
    ######green7######
    FiltersSet.append(0)


    ######blue0######
    FiltersSet.append(0)
    ######blue1######
    FiltersSet.append(0)
    ######blue2######
    FiltersSet.append(0)
    ######blue3######
    FiltersSet.append(0)
    ######blue4######
    FiltersSet.append(0)
    ######blue5######
    FiltersSet.append(0)
    ######blue6######
    FiltersSet.append(0)
    ######blue7######
    FiltersSet.append(0)

    ######edge######
    FiltersSet.append(0)

    ######contour######
    FiltersSet.append(0)


    ChangeLog = []

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
    fileHeaderWindow()

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
    fm.add_command(label=lang[3],command=imageSave)
    fm.add_command(label=lang[4], command=exit)
    """меню фильтры"""
    """filterMenu = tk.Menu(m)
    m.add_cascade(label=lang[14],
                  menu=filterMenu)
    filterMenu.add_command(label=lang[15])
    filterMenu.add_command(label=lang[16])"""


    """меню Помощь"""
    hm = tk.Menu(m)
    m.add_cascade(label=lang[5],
                  menu=hm)
    hm.add_command(label=lang[6])
    hm.add_command(label=lang[7])


def imageChoose():
    global openedPicture,ImageLabel,originalImage, ChangeLog, filterWindow,REDWindow
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
        originalImage = Image.open(openedPicture)
        createVaribles()
        filterWindow.destroy()
        filterWindowFunction()
        if 'REDWindow' in globals():REDWindow.destroy()
        AddPictureToChangelog('original',deepcopy(originalImage))
        showImage(originalImage)
        changePreview(originalImage)
        ImageLabel.mainloop()

def imageSave():
    global ChangeLog
    f = filedialog.asksaveasfile(mode='a', defaultextension=".png",title = lang[35])
    if f is None: return
    image = ChangeLog[len(ChangeLog)-1][1]
    image.save(f.name)
    print(f)

def showImage(image):
    global ImageLabel
    photo = ImageTk.PhotoImage(image)
    if 'ImageLabel' in globals(): ImageLabel.destroy()
    ImageLabel = tk.Label(image=photo)
    ImageLabel.image = photo
    ImageLabel.pack()

def preview():
    global previeWindow
    previeWindow = tk.Toplevel()
    previeWindow.title(lang[17])
    #previeWindow.geometry('270x180+1000+0')

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

    global firstFilter,originalImage,FiltersSet,previeWindow,filterWindow

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
    ##################################################################

    def changeFifthFilter():
        global FiltersSet
        """
        third Filter Options
        """
        if FiltersSet[4]==0:
                FiltersSet[4]=1
                image = filters.invert(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('invert',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[4]==1:
                FiltersSet[4]=0
                image = RemovePictureFromChangelog('invert')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
    ##################################################################
    ##################################################################

    def changeSixthFilter1():
        global FiltersSet
        """
        third Filter Options
        """
        if FiltersSet[4]==0:
                FiltersSet[4]=1
                image = filters.invert(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('invert',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[4]==1:
                FiltersSet[4]=0
                image = RemovePictureFromChangelog('invert')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
    ##################################################################
    ##################################################################

    def changeSeventhFilter():
        global FiltersSet
        """
        third Filter Options
        """
        if FiltersSet[29]==0:
                FiltersSet[29]=1
                image = filters.edge(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('edge',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[29]==1:
                FiltersSet[29]=0
                image = RemovePictureFromChangelog('edge')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
    ##################################################################
    ##################################################################

    def changeEighthFilter():
        global FiltersSet
        """
        third Filter Options
        """
        if FiltersSet[30]==0:
                FiltersSet[30]=1
                image = filters.contour(deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                AddPictureToChangelog('contour',image)
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
        elif FiltersSet[30]==1:
                FiltersSet[30]=0
                image = RemovePictureFromChangelog('contour')
                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()
    ##################################################################



    filterWindow = tk.Toplevel(width=500)
    filterWindow.geometry('210x300+1000+400')
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

    ###################################################
    #                  fifth filter                   #
    ###################################################


    fifthFilter = tk.Checkbutton(filterWindow,
                                     text = lang[21],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeFifthFilter
                                 )
    fifthFilter.pack()

    ###################################################
    #                  sixth filter                   #
    ###################################################

    sixthFilter = tk.Button(filterWindow, text=lang[22], command = REDWindows )
    sixthFilter.pack()

    ###################################################
    #                  seventh filter                 #
    ###################################################


    seventhFilter = tk.Checkbutton(filterWindow,
                                     text = lang[33],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeSeventhFilter
                                 )
    seventhFilter.pack()

    ###################################################
    #                  eighth filter                  #
    ###################################################


    eighthFilter = tk.Checkbutton(filterWindow,
                                     text = lang[34],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = changeEighthFilter
                                 )
    eighthFilter.pack()

def AddPictureToChangelog(filter,image):
    global ChangeLog

    if filter[:3]=='colorShow':
        plane=filter.split(':')[1]
        z = 0
        success=0
        while z<len(ChangeLog):
            if ChangeLog[z][0][:9]=='colorShow':
                success=1
                ChangeLog[z][0]+=':'+plane+':'
            z+=1
        if not success:
            ChangeLog.append([filter,image])
            print('addchange',ChangeLog)

    else:
        ChangeLog.append([filter,image])
        print('addchange',ChangeLog)

def RemovePictureFromChangelog(filter):
    global ChangeLog,originalImage,imageWindow,previeWindow

    #fail#

    cross = []


    print('removechange',filter,ChangeLog )


    if filter[:9]=='colorShow':

        #fail#

        plane  = filter.split(':')[1]
        i = 0
        number = 0
        for x in ChangeLog:
            if 'colorShow' in x[0]:
                cross=x
                number = i
            i+=1
        x = number-1

        #fail#

        n = ChangeLog[number][0]
        print('n',n)
        k = n.replace(':'+plane+':',':').replace(':'+plane,':').replace(':','')
        print('k',k)
        if k.replace(':','')=='colorShow':
            print('to remove',ChangeLog[number])
            ChangeLog.remove(ChangeLog[number])
        else:
            ChangeLog[number][0] = n.replace(':'+plane+':',':').replace(':'+plane,':').replace('::',':')
            print(ChangeLog[number][0])


        print('removed1',ChangeLog)
    else:

        for m in ChangeLog:
            if m[0]==filter: cross=m
        x = ChangeLog.index(cross)-1
        ChangeLog.remove(cross)
        print('removed2',ChangeLog)



    ChangeLog[0][1] =deepcopy(originalImage)
    if x == 0: startimage = deepcopy(originalImage)
    elif x > 0: startimage = ChangeLog[x-1][1]

    if len(ChangeLog)>1:

        while x<len(ChangeLog):
            if ChangeLog[x][0]=='rotate90': startimage = filters.rotate90(deepcopy(startimage))
            elif ChangeLog[x][0]=='rotate180': startimage = filters.rotate180(deepcopy(startimage))
            elif ChangeLog[x][0]=='sepia': startimage = filters.sepia(deepcopy(startimage))
            elif ChangeLog[x][0]=='white_pix': startimage = filters.whitePixels(deepcopy(startimage))
            elif ChangeLog[x][0]=='invert': startimage = filters.invert(deepcopy(startimage))
            elif ChangeLog[x][0]=='edge': startimage = filters.edge(deepcopy(startimage))
            elif ChangeLog[x][0]=='contour': startimage = filters.contour(deepcopy(startimage))
            elif ChangeLog[x][0][0:9]=='colorShow':
                startimage = filters.colorShow(startimage,ChangeLog[x][0][9:].replace('::',':'))
            ChangeLog[x][1]=deepcopy(startimage)
            x+=1
    print('start',startimage)
    return startimage


def REDWindows():
    global REDWindow,originalImage
    REDWindow = tk.Toplevel()
    REDWindow.title(lang[22])
    REDWindow.geometry('300x220+1000+0')



    ##################################################################

    def RED(plane):
            global FiltersSet,ChangeLog,originalImage



            if FiltersSet[5+plane]==0:

                ##success##

                FiltersSet[5+plane]=1

                z = 0
                success = 0
                while z<len(ChangeLog):
                    fil = ChangeLog[z]
                    if 'colorShow:' in fil[0]:
                        ChangeLog[z][0]=(ChangeLog[z][0]+':'+str(plane)+':').replace('::',':')
                        success = 1
                        x = z
                        startimage = deepcopy(ChangeLog[z-1][1])
                        z = len(ChangeLog)
                    z+=1
                if success:
                    if x == 0: startimage = deepcopy(originalImage)
                    while x<len(ChangeLog):
                        if ChangeLog[x][0]=='rotate90': startimage = filters.rotate90(deepcopy(startimage))
                        elif ChangeLog[x][0]=='rotate180': startimage = filters.rotate180(deepcopy(startimage))
                        elif ChangeLog[x][0]=='sepia': startimage = filters.sepia(deepcopy(startimage))
                        elif ChangeLog[x][0]=='white_pix': startimage = filters.whitePixels(deepcopy(startimage))
                        elif ChangeLog[x][0]=='invert': startimage = filters.invert(deepcopy(startimage))
                        elif ChangeLog[x][0]=='edge': startimage = filters.edge(deepcopy(startimage))
                        elif ChangeLog[x][0]=='contour': startimage = filters.contour(deepcopy(startimage))
                        elif ChangeLog[x][0][0:9]=='colorShow':
                            startimage = filters.colorShow(startimage,ChangeLog[x][0][9:].replace('::',':'))
                        ChangeLog[x][1]=deepcopy(startimage)
                        x+=1
                if not success:

                    AddPictureToChangelog('colorShow:'+str(plane),deepcopy(ChangeLog[len(ChangeLog)-1][1]))
                    x = len(ChangeLog)-2
                    ChangeLog[0][1] = deepcopy(originalImage)
                    if x == 0: startimage = deepcopy(originalImage)
                    elif x > 0: startimage = ChangeLog[x-1][1]

                    while x<len(ChangeLog):
                        if ChangeLog[x][0]=='rotate90': startimage = filters.rotate90(deepcopy(startimage))
                        elif ChangeLog[x][0]=='rotate180': startimage = filters.rotate180(deepcopy(startimage))
                        elif ChangeLog[x][0]=='sepia': startimage = filters.sepia(deepcopy(startimage))
                        elif ChangeLog[x][0]=='white_pix': startimage = filters.whitePixels(deepcopy(startimage))
                        elif ChangeLog[x][0]=='invert': startimage = filters.invert(deepcopy(startimage))
                        elif ChangeLog[x][0]=='edge': startimage = filters.edge(deepcopy(startimage))
                        elif ChangeLog[x][0]=='contour': startimage = filters.contour(deepcopy(startimage))
                        elif ChangeLog[x][0][0:9]=='colorShow':
                            startimage = filters.colorShow(startimage,ChangeLog[x][0][9:].replace('::',':'))
                        ChangeLog[x][1]=deepcopy(startimage)
                        x+=1


                showImage(startimage)
                changePreview(startimage)
                previeWindow.mainloop()
                imageWindow.mainloop()
                ##success##

            elif FiltersSet[5+plane]==1:
                ##fail##

                FiltersSet[5+plane]=0

                image = RemovePictureFromChangelog('colorShow:'+str(plane))


                print('orign',image)


                showImage(image)
                changePreview(image)
                previeWindow.mainloop()
                imageWindow.mainloop()


    REDtext = tk.Label(REDWindow,text=lang[22])
    REDtext.grid(row = 1, column = 1)

    RED0 = tk.Checkbutton(REDWindow,
                                     text = lang[23],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(7)
                                 )
    RED0.grid(row = 2, column = 1)

    RED1 = tk.Checkbutton(REDWindow,
                                     text = lang[24],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(6)
                                 )
    RED1.grid(row = 3, column = 1)

    RED2 = tk.Checkbutton(REDWindow,
                                     text = lang[25],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(5)
                                 )
    RED2.grid(row = 4, column = 1)

    RED3 = tk.Checkbutton(REDWindow,
                                     text = lang[26],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(4)
                                 )
    RED3.grid(row = 5, column = 1)

    RED4 = tk.Checkbutton(REDWindow,
                                     text = lang[27],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(3)
                                 )
    RED4.grid(row =6, column = 1)

    RED5 = tk.Checkbutton(REDWindow,
                                     text = lang[28],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(2)
                                 )
    RED5.grid(row = 7, column = 1)

    RED6 = tk.Checkbutton(REDWindow,
                                     text = lang[29],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(1)
                                 )
    RED6.grid(row = 8, column = 1)

    RED7 = tk.Checkbutton(REDWindow,
                                     text = lang[30],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(0)
                                 )
    RED7.grid(row = 9, column = 1)




    GREENtext = tk.Label(REDWindow,text=lang[31])
    GREENtext.grid(row = 1, column = 2)

    GREEN0 = tk.Checkbutton(REDWindow,
                                     text = lang[23],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(15)
                                 )
    GREEN0.grid(row = 2, column = 2)

    GREEN1 = tk.Checkbutton(REDWindow,
                                     text = lang[24],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(14)
                                 )
    GREEN1.grid(row = 3, column = 2)

    GREEN2 = tk.Checkbutton(REDWindow,
                                     text = lang[25],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(13)
                                 )
    GREEN2.grid(row = 4, column = 2)

    GREEN3 = tk.Checkbutton(REDWindow,
                                     text = lang[26],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(12)
                                 )
    GREEN3.grid(row = 5, column = 2)

    GREEN4 = tk.Checkbutton(REDWindow,
                                     text = lang[27],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(11)
                                 )
    GREEN4.grid(row =6, column = 2)

    GREEN5 = tk.Checkbutton(REDWindow,
                                     text = lang[28],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(10)
                                 )
    GREEN5.grid(row = 7, column = 2)

    GREEN6 = tk.Checkbutton(REDWindow,
                                     text = lang[29],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(9)
                                 )
    GREEN6.grid(row = 8, column = 2)

    GREEN7 = tk.Checkbutton(REDWindow,
                                     text = lang[30],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(8)
                                 )
    GREEN7.grid(row = 9, column = 2)



    BLUEtext = tk.Label(REDWindow,text=lang[32])
    BLUEtext.grid(row = 1, column = 3)

    BLUE0 = tk.Checkbutton(REDWindow,
                                     text = lang[23],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(23)
                                 )
    BLUE0.grid(row = 2, column = 3)

    BLUE1 = tk.Checkbutton(REDWindow,
                                     text = lang[24],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(22)
                                 )
    BLUE1.grid(row = 3, column = 3)

    BLUE2 = tk.Checkbutton(REDWindow,
                                     text = lang[25],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(21)
                                 )
    BLUE2.grid(row = 4, column = 3)

    BLUE3 = tk.Checkbutton(REDWindow,
                                     text = lang[26],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(20)
                                 )
    BLUE3.grid(row = 5, column = 3)

    BLUE4 = tk.Checkbutton(REDWindow,
                                     text = lang[27],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(19)
                                 )
    BLUE4.grid(row =6, column = 3)

    BLUE5 = tk.Checkbutton(REDWindow,
                                     text = lang[28],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(18)
                                 )
    BLUE5.grid(row = 7, column = 3)

    BLUE6 = tk.Checkbutton(REDWindow,
                                     text = lang[29],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(17)
                                 )
    BLUE6.grid(row = 8, column = 3)

    BLUE7 = tk.Checkbutton(REDWindow,
                                     text = lang[30],
                                     onvalue = 1,
                                     offvalue = 0,
                                     command = lambda: RED(16)
                                 )
    BLUE7.grid(row = 9, column = 3)

def fileHeaderWindow():
    fileWindow = tk.Toplevel()
    fileWindow.title(lang[36])
    fileWindow.geometry('200x300+1000+0')
    print('fileheader')

main()