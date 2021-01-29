#OOP -> instead of having one long an complicated code (procedural). you simplify the relationships in your code by seprating it into different components that can later reused in other code.
#OOP tries to model real world objects -> divide to what object has (attributes -> fancy way to say variable) and what object does(methods -> functions)
# we use the object blueprint to generate multiple versions of the object-> the blue print is a class and the versions generated are objects 
#object is the actual thing that we will be using in the code
# creating an object -> car = CarBluePrint() -> note the pascal case of the class
# from turtle import Turtle , Screen
# timmy =  Turtle()
# print (timmy)
# myScreen= Screen ()

# #accessing attributes -> car.speed
# print (myScreen.canvheight)

# #using methods -> car.stop()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.speed("normal")
# myScreen.exitonclick()

#python package is a whole bunch of code that other people have written -> serve a particular purpose
#to use packages you find you need to install it

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle", "Charmander"])
table.add_column("Type",["Electric","Water", "Fire"])
table.align="l"
#table.add_column("Type")
print(table)
