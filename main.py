import ctypes
import tkinter as tk
from tkinter import ttk
import os

class window:
    def __init__(self):

        suggestions = ['','','']

        self.root = tk.Tk()
        self.root.title("AutoCorrect Suggestions")
        self.root.geometry('400x300')
    
        frame1 = ttk.Frame(self.root)
        frame1.grid()
        
        self.menubar = tk.Menu(self.root)
        self.root.config(menu = self.menubar)

        #suggestions are the labels at the buttons at the top of the screen which suggest words which are similar the word that is currently being typed
        self.suggestion1 = ttk.Button(frame1, text='', command=self.replace(suggestions[0]))
        self.suggestion1.grid(row=0, column=0, columnspan=3)
        self.suggestion2 = ttk.Button(frame1, text='', command=self.replace(suggestions[1]))
        self.suggestion2.grid(row=0, column=3, columnspan=3)
        self.suggestion3 = ttk.Button(frame1, text='', command=self.replace(suggestions[2]))
        self.suggestion3.grid(row=0, column=6, columnspan=3)
        self.del_button = ttk.Button(frame1, text='Delete Text', command=self.delete)
        self.del_button.grid(row=0, column=9, columnspan=3)
        self.text = tk.Text(frame1, height=14, width=50)
        self.text.grid(row=1, column=0,columnspan=12)
       
        self.root.bind('<Key>',self.update)

        self.fileMenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Dictionaries", menu=self.fileMenu)
        files = os.listdir(os.getcwd()+'/Dicts')
        
        self.fileselected = tk.StringVar()
        for file in files:
            self.fileMenu.add_radiobutton(label=file, variable=self.fileselected, value = file)


        self.root.mainloop()

    def replace(self,word):
        print(word)
    
    def update(self,event):
        self.root.after(1,self._update)
    
    def _update(self):
        
        file = os.getcwd()+'/Dicts/'+self.fileselected.get()
        if self.fileselected.get()!='':
            self.filename = file
        text = self.text.get(1.0, 'end')
        if text[len(text)-2]!=' ':
            text = ''.join([letter for letter in text if letter != '\n'])
            textlist = text.split(' ')
            if textlist:
                currentword = textlist[len(textlist)-1]
                print(file)
                print(currentword)

    def delete(self):
        self.text.delete(1.0,'end')

if __name__ == "__main__":
    window()

