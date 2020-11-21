from tkinter import *
root = Tk()
root.title('Maulik Ka GUI')
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
#The line goes from the point x1, y1, x2, y2
# can_widget.create_line(0, 0, 800, 400, fill='red')
# can_widget.create_line(0, 400, 800, 0, fill='red')
#To Creat a rectanglt specify parameters in this order = cors of top and cors of bottom right
# can_widget.create_rectangle(3, 5, 700, 300, fill='blue')
#This widget of canvas creates text
# can_widget.create_text(200, 200, text='Python')

can_widget.create_oval(3, 5, 700, 300, fill='blue')
root.mainloop()