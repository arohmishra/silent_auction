#silent auction

import os 

items= {}
def add_items(name, bid):
    items[name]= bid

flag = "yes"
while flag == "yes":
    name = input("enter your name :").lower()
    bid = int(input("enter your bid amount :"))
    add_items(name,bid)

    flag = input("are there any other bidders ? (yes/no) :").lower()

    if flag == "yes":
        os.system('cls')

   
max_bid = 0
for key in items:
    if  max_bid < items[key]:
        max_bid = items[key]
        winner = key      
         
print("Auction has ended")      
print(f"winner is {winner} with a bid of {max_bid} ")

