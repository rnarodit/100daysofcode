#askoython.com -> search for random module
# module ->  a piece of code you import to your code that provides that code functionallity. so import a module instead of coding that funcitonallity into your current code making it super hard to understand
# to use the random module you first need to import it
import random

# you can create your own modules
import my_moudleex
#print (my_moudleex.pi) 

random_integer = random.randint(1,10) # get random integer b/w 1 and 10 included [1,10]
print (random_integer)

random_float= random.random() # random float number [0,1) (not including 1 )
print(random_float)

random_float2= random.uniform(0,5)
print(random_float2)

#using random numbers
love_score = random.randint(1, 100)
print (f"Your love score is {love_score}")