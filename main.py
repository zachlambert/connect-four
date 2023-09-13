
from state import State
from action import Action
import pickle

class RandomAgent:
    def __init__(self):
        pass
    def compute_action(self, marker: chr, state: State) -> Action:
        action = Action(0, 0)
        return action

class ManualAgent:
    def __init__(self):
        pass
    def compute_action(self, marker: chr, state: State) -> Action:
        valid = False
        print(f'Size: (state.cols, state.rows)')
        action = Action()
        while True:
            try:
                coords = [int(char) for char in input().split(' ')]
            except ValueError:
                print('Invalid')
                continue
            if len(coords) != 2:
                print('Invalid')
                continue
            if coords[0] < 0 or coords[1] < 0 or coords[0] >= state.cols or coords[1] >= state.rows:
                print('Invalid')
                continue
            action.x = int(coords[0])
            action.y = int(coords[1])
            break
        return action

def main():
    state = State(10, 10)

    agent_pickles = []
    agents = [ManualAgent()]
    markers = ['x', 'o', '*', '?']

    for file_name in agent_pickles:
        # TODO: Check this is correct
        agents.append(pickle.load(open(file_name, 'r')))

    agent_i = 0
    n = 0
    while state.winner is None:
        print(f'Iteration {n}')
        print(state)
        marker = markers[agent_i]
        agent = agents[agent_i]
        print(f'Agent {marker} makes action:')
        action = agent.compute_action(marker, state)
        if not state.action_valid(marker, action):
            print('Invalid action')
        else:
            print(f'Valid action ({action.x}, {action.y})')
        state.update(marker, action)
        input('Press enter to continue')

    pickle.load()

    print(state)
    state.update('x', RandomAgent().compute_action('x', state))
    print(state)

if __name__ == "__main__":
    main()
