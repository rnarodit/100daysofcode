from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
marks = ""
REPS =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global marks
    marks =""
    window.after_cancel(timer)
    time_label.config (text="Timer")
    check_label.config (text="")
    canvas.itemconfig(timer_text, text="00:00")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():# function that starts timer when we press the start button
    global REPS
    REPS +=1
    work_sec = 60*WORK_MIN
    short_break_sec = 60*SHORT_BREAK_MIN
    long_break_sec= 60 * LONG_BREAK_MIN
    if (REPS % 2 != 0):
        count_down(work_sec)
        time_label.config (text ="Work" ,bg=YELLOW, fg=GREEN , font= (FONT_NAME, 35, "bold"))

    elif (REPS % 2 ==0 and REPS % 8 != 0):
        count_down(short_break_sec)
        time_label.config(text ="Short Break" ,bg=YELLOW, fg=PINK , font= (FONT_NAME, 35, "bold"))

    else:
        count_down(long_break_sec)
        time_label.config(text ="Long Break" ,bg=YELLOW, fg=RED , font= (FONT_NAME, 35, "bold"))
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global REPS
    
    count_minutes = math.floor(count/60) # get the minutes with out seconds rounding down
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = "0"+str(count_seconds) #dynamic typing is changing the type of variable by changing the contents in it , can't be done in all languages 
    canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_seconds}') # changing  canvas attribute values
    if(count>0):
        global timer
        timer=window.after(1000, count_down, count- 1)
    else:
        start_timer()
        if (REPS % 2 == 0):
            global marks
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50, bg=YELLOW)



time_label = Label (text ="Timer" ,bg=YELLOW, fg=GREEN , font= (FONT_NAME, 35, "bold"))
time_label.grid(column= 1,row = 0)

canvas = Canvas(width=200 , height=224, bg=YELLOW,  highlightthickness=0)
tomato_img=PhotoImage(file="Day 28/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text= canvas.create_text(100,130,text="00:00", fill="white", font= (FONT_NAME, 45, "bold"))
canvas.grid(column= 1, row = 1 )


start_button= Button (text="Start", bg=YELLOW, command=start_timer)
start_button.grid(column = 0 , row=2)

reset_button= Button (text="reset",  bg=YELLOW ,command= reset_timer )
reset_button.grid(column = 2 , row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font= (FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()