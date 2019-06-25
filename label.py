from tkinter import filedialog, Tk,Label
from tkinter import Button
from PIL import Image, ImageTk
import os
import glob
import shutil

def func1():
    shutil.copy(next(li),'C:/Users/신은성/Downloads/7')
    next_img()
def func2():
    shutil.copy(next(li),'C:/Users/신은성/Downloads/8')
    next_img()

root = Tk()
root.geometry('800x800')
root.resizable(0,0)
panel=Label(root)
panel.pack()
# path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
path=filedialog.askdirectory()

li=iter(glob.glob(os.path.join(path, '*')))
def next_img():
    try:
        img = next(li)  # get the next image from the iterator
    except StopIteration:
        return  # if there are no more images, do nothing

    # load the image and display it
    img = Image.open(img)
    img=img.resize((500,500),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.img = img  # keep a reference so it's not garbage collected
    panel['image'] = img

btn = Button(root,text='Next image', command=next_img)
btn.pack()
button1=Button(root, overrelief='solid',width=15, command=func1,text='수리중:7')
button2=Button(root, overrelief='solid',width=15, command=func2,text='저품질:8')
# button3=Button(root,  overrelief='solid',width=15, command=nxt(li),text='다  음')
button1.pack()
button2.pack()
# im = Image.open(nxt(li))
# tkimage = ImageTk.PhotoImage(im)
# myvar=Label(root,image = tkimage)
# myvar.image = tkimage
# myvar.pack(side='left')


root.mainloop()


if __name__=='__main__':
    None