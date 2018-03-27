import os


class Environment:

    # Creates environment setting every cell's status to dead
    def __init__(self, rows, columns):
        self.matrix = []
        self.alive = {}
        for i in range(rows):
            r = []
            for n in range(columns):
                r.append(' ')
                self.alive[(i, n)] = False
            self.matrix.append(r)

    # Sets certain cell alive
    def set_alive(self, row, column):
        self.matrix[row][column] = '□'
        self.alive[(row, column)] = True
        if row == len(self.matrix) - 1:
            self.add_row()
        if column == len(self.matrix[0]) - 1:
            self.add_column()

    # Sets certain cell dead
    def set_dead(self, row, column):
        self.matrix[row][column] = ' '
        self.alive[(row, column)] = False

    # Prints environment
    def print_env(self):
        os.system('cls')
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                print(self.matrix[i][n], end='')
            print()

    # Returns whether every cell is dead
    def all_dead(self):
        states = list(self.alive.values())
        for s in states:
            if s:
                return False
        return True

    # Returns current population
    def population(self):
        ppl = 0
        states = list(self.alive.values())
        for s in states:
            if s:
                ppl += 1
        return ppl

    # Returns size of matrix as string
    def size(self):
        return str(len(self.matrix)) + 'x' + str(len(self.matrix[0]))

    # Returns number of certain cell's alive neighbors
    def alive_neighbors(self, row, column):
        n_alive = 0
        if row > 0 and self.alive[(row - 1, column)]:
            n_alive += 1
        if row < len(self.matrix) - 1 and self.alive[(row + 1, column)]:
            n_alive += 1
        if column > 0 and self.alive[(row, column - 1)]:
            n_alive += 1
        if column < len(self.matrix[0]) - 1 and self.alive[(row, column + 1)]:
            n_alive += 1
        if column > 0 and row > 0 and self.alive[(row - 1, column - 1)]:
            n_alive += 1
        if column < len(self.matrix[0]) - 1 and row > 0 and self.alive[(row - 1, column + 1)]:
            n_alive += 1
        if column > 0 and row < len(self.matrix) - 1 and self.alive[(row + 1, column - 1)]:
            n_alive += 1
        if column < len(self.matrix[0]) - 1 and row < len(self.matrix) - 1 and self.alive[(row + 1, column + 1)]:
            n_alive += 1
        return n_alive

    # Expands matrix by new row of dead cells
    def add_row(self):
        row = []
        for i in range(len(self.matrix[0])):
            row.append(' ')
            self.alive[(len(self.matrix), i)] = False
        self.matrix.append(row)

    # Expands matrix by new column of dead cells
    def add_column(self):
        for i in range(len(self.matrix)):
            self.alive[(i, len(self.matrix[i]))] = False
            self.matrix[i].append(' ')
