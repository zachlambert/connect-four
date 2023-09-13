
import sys
from state import State
from action import Action
import pickle
from random import randint

class RandomAgent:
    def __init__(self):
        pass
    def compute_action(self, marker: chr, state: State) -> Action:
        while True:
            action = Action(randint(0, state.cols-1), randint(0, state.rows-1))
            if state.action_valid(marker, action):
                break
        return action

class ManualAgent:
    def __init__(self):
        pass
    def compute_action(self, marker: chr, state: State) -> Action:
        valid = False
        print(f'Size: ({state.cols}, {state.rows})')
        action = Action(0,0)
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
    state = State(10, 10, 5)

    agent_pickles = sys.argv[1:]
    agents = [RandomAgent(), ManualAgent()]
    markers = ['x', 'o', '*', '?']

    for file_name in agent_pickles:
        agents.append(pickle.load(open(file_name, 'rb')))

    agent_i = 0
    n = 0
    valid_actions = 0
    while state.winner is None and valid_actions < state.rows*state.cols:
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
            valid_actions += 1
        state.update(marker, action)
        agent_i = (agent_i + 1) % len(agents)
        n += 1

    if state.winner is None:
        print('Game ended with no valid moves remaining and no winner')
    else:
        print(f'Game ended with winner {state.winner}')

if __name__ == "__main__":
    main()
