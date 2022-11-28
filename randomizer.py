import random
list_of_words=["seminar","command","company","sycamore","compass","bank","binding","perennial","stapler","lathe","doctor","guarantee","settlement","trust","partentity","mercury","terrible","trunk","oust","weight","truth","suburb","binder","coupon","superior","barometer","subject","comfortly","ricbacker","canyonhalter","technology","expectation","pleasant","is","lander","reliable","mind","flight","freedom","calendar","partner","ship","dripping","lance","develop","opportunity","garden","fertilizer","agenda","cope","common","dollar","choral","links","army","lunch","baby","warsaw","upgrade","urn","hear","ingdigest","greenhouse","probability","sun","beam","curriculum","kitchen","ware","misconduct","shareholder"]



def randomWord():
  word=random.choice(list_of_words)
  splits=list(word)
  spaces=len(splits)
  # return word
  # return splits
  # return spaces
  my_list = [ ]
  while len(my_list) < len(spaces):
    my_list.append('_')
  return(my_list)
    
  makeList = (randomWord(word))
  print(f"Ok I have picked a word it has {spaces} letters in it. Try to guess")
  print(makeList)
