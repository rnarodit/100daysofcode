THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):# after : we specifiy what data type quiz_brain is 
        self.quiz= quiz_brain
        self.window =Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20 , pady=20 , bg= THEME_COLOR)

        self.score_label= Label(text="Score:")
        self.score_label.grid(column=1, row= 0)
        self.score_label.config(bg=THEME_COLOR, fg="white")

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text= self.canvas.create_text(150,125,text="Title", width=280 , fill=THEME_COLOR, font= ("Arial", 20, "italic")) # width param helps us fit the question text within the canvas
        self.canvas.grid(column=0 , row=1 , columnspan=2, pady=50)

        wrong_img = PhotoImage(file="Day 34/images/false.png") # do not need self keyword here bc we use this image only inside the class and nowhere else
        self.button_wrong = Button(image=wrong_img, highlightthickness=0,command= self.answer_true)
        self.button_wrong.grid(column=1, row=2)

        right_img = PhotoImage(file="Day 34/images/true.png" )
        self.button_right = Button(image=right_img, highlightthickness=0, command= self.answer_false  )
        self.button_right.grid(column=0, row=2)
        
        self.get_next_qeustion()
        
        self.window.mainloop()

    def get_next_qeustion(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="you have reached the end of the quiz")
            self.button_right.config(state = "disabled")
            self.button_wrong.configure(state="disabled")
    
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback (self, is_right):
        
        if (is_right == False):
            self.canvas.configure(bg="Red")
        else:
            self.canvas.configure(bg="Green")
        self.window.after(1000,self.get_next_qeustion)