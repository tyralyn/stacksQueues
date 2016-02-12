# a value of true in the animalShelter class corresponds to a cat

class animalShelter:
	def __init__(self):
		self.stack=[]
		self.temp=[]
	def enQ(self,item):
		self.stack.append(item)
	def deQCat(self):
		for i in range (0, len(self.stack)):
			if self.stack[i]:
				r = self.stack[i]
				self.stack.remove(i)
				return r
	def deQDog(self):
		for i in range (0, len(self.stack)):
			if not self.stack[i]:
				r = self.stack[i]
				self.stack.remove(i)
				return r 
	def deQAny(self):
		r = self.stack[0]
		self.stack.remove(0)
		return r

a = animalShelter()
a.enQ(False)
a.enQ(False)
a.enQ(True)
a.enQ(False)
a.enQ(False)
a.enQ(False)
a.enQ(True)
a.enQ(True)