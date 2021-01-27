################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#local scope -> can only access veriable in the function it is used in. if you need it to be accessible outside the function you need to use global scope
# def drink_potion () :
#     potion_strength = 2
#     print (potion_strength)
# drink_potion()


#Global Scope
player_health = 10 #global variable  avaiable anywhere
# def game():
# def drink_potion () :
#     potion_strength = 2 # local variable , available only inside the function 
#     print (player_health)
# drink_potion()

#name space -> scope in which the variable, function was created in 
def game():
    def drink_potion () :
        potion_strength = 2 
        print (player_health)
    drink_potion() # can only call drink_potion within the game () function f

#there is no block scope :
# if 3>2 :
#     a_veriable = 10  "this veriable is not limited to inside the if statement but to the function it is in. if no function than it is global"
# game_level = 3
# enemies = ["Skeleton" , "Zombie" , "Alien"]
# if game_level < 5:
#     new_enemy = enemies [0]

# print (new_enemy)

# game_level = 3
# def create_enemy ()
#     enemies = ["Skeleton" , "Zombie" , "Alien"]
#     if game_level < 5:
#         new_enemy = enemies [0]

# print (new_enemy)# print statement won't work this time since new_enemy is the create_enemy() function scope

enemies = "skeleton"
def increase_enemies() :
    #enemies = "zombie" # we are creating a completely new veriable here, don't call ur local and global variables the same name
    #global enemies # this is the way to modify a global veriable inside a function, DONT DO THIS VERY OFTEN BEVCAUSE IT IS PRON TO CREATING BUGS AND ERRORS, use return statements instead
    #print (f"Enemies inside function : {enemies}")
    return enemies + 1 # the best way to modify global variables 
increase_enemies()
print (f"Enemies outside function : {enemies}")

# global constants -> veriables that u define and you're never planning on changing them ever again 
PI = 3.14159 # convention in python to signify constanst is all upper case, or upper case separated by underscore


