from tkinter import *
root = Tk()
root.geometry('655x333')
def getvals():
    print(f'The value of username is: {userentry.get()}')
    print(f'The value of pasword is: {passentry.get()}')
user = Label(root, text='Username')
password = Label(root, text='Password')
user.grid()
password.grid(rows=1)
#Variable Classes in tkinter
#BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passvalue = StringVar()
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button = Button(text='Submit', command=getvals)
Button.grid(row=2, column=1)
root.mainloop()