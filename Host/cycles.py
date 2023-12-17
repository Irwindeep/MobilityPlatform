import sys

class Cycle:
	def __init__(self, name):
		self.name = name
		self.next = None
		self.isAvail = True


class Cycles:
	def __init__(self):
		self.head = None
	def is_empty(self):
		return self.head == None
	def append(self, cycle, avail):
		newCycle = Cycle(cycle)
		if avail == "Available":
			newCycle.isAvail = True
		else:
			newCycle.isAvail = False
		if self.head == None:
			self.head = newCycle
			return
		current = self.head
		while current.next != None:
			current = current.next
		current.next = newCycle
	def printall(self):
		current = self.head
		if current.isAvail == True:
			avail = "Available"
		else:
			avail = "Not_Available"
		while current != None:
			print(f"{current.name} {avail}")
			current = current.next
	def printAvail(self):
		current = self.head
		i = 1
		while current != None:
			if current.isAvail:
				print(f"{i}. {current.name}")
				i += 1
			current = current.next
	def findIndex(self, index):
		i = 0
		current = self.head
		while current != None and i != index:
			if current.isAvail:
				i += 1
			current = current.next
		print(current.name)
				
global cycles
cycles = Cycles()

if __name__ == "__main__":
	if len(sys.argv) == 1:
		with open("/home/Host/Project/cycles.txt", "r") as file:
			for line in file:
				elements = line.split()
				name = elements[0]
				avail = elements[1]
				cycles.append(name, avail)
		cycles.printAvail()
	elif len(sys.argv) == 2:
		index = int(sys.argv[1])-1
		with open("/home/Host/Project/cycles.txt", "r") as file:
			for line in file:
				elements = line.split()
				name = elements[0]
				avail = elements[1]
				cycles.append(name, avail)
			cycles.findIndex(index)
