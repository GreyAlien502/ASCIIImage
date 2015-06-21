import manipulate

class sprite:
	def __init__(self,n,state):
		self.n = n
		self.state = state
	def __str__(self):
		output = "\n"
		for i in range(len(self.state)):
			output = manipulate.overlay(
				output,
				str(self.n[self.state[i][0]]),
				self.state[i][1],
				self.state[i][2])
		return output
