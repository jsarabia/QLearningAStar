import heapq
import math

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def push(self, loc, priority):
        insert = (priority, loc)
        heapq.heappush(self.elements, insert)

    def pop(self):
        (priority, loc) = heapq.heappop(self.elements)
        return loc


def heuristic(current, goal):
    (x1, y1) = current
    (x2, y2) = goal
    return math.sqrt(pow(abs(x1 - x2),2) + pow(abs(y1 - y2),2))

def aStar(grid, start, goal):
    open_nodes = PriorityQueue()
    open_nodes.push(start, 0)
    return_paths = {}
    gcost = {} #cost from start to current node
    fcost = {} #cost from start to current node + cost from current node to end
    hcost = {} #cost from current node to end.
    return_paths[start] = None
    gcost[start] = 0
    hcost[start] = heuristic(start, goal)
    fcost[start] = gcost[start] + heuristic(start, goal)
    
    while not len(open_nodes.elements) == 0:
        current = open_nodes.pop()
        
        if current == goal:
            return return_paths, gcost, hcost, fcost
        
        for next in grid.adjacent(current):
            new_cost = gcost[current] + grid.weight(next)
            if next not in gcost or new_cost < gcost[next]:
                gcost[next] = new_cost
                hcost[next] = heuristic(goal, next)
                fcost[next] = new_cost + heuristic(goal, next)
                open_nodes.push(next, fcost[next])
                return_paths[next] = current

    print("a_star failure")
    return return_paths, gcost, hcost, fcost

def draw_grid(grid, list, start, goal,):
    for y in range(grid.rows):
        for x in range(grid.cols):
            if start == (x, y):
                print("START\t", end="")
            elif goal == (x, y):
                print("GOAL\t", end="")
            elif (x, y) in grid.walls:
                print("x\t", end="")
            elif (x, y) in list:
                print("%.1f\t" % list[(x, y)], end="")
            else:
                print("-\t", end="")
        print()
    print()

def reconstruct_path(self, return_paths, start, goal):
    current = goal
    path = [current]
    while current in return_paths:
        current = return_paths[current]
        path.append(current)
    path.reverse()
    for y in path:
        print (y)
    return path