
from action import Action

class State:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [' ' for i in range(rows * cols)]
        self.winner = None

    def read(self, x, y) -> chr:
        return self.data[y*self.cols + x]

    def write(self, x, y, value):
        self.data[y*self.cols + x] = value

    def __repr__(self):
        divider = '-' * self.cols
        full = divider + '\n'
        for x in range(self.rows-1, -1, -1):
            row = ''
            for y in range(self.cols):
                row += self.read(x, y)
            full += row + '\n'
        full += divider
        return full

    def action_valid(self, marker: chr, action: Action) -> bool:
        if self.read(action.x, action.y) != ' ':
            return False
        return True

    def update(self, marker: chr, action: Action):
        self.write(action.x, action.y, marker)

        # TODO: Check if there is a winner
        # Set winner to the marker of the winner
        winner = None

        return True
