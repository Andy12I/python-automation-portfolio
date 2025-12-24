#guess the number game
import random #import random

number = random.randint(1,100) #pick number between 1 and 100


while True: #start a while loop
  
  guess = input("guess a number. ") #ask user for a guess
  
  try :
   guess = int(guess) #make the guess an integer
  except ValueError:
    print("Hey! That's not a number. Try again.")
    continue
  
  if guess<number:
    print("Too low!")
  elif guess>number:
    print("Too high!")
  else :
    print("You won!")
    break