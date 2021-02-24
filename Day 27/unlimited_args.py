def add (*args): #undifned number of arguments, *args is a tuple. can accept any number of args. name after * doesn't have to be args * is the imporant part
    total=0
    print (args[0])# can access speicifc argument in the tuple of arguments
    for n in args:
         total += n
    return total


print(add(4,5,6,7))


def calculate (n,**kwargs): #unlimited key word arguments(**kwargs, n parameter is not necessary ), creates dictionary of key word arguments and their value that were sent to the function
    print (kwargs)
    # for key,value in kwargs.items():
    #     print (key)
    #     print(value)
    # print (kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print (n)
calculate (2,add = 3, multiply= 5)

class Car:
    def __init__(self, **kw): # class that you can initlize by passing in multiple  key word arguments
        #self.make = kw["make"]
        #self.model = kw ["model"] if we use square brackets to get the value from the dictionary program will crash when the specified arguments are not passed at class initlizatoin , below method to getting stuff from a dictionary will not cause a crash . allows for optional key word arguments 
        self.make = kw.get("make")
        self.model=kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make ="nissan") # if we do not put one of 
print (my_car.model)