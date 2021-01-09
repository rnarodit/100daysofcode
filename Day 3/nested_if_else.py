#if condition:
#     if another condition:
#             do this
#     else:
#         do this
# else:
#     do this
# computer looks at outside if /else first and if the condtion in the if statement outside is true the internal if/else is executed. if not than it skips to the outside else statement immidiatly 
height= int(input("What is your height in cm? ")) 
if height  >= 120:
    print("You can ride the rollercoaster! ")
    age=int("What is your age?")
    if age <= 18:
        print("You pay $5.")
    else:
        print("You pay $7.")
    
else:
    print("Sorry, you have to grow taller b4 you cann ride.")

#elif is used when you have more than 1 condition to check:
#if condition1:
#     do a
#elif condition2:
#     do b
#else:
#     do this

if height  >= 120:
    print("You can ride the rollercoaster! ")
    age=int("What is your age?")
    if age <12:
        print("Please pay $5.")
    elif age <=18 :
        print("please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller b4 you cann ride.")

#multiple if -> evaluates and executes each if unlike elif where it stops on the if statement that is true and does not execute the rest
#if condition 1: 
#   do a
#if condition 2:
#   do b
#if condition 3:
#    do c
bill = 0
if height  >= 120:
    print("You can ride the rollercoaster! ")
    age=int("What is your age?")
    if age <12:
        print("Child ticeket are $5.")
        bill = 5
    elif age <=18 :
        print("Youth tickets are  $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken ? Y or N")
    if wants_photo == "Y": #don't need else statement bc if they do not want a photo we will not add anything to the bill
        # add $3 to their bill 
        bill += 3 
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller b4 you cann ride.")


#Checking for multiple conditions in a single if statement is done by using logical operators.
# A and B -> both conditions need to be true for the entire thing to evaluate to true
# C or D -> one need to be true for the entire thing to evaluate to true
# not E -> reverses the condition 
bill = 0
if height  >= 120:
    print("You can ride the rollercoaster! ")
    age=int("What is your age?")
    if age <12:
        print("Child ticeket are $5.")
        bill = 5
    elif age <=18 :
        print("Youth tickets are  $7.")
        bill = 7
    elif age >= 45 and  age <= 55:
        print ("your ticket is $0")
        # do not need to assign bill to anything becasue with elif this will be the only statement that is executed and bill is already = 0
    else:
        print("Adult tickets are $12.")
        bill = 12
    
    wants_photo = input("Do you want a photo taken ? Y or N")
    if wants_photo == "Y": #don't need else statement bc if they do not want a photo we will not add anything to the bill
        # add $3 to their bill 
        bill += 3 
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller b4 you cann ride.")