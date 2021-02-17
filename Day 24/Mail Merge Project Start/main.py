#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_list = []
with open ("Day 24/Mail Merge Project Start/Input/Names/invited_names.txt" ) as names:
    name_list = names.readlines()

with open ("Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt" ) as start_letter:
    contents = start_letter.read()

for name in name_list:
    current_name = name.strip()
    new_letter = contents.replace("[name]",current_name)
    f = open (f"Day 24/Mail Merge Project Start/Output/ReadyToSend/{current_name}.txt" , mode = "w")
    f.write(new_letter)
    f.close()