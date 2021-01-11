3 + 5
7 - 4
3 * 2
#dividing things will always give you a floating point number
6 / 3 
#raise number to a power
2 ** 2

#priority to operations -> PEMDAS 
# 1)parenthesis()
# 2)Exponents
# 3)Division/ multiplication -> whichever is to the left goes first
# addition/ Subtraction -> whichever is leftest goes first


#rounding numbers -> round(number, number of decimal places to round too) 
print (round(8/3 , 2 )) \

# floor division -> // cuts of all numbers after the decimaland returns an integer
print(type(8//3))

# can put stuff in a variable and do operations on that variable -> += , -= , *= , /=
result = 4/2
result /= 2
print (result)

#f-strings lets you to create string from multiple data types
score=0
height=1.8
isWinning= True
print(f"Your Score is {score}, your height is {height}, you are winning is {isWinning} ")