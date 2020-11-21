from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('455x233')
root.title('Slider Tutorial')
# myslider = Scale(root, from_=0, to=455)
# myslider.pack()
def getdollar():
    tmsg.showinfo('Good News', f'We have credited {myslider2.get()} dollars to your account')
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(34)
myslider2.pack()
Label(root, text='How many dollars do you want').pack()
Button(root, text='Get Dollars!', command=getdollar, font='comicsansms').pack()
root.mainloop()