import random

#choose number of gasses based on user inputed diffulty level. 10 for easy. 5 for hard
def num_guesses ():
    difficulty = input("Choose Da difficulty. Type 'easy' or 'hard': ").lower ()
    if (difficulty == 'hard'):
        return 5
    elif (difficulty == 'easy') :
        return 10
    else:
        return 0
    
#get number for us to guess 
number = random.randint(1,100)
#get amount of guesses 
chances =  num_guesses ()
win = False

print(f"Number is {number} ")
# keep going while user have not won yet and he has more guesses left
while (chances > 0 and win == False) :
    guess = int (input("Make a Guess "))
    if (guess > number) :
        print ("Too High.\nGuess again. ")
        chances -= 1
        print (f"you have {chances} remaining to guess the number ")
    elif (guess < number ):
        print ("Too Low.\nGuess again. ")
        chances -= 1
        print (f"you have {chances} remaining to guess the number ")
    else:
        print (f"you guessed correctly you win. Number was {number}")
        win = True
if(chances == 0 and win == False):
    print ("You ran out of gasses, you lose. ")