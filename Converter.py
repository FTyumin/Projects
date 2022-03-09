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


first_entry = Entry(note)
first_entry.pack(pady=30,padx=10)


conversion = LabelFrame(currency_frame,text='Conversion')
conversion.pack(pady=20)


conversion_label = Label(conversion, text='Currency')
conversion_label.pack(pady=10)


conversion_entry = Entry(conversion)
conversion_entry.pack(pady=10,padx=10)


rate_label = Label(conversion,text="Conversion Rate")
rate_label.pack(pady=10)

rate_entry = Entry(conversion)
rate_entry.pack(pady=10,padx=10)


button_frame = Frame(currency_frame)
button_frame.pack(pady=20)



root.mainloop()