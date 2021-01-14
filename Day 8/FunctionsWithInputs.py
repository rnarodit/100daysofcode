def greet ():
    print ("Hello")
    print ("There")
    print ("Guy")
greet()

#functions with inputs
# def my_function (something):
    #do this with something
    #then do this 
    # finally do this
# call the function -> myfunction (123) -> 123 will be passed to the variabale called something in this example -> we esentially create a variable something (parameter -> name of data that u use to refere to the data inside the function) = 123 (argument->actual data)
# def greet_with_name (name):
#     print (f"Hello {name}")
#     print (f"how are u {name}")

# greet_with_name ("bob")

#functions with more than 1 input
def greet_with(name, location):
    print (f"Hello {name}")
    print (f"What is it like {location}")

#greet_with ("NO where", "Ron") # position of the data matters, arguments are assigned to parameter based on parameter order in the function definition

#can also use key work arguments when calling a fuunction
greet_with (location = "Israel" , name = "Ron") # you can change to order around now but the bindings will still be respected, position won't matter anymore 