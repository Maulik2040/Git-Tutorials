from tkinter import *
root = Tk()
root.title('My GUI with Harry')
#Important Label Options
# text = adds the text
# bd = background
# fg = foreground
# font = sets the font
# padx = x_padding
# pady = y_paddign
# relief = borde_styling = SUNKEN, RAISED, GROOVE, RIDGE
text_label = Label(text = 'Wikipedia began with its first \nedit on 15 January 2001, two days after the domain was registered[2] by Jimmy \nWales and Larry Sanger. Its technological and conceptual', bg="red", fg='white', padx=10, pady=14, font='comicsansms 19 bold', borderwidth=3, relief=SUNKEN)
#Important Pack Options
#side = top, bottom, left, right
#fill
#padx
#pady
text_label.pack(side=BOTTOM, anchor="sw", fill=Y)
root.mainloop()