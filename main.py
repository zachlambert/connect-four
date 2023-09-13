
from state import State
from action import Action

class RandomAgent:
    def __init__(self):
        pass
    def compute_action(self, marker: chr, state: State) -> Action:
        action = Action(0, 0)
        return action

def main():
    state = State(10, 10)
    print(state)
    state.update('x', RandomAgent().compute_action('x', state))
    print(state)

if __name__ == "__main__":
    main()
