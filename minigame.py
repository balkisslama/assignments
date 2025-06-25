#importing the python "random" module:
import random

#asking the user to pick a choice from a list:
user=input("please enter your choice from this list (rock, scissors, paper)\n")

#printing the user's  choice on screen:
print (f"you entered : {user}")

#Creating a list of options for the computer to choose randomly from:
options = ["rock","scissors","paper"]

#Computer makes a random choice using the "random" module choice() method:
rando = random.choice(options)

#printing the computer's choice:
print(f"the computer picked: {rando}")

#Rules of the game:
if rando == user : print ("It's a tie.")
elif (user== 'rock' and rando== 'scissors') or (user=='scissors' and rando=="paper") or (user=='paper' and rando=="rock"):
    print ("Congrats you won!")
else:
    print ("sorry! Computer won this time!")