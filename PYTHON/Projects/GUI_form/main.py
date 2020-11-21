from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("655x455")
root.title("Entry To Database")
#Form Start
def submit_value():
    first_name = first_nameentryval.get()
    last_name = last_nameentryval.get()
    email = emailentryval.get()
    password = passwordentryval.get()
    tmsg.showinfo("Information", "Value Submitted Successfully")
blank = Label(text="").grid()
first_nameentryval = StringVar()
first_name = Label(text="First Name").grid(row=1, column=1)
first_nameentry = Entry(textvariable=first_nameentryval).grid(row=1, column=2)

last_nameentryval = StringVar()
last_name = Label(text="Last Name").grid(row=2, column=1)
last_nameentry = Entry(textvariable=last_nameentryval).grid(row=2, column=2)

emailentryval = StringVar()
email = Label(text="Email").grid(row=3, column=1)
emailentry = Entry(textvariable=emailentryval).grid(row=3, column=2)

passwordentryval = StringVar()
password = Label(text="Pasword").grid(row=4, column=1)
passwordentry = Entry(textvariable=passwordentryval).grid(row=4, column=2)

submit_button = Button(text="Submit", command=submit_value).grid(row=5, column=2)
root.mainloop()