from tkinter import *
from tkinter import ttk
from tkinter import messagebox 


root = Tk()
root.title('Currency Converter')
root.geometry('500x500')


note = ttk.Notebook(root)
note.pack(pady=5)


currency_frame = Frame(note,width=480,height=480)
conversion_frame = Frame(note,width=480,height=480)


currency_frame.pack(fill='both',expand=1)
conversion_frame.pack(fill='both',expand=1)


note.add(currency_frame, text='Currencies')
note.add(conversion_frame,text='Convert')


first = LabelFrame(currency_frame,text='Choose currency')
first.pack(pady=20)


root.mainloop()