from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


class TextEditor:
    def __init__(self, master) -> None:
        self.master = master
        self.master.title('Text Editor')
        # self.master.resizable(False,False)
        self.master.rowconfigure(0,minsize=800,weight=1)
        self.master.columnconfigure(1,minsize=800,weight=1)
        self.text_editor = Text(self.master, font=('Arial', '10'))
        self.text_editor.grid(row=0, column=1, sticky='nsew')

        self.menu_frame = Frame(self.master, relief=RAISED, bd=2)
        self.menu_frame.grid(row=0,column=0, sticky='ns')
        self.open_button = ttk.Button(self.menu_frame, text='Open',command=self.file_open)
        self.open_button.grid(column=0, row=0, pady=5, sticky='ew', padx=5)
        self.save_button = ttk.Button(self.menu_frame, text='Save As..', command=self.save_file_as)
        self.save_button.grid(column=0, row=1,sticky='ew', padx=5)

    def file_open(self):
        """Open a file for editing"""
        file_path = askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        if not file_path:
            return
        self.text_editor.delete('1.0', END)
        with open(file_path, mode='r', encoding='utf-8') as input_file:
            text = input_file.read()
            self.text_editor.insert(END,text)
            self.master.title(f'Simple Text Editor- {file_path}')
            
    def save_file_as(self):
        """Saves the current file as new file in .txt"""
        file_path = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )
        if not file_path:
            return
        with open(file_path, mode='w', encoding='utf-8') as output_file:
            text = self.text_editor.get(1.0,END)
            output_file.write(text)
        self.master.title(f'Simple Text Editor- {file_path}')


def main():
    main_window = Tk()
    textEditor = TextEditor(main_window)

    main_window.mainloop()

if __name__=='__main__':
    main()