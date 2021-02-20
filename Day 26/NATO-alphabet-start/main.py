import pandas


#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print (nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input ("Please input a word").upper()

nato_translate = [nato_dict[letter] for letter in word]
print (nato_translate)