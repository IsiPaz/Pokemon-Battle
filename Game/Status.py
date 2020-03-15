class Status:

	def __init__(self, status, probability):

		self.__Status = status
		self.__Probability = probability

	def getStatus(self):
		return self.__Status

	def getProbability(self):
		return self.__Probability