from tkinter import *
root = Tk()
root.geometry('655x455')
root.title('Statusbar Tutorial')
def upload():
    statusvar.set('Busy..')
    sbar.update()
    import time
    time.sleep(5)
    statusvar.set('Ready Now')
statusvar = StringVar()
statusvar.set('Ready')
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor='w')
sbar.pack(side=BOTTOM, fill=X)
Button(root, text='Upload', command=upload).pack()
root.mainloop()