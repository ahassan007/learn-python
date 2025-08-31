
from math import pi # This will allow us to use print(pi) without having to make a ref to maht.pi
import math

import random as rdm # allows you to change the value from random to rdm e.g rdm.random

import kansas

from rps7 import rock_paper_scissors

import rps7

print(math.pi)

print(pi) # Same result as the above

# How to check all the function availiable in a module 

# for item in dir(rdm):
#     print(item)

print(kansas.capital)

kansas.randomfunfact()

print(__name__) # This prints the name of the current module which should be __main__

print(kansas.__name__) # This should print the name of the kansas module 

#RUns the module 
rock_paper_scissors()

# The below code does the same as the above 
#run = rps7.rps()

#run()