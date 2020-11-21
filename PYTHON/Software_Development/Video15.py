from tkinter import *
root = Tk()
root.geometry('655x455')
root.title('Scrollbar Tutorial')
#For Connecting Scrollbar To Widget
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f'Item {i}') 
# listbox.pack()

text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)

scrollbar.config(command=text.yview)

root.mainloop()