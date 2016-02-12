class queueViaStacks():
	def __init__(self):
		self.s1=[]
		self.s2=[]
	def add(self,item):
		if len(self.s2)>=0:
			for i in range (len(self.s2)-1,-1,-1):
				self.s1.append(self.s2.pop())
		self.s1.append(item)
	def remove(self):
		if len(self.s1)>=0:
			for i in range (len(self.s1)-1,-1,-1):
				self.s2.append(self.s1.pop())
		return(self.s2.pop())

s=queueViaStacks()
s.add(1)
s.add(2)
s.remove()
s.add(3)
s.add(4)
s.add(5)

