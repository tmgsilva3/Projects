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
  pass
  

print("""Hello! Welcome to the Calculator Game
Here you can test your Math skills and practice all sorts of arithmetic
You can choose many levels and the numbers are generated randomly (available soon!)
Enjoy!""")

c = input("Would you like random numbers or fixed numbers? Choose 'random' or 'fixed'")

if(c.lower() == 'random'):
  randarith()

elif(c.lower() == 'fixed'):
  numarith()

else:
  print("Choose a valid choice.")
