from random import choice
word=choice (["seminar","command","company","sycamore","compass","bank","binding","perennial","stapler","lathe","doctor","guarantee","settlement","trust","partentity","mercury","terrible","trunk","oust","weight","truth","suburb","binder","coupon","superior","barometer","subject","comfortly","ricbacker","canyonhalter","technology","expectation","pleasant","is","lander","reliable","mind","flight","freedom","calendar","partner","ship","dripping","lance","develop","opportunity","garden","fertilizer","agenda","cope","common","dollar","choral","links","army","lunch","baby","warsaw","upgrade","urn","hear","ingdigest","greenhouse","probability","sun","beam","curriculum","kitchen","ware","misconduct","shareholder", "pneumonoultramicroscopicsilicovolcanoconiosis"])
letter_guessed = []
wrong = []
def processes():
  tries = 6
  while tries>=0:
    output = ""
    for letter in word:
      if letter in letter_guessed:
        output += letter
      else: 
        output += "_"

    if output == word:
      break

    print("Guess this word: ", output)
    print(tries, "tries left")
    guess = input("Choose a letter: ")

    if guess in letter_guessed or guess in wrong:
      print('You already guessed that')
    elif guess in word:
      print ("You got it!")
      letter_guessed.append(guess)
    else: 
      print("Wrong dumbass!")
      tries -= 1
      wrong.append(guess)
    print()
  if output==word:
    print(f"You guessed the word! It was {word}")
  else:
    print(f"You lost bitch! It was {word}")
