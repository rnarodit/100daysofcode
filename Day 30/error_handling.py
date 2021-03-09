# catching exeptions -> cath an error when it occurs in order to gracefully recover
#try -> comes before block of code . olace it b4 something that might cause an exception
#except -> do this if there was an exception
#else -> do this if there were no exceptions 
#finally -> do this no matter what happens

#file not found
# try:# if there are multiple exceptions more except statements can be written to cath all the exceptions and handle each one in a different manner
#     file = open("Day 30/a_file.txt")
#     a_dictionary = {"key": "value"}
#     #print (a_dictionary["asdasd"])
#     print (a_dictionary["key"])
# except FileNotFoundError:# create a file if file cannot be read 
#     file= open ("Day 30/a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:# capture the error message that is originally  genrated by the excpetion
#    # print ("That Key does not Exist")
#    print(f"the key {error_message} does not exist")

# else: # executes if everything succeeds
#     content = file.read()
#     print(content)

# finally:# execute in success and failrue of the code.
#     file.close()
#     print ("file was closed")
   
#     # allows us to raise our own exeptions 
    
#     raise KeyError ("this is an error that i made up")


height = float(input("Height: "))
weight =int(input("Weight: "))
if height> 3:
    raise ValueError("Human height should not be over 3m")
bmi= weight/(height ** 2)
print (bmi)