# Lets import random for chosing randomly between rock , paper or Scissors..!
import random

# Also , lets add 2 functions
# 1 for getting user and computers choices and
# 2 for evaluating who won between each of them.

def rock_paper_get_choices():
    """
    This function gets the user's inputs and choses randomly for computers choices..
    """
    user_inp=input("'r':- Rock\n'p':- Paper\n's':- Scissors\nWhat\'s  your choice\n")
    comp_choice=random.choice(['r','p','s'])

    print(f"You chose {user_inp} and computer chose {comp_choice}..!!")

    # let's handle a scenario where both have same choice.
    if user_inp==comp_choice:
        return "It's a Tie..!!"
    
    if rock_paper_who_wins(user_inp,comp_choice):
        return "You Won..!!"

    return "You lost to Computer..!"


def rock_paper_who_wins(user,comp):
    """
    This function evaluates who won the actual game and returns true only if user won.
    i/p:- is choices from user and computer.
    """
    # Rock paper scissor logic is as below
    # r>s , s>p and p>r
    if (user=='r' and comp=='s') or (user=='s' and comp=='p') or (user=='p' and comp=='r'):
        return True

result=rock_paper_get_choices()
print(result)