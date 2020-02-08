#~~Sebastian Hernandez CS 3750 Project 1
#This program will roll a pair of dice. The user must guess the correct 
#sum of the two die. If they guess correctly, they win. If they guess 
#incorrectly, the computer wins
from random import randint
from time import sleep

def intro():
  print("Two dice will be rolled. You must guess the total")
  print("But be careful...")
  sleep(2)
  print("Your life depends on it...")
  sleep(1)

def get_user_guess():
  guess = int(input("What is your guess for the total rolled? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("\nThe maximum possible value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("Your guess is invalid!!!")
    return 1
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is %d" % first_roll)
    sleep(1)
    print("The second roll is %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("The total is %d" % total_roll)
    print("Result...")
    sleep(1)
    if(guess == total_roll):
      print("You're lucky. You get to live...for now")
    else:
      print("You get to take a long, nice nap...at the bottom of the ocean")
    print("\nDare you to try again")
    play = int(input("Enter 1 to play again, or 0 to quit: "))
    return play

intro()
play = 1
while(play == 1):
    play = roll_dice(6)
