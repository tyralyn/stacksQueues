class singleArrayNStacks:
	def __init__(self, numStacks, arrayLength):
		self.numStacks=numStacks
		self.arrayLength=arrayLength
		self.l = [None]*arrayLength
		self.startIndices=[]
		self.topOfStack=[]
		j = 0
		for i in range (0,numStacks):
			self.startIndices.append(j)
			self.topOfStack.append(j)
			if i < arrayLength%numStacks:
				j += (arrayLength//numStacks) + 1
			else:
				j += arrayLength//numStacks
	def stackFull(self, stackId):
		nextStackId=(stackId+1)%self.numStacks
		if self.topOfStack[stackId]==self.startIndices[nextStackId]:
			return True	
		else:
			return False
	def stackEmpty(self, stackId):
		if self.topOfStack[stackId]==self.startIndices[stackId]:
			return True	
		else:
			return False
	def push(self, item, stackId):
		if self.stackFull(stackId):
			return "can't add to stack, stack full"
		else:
			self.l[self.topOfStack[stackId]]=item
			self.topOfStack[stackId]+=1
	def pop(stackId):
		if self.stackEmpty(stackId):
			return "can't pop, stack is empty"
		else:
			r=self.l[self.topOfStack[stackId]]
			self.l[self.topOfStack[stackId]-1]=None
			self.topOfStack[stackId]-=1
			return r
	def printStacks(self):
		for i in range (0, self.numStacks):
			print("stack ",i,": ", ', '.join(self.l[self.startIndices[i]:self.topOfStack[i]]))
