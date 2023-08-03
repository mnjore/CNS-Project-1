import math

from pox.core import core

log = core.getLogger()

class Entropy(object):

	# Variable counter stores number of ips in list
	# while the variable value stores the entropy value
	counter = 0
	value = 1
	# hashTable and ipList store the ip information used for calculation
	hashTable = {}
	ipList = []

	# This function collects the ip addresses & creates the hash table
	def ipCollect(self, element):
		'''
		print("Testing values")
		print("counter = " + str(self.counter))
		print("Length of ipList is ")
		print(len(self.ipList))
		print("$$$$$$$$")
		'''
		# Initalising the counter n for the hash table
		n = 0
		self.counter +=1
		self.ipList.append(element)
		if self.counter == 50:
		# Loop creating the hashtable
			for ip in self.ipList:
				n +=1
				if ip not in self.hashTable:
					self.hashTable[ip] =0
				self.hashTable[ip] +=1
			self.calculateEntropy(self.hashTable)
			'''
			log.info(self.hashTable)
			log.info(self.value)
			'''
			# Clearing the iplist, hashtable and counter
			self.hashTable = {}
			self.ipList = []
			n = 0
			self.counter = 0

	# The function to calculate the entropy value
	def calculateEntropy(self, lists):
		'''
		print("calculateEntropy function called")
		'''
		n = 50
		elist = []
		for a,b in lists.items():
			'''
			log.info("b =")
			log.info(b)
			log.info("b belongs to ")
			log.info(a)
			log.info("n =")
			log.info(n)
			'''
			c = b/float(n)
			'''
			log.info("Value of c is ")
			log.info(c)
			'''
			c = abs(c)
			
			# Calculating entropy of each ip
			elist.append(-c * math.log(c, 2))
			'''
			log.info("Entropy = ")
			log.info(sum(elist))
			log.info("$$$$$$$")
			'''			
			# Calculating final entropy value using sum
			self.value = sum(elist)

	def __init__(self):
		pass