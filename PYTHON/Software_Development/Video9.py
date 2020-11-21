from tkinter import *
root = Tk()
root.title('Events in Tkinter')
def Maulik(event):
    print(f'You clicked on the button at {event.x}, {event.y}')
root.geometry('644x334')
widget = Button(root, text = 'Click Me Please', bg="grey", fg='white')
widget.pack()

widget.bind('<Button-1>', Maulik)
widget.bind('<Double-1>', quit)
root.mainloop()