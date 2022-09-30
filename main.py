from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.


all_bids = {}
completed = False

def find_highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  

while not completed:
  print(logo)
  name=input("Enter your name: \n")
  bid=int(input("Enter your bid: \n"))
  all_bids={}
  all_bids[name]=bid
  should_continue=input("Are there any more bidders- Type y or n. \n").lower()
  if should_continue=='n':
    completed=True
    find_highest_bidder(all_bids)
  elif should_continue=='y':
    clear()
    
  