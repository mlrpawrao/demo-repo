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

# let's create a function to chose valid word from above word's list.
def chose_word(words):
    """
    i/p:- list of words.
    o/p:- chose single valid word.
    """
    word_chosen=random.choice(words)
    while '\'' in word_chosen or '-' in word_chosen:
        word_chosen=random.choice(words)
    return word_chosen.upper()

print(chose_word(words_list))
