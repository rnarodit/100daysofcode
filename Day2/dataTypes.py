#data types
#strings-> string of charachters enclosed by double quotes /single quotes . 
#can refer to a specific charachter in a string. remember 0 represents the first position in the string -> pulling an element from a string is called subscript 
print("Hello"[4])

#putting number in quotes make them a string so addition will just concactinate them
print("123"+"345")


#Integer-> to declare just write number w/o anything else
print(123+345)
#can put undersocres in a large number instead of commas to make it more readable and the computer will ignore it 
print(123_456)


#Float -> floating ponit number, number that has a decimal 
3141.59

#Boolean -> two possible value. begin with  capital T or F 
True
False

#Type erros using data types where they cannot be used
# len(2) for ex
#can use type check funciton to check the data type of something -> type()
num_char= len(input("what is your name? "))
print(type(num_char))
#you can convert data types -> str(), int() , float()
new_num_char= str(num_char)
print("Your name has "+ new_num_char + " characters.")
a=float(123)
print (type(a))