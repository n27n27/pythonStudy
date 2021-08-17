import random
from enum import Enum

class RPS(Enum):
    ROCK = 0, 
    PAPER = 1,
    SCISSORS = 2

print(RPS.ROCK == RPS.PAPER)
