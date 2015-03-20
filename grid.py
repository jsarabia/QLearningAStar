import aStar
import qLearning

class Grid:
    def __init__(self):
        self.world = []
    def readFile(self, path):
       with open(path, "r") as ifs:
            for line in ifs:
                ls = [x for x in line]
                self.world.append(ls)
    def printWorld(self):
        for x in self.world:
            line = ''
            for y in x:
                line += str(y) + " "
            print(line)

Grid.aStar = aStar.aStar
Grid.qLearning = qLearning.qLearning

g = Grid()
g.readFile("world.txt")
g.printWorld();



