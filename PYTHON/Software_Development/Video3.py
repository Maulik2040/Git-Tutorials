from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry('455x244')
# photo = PhotoImage(file='My.jpg')
#For JPG images
image = Image.open('My.JPG')
photo = ImageTk.PhotoImage(image)
Maulik = Label(image=photo)
Maulik.pack()
root.mainloop()