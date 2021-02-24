#import tkinter
from tkinter import * 
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height = 300) #tkinter window autoscales to fit all the components you have inside of it. however if you don't many components this methods is useful to prevent window size from beign to small
window.config(padx= 20, pady=20) # give some space from the edges of entire windows, can do this at widget level
#creating a label
my_label = Label(text= " I am a label" , font= ("Arial", 24, "bold"))
#my_label.pack() # need this to get the label to show up, we first create the component (in this case a label) and then we specify where do we want the component to be for it to show up . pack centers it on the screen
#my_label.pack(side= "left")
my_label.pack()
my_label["text"] = "New text" #changing property of a component
#my_label.pack()
#y_label.place(x=100,y=200)
my_label.grid(column = 0, row=0)# grid system is relative to other components, so go compnents you want at the top right first and so on
my_label.config(padx=50 , pady=50)

#my_label.config (text = "New text") -> does the same as the line above 
#button
def button_clicked():
    my_label["text"] = input.get()
#     my_label["text"] = "Button Got Clicked"
button = Button (text = "Click me" , command = button_clicked)
#button =Button( text ="click me", command= button_clicked) # command atribute specifies the funtion to use when the button is clicked
#button.pack()
button.grid(column=1 , row=1)

new_button= Button(text = "New Button")
new_button.grid(column=2, row=0)
#Entry -> input
input = Entry(width=10)
#input.pack()
#print(input.get())
input.grid(column =3, row=2 )




window.mainloop ()# keeps windows on the screen, this line always needs to be in the end of our program


#tkinter positioning : pack , place-> all about precise positining with x and y values, grid -> imagines entire windows is a grid and you can devide it up into roas and columns 
# with out one of the commands above a widget will not sho up on the screen
# you can't use pack and grid in the same program choose either or 