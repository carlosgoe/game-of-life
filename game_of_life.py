from environment import Environment
from time import sleep
import random
import copy

# Initial environment of size rows*columns
rows = 5
columns = 10
env = Environment(rows, columns)


# Plus one generation
def t_plus_1():
    old_env = copy.copy(env)
    for i in range(len(old_env.matrix)):
        for n in range(len(old_env.matrix[0])):
            if old_env.alive_neighbors(i, n) < 2 or old_env.alive_neighbors(i, n) > 3:
                env.set_dead(i, n)
            elif not old_env.alive[(i, n)] and old_env.alive_neighbors(i, n) == 3:
                env.set_alive(i, n)
    env.print_env()


# Generates a random initial state of alive and dead cells
def generate():
    for i in range(rows):
        for n in range(columns):
            if random.choice([True, False]):
                env.set_alive(i, n)
    env.print_env()


# Used to set initial state manually
def initial_state(*positions):
    for p in positions:
        env.set_alive(*p)
    env.print_env()


# Starts game of life with the default time between generations being 1s
def start(delay=1):
    t = 0
    while True:
        if env.all_dead():
            break
        t_plus_1()
        t += 1
        print('\nTime: ' + str(t))
        print('Population: ' + str(env.population()))
        print('Size: ' + str(env.size()))
        sleep(delay)
    print('No living cell left.')
