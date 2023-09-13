from myagent import AgentSmith
import pickle

agent = AgentSmith()
filehandler = open(b"agentSmith.obj","wb")
pickle.dump(agent, filehandler)
filehandler.close()
