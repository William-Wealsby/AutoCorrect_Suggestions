import ctypes
import tkinter as tk
from tkinter import ttk
import os

class window:
    def __init__(self):

        self.suggestions = ['','','']

        self.root = tk.Tk()
        self.root.title("AutoCorrect Suggestions")
        self.root.geometry('400x300')
    
        frame1 = ttk.Frame(self.root)
        frame1.grid()
        
        self.menubar = tk.Menu(self.root)
        self.root.config(menu = self.menubar)

        #suggestions are the labels at the buttons at the top of the screen which suggest words which are similar the word that is currently being typed 
        self.text = tk.Text(frame1, height=14, width=48)
        self.suggestion1 = ttk.Button(frame1, text='', command=lambda:self.replace(self.suggestions[0]))
        self.suggestion1.grid(row=0, column=0, columnspan=3)
        self.suggestion2 = ttk.Button(frame1, text='', command=lambda:self.replace(self.suggestions[1]))
        self.suggestion2.grid(row=0, column=3, columnspan=3)
        self.suggestion3 = ttk.Button(frame1, text='', command=lambda:self.replace(self.suggestions[2]))
        self.suggestion3.grid(row=0, column=6, columnspan=3)
        self.del_button = ttk.Button(frame1, text='Delete Text', command=self.delete)
        self.del_button.grid(row=0, column=9, columnspan=3)
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
        text = self.text.get(1.0, 'end')
        text = ''.join([letter for letter in text if letter != '\n'])
        textlist = text.split(' ')
        textlist[len(textlist)-1] = word
        text = ' '.join(textlist)
        self.text.delete(1.0,'end')
        self.text.insert(1.0,text)
    
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
                self.search(currentword)
                self.suggestion1.config(text=self.suggestions[0])
                self.suggestion2.config(text=self.suggestions[1])
                self.suggestion3.config(text=self.suggestions[2])

                
    def search(self,word):
        # create 1 buffers for 3 strings, 61 length characters long (20 letters max each and the return character)
        c_string = 

        self.suggestions = ['three','test','words']

    def delete(self):
        self.text.delete(1.0,'end')

if __name__ == "__main__":
    window()

