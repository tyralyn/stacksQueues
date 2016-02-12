class sortStack:
	def __init__(self):
		self.temp=[]
		self.stack=[]
	def peek(self):
		return (self.stack[-1])
	def pop(self):
		return (self.stack.pop())
	def push(self, item):
		while(True):
			if (self.peek()>=item):
				self.temp.append(self.stack.pop())
			else:
				self.stack.append(item)
				break
		for i in range (0, len(self.temp)):
			self.stack.append(self.temp.pop())

s=sortStack()
s.push(4)
s.push(2)
s.push(10)
