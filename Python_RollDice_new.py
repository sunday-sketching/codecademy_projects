# https://docs.python.org/2/library/random.html

"""Guess numbers, guys."""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Your guess is too big."
  else:
    print "Rolling..."
    sleep(2)
    print "Your first roll is: %d" % first_roll
    sleep(1)
    print "Your second roll is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess > total_roll:
      print "YOU WON"
    else:
      print "YOU LOST"
    
roll_dice(6)