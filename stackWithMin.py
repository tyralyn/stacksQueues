class stackWithMin:
	def __init__(self):
		self.stack=[]
		self.minStack=[]
		self.stackHeight=-1
	def push(self,item):
		if self.stackHeight < 0:
			self.minStack.append(item)
		elif item <= self.minStack[self.stackHeight]:
			self.minStack.append(item)
		else:
			self.minStack.append(self.minStack[self.stackHeight])
		self.stack.append(item)
		self.stackHeight+=1
	def pop(self):
		stackHeight-=1
		self.minStack.pop()
		return (self.stack.pop())
	def min(self):
			return (self.minStack[self.stackHeight])

j=stackWithMin()
j.push(2)
j.push(9)
j.push(1)
j.push(0)
j.push(3)
print(j.stack)
