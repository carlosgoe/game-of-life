from environment import Environment
from time import sleep
import os

# Set number of rows and columns for initial state
rows = 8
columns = 8

# Create and print initial environment
env = Environment(rows, columns)
env.print_env()

# Set inital values
population = None
t = 0

# Run Game of Life until population is 0
while population != 0:
    sleep(0.125)
    population, size = env.next_state()
    t += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    env.print_env()
    print('\nTime: {0}\nPopulation: {1}\nSize: {2}'.format(t, population, size))
