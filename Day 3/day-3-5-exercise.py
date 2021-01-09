# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#name1_Lower = name1.lower()
#name2_Lower =name2.lower()
#num_in_true = name1_Lower.count("t") + name1_Lower.count("r") + name1_Lower.count("u") + name1_Lower.count("e") + name2_Lower.count("t") + name2_Lower.count("r") + name2_Lower.count("u") + name2_Lower.count("e")
#num_in_love = name1_Lower.count("l") + name1_Lower.count("o") + name1_Lower.count("v") + name1_Lower.count("e") + name2_Lower.count("l") + name2_Lower.count("o") + name2_Lower.count("v") + name2_Lower.count("e")
#suggested method is actually to combine both strings bc it is more efficient:
comibned_string = name1 + name2

lower_case_string= comibned_string.lower ()

true_count= lower_case_string.count("t") + lower_case_string.count("r") + lower_case_string.count("u") + lower_case_string.count("e")

love_count= lower_case_string.count("l") + lower_case_string.count("o") + lower_case_string.count("v") + lower_case_string.count("e") 

digit= int(str(true_count) + str(love_count))

if digit < 10 or digit > 90 :
    print(f"Your score is {digit} ,you go together like coke and mentos.")
elif digit >= 40 and digit <= 50:
    print(f"Your score is {digit} ,you are alright together.")
else:
    print(f"Your score is {digit}")
