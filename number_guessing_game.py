import random

Number=random.randint(0,100)
# guess=int(input("Guess a number between 0 and 100, you've got 5 chances:"))

chances=5

while chances!=0:
    guess = int(input(f"Guess a number between 0 and 100, you've got {chances} chances left:"))
    if guess > Number:
        print("Too High")
    elif guess < Number:
        print("Too low")
    elif guess == Number:
        print("You've guessed a right number, You Win!!")
        break
    else:
        print("Invalid input")
    chances-=1

if chances == 0:
    print("You've got 0 chances left, you lose!!")
    print(f"correct answer is :{Number}")