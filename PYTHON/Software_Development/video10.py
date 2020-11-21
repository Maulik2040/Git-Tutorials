from tkinter import *
root = Tk()
root.geometry('733x566')
root.title('Pycharm')
def myfunc():
    print('My name is Maulik Mishra')
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

fileenbar = Menu(root)
m1 = Menu(fileenbar, tearoff=0)
m1.add_command(label='New Project', command=myfunc)
m1.add_command(label='Save As', command=myfunc)
m1.add_separator()
m1.add_command(label='Print', command=myfunc)

root.config(menu=fileenbar)
fileenbar.add_cascade(label='File', menu=m1)

mainenbar = Menu(root)
m2 = Menu(fileenbar, tearoff=0)
m2.add_command(label='New Project', command=myfunc)
m2.add_command(label='Save As', command=myfunc)
m2.add_separator()
m2.add_command(label='Print', command=myfunc)

root.config(menu=fileenbar)
mainenbar.add_cascade(label='Edit2', menu=m1)

root.mainloop()