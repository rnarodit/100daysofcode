#functions with inputs 
# def my_function (something):
    #do something
    #do something 
    #do something
# functions with outputs 
# def function () :
    #results = 3*2
    #return results -> output of the function
# output = myfunction () will store the output of the function 

# def format_name (f_name , l_name):
#      modified = f_name.title() + " "+ l_name.title()
#      return modified  # return tells the computer that the function is over and that u should exit the function
# print (format_name("ron", "NARODITSKY"))

#multiple return values 
def format_name (f_name , l_name):
    """Take a first and last name and format it to return the titile case version of the name. """#Docstrings -> a way to create bits of documentation as we code. when we use function later in the code the docstring will show up in the IDE to describe the funtion we are using  . can be written on multiple line unlike a regular string
    if f_name == "" or l_name == "" :
        return "You didn't provide valid inputs" # -> terminates function early if we have empty first lame or last name
    modified = f_name.title() + " "+ l_name.title()
    return modified  # return tells the computer that the function is over and that u should exit the function
print (format_name(input("What is your first name ?"), input("What is your last name ? ")))



