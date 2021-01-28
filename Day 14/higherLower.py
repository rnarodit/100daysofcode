#import art
from art import logo, vs
#import random
import random
#import data 
from game_data import data 
#import os to clear the screen
import os

#choose data at random
def chooseData (): # could have done this with random.choice(data)
    position = random.randint (0, len(data) -1 )
    return data [position]

def moreFollowers (choiceA , choiceB, playerChoice):
    followersA= int(choiceA ['follower_count'])
    followersB = int(choiceB ['follower_count'])
    if( followersA > followersB  and playerChoice == 'a') :
        return True 
    elif (followersB > followersA and playerChoice == 'b'):
        return True
    else:
        return False


winning = True
compareA = chooseData ()
compareB = chooseData ()
while(compareA == compareB):
    compareB = chooseData ()
score = 0
#Display name , description , and country for a and b
print (logo)
while (winning == True) :
    print (f"Compare A, {compareA['name']}, a {compareA ['description']}, from {compareA['country']}")
    print (vs)
    print (f"Compare B, {compareB['name']}, a {compareB ['description']}, from {compareB['country']}")
    choice = input ("Who has more followers ? Type 'A' or 'B'").lower()
    correct = moreFollowers (compareA, compareB, choice)
    os.system('cls')
    print (logo)
    if correct == True :
        compareA = compareB
        compareB = chooseData ()
        score += 1
        print (f"That's right , current score: {score}")
    else :
        winning = False
        print (f"Sorry, that's wrong. Final score: {score}")
    



#ask user to ask to choose between a and b 

# check if user was right, if yes keep playing if no game over

