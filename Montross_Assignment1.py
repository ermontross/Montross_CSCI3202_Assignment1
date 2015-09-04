#assignment #1
#due September 4
#Emma Montross

#queue class using a list
class Queue():
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0,item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

#stack class using a list
class Stack():
	def __init__(self):
		self.stack = []
		
	def isEmpty(self):
		return self.stack == []
		
	def push(self,value):
		self.stack.append(value)
		
	def pop(self):
		return self.stack.pop()
		
	def checkSize(self):
		return len(self.stack)

#node class to define the nodes for the Binary Tree
class Node():
	def __init__(self,key,parent):
		self.parent = parent
		self.key = key
		self.left = None
		self.right = None

#tree class to use with Binary tree (main purpose is to have a root)
class Tree():
	def __init__(self):
		self.root = None
	
	def setRoot(self,node):
		self.root = node
	
#Binary Tree class using nodes
class BinaryTree(Tree):
	
	def lookup(self,node,value):
		if value < node.key:
			if node.left == None:
				return None
			return self.lookup(node.left,value)
		elif value > node.key:
			if node.right == None:
				return None
			return self.lookup(node.right,value)
		else:
			return node
		
	def add(self,value,parentValue):
		if self.root == None:
			self.setRoot(Node(value,None))
			print("root = %d" % value)
		else:
			parent = self.lookup(self.root,parentValue)
			if parent == None:
				print("Parent not found")
			elif parent.left == None and value < parent.key:
				node = Node(value,parent)
				parent.left = node
				print("%d added" % node.key)
			elif parent.right == None and value > parent.key:
				node = Node(value,parent)
				parent.right = node
				print("%d added" % node.key)
			else:
				print("Parent has two children, node not added")
			
	def delete(self,value):
		node = self.lookup(self.root,value)
		if node == None:
			print("Node not found")
		elif node.left == None and node.right == None:
			if node.parent.left == node:
				node.parent.left = None
				print("%d deleted" % value)
			else:
				node.parent.right = None
				print("%d deleted" % value)
		else:
			print("Node not deleted, has children")
	
	def printTree1(self):
		print("TREE:")
		self.printTree(self.root)
	
	def printTree(self,node):
		if node.left:
			self.printTree(node.left)
		print node.key
		if node.right:
			self.printTree(node.right)

#vertex class to define graph vertices	
class Vertex():
	def __init__(self,key):
		self.key = key
		self.adj = []
		self.numAdj = 0

#graph class using lists of vertices
class Graph():
	def __init__(self):
		self.vertices = []
		self.numVertices = 0
		
	def addVertex(self,value):
		if value in self.vertices:
			print("Vertex already exits")
		else:
			self.numVertices = self.numVertices + 1
			vertex = Vertex(value)
			self.vertices.append(vertex)
			print("%d vertex added" % vertex.key)
			
	def printVertices(self):
		if self.vertices == None:
			print "empty"
		else:
			for i in range(0,self.numVertices):
				print self.vertices[i].key
	
	def addEdge(self,value1,value2):
		index1 = -1
		index2 = -1
		for i in range(0,self.numVertices):
			if self.vertices[i].key == value1:
				index1 = i
			elif self.vertices[i].key == value2:
				index2 = i
		if index1 != -1 and index2 != -1:
			self.vertices[index1].adj.append(value2)
			self.vertices[index1].numAdj = self.vertices[index1].numAdj + 1
			print("edge added between %d and %d" % (value1,value2))
			self.vertices[index2].adj.append(value1)
			self.vertices[index2].numAdj = self.vertices[index2].numAdj + 1
		else:
			print("One or more vertices not found")
			
	def findVertex(self,value):
		for i in range(0,self.numVertices):
			if self.vertices[i].key == value:
				print("adjacent vertices to %d: " % value)
				for j in range(0,self.vertices[i].numAdj):
					print("%d" % self.vertices[i].adj[j])
					
#---------------------------------------------------#	
#list to test queue and stack classes with
test = [1,2,3,4,5,6,7,8,9,10]

#TESTING QUEUE CLASS
print("TESTING QUEUE CLASS")
#instance of queue class
queue = Queue()
#loop for enqueuing all the values in the test array
for i in range(0,10):
	queue.enqueue(test[i])
	print("enqueued: %d" % test[i])
#loop for dequeuing the entire queue
for j in range(0,10):
	temp = queue.dequeue()
	print("dequeued: %d" % temp)
	
#TESTING STACK CLASS
print("\nTESTING STACK CLASS")
#instance of stack class
stack = Stack()
#loop for pushing all the values in the test array onto the stack
for i in range(0,10):
	stack.push(test[i])
	print("pushed: %d" % test[i])
#loop for popping all the values off the stack
for i in range(0,10):
	temp = stack.pop()
	print("popped: %d" % temp)

#TESTING BINARY TREE
print("\nTESTING BINARY TREE")
#instance of binary tree class
tree = BinaryTree()
#add nodes to the tree
tree.add(5,4)
tree.add(4,5)
tree.add(2,4)
tree.add(3,4)
tree.add(6,5)
tree.add(7,5)
tree.add(7,6)
tree.add(10,7)
tree.add(9,10)
tree.add(8,9)
tree.add(11,10)
tree.add(12,11)
tree.add(13,12)
#print the tree
tree.printTree1()
#deleting some nodes (some of these purposely will not get deleted)
tree.delete(0)
tree.delete(6)
tree.delete(1)
tree.delete(2)
tree.delete(13)
tree.delete(12)
tree.delete(11)
#print tree
tree.printTree1()

#TESTING GRAPH CLASS
print("\nTESTING GRAPH CLASS")
#instance of graph class
graph = Graph()
#loop adding vertices 1-10 to the graph
for i in range(0,10):
	graph.addVertex(test[i])
#loop adding 5 edges
for j in range(1,6):
	graph.addEdge(j,11-j)
#adding 15 other edges
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(4,5)
graph.addEdge(6,7)
graph.addEdge(8,9)
graph.addEdge(9,10)
graph.addEdge(1,3)
graph.addEdge(1,4)
graph.addEdge(1,5)
graph.addEdge(2,5)
graph.addEdge(3,7)
graph.addEdge(5,8)
graph.addEdge(6,3)
graph.addEdge(7,5)
graph.addEdge(8,10)
#finding vertices 1-5
for k in range(1,6):
	graph.findVertex(k)

	
