import pandas


#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print (nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
validInput= False
while (validInput == False):
    word = input ("Please input a word").upper()
    try:
        nato_translate = [nato_dict[letter] for letter in word]
    except KeyError:
        print ("You can only Enter Letters")
    else:
        validInput= True

print (nato_translate)