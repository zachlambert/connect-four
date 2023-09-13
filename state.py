
from action import Action

class State:
    def __init__(self, rows, cols, win_count):
        self.rows = rows
        self.cols = cols
        self.win_count = win_count
        self.data = [' ' for i in range(rows * cols)]
        self.winner = None

    def read(self, x, y) -> chr:
        return self.data[y*self.cols + x]

    def write(self, x, y, value):
        self.data[y*self.cols + x] = value

    def __repr__(self):
        divider = '----' * self.cols + '-'
        full = ''
        for y in range(self.rows-1, -1, -1):
            row = ''
            for x in range(self.cols):
                row += '| ' + self.read(x, y) + ' '
            row += '|'
            full += divider + '\n' + row + '\n'
        full += divider
        return full

    def action_in_bounds(self, marker: chr, action: Action) -> bool:
        if action.x < 0 or action.y < 0 or action.x >= self.cols or action.y >= self.rows:
            return False
        return True

    def action_valid(self, marker: chr, action: Action) -> bool:
        if not self.action_in_bounds(chr, action):
            return False
        if self.read(action.x, action.y) != ' ':
            return False
        return True

    def update(self, marker: chr, action: Action):
        self.write(action.x, action.y, marker)

        deltas = [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1)
        ]
        for delta in deltas:
            x = action.x
            y = action.y
            count = 0
            while count < self.win_count:
                x += delta[0]
                y += delta[1]
                if x < 0 or y < 0 or x >= self.cols or y >= self.rows:
                    break
                if self.read(x, y) != marker:
                    break
                count += 1
            if count == self.win_count:
                self.winner = marker
                break

        return True
