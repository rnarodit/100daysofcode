# inheritance -> inherit attributes and methods from a class and then adding functionallty
# class fish (class to inherit from):
#         def __init__(self):
#             super.__init__()-> get a hold of attributes and methods from the parent class 

class Animal :
    def __init__(self):
        self.num_eyes = 2
    
    def breath (self):
        print("inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_eyes = 3
    def breath(self):
        super().breath() # calling breath method from parent class
        print ("doing this underwater")
    def swim (self):
        print ("Moving in water")

nemo = Fish()
nemo.swim ()
nemo.breath()
print (nemo.num_eyes)