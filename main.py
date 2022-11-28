from chose import ask_user
from randomizer import randomWord

#intro 
name=input('What is your name?')
print(f"Welcome to hangman, {name}, I will pick a word and you have 6 lives to guess that word, if you get a letter wrong you will lose a life. Good luck!")

#pick word
randomWord()
ask_user()
