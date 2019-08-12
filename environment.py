import os
import numpy as np


class Environment:

    # Creates environment
    def __init__(self, rows, columns, custom=None):
        self.matrix = np.random.randint(0, 2, (rows, columns)) if custom is None else np.array(custom)
        positions = np.argwhere(self.matrix == 1)
        if positions.size > 0:
            self.matrix = self.matrix[np.min(positions[:, 0]):np.max(positions[:, 0]) + 1, np.min(positions[:, 1]):np.max(positions[:, 1]) + 1]
        else:
            self.matrix = np.empty((0, 0))
    
    # Applies rules to get next state
    def next_state(self):
        positions = np.argwhere(self.matrix == 1)
        if np.min(positions[:, 1]) == 0:
            self.matrix = np.concatenate((np.zeros((self.matrix.shape[0], 1)), self.matrix), axis=1)
        if np.max(positions[:, 1]) == self.matrix.shape[1] - 1:
            self.matrix = np.concatenate((self.matrix, np.zeros((self.matrix.shape[0], 1))), axis=1)
        if np.min(positions[:, 0]) == 0:
            self.matrix = np.concatenate((np.zeros((1, self.matrix.shape[1])), self.matrix), axis=0)
        if np.max(positions[:, 0]) == self.matrix.shape[0] - 1:
            self.matrix = np.concatenate((self.matrix, np.zeros((1, self.matrix.shape[1]))), axis=0)
        new_env = np.zeros((self.matrix.shape[0], self.matrix.shape[1]))
        for r in range(self.matrix.shape[0]):
            for c in range(self.matrix.shape[1]):
                n_alive = 0
                if r > 0 and self.matrix[r - 1, c] == 1:
                    n_alive += 1
                if r < self.matrix.shape[0] - 1 and self.matrix[r + 1, c] == 1:
                    n_alive += 1
                if c > 0 and self.matrix[r, c - 1] == 1:
                    n_alive += 1
                if c < self.matrix.shape[1] - 1 and self.matrix[r, c + 1] == 1:
                    n_alive += 1
                if c > 0 and r > 0 and self.matrix[r - 1, c - 1] == 1:
                    n_alive += 1
                if c < self.matrix.shape[1] - 1 and r > 0 and self.matrix[r - 1, c + 1] == 1:
                    n_alive += 1
                if c > 0 and r < self.matrix.shape[0] - 1 and self.matrix[r + 1, c - 1] == 1:
                    n_alive += 1
                if c < self.matrix.shape[1] - 1 and r < self.matrix.shape[0] - 1 and self.matrix[r + 1, c + 1] == 1:
                    n_alive += 1
                if (self.matrix[r, c] == 0 and n_alive == 3) or (self.matrix[r, c] == 1 and 2 <= n_alive <= 3):
                    new_env[r, c] = 1
        positions = np.argwhere(new_env == 1)
        if positions.size > 0:
            self.matrix = new_env[np.min(positions[:, 0]):np.max(positions[:, 0]) + 1, np.min(positions[:, 1]):np.max(positions[:, 1]) + 1]
        else:
            self.matrix = np.empty((0, 0))
        return int(np.sum(self.matrix)), '{0}x{1}'.format(self.matrix.shape[0], self.matrix.shape[1])

    # Prints environment
    def print_env(self):
        print(' ' + str(self.matrix).replace('.', '').replace(']', '').replace('[', '').replace('0', ' ').replace('1', '■'))
