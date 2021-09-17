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
        guess=rand.randint(low_val,high_val)
        user_feedback=input(f"Computer has guessed {guess}.. Type H for High,L for Low and C if correct..!! :-  ").lower()
        if user_feedback=='h':
            high_val=guess-1
        elif user_feedback=='l':
            low_val=guess+1
        # You need to check if user enters invalid values and give proper message.
    print(f"Computer has guessed your number {guess} correctly...!!")

high_val=int(input("Enter upper limit of number from 1 : - "))
guess_by_computer(high_val)