# lets import random module for generating random numbers.
# Implemented the Git version controlling.
import random as rand

# Now , lets define a function that will allow users to guess a number between a range.
def guess_number(high_num):
    """
    I/P: - This function takes 1 arg which is the upper limit of the number range
    in which you want to guess.
    
    O/P: - gives fun in guessing number.
    """
    # Define a variable that will hold your guesses , initialized to 0 as placeholder 
    # since user can select from 1- high_num only.
    my_guess=0
    rand_num=rand.randint(1,high_num) # Generate a random number between the range.
    # Now , lets see how we can repeatedly ask user to guess number
    # untill they can guess correctly.
    # print(rand_num)
    while my_guess!=rand_num: # continue loop until they guess correctly.
        my_guess=int(input(f"Guess a number between 1 and {high_num}..!"))  # Get input from user.
        if my_guess < rand_num:
            print("Sorry , your guess is low..!! Try again.. :) ")
        elif my_guess>rand_num:
            print("Sorry , your guess is high..!! Try again.. :) ")
        # Since the above while condition handles the equal to, we don't need to explicity state the obvious.
        #Pawan Commented :-  It will work outside the loop.
    print(f"Yayyy..!! You guessed {rand_num} correctly...!!!")

# high_val=int(input("Enter upper limit of number from 1 "))
# guess_number(high_val)

"""
Part 2:- Where we will have a number between range 1-x and computer needs to guess.
It can be done by feedback from user to inform computer if guess is high/low.
"""
def guess_by_computer(high_num):
    """
    I/P: - This function takes 1 arg which is the upper limit of the number range
    in which you want computer to guess.
    
    O/P: - Computer guesses your number.!!
    """
    low_val=1
    high_val=high_num
    guess=0
    user_feedback=''
    while user_feedback !='c':
        if low_val!=high_val:
            guess=rand.randint(low_val,high_val)
        else:
            guess=low_val # or can be high if same number.
        user_feedback=input(f"Computer has guessed {guess}.. Type H for High,L for Low and C if correct..!! :-  ").lower()
        if user_feedback=='h':
            high_val=guess-1
        elif user_feedback=='l':
            low_val=guess+1
        # You need to check if user enters invalid values and give proper message.
    print(f"Computer has guessed your number {guess} correctly...!!")

high_val=int(input("Enter upper limit of number from 1 : - "))
guess_by_computer(high_val)
