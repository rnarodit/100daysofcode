from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_bank.append(Question(question["question"],question["correct_answer"]))
print (question_bank[0].text)

quiz = QuizBrain(question_bank)
while (quiz.still_has_questions()):
    quiz.next_question()

print ("you've Completed the Quiz ")
print (f"Final score is {quiz.score}/{quiz.question_number}")
