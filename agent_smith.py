from main import Action, State

class AgentSmith:
    def __init__(self):
        pass
    def compute_action(self, marker: chr, state: State) -> Action:
        for y in range(0,state.rows):
            for x in range(0,state.cols):
                print(state.rows,state.cols)
                print(x,y,)
                print(state.read(x,y))
                if state.read(x,y) == " ":
                    print("doing", x,y)
                    return Action(x,y)

