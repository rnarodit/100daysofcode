# new_dict = {new_key: new_value for item in list(or anything you can iterate through)}
#new_dict = {new_key: new_value for (key,value) in dict.items()}
#new_dict = {new_key: new_value for (key,value) in dict.items() if test}

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name:random.randint(1,100) for name in names}


passed_students = {name:score for (name,score) in student_scores.items() if score>60}
print (passed_students)