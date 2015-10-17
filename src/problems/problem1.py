





class Problem1():

	def __init__(self, fileName):
		fileHandle = open(fileName, 'r')
	
		for line in fileHandle:
			self.dnaString = line		


	def solve():

		solutionCount = {}
		solutionCount['A'] = 0
		solutionCount['C'] = 0
		solutionCount['G'] = 0
		solutionCount['T'] = 0

		for i in range(len(self.dnaString)):
			solutionCount[self.dnaString[i]]++

		print(solutionCount['A'] + ' ' + solutionCount['C'] + ' ' + solutionCount['G'] + ' ' + solutionCount['T'])