from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Hình ảnh')
        self.pack(fill=BOTH, expand=1)
        Style().configure('TFrame',background='#333')
        pexel = Image.open('C:\\Users\\khanh\\OneDrive\\Hình ảnh\\Saved Pictures\\pexel1.jpg')
        pexel = pexel.resize((100,100),Image.BILINEAR)
        pexel1 = ImageTk.PhotoImage(pexel)
        label1 = Label(self, image=pexel1)
        label1.image = pexel1
        label1.place(x=20,y=20)


root = Tk()
root.geometry('400x280+400+300')
app = Example(root)
root.mainloop()