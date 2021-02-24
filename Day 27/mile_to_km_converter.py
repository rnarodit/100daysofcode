from tkinter import *
window = Tk()
window.title("Mile to KM Converted")
window.minsize(width= 300, height = 100)

eq_label = Label(text="is equal to")
eq_label.grid(column= 0, row =1 )
eq_label.config(padx=5)

calc_label = Label(text="0")
calc_label.grid(column= 1, row =1 )
calc_label.config(padx=5)

km_label = Label(text="Km")
km_label.grid(column= 2, row =1)
km_label.config(padx=5)

input= Entry( width=10)
input.insert(END, string = 0)
input.grid(column =1, row=0 )
input.config()

miles_label = Label(text="Miles")
miles_label.grid(column= 2, row =0 )
miles_label.config(padx=5)

def button_clicked():
    miles= float(input.get())
    km= miles * 1.609
    calc_label.config(text=str(km))
    
button = Button(text="calculate", command= button_clicked)
button.grid(column=1, row=3 )










window.mainloop ()