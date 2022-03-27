#Guess the number 
import random
import math
#Random Integer
lower = 1
upper = 99
x=random.randint(lower,upper)
# Algo
print("You have 7 tries to guess the correct number on the basis of high and low.\n The number is between 0 and 100 \n All the best!")
count =0
while count < 7:
  count +=1

  guess = int(input("Guess the number: "))

  if guess == x:
    print("Congratulations you guessed the correct number in ", count , "attempt")
    break
  elif guess > x:
    print("Your guess is too high")
    
  elif guess < x:
    print("Your guess is too small")
    

if count == 7:
  print("OOPS! you ran out of tries, Better Luck next time.")
  print("The correct answer is ", x)

