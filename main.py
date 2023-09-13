

class State:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.state = [0 for i in range(rows * cols)]
        self.height = [0 for i in range(cols)]
        self.winner = None

    def get_(self, x, y):
        return state[y*self.cols + x]

    def set(self, x, y):
        return state[y*self.cols + x]

    def __repr__(self):
        for x in range(self.rows-1, 0, -1):
            row = ""
            for y in range(self.cols):
                row += self.get(x, y)
            print(row)

class Action:
    def __init__(self):
        pass

class Agent:
    def __init__(self):
        pass
    def policy(self, state: State) -> Action:
        pass

def main():
    state = State(10, 10)
    pass

if __name__ == "__main__":
    main()
