class Grid:
	def __init__(self):
		self.world = []
	def readFile(self, path):
		with open(path, "r") as ifs:
			for line in ifs:
				ls = [x in line]
				self.world.append(ls)

g = Grid()
g.readFile("file.txt")