import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors"))
rock_paper_scissor = ["rock", "paper", "scissors"]
art = [rock, paper, scissors]
your_choice = rock_paper_scissor[choice_input]
your_art = art[choice_input]
computer_input = random.randint(0,2)
computer_choice = rock_paper_scissor [computer_input]
computer_art = art [computer_input]



print(your_art)
print(f"Computer chose:\n {computer_art}")

if((your_choice == "rock" and computer_choice == "scissors") or (your_choice == "scissors" and computer_choice == "paper" ) or (your_choice == "paper" and computer_choice == "rock" ) ):
    print ("You Win !")
elif ((your_choice == "scissors" and computer_choice == "rock") or (your_choice == "paper" and computer_choice == "scissors" ) or (your_choice == "rock" and computer_choice == "paper" ) ):
    print("You lose")
else:
    print ("it's a tie !")