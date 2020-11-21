from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('733x566')
filemenubar = Menu(root)
def Print():
    print('This is an example of printing')
def help():
    tmsg.showinfo('Help', 'Maulik will Help you with this GUI')
def rate():
    tmsg.showwarning('Maulik, Thappad Khayega')
m1 = Menu(filemenubar, tearoff=0)
m1.add_command(label='Save Project', command=Print)
m1.add_command(label='New Project', command=Print)
m1.add_command(label='Open Project', command=Print)
m1.add_command(label='New', command=Print)
m1.add_command(label='Save Project as', command=Print)
root.config(menu=filemenubar)
filemenubar.add_cascade(label='Edit', menu=m1)

m1 = Menu(filemenubar, tearoff=0)
m1.add_command(label='Save Project', command=rate)
m1.add_command(label='New Project', command=help)
m1.add_command(label='Open Project', command=help)
m1.add_command(label='New', command=help)
m1.add_command(label='Save Project as', command=help)
root.config(menu=filemenubar)
filemenubar.add_cascade(label='Help', menu=m1)
root.mainloop()