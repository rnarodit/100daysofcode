# age : int # decalre data type of variable b4 intializing it . if correct data type is not used when the variable gets assigned a value an error will occur 
# name : str
# height: float
# #is_human : bool

def police_check(age:int)->bool: # can also declare a type for function input, arrow specified what value will be returned 
    if age>18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(19):
    print ("you may pass")
else:
    print ("Pay a fine")