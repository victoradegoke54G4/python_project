from tkinter import *
from tkinter import ttk, messagebox

class LengthConverter:
    def __init__(self, master) -> None:
        master.title('Length(Mile -> KM)')
        master.resizable(False,False)
        self.frame_entry = ttk.Frame(master=master)
        self.frame_entry.grid(row=0, column=0, padx=10)
        self.mile_entry = ttk.Entry(master=self.frame_entry,width=10)
        self.mile_entry.grid(row=0, column=0, sticky='e')
        self.mile_label = ttk.Label(master=self.frame_entry, text='Mile')
        self.mile_label.grid(row=0, column=1, sticky='w', padx=5)
        self.convert_button = ttk.Button(master=master, width=5, text='\N{RIGHTWARDS BLACK ARROW}', command=self.mile_to_km)
        self.convert_button.grid(row=0, column=1,pady=10)
        self.result_label = ttk.Label(master=master, text='KM')
        self.result_label.grid(row=0,column=2,padx=20)


    def mile_to_km(self):
        """Convert mile to km"""
        mile = self.mile_entry.get()
        try:
            km = float(mile) * 1.609344
        except ValueError:
            messagebox.showinfo(title='Feedback', message='Invalid input!')
        else:
            self.result_label['text'] = f'{round(km,2)} KM'



def main():
    main_window = Tk()
    pomodoro = LengthConverter(main_window)

    main_window.mainloop()

if __name__=='__main__':
    main()