
from state import State
from action import Action
from copy import deepcopy


class AgentZach:
    def __init__(self):
        self.history = []
        self.delta_i = 0

    def get_initial(self, marker: chr, state: State) -> Action:
        initial = Action(
            int(state.rows/2),
            int(state.cols/2))
        while not state.action_valid(marker, initial):
            initial.x += 1
            if initial.x == state.cols:
                initial.x = 0
                initial.y += 1
                if initial.y == state.rows:
                    initial.y = 0
        return initial

    def compute_action(self, marker: chr, state: State) -> Action:
        if len(self.history) == 0:
            initial = self.get_initial(chr, state)
            self.history.append(initial)
            return initial

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
        initial_delta_i = self.delta_i
        success = False
        action = None
        while not success:
            self.delta_i = initial_delta_i
            while True:
                action = deepcopy(self.history[-1])
                delta = deltas[self.delta_i]
                action.x += delta[0]
                action.y += delta[1]
                if not state.action_valid(marker, action):
                    self.delta_i = (self.delta_i + 1) % len(deltas)
                    if self.delta_i == initial_delta_i:
                        break
                else:
                    success = True
                    break
            if not success:
                self.history = self.history[:-1]
                if len(self.history) == 0:
                    initial = self.get_initial(chr, state)
                    self.history.append(initial)
                    return initial
        self.history.append(action)

        return action
