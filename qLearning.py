import random as rnd

def qLearning(self, start, goal):
    q_table = []
    qInit(q_table, self.world, goal)
    printQTable(q_table)
    printRewards(q_table)
    for i in range(1000):
        y = rnd.randint(0, len(q_table)-1)
        x = rnd.randint(0, len(q_table[y])-1)
        episode(self.world, q_table, q_table[y][x], 0, .5)
    printRewards(q_table)

#gets neighbors, updates the reward, and then moves to the next state
#returns if depth exceeded, goal reached, or an invalid state reached
def episode(world, qt, state, depth, gamma):
    if(depth>150):
        return 0
    pos = state.getPosition()
    x = pos[0]
    y = pos[1]
    if(world[y][x] == "x"):
        return 0
    if(qt[y][x].getReward() == 100):
        return
    neighbors = getNeighbors(world, qt, state)
    chosenState = nextState(qt,neighbors)
    chosenState.visit()
    qt[y][x].setReward(state.getReward() + gamma*chosenState.getReward()*(1.0/2**chosenState.timesVisited()))

    episode(world, qt, nextState(qt, neighbors), depth+1, gamma)

#looks u/d/l/r for valid neighbors and adds them to a list
def getNeighbors(world, qt, state):
    neighbors = []
    pos = state.getPosition()
    x = pos[0]
    y = pos[1]
    n = len(qt)
    m = len(qt[y])

    if(x+1 < m and qt[y][x+1] != "x"):
        neighbors.append(qt[y][x+1])
    if(x-1 >= 0 and qt[y][x-1] != "x"):
        neighbors.append(qt[y][x-1])
    if(y+1 < n and qt[y+1][x] != "x"):
        neighbors.append(qt[y+1][x])
    if(y-1 >=0 and qt[y-1][x] != "x"):
        neighbors.append(qt[y-1][x])
    
    return neighbors

#given a list of neighboring states, the one with the highest reward is returned
def nextState(qt, neighbors):
    index = 0
    maxReward = 0
    i = 0
    for x in neighbors:
        if(x.getReward() > maxReward):
            maxReward = x.getReward()
            index  = i 
        i+=0
    if (maxReward == 0):
        index = rnd.randint(0,len(neighbors)-1)
    return neighbors[index]

def qInit(qt, world, goal):
    n = len(world)
    m = len(world[0])   
    for y in range(n):
        ls = []
        for x in range(m):
            temp = State(x,y)
            if(world[y][x] == "x"):
                temp.addAction("invalid", 0)
            if(x+1 < m and world[y][x+1] != "x"):
                temp.addAction("right", 0)
            if(x-1 >= 0 and world[y][x-1] != "x"):
                temp.addAction("left", 0)
            if(y+1 < n and world[y+1][x] != "x"):
                temp.addAction("down", 0)
            if(y-1 >=0 and world[y-1][x] != "x"):
                temp.addAction("up", 0)
            if(y == goal[1] and x == goal[0]):
                temp.setReward(100)
            ls.append(temp)
        qt.append(ls)

def printQTable(qt):
    for y in range(len(qt)):
        for x in range(len(qt[y])):
            string = "State " + str(qt[y][x].getPosition()) + "'s Actions: " + str(qt[y][x].getActions())
            print(string)

def printRewards(qt):
    for y in range(len(qt)):
        string = ""
        for x in range(len(qt[y])):
            string += str(qt[y][x].getReward()) + " "
        print(string)
class State:
    def __init__(self, x, y):
        self.position = (x, y)
        self.actions = {}
        self.reward = 0
        self.visited = 0
    def addAction(self,direction, value):
        self.actions[direction] = value
    def getPosition(self):
        return self.position
    def getActions(self):
        return self.actions
    def setReward(self, reward):
        self.reward = reward
    def getReward(self):
        return self.reward
    def visit(self):
        self.visited+=1
    def timesVisited(self):
        return self.visited    


