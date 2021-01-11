#for loop on lists ->
#for item in list_of_items:
    #do something to each item 

fruits = ["Apple", "Peach", "Pear"]
# variable name after for can be anything 
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)


#range () helps u generate  a range of numbers for a for loop to loop through without using a list
# for number in range (a,b):
    #print number 
for number in range (1,10):#not including 10, need to go one over (1,11) to get the number 10 in there
    print(number)

for number in range (1,11,3):# can increase the step of your for loop , 3rd number in the range function
    print(number)

total = 0
for number in range (1,101):
    total += number
print(total)