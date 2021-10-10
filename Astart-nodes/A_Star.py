
# -*- coding: utf-8 -*-

# /https://www.youtube.com/watch?v=ob4faIum4kQ

from Queue import PriorityQueue

class State(object):
	def __init__(self,value,parent,start=0,goal=0):
		self.children = []
		self.parent = parent
		self.value = value
		self.dist = 0
		if parent:
			self.path = parent.path[:]
			self.path.append(value)
			self.start = parent.start
			self.goal = parent.goal
		else:
			self.path = [value]
			self.start = start
			self.goal = goal

	def GetDist(self): #não é para fazer nada aqui.
		pass
	def CreateChildren(self): #não é para fazer nada aqui.
		pass

class State_String(State):
	def __init__(self,value,parent,start=0,goal=0):
		super(State_String,self).__init__(value,parent,start,goal)
		self.dist = self.GetDist()

	def GetDist(self):
		if self.value == self.goal:
			return 0
		dist = 0
		for i in range(len(self.goal)):
			letter = self.goal[i]
			dist += abs(i -
				self.value.index(letter))
		return dist

	def CreateChildren(self):
		if not self.children:
			for i in xrange(len(self.goal)-1):
				val = self.value
				val = val[:1] + val[i+1] + val[i] + val[i+2:]
				child = State_String(val,self)
				self.children.append(child)

class AStar_Solver:
	def __init__(self,start,goal): #seta variavéis iniciais, para poder chamar o Solve.
		self.path = []
		self.visistedQueue = []
		self.priorityQueue = PriorityQueue()
		self.start = start
		self.goal = goal

	def Solve(self): 
		startState = State_String(  self.start,
									0,
									self.start,
									self.goal) # determina o estado inicial de acordo com as variaveis que foram entradas posteriormente
		count = 0 
		self.priorityQueue.put((0,count, startState)) # 
		
		while(not self.path and self.priorityQueue.qsize()):
			closestChild=self.priorityQueue.get()[2]
			closestChild.CreateChildren()
			self.visistedQueue.append(closestChild.value)
			for child in closestChild.children:
				if child.value not in self.visistedQueue:
					count+=1
					if not child.dist:
						self.path = child.path
						break
					self.priorityQueue.put((child.dist,count,child))
		if not self.path:
			print "Goal of " + self.goal + "is not possible"
		for i in self.priorityQueue:
			print "do priorityQueue " + i 
		return self.path

##---------------

if __name__ == "__main__":
	start1 = "algo"
	goal1 = "goal"
	print 'começando'
	a = AStar_Solver(start1,goal1)
	a.Solve()
	for i in xrange(len(a.path)):
		print "%d)" %i + a.path[i]

