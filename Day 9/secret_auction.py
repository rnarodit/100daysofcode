import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
print (logo)
more_bids= True
bids = {}
while ( more_bids == True):
    name= input ("what is your name ? ")
    bid= int (input ("What's your bid ? $"))
    bids [name] = bid
    additional_bids= input ("Are there addtional bids ?")
    if additional_bids == "no":
        more_bids = False
    os.system('cls')
winning_bidder = ""
winning_bid = 0
for name in bids :
    if bids [name] > winning_bid :
        winning_bidder = name
        winning_bid = bids [name]

print (f"The Winner is {winning_bidder} with a bid of ${winning_bid} ")
