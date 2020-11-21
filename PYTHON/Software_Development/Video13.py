from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('633x455')
root.title('Radiobutton Tutorial')
def Order():
    tmsg.showinfo('Order Status', f'Your Ordering of {var.get()} has been taken place on 19 August 2020')
var = StringVar()
var.set('Radio')
Label(root, text='What would you like to eat sir?', justify=LEFT, padx=14, font='lucida 16 bold').pack()
radio = Radiobutton(root, text='Dosa', padx=14, variable=var, value='Dosa').pack(anchor='w')
radio = Radiobutton(root, text='Paratha', padx=14, variable=var, value=2).pack(anchor='w')
radio = Radiobutton(root, text='Samosa', padx=14, variable=var, value=3).pack(anchor='w')
radio = Radiobutton(root, text='Vada Pav', padx=14, variable=var, value=4).pack(anchor='w')
radio = Radiobutton(root, text='Poha', padx=14, variable=var, value=5).pack(anchor='w')
Button(root, text='Order Now', command=Order).pack()
root.mainloop()