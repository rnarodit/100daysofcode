import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

randomInt = random.randint(0,len(names)-1) # len  can be used to get the number of items in a list or number of chars in a string
print(f"{names[randomInt]} is going to buy the meal today!")


