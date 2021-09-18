"""
5) Hangman Game:-
- Words list can be custom list in program  (also , can be stored in a list in a python file and referenced in this file. 
  As in Freecodecamp Tutorial.)
- Or Words can be read from a url.(https://raw.githubusercontent.com/dwyl/english-words/master/words.txt)
"""
import random

# Let's create a words list as below.
# Let's also include some invalid entries such as let's and go-pro (invalid meaning , ' - _ etc...)
words_list=['ash','lake','listen','rage','nature','instinct','finance','jail','omission','tower','compromise','steam','coma','lecture','council',
'cheek','injection','hour','consolidate','rehearsal','funeral','trend','trade','terrify','sin','manual','genuine','knit','broccoli',
'me','crouch','burst','stop','ant','moon','border','word','poison','correspond','he','feminist','dead','single','crew','draw','knee',
'presentation','calorie','by','plagiarize','let\'s','go-pro']

# words_list=['ash','lake','let\'s','go-pro']

# let's create a function to chose valid word from above word's list.
def chose_word(words):
    """
    i/p:- list of words.
    o/p:- chose single valid word.
    """
    word_chosen=random.choice(words)   # 1st , chose a random word from words list
    while '\'' in word_chosen or '-' in word_chosen: # check if it's one of invalid words.
        word_chosen=random.choice(words)             # If Invalid , chose another word.
    # print("Chosen Word:-",word_chosen)
    return word_chosen.upper()                       # return word if chosen one is valid.

# def track_lives(live_cnt,lives=10):
#   """
#   This function tracks the lives left if in case wrong guesses.
#   You can input the number of lives for the game and count of lives as input.
#   Output will print number of lives left.
#   """

def hangman_game():
  """
  Main Hangman game module
  """
  # get input word for the game from the chose_word() function
  input_word=chose_word(words_list)
  print("Hello there...\n Welcome to Hangman game...\n Lets start the guessing game")
  lives_left=10           # track and initialize the lives count.
  guessed_words=set()     # track guessed words as a set (no duplicates allowed in sets..!)
  actual_words=set(input_word) # Convert the word to set to avoid guessing same character's..

  print("Below is the pattern of word..!! ")
  # While , we have lives left and when all the characters are not guessed , then continue loop.
  while lives_left>0 and len(actual_words)>0:
    print_word=" ".join([letter if letter in guessed_words else '-' for letter in input_word])
    print(print_word)
    guess=input("\nEnter your guessed word..! :- ").upper()
    if guess.isalpha():
        if guess in guessed_words:
            print("You have already guessed "+ guess +". Please check below guesses and enter.")
        else:
            guessed_words.add(guess)
            if guess in input_word:
                actual_words.remove(guess)
            else:
                lives_left-=1
                print(f"Oops!! You have {lives_left} lives remaining to Guess.{guess} not in chosen word..!")
                print("***** You have used \" {} \" alphabets so far.! ******\n".format(" ".join(guessed_words)))
    else:
      print("Please enter word only..!")
  if lives_left==0:
    print("You Lost..!! Correct word is :- ",input_word)
  else:
    print("You won by guessing {} correctly with {} lives remaining...!".format(input_word,lives_left))

hangman_game()
