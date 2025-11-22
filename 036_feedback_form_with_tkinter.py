from tkinter import *
from tkinter import ttk,messagebox
from turtle import color


class Feedback:
    def __init__(self, master) -> None:
        master.title('Appmillers Online Courses')
        master.resizable(False,False)
        master.configure(background='#ECECEC')
    
        

        self.style = ttk.Style()
        self.style.configure('Tlabel', font=('Arial',12))
        self.style.configure('Header.Tlabel', font=('Arial',18, 'bold'))

        self.header_frame = ttk.Frame(master, padding=5)
        self.header_frame.pack()

        self.logo = PhotoImage(file='036_logo_appmillers_logo.gif')
        ttk.Label(self.header_frame, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.header_frame, font=('Arial',18, 'bold'), text='Thank for joining Us!').grid(row=0, column=1)
        ttk.Label(self.header_frame, wraplength=300, text='We are glad you chose Appmillers for your online study.' \
                                            ' Please tell us what you think about our onlne courses.').grid(row=1, column=1,padx=(5,5))
        
        self.content_frame = ttk.Frame(master, padding=20)
        self.content_frame.pack()

        ttk.Label(self.content_frame, text='Name:').grid(row=0, column=0, sticky='sw')
        ttk.Label(self.content_frame, text='Email:').grid(row=0, column=1, sticky='sw')
        ttk.Label(self.content_frame, text='Comments:').grid(row=2, column=0, sticky='sw')
        self.name_entry = ttk.Entry(self.content_frame, width=20)
        self.name_entry.grid(row=1,column=0, sticky='sw')
        self.email_entry = ttk.Entry(self.content_frame, width=20)
        self.email_entry.grid(row=1, column=1, sticky='sw')
        self.comment_text =Text(self.content_frame, font=('Arial', 10), width=50,height=10)
        self.comment_text.grid(row=3, column=0, rowspan=2, columnspan=2)

        ttk.Button(self.content_frame, text='Submit', command=self.submit).grid(row=5, column=0, sticky='e')
        ttk.Button(self.content_frame, text='Clear', command=self.clear).grid(row=5, column=1, sticky='w')
    
    def clear(self):
        self.name_entry.delete(0,'end')
        self.email_entry.delete(0,'end')
        self.comment_text.delete(1.0,'end')

    def submit(self):
        if not (self.name_entry.get() or self.email_entry.get() or self.comment_text.get('end')) :
            messagebox.showinfo(title='Error', message='Invalid Input!')   
        else:
            print(f'Name; {self.name_entry.get()}')
            print(f'Email; {self.email_entry.get()}')
            print(f'Comments; {self.comment_text.get('1.0','end')}')
            self.clear()
            messagebox.showinfo(title='Feedback', message='Comments submitted!')




def main():
    main_window = Tk()
    feedback = Feedback(main_window)
    main_window.mainloop()


if __name__=='__main__':
    main()