student_dict ={
    "student": ["Angela","Ron", "Bob"],
    "score": [56,76,98]

} 

# for (key,value) in student_dict.items(): # loop through dictionary 
#     print (key)
#     print (value)

# looping through a data frame is very similar to dictionary 
import pandas
student_data = pandas.DataFrame(student_dict)
print (student_data)

for (key,value) in student_data.items(): #loop through data frame
    print(key)
    print(value)
#Loop through rows of a data frame
for (index,row_data) in student_data.iterrows():
    #print (row_data.score)
    if row_data.student == "Angela":
        print (row_data.score)

students ={row.student:row.score for (index, row) in student_data.iterrows() }

print (students)