import random

print("Welcome to Number guessing game, You have got 7 chances to guess the Number Right!! ")

a,b= map( int,input("Select a range of Numbers :").split())

rand_int= int(random.randint(a,b))

chances = 7
guess_counter =0

while guess_counter <chances:
    guess_counter+=1
    user=int(input("Guess a number between range:"))

    if user > rand_int:
        print("Try Again!You've guessed too big")
    elif user < rand_int:
        print("Try Again!You've guessed too small")
    elif user == rand_int:
        print("you've guessed a right number, You Win!!")
        break
    else:
        print("Invalid Input")


