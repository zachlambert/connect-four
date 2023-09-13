
import sys
from state import State
from action import Action
import pickle

class RandomAgent:
    def __init__(self):
        pass
    def compute_action(self, marker: chr, state: State) -> Action:
        action = Action()
        action.x = 0
        action.y = 0
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

def save_agent(file_name, agent):
    pickle.dump(agent, open(file_name, 'wb'))

def main():
    state = State(10, 10)

    agent_pickles = sys.argv[1:]
    agents = [ManualAgent()]
    markers = ['x', 'o', '*', '?']

    for file_name in agent_pickles:
        agents.append(pickle.load(open(file_name, 'rb')))

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
            print(f'Invalid action ({action.x}, {action.y})')
        else:
            print(f'Valid action ({action.x}, {action.y})')
        state.update(marker, action)
        input('Press enter to continue')
        agent_i += 1

    pickle.load()

    print(state)
    state.update('x', RandomAgent().compute_action('x', state))
    print(state)

if __name__ == "__main__":
    main()
