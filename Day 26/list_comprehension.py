# list comprehension is a case in which you create a new list from a previous list w/o using a for loop
# ex: new_list = [new_item for item in list]
numbers = [1,2,3]
#new_list = []

# for n in list :
#     add_1 = n+1
#     new_list.append(add_1)

# new_list = [n+1 for n in numbers] # list comprehension

# name="Angela"
# new_list2 = [letter for letter in name] # can also use list comprehension on strings
# print (new_list2)

#python sequences : list , range, string , touples all work with list comprehension

new_list = [n*2 for n in range (1,5)]
print (new_list)

#conditional list comprehension:
# new_list = [new_item for item in list if test] # only add new item and perform code if the test passes
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print (short_names)
long_names = [name.upper() for name in names if len(name) > 5 ]
print (long_names)

