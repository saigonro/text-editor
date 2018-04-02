from Tkinter import * 
import tkFileDialog

class Files(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title('SimpleTextEditor')
        self.pack(fill = BOTH, expand = 1)

        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label = 'Save', command = self.save_command)
        fileMenu.add_command(label = 'Open', command = self.onOpen)
        menubar.add_cascade(label = 'File', menu = fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill = BOTH, expand = 1)


    def onOpen(self):

        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text

    def save_command(self):
        file = tkFileDialog.asksaveasfile(mode = 'w')
        if file != None:
                data = self.txt.get('1.0', END+'-1c')
                file.write(data)
                file.close()


root = Tk()

top = Frame(root)
top.pack(fill = BOTH, expand = 1)

bottom = Frame(root)
bottom.pack()

ex = Files(root)
ex.pack(side = 'bottom')

root.geometry("600x600+100+100")
root.mainloop()
