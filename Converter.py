from tkinter import *
from tkinter import ttk
from tkinter import messagebox



root = Tk()
root.title('Codemy.com - Currency Conversion')
root.geometry("500x500")


my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)


currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)


my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")


my_notebook.tab(1, state='disabled')



def lock():
	my_notebook.tab(1,state='disabled')
def unlock():
	pass
home = LabelFrame(currency_frame, text="Your Home Currency")
home.pack(pady=20)


home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)


conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)


conversion_label = Label(conversion, text="Currency To Convert To...")
conversion_label.pack(pady=10)


conversion_entry = Entry(conversion, font=("Times New Roman", 24))
conversion_entry.pack(pady=10, padx=10)


rate_label = Label(conversion, text="Current Conversion Rate...")
rate_label.pack(pady=10)


rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)


button_frame = Frame(currency_frame)
button_frame.pack(pady=20)


lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)

#CONVERSION
amount_label = LabelFrame(conversion_frame,text="Amount To Convert")
amount_label.pack(pady=20)

def convert():
    pass

def clear():
    amount_entry.delete(0,END)
    conversion_entry.delete(0,END)

#Entry Box For Amount
amount_entry = Entry(amount_label,font=("Helvetica",24))
amount_entry.pack(pady=10,padx=10)

conver_button = Button(amount_label,text="Convert",command=convert)
conver_button.pack(pady=20)


converted_label = LabelFrame(conversion_frame,text="Converted Currency")
converted_label.pack(pady=20)


converted_entry = Entry(converted_label,font=("Helvetica",24),bd=0,bg='systembuttonface')
converted_entry.pack(pady=10,padx=10)


clear_button = Button(conversion_frame,text="Clear",command=clear)
clear_button.pack(pady=20)


spacer = Label(conversion_frame,text='',width=68)

root.mainloop()