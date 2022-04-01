def CreateCard(n):
  global flashcards
  global m
  m = n
  flashcards = []
  FillCards()

  
def FillCards():
  for i in range(m):
    term = input("Please add a term. ")
    definition = input("Please add a definition ")
    flashcards.append([term, definition])
  form = input("View your cards or study in test form? enter view or test? ")
  choice(form)

def choice(form):
  if form == "test":
    Study(input("Would you like to study by terms or definitions? ")) #list user options
  if form == "view":
    View()
    
  
def View():
  for i in range(m):
    print(flashcards[i][0]+  ": "+  flashcards[i][1])


def Study(choice):
  answ = ""
  if(choice == "terms"):
    while answ != "stop":
      for i in range(m):
        print(flashcards[i][0])
        ans = input("What is the answer to " + flashcards[i][0] + "? ")
        answ = ans
        if(ans == flashcards[i][1]):
          print("Correct!")
        elif(ans == "stop"):
          print()
        else:
          print("Not quite, the answer was: " + flashcards[i][1])
  elif(choice == "definitions"):
    for i in range(m):
      print(flashcards[i][1])
      ans = input("What is the answer to " + flashcards[i][1] + "? ")
      if(ans == flashcards[i][0]):
        print("Correct!")
      elif(ans == "stop"):
        print()
      else:
        print("Not quite, the answer was: " + flashcards[i][0])
  else:
    print("Invalid input")





CreateCard(int(input("How much flashcards would you like to create? ")))