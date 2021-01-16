# can think about a dictionary like a form of a table key on the left value on the right 
#syntax {key : value} => for ex {"Bug" : "an error in a program that prevents it from runnign as expected"}
# multiple values in a dictionary : {key value, key:value}
# end last key:Data pair in dictionary with a  , so you can just press enter and keep typing key:value pairs
#need to use the correct  data types in the dictionary 
programming_dictionary = { 
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
   
    }

#retrieve value from a dictionary : use the value of key
print (programming_dictionary["Bug"]) # spell the key correctly , if u put a key that does not exist you will get a key error

#Adding item to dictionary 
programming_dictionary ["Loop"] = "The action of doing something over and over again"
#print(programming_dictionary)

#empty dictionary 
empty_dictionary = {}

#wipe dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#edit item
programming_dictionary ["Bug"] = "A moth in your computer "
#print(programming_dictionary)

#loop through dictionary 
for key in programming_dictionary:
    print (key)
    print (programming_dictionary[key])

#Nesting putting dictionaries and keys inside one another { key : [List], Key2: {Dictionary}}
capitals = {
    "France": "Paris",
    "Germany" : "Berlin" ,

}

#Nesting list in dictionary
# #travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Berlin" , "hamburg", "stuttgart"]
# } 

#Nesting dictionary into dictionary 
# travel_log = {
#     "France" : {"Cities visited": ["Paris", "Lille", "Dijon"] , "total_visits": 12} ,
#     "Germany" : {"Cities visited": ["Berlin", "Hamburg", "Stuttgart"] , "total_visits":5} ,
# } 

#dictionary inside a list -> access items via position in a list
travel_log = [
    {
        "Countery": "France" , 
        "Cities visited": ["Paris", "Lille", "Dijon"] , 
        "total_visits": 12
        } ,
    {
        "Countery": "Germany" , 
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"] , 
        "total_visits":5
        } ,
]

print (travel_log[0])
