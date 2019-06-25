from tkinter import Tk, Frame, Button
import os
import glob

root = Tk()

framePhoto = Frame(root, bg='gray50', width=800, height=600, bd=4)

prevBtn = Button(self.framePhoto, text='Previous', command=lambda s= s.getImgOpen('prev'),bg='blue', fg='red')
prevBtn.place(relx=0.85, rely=0.99, anchor=SE)


nextBtn = Button(self.framePhoto, text='Next', command=lambda s= s.getImgOpen('next'),
                bg='green', fg='black')
nextBtn.place(relx=0.90, rely=0.99, anchor=SE)


def getImgList(self, path, ext):
    imgList = [os.path.normcase(f) for f in os.listdir(path)]
    imgList = [os.path.join(path, f) for f in imgList if os.path.splitext(f)[1] == ext]
    self.images.extend(imgList)

def getImgOpen(self, seq):
    print
    'Opening %s' % seq
    if seq == 'ZERO':
        self.imgIndex = 0
    elif (seq == 'prev'):
        if (self.imgIndex == 0):
            self.imgIndex = len(self.images) - 1
        else:
            self.imgIndex -= 1
    elif (seq == 'next'):
        if (self.imgIndex == len(self.images) - 1):
            self.imgIndex = 0
        else:
            self.imgIndex += 1

    self.masterImg = Image.open(self.images[self.imgIndex])
    self.master.title(self.images[self.imgIndex])
    self.masterImg.thumbnail((400, 400))
    self.img = ImageTk.PhotoImage(self.masterImg)
    self.lbl['image'] = self.img
    return