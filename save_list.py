#!/usr/bin/env python3
class LinkedListNode:
	"""A simple implementation of a doubly-linked list"""
	def __init__(self):
		self.prev = None
		self.next = None

	def insert(self, node):
		"""Insert another node before us in the list"""
		if node.prev is not None or node.next is not None:
			raise NotImplementedError("don't support inserting full lists right now")
		node.prev = self.prev
		node.next = self
		self.prev = node
		return node

	def insert_after(self, node):
		"""Insert another node after us in the list"""
		if node.prev is not None or node.next is not None:
			raise NotImplementedError("don't support inserting full lists right now")
		node.next = self.next
		node.prev = self
		self.next = node
		return node


def create_long_list(n: int) -> LinkedListNode:
	if n <= 0:
		raise ValueError("Must be positive number of nodes")
	# Create the first node
	n = n-1
	head = LinkedListNode()
	tail = head
	# Add additional nodes until we have enough
	while n > 0:
		tail = tail.insert_after(LinkedListNode())
		n -= 1
	return head


if __name__ == '__main__':
	import pickle
	import sys
	# Get number of list nodes from command line
	#error starts from 333 without sys.setrecursionlimit set to anything
	#The default recursionlimit or limit of stack is 1000
	#The error occurs when pickle.pyi reaches the maximum python call stack which is 1000 as said above

	n = 16666
	limit = 50000
	#Sets the maximum depth of the Python interpreter stack to the desired amount
	#Prevents infinite recursion
	#This solution works for above N limit on my windows machine, however I believe it is platform dependent
	#It could potentially crash on other machines, I don't have means to test it
	#Ideally, if our n limit increases, we could just increase setrecursionlimit() to higher value than current
	#However, there might be also be a limit on how much you can increase it	
	#This command could be useful: 'resource.setrlimit' to increase the stack size as well
	#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
	#There are probably different solutions to it
	#One could be making the base code less recursive to reduce usage of maximum python call stack

	sys.setrecursionlimit(limit)

	if len(sys.argv) > 1:
		n = int(sys.argv[1])

	# Create the list and pickle it
	l = create_long_list(n)
	with open('tmpfile', 'wb') as pf:
		pickle.dump(l, pf)
