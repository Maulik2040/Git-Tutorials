from tkinter import *
root = Tk()
root.geometry('633x455')
root.title('Listbox Tutorial')
def add():
    global i
    lbx.insert(ACTIVE, f'{i}')
    i+=1
i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, 'First Item of our List Box')
Button(root, text='Add Item', command=add).pack()
root.mainloop()