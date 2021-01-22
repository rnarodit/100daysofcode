############DEBUGGING#####################
# 1 describe the problem
# 2 reproduce the bug 
# 3 Play computer
# 4 fix the errors 
# 5 print is your friend 
# 6 use a debugger 
# 7 Take a break
# 8 Ask a friend
# 9 Run code often 
# 10 Ask StackOverflow 


# Describe Problem
# def my_function():
#   for i in range(1, 21):# range was 1,20 before , code didn't work bc 20 was not included 
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #dice_num = 6 # original value was randint(1,6) , we would get an error every time six was chosen because it is out of the range of the dic_img list. we put 6 there to reproduce the problem
# dice_num = randint(0,5) # fix 
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# #if year > 1980 and year < 1994: # does not capture 1994 since it is not inclusive
# if year > 1980 and year <= 1994 :
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# #age = input("How old are you?")
# age = int(input("How old are you?")) # need to convert to Integer since we are doing a comparison to another integer in the if statement 
# if age > 18:
# #print("You can drive at age {age}.") incorrect syntax for f strings, also print statement was not indented to be inside the IF staement 
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print (pages)
# #word_per_page == int(input("Number of words per page: ")) # need to use one equal operator. found out this issue by using print statements after each input function
# word_per_page = int(input("Number of words per page: "))
# print (word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  #b_list.append(new_item) # only final new_item is inputed in the list since this statement is not inside the for loop
    b_list.append(new_item) # need to indent this staement so it is in the for loop
  print(b_list)

mutate([1,2,3,5,8,13])