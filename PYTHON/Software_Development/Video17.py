from tkinter import *
class GUI(Tk):
    def __int__(self):
        super().__init__()
        self.geometry('744x377')
    def status(self):
        self.var = StringVar()
        self.var.set('Ready')
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor='w')
        self.statusbar.pack(side=BOTTOM, fill=X)
    def click(self):
        print('Button Clicked')
    def createbutton(self, text):
        Button(text=text, command=self.click).pack()
if __name__ == '__main__':
    window = GUI()        
    window.status()
    window.createbutton('Click Me')
    window.mainloop()
    