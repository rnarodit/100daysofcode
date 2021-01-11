#list is a data structure (way to organize and store data in python)
#use to store pieces of data that belong to each other
#good for maintaining data in certain order
# list ex -> fruites = [item1, item2] 


states_of_america= ["Delaware", "Pennsyivania", "New Jersey"] # you can choose to arrange the items in the list in an order you want. for ex create a list of states and add each state based on the order it joined the union
num_of_states= len(states_of_america) #len() gives the # if items in a list
#state= states_of_america[1]

#print (states_of_america[0])# print first item of the list, note that we start with 0 and not 1. last item is in position n-1 
#print (states_of_america[-1]) # can also use negative indexes which get items in the list starting from the end with -1 being the first one 
#states_of_america[1]= "pencilvania" # you can alter the data of a specific item in the list
#states_of_america.append("RonLand") # can add an item to the end of the list
#states_of_america.extend(["angelaland,joniland"]) # add multiple items to the end of the list

#index out of range error
#print(states_of_america[3])

#dirty__dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits= ["strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
veggies= ["Spinach", "Kale", "Celery", "Potatoes" ]

#nested list
dirty_dozen=[fruits,veggies]
print(dirty_dozen)