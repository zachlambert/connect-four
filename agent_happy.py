from action import Action
from state import State
from random import randrange
import pickle

class AgentHappy:
    def compute_action(self, marker, state) -> Action:
        action = Action(8, 8)
        # for i in range(state.rows):
        #     for j in range(state.cols):
        #         current = state.data[j*state.cols + i]
                           
        #         if current == " ":
        #              action.x = i
        #              action.y = j
        #         return action
        #     else:
        action.x = randrange(1, 9, 1)
        action.y = randrange(1, 9, 1)
        return action
            
#make love not war
#this was fun