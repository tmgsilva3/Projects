import random

def randarith():
  a = random.randint(1,10)
  b = random.randint(1,10)
  c = a + b
  answer = int(input("{} + {} = ".format(a, b)))
  if (c == answer):
      print("You got it!")  
  else:
      print("Incorrect!")
  

def numarith():
  a = int(input("Insert first number: "))
  b = int(input("Insert second number: "))
  c = a + b
  answer = int(input("{} + {} = ".format(a, b)))
  if (c == answer):
      print("You got it!")
  else:
      print("Incorrect!")
      
      
def repeat():
    answer = input("Do you want to go again? Yes or No?\n")
    if(answer.lower() == 'yes'):
        answer2 = input("Which mode 'Random' or 'Fixed' mode?\n")
        if(answer2.lower() == 'random'):
            randarith()
            repeat()
        elif(answer2.lower() == 'fixed'):
            numarith()
            repeat()
        else:
            print("Choose a valid choice.")
    elif(answer.lower() == 'no'):
        pass
  

print("""Hello! Welcome to the Calculator Game
Here you can test your Math skills and practice all sorts of arithmetic
You can choose many levels and the numbers are generated randomly (available soon!)
Enjoy!""")

c = input("Would you like random numbers or fixed numbers? Choose 'random' or 'fixed'\n")

if(c.lower() == 'random'):
  randarith()
  repeat()

elif(c.lower() == 'fixed'):
  numarith()
  repeat()
else:
  print("Choose a valid choice.")
